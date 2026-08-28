---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-28 11:22:10 AM PDT (2026-08-28 18:22:10 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.24** | **-0.50** | **-0.74** | **-1.45** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.81** | **-0.50** | **-1.31** | **+10.88** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.24** | **-0.50** | **-0.74** | **-2.07** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-1.24** | **-0.50** | **-0.74** | **-1.41** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-1.24** | **-0.50** | **-0.74** | **-1.95** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-1.24** | **-0.50** | **-0.74** | **-2.43** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-1.24** | **-0.50** | **-0.74** | **-2.07** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (2.50h old) | 08-28 08:52 |
| ✅ | **TimesFM Forecasts** | Fresh (3.31h old) | 08-28 08:03 |
| ❌ | **Holding Times config** | STALE! (170.3h old) | Limit 112.4h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-28 11:22 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-28 11:21 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-28 11:22 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 884 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `19,454` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 5 | 60.0% | 0 | 🟢 OK |
| `ADA-USD` | 37 | 67.6% | 1 | 🟢 OK |
| `DOGE-USD` | 23 | 56.5% | 1 | 🟢 OK |
| `ETH-USD` | 13 | 76.9% | 0 | 🟢 OK |
| `LINK-USD` | 26 | 69.2% | 0 | 🟢 OK |
| `AVAX-USD` | 20 | 55.0% | 1 | 🟢 OK |
| `SOL-USD` | 7 | 71.4% | 1 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USDC` | SELL | 1.0001 | `4d9f1df5-f1ce-408b-8fcb-f870df3e47db` |
| `SOL-USD` | SELL | 105.06 | `a1d47425-278f-48b2-b43e-96c976f2575b` |
| `LINK-USD` | SELL | 11.531 | `e808da2b-1baf-4b74-9a92-9aa8d9ee6749` |
| `USDT-USDC` | BUY | 0.9999 | `68931935-20e1-42fc-8903-80309be420eb` |
| `BTC-USD` | SELL | 78026.62 | `31b2708d-79fd-4a42-bf4c-bb993a1dde68` |
| `ADA-USD` | SELL | 0.20391 | `0141a18e-ef35-435a-87bd-1f0fe24b1f37` |
| `USDT-USDC` | SELL | 1.0001 | `5fa15d4a-6b18-45bf-9b63-87c4abf65231` |
| `AVAX-USD` | SELL | 7.278 | `e8be5e00-48db-47d5-a2f3-57fda53bab2a` |
| `DOGE-USD` | SELL | 0.08506 | `cfa4bf53-570e-40b9-8dad-5142f7b07a7e` |
| `USDT-USDC` | SELL | 1.0001 | `c6df0641-6530-4045-8576-80625cc069b0` |
| `USDT-USDC` | SELL | 1.0001 | `66cab2eb-254c-4f1b-b5b6-1251e98e9290` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.3h ago (2026-08-28 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **55.6h (2d 7h 37m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-28 08:52:07 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **54.6h (2d 6h 37m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:22:09 PM
   CPU:   7.7%  |  MEM:   8.6% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3040732  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3040760  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 3040762  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3057845  | RUNNING         | 9        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3062753  | COOL-DOWN       | 78       | Next run in 14.6s
Trader ADA-USD       | 3040765  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3059612  | RUNNING         | 10       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3040767  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3040768  | RUNNING         | 0        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:38 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:54 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:51:59 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:52:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:52:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 01:52:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-28 07:28:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-28 07:28:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-28 07:44:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-28 07:45:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product_book | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1001] [LINK-USD] Failed to post sell limit order after maximum repricing attempts. Proceeding to immediate liquidation.
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:14 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: cancel_orders | Sleeping 1.19s... | Error: 400 Client Error: Bad Request {"error":"
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:15 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 2/5). Func: cancel_orders | Sleeping 2.17s... | Error: 400 Client Error: Bad Request {"error":"
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:18 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 3/5). Func: cancel_orders | Sleeping 4.46s... | Error: 400 Client Error: Bad Request {"error":"
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:22 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 4/5). Func: cancel_orders | Sleeping 8.16s... | Error: 400 Client Error: Bad Request {"error":"
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:30 [ERROR] [async_sfgk_trader.py:_execute_api_call:206] [LINK-USD] Coinbase API Call Failed permanently after 5 attempts. Func: cancel_orders | Error: 400 Client Error: Bad Request {"error":"unknown"
logs/watchdog_Trader_LINK_USD.log:    handle_exception(response)  # Raise an HTTPError for bad responses
logs/watchdog_Trader_LINK_USD.log:  File "/opt/hft_trader/venv/lib64/python3.9/site-packages/coinbase/rest/rest_base.py", line 47, in handle_exception
logs/watchdog_Trader_LINK_USD.log:    raise HTTPError(http_error_msg, response=response)
logs/watchdog_Trader_LINK_USD.log:requests.exceptions.HTTPError: 400 Client Error: Bad Request {"error":"unknown","error_details":"proto: (line 1:16): invalid value for string field orderIds: null","message":"proto: (line 1:16): invalid value for str
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1205] [LINK-USD] Failed to cancel GTC order: 400 Client Error: Bad Request {"error":"unknown","error_details":"proto: (line 1:16): invalid value f
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:30 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.14s... | Error: 400 Client Error: Bad Request {"error":"INVA
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:32 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 2/5). Func: get_order | Sleeping 2.25s... | Error: 400 Client Error: Bad Request {"error":"INVA
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:34 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 3/5). Func: get_order | Sleeping 4.30s... | Error: 400 Client Error: Bad Request {"error":"INVA
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:38 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 4/5). Func: get_order | Sleeping 8.28s... | Error: 400 Client Error: Bad Request {"error":"INVA
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:47 [ERROR] [async_sfgk_trader.py:_execute_api_call:206] [LINK-USD] Coinbase API Call Failed permanently after 5 attempts. Func: get_order | Error: 400 Client Error: Bad Request {"error":"INVALID_ARGU
logs/watchdog_Trader_LINK_USD.log:    handle_exception(response)  # Raise an HTTPError for bad responses
logs/watchdog_Trader_LINK_USD.log:  File "/opt/hft_trader/venv/lib64/python3.9/site-packages/coinbase/rest/rest_base.py", line 47, in handle_exception
logs/watchdog_Trader_LINK_USD.log:    raise HTTPError(http_error_msg, response=response)
logs/watchdog_Trader_LINK_USD.log:requests.exceptions.HTTPError: 400 Client Error: Bad Request {"error":"INVALID_ARGUMENT","error_details":"invalid OrderId None passed to endpoint","message":"invalid OrderId None passed to endpoint"}
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1213] [LINK-USD] Failed to check GTC order fill size: 400 Client Error: Bad Request {"error":"INVALID_ARGUMENT","error_details":"invalid OrderId N
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:2026-08-28 07:28:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-28 15:39:34 [ERROR] [async_sfgk_trader.py:fetch_live_state:761] [SOL-USD] CRITICAL: DVOL cache is stale (1373277.3s old > 150s limit, Fail-Closed)
```
</details>

