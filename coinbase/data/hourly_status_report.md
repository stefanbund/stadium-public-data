# Hourly Status Report

Generated at: 2026-08-03 12:00:09 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=34.85 | Z-Score=-1.76 (Thresh <= 0.5) | RSI=47.1 | Exhaustion=0/100
  Volatility Trend: UPWARD (Expansion)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=49.42 | Z-Score=-1.95 (Thresh <= 0.5) | RSI=46.0 | Exhaustion=0/100
  Volatility Trend: UPWARD (Expansion)
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
• Recent EC2 Errors: None

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-03 15:00:14 to 2026-08-03 18:59:52
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 126831 (12683100.0%)
  - Layer 2.5: Neural Network Low Trend Conviction    :    0 (0.0%)
  - Layer 5: Hawkes Microstructure Toxicity Gating    :    0 (0.0%)
  - Layer 4: SFGK Execution Horizon Gate              : 1524 (152400.0%)
  - timesfm_gating                                    :  783 (78300.0%)
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
• Time Until Next Optimizer:  151.0 hour(s) (6d 6h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-03 08:00:18 AM PDT
• Rebuilt in last 8 hrs?: 🟢 (4.0 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
