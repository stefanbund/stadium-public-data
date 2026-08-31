---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-31 03:52:58 PM PDT (2026-08-31 22:52:58 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+2.49** | **-0.50** | **+2.99** | **+3.41** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.41** | **-0.50** | **+0.91** | **+16.49** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+2.49** | **-0.50** | **+2.99** | **+3.59** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+2.49** | **-0.50** | **+2.99** | **+3.41** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+2.49** | **-0.50** | **+2.99** | **+2.77** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+2.49** | **-0.50** | **+2.99** | **+2.40** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+2.49** | **-0.50** | **+2.99** | **+2.77** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (3.15h old) | 08-31 12:43 |
| ✅ | **TimesFM Forecasts** | Fresh (3.01h old) | 08-31 12:52 |
| ❌ | **Holding Times config** | STALE! (246.8h old) | Limit 20.9h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-31 15:52 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-31 15:53 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-31 15:52 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1716 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `55,995` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 73 | 68.5% | 0 | 🟢 OK |
| `DOGE-USD` | 56 | 71.4% | 0 | 🟢 OK |
| `ETH-USD` | 25 | 68.0% | 0 | 🟢 OK |
| `LINK-USD` | 62 | 74.2% | 1 | 🟢 OK |
| `AVAX-USD` | 50 | 74.0% | 0 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USD` | SELL | 0.99971 | `12f82322-ff5f-4c79-bbcc-b04ceb1fdc0c` |
| `LINK-USD` | SELL | 11.404 | `886d3b7d-9fa9-4d3e-bc14-f96aeb92b866` |
| `DOGE-USD` | SELL | 0.08339 | `3cb4219d-b8a8-4738-8e10-19a43aabaf0d` |
| `AVAX-USD` | SELL | 7.245 | `b8ce285c-6b87-4b7e-8424-373c5bea8f80` |
| `ADA-USD` | SELL | 0.19966 | `03cd09ff-42ee-4fac-ae12-42de2b1a5d3d` |
| `USDT-USD` | SELL | 0.99971 | `0f7382b6-3e16-4993-80e2-3e779f53b9db` |
| `ETH-USD` | BUY | 2465.11 | `65c7defc-7db8-4a07-a814-b2f4149148e1` |
| `USDT-USD` | SELL | 0.9997 | `b84fcbf6-77a1-4645-9a93-e898ae6dad57` |
| `USDT-USD` | SELL | 0.9997 | `3e3f1d13-3bdf-4a10-8a66-9f41c7c780e7` |
| `USDT-USD` | SELL | 0.9997 | `4c787e3f-7495-48a5-945f-943e9345aca9` |
| `USDT-USD` | SELL | 0.9997 | `302b364b-450d-4b23-a98b-9ac7c07dc1dd` |
| `USDT-USD` | SELL | 0.9997 | `64a1991d-b50d-4b70-983a-3c0c1398f1d8` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.0h ago (2026-08-31 12:52 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **147.1h (6d 3h 6m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 12:43:56 PM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **146.1h (6d 2h 6m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  10:52:57 PM
   CPU:  10.9%  |  MEM:   8.3% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2588629  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2588746  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 2588748  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2593945  | RUNNING         | 13       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2645648  | RUNNING         | 123      | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2604166  | RUNNING         | 35       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2593948  | RUNNING         | 13       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2646884  | COOL-DOWN       | 155      | Next run in 14.8s
Trader LINK-USD      | 2588757  | RUNNING         | 0        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-31 17:34:44 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 17:37:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 17:40:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: limit_order_gtc_buy | Sleeping 1.46s... | Error: 429 Client Error: Too Many Request
logs/watchdog_Trader_SOL_USD.log:2026-08-31 17:52:49 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:40:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:57:28 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:57:51 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:58:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:58:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:58:57 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:59:19 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 19:59:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 20:00:03 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.37s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 20:00:24 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 20:05:28 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 20:23:57 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 20:34:01 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 20:59:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:01:14 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.37s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:14:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:25:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:28:10 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:31:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.41s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:49:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:53:04 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.30s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:55:58 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:57:29 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.28s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:57:51 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:58:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.47s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:58:57 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.32s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:59:19 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 21:59:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:00:03 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:00:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:00:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:01:09 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:01:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:01:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:02:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 22:47:12 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.41s... | Error: 429 Client Error: Too Many Requests
```
</details>

