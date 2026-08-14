# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-13 07:12:01 PM PDT (2026-08-14 02:12:01 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-2.09** | **-0.50** | **-1.59** | **+14.48** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.40** | **-0.50** | **-0.90** | **+28.34** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-2.09** | **-0.50** | **-1.59** | **+14.48** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-2.09** | **-0.50** | **-1.59** | **+14.48** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-2.09** | **-0.50** | **-1.59** | **+14.48** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-2.09** | **-0.50** | **-1.59** | **+14.48** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-2.09** | **-0.50** | **-1.59** | **+14.48** | 5.0 | 🔴 DAW VETOED |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

![VRP Chart AVAX-USD](./images/vrp_chart_AVAX-USD.png)  

![VRP Chart ETH-USD](./images/vrp_chart_ETH-USD.png)  

![VRP Chart ADA-USD](./images/vrp_chart_ADA-USD.png)  

![VRP Chart DOGE-USD](./images/vrp_chart_DOGE-USD.png)  

![VRP Chart BTC-USD](./images/vrp_chart_BTC-USD.png)  

![VRP Chart LINK-USD](./images/vrp_chart_LINK-USD.png)  

![VRP Chart SOL-USD](./images/vrp_chart_SOL-USD.png)  

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
| ✅ | **Go-List JSON** | Fresh (12.06h old) | 08-13 07:08 |
| ✅ | **TimesFM Forecasts** | Fresh (3.17h old) | 08-13 16:02 |
| ✅ | **Holding Times config** | Fresh (33.54h old) | 08-12 09:39 |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-13 19:11 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-13 19:11 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-13 19:12 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 196 recent read events).


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `189` | **100.0%** |
| Layer 2A: Vol Surface Skew & VRP Gate | `0` | **0.0%** |
| Layer 2B: DVOL Directional Momentum Bias | `0` | **0.0%** |
| Layer 2C: KER Efficiency Noise Filter | `0` | **0.0%** |
| Layer 2.5: TimesFM Forecast Velocity Gate | `0` | **0.0%** |
| Layer 3: SDR Liquidity Sizing Floor | `0` | **0.0%** |
| Layer 4: SFGK Commercial Margin Gate (< 0.25%) | `0` | **0.0%** |
| Layer 5: Hawkes Microstructure Toxicity | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |

![8-Stage Funnel Rejection Waterfall](./images/funnel_waterfall_breakdown.png)

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
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.2h ago (2026-08-13 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-12 01:22:32 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-16 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **71.8h (2d 23h 47m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-16 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **70.8h (2d 22h 47m)**)
- **Selected Mega Cap Universe**: `Could not fetch active universe from EC2`

![TimesFM Forecast Matrix](./images/timesfm_forecast_matrix.png)

### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.
![Sweep ROI Comparison](./images/sweep_roi_comparison.png)
![Sweep Win Rate Scatter](./images/sweep_winrate_scatter.png)

---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  02:11:58 AM
   CPU:   2.4%  |  MEM:   5.9% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1974424  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1982094  | COOL-DOWN       | 26       | Next run in 10.0s
Trader ETH-USD       | 1982095  | COOL-DOWN       | 26       | Next run in 10.0s
Trader ADA-USD       | 1982096  | COOL-DOWN       | 26       | Next run in 10.0s
Trader DOGE-USD      | 1982097  | COOL-DOWN       | 26       | Next run in 10.0s
Trader BTC-USD       | 1982098  | COOL-DOWN       | 26       | Next run in 10.0s
Trader LINK-USD      | 1982099  | COOL-DOWN       | 26       | Next run in 10.0s
Trader SOL-USD       | 1982100  | COOL-DOWN       | 26       | Next run in 10.0s
================================================================================
```

---
## 6. ☀️ Mac Mini Day Trader Intelligence
**Day Trader Watchdog Status**: 🟢 ONLINE

Error reading recommendations: name 'pd' is not defined

---
## 7. ⚠️ Actionable Error & Incident Radar (Last 10h)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
No critical errors in current window.
```
</details>

