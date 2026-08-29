---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-28 10:36:16 PM PDT (2026-08-29 05:36:16 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **N/A** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.46** | **-0.50** | **-0.96** | **+13.42** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **N/A** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **N/A** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **N/A** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **+0.31** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **+1.43** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (1.17h old) | 08-28 21:26 |
| ✅ | **TimesFM Forecasts** | Fresh (1.74h old) | 08-28 20:51 |
| ✅ | **Holding Times config** | Fresh (1.17h old) | 08-28 21:26 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-28 22:36 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-28 22:36 |
| ❌ | **Live Trading Telemetry** | STALE! (0.2h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 490 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `20,488` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 9 | 44.4% | 2 | ⚠️ DRIFT |
| `ADA-USD` | 44 | 65.9% | 1 | 🟢 OK |
| `DOGE-USD` | 30 | 63.3% | 0 | 🟢 OK |
| `ETH-USD` | 14 | 71.4% | 1 | 🟢 OK |
| `LINK-USD` | 32 | 68.8% | 0 | 🟢 OK |
| `AVAX-USD` | 26 | 57.7% | 0 | 🟢 OK |
| `SOL-USD` | 20 | 80.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | BUY | 7.296 | `1af7ab1b-41b1-4623-a837-5c7a9800dcd3` |
| `USDT-USDC` | SELL | 1.0001 | `5fa15d4a-6b18-45bf-9b63-87c4abf65231` |
| `USDT-USDC` | SELL | 1.0001 | `c6df0641-6530-4045-8576-80625cc069b0` |
| `USDT-USDC` | SELL | 1.0001 | `66cab2eb-254c-4f1b-b5b6-1251e98e9290` |
| `USDT-USDC` | SELL | 1.0001 | `b697dc68-9e4c-47f8-b03f-079cc7e80d03` |
| `SOL-USD` | SELL | 104.15 | `9fafa961-46d0-4117-b653-4036e0451453` |
| `BTC-USD` | BUY | 77553.61 | `a8bc57dc-b145-4cbc-acec-d1997cb27ae5` |
| `LINK-USD` | BUY | 11.353 | `7334baf9-03c4-40d0-a207-60766a888c3c` |
| `ADA-USD` | SELL | 0.20324 | `d5465c97-f5aa-4806-a399-06c46dd6f5ca` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.7h ago (2026-08-28 08:51 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **44.4h (1d 20h 23m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-28 09:26:20 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **43.4h (1d 19h 23m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:36:13 AM
   CPU:   5.8%  |  MEM:   8.4% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3531896  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3531994  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 3531996  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3583508  | RUNNING         | 8        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3584224  | RUNNING         | 17       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3578018  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3582381  | RUNNING         | 14       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3582755  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3582857  | RUNNING         | 26       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:IndentationError: expected an indented block
logs/watchdog_Trader_SOL_USD.log:2026-08-29 04:26:29 [WARNING] [async_sfgk_trader.py:_execute_api_call:263] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.37s... | Error: 429 Client Error: Too Many Requests
```
</details>

