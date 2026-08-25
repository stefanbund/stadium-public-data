---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-25 03:50:07 PM PDT (2026-08-25 22:50:07 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.22** | **-0.50** | **+0.72** | **-4.14** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.08** | **-0.50** | **+0.58** | **+10.85** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.22** | **-0.50** | **+0.72** | **-4.14** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.22** | **-0.50** | **+0.72** | **-4.14** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.22** | **-0.50** | **+0.72** | **-4.14** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.22** | **-0.50** | **+0.72** | **-4.14** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.22** | **-0.50** | **+0.72** | **-4.14** | 5.0 | 🔴 DAW VETOED |



### 📖 Volatility & VRP Safety Barometer
The system's Layer 1 DAW Causal Gate continuously gauges execution safety using **Deribit DVOL Z-Score ($Z$)** and **Variance Risk Premium (VRP)**:
- **Mathematical Principle**: $\text{VRP} = \text{IV}_{\text{Deribit DVOL}} - \text{RV}_{\text{Realized Vol}}$ and $Z = \frac{\text{DVOL}_t - \mu_{\text{4h}}}{\sigma_{\text{4h}}}$.
- **Regime Safety Spectrum**:
  - 🟢 **Safe / Compression ($Z \le Z_{opt}$)**: Derivatives market prices low tail risk. Order books are deep, adverse selection is minimal, and TimesFM zero-shot scalps operate at peak win rates.
  - 🔴 **Hostile / Expansion ($Z > Z_{opt}$)**: Options pricing aggressive shock risk. Taker order sweeps cause adverse selection; **DAW Causality Veto is active** to preserve capital.
---
## 2. 🔒 MLOps & Trading Telemetry Provenance & Utilization Certification: 🔴 CRITICAL SYNC/UTILIZATION FAILURE
We hereby certify that the mission-critical algorithmic data assets uploaded by the Mac Mini MLOps node have been audited for freshness, fall within their strict operational due dates, and are actively being utilized by the live EC2 HFT Trader.

| Status | Data Asset | Freshness / State | Details / Timestamp |
| :---: | :--- | :--- | :--- |
| ✅ | **Go-List JSON** | Fresh (6.80h old) | 08-25 09:02 |
| ✅ | **TimesFM Forecasts** | Fresh (2.99h old) | 08-25 12:50 |
| ❌ | **Holding Times config** | STALE! (102.8h old) | Limit 44.8h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-25 15:50 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-25 15:50 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-25 15:50 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1697 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `2,533` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 1 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `ETH-USD` | SELL | 2503.11 | `b8603d38-2b4a-481a-803a-19ecf1beb593` |
| `SOL-USD` | SELL | 100.69 | `8dcd9986-8156-403f-81ee-b1dc96d2b3c7` |
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `ADA-USD` | SELL | 0.22031 | `d968b8ef-1180-4f05-bc11-01087aa5d99a` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `ADA-USD` | SELL | 0.22503 | `eb72afdd-a3d7-40b8-9598-30b5ca2b74ef` |
| `DOGE-USD` | SELL | 0.09237 | `3160f212-8ff6-4b19-a291-73c17cdf2a97` |
| `AVAX-USD` | SELL | 7.625 | `c14c3c5a-f35f-4043-a616-ea4c20cfa9f2` |
| `BTC-USD` | SELL | 79882.66 | `560ee9a9-d0c6-4242-b2d2-c0d7ddc7393f` |
| `DOGE-USD` | SELL | 0.09132 | `2f2ed9b7-454b-4377-9672-5f4c78c84b1e` |
| `AVAX-USD` | SELL | 7.558 | `fc9234ee-6ef0-4ba3-a44b-d86922f91144` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.0h ago (2026-08-25 12:50 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **123.2h (5d 3h 9m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-25 09:02:14 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **122.2h (5d 2h 9m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  10:50:05 PM
   CPU:  13.4%  |  MEM:   6.1% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3834078  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3834154  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 3834156  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3887142  | RUNNING         | 175      | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3887143  | RUNNING         | 177      | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3886848  | COOL-DOWN       | 173      | Next run in 4.5s
Trader DOGE-USD      | 3887144  | RUNNING         | 174      | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3887145  | RUNNING         | 177      | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3886849  | COOL-DOWN       | 174      | Next run in 4.5s
```

---
## 6. ☀️ Mac Mini Day Trader Intelligence & PnL
**Guardian Watchdog Status**: 🟢 ONLINE

### 💰 Cumulative PnL Dashboards
| Environment | Total Trades | Win Rate | Net PnL (USD) |
| :--- | :--- | :--- | :--- |
| **LIVE EC2** | 0 | N/A | **$+0.00** |
| **SHADOW (Paper)** | 0 | N/A | **$+0.00** |

---
## 7. ⚠️ Actionable Error & Incident Radar (Last 10h)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:38 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:08:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:09:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:00 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:10:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-25 21:11:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_AVAX_USD.log:2026-08-25 18:36:43 [WARNING] [async_sfgk_trader.py:_safe_requests_get:261] [AVAX-USD] requests.get Exception (Attempt 1/5). Sleeping 1.40s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443):
logs/watchdog_Trader_BTC_USD.log:2026-08-25 20:08:21 [WARNING] [async_sfgk_trader.py:_safe_requests_get:261] [BTC-USD] requests.get Exception (Attempt 1/5). Sleeping 1.33s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
logs/watchdog_Trader_DOGE_USD.log:2026-08-25 20:08:29 [WARNING] [async_sfgk_trader.py:_safe_requests_get:261] [DOGE-USD] requests.get Exception (Attempt 1/5). Sleeping 1.25s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443):
logs/watchdog_Trader_LINK_USD.log:2026-08-25 16:44:16 [WARNING] [async_sfgk_trader.py:_safe_requests_get:261] [LINK-USD] requests.get Exception (Attempt 1/5). Sleeping 1.34s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443):
logs/watchdog_Trader_SOL_USD.log:2026-08-25 20:08:31 [WARNING] [async_sfgk_trader.py:_safe_requests_get:261] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.34s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
```
</details>

