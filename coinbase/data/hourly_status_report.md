---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-17 07:34:13 AM PDT (2026-08-17 14:34:13 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `74.2%` | **Completed Trades**: `89`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.32** | **-0.50** | **+0.18** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-0.40** | **-0.50** | **+0.10** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.32** | **-0.50** | **+0.18** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.32** | **-0.50** | **+0.18** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.32** | **-0.50** | **+0.18** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.32** | **-0.50** | **+0.18** | **N/A** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.32** | **-0.50** | **+0.18** | **N/A** | 5.0 | 🔴 DAW VETOED |

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
| ✅ | **Go-List JSON** | Fresh (0.62h old) | 08-17 06:57 |
| ✅ | **TimesFM Forecasts** | Fresh (0.59h old) | 08-17 06:58 |
| ✅ | **Holding Times config** | Fresh (0.59h old) | 08-17 06:59 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-17 07:34 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-17 07:34 |
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

- **TimesFM Forecast DB**: 🟢 Updated 0.6h ago (2026-08-17 06:58 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-17 06:58:43 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **155.4h (6d 11h 25m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **154.4h (6d 10h 25m)**)
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
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  02:34:12 PM
   CPU:   3.6%  |  MEM:   8.2% (14.1GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2205398  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2231288  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2231289  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2231290  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2231291  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2231292  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2231293  | RUNNING         | 24       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 2231294  | RUNNING         | 24       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:14:47 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1388.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:16:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1468.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:17:27 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1548.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:18:47 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1629.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:20:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1709.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:21:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1789.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:22:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1869.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:24:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (1949.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:25:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2029.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:26:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2109.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:28:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2190.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:29:29 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2270.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:30:49 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2350.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:32:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2430.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-17 14:33:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (2511.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:01:25 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (586.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:02:45 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (666.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:04:06 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (747.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:05:26 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (827.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:06:45 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (907.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:08:06 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (987.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:09:26 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1067.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:10:46 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1147.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:12:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1228.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:13:27 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1308.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:14:47 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1388.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:16:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1468.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:17:27 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1548.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:18:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1629.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:20:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1709.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:21:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1789.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:22:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1869.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:24:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (1949.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:25:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2029.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:26:49 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2110.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:28:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2190.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:29:29 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2270.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:30:49 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2350.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:32:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2430.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-17 14:33:29 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (2511.0s old > 150s limit, Fail-Closed)
```
</details>

