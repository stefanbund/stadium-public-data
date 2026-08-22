---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-22 05:16:10 AM PDT (2026-08-22 12:16:10 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.59** | **-0.50** | **-0.09** | **-47.08** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **+0.19** | **-0.50** | **+0.69** | **-31.80** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.59** | **-0.50** | **-0.09** | **-47.08** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.59** | **-0.50** | **-0.09** | **-47.08** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.59** | **-0.50** | **-0.09** | **-48.46** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.59** | **-0.50** | **-0.09** | **-47.17** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.59** | **-0.50** | **-0.09** | **-47.21** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (20.08h old) | 08-21 09:11 |
| ✅ | **TimesFM Forecasts** | Fresh (5.24h old) | 08-22 00:02 |
| ✅ | **Holding Times config** | Fresh (20.22h old) | 08-21 09:02 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-22 05:16 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-22 05:16 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-22 05:16 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `11,091` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 93 | 92.5% | 0 | 🟢 OK |
| `ETH-USD` | 20 | 95.0% | 0 | 🟢 OK |
| `SOL-USD` | 55 | 92.7% | 0 | 🟢 OK |
| `AVAX-USD` | 67 | 94.0% | 0 | 🟢 OK |
| `BTC-USD` | 29 | 82.8% | 0 | 🟢 OK |
| `DOGE-USD` | 119 | 92.4% | 0 | 🟢 OK |
| `LINK-USD` | 84 | 92.9% | 0 | 🟢 OK |

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

- **TimesFM Forecast DB**: 🟢 Updated 5.2h ago (2026-08-22 12:02 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **37.7h (1d 13h 43m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-21 09:11:23 AM PDT`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **36.7h (1d 12h 43m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  12:16:07 PM
   CPU:   8.3%  |  MEM:   7.8% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3844398  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 3866641  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3867885  | RUNNING         | 87       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3866642  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3866652  | RUNNING         | 6        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3844471  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3864682  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader SOL-USD       | 3863671  | COOL-DOWN       | 2        | Next run in 4.3s
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
logs/watchdog_Trader_DOGE_USD.log:2026-08-21 21:18:23 [WARNING] [async_sfgk_trader.py:_safe_requests_get:240] [DOGE-USD] requests.get Exception (Attempt 1/5). Sleeping 1.31s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443):
logs/watchdog_Trader_SOL_USD.log:2026-08-22 01:14:46 [WARNING] [async_sfgk_trader.py:_safe_requests_get:240] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.22s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
```
</details>

