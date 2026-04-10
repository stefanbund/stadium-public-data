#!/usr/bin/env python3
import os
import json
import base64
from datetime import datetime
from pathlib import Path

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOCAL_STATUS_FILE = PROJECT_ROOT / "guardian_status.json"
REMOTE_STATUS_FILE = PROJECT_ROOT / "logs" / "remote_status.json"
OUTPUT_FILE = PROJECT_ROOT / "system_status_dashboard.html"

def generate_dashboard():
    # Load Local Status
    local_data = {}
    if LOCAL_STATUS_FILE.exists():
        with open(LOCAL_STATUS_FILE, "r") as f:
            local_data = json.load(f)
            
    # Load Remote Status
    remote_data = {}
    if REMOTE_STATUS_FILE.exists():
        with open(REMOTE_STATUS_FILE, "r") as f:
            remote_data = json.load(f)

    # Decode log tail if present
    remote_log_tail = ""
    if "log_tail" in remote_data:
        try:
            remote_log_tail = base64.b64decode(remote_data["log_tail"]).decode('utf-8')
        except:
            remote_log_tail = "Error decoding log."

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guardian System Status</title>
    <style>
        :root {{
            --bg: #0f172a;
            --card: #1e293b;
            --accent: #38bdf8;
            --green: #4ade80;
            --red: #f87171;
            --text: #f8fafc;
            --text-dim: #94a3b8;
        }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 1rem;
            font-size: 14px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }}
        .card {{
            background: var(--card);
            border: 1px solid #334155;
            border-radius: 0.75rem;
            padding: 1rem;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            border-bottom: 1px solid #334155;
            padding-bottom: 0.5rem;
        }}
        .title {{
            font-weight: 600;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .status {{
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 10px;
            font-weight: bold;
        }}
        .online {{ background: rgba(74, 222, 128, 0.2); color: var(--green); }}
        .offline {{ background: rgba(248, 113, 113, 0.2); color: var(--red); }}
        
        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.5rem;
            margin-bottom: 1rem;
        }}
        .metric-box {{
            text-align: center;
            background: rgba(15, 23, 42, 0.5);
            padding: 0.5rem;
            border-radius: 0.5rem;
        }}
        .metric-val {{ font-size: 1.25rem; font-weight: 600; color: var(--text); }}
        .metric-label {{ font-size: 10px; color: var(--text-dim); text-transform: uppercase; }}

        .service-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .service-item {{
            display: flex;
            justify-content: space-between;
            padding: 0.4rem 0;
            border-bottom: 1px solid #334155;
        }}
        .service-item:last-child {{ border: none; }}
        
        pre {{
            background: #000;
            padding: 0.75rem;
            border-radius: 0.5rem;
            font-size: 11px;
            color: var(--green);
            overflow-x: auto;
            max-height: 150px;
        }}
        .refresh {{ font-size: 10px; color: var(--text-dim); text-align: right; margin-top: 1rem; }}
    </style>
</head>
<body>
    <div class="grid">
        <!-- LOCAL HOST (M4 LAPTOP) -->
        <div class="card">
            <div class="header">
                <span class="title">Local Core (M4 Laptop)</span>
                <span class="status online">ONLINE</span>
            </div>
            <div class="metric-grid">
                <div class="metric-box">
                    <div class="metric-val">{local_data.get('system', {}).get('cpu_percent', 'N/A')}%</div>
                    <div class="metric-label">CPU</div>
                </div>
                <div class="metric-box">
                    <div class="metric-val">{local_data.get('system', {}).get('memory_percent', 'N/A')}%</div>
                    <div class="metric-label">RAM</div>
                </div>
                <div class="metric-box">
                    <div class="metric-val">{local_data.get('system', {}).get('memory_free_gb', 'N/A')}G</div>
                    <div class="metric-label">FREE</div>
                </div>
            </div>
            <div class="service-list">
                {"".join([f'<div class="service-item"><span>{s["name"]}</span><span style="color: {"var(--green)" if s["status"]=="RUNNING" else "var(--red)"}">{s["status"]}</span></div>' for s in local_data.get('services', [])])}
            </div>
        </div>

        <!-- REMOTE HOST (MAC MINI) -->
        <div class="card">
            <div class="header">
                <span class="title">Remote MLOps (Mac Mini)</span>
                <span class="status {"online" if remote_data.get('status')=="ONLINE" else "offline"}">{remote_data.get('status', 'UNKNOWN')}</span>
            </div>
            {f'''
            <div class="metric-grid">
                <div class="metric-box">
                    <div class="metric-val">{remote_data.get('cpu', 'N/A')}%</div>
                    <div class="metric-label">CPU Load</div>
                </div>
                <div class="metric-box">
                    <div class="metric-val">{remote_data.get('mem', 'N/A')}%</div>
                    <div class="metric-label">RAM Load</div>
                </div>
                <div class="metric-box">
                    <div class="metric-val" style="font-size: 10px;">{remote_data.get('uptime', 'N/A')}</div>
                    <div class="metric-label">Uptime</div>
                </div>
            </div>
            <span class="title" style="font-size: 10px;">Remote ML Log Tail:</span>
            <pre>{remote_log_tail or 'No log data available.'}</pre>
            ''' if remote_data.get('status') == "ONLINE" else f'<div style="text-align: center; padding: 2rem; color: var(--red);">Host unreachable: {remote_data.get("error", "Unknown error")}</div>'}
        </div>
    </div>
    <div class="refresh">Last heartbeat: {timestamp}</div>
</body>
</html>
    """

    with open(OUTPUT_FILE, "w") as f:
        f.write(html_content)
    print(f"✅ System Status Dashboard generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_dashboard()
