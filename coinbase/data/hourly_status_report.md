---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-01 09:43:19 PM PDT (2026-09-02 04:43:19 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-2.05** | **-0.50** | **-1.55** | **+7.74** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.64** | **-0.50** | **+1.14** | **+21.68** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-2.05** | **-0.50** | **-1.55** | **+7.85** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-2.05** | **-0.50** | **-1.55** | **+7.69** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-2.05** | **-0.50** | **-1.55** | **+7.69** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-2.05** | **-0.50** | **-1.55** | **+7.32** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-2.05** | **-0.50** | **-1.55** | **+7.69** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (32.99h old) | 08-31 12:43 |
| ✅ | **TimesFM Forecasts** | Fresh (0.84h old) | 09-01 20:53 |
| ✅ | **Holding Times config** | Fresh (33.00h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-01 21:43 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-01 21:43 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 09-01 21:43 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1738 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `78,983` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 89 | 65.2% | 0 | 🟢 OK |
| `DOGE-USD` | 75 | 69.3% | 0 | 🟢 OK |
| `ETH-USD` | 33 | 57.6% | 0 | 🟢 OK |
| `LINK-USD` | 77 | 71.4% | 0 | 🟢 OK |
| `AVAX-USD` | 69 | 69.6% | 0 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `266434` on Live EC2 (CPU: `1.0%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **4 Orders** (`$19,988.60 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **0 Orders** (`$0.00 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$19,988.60 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,189,910.48 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **43.8% Complete** | `$2,810,089.52 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99943 | 5,000.0 | `$4,997.15` | `15587258-df04-4c49-aac7-98fc24dee0fa` |
| `USDT-USD` | 🟢 **BUY** | 0.99943 | 5,000.0 | `$4,997.15` | `acc44f2a-dfcf-4f99-8bbc-a88e95c5cd2c` |
| `USDT-USD` | 🟢 **BUY** | 0.99943 | 5,000.0 | `$4,997.15` | `1e74f27a-4f78-443a-a8ea-1a79b2c23dd3` |
| `USDT-USD` | 🟢 **BUY** | 0.99943 | 5,000.0 | `$4,997.15` | `10013592-7f03-4f6f-aa91-d6f15a4cc7cb` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 11529.1900 | 5000.0000 | **16529.1900** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 0.0000 | 3544.5149 | **3544.5149** |
| `DOGE` | 0.3000 | 0.0000 | **0.3000** |
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
| `LINK-USD` | SELL | 11.27000 | 120.38 | `b19c544f-6112-4dcb-bbc6-2c220ba0f0e5` |
| `ADA-USD` | SELL | 0.19835 | 3,544.51 | `70327ad5-5942-4871-a3e1-57e4b075f107` |
| `USDT-USD` | BUY | 0.99943 | 5,000.00 | `c7dfcb8c-777d-4327-ac6b-6b8071ef2f02` |
| `USDT-USD` | BUY | 0.99943 | 5,000.00 | `43174b9f-b73a-4bf7-9c5d-2dec2fa5550b` |
| `USDT-USD` | BUY | 0.99943 | 5,000.00 | `b5342a17-76a2-46a0-98f7-3043040143d1` |
| `USDT-USD` | BUY | 0.99943 | 5,000.00 | `e1b363bc-ebc3-40a7-8b7e-1c74d5fde7a0` |
| `USDT-USD` | SELL | 0.99944 | 5,000.00 | `86645247-ffff-4c84-8456-e30a2f6e2359` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.8h ago (2026-09-01 08:53 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **117.3h (4d 21h 16m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 12:43:56 PM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **116.3h (4d 20h 16m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  04:43:16 AM
   CPU:  17.5%  |  MEM:   7.5% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 266402   | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 266431   | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 266434   | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 310899   | COOL-DOWN       | 29       | Next run in 3.6s
Trader ETH-USD       | 313308   | RUNNING         | 101      | Evaluating Funnel/Polling Order
Trader ADA-USD       | 266437   | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 313309   | RUNNING         | 101      | Evaluating Funnel/Polling Order
Trader BTC-USD       | 313310   | RUNNING         | 124      | Evaluating Funnel/Polling Order
Trader LINK-USD      | 266440   | RUNNING         | 0        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:35:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:35:42 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:37:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:38:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:40:03 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.44s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:40:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:40:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:41:09 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:41:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:41:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.30s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:42:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:42:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:42:59 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:58:32 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-01 23:59:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.41s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:00:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:17:50 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:20:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:22:50 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:23:11 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:25:21 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:28:12 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:29:16 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.20s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 00:32:07 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 01:11:19 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 01:27:56 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 02:12:13 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 02:37:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.17s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:06:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:07:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:10:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:12:21 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:13:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:14:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.28s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:17:24 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.46s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:59:01 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 03:59:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:05:51 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:29:12 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:34:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests
```
</details>

