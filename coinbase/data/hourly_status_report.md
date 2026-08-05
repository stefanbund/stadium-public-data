# Hourly Status Report

Generated at: 2026-08-05 10:42:46 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=34.19 | Z-Score=-1.07 (Thresh <= -0.5) | RSI=23.0 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=47.69 | Z-Score=-2.64 (Thresh <= -0.5) | RSI=34.5 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)

[2] Host Daemon Status (Mac Mini & Local)
--------------------------------------------------
⚠️ Unable to query Mac Mini PM2 daemon: /bin/sh: pm2: command not found


[3] Remote Trading Engine & Guardian Watchdog (AWS EC2)
--------------------------------------------------
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:42:41 PM
   CPU:   1.5%  |  MEM:   6.1% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 457105   | [92mRUNNING        [0m | -        | Continuous Websocket Feed
Trader DOT-USD       | 474845   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
Trader ETH-USD       | 474846   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
Trader ADA-USD       | 474847   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
Trader DOGE-USD      | 474848   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
Trader BTC-USD       | 474849   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
Trader LTC-USD       | 474850   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
Trader SOL-USD       | 474851   | [93mCOOL-DOWN      [0m | 113      | Next run in 5.0s
================================================================================

• Recent EC2 Errors:
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:34:50,446 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:35:25,742 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:36:00,809 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:36:35,903 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
    logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:37:11,198 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-05 17:37:46 to 2026-08-05 17:42:28
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 121188 (99.5%)
  - Layer 2.5: TimesFM Forecast Gate                  :    0 (0.0%)
  - Layer 3: SDR Liquidity Filter                     :    0 (0.0%)
  - Layer 4: SFGK Execution Horizon Gate              :  605 (0.5%)
  - Layer 5: Hawkes Microstructure Toxicity Gating    :    0 (0.0%)
  - System: Unclassified Engine Veto                  :    0 (0.0%)

• Asset Performance & Drift Status:
  Asset        | Trades   | Win Rate   | Loss Streak 
  --------------------------------------------------
  ADA-USD      | 532      |    100.0% | 0            🟢 OK
  AVAX-USD     | 532      |    100.0% | 0            🟢 OK
  LINK-USD     | 532      |    100.0% | 0            🟢 OK
  SOL-USD      | 458      |     99.1% | 2            🟢 OK

[5] VSTEF Optimizer & Parameter Schedule
--------------------------------------------------
• Last Weekly VSTEF Run:      2026-08-05 09:22:38 AM UTC-07:00
• Next Scheduled VSTEF Run:  2026-08-09 07:00:00 PM UTC-07:00 (Monday 02:00 UTC)
• Time Until Next Optimizer:  104.3 hour(s) (4d 8h 17m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-05 08:38:42 AM PDT
• Rebuilt in last 8 hrs?: 🟢 (2.1 hours ago)
• Recent Mac Mini Errors: None or could not read log.

[7] Day Trade Orchestrator (Mac Mini)
--------------------------------------------------
• No recent trade attempts or logs found (orchestrator may be idle).
================================================================================

```
