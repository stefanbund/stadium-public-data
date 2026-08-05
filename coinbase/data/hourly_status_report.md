# Hourly Status Report

Generated at: 2026-08-05 10:00:13 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=34.32 | Z-Score=-0.34 (Thresh <= 0.5) | RSI=49.3 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=47.70 | Z-Score=-2.66 (Thresh <= 0.5) | RSI=26.7 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)

[2] Host Daemon Status (Mac Mini & Local)
--------------------------------------------------
⚠️ Unable to query Mac Mini PM2 daemon: Permission denied, please try again.
Received disconnect from ::1 port 22:2: Too many authentication failures
Disconnected from ::1 port 22


[3] Remote Trading Engine Processes (AWS EC2)
--------------------------------------------------
🟢 Watchdog (guardian_sfgk):  ACTIVE
🟢 L3 Order Book Feed:        ACTIVE
🟢 Active Traders:             0 asset loop(s) running
• Recent EC2 Errors:
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 16:58:28,221 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:Warning: Failed to load local key file at /opt/hft_trader/traditional-cdp_api_key .json: [Errno 2] No such file or directory: '/opt/hft_trader/traditional-cdp_api_key .json'
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 16:59:03,330 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:Warning: Failed to load local key file at /opt/hft_trader/traditional-cdp_api_key .json: [Errno 2] No such file or directory: '/opt/hft_trader/traditional-cdp_api_key .json'
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 16:59:38,499 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 121083 (12108300.0%)
  - Layer 2.5: Neural Network Low Trend Conviction    :    0 (0.0%)
  - Layer 5: Hawkes Microstructure Toxicity Gating    :    0 (0.0%)
  - Layer 4: SFGK Execution Horizon Gate              :  605 (60500.0%)

• Asset Performance & Drift Status:
  Asset        | Trades   | Win Rate   | Loss Streak 
  --------------------------------------------------
  ADA-USD      | 532      |    100.0% | 0            🟢 OK
  AVAX-USD     | 532      |    100.0% | 0            🟢 OK
  LINK-USD     | 532      |    100.0% | 0            🟢 OK
  SOL-USD      | 458      |     99.1% | 2            🟢 OK

[5] VSTEF Optimizer & Parameter Schedule
--------------------------------------------------
• Last Weekly VSTEF Run:      Never
• Next Scheduled VSTEF Run:  2026-08-09 07:00:00 PM UTC-07:00 (Monday 02:00 UTC)
• Time Until Next Optimizer:  105.0 hour(s) (4d 8h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-05 08:38:42 AM PDT
• Rebuilt in last 8 hrs?: 🟢 (1.4 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
