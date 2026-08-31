---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-31 02:00:05 AM PDT (2026-08-31 09:00:05 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.75** | **-0.50** | **-0.25** | **+4.33** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.85** | **-0.50** | **-1.35** | **+17.83** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.75** | **-0.50** | **-0.25** | **+4.33** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.75** | **-0.50** | **-0.25** | **+4.33** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.75** | **-0.50** | **-0.25** | **+4.33** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.75** | **-0.50** | **-0.25** | **+4.33** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.75** | **-0.50** | **-0.25** | **+4.33** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (0.78h old) | 08-31 01:13 |
| ✅ | **TimesFM Forecasts** | Fresh (0.80h old) | 08-31 01:12 |
| ✅ | **Holding Times config** | Fresh (0.78h old) | 08-31 01:13 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-31 02:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-31 02:00 |
| ❌ | **Live Trading Telemetry** | STALE! (0.2h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1699 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `45,770` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 11 | 45.5% | 1 | 🟢 OK |
| `ADA-USD` | 61 | 63.9% | 0 | 🟢 OK |
| `DOGE-USD` | 46 | 65.2% | 1 | 🟢 OK |
| `ETH-USD` | 22 | 68.2% | 0 | 🟢 OK |
| `LINK-USD` | 55 | 74.5% | 0 | 🟢 OK |
| `AVAX-USD` | 41 | 70.7% | 0 | 🟢 OK |
| `SOL-USD` | 22 | 77.3% | 1 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USD` | BUY | 0.99989 | `3785cacc-1fad-4ca0-849e-85dd67977b0d` |
| `USDT-USD` | BUY | 0.99989 | `ff96afe4-fcef-4f13-a382-cf3e2ac41c26` |
| `USDT-USD` | BUY | 0.99989 | `30785a7f-5049-4ed0-a5d9-9f6036743c5e` |
| `USDT-USD` | BUY | 0.99989 | `5e60dbd5-97c4-4ad3-9eeb-c4608f2b49af` |
| `USDT-USD` | BUY | 0.99989 | `418beafd-5eca-4447-b9d0-4b86aab20127` |
| `USDT-USD` | BUY | 0.99989 | `d17c269a-f0f4-4bab-b987-91a8bc6faa7b` |
| `USDT-USD` | BUY | 0.99989 | `4975e442-3ab9-4b37-bbf2-ae6e0616335d` |
| `USDT-USD` | BUY | 0.99989 | `1f42cb4e-d028-4ca4-9648-acc3cdd4aff5` |
| `USDT-USD` | BUY | 0.99989 | `85ef4a52-5e1f-4a2b-9991-531b73a1730c` |
| `USDT-USD` | SELL | 0.99993 | `239e44b1-6743-4c6c-9041-e86fe2ce879b` |
| `AVAX-USD` | BUY | 7.206 | `1f0a0cdc-d37a-4729-b424-8aee95011796` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.8h ago (2026-08-31 01:12 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **161.0h (6d 16h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 01:13:25 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **160.0h (6d 15h 59m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, HNT, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  09:00:01 AM
   CPU:   4.9%  |  MEM:   6.1% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1850239  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1850318  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1850325  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1902100  | COOL-DOWN       | 121      | Next run in 4.0s
Trader ETH-USD       | 1903566  | COOL-DOWN       | 167      | Next run in 9.4s
Trader ADA-USD       | 1902212  | COOL-DOWN       | 66       | Next run in 14.7s
Trader DOGE-USD      | 1902196  | COOL-DOWN       | 110      | Next run in 9.4s
Trader BTC-USD       | 1902197  | COOL-DOWN       | 144      | Next run in 9.4s
Trader LINK-USD      | 1902218  | RUNNING         | 47       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:00:12 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.48s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:01:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.47s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:02:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.40s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:03:02 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.30s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:03:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:04:28 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:05:10 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 14:05:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 17:01:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 21:57:40 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-30 23:56:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.41s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 01:56:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 01:57:28 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 01:57:50 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 01:58:33 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 01:58:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
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
```
</details>

