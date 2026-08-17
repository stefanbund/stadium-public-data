---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-17 02:38:59 PM PDT (2026-08-17 21:38:59 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `74.2%` | **Completed Trades**: `89`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.31** | **-0.50** | **+1.81** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.89** | **-0.50** | **+1.39** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.31** | **-0.50** | **+1.81** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.31** | **-0.50** | **+1.81** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.31** | **-0.50** | **+1.81** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.31** | **-0.50** | **+1.81** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.31** | **-0.50** | **+1.81** | **N/A** | 5.0 | 🔴 DAW VETOED |

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
| ✅ | **Go-List JSON** | Fresh (7.70h old) | 08-17 06:57 |
| ✅ | **TimesFM Forecasts** | Fresh (6.60h old) | 08-17 08:03 |
| ✅ | **Holding Times config** | Fresh (124.99h old) | 08-12 09:39 |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-17 14:38 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-17 14:38 |
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

- **TimesFM Forecast DB**: 🟢 Updated 6.6h ago (2026-08-17 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-17 06:58:43 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **148.3h (6d 4h 20m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **147.3h (6d 3h 20m)**)
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
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  09:38:56 PM
   CPU:   3.2%  |  MEM:   8.3% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2486652  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2568483  | RUNNING         | 78       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2568484  | RUNNING         | 78       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2568485  | RUNNING         | 78       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2568486  | RUNNING         | 78       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2568487  | RUNNING         | 78       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2568488  | RUNNING         | 78       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 2568489  | RUNNING         | 78       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:46:21 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (24882.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:47:41 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (24962.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:49:01 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25042.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:50:21 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25122.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:51:41 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25203.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:53:02 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25283.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:54:22 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25363.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:55:42 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25443.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:57:02 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25523.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:58:22 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25603.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 20:59:43 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25684.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:01:03 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25764.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:02:23 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25844.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:03:43 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (25924.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:05:03 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26004.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:06:24 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26085.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:07:44 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26165.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:09:04 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26245.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:10:24 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26325.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:11:44 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26405.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:13:05 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26486.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:14:25 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26566.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:15:45 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26646.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:17:05 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26726.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:18:25 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26806.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:19:45 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26886.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:21:06 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (26967.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:22:25 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27047.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:23:46 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27127.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:25:06 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27207.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:26:26 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27287.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:27:46 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27367.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:29:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27448.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:30:27 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27528.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:31:47 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27608.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:33:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27688.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:34:27 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27768.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:35:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27849.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:37:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (27929.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 21:38:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (28009.5s old > 150s limit, Fail-Closed)
```
</details>

