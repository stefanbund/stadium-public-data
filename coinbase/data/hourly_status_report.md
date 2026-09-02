---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 04:00:08 PM PDT (2026-09-02 23:00:08 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.72** | **-0.50** | **-0.22** | **+10.15** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.48** | **-0.50** | **-0.98** | **+23.62** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.72** | **-0.50** | **-0.22** | **+9.22** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.72** | **-0.50** | **-0.22** | **+10.02** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.72** | **-0.50** | **-0.22** | **+9.65** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.72** | **-0.50** | **-0.22** | **+9.71** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.72** | **-0.50** | **-0.22** | **+9.65** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (8.30h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (3.12h old) | 09-02 12:53 |
| ✅ | **Holding Times config** | Fresh (51.28h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 16:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 16:00 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 09-02 16:00 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1727 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `83,986` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 12 | 75.0% | 0 | 🟢 OK |
| `DOGE-USD` | 82 | 65.9% | 3 | 🟢 OK |
| `ETH-USD` | 38 | 55.3% | 2 | 🟢 OK |
| `LINK-USD` | 91 | 67.0% | 1 | 🟢 OK |
| `AVAX-USD` | 74 | 66.2% | 1 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `1396735` on Live EC2 (CPU: `1.1%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **7 Orders** (`$34,988.10 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **2 Orders** (`$9,997.50 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$44,985.60 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,295,739.67 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **45.9% Complete** | `$2,704,260.33 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `000db735-19a1-4ded-9b35-e7baf2a5c905` |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `34fd03f2-4e3f-4e57-b49d-688ef29231f5` |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `008ef6dc-c880-4e32-8361-f622cfa3d813` |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `09ab2a3d-8a7c-422d-bd17-3c3baaef9903` |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `420558fd-1038-4fc9-89df-a2fdf7fb346a` |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `3ed45b4b-87f8-45b6-b3ce-05cab78f598c` |
| `USDT-USD` | 🟢 **BUY** | 0.99966 | 5,000.0 | `$4,998.30` | `d4759ed8-6674-4899-9f23-2761f0424f7e` |
| `USDT-USD` | 🔴 **SELL** | 0.99980 | 5,000.0 | `$4,999.00` | `3810b51b-920c-4f6d-9bb1-0c0274a5cef0` |
| `USDT-USD` | 🔴 **SELL** | 0.99970 | 5,000.0 | `$4,998.50` | `bb8c4dbe-c137-46f9-8b05-20ba7e211819` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 6224.5800 | 5000.0000 | **11224.5800** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 0.0000 | 3824.4585 | **3824.4585** |
| `DOGE` | 0.2000 | 27580.9000 | **27581.1000** |
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
| `ADA-USD` | SELL | 0.19935 | 3,824.46 | `8f5c18a6-ee5f-4d7e-b9d4-53b85dd68869` |
| `USDT-USD` | SELL | 0.99980 | 5,000.00 | `3810b51b-920c-4f6d-9bb1-0c0274a5cef0` |
| `AVAX-USD` | SELL | 7.16600 | 186.53 | `c5533c2b-bc23-4d7f-b4eb-5c92821f53ab` |
| `DOGE-USD` | SELL | 0.08143 | 27,580.90 | `0b5b8ecc-148c-4956-b467-4c7381568f5b` |
| `LINK-USD` | BUY | 11.02100 | 128.28 | `3e70fbe8-fdac-4ab5-8515-0d52304ea942` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.1h ago (2026-09-02 12:53 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **99.0h (4d 2h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **98.0h (4d 1h 59m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  11:00:04 PM
   CPU:   2.9%  |  MEM:   7.7% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1396621  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1396733  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1396735  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1400833  | RUNNING         | 11       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1456230  | COOL-DOWN       | 130      | Next run in 9.5s
Trader ADA-USD       | 1398064  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1403988  | RUNNING         | 11       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1456203  | COOL-DOWN       | 170      | Next run in 3.9s
Trader LINK-USD      | 1455439  | RUNNING         | 111      | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-09-02 17:59:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 17:59:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.36s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 18:51:32 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 18:52:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 19:25:09 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.19s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 19:25:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.20s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 19:59:31 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.22s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 19:59:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:00:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:00:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.39s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:00:58 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.45s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:01:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:08:09 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.31s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:08:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:13:53 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.44s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:36:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.44s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 20:57:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:31:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:33:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:35:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:40:18 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:44:37 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.16s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:46:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:48:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:51:29 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:52:12 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:52:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:52:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:53:17 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.16s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:54:43 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:55:26 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.28s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:59:11 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.25s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:59:33 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 21:59:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 22:00:17 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 22:00:38 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 22:01:21 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 22:01:42 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 22:02:04 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.32s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 22:03:12 [ERROR] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.44s... | Error: 401 Client Error: Unauthorized Unauthorized
```
</details>

