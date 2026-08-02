# Hourly Status Report

Generated at: 2026-08-02 12:00:08 

```text
================================================================================
                 UNIFIED TRADING SYSTEM STATUS & DECISION REPORT                 
================================================================================

[1] DVOL Market Regime & Safety Assessment
--------------------------------------------------
• DVOL BTC: Close=34.89 | Z-Score=-2.54 (Thresh <= 0.5) | RSI=32.5 | Exhaustion=20/100
  Volatility Trend: DOWNWARD (Compression)
  Safety Status:    🟢 BORING_AND_SAFE (Trading Approved)
• DVOL ETH: Close=49.85 | Z-Score=-3.64 (Thresh <= 0.5) | RSI=45.8 | Exhaustion=20/100
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
    logs/watchdog_Trader_SOL_USD.log:2026-07-28 23:50:22,693 - ERROR - HTTP Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8
    logs/watchdog_Trader_SOL_USD.log:2026-07-28 23:50:22,693 - WARNING - [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.21s... | Error: 503 Server Error: Service Unavailable go/sg/ef39e44f-b3f6-48e6-b767-772e408986f8
    logs/watchdog_Trader_SOL_USD.log:2026-07-29 00:43:39,159 - ERROR - Error fetching candles for BTC-USD: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): Read timed out. (read timeout=10)
    logs/watchdog_Trader_SOL_USD.log:2026-07-30 03:06:44,049 - ERROR - Error fetching candles for SOL-USD: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): Read timed out. (read timeout=10)
    logs/watchdog_Trader_SOL_USD.log:2026-07-31 23:26:42,119 - WARNING - [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.45s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): Read timed out. (read timeout=10)

[4] 5-Layer Funnel Decision Audit & Performance Summary
--------------------------------------------------
• Report Window (Recent Decisions): 2026-08-02 18:36:07 to 2026-08-02 19:00:00
• Cumulative Performance Metrics  : Total Trades=0 | System Win Rate=0.00% (Cumulative since daemon launch)
• Decision Funnel:    Evaluated=0 | Approved=0 | Rejected=0
• Rejection Reasons Breakdown:
  - Layer 1: DAW Causal Volatility Veto               : 121587 (12158700.0%)
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
• Next Scheduled VSTEF Run:  2026-08-02 07:00:00 PM UTC-07:00 (Monday 02:00 UTC)
• Time Until Next Optimizer:  7.0 hour(s) (0d 6h 59m)

[6] TimesFM Database & Mac Mini Host Check
--------------------------------------------------
⚠️ Could not fetch PM2 info for 'timesfm-recreate' on Mac Mini.
• EC2 DB Last Updated:    2026-08-02 08:00:18 AM PDT
• Rebuilt in last 8 hrs?: 🟢 (4.0 hours ago)
• Recent Mac Mini Errors: None or could not read log.
================================================================================

```
