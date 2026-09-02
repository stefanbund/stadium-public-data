---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 08:41:44 AM PDT (2026-09-02 15:41:44 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.91** | **-0.50** | **-0.41** | **+9.04** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-0.95** | **-0.50** | **-0.45** | **+23.39** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.91** | **-0.50** | **-0.41** | **+9.02** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.91** | **-0.50** | **-0.41** | **+6.64** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.91** | **-0.50** | **-0.41** | **+9.34** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.91** | **-0.50** | **-0.41** | **+8.97** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.91** | **-0.50** | **-0.41** | **+9.34** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (0.99h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (0.64h old) | 09-02 08:03 |
| ✅ | **Holding Times config** | Fresh (0.99h old) | 09-02 07:42 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 08:41 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 08:41 |
| ❌ | **Live Trading Telemetry** | STALE! (1.0h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1670 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `78,689` | **100.0%** |
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
| **Daemon Engine** | 🟢 RUNNING | PID `896883` on Live EC2 (CPU: `1.2%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **7 Orders** (`$34,979.70 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **3 Orders** (`$14,991.45 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$49,971.15 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,261,078.33 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **45.2% Complete** | `$2,738,921.67 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `7eb3f0a8-99aa-4ac3-bb33-72ea0ed5c09c` |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `9e2fdc6f-a33c-457e-858b-32489c24f413` |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `6fee07ac-7ec9-4e0f-905e-bd66ccfe67ee` |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `8e892107-5d23-479d-be8e-67674dad7782` |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `fbc80c8b-9f20-483e-828e-f2917365083f` |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `4a8e150d-316e-4f95-ab2f-e313963e5309` |
| `USDT-USD` | 🟢 **BUY** | 0.99942 | 5,000.0 | `$4,997.10` | `9331d02c-9bb2-4c03-9d66-8f649117a1a2` |
| `USDT-USD` | 🔴 **SELL** | 0.99943 | 5,000.0 | `$4,997.15` | `a3fad2a4-54cb-4aa6-ad9c-3b87106a3066` |
| `USDT-USD` | 🔴 **SELL** | 0.99943 | 5,000.0 | `$4,997.15` | `6b6dcc14-1cc6-481a-bb00-9975dc736d57` |
| `USDT-USD` | 🔴 **SELL** | 0.99943 | 5,000.0 | `$4,997.15` | `bec818a0-eda8-481e-9523-d8dbd067f66e` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 4495.5800 | 15000.0000 | **19495.5800** |
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
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `7eb3f0a8-99aa-4ac3-bb33-72ea0ed5c09c` |
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `9e2fdc6f-a33c-457e-858b-32489c24f413` |
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `6fee07ac-7ec9-4e0f-905e-bd66ccfe67ee` |
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `8e892107-5d23-479d-be8e-67674dad7782` |
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `fbc80c8b-9f20-483e-828e-f2917365083f` |
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `4a8e150d-316e-4f95-ab2f-e313963e5309` |
| `USDT-USD` | BUY | 0.99942 | 5,000.00 | `9331d02c-9bb2-4c03-9d66-8f649117a1a2` |
| `USDT-USD` | SELL | 0.99943 | 5,000.00 | `a3fad2a4-54cb-4aa6-ad9c-3b87106a3066` |
| `USDT-USD` | SELL | 0.99943 | 5,000.00 | `6b6dcc14-1cc6-481a-bb00-9975dc736d57` |
| `USDT-USD` | SELL | 0.99943 | 5,000.00 | `bec818a0-eda8-481e-9523-d8dbd067f66e` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.6h ago (2026-09-02 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **106.3h (4d 10h 18m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **105.3h (4d 9h 17m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  03:41:45 PM
   CPU:   7.5%  |  MEM:   5.5% (14.6GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 896789   | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 896881   | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 896883   | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 1002158  | COOL-DOWN       | 84       | Next run in 14.1s
Trader ETH-USD       | 1002159  | COOL-DOWN       | 209      | Next run in 14.1s
Trader ADA-USD       | 1002162  | COOL-DOWN       | 81       | Next run in 19.3s
Trader DOGE-USD      | 1002163  | COOL-DOWN       | 69       | Next run in 19.3s
Trader BTC-USD       | 1001951  | COOL-DOWN       | 218      | Next run in 3.6s
Trader LINK-USD      | 1002160  | COOL-DOWN       | 78       | Next run in 14.1s
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
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
logs/watchdog_Trader_SOL_USD.log:SyntaxError: 'continue' not properly in loop
```
</details>

