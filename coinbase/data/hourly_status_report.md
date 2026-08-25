---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 05:56:34 PM PDT (2026-08-25 00:56:34 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.91** | **-0.50** | **+1.41** | **-8.26** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-0.73** | **-0.50** | **-0.23** | **+6.43** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.91** | **-0.50** | **+1.41** | **-7.92** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.91** | **-0.50** | **+1.41** | **-8.32** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.91** | **-0.50** | **+1.41** | **-7.92** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.91** | **-0.50** | **+1.41** | **-7.92** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.91** | **-0.50** | **+1.41** | **-7.92** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (2.79h old) | 08-24 15:09 |
| ✅ | **TimesFM Forecasts** | Fresh (1.91h old) | 08-24 16:02 |
| ❌ | **Holding Times config** | STALE! (80.9h old) | Limit 22.9h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 17:56 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 17:56 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-24 17:56 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 691 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `631` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 7 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 9 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 7 | 85.7% | 0 | 🟢 OK |
| `AVAX-USD` | 4 | 100.0% | 0 | 🟢 OK |
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



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.9h ago (2026-08-24 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 12:54:26 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **145.1h (6d 1h 3m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 03:09:32 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **144.1h (6d 0h 3m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  12:56:34 AM
   CPU:  12.1%  |  MEM:   5.6% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2787103  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2787217  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2787219  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2837364  | COOL-DOWN       | 44       | Next run in 14.7s
Trader ETH-USD       | 2837464  | RUNNING         | 183      | Evaluating Funnel/Polling Order
Trader ADA-USD       | 2837075  | COOL-DOWN       | 22       | Next run in 4.0s
Trader DOGE-USD      | 2837159  | COOL-DOWN       | 31       | Next run in 9.4s
Trader BTC-USD       | 2837076  | COOL-DOWN       | 35       | Next run in 4.0s
Trader LINK-USD      | 2837077  | COOL-DOWN       | 42       | Next run in 4.0s
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

