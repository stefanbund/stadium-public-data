---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 03:14:06 PM PDT (2026-08-24 22:14:06 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.70** | **-0.50** | **-0.20** | **N/A** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.56** | **-0.50** | **-1.06** | **+9.66** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.70** | **-0.50** | **-0.20** | **-5.34** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-0.70** | **-0.50** | **-0.20** | **N/A** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-0.70** | **-0.50** | **-0.20** | **N/A** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-0.70** | **-0.50** | **-0.20** | **N/A** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-0.70** | **-0.50** | **-0.20** | **N/A** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (0.08h old) | 08-24 15:09 |
| ✅ | **TimesFM Forecasts** | Fresh (2.33h old) | 08-24 12:54 |
| ✅ | **Holding Times config** | Fresh (0.08h old) | 08-24 15:09 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-24 15:14 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-24 15:14 |
| ❌ | **Live Trading Telemetry** | NOT FOUND ON EC2 | - |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 22 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `10` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



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
| `AVAX-USD` | BUY | 7.512 | `a90a3078-8c18-4d6b-b207-68245b7a2324` |
| `AVAX-USD` | BUY | 7.512 | `0b0a69ab-0416-47aa-819d-2f2e2e8986f4` |
| `ADA-USD` | SELL | 0.22138 | `f2754a2e-0b90-4c7f-a6bb-38b829d1e6c0` |
| `AVAX-USD` | BUY | 7.533 | `13e01280-703e-4f7a-a00d-b6a53d642d3e` |
| `DOGE-USD` | BUY | 0.08976 | `f443d043-54f2-412a-916e-050a40e29382` |
| `SOL-USD` | BUY | 97.32 | `cc932aeb-f7e2-4a1e-a503-2378818a512c` |
| `BTC-USD` | BUY | 78752.95 | `c7c681af-dff2-4bd5-a809-255c0b2c1c91` |
| `BTC-USD` | BUY | 78768.91 | `73507a14-4052-4642-b866-fb9fcb080714` |
| `ADA-USD` | BUY | 0.22017 | `ea7f79a4-1cfa-4b0f-8961-78aca7a42711` |
| `DOGE-USD` | BUY | 0.08979 | `227386b0-4faa-44de-bcdf-1a3224d40410` |
| `ETH-USD` | BUY | 2477.71 | `e3cc20fe-f4de-413a-8a0c-bd8b5de86a48` |
| `ADA-USD` | BUY | 0.22047 | `ea92ecce-f056-411e-b9ac-2690828f3f6b` |
| `LINK-USD` | BUY | 11.573 | `6beae88a-4dbc-4a92-966c-798cdefd8c14` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 2.3h ago (2026-08-24 12:54 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 12:54:26 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **147.8h (6d 3h 45m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 03:09:32 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **146.8h (6d 2h 45m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  10:14:04 PM
   CPU:   2.5%  |  MEM:   8.1% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2706004  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 2706010  | RUNNING         | -        | Oracle Yield Analysis
Stable Farmer        | 2706012  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 2707994  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2708486  | COOL-DOWN       | 9        | Next run in 5.0s
Trader ADA-USD       | 2706015  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2708006  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2708007  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 2708008  | RUNNING         | 1        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:12:37 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:12:43 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:12:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:12:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:12:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:18 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:54 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:13:59 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:14:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
logs/watchdog_Trader_ADA_USD.log:2026-08-24 22:14:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1006] [ADA-USD] Error polling sell order / ticker: name 'price_buffer' is not defined
```
</details>

