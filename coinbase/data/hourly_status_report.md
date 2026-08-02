# Hourly Status Report

Generated at: 2026-08-01 21:04:57 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=35.18 | Z-Score=-3.05 (Thresh <= 0.5) | RSI=33.3 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=50.41 | Z-Score=-0.14 (Thresh <= 0.5) | RSI=31.2 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)

[2] Host Daemon Status (Mac Mini & Local)
--------------------------------------------------
🟢 Mac Mini PM2 [dvol-sync]:        Status=ONLINE | Restarts=21 | Uptime=109.2h
🟢 Mac Mini PM2 [vol-surface-sync]: Status=ONLINE | Restarts=0 | Uptime=13.6h

[3] Remote Trading Engine Processes (AWS EC2)
--------------------------------------------------
🟢 Watchdog (guardian_sfgk):  ACTIVE
🟢 L3 Order Book Feed:        ACTIVE
🟢 Active Traders:             2 asset loop(s) running
   Traders active on:          ADA-USD, LINK-USD
• Recent EC2 Errors:
    logs/watchdog_Trader_SOL_USD.log:2026-07-28 23:50:22,693 - ERROR - HTTP Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8
    logs/watchdog_Trader_SOL_USD.log:2026-07-28 23:50:22,693 - WARNING - [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.21s... | Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8
    logs/watchdog_Trader_SOL_USD.log:2026-07-29 00:43:39,159 - ERROR - Error fetching candles for BTC-USD: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): Read timed out. (read timeout=10)
    logs/watchdog_Trader_SOL_USD.log:2026-07-30 03:06:44,049 - ERROR - Error fetching candles for SOL-USD: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): Read timed out. (read timeout=10)
    logs/watchdog_Trader_SOL_USD.log:2026-07-31 23:26:42,119 - WARNING - [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.45s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): Read timed out. (read timeout=10)

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-02 00:05:01 to 2026-08-02 04:04:42
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 137017 (13701700.0%)
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
• Time Until Next Optimizer:  21.9 hour(s) (0d 21h 55m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
• Scheduled (cron):       0 */8 * * *
• Last Rebuild Started:   2026-08-01T23:00:00.002Z
• EC2 DB Last Updated:    2026-08-01 04:00:18 PM PDT
• Rebuilt in last 8 hrs?: 🟢 (5.1 hours ago)
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
