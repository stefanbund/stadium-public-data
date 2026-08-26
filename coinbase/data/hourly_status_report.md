---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-26 12:00:04 PM PDT (2026-08-26 19:00:04 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.22** | **-0.50** | **-0.72** | **N/A** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.18** | **-0.50** | **-0.68** | **+17.89** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.22** | **-0.50** | **-0.72** | **N/A** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-1.22** | **-0.50** | **-0.72** | **N/A** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-1.22** | **-0.50** | **-0.72** | **N/A** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-1.22** | **-0.50** | **-0.72** | **N/A** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-1.22** | **-0.50** | **-0.72** | **N/A** | 5.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (1.26h old) | 08-26 10:44 |
| ✅ | **TimesFM Forecasts** | Fresh (3.95h old) | 08-26 08:03 |
| ❌ | **Holding Times config** | STALE! (123.0h old) | Limit 65.0h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-26 12:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-26 12:00 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-26 12:00 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 168 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `149` | **100.0%** |
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
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `ADA-USD` | SELL | 0.22503 | `eb72afdd-a3d7-40b8-9598-30b5ca2b74ef` |
| `DOGE-USD` | SELL | 0.09237 | `3160f212-8ff6-4b19-a291-73c17cdf2a97` |
| `AVAX-USD` | SELL | 7.625 | `c14c3c5a-f35f-4043-a616-ea4c20cfa9f2` |
| `ETH-USD` | SELL | 2503.11 | `b8603d38-2b4a-481a-803a-19ecf1beb593` |
| `SOL-USD` | SELL | 100.69 | `8dcd9986-8156-403f-81ee-b1dc96d2b3c7` |
| `BTC-USD` | SELL | 79882.66 | `560ee9a9-d0c6-4242-b2d2-c0d7ddc7393f` |
| `DOGE-USD` | SELL | 0.09132 | `2f2ed9b7-454b-4377-9672-5f4c78c84b1e` |
| `ADA-USD` | SELL | 0.22031 | `d968b8ef-1180-4f05-bc11-01087aa5d99a` |
| `AVAX-USD` | SELL | 7.558 | `fc9234ee-6ef0-4ba3-a44b-d86922f91144` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.9h ago (2026-08-26 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **103.0h (4d 6h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-26 10:44:36 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **102.0h (4d 5h 59m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  07:00:02 PM
   CPU:   7.1%  |  MEM:   8.2% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 645754   | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 645852   | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 645854   | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 645855   | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 662063   | COOL-DOWN       | 63       | Next run in 10.0s
Trader ADA-USD       | 645857   | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 645858   | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 645859   | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 645860   | RUNNING         | 0        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:47:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:47:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:48:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:48:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:48:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:49:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:49:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:49:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:50:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:50:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:50:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:51:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:51:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:51:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:52:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:52:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:52:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:53:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:53:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:53:52 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:54:12 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:54:32 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:54:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:55:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:55:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:55:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:56:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:56:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:56:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:57:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:57:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:57:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:58:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:58:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:58:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:59:13 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:59:33 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_ETH_USD.log:2026-08-26 18:59:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [ETH-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_LINK_USD.log:2026-08-26 18:38:53 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [LINK-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 18:38:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
```
</details>

