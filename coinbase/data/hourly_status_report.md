# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-17 06:40:24 AM PDT (2026-08-17 13:40:24 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.51** | **-0.50** | **-0.01** | **+16.16** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-0.19** | **-0.50** | **+0.31** | **+27.80** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.51** | **-0.50** | **-0.01** | **+16.16** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.51** | **-0.50** | **-0.01** | **+16.16** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.51** | **-0.50** | **-0.01** | **+16.16** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.51** | **-0.50** | **-0.01** | **+16.16** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.51** | **-0.50** | **-0.01** | **+16.16** | 5.0 | 🔴 DAW VETOED |

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
| ✅ | **Go-List JSON** | Fresh (5.65h old) | 08-17 01:01 |
| ✅ | **TimesFM Forecasts** | Fresh (1.99h old) | 08-17 04:41 |
| ✅ | **Holding Times config** | Fresh (5.45h old) | 08-17 01:13 |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-17 06:40 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-17 06:40 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-17 06:40 |

<br>

> **Utilization Certification**: 🔴 **FAILED.** Guardian watchdog offline, unable to certify utilization.


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `72,153` | **100.0%** |
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

- **TimesFM Forecast DB**: 🟢 Updated 2.0h ago (2026-08-17 04:41 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-17 01:13:06 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-23 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **156.3h (6d 12h 19m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `Never`
- **Next Scheduled Run**: `2026-08-23 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **155.3h (6d 11h 19m)**)
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
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  01:40:24 PM
   CPU:   5.3%  |  MEM:   5.4% (14.6GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2079086  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2182955  | COOL-DOWN       | 337      | Next run in 9.7s
Trader ETH-USD       | 2182956  | COOL-DOWN       | 337      | Next run in 9.7s
Trader ADA-USD       | 2182957  | COOL-DOWN       | 337      | Next run in 9.7s
Trader DOGE-USD      | 2182958  | COOL-DOWN       | 337      | Next run in 9.7s
Trader BTC-USD       | 2182959  | COOL-DOWN       | 337      | Next run in 9.7s
Trader LINK-USD      | 2182960  | COOL-DOWN       | 337      | Next run in 9.7s
Trader SOL-USD       | 2182962  | COOL-DOWN       | 337      | Next run in 9.7s
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
logs/watchdog_Trader_ADA_USD.log:2026-08-16 09:26:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [ADA-USD] CRITICAL: DVOL cache is stale (151.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_ADA_USD.log:2026-08-16 14:40:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:485] [ADA-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 343) (Fail-Closed)
logs/watchdog_Trader_ADA_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_ADA_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 343)
logs/watchdog_Trader_AVAX_USD.log:2026-08-16 09:26:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [AVAX-USD] CRITICAL: DVOL cache is stale (151.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_AVAX_USD.log:2026-08-16 14:40:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:485] [AVAX-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 343) (Fail-Closed)
logs/watchdog_Trader_AVAX_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_AVAX_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 343)
logs/watchdog_Trader_BTC_USD.log:2026-08-16 09:26:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [BTC-USD] CRITICAL: DVOL cache is stale (152.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_BTC_USD.log:2026-08-16 14:40:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:485] [BTC-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 343) (Fail-Closed)
logs/watchdog_Trader_BTC_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_BTC_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 343)
logs/watchdog_Trader_DOGE_USD.log:2026-08-16 09:26:31 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [DOGE-USD] CRITICAL: DVOL cache is stale (152.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_DOGE_USD.log:2026-08-16 14:40:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:485] [DOGE-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 343) (Fail-Closed)
logs/watchdog_Trader_DOGE_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_DOGE_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 343)
logs/watchdog_Trader_ETH_USD.log:2026-08-16 09:26:31 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [ETH-USD] CRITICAL: DVOL cache is stale (152.0s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-16 09:26:31 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [LINK-USD] CRITICAL: DVOL cache is stale (152.1s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:2026-08-16 14:40:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:485] [LINK-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 343) (Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_LINK_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 343)
logs/watchdog_Trader_SOL_USD.log:2026-08-16 09:26:30 [ERROR] [async_sfgk_trader.py:fetch_live_state:469] [SOL-USD] CRITICAL: DVOL cache is stale (151.9s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-08-16 14:40:08 [ERROR] [async_sfgk_trader.py:fetch_live_state:485] [SOL-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 343) (Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_SOL_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 343)
```
</details>

