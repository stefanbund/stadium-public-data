---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 10:15:02 AM PDT (2026-09-02 17:15:02 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.12** | **-0.50** | **-0.62** | **+8.49** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-2.20** | **-0.50** | **-1.70** | **+21.79** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.12** | **-0.50** | **-0.62** | **+8.49** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-1.12** | **-0.50** | **-0.62** | **+8.49** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-1.12** | **-0.50** | **-0.62** | **+8.49** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-1.12** | **-0.50** | **-0.62** | **+7.63** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-1.12** | **-0.50** | **-0.62** | **+8.49** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (2.55h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (2.20h old) | 09-02 08:03 |
| ✅ | **Holding Times config** | Fresh (45.53h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 10:15 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 10:14 |
| ✅ | **Live Trading Telemetry** | Fresh (0.01h old) | 09-02 10:14 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1344 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `79,534` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 8 | 62.5% | 1 | 🟢 OK |
| `DOGE-USD` | 82 | 65.9% | 3 | 🟢 OK |
| `ETH-USD` | 36 | 58.3% | 0 | 🟢 OK |
| `LINK-USD` | 87 | 69.0% | 1 | 🟢 OK |
| `AVAX-USD` | 72 | 66.7% | 3 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `1019642` on Live EC2 (CPU: `1.2%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **9 Orders** (`$44,973.00 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **1 Orders** (`$4,997.05 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$49,970.05 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,267,295.16 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **45.3% Complete** | `$2,732,704.84 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `6ac3dcdf-ebd6-4252-9efc-5bff1ac4924b` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `ec0fc08f-dd8a-42e1-8937-11f1ded8793e` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `63be2c87-38f9-4fd0-8f2b-ef14d47eec22` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `8226855a-653f-4cb8-8351-7d60b9083028` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `e7193951-8dfe-47bc-a6ed-38487fc39acb` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `fed7af7f-9d4f-4e45-b89f-f46986923097` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `93a345bf-a55a-4cf2-a375-e093ab711f8d` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `ff22bb6c-451a-436a-9d5c-0b26298b8c39` |
| `USDT-USD` | 🟢 **BUY** | 0.99940 | 5,000.0 | `$4,997.00` | `55988e83-ac08-4842-9fe4-48d7c0200a99` |
| `USDT-USD` | 🔴 **SELL** | 0.99941 | 5,000.0 | `$4,997.05` | `ef7755ae-e91d-4990-b448-0e68841cf97b` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 548.4500 | 5000.0000 | **5548.4500** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `DOGE` | 0.2000 | 0.0000 | **0.2000** |
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
| `LINK-USD` | SELL | 11.16600 | 129.38 | `de796d1d-975f-4b44-943d-1d50c5b07d1a` |
| `ETH-USD` | SELL | 2,402.19000 | 0.59 | `cc9bf3aa-03da-4d5e-99ea-709638ed8bc9` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `6ac3dcdf-ebd6-4252-9efc-5bff1ac4924b` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `ec0fc08f-dd8a-42e1-8937-11f1ded8793e` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `63be2c87-38f9-4fd0-8f2b-ef14d47eec22` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `8226855a-653f-4cb8-8351-7d60b9083028` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `e7193951-8dfe-47bc-a6ed-38487fc39acb` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `fed7af7f-9d4f-4e45-b89f-f46986923097` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `93a345bf-a55a-4cf2-a375-e093ab711f8d` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `ff22bb6c-451a-436a-9d5c-0b26298b8c39` |
| `USDT-USD` | BUY | 0.99940 | 5,000.00 | `55988e83-ac08-4842-9fe4-48d7c0200a99` |
| `USDT-USD` | SELL | 0.99941 | 5,000.00 | `ef7755ae-e91d-4990-b448-0e68841cf97b` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 2.2h ago (2026-09-02 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **104.7h (4d 8h 44m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **103.7h (4d 7h 44m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:15:03 PM
   CPU:  14.7%  |  MEM:   7.0% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1019566  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1019640  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1019642  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1099661  | COOL-DOWN       | 43       | Next run in 14.6s
Trader ETH-USD       | 1051184  | RUNNING         | 59       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1099716  | RUNNING         | 209      | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1099717  | RUNNING         | 35       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1099662  | COOL-DOWN       | 214      | Next run in 14.6s
Trader LINK-USD      | 1050762  | RUNNING         | 75       | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:2026-09-02 15:59:04 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 15:59:25 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.36s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 15:59:47 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.21s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:00:08 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:00:30 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:00:51 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.30s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:01:55 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.12s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:13:15 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.29s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:16:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.33s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:19:58 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.13s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 16:20:41 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.50s... | Error: 429 Client Error: Too Many Requests
```
</details>

