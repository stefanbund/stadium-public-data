---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-04 10:08:46 AM PDT (2026-09-04 17:08:46 UTC)`  
> **System Health**: **🟢 ALL SYSTEMS NOMINAL** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **-26.22** | -1.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-2.20** | **-0.50** | **-1.70** | **-13.47** | -1.0 | 🟢 SAFE |
| `ADA-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **-29.29** | -1.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **-28.42** | -1.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **-29.21** | -1.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **-29.44** | -1.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-1.48** | **-0.50** | **-0.98** | **-29.29** | -1.0 | 🟢 SAFE |



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
| ✅ | **Go-List JSON** | Fresh (21.52h old) | 09-03 12:37 |
| ✅ | **TimesFM Forecasts** | Fresh (2.09h old) | 09-04 08:03 |
| ✅ | **Holding Times config** | Fresh (93.42h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-04 10:08 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-04 10:08 |
| ❌ | **Live Trading Telemetry** | STALE! (0.6h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 220 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `108,404` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 23 | 47.8% | 0 | 🟢 OK |
| `ADA-USD` | 46 | 76.1% | 0 | 🟢 OK |
| `DOGE-USD` | 108 | 65.7% | 0 | 🟢 OK |
| `ETH-USD` | 51 | 60.8% | 0 | 🟢 OK |
| `LINK-USD` | 119 | 68.9% | 0 | 🟢 OK |
| `AVAX-USD` | 90 | 62.2% | 0 | 🟢 OK |
| `SOL-USD` | 39 | 74.4% | 0 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | ⚪ DECOMMISSIONED (Volume Excluded from Fee Tier) | PID `-` on Live EC2 (CPU: `0.0%`, RAM: `0.0%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | ⚪ INACTIVE | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **0 Orders** (`$0.00 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **0 Orders** (`$0.00 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$0.00 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,717,758.57 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **54.4% Complete** | `$2,282,241.43 USD` to reach $5,000,000.00 threshold |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 17980.3300 | 0.0000 | **17980.3300** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 0.0000 | 3274.3141 | **3274.3141** |
| `DOGE` | 0.6000 | 0.0000 | **0.6000** |
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
| `ADA-USD` | SELL | 0.21490 | 3,274.31 | `4c34642b-b863-447b-a3ea-89eb100c9f13` |
| `LINK-USD` | SELL | 11.74300 | 0.11 | `4698c39c-4a61-40ff-80f0-bfb331a6b275` |
| `SOL-USD` | SELL | 102.09000 | 65.14 | `cd77110c-c44d-4a2a-b49d-70bce2e04880` |
| `ETH-USD` | SELL | 2,463.99000 | 0.48 | `992622b4-e39d-438b-aea7-1371ccf42e75` |
| `DOGE-USD` | BUY | 0.08446 | 19,385.50 | `bda121ca-6872-4883-9903-9841aa4f641b` |
| `BTC-USD` | BUY | 79,606.00000 | 0.01 | `10e6ac63-54ea-4f52-a438-60a86ee20123` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 2.1h ago (2026-09-04 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **56.9h (2d 8h 51m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-03 12:37:49 PM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **55.8h (2d 7h 50m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  05:08:43 PM
   CPU:  10.2%  |  MEM:   9.1% (14.0GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 3453232  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 3453369  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | -        | DISABLED        | -        | Excluded from Fee Tier
Trader AVAX-USD      | 3503804  | COOL-DOWN       | 25       | Next run in 0.0s
Trader ETH-USD       | 3498535  | RUNNING         | 12       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 3480469  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 3504779  | RUNNING         | 15       | Evaluating Funnel/Polling Order
Trader BTC-USD       | 3504832  | RUNNING         | 15       | Evaluating Funnel/Polling Order
Trader LINK-USD      | 3492631  | RUNNING         | 7        | Evaluating Funnel/Polling Order
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
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:2026-09-04 04:00:16 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-09-04 08:09:10 [WARNING] [async_sfgk_trader.py:_execute_api_call:299] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.49s... | Error: ('Connection aborted.', ConnectionResetError
logs/watchdog_Trader_SOL_USD.log:2026-09-04 08:15:10 [WARNING] [async_sfgk_trader.py:_safe_requests_get:340] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.22s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
logs/watchdog_Trader_SOL_USD.log:2026-09-04 12:37:33 [WARNING] [async_sfgk_trader.py:_safe_requests_get:340] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.15s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
```
</details>

