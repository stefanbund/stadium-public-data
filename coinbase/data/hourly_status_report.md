---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-19 11:55:33 PM PDT (2026-08-20 06:55:33 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.97** | **-0.50** | **-0.47** | **-40.63** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-0.14** | **-0.50** | **+0.36** | **-26.23** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.97** | **-0.50** | **-0.47** | **-40.23** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.97** | **-0.50** | **-0.47** | **-40.59** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.97** | **-0.50** | **-0.47** | **-40.47** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.97** | **-0.50** | **-0.47** | **-40.88** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.97** | **-0.50** | **-0.47** | **-40.63** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (6.21h old) | 08-19 17:43 |
| ✅ | **TimesFM Forecasts** | Fresh (1.19h old) | 08-19 22:44 |
| ❌ | **Holding Times config** | STALE! (182.3h old) | Limit 168h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-19 23:55 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-19 23:55 |
| ❌ | **Live Trading Telemetry** | STALE! (0.2h old) | Limit 0.05h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `0` | **0.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `DOGE-USD` | 20 | 90.0% | 0 | 🟢 OK |
| `LINK-USD` | 16 | 87.5% | 0 | 🟢 OK |
| `SOL-USD` | 19 | 89.5% | 0 | 🟢 OK |
| `ETH-USD` | 11 | 81.8% | 0 | 🟢 OK |
| `ADA-USD` | 14 | 78.6% | 0 | 🟢 OK |
| `AVAX-USD` | 14 | 85.7% | 0 | 🟢 OK |
| `BTC-USD` | 13 | 92.3% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `LINK-USD` | SELL | 10.595 | `9864461e-fe6d-4ecc-bd07-a886c83e884b` |
| `ETH-USD` | SELL | 2273.73 | `6178a012-db27-414b-b669-edf54fdb2f0d` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.2h ago (2026-08-19 10:44 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **91.1h (3d 19h 4m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **90.1h (3d 18h 4m)**)
- **Selected Mega Cap Universe**: `Could not fetch active universe from EC2`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:55:32 AM
   CPU:   8.1%  |  MEM:   8.4% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1209007  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1256459  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1256508  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1253470  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1255037  | RUNNING         | 6        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1256087  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1259720  | RUNNING         | 10       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 1255045  | RUNNING         | 7        | Evaluating Funnel/Polling Order
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
No critical errors in current window.
```
</details>

