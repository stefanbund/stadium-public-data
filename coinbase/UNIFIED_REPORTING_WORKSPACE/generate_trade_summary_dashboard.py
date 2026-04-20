#!/usr/bin/env python3
import os
import json
import glob
import sys
from datetime import datetime
from pathlib import Path

# Setup project root for imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))
from shared_lib.github_pusher import push_to_github

def get_trade_data(log_dir):
    log_files = glob.glob(os.path.join(log_dir, "trading_bot.log*"))
    def sort_key(filename):
        if filename.endswith(".log"): return 0
        try: return int(filename.split(".")[-1])
        except ValueError: return 999
    log_files.sort(key=sort_key, reverse=True) # Oldest first

    all_decisions = []
    active_events = {} # symbol -> event object
    
    for log_file in log_files:
        if not os.path.isfile(log_file): continue
        try:
            with open(log_file, "r") as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        msg = data.get("message", "")
                        symbol = data.get("symbol")
                        if not symbol and msg.startswith("["):
                            end_idx = msg.find("]")
                            if end_idx != -1: symbol = msg[1:end_idx]
                        if not symbol: continue
                        timestamp = data.get("timestamp")
                        
                        if "Tier:" in msg:
                            tier = data.get("tier", "Unknown")
                            prob = data.get("probability", 0.0)
                            target = data.get("threshold", 0.0)
                            passed = data.get("passed", False)
                            
                            if tier == "Directional":
                                # New event
                                event = {
                                    "symbol": symbol,
                                    "timestamp": timestamp,
                                    "status": "FAIL" if not passed else "PENDING",
                                    "insight": f"Dir: {prob:.1%} vs {target:.1%}" if not passed else f"Dir: {prob:.1%}",
                                    "last_tier": tier,
                                    "prob": prob,
                                    "target": target
                                }
                                all_decisions.append(event)
                                active_events[symbol] = event
                            else:
                                if symbol in active_events:
                                    event = active_events[symbol]
                                    event["timestamp"] = timestamp
                                    if not passed:
                                        event["status"] = "FAIL"
                                        if "Crash" in tier:
                                            event["insight"] = f"CRASH! Prob {prob:.1%} > {target:.1%}"
                                        else:
                                            event["insight"] = f"{tier} Failed: {prob:.1%} < {target:.1%}"
                                    else:
                                        if event["insight"]: event["insight"] += " | "
                                        event["insight"] += f"{tier}: {prob:.1%}"
                                    event["last_tier"] = tier
                                    event["prob"] = prob
                                    event["target"] = target

                        if "FINAL DECISION: TRADE APPROVED" in msg:
                            if symbol in active_events:
                                active_events[symbol]["status"] = "PASS"
                                if "ALL TIERS PASSED" not in active_events[symbol]["insight"]:
                                    active_events[symbol]["insight"] = "ALL TIERS PASSED - " + active_events[symbol]["insight"]
                        elif "FINAL DECISION: TRADE REJECTED" in msg:
                            if symbol in active_events:
                                active_events[symbol]["status"] = "FAIL"
                    except: continue
        except: continue
    return all_decisions

