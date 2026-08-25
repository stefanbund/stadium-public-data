---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-25 12:08:01 AM PDT (2026-08-25 07:08:01 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.07** | **-0.50** | **+0.43** | **-4.84** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.36** | **-0.50** | **+0.86** | **+9.74** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.07** | **-0.50** | **+0.43** | **-5.10** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.07** | **-0.50** | **+0.43** | **-4.84** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.07** | **-0.50** | **+0.43** | **-4.84** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.07** | **-0.50** | **+0.43** | **-5.22** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.07** | **-0.50** | **+0.43** | **-4.84** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (4.86h old) | 08-24 19:16 |
| ✅ | **TimesFM Forecasts** | Fresh (0.10h old) | 08-25 00:01 |
| ❌ | **Holding Times config** | STALE! (87.1h old) | Limit 29.1h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-25 00:07 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-25 00:08 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-25 00:07 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 2000 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `3,981` | **100.0%** |
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
| `DOGE-USD` | 3 | 66.7% | 0 | 🟢 OK |
| `LINK-USD` | 5 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `ADA-USD` | SELL | 0.22728 | `bf03c112-f8fa-4a59-8cb1-e0b98a5b8ac2` |
| `LINK-USD` | SELL | 11.809 | `8a7d2ebb-36f1-4abc-9889-2c85b18118f4` |
| `ETH-USD` | SELL | 2512.32 | `fbc1490b-4d58-459c-93f6-eb6dce1d28a9` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.1h ago (2026-08-25 12:01 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **138.9h (5d 18h 51m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 07:16:47 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **137.9h (5d 17h 51m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  07:07:58 AM
   CPU:  19.9%  |  MEM:   7.9% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3084610  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3084662  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 3084664  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3151171  | RUNNING         | 197      | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3119671  | RUNNING         | 109      | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3114924  | RUNNING         | 70       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3151172  | RUNNING         | 137      | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3151173  | RUNNING         | 220      | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3120195  | RUNNING         | 94       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:04:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:04:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:04:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:04:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:05:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:06:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:00 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:07:57 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 07:08:02 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

