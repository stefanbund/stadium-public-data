# Hourly Status Report

Generated at: 2026-08-02 22:00:09 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=35.59 | Z-Score=2.67 (Thresh <= 0.5) | RSI=86.2 | Exhaustion=80/100
  Volatility Trend: UPWARD (Expansion)
  Safety Status:    🔴 REJECTED_TOO_RISKY (Vetoed by DAW)
  Veto Rationale:   Volatility Expansion (Z-Score=2.67 > 0.5), High Volatility Toxicity (Exhaustion=80 >= 30)
• DVOL ETH: Close=50.30 | Z-Score=0.65 (Thresh <= 0.5) | RSI=83.6 | Exhaustion=60/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🔴 REJECTED_TOO_RISKY (Vetoed by DAW)
  Veto Rationale:   Volatility Expansion (Z-Score=0.65 > 0.5), High Volatility Toxicity (Exhaustion=60 >= 30)

[2] Host Daemon Status (Mac Mini & Local)
--------------------------------------------------
⚠️ Unable to query Mac Mini PM2 daemon: Permission denied, please try again.
Received disconnect from ::1 port 22:2: Too many authentication failures
Disconnected from ::1 port 22


[3] Remote Trading Engine Processes (AWS EC2)
--------------------------------------------------
🟢 Watchdog (guardian_sfgk):  ACTIVE
🟢 L3 Order Book Feed:        ACTIVE
🟢 Active Traders:             2 asset loop(s) running
   Traders active on:          ADA-USD, LTC-USD
• Recent EC2 Errors: None

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-03 01:00:24 to 2026-08-03 05:00:02
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 123671 (12367100.0%)
  - Layer 2.5: Neural Network Low Trend Conviction    :    0 (0.0%)
  - Layer 5: Hawkes Microstructure Toxicity Gating    :    0 (0.0%)
  - Layer 4: SFGK Execution Horizon Gate              :  605 (60500.0%)
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
• Time Until Next Optimizer:  165.0 hour(s) (6d 20h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-02 04:00:18 PM PDT
• Rebuilt in last 8 hrs?: 🟢 (6.0 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
