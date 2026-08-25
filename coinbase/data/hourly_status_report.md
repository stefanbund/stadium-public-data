---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 07:09:13 PM PDT (2026-08-25 02:09:13 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.75** | **-0.50** | **+2.25** | **-6.03** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.09** | **-0.50** | **+1.59** | **+8.55** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.75** | **-0.50** | **+2.25** | **-5.99** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.75** | **-0.50** | **+2.25** | **-6.00** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.75** | **-0.50** | **+2.25** | **-6.00** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.75** | **-0.50** | **+2.25** | **-6.00** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.75** | **-0.50** | **+2.25** | **-6.00** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (4.00h old) | 08-24 15:09 |
| ✅ | **TimesFM Forecasts** | Fresh (3.12h old) | 08-24 16:02 |
| ❌ | **Holding Times config** | STALE! (82.1h old) | Limit 24.2h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 19:09 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 19:09 |
| ✅ | **Live Trading Telemetry** | Fresh (0.01h old) | 08-24 19:09 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1477 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `1,654` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 9 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 9 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 6 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 9 | 88.9% | 0 | 🟢 OK |
| `AVAX-USD` | 5 | 100.0% | 0 | 🟢 OK |
| `BTC-USD` | 1 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.655 | `0e0da8e9-65c3-40f9-bc10-7ca89cfec5cb` |
| `DOGE-USD` | SELL | 0.09233 | `60d899b5-20f6-418d-8d95-8e76b7fca1e2` |
| `ETH-USD` | SELL | 2514.95 | `dd05ead3-9b5a-497a-ac26-256d87814b6f` |
| `DOGE-USD` | SELL | 0.09148 | `0ebc710b-bc1f-4951-beac-7c74d2439e3e` |
| `LINK-USD` | SELL | 11.779 | `76f25872-d2ef-478a-a931-e9a7e4634683` |
| `AVAX-USD` | SELL | 7.616 | `81cbfc6e-06d6-4a63-965b-b3ba9b78ac37` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.1h ago (2026-08-24 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **143.8h (5d 23h 50m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 03:09:32 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **142.8h (5d 22h 50m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  02:09:09 AM
   CPU:  15.1%  |  MEM:   6.6% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2881653  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2881747  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2881749  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2897713  | RUNNING         | 34       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2899023  | COOL-DOWN       | 50       | Next run in 9.0s
Trader ADA-USD       | 2899013  | COOL-DOWN       | 25       | Next run in 3.5s
Trader DOGE-USD      | 2899333  | RUNNING         | 38       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2899139  | COOL-DOWN       | 56       | Next run in 14.6s
Trader LINK-USD      | 2894669  | RUNNING         | 41       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:35:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:35:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:36:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:16 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:37:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:54 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:38:59 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:42:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:42:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:42:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:42:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:42:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:42:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

