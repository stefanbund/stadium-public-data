---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-01 10:42:03 PM PDT (2026-09-02 05:42:03 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-2.74** | **-0.50** | **-2.24** | **+7.19** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.09** | **-0.50** | **+0.59** | **+21.31** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-2.74** | **-0.50** | **-2.24** | **+7.10** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-2.74** | **-0.50** | **-2.24** | **+7.19** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-2.74** | **-0.50** | **-2.24** | **+7.18** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-2.74** | **-0.50** | **-2.24** | **+7.25** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-2.74** | **-0.50** | **-2.24** | **+7.18** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (33.97h old) | 08-31 12:43 |
| ✅ | **TimesFM Forecasts** | Fresh (1.82h old) | 09-01 20:53 |
| ✅ | **Holding Times config** | Fresh (33.98h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-01 22:42 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-01 22:42 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 09-01 22:42 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1949 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `79,839` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 90 | 64.4% | 1 | 🟢 OK |
| `DOGE-USD` | 76 | 69.7% | 0 | 🟢 OK |
| `ETH-USD` | 33 | 57.6% | 0 | 🟢 OK |
| `LINK-USD` | 78 | 70.5% | 1 | 🟢 OK |
| `AVAX-USD` | 69 | 69.6% | 0 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `266434` on Live EC2 (CPU: `1.1%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **5 Orders** (`$24,986.95 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **3 Orders** (`$14,992.50 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$39,979.45 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,197,584.66 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **44.0% Complete** | `$2,802,415.34 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99943 | 5,000.0 | `$4,997.15` | `1923c317-c8bb-413a-84b3-b78319ba6da7` |
| `USDT-USD` | 🟢 **BUY** | 0.99949 | 5,000.0 | `$4,997.45` | `29ee5db8-1c6b-4dbb-8e59-4b1820b9de5b` |
| `USDT-USD` | 🟢 **BUY** | 0.99949 | 5,000.0 | `$4,997.45` | `7194219a-8eca-44d1-81c2-a5f066a5167b` |
| `USDT-USD` | 🟢 **BUY** | 0.99949 | 5,000.0 | `$4,997.45` | `efecf156-e45e-46e2-8bbc-c9dc1c3b0c39` |
| `USDT-USD` | 🟢 **BUY** | 0.99949 | 5,000.0 | `$4,997.45` | `45d42ec6-3e80-4ffc-a2ae-7d850f7ab962` |
| `USDT-USD` | 🔴 **SELL** | 0.99950 | 5,000.0 | `$4,997.50` | `f8024a07-e6cd-49b4-a6f3-5fdaa28b930e` |
| `USDT-USD` | 🔴 **SELL** | 0.99950 | 5,000.0 | `$4,997.50` | `c7eef135-be70-4123-9ce9-0e845526db6d` |
| `USDT-USD` | 🔴 **SELL** | 0.99950 | 5,000.0 | `$4,997.50` | `7c8f334a-d7a9-49fa-ab2c-16e1ab8a002e` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 6422.5800 | 15000.0000 | **21422.5800** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 0.0000 | 3776.2811 | **3776.2811** |
| `DOGE` | 0.4000 | 0.0000 | **0.4000** |
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
| `LINK-USD` | BUY | 11.25700 | 116.99 | `de12be09-e34e-47cd-8b27-15befad90eb6` |
| `USDT-USD` | BUY | 0.99943 | 5,000.00 | `1923c317-c8bb-413a-84b3-b78319ba6da7` |
| `ADA-USD` | SELL | 0.19915 | 3,776.28 | `a3e6053a-e96a-4c12-91e2-cd494f2bdb9c` |
| `USDT-USD` | BUY | 0.99949 | 5,000.00 | `29ee5db8-1c6b-4dbb-8e59-4b1820b9de5b` |
| `USDT-USD` | BUY | 0.99949 | 5,000.00 | `7194219a-8eca-44d1-81c2-a5f066a5167b` |
| `USDT-USD` | BUY | 0.99949 | 5,000.00 | `efecf156-e45e-46e2-8bbc-c9dc1c3b0c39` |
| `USDT-USD` | BUY | 0.99949 | 5,000.00 | `45d42ec6-3e80-4ffc-a2ae-7d850f7ab962` |
| `USDT-USD` | SELL | 0.99950 | 5,000.00 | `f8024a07-e6cd-49b4-a6f3-5fdaa28b930e` |
| `USDT-USD` | SELL | 0.99950 | 5,000.00 | `c7eef135-be70-4123-9ce9-0e845526db6d` |
| `USDT-USD` | SELL | 0.99950 | 5,000.00 | `7c8f334a-d7a9-49fa-ab2c-16e1ab8a002e` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.8h ago (2026-09-01 08:53 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **116.3h (4d 20h 17m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-31 12:43:56 PM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **115.3h (4d 19h 17m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:42:02 AM
   CPU:  14.4%  |  MEM:   6.4% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 266402   | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 266431   | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 266434   | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 376315   | COOL-DOWN       | 152      | Next run in 14.7s
Trader ETH-USD       | 376044   | COOL-DOWN       | 257      | Next run in 3.6s
Trader ADA-USD       | 363828   | RUNNING         | 75       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 376316   | COOL-DOWN       | 196      | Next run in 14.7s
Trader BTC-USD       | 376143   | COOL-DOWN       | 286      | Next run in 9.1s
Trader LINK-USD      | 374628   | RUNNING         | 103      | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:44:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:48:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:49:24 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:50:07 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:51:33 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:56:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:57:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:58:00 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.30s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:58:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:58:44 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:59:06 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 04:59:49 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.37s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:00:11 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:00:33 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:00:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:01:38 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:02:00 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:07:02 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:12:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 05:13:09 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests
```
</details>

