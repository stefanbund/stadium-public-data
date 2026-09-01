---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-01 01:28:22 AM PDT (2026-09-01 08:28:22 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+5.16** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-2.19** | **-0.50** | **-1.69** | **+17.25** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+2.86** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+5.83** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+2.20** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+5.40** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+2.20** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (12.74h old) | 08-31 12:43 |
| ✅ | **TimesFM Forecasts** | Fresh (1.23h old) | 09-01 00:14 |
| ✅ | **Holding Times config** | Fresh (12.75h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-01 01:28 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-01 01:28 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 09-01 01:28 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1811 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `63,778` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 80 | 66.2% | 2 | 🟢 OK |
| `DOGE-USD` | 60 | 68.3% | 2 | 🟢 OK |
| `ETH-USD` | 25 | 68.0% | 0 | 🟢 OK |
| `LINK-USD` | 66 | 71.2% | 0 | 🟢 OK |
| `AVAX-USD` | 55 | 70.9% | 0 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `3187747` on Live EC2 (CPU: `1.0%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **0 Orders** (`$0.00 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **8 Orders** (`$39,984.80 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$39,984.80 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,040,859.09 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **40.8% Complete** | `$2,959,140.91 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `5102c1fd-81fc-47b7-913e-cb73a377ca33` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `8614096c-5011-4ffd-ba94-edd7f6c2e54e` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `0447b9e7-7587-41e7-ae3d-88c3b3f06a79` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `740a2bed-bd74-479d-9a8a-5ecfdb04e0c9` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `d1d774fd-d274-4ff3-9ace-665a2a2035d3` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `d82c5c6e-606d-4218-8a39-9e214eb753f3` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `096ba694-a7c9-4510-9f69-f509b3717206` |
| `USDT-USD` | 🔴 **SELL** | 0.99962 | 5,000.0 | `$4,998.10` | `b999d36f-a513-439b-b24d-16a5acf0c124` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 6376.9500 | 40000.0000 | **46376.9500** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 4115.3123 | 0.0000 | **4115.3123** |
| `DOGE` | 0.1000 | 26816.0000 | **26816.1000** |
| `FIL` | 0.0050 | 0.0000 | **0.0050** |
| `ALEPH` | 2.4000 | 0.0000 | **2.4000** |
| `SKL` | 0.1000 | 0.0000 | **0.1000** |
| `SAFE` | 0.1400 | 0.0000 | **0.1400** |
| `AIOZ` | 0.3000 | 0.0000 | **0.3000** |
| `BTRST` | 0.0100 | 0.0000 | **0.0100** |
| `FET` | 0.2000 | 0.0000 | **0.2000** |
| `PYR` | 0.5400 | 0.0000 | **0.5400** |
| `MPL` | 0.0005 | 0.0000 | **0.0005** |
| `MOBILE` | 0.8691 | 0.0000 | **0.8691** |
| `SHPING` | 0.7952 | 0.0000 | **0.7952** |
| `AUCTION` | 0.0002 | 0.0000 | **0.0002** |

### Open Maker Orders on the Book

| Product | Side | Limit Price | Base Size | Order ID |
| :--- | :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.00551 | 8,234.10 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.28300 | 188.59 | `080103b4-abb1-497b-903b-2e74dd5ead61` |
| `DOGE-USD` | SELL | 0.08303 | 26,816.00 | `2d529455-9a76-4d74-aa8f-cb7f28a33326` |
| `LINK-USD` | SELL | 11.41000 | 115.23 | `ee0a2bfe-17cd-4539-b352-b6f838dbc29a` |
| `ETH-USD` | SELL | 2,461.27000 | 0.29 | `a6ddfe4c-fb27-4539-ba4c-d194da8400fb` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `5102c1fd-81fc-47b7-913e-cb73a377ca33` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `8614096c-5011-4ffd-ba94-edd7f6c2e54e` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `0447b9e7-7587-41e7-ae3d-88c3b3f06a79` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `740a2bed-bd74-479d-9a8a-5ecfdb04e0c9` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `d1d774fd-d274-4ff3-9ace-665a2a2035d3` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `d82c5c6e-606d-4218-8a39-9e214eb753f3` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `096ba694-a7c9-4510-9f69-f509b3717206` |
| `USDT-USD` | SELL | 0.99962 | 5,000.00 | `b999d36f-a513-439b-b24d-16a5acf0c124` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.2h ago (2026-09-01 12:14 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **137.5h (5d 17h 31m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 12:43:56 PM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **136.5h (5d 16h 31m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  08:28:22 AM
   CPU:  17.5%  |  MEM:   7.7% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3187714  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3187745  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 3187747  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 3211189  | RUNNING         | 33       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 3214377  | RUNNING         | 67       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3216899  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3199590  | RUNNING         | 30       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3216746  | COOL-DOWN       | 86       | Next run in 14.7s
Trader LINK-USD      | 3202709  | RUNNING         | 31       | Evaluating Funnel/Polling Order
```

---
## 8. ☀️ Mac Mini Day Trader Intelligence & PnL
**Guardian Watchdog Status**: 🟢 ONLINE (PID 90216)

### 💰 Cumulative PnL Dashboards
| Environment | Total Trades | Win Rate | Net PnL (USD) |
| :--- | :--- | :--- | :--- |
| **LIVE EC2** | 0 | N/A | **$+0.00** |
| **SHADOW (Paper)** | 0 | N/A | **$+0.00** |

---
## 9. ⚠️ Actionable Error & Incident Radar (Last 10h)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:14:42 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:16:49 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:24:56 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:38:43 [ERROR] [async_sfgk_trader.py:fetch_live_state:840] [SOL-USD] CRITICAL: DVOL cache is stale (931.6s old > 150s limit, Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:45:19 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:46:44 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:48:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 06:59:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.16s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:07:59 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:14:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:15:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:16:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:18:02 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:19:50 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:21:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:21:59 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:22:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:22:42 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:23:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:24:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:24:52 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:25:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:25:56 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.10s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:26:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:27:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:28:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.28s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:29:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:58:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:58:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:58:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.36s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:59:10 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.32s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 07:59:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:00:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:00:58 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:01:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.36s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:01:42 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.16s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:02:03 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:02:24 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:02:46 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 08:07:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.20s... | Error: 429 Client Error: Too Many Requests
```
</details>

