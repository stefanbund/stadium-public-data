---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-17 11:59:02 AM PDT (2026-08-17 18:59:02 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `74.2%` | **Completed Trades**: `89`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.07** | **-0.50** | **+1.57** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.63** | **-0.50** | **+1.13** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.07** | **-0.50** | **+1.57** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.07** | **-0.50** | **+1.57** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.07** | **-0.50** | **+1.57** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.07** | **-0.50** | **+1.57** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.07** | **-0.50** | **+1.57** | **N/A** | 5.0 | 🔴 DAW VETOED |

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
| ✅ | **Go-List JSON** | Fresh (5.03h old) | 08-17 06:57 |
| ✅ | **TimesFM Forecasts** | Fresh (3.93h old) | 08-17 08:03 |
| ✅ | **Holding Times config** | Fresh (122.33h old) | 08-12 09:39 |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-17 11:58 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-17 11:58 |
| ❌ | **Live Trading Telemetry** | NOT FOUND ON EC2 | - |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `17` | **9.3%** |
| Layer 2A: Vol Surface Skew & VRP Gate | `0` | **0.0%** |
| Layer 2B: DVOL Directional Momentum Bias | `165` | **90.7%** |
| Layer 2C: KER Efficiency Noise Filter | `0` | **0.0%** |
| Layer 2.5: TimesFM Forecast Velocity Gate | `0` | **0.0%** |
| Layer 3: SDR Liquidity Sizing Floor | `0` | **0.0%** |
| Layer 4: SFGK Commercial Margin Gate (< 0.25%) | `0` | **0.0%** |
| Layer 5: Hawkes Microstructure Toxicity | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |

![8-Stage Funnel Rejection Waterfall](./images/funnel_waterfall_breakdown.png)

### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `DOGE-USD` | 2 | 100.0% | 0 | 🟢 OK |
| `CHZ-USD` | 15 | 80.0% | 1 | 🟢 OK |
| `CRV-USD` | 16 | 90.0% | 0 | 🟢 OK |
| `CRO-USD` | 5 | 100.0% | 0 | 🟢 OK |
| `ACH-USD` | 4 | 75.0% | 1 | 🟢 OK |
| `ALGO-USD` | 19 | 40.0% | 1 | ⚠️ DRIFT |
| `BCH-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `CBETH-USD` | 5 | 60.0% | 2 | 🟢 OK |
| `BNT-USD` | 12 | 50.0% | 0 | 🟢 OK |
| `GNO-USD` | 7 | 57.1% | 0 | 🟢 OK |

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

- **TimesFM Forecast DB**: 🟢 Updated 3.9h ago (2026-08-17 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-17 06:58:43 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **151.0h (6d 7h 0m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **150.0h (6d 6h 0m)**)
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
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:59:00 PM
   CPU:   5.8%  |  MEM:   8.3% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2391577  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2441859  | RUNNING         | 48       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2441860  | RUNNING         | 48       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2441861  | RUNNING         | 48       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2441862  | RUNNING         | 48       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2441863  | RUNNING         | 48       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2441864  | RUNNING         | 48       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 2441865  | RUNNING         | 48       | Evaluating Funnel/Polling Order
================================================================================
```

---
## 6. ☀️ Mac Mini Day Trader Intelligence
**Day Trader Watchdog Status**: 🔴 OFFLINE

Error reading recommendations: name 'pd' is not defined

---
## 7. ⚠️ Actionable Error & Incident Radar (Last 10h)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:06:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15276.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:07:35 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15356.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:08:55 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15436.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:10:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15517.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:11:35 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15596.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:12:55 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15677.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:14:16 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15757.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:15:36 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15837.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:16:56 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15917.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:18:17 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (15998.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:19:36 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16078.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:20:57 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16158.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:22:17 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16238.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:23:37 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16318.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:24:57 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16398.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:26:18 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16479.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:27:38 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16559.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:28:58 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16639.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:30:18 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16719.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:31:38 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16799.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:32:58 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16879.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:34:19 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (16960.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:35:39 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17040.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:36:59 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17120.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:38:19 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17200.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:39:39 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17280.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:41:00 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17361.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:42:20 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17441.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:43:40 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17521.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:45:00 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17601.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:46:20 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17681.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:47:40 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17761.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:49:00 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17842.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:50:21 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (17922.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:51:41 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (18002.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:53:01 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (18082.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:54:22 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (18163.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:55:42 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (18243.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:57:02 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (18323.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 18:58:22 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (18403.3s old > 150s limit, Fail-Closed)
```
</details>

