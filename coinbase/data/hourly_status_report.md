# Hourly Status Report

Generated at: 2026-08-01 20:15:14 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=35.33 | Z-Score=-2.00 (Thresh <= 0.5) | RSI=14.8 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=50.57 | Z-Score=0.34 (Thresh <= 0.5) | RSI=27.6 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)

[2] Host Daemon Status (Mac Mini & Local)
--------------------------------------------------
🟢 Mac Mini PM2 [dvol-sync]:        Status=ONLINE | Restarts=21 | Uptime=108.2h
🟢 Mac Mini PM2 [vol-surface-sync]: Status=ONLINE | Restarts=0 | Uptime=12.6h

[3] Remote Trading Engine Processes (AWS EC2)
--------------------------------------------------
🟢 Watchdog (guardian_sfgk):  ACTIVE
🟢 L3 Order Book Feed:        ACTIVE
🟢 Active Traders:             5 asset loop(s) running
   Traders active on:          AVAX-USD, ETH-USD, DOGE-USD, BTC-USD, SOL-USD
• Recent EC2 Errors: ⚠️ Could not fetch errors.

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-01 23:09:07 to 2026-08-02 03:09:02
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 135913 (13591300.0%)
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
• Last Weekly VSTEF Run:      2026-07-24 10:35:39 AM UTC-07:00
• Next Scheduled VSTEF Run:  2026-08-02 07:00:00 PM UTC-07:00 (Monday 02:00 UTC)
• Time Until Next Optimizer:  22.8 hour(s) (0d 22h 50m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
• Scheduled (cron):       0 */8 * * *
• Last Rebuild Started:   2026-08-01T23:00:00.002Z
• EC2 DB Last Updated:    2026-08-01 04:00:18 PM PDT
• Rebuilt in last 8 hrs?: 🟢 (4.2 hours ago)
• Recent Mac Mini Errors:
    File "/Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/generate_timesfm_forecasts.py", line 6, in <module>
        import torch
      File "/Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/venv/lib/python3.9/site-packages/torch/__init__.py", line 416, in <module>
        from torch._C import *  # noqa: F403
    KeyboardInterrupt

[7] Day Trade Orchestrator (Mac Mini)
--------------------------------------------------
• Recent Day Trade Efforts & Logs:
    2026-07-27 07:55:00 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:07 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:12 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:17 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:22 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:27 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:32 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:37 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:44 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:49 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:54 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:55:59 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:56:04 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:56:09 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
    2026-07-27 07:56:14 [INFO] No valid actionable day trade recommendations found at this time. Sleeping...
================================================================================

```
