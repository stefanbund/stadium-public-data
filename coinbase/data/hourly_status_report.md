---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-27 01:43:36 AM PDT (2026-08-27 08:43:36 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.99** | **-0.50** | **-1.49** | **+5.12** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.69** | **-0.50** | **-1.19** | **+20.23** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.99** | **-0.50** | **-1.49** | **+5.24** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-1.99** | **-0.50** | **-1.49** | **+5.24** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-1.99** | **-0.50** | **-1.49** | **+5.24** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-1.99** | **-0.50** | **-1.49** | **+5.24** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-1.99** | **-0.50** | **-1.49** | **+5.24** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (14.99h old) | 08-26 10:44 |
| ✅ | **TimesFM Forecasts** | Fresh (1.70h old) | 08-27 00:02 |
| ❌ | **Holding Times config** | STALE! (136.7h old) | Limit 78.7h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-27 01:43 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 08-27 01:43 |
| ✅ | **Live Trading Telemetry** | Fresh (0.01h old) | 08-27 01:43 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 2174 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `14,427` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ETH-USD` | 1 | 100.0% | 0 | 🟢 OK |
| `ADA-USD` | 6 | 83.3% | 0 | 🟢 OK |
| `AVAX-USD` | 2 | 50.0% | 1 | 🟢 OK |
| `DOGE-USD` | 3 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 5 | 100.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `USDT-USDC` | SELL | 1.0001 | `a69d9998-a1ee-4622-87af-a15bb8d32eaf` |
| `ADA-USD` | SELL | 0.22853 | `2beee26b-f88c-4929-8625-ec618ae9e32d` |
| `LINK-USD` | SELL | 11.886 | `e550166a-4422-4a46-9c78-7db264061242` |
| `AVAX-USD` | SELL | 7.708 | `7c4cd0f2-8347-4458-a3a5-8619324273a2` |
| `ADA-USD` | SELL | 0.22818 | `7af97780-5e33-47e5-9caf-12bec2c8a7d5` |
| `ADA-USD` | SELL | 0.22503 | `eb72afdd-a3d7-40b8-9598-30b5ca2b74ef` |
| `DOGE-USD` | SELL | 0.09237 | `3160f212-8ff6-4b19-a291-73c17cdf2a97` |
| `AVAX-USD` | SELL | 7.625 | `c14c3c5a-f35f-4043-a616-ea4c20cfa9f2` |
| `DOGE-USD` | SELL | 0.09132 | `2f2ed9b7-454b-4377-9672-5f4c78c84b1e` |
| `LINK-USD` | BUY | 11.845 | `47a1cc74-dda6-4911-aeb9-7d4bb12449c0` |
| `ADA-USD` | SELL | 0.22031 | `d968b8ef-1180-4f05-bc11-01087aa5d99a` |
| `AVAX-USD` | SELL | 7.558 | `fc9234ee-6ef0-4ba3-a44b-d86922f91144` |
| `ADA-USD` | BUY | 0.21529 | `d60f726c-3023-4ef9-a8c2-32f979fc78ff` |
| `DOGE-USD` | BUY | 0.08884 | `badf2c40-c803-4462-ae12-77150b85f302` |
| `BTC-USD` | BUY | 79864.3 | `0453538c-6ca2-4649-879f-38a66578d051` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.7h ago (2026-08-27 12:02 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **89.3h (3d 17h 16m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-26 10:44:36 AM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **88.3h (3d 16h 16m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  08:43:35 AM
   CPU:  13.0%  |  MEM:   7.7% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1334286  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1334424  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1334426  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1378079  | COOL-DOWN       | 144      | Next run in 3.7s
Trader ETH-USD       | 1378087  | COOL-DOWN       | 145      | Next run in 9.4s
Trader ADA-USD       | 1378251  | RUNNING         | 112      | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1378252  | RUNNING         | 66       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1378088  | RUNNING         | 145      | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1378089  | RUNNING         | 86       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:11:03 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:11:23 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:11:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:12:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:12:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:12:44 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:13:04 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:13:24 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:13:45 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:14:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:14:25 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:14:45 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:15:05 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:15:26 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:15:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:16:06 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:16:26 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:16:46 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:17:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:17:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:17:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:18:07 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:18:27 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:18:47 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:19:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:19:28 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:19:48 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:20:08 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:20:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:20:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:21:09 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:21:29 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:21:49 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:22:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:22:30 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:22:50 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:23:10 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:23:31 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:23:51 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
logs/watchdog_Trader_SOL_USD.log:2026-08-26 19:24:11 [ERROR] [async_sfgk_trader.py:perform_trade_cycle:678] [SOL-USD] MAO state read failed: local variable 'json' referenced before assignment
```
</details>

