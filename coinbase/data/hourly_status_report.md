---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-18 08:08:34 AM PDT (2026-08-18 15:08:34 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.92** | **-0.50** | **+1.42** | **+5.05** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-0.88** | **-0.50** | **-0.38** | **+22.59** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.92** | **-0.50** | **+1.42** | **+11.48** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.92** | **-0.50** | **+1.42** | **+5.05** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.92** | **-0.50** | **+1.42** | **+5.05** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.92** | **-0.50** | **+1.42** | **+11.48** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.92** | **-0.50** | **+1.42** | **+11.48** | 5.0 | 🔴 DAW VETOED |

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
## 2. 🔒 MLOps & Trading Telemetry Provenance & Utilization Certification: 🔴 CRITICAL SYNC/UTILIZATION FAILURE
We hereby certify that the mission-critical algorithmic data assets uploaded by the Mac Mini MLOps node have been audited for freshness, fall within their strict operational due dates, and are actively being utilized by the live EC2 HFT Trader.

| Status | Data Asset | Freshness / State | Details / Timestamp |
| :---: | :--- | :--- | :--- |
| ✅ | **Go-List JSON** | Fresh (13.63h old) | 08-17 18:31 |
| ✅ | **TimesFM Forecasts** | Fresh (0.11h old) | 08-18 08:02 |
| ✅ | **Holding Times config** | Fresh (13.40h old) | 08-17 18:45 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-18 08:08 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-18 08:08 |
| ❌ | **Live Trading Telemetry** | STALE! (0.7h old) | Limit 0.05h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `0` | **0.0%** |
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


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |

![24-Hour Realized P&L](./images/realized_pnl_timeline.png)

---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.1h ago (2026-08-18 08:02 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-17 06:44:25 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **130.9h (5d 10h 51m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **129.9h (5d 9h 51m)**)
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
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  03:08:30 PM
   CPU:   2.9%  |  MEM:   6.8% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3315631  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 3379025  | RUNNING         | 206      | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3411196  | COOL-DOWN       | 318      | Next run in 4.6s
Trader ADA-USD       | 3411210  | COOL-DOWN       | 308      | Next run in 9.7s
Trader DOGE-USD      | 3379028  | RUNNING         | 206      | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3379029  | RUNNING         | 206      | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3411197  | COOL-DOWN       | 313      | Next run in 4.6s
Trader SOL-USD       | 3411268  | RUNNING         | 315      | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:35:26 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2117.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:36:43 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2194.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:38:01 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2272.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:39:19 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2350.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:40:36 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2427.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:41:54 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2505.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:43:11 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2582.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:44:29 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2660.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:45:46 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2737.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:47:04 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2815.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:48:21 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2892.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:49:38 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2969.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:50:56 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3047.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:52:13 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3124.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:53:31 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3202.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:54:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3279.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:56:05 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3356.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:57:23 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3434.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:58:40 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3511.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 09:59:58 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3589.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:01:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3666.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:02:32 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3743.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:03:50 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3821.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:05:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3898.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:06:25 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (3976.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:07:42 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4053.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:08:59 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4130.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:10:17 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4208.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:11:34 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4285.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:12:51 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4362.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:14:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4440.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:15:26 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4517.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:16:43 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4594.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:18:00 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4671.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:19:18 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4749.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:20:35 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4826.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:21:52 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4903.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:23:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (4980.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:24:27 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (5058.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 10:25:44 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (5135.3s old > 150s limit, Fail-Closed)
```
</details>

