---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-31 03:00:08 AM PDT (2026-08-31 10:00:08 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.33** | **-0.50** | **+0.83** | **+4.05** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.83** | **-0.50** | **-1.33** | **+17.75** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.33** | **-0.50** | **+0.83** | **+3.87** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.33** | **-0.50** | **+0.83** | **+4.05** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.33** | **-0.50** | **+0.83** | **+4.05** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.33** | **-0.50** | **+0.83** | **+4.05** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.33** | **-0.50** | **+0.83** | **+4.05** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (1.78h old) | 08-31 01:13 |
| ✅ | **TimesFM Forecasts** | Fresh (1.80h old) | 08-31 01:12 |
| ✅ | **Holding Times config** | Fresh (1.79h old) | 08-31 01:13 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-31 03:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-31 03:00 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-31 03:00 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 2105 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `46,576` | **100.0%** |
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
| `DOGE-USD` | 47 | 66.0% | 0 | 🟢 OK |
| `ETH-USD` | 22 | 68.2% | 0 | 🟢 OK |
| `LINK-USD` | 55 | 74.5% | 0 | 🟢 OK |
| `AVAX-USD` | 42 | 71.4% | 0 | 🟢 OK |
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
| `ADA-USD` | SELL | 0.19715 | `f72275bf-9b40-44da-ae99-2d6d0559319d` |
| `LINK-USD` | BUY | 11.29 | `3c32fa05-ae4e-4361-8702-336d837dacf6` |
| `AVAX-USD` | BUY | 7.208 | `aee3b8af-5577-4c1a-a3bd-2fcf39503d39` |
| `DOGE-USD` | BUY | 0.0827 | `3109b173-2f35-458b-888d-3235c293e781` |
| `USDT-USD` | SELL | 0.99964 | `78c8b3f7-b337-4b09-9bd0-14904727467f` |
| `USDT-USD` | SELL | 0.99964 | `e650c7bc-039e-494d-aa7e-73d0f14af2e8` |
| `USDT-USD` | SELL | 0.99964 | `39047963-2f98-4651-83ba-1ea44f41ad97` |
| `USDT-USD` | SELL | 0.99964 | `1ba5ca6e-1d46-4122-82e5-69f0fa7a622e` |
| `USDT-USD` | SELL | 0.99964 | `2048f08e-548b-4a9d-959d-008671056801` |
| `USDT-USD` | SELL | 0.99964 | `e00d4dbb-a9d4-4849-bdca-bf79ced3139c` |
| `USDT-USD` | SELL | 0.99964 | `3d20c4b7-ea6b-43a0-bc74-151ff9155eda` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.8h ago (2026-08-31 01:12 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **160.0h (6d 15h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 01:13:25 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **159.0h (6d 14h 59m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, HNT, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  10:00:06 AM
   CPU:   4.0%  |  MEM:   6.6% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1951795  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1951889  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1951891  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1954428  | COOL-DOWN       | 8        | Next run in 9.5s
Trader ETH-USD       | 1954429  | COOL-DOWN       | 8        | Next run in 9.5s
Trader ADA-USD       | 1951894  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1954430  | COOL-DOWN       | 8        | Next run in 9.5s
Trader BTC-USD       | 1954431  | COOL-DOWN       | 8        | Next run in 9.5s
Trader LINK-USD      | 1954432  | COOL-DOWN       | 8        | Next run in 9.5s
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
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:00:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: limit_order_gtc_buy | Sleeping 1.42s... | Error: 429 Client Error: Too Many Request
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:57:01 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:57:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:57:45 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:58:07 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:58:29 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-31 09:59:56 [WARNING] [async_sfgk_trader.py:_execute_api_call:287] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests
```
</details>

