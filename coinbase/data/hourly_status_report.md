---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-27 07:48:59 AM PDT (2026-08-27 14:48:59 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.01** | **-0.50** | **+1.51** | **+7.19** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.01** | **-0.50** | **+1.51** | **+22.67** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.01** | **-0.50** | **+1.51** | **+7.38** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.01** | **-0.50** | **+1.51** | **+7.38** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.01** | **-0.50** | **+1.51** | **+7.19** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.01** | **-0.50** | **+1.51** | **+7.19** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.01** | **-0.50** | **+1.51** | **+7.19** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (0.03h old) | 08-27 07:47 |
| ✅ | **TimesFM Forecasts** | Fresh (2.96h old) | 08-27 04:51 |
| ✅ | **Holding Times config** | Fresh (0.04h old) | 08-27 07:47 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-27 07:48 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-27 07:49 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-27 07:48 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 19 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `17` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USDC` | SELL | 1.0001 | `a69d9998-a1ee-4622-87af-a15bb8d32eaf` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `ADA-USD` | SELL | 0.22503 | `eb72afdd-a3d7-40b8-9598-30b5ca2b74ef` |
| `DOGE-USD` | SELL | 0.09237 | `3160f212-8ff6-4b19-a291-73c17cdf2a97` |
| `AVAX-USD` | SELL | 7.625 | `c14c3c5a-f35f-4043-a616-ea4c20cfa9f2` |
| `DOGE-USD` | SELL | 0.09132 | `2f2ed9b7-454b-4377-9672-5f4c78c84b1e` |
| `ADA-USD` | SELL | 0.22031 | `d968b8ef-1180-4f05-bc11-01087aa5d99a` |
| `AVAX-USD` | SELL | 7.558 | `fc9234ee-6ef0-4ba3-a44b-d86922f91144` |
| `ADA-USD` | BUY | 0.21542 | `3f6a76a8-6d1c-4cf7-9bc4-cf2569c550dd` |
| `DOGE-USD` | BUY | 0.08883 | `40413234-8894-4b5a-8282-bb2b347291e1` |
| `AVAX-USD` | SELL | 7.545 | `46894ef5-9c30-483c-8fba-7143dff35b0f` |
| `USDT-USDC` | BUY | 0.9999 | `139f6fff-865f-4613-a73b-09a86aa9ae35` |
| `USDT-USDC` | BUY | 0.9999 | `dc6294da-3394-4484-91c1-d5bb7f6e619c` |
| `USDT-USDC` | BUY | 0.9999 | `1f304da6-718c-43b1-996d-93e08631dbcb` |
| `USDT-USDC` | BUY | 0.9999 | `10b90f3e-2aaa-48cc-b927-55a94fc3b26a` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.0h ago (2026-08-27 04:51 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **83.2h (3d 11h 10m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-27 07:47:00 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **82.2h (3d 10h 10m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  02:48:55 PM
   CPU:   5.1%  |  MEM:   6.4% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1689300  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1689352  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1689354  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1690091  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1690092  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1689903  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1689904  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1690093  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1690094  | RUNNING         | 2        | Evaluating Funnel/Polling Order
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

