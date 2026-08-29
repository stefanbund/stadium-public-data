---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-28 09:57:06 PM PDT (2026-08-29 04:57:06 UTC)`  
> **System Health**: **🟢 ALL SYSTEMS NOMINAL** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.37** | **-0.50** | **-0.87** | **N/A** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.43** | **-0.50** | **-0.93** | **N/A** | 5.0 | 🟢 SAFE |
| `ADA-USD` | DVOL_BTC | **-1.37** | **-0.50** | **-0.87** | **+0.24** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-1.37** | **-0.50** | **-0.87** | **N/A** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-1.37** | **-0.50** | **-0.87** | **N/A** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-1.37** | **-0.50** | **-0.87** | **+0.27** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-1.37** | **-0.50** | **-0.87** | **+0.39** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (0.52h old) | 08-28 21:26 |
| ✅ | **TimesFM Forecasts** | Fresh (1.09h old) | 08-28 20:51 |
| ✅ | **Holding Times config** | Fresh (0.52h old) | 08-28 21:26 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-28 21:57 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-28 21:57 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-28 21:57 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 500 recent read events).


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
| `SOL-USD` | 19 | 78.9% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `DOGE-USD` | SELL | 0.0852 | `df258d6c-8acd-4568-94b0-04381bf23ca2` |
| `USDT-USDC` | SELL | 1.0001 | `5fa15d4a-6b18-45bf-9b63-87c4abf65231` |
| `USDT-USDC` | SELL | 1.0001 | `c6df0641-6530-4045-8576-80625cc069b0` |
| `USDT-USDC` | SELL | 1.0001 | `66cab2eb-254c-4f1b-b5b6-1251e98e9290` |
| `USDT-USDC` | SELL | 1.0001 | `b697dc68-9e4c-47f8-b03f-079cc7e80d03` |
| `ADA-USD` | SELL | 0.20364 | `faf970f4-cc82-4d21-b9a2-4dd5c6a768e4` |
| `AVAX-USD` | SELL | 7.31 | `1b4aecfe-f1fb-4563-986a-08e6b6f566bf` |
| `BTC-USD` | SELL | 77795.24 | `f521e3cb-7bcb-4005-8d60-751adc2577a5` |
| `ETH-USD` | SELL | 2442.78 | `2984ffa4-2f74-4bb7-bf67-162fad68473f` |
| `SOL-USD` | SELL | 104.1 | `81316345-ea50-4c67-a639-4a9721a77ae0` |
| `LINK-USD` | BUY | 11.355 | `42778d11-5641-4110-a848-da8258e0aa25` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.1h ago (2026-08-28 08:51 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **45.0h (1d 21h 2m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-28 09:26:20 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **44.0h (1d 20h 2m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  04:57:02 AM
   CPU:   4.6%  |  MEM:   8.8% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3531896  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3531994  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 3531996  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3531997  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3531999  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3532000  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3532001  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3532002  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3553693  | RUNNING         | 12       | Evaluating Funnel/Polling Order
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

