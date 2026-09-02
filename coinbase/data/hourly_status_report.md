---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 09:37:15 AM PDT (2026-09-02 16:37:15 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.43** | **-0.50** | **-0.93** | **+9.04** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-2.02** | **-0.50** | **-1.52** | **+21.79** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-1.43** | **-0.50** | **-0.93** | **+8.25** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-1.43** | **-0.50** | **-0.93** | **+8.54** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-1.43** | **-0.50** | **-0.93** | **+8.25** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-1.43** | **-0.50** | **-0.93** | **+7.63** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-1.43** | **-0.50** | **-0.93** | **+8.20** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (1.92h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (1.57h old) | 09-02 08:03 |
| ✅ | **Holding Times config** | Fresh (44.90h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 09:37 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 09:37 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 09-02 09:37 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1492 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `79,158` | **100.0%** |
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
| `DOGE-USD` | 81 | 66.7% | 2 | 🟢 OK |
| `ETH-USD` | 36 | 58.3% | 0 | 🟢 OK |
| `LINK-USD` | 87 | 69.0% | 1 | 🟢 OK |
| `AVAX-USD` | 71 | 67.6% | 2 | 🟢 OK |
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
| **Active BUY Tranches** | **2 Orders** (`$9,994.70 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **6 Orders** (`$29,984.40 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$39,979.10 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,266,105.74 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **45.3% Complete** | `$2,733,894.26 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99947 | 5,000.0 | `$4,997.35` | `d3eb1dd4-a522-499b-85b6-1a0c765e0f6b` |
| `USDT-USD` | 🟢 **BUY** | 0.99947 | 5,000.0 | `$4,997.35` | `51a6ac4c-4b0a-4637-ae21-7525e9fc82e5` |
| `USDT-USD` | 🔴 **SELL** | 0.99948 | 5,000.0 | `$4,997.40` | `01e824f2-5fea-4c40-9496-e48f958942de` |
| `USDT-USD` | 🔴 **SELL** | 0.99948 | 5,000.0 | `$4,997.40` | `7cbd1a91-8ecb-467e-8022-b651c22ac026` |
| `USDT-USD` | 🔴 **SELL** | 0.99948 | 5,000.0 | `$4,997.40` | `ba44a759-9120-4ef3-bc4b-7366ee47df59` |
| `USDT-USD` | 🔴 **SELL** | 0.99948 | 5,000.0 | `$4,997.40` | `2d858696-ef43-4ddb-b3e4-49276bdf4730` |
| `USDT-USD` | 🔴 **SELL** | 0.99948 | 5,000.0 | `$4,997.40` | `d98056f4-2c68-4ed7-b190-3f39b31eb4c1` |
| `USDT-USD` | 🔴 **SELL** | 0.99948 | 5,000.0 | `$4,997.40` | `08394073-ae05-4d7e-8442-c36b3c17f8ff` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 35672.3900 | 0.0000 | **35672.3900** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `DOGE` | 0.2000 | 26676.2000 | **26676.4000** |
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
| `AVAX-USD` | SELL | 7.17600 | 166.61 | `8f8d6f0e-35bf-4bdc-a0bc-8dc6dedfeec1` |
| `DOGE-USD` | SELL | 0.08187 | 26,676.20 | `83491859-00a2-4a45-9505-c2ac9cff69d4` |
| `LINK-USD` | SELL | 11.16600 | 129.38 | `de796d1d-975f-4b44-943d-1d50c5b07d1a` |
| `ETH-USD` | SELL | 2,402.19000 | 0.59 | `cc9bf3aa-03da-4d5e-99ea-709638ed8bc9` |
| `USDT-USD` | BUY | 0.99947 | 5,000.00 | `d3eb1dd4-a522-499b-85b6-1a0c765e0f6b` |
| `USDT-USD` | BUY | 0.99947 | 5,000.00 | `51a6ac4c-4b0a-4637-ae21-7525e9fc82e5` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 1.6h ago (2026-09-02 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **105.4h (4d 9h 22m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **104.4h (4d 8h 22m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  04:37:12 PM
   CPU:  11.5%  |  MEM:   7.6% (14.2GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1019566  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1019640  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 1019642  | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1019643  | RUNNING         | 0        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1051184  | RUNNING         | 59       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1060394  | COOL-DOWN       | 102      | Next run in 14.7s
Trader DOGE-USD      | 1031021  | RUNNING         | 22       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 1060255  | COOL-DOWN       | 107      | Next run in 9.5s
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

