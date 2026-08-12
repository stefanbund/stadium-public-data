# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-11 09:52:53 PM PDT (2026-08-12 04:52:53 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) tracking and causal volatility gating against the promoted optimal threshold ($Z \le -0.5$).

| Symbol | Spot DVOL | 4h Rolling Z-Score | 14p RSI | Exhaustion Index | Vol Trend | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | **35.96** | **-0.11** (≤ -0.5) | 38.3 | 0/100 (< 30) | Expansion 📈 | 🔴 DAW Vetoed |
| `ETH-USD` | **49.38** | **+1.01** (≤ -0.5) | 66.2 | 20/100 (< 30) | Compression 📉 | 🔴 DAW Vetoed |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

### 📖 Volatility & VRP Safety Barometer
The system's Layer 1 DAW Causal Gate continuously gauges execution safety using **Deribit DVOL Z-Score ($Z$)** and **Variance Risk Premium (VRP)**:
- **Mathematical Principle**: $\text{VRP} = \text{IV}_{\text{Deribit DVOL}} - \text{RV}_{\text{Realized Vol}}$ and $Z = \frac{\text{DVOL}_t - \mu_{\text{4h}}}{\sigma_{\text{4h}}}$.
- **Regime Safety Spectrum**:
  - 🟢 **Safe / Compression ($Z \le -0.5$)**: Derivatives market prices low tail risk. Order books are deep, adverse selection is minimal, and TimesFM zero-shot scalps operate at peak win rates (>99%).
  - 🟡 **Transition ($-0.5 < Z < +0.5$)**: Neutral/shifting volatility; trade pacing is cautious.
  - 🔴 **Hostile / High VRP ($Z \ge +0.5$)**: Options pricing aggressive shock risk. Taker order sweeps cause adverse selection; **DAW Causality Veto is active** to preserve capital.
> **Current Live Margin of Safety**:
> - **BTC-USD**: $Z = -0.11$ (Safety Margin: **+0.39** vs. gate $-0.5$) $\rightarrow$ **🔴 DAW VETOED**
> - **ETH-USD**: $Z = +1.01$ (Safety Margin: **+1.51** vs. gate $-0.5$) $\rightarrow$ **🔴 DAW VETOED**

---
## 2. 🔒 MLOps Data Provenance & Utilization Certification: 🔴 CRITICAL SYNC/UTILIZATION FAILURE
We hereby certify that the mission-critical algorithmic data assets uploaded by the Mac Mini MLOps node have been audited for freshness, fall within their strict operational due dates, and are actively being utilized by the live EC2 HFT Trader.

✅ **Go-List JSON**: Fresh (8.25h old) - 08-11 13:38
✅ **TimesFM Forecasts**: Fresh (4.68h old) - 08-11 17:12
❌ **Holding Times config**: STALE! (13.7h old, limits 9h)
✅ **BTC DVOL Cache**: Fresh (0.00h old) - 08-11 21:52
✅ **ETH DVOL Cache**: Fresh (0.00h old) - 08-11 21:52

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 2923 recent read events).


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `121,449` | **99.5%** |
| Layer 2A: Vol Surface Skew & VRP Gate | `0` | **0.0%** |
| Layer 2B: DVOL Directional Momentum Bias | `0` | **0.0%** |
| Layer 2C: KER Efficiency Noise Filter | `0` | **0.0%** |
| Layer 2.5: TimesFM Forecast Velocity Gate | `0` | **0.0%** |
| Layer 3: SDR Liquidity Sizing Floor | `0` | **0.0%** |
| Layer 4: SFGK Commercial Margin Gate (< 0.25%) | `605` | **0.5%** |
| Layer 5: Hawkes Microstructure Toxicity | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |

![8-Stage Funnel Rejection Waterfall](./images/funnel_waterfall_breakdown.png)

### Active Universe Performance & Drift Matrix
| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 532 | 100.0% | 0 | 🟢 OK |
| `AVAX-USD` | 532 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 532 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 458 | 99.1% | 2 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

### Active Wallet Balances
| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `CBETH` | 0.9734 | 0.0000 | **0.9734** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 13260.3378 | 0.0000 | **13260.3378** |
| `DOGE` | 0.1000 | 0.0000 | **0.1000** |
| `FIL` | 0.0050 | 0.0000 | **0.0050** |
| `ALEPH` | 2.4000 | 0.0000 | **2.4000** |
| `SKL` | 0.1000 | 0.0000 | **0.1000** |
| `SAFE` | 0.1400 | 0.0000 | **0.1400** |
| `AIOZ` | 0.3000 | 0.0000 | **0.3000** |
| `BTRST` | 0.0100 | 0.0000 | **0.0100** |
| `FET` | 0.2000 | 0.0000 | **0.2000** |
| `PYR` | 0.5400 | 0.0000 | **0.5400** |
| `MPL` | 0.0005 | 0.0000 | **0.0005** |
| `MOBILE` | 0.8691 | 0.0000 | **0.8691** |
| `SHPING` | 0.7952 | 0.0000 | **0.7952** |
| `AUCTION` | 0.0002 | 0.0000 | **0.0002** |
| `LIT` | 0.0085 | 0.0000 | **0.0085** |

### Open Maker Orders on the Book
| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |

![24-Hour Realized P&L](./images/realized_pnl_timeline.png)

---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 4.7h ago (2026-08-11 05:12 PM PDT)
- **Last Weekly VSTEF Optimization**: `Never`
- **Next Scheduled VSTEF Run**: `2026-08-16 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **117.1h (4d 21h 7m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-11 10:42:12 AM PDT`
- **Next Scheduled Run**: `2026-08-16 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **116.1h (4d 20h 6m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, XRP, SOL, ZEC, HYPE, LINK, ADA, PUMP`

![TimesFM Forecast Matrix](./images/timesfm_forecast_matrix.png)

### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.
![Sweep ROI Comparison](./images/sweep_roi_comparison.png)
![Sweep Win Rate Scatter](./images/sweep_winrate_scatter.png)

---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:39:23 PM
   CPU:   0.5%  |  MEM:   6.5% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 457105   | RUNNING         | -        | Continuous Websocket Feed
Trader DOT-USD       | 494955   | COOL-DOWN       | 281      | Next run in 9.9s
Trader ETH-USD       | 494956   | COOL-DOWN       | 281      | Next run in 9.9s
Trader ADA-USD       | 494957   | COOL-DOWN       | 281      | Next run in 9.9s
Trader DOGE-USD      | 494958   | COOL-DOWN       | 281      | Next run in 9.9s
Trader BTC-USD       | 494959   | COOL-DOWN       | 281      | Next run in 9.9s
Trader LTC-USD       | 494960   | COOL-DOWN       | 281      | Next run in 9.9s
Trader SOL-USD       | 494961   | COOL-DOWN       | 281      | Next run in 9.9s
================================================================================
```

---
## 6. ⚠️ Actionable Error & Incident Radar (Last 60m)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:43:32,714 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (28936.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:44:52,998 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29017.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:46:13,564 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29097.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:47:33,983 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29178.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:48:54,535 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29258.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:50:14,949 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29338.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:51:35,418 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29419.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 04:52:55,629 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (29499.6s old > 150s limit, Fail-Closed)
```
</details>

