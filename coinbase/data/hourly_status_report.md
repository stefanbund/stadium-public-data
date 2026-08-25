---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 09:21:53 PM PDT (2026-08-25 04:21:53 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.03** | **-0.50** | **+1.53** | **-8.62** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.31** | **-0.50** | **+1.81** | **+6.30** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.03** | **-0.50** | **+1.53** | **-8.58** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.03** | **-0.50** | **+1.53** | **-8.38** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.03** | **-0.50** | **+1.53** | **-8.58** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.03** | **-0.50** | **+1.53** | **-8.62** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.03** | **-0.50** | **+1.53** | **-8.58** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (2.09h old) | 08-24 19:16 |
| ✅ | **TimesFM Forecasts** | Fresh (0.52h old) | 08-24 20:50 |
| ❌ | **Holding Times config** | STALE! (84.3h old) | Limit 26.4h |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-24 21:21 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-24 21:21 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-24 21:21 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1867 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `1,835` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 2 | 100.0% | 0 | 🟢 OK |
| `AVAX-USD` | 3 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 3 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.68 | `3765f8c7-8d5a-486d-af69-6f023c74f9ad` |
| `DOGE-USD` | SELL | 0.09228 | `96b978c0-84a5-4644-a422-0faedfd41c0c` |
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `DOGE-USD` | SELL | 0.09295 | `b741e8d2-157e-4e19-8f97-4bdfa872d379` |
| `ETH-USD` | SELL | 2504.4 | `a76f1413-22b8-440d-97bc-7313b6306a21` |
| `LINK-USD` | BUY | 11.699 | `c44f4a8c-7f1b-4441-9486-6551ebdea107` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.5h ago (2026-08-24 08:50 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **141.6h (5d 21h 38m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 07:16:47 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **140.6h (5d 20h 37m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  04:21:50 AM
   CPU:  10.2%  |  MEM:   6.3% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2984354  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2984430  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2984432  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3011977  | COOL-DOWN       | 63       | Next run in 14.9s
Trader ETH-USD       | 3011701  | COOL-DOWN       | 83       | Next run in 4.6s
Trader ADA-USD       | 3011702  | COOL-DOWN       | 71       | Next run in 4.6s
Trader DOGE-USD      | 2984581  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3011703  | COOL-DOWN       | 95       | Next run in 4.6s
Trader LINK-USD      | 3010697  | RUNNING         | 45       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:08:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:08:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:08:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:08:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:08:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:08:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:16 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:21 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:09:57 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:02 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:38 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:54 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:10:59 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:45 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_LINK_USD.log:2026-08-25 04:11:50 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [LINK-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

