---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 10:55:14 PM PDT (2026-08-25 05:55:14 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.17** | **-0.50** | **+1.67** | **-8.42** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.91** | **-0.50** | **+1.41** | **+6.14** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.17** | **-0.50** | **+1.67** | **-8.50** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.17** | **-0.50** | **+1.67** | **-8.61** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.17** | **-0.50** | **+1.67** | **-8.42** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.17** | **-0.50** | **+1.67** | **-8.42** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.17** | **-0.50** | **+1.67** | **-8.42** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (3.64h old) | 08-24 19:16 |
| ✅ | **TimesFM Forecasts** | Fresh (2.08h old) | 08-24 20:50 |
| ❌ | **Holding Times config** | STALE! (85.9h old) | Limit 27.9h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 22:55 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 22:55 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-24 22:55 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1886 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `3,033` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `ETH-USD` | 2 | 100.0% | 0 | 🟢 OK |
| `AVAX-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 2 | 50.0% | 1 | 🟢 OK |
| `LINK-USD` | 5 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `ADA-USD` | BUY | 0.22722 | `c0fa761b-c5c1-40d9-aec6-6c02c1afa2bf` |
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `DOGE-USD` | BUY | 0.09272 | `cc9a1aae-209e-4754-99fc-1b73f09ec6f7` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 2.1h ago (2026-08-24 08:50 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **140.1h (5d 20h 4m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 07:16:47 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **139.1h (5d 19h 4m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:55:14 AM
   CPU:   1.9%  |  MEM:   6.5% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3084610  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3084662  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 3084664  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3089729  | COOL-DOWN       | 11       | Next run in 4.0s
Trader ETH-USD       | 3089730  | COOL-DOWN       | 11       | Next run in 4.0s
Trader ADA-USD       | 3089731  | RUNNING         | 11       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3088845  | RUNNING         | 8        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3089840  | COOL-DOWN       | 17       | Next run in 9.6s
Trader LINK-USD      | 3089732  | COOL-DOWN       | 11       | Next run in 4.0s
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
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:22:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:22:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:50 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:23:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:00 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:24:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:25:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:26:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:26:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 05:26:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

