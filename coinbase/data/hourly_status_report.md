# Hourly Status Report

Generated at: 2026-08-05 11:00:14 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=34.12 | Z-Score=-1.46 (Thresh <= 0.5) | RSI=21.0 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=47.81 | Z-Score=-1.81 (Thresh <= 0.5) | RSI=75.5 | Exhaustion=40/100
  Volatility Trend: UPWARD (Expansion)
  Safety Status:    🔴 REJECTED_TOO_RISKY (Vetoed by DAW)
  Veto Rationale:   High Volatility Toxicity (Exhaustion=40 >= 30)

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
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:36:00,809 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:Warning: Failed to load local key file at /opt/hft_trader/traditional-cdp_api_key .json: [Errno 2] No such file or directory: '/opt/hft_trader/traditional-cdp_api_key .json'
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:36:35,903 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:Warning: Failed to load local key file at /opt/hft_trader/traditional-cdp_api_key .json: [Errno 2] No such file or directory: '/opt/hft_trader/traditional-cdp_api_key .json'
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:37:11,198 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-05 17:37:46 to 2026-08-05 17:59:57
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 121552 (12155200.0%)
  - Layer 2.5: Neural Network Low Trend Conviction    :    0 (0.0%)
  - Layer 5: Hawkes Microstructure Toxicity Gating    :    0 (0.0%)
  - Layer 4: SFGK Execution Horizon Gate              :  605 (60500.0%)
  - unknown_veto                                      :    0 (0.0%)
  - timesfm_gating                                    :    0 (0.0%)
  - sdr_liquidity_gate                                :    0 (0.0%)

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
• Time Until Next Optimizer:  104.0 hour(s) (4d 7h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-05 08:38:42 AM PDT
• Rebuilt in last 8 hrs?: 🟢 (2.4 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
