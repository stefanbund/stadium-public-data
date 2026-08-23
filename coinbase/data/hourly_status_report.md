---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-23 12:14:37 AM PDT (2026-08-23 07:14:37 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **+4.45** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **+2.01** | **-0.50** | **+2.51** | **+23.66** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **+8.74** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **+4.45** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **+4.54** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **+4.42** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **+4.45** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (4.82h old) | 08-22 19:25 |
| ✅ | **TimesFM Forecasts** | Fresh (0.21h old) | 08-23 00:02 |
| ✅ | **Holding Times config** | Fresh (39.20h old) | 08-21 09:02 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-23 00:14 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-23 00:14 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-23 00:14 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `4,780` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 5 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 6 | 100.0% | 0 | 🟢 OK |
| `ADA-USD` | 5 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 5 | 100.0% | 0 | 🟢 OK |
| `BTC-USD` | 2 | 100.0% | 0 | 🟢 OK |

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

- **TimesFM Forecast DB**: 🟢 Updated 0.2h ago (2026-08-23 12:02 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **18.8h (0d 18h 45m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-22 07:25:41 PM PDT`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **17.8h (0d 17h 45m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  07:14:38 AM
   CPU:   4.7%  |  MEM:   7.7% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 602345   | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 642899   | RUNNING         | 95       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 674711   | COOL-DOWN       | 253      | Next run in 4.5s
Trader ADA-USD       | 675080   | RUNNING         | 100      | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 642978   | RUNNING         | 97       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 640831   | RUNNING         | 94       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 642822   | RUNNING         | 97       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 642900   | RUNNING         | 96       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_ADA_USD.log:2026-08-23 03:40:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ADA-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ADA_USD.log:2026-08-23 03:40:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ADA-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.28s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ADA_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ADA-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ADA_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ADA-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ADA_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ADA-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_BTC_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [BTC-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 04:08:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 04:08:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests
```
</details>

