---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-20 06:35:19 PM PDT (2026-08-21 01:35:19 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.45** | **-0.50** | **+1.95** | **-19.62** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.38** | **-0.50** | **+1.88** | **-6.42** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.45** | **-0.50** | **+1.95** | **-19.78** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.45** | **-0.50** | **+1.95** | **-19.62** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.45** | **-0.50** | **+1.95** | **-19.78** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.45** | **-0.50** | **+1.95** | **-18.38** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.45** | **-0.50** | **+1.95** | **-18.42** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (24.87h old) | 08-19 17:43 |
| ✅ | **TimesFM Forecasts** | Fresh (2.56h old) | 08-20 16:02 |
| ❌ | **Holding Times config** | STALE! (200.9h old) | Limit 168h |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-20 18:35 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-20 18:35 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-20 18:35 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `4,255` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `DOGE-USD` | 114 | 93.9% | 0 | 🟢 OK |
| `LINK-USD` | 66 | 92.4% | 0 | 🟢 OK |
| `SOL-USD` | 78 | 92.3% | 0 | 🟢 OK |
| `ETH-USD` | 72 | 90.3% | 0 | 🟢 OK |
| `ADA-USD` | 110 | 93.6% | 0 | 🟢 OK |
| `AVAX-USD` | 100 | 93.0% | 0 | 🟢 OK |
| `BTC-USD` | 71 | 93.0% | 0 | 🟢 OK |

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

- **TimesFM Forecast DB**: 🟢 Updated 2.6h ago (2026-08-20 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **72.4h (3d 0h 24m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **71.4h (2d 23h 24m)**)
- **Selected Mega Cap Universe**: `Could not fetch active universe from EC2`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  01:35:18 AM
   CPU:  10.8%  |  MEM:   6.1% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2056912  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2141516  | COOL-DOWN       | 23       | Next run in 15.0s
Trader ETH-USD       | 2141615  | RUNNING         | 13       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2141412  | COOL-DOWN       | 22       | Next run in 4.9s
Trader DOGE-USD      | 2141616  | RUNNING         | 19       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2141507  | COOL-DOWN       | 14       | Next run in 10.0s
Trader LINK-USD      | 2128957  | RUNNING         | 7        | Evaluating Funnel/Polling Order
Trader SOL-USD       | 2129166  | RUNNING         | 6        | Evaluating Funnel/Polling Order
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

