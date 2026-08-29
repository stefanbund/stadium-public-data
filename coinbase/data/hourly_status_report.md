---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-28 05:48:58 PM PDT (2026-08-29 00:48:58 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.04** | **-0.50** | **-0.54** | **+1.28** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.30** | **-0.50** | **-0.80** | **+12.80** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.04** | **-0.50** | **-0.54** | **+0.24** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-1.04** | **-0.50** | **-0.54** | **+1.22** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-1.04** | **-0.50** | **-0.54** | **+1.12** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-1.04** | **-0.50** | **-0.54** | **+0.27** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-1.04** | **-0.50** | **-0.54** | **+0.22** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (0.15h old) | 08-28 17:40 |
| ✅ | **TimesFM Forecasts** | Fresh (1.78h old) | 08-28 16:02 |
| ✅ | **Holding Times config** | Fresh (0.15h old) | 08-28 17:40 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-28 17:49 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-28 17:49 |
| ❌ | **Live Trading Telemetry** | STALE! (3.9h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 668 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `20,471` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 8 | 50.0% | 1 | 🟢 OK |
| `ADA-USD` | 43 | 67.4% | 0 | 🟢 OK |
| `DOGE-USD` | 29 | 62.1% | 0 | 🟢 OK |
| `ETH-USD` | 13 | 76.9% | 0 | 🟢 OK |
| `LINK-USD` | 31 | 67.7% | 0 | 🟢 OK |
| `AVAX-USD` | 25 | 56.0% | 1 | 🟢 OK |
| `SOL-USD` | 17 | 76.5% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USDC` | SELL | 1.0001 | `4d9f1df5-f1ce-408b-8fcb-f870df3e47db` |
| `USDT-USDC` | SELL | 1.0001 | `5fa15d4a-6b18-45bf-9b63-87c4abf65231` |
| `USDT-USDC` | SELL | 1.0001 | `c6df0641-6530-4045-8576-80625cc069b0` |
| `USDT-USDC` | SELL | 1.0001 | `66cab2eb-254c-4f1b-b5b6-1251e98e9290` |
| `USDT-USDC` | SELL | 1.0001 | `b697dc68-9e4c-47f8-b03f-079cc7e80d03` |
| `BTC-USD` | BUY | 77601.23 | `26167636-2101-4415-96b2-0d1cbcbf23a1` |
| `DOGE-USD` | BUY | 0.08509 | `2450b6b6-b2fa-4535-835d-458f87ea7aea` |
| `AVAX-USD` | BUY | 7.293 | `1bd2043e-3c5a-478b-9f3b-47d918d4b62a` |
| `ADA-USD` | SELL | 0.20364 | `faf970f4-cc82-4d21-b9a2-4dd5c6a768e4` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.8h ago (2026-08-28 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **49.2h (2d 1h 10m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-28 05:40:05 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **48.2h (2d 0h 10m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  12:48:58 AM
   CPU:   2.8%  |  MEM:   6.2% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3320892  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3320942  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 3320944  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3363525  | COOL-DOWN       | 32       | Next run in 13.8s
Trader ETH-USD       | 3363529  | COOL-DOWN       | 141      | Next run in 19.1s
Trader ADA-USD       | 3349347  | RUNNING         | 15       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3363531  | COOL-DOWN       | 32       | Next run in 24.4s
Trader BTC-USD       | 3363526  | COOL-DOWN       | 32       | Next run in 13.8s
Trader LINK-USD      | 3363536  | COOL-DOWN       | 23       | Next run in 0.0s
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
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:38 [ERROR] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 4/5). Func: get_order | Sleeping 8.28s... | Error: 400 Client Error: Bad Request {"error":"INVA
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:47 [ERROR] [async_sfgk_trader.py:_execute_api_call:206] [LINK-USD] Coinbase API Call Failed permanently after 5 attempts. Func: get_order | Error: 400 Client Error: Bad Request {"error":"INVALID_ARGU
logs/watchdog_Trader_LINK_USD.log:    handle_exception(response)  # Raise an HTTPError for bad responses
logs/watchdog_Trader_LINK_USD.log:  File "/opt/hft_trader/venv/lib64/python3.9/site-packages/coinbase/rest/rest_base.py", line 47, in handle_exception
logs/watchdog_Trader_LINK_USD.log:    raise HTTPError(http_error_msg, response=response)
logs/watchdog_Trader_LINK_USD.log:requests.exceptions.HTTPError: 400 Client Error: Bad Request {"error":"INVALID_ARGUMENT","error_details":"invalid OrderId None passed to endpoint","message":"invalid OrderId None passed to endpoint"}
logs/watchdog_Trader_LINK_USD.log:2026-08-28 14:07:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1213] [LINK-USD] Failed to check GTC order fill size: 400 Client Error: Bad Request {"error":"INVALID_ARGUMENT","error_details":"invalid OrderId N
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:2026-08-29 00:14:01 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.26s... | Error: 502 Server Error: Bad Gateway <html>   <he
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_LINK_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:2026-08-28 07:28:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-28 15:39:34 [ERROR] [async_sfgk_trader.py:fetch_live_state:761] [SOL-USD] CRITICAL: DVOL cache is stale (1373277.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-29 00:15:17 [WARNING] [async_sfgk_trader.py:_execute_api_call:220] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.40s... | Error: 502 Server Error: Bad Gateway <html>   <head
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
```
</details>

