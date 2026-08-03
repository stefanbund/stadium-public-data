# Hourly Status Report

Generated at: 2026-08-02 19:00:10 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=35.11 | Z-Score=-0.24 (Thresh <= 0.5) | RSI=41.9 | Exhaustion=0/100
  Volatility Trend: UPWARD (Expansion)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=50.25 | Z-Score=0.36 (Thresh <= 0.5) | RSI=62.2 | Exhaustion=0/100
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
(Note: Using local/synced status snapshot)
• Cumulative Performance Metrics  : Total Trades=89 | System Win Rate=74.16% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=200 | Approved=18 | Rejected=182
• Rejection Reasons Breakdown:
  - Layer 2.5: Neural Network Low Trend Conviction    :  165 (90.7%)
  - Layer 1: DAW Causal Volatility Veto               :   17 (9.3%)
  - System: Asset Cooldown Active                     :    0 (0.0%)
  - System: Asset Blacklist Gate                      :    0 (0.0%)

• Asset Performance & Drift Status:
  Asset        | Trades   | Win Rate   | Loss Streak 
  --------------------------------------------------
  DOGE-USD     | 2        |    100.0% | 0            🟢 OK
  CHZ-USD      | 15       |     80.0% | 1            🟢 OK
  CRV-USD      | 16       |     90.0% | 0            🟢 OK
  CRO-USD      | 5        |    100.0% | 0            🟢 OK
  ACH-USD      | 4        |     75.0% | 1            🟢 OK
  ALGO-USD     | 19       |     40.0% | 1            ⚠️ DRIFT
  BCH-USD      | 4        |    100.0% | 0            🟢 OK
  CBETH-USD    | 5        |     60.0% | 2            🟢 OK
  BNT-USD      | 12       |     50.0% | 0            🟢 OK
  GNO-USD      | 7        |     57.1% | 0            🟢 OK

🚨 System Telemetry Alerts:
  - Drift alert for ALGO-USD: Win rate is 40.0% (< 70.0%) over last 10 trades.
  - Drift alert for CBETH-USD: Win rate is 60.0% (< 70.0%) over last 5 trades.
  - Drift alert for BNT-USD: Win rate is 50.0% (< 70.0%) over last 10 trades.
  - Drift alert for GNO-USD: Win rate is 57.1% (< 70.0%) over last 7 trades.

[5] VSTEF Optimizer & Parameter Schedule
--------------------------------------------------
• Last Weekly VSTEF Run:      Never
• Next Scheduled VSTEF Run:  2026-08-09 07:00:00 PM UTC-07:00 (Monday 02:00 UTC)
• Time Until Next Optimizer:  168.0 hour(s) (6d 23h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-02 04:00:18 PM PDT
• Rebuilt in last 8 hrs?: 🟢 (3.0 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
