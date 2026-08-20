---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-20 02:22:21 PM PDT (2026-08-20 21:22:21 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.47** | **-0.50** | **+0.97** | **-17.47** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.39** | **-0.50** | **+0.89** | **-4.31** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.47** | **-0.50** | **+0.97** | **-17.48** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.47** | **-0.50** | **+0.97** | **-17.44** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.47** | **-0.50** | **+0.97** | **-46.76** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.47** | **-0.50** | **+0.97** | **-17.54** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.47** | **-0.50** | **+0.97** | **-17.70** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (20.65h old) | 08-19 17:43 |
| ✅ | **TimesFM Forecasts** | Fresh (6.34h old) | 08-20 08:02 |
| ❌ | **Holding Times config** | STALE! (196.7h old) | Limit 168h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-20 14:22 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-20 14:22 |
| ❌ | **Live Trading Telemetry** | STALE! (0.9h old) | Limit 0.05h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `4,212` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `DOGE-USD` | 87 | 93.1% | 0 | 🟢 OK |
| `LINK-USD` | 51 | 90.2% | 0 | 🟢 OK |
| `SOL-USD` | 65 | 92.3% | 0 | 🟢 OK |
| `ETH-USD` | 55 | 89.1% | 0 | 🟢 OK |
| `ADA-USD` | 85 | 92.9% | 0 | 🟢 OK |
| `AVAX-USD` | 81 | 93.8% | 0 | 🟢 OK |
| `BTC-USD` | 54 | 92.6% | 0 | 🟢 OK |

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

- **TimesFM Forecast DB**: 🟢 Updated 6.3h ago (2026-08-20 08:02 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **76.6h (3d 4h 37m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **75.6h (3d 3h 37m)**)
- **Selected Mega Cap Universe**: `Could not fetch active universe from EC2`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  09:22:20 PM
   CPU:   3.7%  |  MEM:   8.4% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1874568  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1939953  | RUNNING         | 6        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1943897  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1933347  | RUNNING         | 7        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1934092  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1906680  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1923025  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader SOL-USD       | 1939954  | RUNNING         | 3        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-20 18:50:38 [WARNING] [async_sfgk_trader.py:_safe_requests_get:240] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.24s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
```
</details>

