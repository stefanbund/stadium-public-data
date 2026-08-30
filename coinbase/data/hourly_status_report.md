---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-29 09:06:34 PM PDT (2026-08-30 04:06:34 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-3.45** | **-0.50** | **-2.95** | **+24.00** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.11** | **-0.50** | **+1.61** | **+38.01** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-3.45** | **-0.50** | **-2.95** | **+23.97** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-3.45** | **-0.50** | **-2.95** | **+23.97** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-3.45** | **-0.50** | **-2.95** | **+23.97** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-3.45** | **-0.50** | **-2.95** | **+23.97** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-3.45** | **-0.50** | **-2.95** | **+23.97** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (2.33h old) | 08-29 18:46 |
| ✅ | **TimesFM Forecasts** | Fresh (0.24h old) | 08-29 20:52 |
| ❌ | **Holding Times config** | STALE! (204.1h old) | Limit 146.1h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-29 21:06 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-29 21:06 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-29 21:06 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1872 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `22,605` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 9 | 44.4% | 2 | ⚠️ DRIFT |
| `ADA-USD` | 45 | 64.4% | 2 | 🟢 OK |
| `DOGE-USD` | 31 | 64.5% | 0 | 🟢 OK |
| `ETH-USD` | 14 | 71.4% | 1 | 🟢 OK |
| `LINK-USD` | 33 | 69.7% | 0 | 🟢 OK |
| `AVAX-USD` | 27 | 59.3% | 0 | 🟢 OK |
| `SOL-USD` | 20 | 80.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | BUY | 7.295 | `4c05e47a-eef3-4819-8ea4-a67d4bc2b14d` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.2h ago (2026-08-29 08:52 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **21.9h (0d 21h 53m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-29 06:46:46 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **20.9h (0d 20h 53m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  04:06:33 AM
   CPU:   8.2%  |  MEM:   6.0% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 429473   | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 429479   | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 429481   | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 438007   | RUNNING         | 22       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 438902   | COOL-DOWN       | 25       | Next run in 9.7s
Trader ADA-USD       | 438903   | COOL-DOWN       | 31       | Next run in 9.7s
Trader DOGE-USD      | 438904   | COOL-DOWN       | 31       | Next run in 9.7s
Trader BTC-USD       | 438905   | COOL-DOWN       | 31       | Next run in 9.7s
Trader LINK-USD      | 439024   | COOL-DOWN       | 25       | Next run in 14.9s
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
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:46:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:47:28 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:47:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:48:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:49:08 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:55:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 01:56:07 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:56:17 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:56:38 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.48s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:57:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.47s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:57:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:58:44 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:59:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 03:59:26 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:01:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:01:52 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:02:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:02:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:02:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:03:16 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 04:05:01 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests
```
</details>

