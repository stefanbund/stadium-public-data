---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-31 05:03:01 AM PDT (2026-08-31 12:03:01 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.25** | **-0.50** | **+0.75** | **+2.97** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.51** | **-0.50** | **+1.01** | **+17.33** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.25** | **-0.50** | **+0.75** | **+2.81** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.25** | **-0.50** | **+0.75** | **+3.16** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.25** | **-0.50** | **+0.75** | **+2.81** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.25** | **-0.50** | **+0.75** | **+2.85** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.25** | **-0.50** | **+0.75** | **+2.81** | 5.0 | 🔴 DAW VETOED |



### 📖 Volatility & VRP Safety Barometer
The system's Layer 1 DAW Causal Gate continuously gauges execution safety using **Deribit DVOL Z-Score ($Z$)** and **Variance Risk Premium (VRP)**:
- **Mathematical Principle**: $\text{VRP} = \text{IV}_{\text{Deribit DVOL}} - \text{RV}_{\text{Realized Vol}}$ and $Z = \frac{\text{DVOL}_t - \mu_{\text{4h}}}{\sigma_{\text{4h}}}$.
- **Regime Safety Spectrum**:
  - 🟢 **Safe / Compression ($Z \le Z_{opt}$)**: Derivatives market prices low tail risk. Order books are deep, adverse selection is minimal, and TimesFM zero-shot scalps operate at peak win rates.
  - 🔴 **Hostile / Expansion ($Z > Z_{opt}$)**: Options pricing aggressive shock risk. Taker order sweeps cause adverse selection; **DAW Causality Veto is active** to preserve capital.
---
## 2. 🔒 MLOps & Trading Telemetry Provenance & Utilization Certification: 🟢 ALL SYNCED & CERTIFIED
We hereby certify that the mission-critical algorithmic data assets uploaded by the Mac Mini MLOps node have been audited for freshness, fall within their strict operational due dates, and are actively being utilized by the live EC2 HFT Trader.

| Status | Data Asset | Freshness / State | Details / Timestamp |
| :---: | :--- | :--- | :--- |
| ✅ | **Go-List JSON** | Fresh (3.83h old) | 08-31 01:13 |
| ✅ | **TimesFM Forecasts** | Fresh (0.18h old) | 08-31 04:52 |
| ✅ | **Holding Times config** | Fresh (3.84h old) | 08-31 01:13 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-31 05:03 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-31 05:03 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-31 05:03 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1993 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `48,202` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 11 | 45.5% | 1 | 🟢 OK |
| `ADA-USD` | 62 | 64.5% | 0 | 🟢 OK |
| `DOGE-USD` | 48 | 66.7% | 0 | 🟢 OK |
| `ETH-USD` | 22 | 68.2% | 0 | 🟢 OK |
| `LINK-USD` | 56 | 75.0% | 0 | 🟢 OK |
| `AVAX-USD` | 43 | 72.1% | 0 | 🟢 OK |
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
| `USDT-USD` | SELL | 0.99962 | `0b02b00a-a899-46ac-ba9b-f2db5484d3a7` |
| `DOGE-USD` | SELL | 0.08278 | `572e65cf-0303-4f96-b89b-7820bf7f8d71` |
| `USDT-USD` | SELL | 0.99956 | `e96141f9-3293-4ca2-a86b-cb45fc25e603` |
| `LINK-USD` | BUY | 11.224 | `b58d691d-2582-4d30-9d11-eb7a1cac6191` |
| `AVAX-USD` | BUY | 7.184 | `2059f30d-ba18-47cd-bec0-73b1526c8f0b` |
| `USDT-USD` | BUY | 0.99955 | `65e7b50d-d9dd-4869-8e4c-f64aa7c2c2c7` |
| `USDT-USD` | BUY | 0.99955 | `55737f74-e3d0-423e-a6bb-0668059dd362` |
| `USDT-USD` | BUY | 0.99955 | `f65bded2-07ec-417a-b83a-08e6f794d8e0` |
| `USDT-USD` | BUY | 0.99955 | `f1cae698-df0f-4e07-939e-c6201f7f9c48` |
| `USDT-USD` | SELL | 0.99956 | `606c9f8d-6dfa-4a0a-be2b-672295dc44d2` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.2h ago (2026-08-31 04:52 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **157.9h (6d 13h 56m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 01:13:25 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **156.9h (6d 12h 56m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, HNT, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  12:02:59 PM
   CPU:   2.2%  |  MEM:   7.3% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2052945  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2053021  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 2053023  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2057220  | RUNNING         | 13       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2058272  | COOL-DOWN       | 16       | Next run in 9.6s
Trader ADA-USD       | 2058273  | COOL-DOWN       | 16       | Next run in 9.6s
Trader DOGE-USD      | 2053027  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2058274  | COOL-DOWN       | 16       | Next run in 9.6s
Trader LINK-USD      | 2056572  | RUNNING         | 5        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-31 01:59:17 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 02:01:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 02:31:43 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.40s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 03:38:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.32s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 03:42:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.20s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 03:43:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 03:56:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 03:57:09 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.16s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 03:59:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.48s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 04:01:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 04:02:10 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 04:17:24 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
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
```
</details>

