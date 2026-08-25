---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 05:02:17 PM PDT (2026-08-25 00:02:17 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.69** | **-0.50** | **-0.19** | **-5.60** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.53** | **-0.50** | **-1.03** | **+9.17** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.69** | **-0.50** | **-0.19** | **-5.83** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.69** | **-0.50** | **-0.19** | **-5.83** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.69** | **-0.50** | **-0.19** | **N/A** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.69** | **-0.50** | **-0.19** | **-5.60** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.69** | **-0.50** | **-0.19** | **-5.72** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (1.88h old) | 08-24 15:09 |
| ✅ | **TimesFM Forecasts** | Fresh (1.01h old) | 08-24 16:02 |
| ❌ | **Holding Times config** | STALE! (80.0h old) | Limit 22.0h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 17:02 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 17:02 |
| ❌ | **Live Trading Telemetry** | NOT FOUND ON EC2 | - |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 431 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `311` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 2 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 4 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 2 | 50.0% | 1 | 🟢 OK |
| `AVAX-USD` | 2 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.655 | `0e0da8e9-65c3-40f9-bc10-7ca89cfec5cb` |
| `LINK-USD` | SELL | 11.735 | `f3afa462-6fbc-4d29-ad9b-8e1db4c8fb4e` |
| `DOGE-USD` | SELL | 0.09233 | `60d899b5-20f6-418d-8d95-8e76b7fca1e2` |
| `ETH-USD` | SELL | 2514.95 | `dd05ead3-9b5a-497a-ac26-256d87814b6f` |
| `BTC-USD` | BUY | 78779.72 | `7bcd0b72-2e76-4a8d-9780-1201cd5ed145` |
| `LINK-USD` | SELL | 11.645 | `153f5a44-6fbb-4336-8e6a-230b3d74c486` |
| `AVAX-USD` | BUY | 7.525 | `71e689c0-a376-4af3-b4da-7e3ba75626e4` |
| `AVAX-USD` | BUY | 7.52 | `563f4df9-6c59-434c-8ad1-cfce73af0791` |
| `BTC-USD` | BUY | 78783.89 | `03eaa615-0993-49af-aef3-c74251d50e0d` |
| `LINK-USD` | BUY | 11.597 | `8945353c-8873-4bb5-8118-2f6640446cce` |
| `AVAX-USD` | BUY | 7.525 | `f4df0b65-d059-47cf-89a1-23df4674fdfe` |
| `AVAX-USD` | BUY | 7.533 | `75651cc0-b3a9-4324-9eb8-8d26cc5cad62` |
| `BTC-USD` | BUY | 78899.51 | `07803fed-e4f8-4fe4-8fac-9747c810a06c` |
| `LINK-USD` | BUY | 11.608 | `9e77686b-ffde-4b34-843a-2c050a67f4b0` |
| `DOGE-USD` | SELL | 0.09024 | `70f19d32-f043-4994-8a22-5ae41ab7e11c` |
| `ADA-USD` | SELL | 0.22188 | `fdefdb29-8de9-48d0-aa1d-7cdbf837e3e3` |
| `SOL-USD` | BUY | 98.52 | `0b0b2c26-31bc-4fbb-ae58-d1a8f3fc6e13` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.0h ago (2026-08-24 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 12:54:26 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **146.0h (6d 1h 57m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 03:09:32 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **145.0h (6d 0h 57m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  12:02:15 AM
   CPU:  10.7%  |  MEM:   8.2% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2787103  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2787217  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2787219  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2793308  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2794513  | COOL-DOWN       | 27       | Next run in 14.9s
Trader ADA-USD       | 2793309  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2793310  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2793311  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2793329  | RUNNING         | 1        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:43:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:43:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:43:26 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:43:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:43:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:43:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:38 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:54 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:45:59 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:45 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:50 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:46:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:16 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:21 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:26 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:42 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-24 23:47:57 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