def generate_html(decisions):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Sort decisions by timestamp descending
    decisions.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    
    # Limit to most recent 1000 decisions for performance
    display_decisions = decisions[:1000]
    
    # Calculate stats
    unique_symbols = len(set(d['symbol'] for d in decisions))
    total_passes = sum(1 for d in decisions if d['status'] == 'PASS')
    total_fails = sum(1 for d in decisions if d['status'] == 'FAIL')
    
    rows = ""
    for d in display_decisions:
        status_class = "status-" + d['status'].lower()
        # Clean timestamp for display (showing only month-day time)
        ts_display = d['timestamp'][5:19] if len(d['timestamp']) > 19 else d['timestamp']
        
        rows += f"""
        <tr>
            <td><span class="symbol-badge">{d['symbol']}</span></td>
            <td>{ts_display}</td>
            <td><span class="status-badge {status_class}">{d['status']}</span></td>
            <td class="insight-cell">{d['insight']}</td>
        </tr>
        """

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <title>Trading Decision Chronology</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --border: rgba(255, 255, 255, 0.1);
            --accent: #38bdf8;
            --success: #10b981;
            --fail: #ef4444;
            --pending: #f59e0b;
            --text: #f8fafc;
            --text-dim: #94a3b8;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: var(--bg);
            background-image: radial-gradient(circle at top right, #1e293b, transparent), radial-gradient(circle at bottom left, #0f172a, transparent);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            min-height: 100vh;
            padding: 2rem;
        }}

        h1, h2, h3 {{ font-family: 'Outfit', sans-serif; }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border);
        }}

        .title-group h1 {{ font-size: 2rem; color: var(--accent); letter-spacing: -0.02em; }}
        .title-group p {{ color: var(--text-dim); font-size: 0.9rem; }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}

        .stat-card {{
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border);
            padding: 1.5rem;
            border-radius: 1rem;
            text-align: center;
        }}

        .stat-card h3 {{ color: var(--text-dim); font-size: 0.8rem; text-transform: uppercase; margin-bottom: 0.5rem; }}
        .stat-card .value {{ font-size: 2rem; font-weight: 600; color: var(--text); font-family: 'Outfit'; }}

        .card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 1.25rem;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}

        th {{
            background: rgba(15, 23, 42, 0.5);
            padding: 1.25rem 1.5rem;
            color: var(--text-dim);
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        td {{
            padding: 1.25rem 1.5rem;
            border-bottom: 1px solid var(--border);
            font-size: 0.95rem;
            vertical-align: middle;
        }}

        tr:hover td {{
            background: rgba(255, 255, 255, 0.03);
            transition: background 0.3s ease;
        }}

        .symbol-badge {{
            font-family: 'Outfit';
            font-weight: 600;
            color: var(--accent);
            background: rgba(56, 189, 248, 0.1);
            padding: 0.4rem 0.8rem;
            border-radius: 0.5rem;
            border: 1px solid rgba(56, 189, 248, 0.2);
        }}

        .status-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 2rem;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }}

        .status-pass {{ background: rgba(16, 185, 129, 0.1); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.2); }}
        .status-fail {{ background: rgba(239, 68, 68, 0.1); color: var(--fail); border: 1px solid rgba(239, 68, 68, 0.2); }}
        .status-pending {{ background: rgba(245, 158, 11, 0.1); color: var(--pending); border: 1px solid rgba(245, 158, 11, 0.2); }}

        .insight-cell {{
            font-family: 'Inter', monospace;
            font-size: 0.85rem;
            color: var(--text-dim);
        }}

        footer {{
            margin-top: 2rem;
            text-align: center;
            color: var(--text-dim);
            font-size: 0.8rem;
        }}

        @media (max-width: 768px) {{
            body {{ padding: 1rem; }}
            header {{ flex-direction: column; align-items: flex-start; gap: 1rem; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="title-group">
                <h1>Trading Decision Chronology</h1>
                <p>Real-time sequence of hierarchical model inference outcomes, sorted by freshnes.</p>
                <div style="margin-top: 10px; display: flex; gap: 15px;">
                    <a href="index.html" style="color: var(--accent); text-decoration: none; font-size: 0.8rem; font-weight: 600;">← Master Hub</a>
                    <a href="resource_correlation.html" style="color: var(--pending); text-decoration: none; font-size: 0.8rem; font-weight: 600;">Correlated Events</a>
                </div>
            </div>
            <div class="timestamp">
                Last updated: {now}
            </div>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Decisions</h3>
                <div class="value">{len(decisions)}</div>
            </div>
            <div class="stat-card">
                <h3>Unique Symbols</h3>
                <div class="value">{unique_symbols}</div>
            </div>
            <div class="stat-card">
                <h3>Approvals (PASS)</h3>
                <div class="value" style="color: var(--success)">{total_passes}</div>
            </div>
            <div class="stat-card">
                <h3>Rejections (FAIL)</h3>
                <div class="value" style="color: var(--fail)">{total_fails}</div>
            </div>
        </div>

        <div class="card">
            <table>
                <thead>
                    <tr>
                        <th>Symbol</th>
                        <th>Decision Time</th>
                        <th>Status</th>
                        <th>Inference Insights</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>

        <footer>
            Generated by Antigravity AI Trading Pulse &copy; 2026
        </footer>
    </div>
</body>
</html>
    """
    return html

def main():
    log_dir = os.path.join(PROJECT_ROOT, "UNIFIED_TRADER_WORKSPACE", "logs")
    decisions = get_trade_data(log_dir)
    
    html_content = generate_html(decisions)
    
    output_path = os.path.join(PROJECT_ROOT, "trade_decision_summary.html")
    with open(output_path, "w") as f:
        f.write(html_content)
    
    print(f"✅ Chronological Dashboard generated locally at {output_path}")
    
    # Push to GitHub
    files_to_push = [
        {'local': 'trade_decision_summary.html', 'repo': 'trade_decision_summary.html'},
        {'local': str(Path(__file__).resolve()), 'repo': 'UNIFIED_REPORTING_WORKSPACE/generate_trade_summary_dashboard.py'}
    ]
    commit_msg = f"Update Trade Decision Chronology (Source & Report): {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    success = push_to_github(files_to_push, commit_msg)
    if success:
        print("🚀 Successfully uploaded chronological report.")
    else:
        print("❌ Failed to upload to GitHub.")

if __name__ == "__main__":
    main()
    
