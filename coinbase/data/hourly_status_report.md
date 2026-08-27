---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-27 12:26:42 PM PDT (2026-08-27 19:26:42 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.18** | **-0.50** | **+0.68** | **+10.45** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.46** | **-0.50** | **+0.96** | **+26.20** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.18** | **-0.50** | **+0.68** | **+10.44** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.18** | **-0.50** | **+0.68** | **+10.45** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.18** | **-0.50** | **+0.68** | **+10.45** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.18** | **-0.50** | **+0.68** | **+10.48** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.18** | **-0.50** | **+0.68** | **+10.45** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (2.73h old) | 08-27 09:43 |
| ✅ | **TimesFM Forecasts** | Fresh (4.39h old) | 08-27 08:03 |
| ❌ | **Holding Times config** | STALE! (147.4h old) | Limit 89.4h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-27 12:26 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-27 12:26 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-27 12:26 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1580 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `3,509` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 8 | 50.0% | 0 | 🟢 OK |
| `DOGE-USD` | 4 | 50.0% | 0 | 🟢 OK |
| `ETH-USD` | 3 | 66.7% | 1 | 🟢 OK |
| `LINK-USD` | 3 | 33.3% | 2 | 🟢 OK |
| `AVAX-USD` | 6 | 50.0% | 1 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `DOGE-USD` | SELL | 0.08986 | `7310d8e3-3a32-4ed3-a7a6-281de44a71f4` |
| `ADA-USD` | SELL | 0.21673 | `1dc03db5-0c9d-4f4c-aaa3-95fedac1722f` |
| `LINK-USD` | BUY | 11.875 | `13648ed4-1d53-4640-8257-f02c3034ba20` |
| `DOGE-USD` | BUY | 0.0885 | `667692bc-89dd-4a40-894d-aa8d35dfd5c7` |
| `AVAX-USD` | BUY | 7.479 | `b1adffd8-2665-4c01-8335-fc3249d913e5` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 4.4h ago (2026-08-27 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **78.6h (3d 6h 33m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-27 09:43:18 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **77.6h (3d 5h 33m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  07:26:41 PM
   CPU:  15.1%  |  MEM:   7.2% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1845648  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1845788  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1845790  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1923685  | RUNNING         | 54       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1923686  | RUNNING         | 84       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1923687  | RUNNING         | 245      | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1923355  | RUNNING         | 233      | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1923469  | COOL-DOWN       | 262      | Next run in 9.1s
Trader LINK-USD      | 1922501  | RUNNING         | 74       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:07:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:38 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:08:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:45 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:50 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:09:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:16 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:21 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_LINK_USD.log:2026-08-27 19:10:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [LINK-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
```
</details>

