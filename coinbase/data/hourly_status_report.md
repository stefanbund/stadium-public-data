---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 02:37:55 PM PDT (2026-08-24 21:37:55 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.56** | **-0.50** | **-0.06** | **-5.91** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.55** | **-0.50** | **-1.05** | **+9.48** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.56** | **-0.50** | **-0.06** | **-5.98** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.56** | **-0.50** | **-0.06** | **-5.95** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.56** | **-0.50** | **-0.06** | **-5.91** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.56** | **-0.50** | **-0.06** | **-5.93** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.56** | **-0.50** | **-0.06** | **-5.97** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (1.70h old) | 08-24 12:56 |
| ✅ | **TimesFM Forecasts** | Fresh (1.73h old) | 08-24 12:54 |
| ❌ | **Holding Times config** | STALE! (77.6h old) | Limit 19.6h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 14:38 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 14:37 |
| ❌ | **Live Trading Telemetry** | STALE! (0.9h old) | Limit 0.1h |

<br>

> **Utilization Certification**: 🔴 **FAILED.** Guardian watchdog offline, unable to certify utilization.


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `607` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 2 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 2 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.655 | `0e0da8e9-65c3-40f9-bc10-7ca89cfec5cb` |
| `LINK-USD` | SELL | 11.735 | `f3afa462-6fbc-4d29-ad9b-8e1db4c8fb4e` |
| `DOGE-USD` | SELL | 0.09233 | `60d899b5-20f6-418d-8d95-8e76b7fca1e2` |
| `ETH-USD` | SELL | 2514.95 | `dd05ead3-9b5a-497a-ac26-256d87814b6f` |
| `AVAX-USD` | BUY | 7.512 | `a90a3078-8c18-4d6b-b207-68245b7a2324` |
| `AVAX-USD` | BUY | 7.512 | `0b0a69ab-0416-47aa-819d-2f2e2e8986f4` |
| `ADA-USD` | BUY | 0.22017 | `ea7f79a4-1cfa-4b0f-8961-78aca7a42711` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.7h ago (2026-08-24 12:54 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 12:54:26 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **148.4h (6d 4h 22m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 12:56:08 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **147.4h (6d 3h 21m)**)
- **Selected Mega Cap Universe**: `BTC, ADA, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
Guardian watchdog table not available
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
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
logs/watchdog_Trader_SOL_USD.log:NameError: name 'TimesFMForecastGate' is not defined
```
</details>

