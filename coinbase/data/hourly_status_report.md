# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-12 10:55:55 PM PDT (2026-08-13 05:55:55 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) tracking and causal volatility gating against the promoted optimal threshold ($Z \le -0.5$).

| Symbol | Spot DVOL | 4h Rolling Z-Score | 14p RSI | Exhaustion Index | Vol Trend | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | **35.58** | **-1.67** (≤ -0.5) | 22.6 | 0/100 (< 30) | Expansion 📈 | 🟢 Approved |
| `ETH-USD` | **49.52** | **+0.07** (≤ -0.5) | 82.2 | 40/100 (< 30) | Expansion 📈 | 🔴 DAW Vetoed |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

### 📖 Volatility & VRP Safety Barometer
The system's Layer 1 DAW Causal Gate continuously gauges execution safety using **Deribit DVOL Z-Score ($Z$)** and **Variance Risk Premium (VRP)**:
- **Mathematical Principle**: $\text{VRP} = \text{IV}_{\text{Deribit DVOL}} - \text{RV}_{\text{Realized Vol}}$ and $Z = \frac{\text{DVOL}_t - \mu_{\text{4h}}}{\sigma_{\text{4h}}}$.
- **Regime Safety Spectrum**:
  - 🟢 **Safe / Compression ($Z \le -0.5$)**: Derivatives market prices low tail risk. Order books are deep, adverse selection is minimal, and TimesFM zero-shot scalps operate at peak win rates (>99%).
  - 🟡 **Transition ($-0.5 < Z < +0.5$)**: Neutral/shifting volatility; trade pacing is cautious.
  - 🔴 **Hostile / High VRP ($Z \ge +0.5$)**: Options pricing aggressive shock risk. Taker order sweeps cause adverse selection; **DAW Causality Veto is active** to preserve capital.
> **Current Live Margin of Safety**:
> - **BTC-USD**: $Z = -1.67$ (Safety Margin: **-1.17** vs. gate $-0.5$) $\rightarrow$ **🟢 SAFE / COMPRESSED**
> - **ETH-USD**: $Z = +0.07$ (Safety Margin: **+0.57** vs. gate $-0.5$) $\rightarrow$ **🔴 DAW VETOED**

---
## 2. 🔒 MLOps & Trading Telemetry Provenance & Utilization Certification: 🟢 ALL SYNCED & CERTIFIED
We hereby certify that the mission-critical algorithmic data assets uploaded by the Mac Mini MLOps node have been audited for freshness, fall within their strict operational due dates, and are actively being utilized by the live EC2 HFT Trader.

| Status | Data Asset | Freshness / State | Details / Timestamp |
| :---: | :--- | :--- | :--- |
| ✅ | **Go-List JSON** | Fresh (9.58h old) | 08-12 13:21 |
| ✅ | **TimesFM Forecasts** | Fresh (5.70h old) | 08-12 17:13 |
| ✅ | **Holding Times config** | Fresh (13.27h old) | 08-12 09:39 |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-12 22:55 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-12 22:55 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-12 22:56 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1946 recent read events).


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `123,211` | **99.5%** |
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

- **TimesFM Forecast DB**: 🟢 Updated 5.7h ago (2026-08-12 05:13 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-12 01:22:32 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-16 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **92.1h (3d 20h 4m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-12 02:28:22 PM PDT`
- **Next Scheduled Run**: `2026-08-16 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **91.1h (3d 19h 3m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, LSETH, LINK, UNI, XRP, SOL, ZEC`

![TimesFM Forecast Matrix](./images/timesfm_forecast_matrix.png)

### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.
![Sweep ROI Comparison](./images/sweep_roi_comparison.png)
![Sweep Win Rate Scatter](./images/sweep_winrate_scatter.png)

---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:55:52 AM
   CPU:  45.5%  |  MEM:   7.2% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 815328   | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 905045   | COOL-DOWN       | 303      | Next run in 14.9s
Trader ETH-USD       | 905046   | COOL-DOWN       | 303      | Next run in 14.9s
Trader ADA-USD       | 905047   | COOL-DOWN       | 303      | Next run in 14.9s
Trader DOGE-USD      | 905048   | COOL-DOWN       | 303      | Next run in 14.9s
Trader BTC-USD       | 905049   | COOL-DOWN       | 303      | Next run in 14.9s
Trader LINK-USD      | 905050   | COOL-DOWN       | 303      | Next run in 14.9s
Trader SOL-USD       | 905051   | COOL-DOWN       | 303      | Next run in 14.9s
================================================================================
```

---
## 6. ⚠️ Actionable Error & Incident Radar (Last 60m)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
No critical errors in current window.
```
</details>

