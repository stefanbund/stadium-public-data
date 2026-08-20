---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-19 10:00:09 PM PDT (2026-08-20 05:00:09 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.27** | **-0.50** | **+0.23** | **-40.79** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.28** | **-0.50** | **+0.78** | **-26.29** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.27** | **-0.50** | **+0.23** | **-40.82** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.27** | **-0.50** | **+0.23** | **-40.79** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.27** | **-0.50** | **+0.23** | **-40.84** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.27** | **-0.50** | **+0.23** | **-40.48** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.27** | **-0.50** | **+0.23** | **-40.81** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (4.28h old) | 08-19 17:43 |
| ✅ | **TimesFM Forecasts** | Fresh (5.97h old) | 08-19 16:02 |
| ❌ | **Holding Times config** | STALE! (180.3h old) | Limit 168h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-19 22:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-19 22:00 |
| ❌ | **Live Trading Telemetry** | STALE! (0.1h old) | Limit 0.05h |

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
| `DOGE-USD` | 14 | 85.7% | 0 | 🟢 OK |
| `LINK-USD` | 4 | 75.0% | 0 | 🟢 OK |
| `SOL-USD` | 11 | 81.8% | 0 | 🟢 OK |
| `ETH-USD` | 7 | 71.4% | 0 | 🟢 OK |
| `ADA-USD` | 11 | 72.7% | 0 | 🟢 OK |
| `AVAX-USD` | 9 | 77.8% | 0 | 🟢 OK |
| `BTC-USD` | 9 | 88.9% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `LINK-USD` | SELL | 10.595 | `9864461e-fe6d-4ecc-bd07-a886c83e884b` |
| `ETH-USD` | SELL | 2273.73 | `6178a012-db27-414b-b669-edf54fdb2f0d` |
| `SOL-USD` | SELL | 85.66 | `a22d9167-ab29-4976-84ab-ad2f2158ca90` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 6.0h ago (2026-08-19 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **93.0h (3d 20h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **92.0h (3d 19h 59m)**)
- **Selected Mega Cap Universe**: `Could not fetch active universe from EC2`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:00:06 AM
   CPU:   3.4%  |  MEM:   8.4% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1117529  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1170583  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1170939  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1170904  | RUNNING         | 5        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1171037  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1170940  | RUNNING         | 5        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1145567  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader SOL-USD       | 1170905  | RUNNING         | 5        | Evaluating Funnel/Polling Order
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

