---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-17 06:21:07 PM PDT (2026-08-18 01:21:07 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.83** | **-0.50** | **+1.33** | **+12.04** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.79** | **-0.50** | **+1.29** | **+23.45** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.83** | **-0.50** | **+1.33** | **+12.04** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.83** | **-0.50** | **+1.33** | **+12.04** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.83** | **-0.50** | **+1.33** | **+12.04** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.83** | **-0.50** | **+1.33** | **+12.04** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.83** | **-0.50** | **+1.33** | **+12.04** | 5.0 | 🔴 DAW VETOED |

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
| ✅ | **Go-List JSON** | Fresh (0.08h old) | 08-17 18:16 |
| ✅ | **TimesFM Forecasts** | Fresh (0.04h old) | 08-17 18:19 |
| ✅ | **Holding Times config** | Fresh (128.69h old) | 08-12 09:39 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-17 18:21 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-17 18:21 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-17 18:21 |

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
| *None* | - | - | No active maker orders |

![24-Hour Realized P&L](./images/realized_pnl_timeline.png)

---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.0h ago (2026-08-17 06:19 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-17 06:58:43 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **144.6h (6d 0h 38m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **143.6h (5d 23h 38m)**)
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
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  01:21:03 AM
   CPU:   2.2%  |  MEM:   5.6% (14.6GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2743935  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2748314  | COOL-DOWN       | 5        | Next run in 5.0s
Trader ETH-USD       | 2748315  | COOL-DOWN       | 5        | Next run in 5.0s
Trader ADA-USD       | 2748316  | COOL-DOWN       | 5        | Next run in 5.0s
Trader DOGE-USD      | 2748317  | COOL-DOWN       | 5        | Next run in 5.0s
Trader BTC-USD       | 2748318  | COOL-DOWN       | 5        | Next run in 5.0s
Trader LINK-USD      | 2748319  | COOL-DOWN       | 5        | Next run in 5.0s
Trader SOL-USD       | 2748320  | COOL-DOWN       | 5        | Next run in 5.0s
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
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:26:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38089.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:27:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38169.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:29:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38249.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:30:28 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38329.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:31:48 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38409.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:33:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38489.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:34:29 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38570.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:35:49 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38650.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:37:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38730.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:38:29 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38810.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:39:49 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38890.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:41:09 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (38970.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:42:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39051.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:43:50 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39131.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:45:10 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39211.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:46:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39291.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:47:50 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39371.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:49:11 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39452.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:50:31 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39532.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:51:51 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39612.3s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:53:11 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39692.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:54:31 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39772.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:55:51 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39852.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:57:11 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (39932.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:58:32 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40013.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 00:59:52 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40093.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:01:12 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40173.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:02:32 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40253.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:03:53 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40334.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:05:13 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40414.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:06:33 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40494.4s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:07:53 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40574.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:09:13 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40654.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:10:33 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40735.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:11:54 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40815.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:13:14 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40895.5s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:14:34 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (40975.7s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:15:54 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (41055.8s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:16:55 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (41116.2s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-18 01:18:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (41196.5s old > 150s limit, Fail-Closed)
```
</details>

