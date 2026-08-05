# Hourly Status Report

Generated at: 2026-08-04 20:00:07 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=34.22 | Z-Score=0.12 (Thresh <= 0.5) | RSI=71.9 | Exhaustion=40/100
  Volatility Trend: UPWARD (Expansion)
  Safety Status:    🔴 REJECTED_TOO_RISKY (Vetoed by DAW)
  Veto Rationale:   High Volatility Toxicity (Exhaustion=40 >= 30)
• DVOL ETH: Close=47.95 | Z-Score=-0.72 (Thresh <= 0.5) | RSI=38.2 | Exhaustion=20/100
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
🟢 Active Traders:             6 asset loop(s) running
   Traders active on:          DOT-USD, ETH-USD, ADA-USD, DOGE-USD, BTC-USD, SOL-USD
• Recent EC2 Errors:
    logs/watchdog_Trader_BTC_USD.log:2026-08-03 22:27:27 - coinbase.RESTClient - ERROR - HTTP Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8
    logs/watchdog_Trader_BTC_USD.log:2026-08-03 22:27:27,228 - ERROR - HTTP Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8
    logs/watchdog_Trader_BTC_USD.log:2026-08-03 22:27:27,228 - WARNING - [BTC-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.45s... | Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-04 23:00:08 to 2026-08-05 02:59:43
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 131366 (13136600.0%)
  - Layer 2.5: Neural Network Low Trend Conviction    :    0 (0.0%)
  - Layer 5: Hawkes Microstructure Toxicity Gating    :    0 (0.0%)
  - Layer 4: SFGK Execution Horizon Gate              : 4542 (454200.0%)
  - timesfm_gating                                    : 3952 (395200.0%)
  - sdr_liquidity_gate                                :    0 (0.0%)

• Asset Performance & Drift Status:
  Asset        | Trades   | Win Rate   | Loss Streak 
  --------------------------------------------------
  ADA-USD      | 532      |    100.0% | 0            🟢 OK
  AVAX-USD     | 532      |    100.0% | 0            🟢 OK
  LINK-USD     | 532      |    100.0% | 0            🟢 OK
  SOL-USD      | 458      |     99.1% | 2            🟢 OK
  LTC-USD      | 4        |     75.0% | 1            🟢 OK

[5] VSTEF Optimizer & Parameter Schedule
--------------------------------------------------
• Last Weekly VSTEF Run:      Never
• Next Scheduled VSTEF Run:  2026-08-09 07:00:00 PM UTC-07:00 (Monday 02:00 UTC)
• Time Until Next Optimizer:  119.0 hour(s) (4d 22h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-04 04:00:19 PM PDT
• Rebuilt in last 8 hrs?: 🟢 (4.0 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
