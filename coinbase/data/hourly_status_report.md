---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 08:44:34 PM PDT (2026-08-25 03:44:34 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.81** | **-0.50** | **+1.31** | **-8.23** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.24** | **-0.50** | **+1.74** | **+6.80** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.81** | **-0.50** | **+1.31** | **-7.43** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.81** | **-0.50** | **+1.31** | **-8.25** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.81** | **-0.50** | **+1.31** | **-8.19** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.81** | **-0.50** | **+1.31** | **-7.34** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.81** | **-0.50** | **+1.31** | **-8.19** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (1.46h old) | 08-24 19:16 |
| ✅ | **TimesFM Forecasts** | Fresh (4.71h old) | 08-24 16:02 |
| ✅ | **Holding Times config** | Fresh (1.47h old) | 08-24 19:16 |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-24 20:44 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-24 20:44 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-24 20:44 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1398 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `1,370` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `AVAX-USD` | 2 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 1 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.68 | `3765f8c7-8d5a-486d-af69-6f023c74f9ad` |
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `DOGE-USD` | SELL | 0.09295 | `b741e8d2-157e-4e19-8f97-4bdfa872d379` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 4.7h ago (2026-08-24 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **142.3h (5d 22h 15m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 07:16:47 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **141.3h (5d 21h 15m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  03:44:33 AM
   CPU:   2.6%  |  MEM:   7.3% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2907171  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2907224  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2907226  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2976910  | RUNNING         | 189      | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2980024  | COOL-DOWN       | 238      | Next run in 4.7s
Trader ADA-USD       | 2950852  | RUNNING         | 136      | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2972016  | RUNNING         | 174      | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2980025  | COOL-DOWN       | 256      | Next run in 4.7s
Trader LINK-USD      | 2952521  | RUNNING         | 139      | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:41:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:00 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:42:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:43:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-25 03:44:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1007] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
```
</details>

