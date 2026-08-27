---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-27 08:07:29 AM PDT (2026-08-27 15:07:29 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+1.16** | **-0.50** | **+1.66** | **+6.74** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+1.02** | **-0.50** | **+1.52** | **+22.12** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+1.16** | **-0.50** | **+1.66** | **+6.84** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+1.16** | **-0.50** | **+1.66** | **+6.76** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+1.16** | **-0.50** | **+1.66** | **+6.74** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+1.16** | **-0.50** | **+1.66** | **+6.66** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+1.16** | **-0.50** | **+1.66** | **+6.74** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (0.34h old) | 08-27 07:47 |
| ✅ | **TimesFM Forecasts** | Fresh (0.07h old) | 08-27 08:03 |
| ✅ | **Holding Times config** | Fresh (0.34h old) | 08-27 07:47 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-27 08:07 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-27 08:07 |
| ✅ | **Live Trading Telemetry** | Fresh (0.01h old) | 08-27 08:07 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 308 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `295` | **100.0%** |
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
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `ADA-USD` | SELL | 0.22503 | `eb72afdd-a3d7-40b8-9598-30b5ca2b74ef` |
| `DOGE-USD` | SELL | 0.09237 | `3160f212-8ff6-4b19-a291-73c17cdf2a97` |
| `AVAX-USD` | SELL | 7.625 | `c14c3c5a-f35f-4043-a616-ea4c20cfa9f2` |
| `DOGE-USD` | SELL | 0.09132 | `2f2ed9b7-454b-4377-9672-5f4c78c84b1e` |
| `ADA-USD` | SELL | 0.22031 | `d968b8ef-1180-4f05-bc11-01087aa5d99a` |
| `AVAX-USD` | SELL | 7.558 | `fc9234ee-6ef0-4ba3-a44b-d86922f91144` |
| `AVAX-USD` | SELL | 7.545 | `46894ef5-9c30-483c-8fba-7143dff35b0f` |
| `USDT-USDC` | SELL | 1.0001 | `a69d9998-a1ee-4622-87af-a15bb8d32eaf` |
| `ADA-USD` | SELL | 0.21591 | `4c77c654-4c05-45a1-a05c-d8540630e4e3` |
| `LINK-USD` | BUY | 11.843 | `8d2df189-3a75-47fc-bc22-20ce422bac4d` |
| `USDT-USDC` | BUY | 0.9999 | `e7ec0d17-cfc9-4d4c-844c-6723ebe307e4` |
| `USDT-USDC` | BUY | 0.9999 | `6e8df900-0844-4485-90ed-a755275ba902` |
| `USDT-USDC` | BUY | 0.9999 | `d9760f39-83b1-4763-9947-9c48660640bb` |
| `USDT-USDC` | BUY | 0.9999 | `91f5faee-d1cc-4106-bfd0-4ab88fb28735` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.1h ago (2026-08-27 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **82.9h (3d 10h 52m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-27 07:47:00 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **81.9h (3d 9h 52m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  03:07:25 PM
   CPU:  13.8%  |  MEM:   6.8% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1689300  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1689352  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1689354  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1706172  | RUNNING         | 51       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1706173  | RUNNING         | 51       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1692304  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1706105  | COOL-DOWN       | 38       | Next run in 9.9s
Trader BTC-USD       | 1706112  | COOL-DOWN       | 57       | Next run in 15.0s
Trader LINK-USD      | 1705471  | RUNNING         | 42       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:35 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:40 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:04:58 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:14 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:19 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:34 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:39 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:05:55 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:00 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:15 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:20 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:36 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:41 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:06:56 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:01 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:17 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:22 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
logs/watchdog_Trader_ADA_USD.log:2026-08-27 15:07:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:1018] [ADA-USD] Error polling sell order / ticker: 'TradeBotSFGK' object has no attribute 'get_lob_pressure'
```
</details>

