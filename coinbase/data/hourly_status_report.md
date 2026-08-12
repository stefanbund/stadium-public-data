# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-11 05:17:55 PM PDT (2026-08-12 00:17:55 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) tracking and causal volatility gating against the promoted optimal threshold ($Z \le -0.5$).

| Symbol | Spot DVOL | 4h Rolling Z-Score | 14p RSI | Exhaustion Index | Vol Trend | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | **36.20** | **+2.17** (≤ -0.5) | 68.8 | 40/100 (< 30) | Expansion 📈 | 🔴 DAW Vetoed |
| `ETH-USD` | **49.25** | **-0.71** (≤ -0.5) | 31.7 | 20/100 (< 30) | Compression 📉 | 🟢 Approved |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

### 📖 Volatility & VRP Safety Barometer
The system's Layer 1 DAW Causal Gate continuously gauges execution safety using **Deribit DVOL Z-Score ($Z$)** and **Variance Risk Premium (VRP)**:
- **Mathematical Principle**: $\text{VRP} = \text{IV}_{\text{Deribit DVOL}} - \text{RV}_{\text{Realized Vol}}$ and $Z = \frac{\text{DVOL}_t - \mu_{\text{4h}}}{\sigma_{\text{4h}}}$.
- **Regime Safety Spectrum**:
  - 🟢 **Safe / Compression ($Z \le -0.5$)**: Derivatives market prices low tail risk. Order books are deep, adverse selection is minimal, and TimesFM zero-shot scalps operate at peak win rates (>99%).
  - 🟡 **Transition ($-0.5 < Z < +0.5$)**: Neutral/shifting volatility; trade pacing is cautious.
  - 🔴 **Hostile / High VRP ($Z \ge +0.5$)**: Options pricing aggressive shock risk. Taker order sweeps cause adverse selection; **DAW Causality Veto is active** to preserve capital.
> **Current Live Margin of Safety**:
> - **BTC-USD**: $Z = +2.17$ (Safety Margin: **+2.67** vs. gate $-0.5$) $\rightarrow$ **🔴 DAW VETOED**
> - **ETH-USD**: $Z = -0.71$ (Safety Margin: **-0.21** vs. gate $-0.5$) $\rightarrow$ **🟢 SAFE / COMPRESSED**

---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `121,463` | **99.5%** |
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
| `USD` | 0.00 | 0.00 | **0.00** |

### Open Maker Orders on the Book
| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| *None* | - | - | No active maker orders |

![24-Hour Realized P&L](./images/realized_pnl_timeline.png)

---
## 4. 🤖 Foundation Model MLOps & TimesFM 2.0
Zero-shot multi-step forward return forecasts and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.1h ago (2026-08-11 05:12 PM PDT)
- **Last Weekly VSTEF Optimization**: `Never`
- **Next Scheduled VSTEF Run**: `2026-08-16 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **121.7h (5d 1h 42m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

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
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:16:45,503 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (366.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:16:45,503 - ERROR - [SOL-USD] Dependency check failed in fetch_live_state. Aborting cycle.
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:17:05,610 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (386.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:17:05,610 - ERROR - [SOL-USD] Dependency check failed in fetch_live_state. Aborting cycle.
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:17:25,987 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (407.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:17:25,987 - ERROR - [SOL-USD] Dependency check failed in fetch_live_state. Aborting cycle.
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:17:46,079 - ERROR - [SOL-USD] CRITICAL: DVOL cache is stale (427.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-12 00:17:46,080 - ERROR - [SOL-USD] Dependency check failed in fetch_live_state. Aborting cycle.
```
</details>

