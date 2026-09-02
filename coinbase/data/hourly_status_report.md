---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 11:00:08 AM PDT (2026-09-02 18:00:08 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.13** | **-0.50** | **-0.63** | **+7.97** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.50** | **-0.50** | **-1.00** | **+22.21** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.13** | **-0.50** | **-0.63** | **+7.83** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-1.13** | **-0.50** | **-0.63** | **+7.96** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-1.13** | **-0.50** | **-0.63** | **+7.51** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-1.13** | **-0.50** | **-0.63** | **+8.04** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-1.13** | **-0.50** | **-0.63** | **+8.04** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (3.30h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (2.95h old) | 09-02 08:03 |
| ✅ | **Holding Times config** | Fresh (46.28h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 11:00 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 11:00 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 09-02 11:00 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1612 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `80,223` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 9 | 66.7% | 0 | 🟢 OK |
| `DOGE-USD` | 82 | 65.9% | 3 | 🟢 OK |
| `ETH-USD` | 37 | 56.8% | 1 | 🟢 OK |
| `LINK-USD` | 88 | 68.2% | 2 | 🟢 OK |
| `AVAX-USD` | 72 | 66.7% | 3 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `1147595` on Live EC2 (CPU: `1.1%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **8 Orders** (`$39,980.85 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **1 Orders** (`$4,997.70 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$44,978.55 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,273,198.51 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **45.5% Complete** | `$2,726,801.49 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99951 | 5,000.0 | `$4,997.55` | `6ff4e5e3-1d81-417f-9de4-28fdcb934f87` |
| `USDT-USD` | 🟢 **BUY** | 0.99952 | 5,000.0 | `$4,997.60` | `84be727c-5ff2-4a4e-a8a3-ad3b29a28eea` |
| `USDT-USD` | 🟢 **BUY** | 0.99952 | 5,000.0 | `$4,997.60` | `36b1bf14-eb1b-44c5-a81a-67fa754acbad` |
| `USDT-USD` | 🟢 **BUY** | 0.99952 | 5,000.0 | `$4,997.60` | `49f4a3e0-7a32-42f0-89cb-845d7ec41313` |
| `USDT-USD` | 🟢 **BUY** | 0.99952 | 5,000.0 | `$4,997.60` | `945cbb20-69e4-4cfb-a022-468b386dd12f` |
| `USDT-USD` | 🟢 **BUY** | 0.99952 | 5,000.0 | `$4,997.60` | `07f273c7-9915-474b-90e4-399e4ec352c8` |
| `USDT-USD` | 🟢 **BUY** | 0.99953 | 5,000.0 | `$4,997.65` | `c9129031-7e9b-4ceb-a647-9d952669eda8` |
| `USDT-USD` | 🟢 **BUY** | 0.99953 | 5,000.0 | `$4,997.65` | `e072e1f2-39c5-48f8-bb18-13f93b2d845d` |
| `USDT-USD` | 🔴 **SELL** | 0.99954 | 5,000.0 | `$4,997.70` | `c68cf2a4-dead-4a57-88ff-ffebb8b654ab` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 1733.6700 | 5000.0000 | **6733.6700** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 0.0000 | 4410.8282 | **4410.8282** |
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
| `ADA-USD` | SELL | 0.19706 | 4,410.83 | `31353691-efa4-4461-9272-66ce5ccaa394` |
| `AVAX-USD` | BUY | 7.15000 | 185.97 | `28611822-a866-4d53-a13d-a19d42e18398` |
| `USDT-USD` | BUY | 0.99951 | 5,000.00 | `6ff4e5e3-1d81-417f-9de4-28fdcb934f87` |
| `LINK-USD` | BUY | 11.09900 | 105.63 | `b77a92ba-eeca-4aef-9342-949a9dbcd53c` |
| `USDT-USD` | BUY | 0.99952 | 5,000.00 | `84be727c-5ff2-4a4e-a8a3-ad3b29a28eea` |
| `USDT-USD` | BUY | 0.99952 | 5,000.00 | `36b1bf14-eb1b-44c5-a81a-67fa754acbad` |
| `USDT-USD` | BUY | 0.99952 | 5,000.00 | `49f4a3e0-7a32-42f0-89cb-845d7ec41313` |
| `USDT-USD` | BUY | 0.99952 | 5,000.00 | `945cbb20-69e4-4cfb-a022-468b386dd12f` |
| `USDT-USD` | BUY | 0.99952 | 5,000.00 | `07f273c7-9915-474b-90e4-399e4ec352c8` |
| `USDT-USD` | SELL | 0.99954 | 5,000.00 | `c68cf2a4-dead-4a57-88ff-ffebb8b654ab` |
| `DOGE-USD` | BUY | 0.08130 | 29,627.40 | `17cc1b7b-ca7a-4b80-9ed5-8375d7c719e8` |
| `USDT-USD` | BUY | 0.99953 | 5,000.00 | `c9129031-7e9b-4ceb-a647-9d952669eda8` |
| `USDT-USD` | BUY | 0.99953 | 5,000.00 | `e072e1f2-39c5-48f8-bb18-13f93b2d845d` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 2.9h ago (2026-09-02 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **104.0h (4d 7h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **103.0h (4d 6h 59m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:00:08 PM
   CPU:  15.2%  |  MEM:   7.6% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1147587  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1147593  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1147595  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1148358  | RUNNING         | 2        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1148717  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1147598  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1147897  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1148722  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader LINK-USD      | 1148724  | RUNNING         | 3        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:2026-09-02 17:59:05 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.38s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 17:59:27 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-02 17:59:48 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_accounts | Sleeping 1.36s... | Error: 429 Client Error: Too Many Requests
```
</details>

