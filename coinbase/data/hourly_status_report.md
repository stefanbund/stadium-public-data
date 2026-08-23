---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-23 03:13:58 PM PDT (2026-08-23 22:13:58 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+3.64** | **-0.50** | **+4.14** | **+11.75** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+4.16** | **-0.50** | **+4.66** | **+28.63** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+3.64** | **-0.50** | **+4.14** | **+11.75** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+3.64** | **-0.50** | **+4.14** | **+11.75** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+3.64** | **-0.50** | **+4.14** | **+11.75** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+3.64** | **-0.50** | **+4.14** | **+11.75** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+3.64** | **-0.50** | **+4.14** | **+11.75** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (19.81h old) | 08-22 19:25 |
| ✅ | **TimesFM Forecasts** | Fresh (0.49h old) | 08-23 14:44 |
| ✅ | **Holding Times config** | Fresh (54.19h old) | 08-21 09:02 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-23 15:13 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-23 15:14 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-23 15:13 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `21,866` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | 8 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 9 | 88.9% | 0 | 🟢 OK |
| `DOGE-USD` | 8 | 100.0% | 0 | 🟢 OK |
| `ADA-USD` | 7 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 6 | 100.0% | 0 | 🟢 OK |
| `BTC-USD` | 3 | 66.7% | 1 | 🟢 OK |
| `ETH-USD` | 3 | 66.7% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.5h ago (2026-08-23 02:44 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **3.8h (0d 3h 45m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-22 07:25:41 PM PDT`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **2.8h (0d 2h 45m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  10:13:57 PM
   CPU:  18.2%  |  MEM:   6.3% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1460195  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1484132  | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1484133  | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1484134  | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1484135  | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1484136  | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1484137  | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 1484138  | RUNNING         | 75       | Evaluating Funnel/Polling Order
================================================================================
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
logs/watchdog_Trader_AVAX_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_AVAX_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_BTC_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [BTC-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_BTC_USD.log:2026-08-23 14:42:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [BTC-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_BTC_USD.log:2026-08-23 14:42:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [BTC-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.44s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_BTC_USD.log:2026-08-23 18:20:16 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [BTC-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_BTC_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_BTC_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 18:20:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [DOGE-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_DOGE_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_DOGE_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_ETH_USD.log:2026-08-23 07:45:04 [ERROR] [async_sfgk_trader.py:fetch_live_state:492] [ETH-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 328) (Fail-Closed)
logs/watchdog_Trader_ETH_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_ETH_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 328)
logs/watchdog_Trader_ETH_USD.log:2026-08-23 07:49:57 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 08:52:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 08:52:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 09:26:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 22:09:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 22:09:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-23 08:52:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-23 09:26:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-23 18:20:16 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [LINK-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_LINK_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_SOL_USD.log:2026-08-23 04:08:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 04:08:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 07:14:47 [WARNING] [async_sfgk_trader.py:_safe_requests_get:249] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.14s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
logs/watchdog_Trader_SOL_USD.log:2026-08-23 16:48:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:492] [SOL-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 13 column 1 (char 339) (Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_SOL_USD.log:json.decoder.JSONDecodeError: Extra data: line 13 column 1 (char 339)
logs/watchdog_Trader_SOL_USD.log:2026-08-23 18:20:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [SOL-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_SOL_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
```
</details>

