---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-31 09:02:43 AM PDT (2026-08-31 16:02:43 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.19** | **-0.50** | **+1.69** | **-1.11** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.24** | **-0.50** | **+0.74** | **+13.06** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.19** | **-0.50** | **+1.69** | **-1.04** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.19** | **-0.50** | **+1.69** | **-1.09** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.19** | **-0.50** | **+1.69** | **-1.15** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.19** | **-0.50** | **+1.69** | **-1.09** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.19** | **-0.50** | **+1.69** | **-1.15** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (7.82h old) | 08-31 01:13 |
| ✅ | **TimesFM Forecasts** | Fresh (0.99h old) | 08-31 08:03 |
| ❌ | **Holding Times config** | STALE! (240.0h old) | Limit 14.0h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-31 09:02 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-31 09:02 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-31 09:02 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1885 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `51,507` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 11 | 45.5% | 1 | 🟢 OK |
| `ADA-USD` | 65 | 66.2% | 0 | 🟢 OK |
| `DOGE-USD` | 52 | 69.2% | 0 | 🟢 OK |
| `ETH-USD` | 23 | 65.2% | 1 | 🟢 OK |
| `LINK-USD` | 58 | 75.9% | 0 | 🟢 OK |
| `AVAX-USD` | 47 | 74.5% | 0 | 🟢 OK |
| `SOL-USD` | 22 | 77.3% | 1 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USD` | SELL | 0.99985 | `871d3e3d-7b72-48c1-ad37-909dc4327720` |
| `USDT-USD` | SELL | 0.99981 | `92f08680-d898-474d-b832-eba9fa2a0153` |
| `USDT-USD` | SELL | 0.99979 | `b6223ed6-7279-4922-bd37-08d329fd5a7c` |
| `USDT-USD` | SELL | 0.99978 | `5fc38c70-d51a-4b9c-8110-8c892231f119` |
| `AVAX-USD` | SELL | 7.231 | `c71a834a-95f6-486c-9517-44ff52c4f695` |
| `ADA-USD` | SELL | 0.19711 | `94edbc9e-027a-4c8d-9242-5d267741004a` |
| `ETH-USD` | SELL | 2473.84 | `d2a5787d-7e6a-4e30-89c4-3d76e19d4b74` |
| `LINK-USD` | SELL | 11.397 | `5a6754dd-b44a-4736-b195-f31efc390cd1` |
| `USDT-USD` | BUY | 0.99964 | `9c24d5da-55d5-4ae0-9cd4-46acc3e120cd` |
| `USDT-USD` | BUY | 0.99964 | `90d1ef0b-0531-4a74-a94e-a4d161f38bbf` |
| `USDT-USD` | SELL | 0.99965 | `c2e19d7d-81be-4574-b2bc-acc306fa3919` |
| `USDT-USD` | SELL | 0.99965 | `29b66a5f-459c-41c6-9014-7ecb894e4b8f` |
| `USDT-USD` | SELL | 0.99965 | `2d65b1d2-dbcb-4e5c-b17b-d98f8dee9d0e` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.0h ago (2026-08-31 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **154.0h (6d 9h 57m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 01:13:25 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **152.9h (6d 8h 56m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, HNT, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  04:02:42 PM
   CPU:  12.3%  |  MEM:   7.9% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2256241  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2256287  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 2256289  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2256290  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2258404  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2256292  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2259233  | COOL-DOWN       | 9        | Next run in 14.6s
Trader BTC-USD       | 2260924  | RUNNING         | 15       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2260917  | RUNNING         | 9        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-31 04:21:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.48s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 04:52:04 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.32s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 06:35:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.17s... | Error: ('Connection aborted.', ConnectionResetError
logs/watchdog_Trader_SOL_USD.log:2026-08-31 07:37:11 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: list_orders | Sleeping 1.10s... | Error: 503 Server Error: Service Unavailable go/s
logs/watchdog_Trader_SOL_USD.log:2026-08-31 07:57:21 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.44s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 07:58:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 07:58:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.32s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 07:59:56 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 08:00:19 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 08:02:32 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 08:02:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 08:50:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product_book | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:00:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: limit_order_gtc_buy | Sleeping 1.42s... | Error: 429 Client Error: Too Many Request
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:57:01 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:57:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:57:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:58:07 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:58:29 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:59:56 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 10:01:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 10:29:49 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 11:57:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 11:57:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.30s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 11:58:14 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 11:58:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:00:00 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:00:43 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:01:04 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:06:02 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.40s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:16:17 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:21:16 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.48s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 12:22:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 13:12:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 13:18:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 13:22:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 13:57:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 14:04:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 14:24:03 [ERROR] [async_sfgk_trader.py:fetch_live_state:828] [SOL-USD] CRITICAL: DVOL cache is stale (1627946.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-31 15:09:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 15:12:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests
```
</details>

