---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 02:00:05 PM PDT (2026-08-24 21:00:05 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **-5.91** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.68** | **-0.50** | **-1.18** | **+9.26** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **-5.98** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **-5.95** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **-5.91** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **-5.93** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.62** | **-0.50** | **-0.12** | **-5.97** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (1.07h old) | 08-24 12:56 |
| ✅ | **TimesFM Forecasts** | Fresh (1.10h old) | 08-24 12:54 |
| ✅ | **Holding Times config** | Fresh (1.07h old) | 08-24 12:56 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 14:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 14:00 |
| ❌ | **Live Trading Telemetry** | STALE! (0.3h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `596` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 3 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 2 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `LINK-USD` | SELL | 11.735 | `f3afa462-6fbc-4d29-ad9b-8e1db4c8fb4e` |
| `DOGE-USD` | SELL | 0.09233 | `60d899b5-20f6-418d-8d95-8e76b7fca1e2` |
| `AVAX-USD` | SELL | 7.655 | `0e0da8e9-65c3-40f9-bc10-7ca89cfec5cb` |
| `ETH-USD` | SELL | 2514.95 | `dd05ead3-9b5a-497a-ac26-256d87814b6f` |
| `ADA-USD` | SELL | 0.22067 | `1f0fb426-0404-4acc-b5d6-738ceb352479` |
| `AVAX-USD` | BUY | 7.512 | `a90a3078-8c18-4d6b-b207-68245b7a2324` |
| `AVAX-USD` | BUY | 7.512 | `0b0a69ab-0416-47aa-819d-2f2e2e8986f4` |
| `SOL-USD` | SELL | 96.84 | `ccb41d8a-3b5d-478f-890c-27e9ff3bf6fa` |
| `DOGE-USD` | SELL | 0.08954 | `28ad2247-a6db-4062-9eae-0717a7de2a77` |
| `BTC-USD` | BUY | 78836.27 | `636d1e64-94d7-4ca7-8094-2fcbe2adeee0` |
| `AVAX-USD` | BUY | 7.544 | `5a400a7a-a142-4acd-a2e1-6daa893d99cf` |
| `LINK-USD` | BUY | 11.579 | `7bbd4162-e603-4326-8b2f-a2732afb6833` |
| `ADA-USD` | SELL | 0.22045 | `d6f2afb1-f124-41a5-aa0e-df23e00b856d` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.1h ago (2026-08-24 12:54 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 12:54:26 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **149.0h (6d 4h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 12:56:08 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **148.0h (6d 3h 59m)**)
- **Selected Mega Cap Universe**: `BTC, ADA, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  09:00:05 PM
   CPU:   1.5%  |  MEM:   8.0% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2595100  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2645708  | RUNNING         | 88       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2646134  | COOL-DOWN       | 186      | Next run in 9.9s
Trader ADA-USD       | 2643962  | RUNNING         | 80       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2629364  | RUNNING         | 72       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2645567  | RUNNING         | 112      | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2645709  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 2629459  | RUNNING         | 93       | Evaluating Funnel/Polling Order
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

