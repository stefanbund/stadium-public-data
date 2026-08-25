---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 05:20:23 PM PDT (2026-08-25 00:20:23 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.65** | **-0.50** | **-0.15** | **-5.77** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.49** | **-0.50** | **-0.99** | **+8.87** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.65** | **-0.50** | **-0.15** | **-5.78** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.65** | **-0.50** | **-0.15** | **-5.74** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.65** | **-0.50** | **-0.15** | **-5.77** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.65** | **-0.50** | **-0.15** | **-5.79** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.65** | **-0.50** | **-0.15** | **-5.77** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (2.18h old) | 08-24 15:09 |
| ✅ | **TimesFM Forecasts** | Fresh (1.31h old) | 08-24 16:02 |
| ❌ | **Holding Times config** | STALE! (80.3h old) | Limit 22.3h |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-24 17:20 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 17:20 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-24 17:20 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 501 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `363` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 5 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 6 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `DOGE-USD` | 5 | 80.0% | 0 | 🟢 OK |
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
| `DOGE-USD` | SELL | 0.09054 | `0928e0f5-261c-447f-be4b-4df2dc974c65` |
| `ADA-USD` | SELL | 0.22253 | `ca96fe05-e6f9-487b-9d50-8203e7d1845e` |
| `SOL-USD` | SELL | 100.68 | `86f4bbcd-5852-4886-9c2f-ef077a094894` |
| `AVAX-USD` | SELL | 7.565 | `d1d301ea-2ca4-498e-9619-f6c8c29c174a` |
| `BTC-USD` | SELL | 79123.9 | `954ec299-249b-436d-a492-6f4c5972cf6c` |
| `LINK-USD` | SELL | 11.655 | `c73e6962-306b-4a88-9fd5-0c2ee4638906` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.3h ago (2026-08-24 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 12:54:26 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **145.7h (6d 1h 39m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 03:09:32 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **144.7h (6d 0h 39m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  12:20:20 AM
   CPU:   7.4%  |  MEM:   8.2% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2787103  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2787217  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2787219  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2800931  | RUNNING         | 5        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2808325  | COOL-DOWN       | 79       | Next run in 4.5s
Trader ADA-USD       | 2803718  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2802897  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2799137  | RUNNING         | 4        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2804660  | RUNNING         | 7        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:38 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:17:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:45 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:50 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:18:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:00 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:21 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:26 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:19:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:20:02 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:20:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:20:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:20:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:20:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_SOL_USD.log:2026-08-25 00:20:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [SOL-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

