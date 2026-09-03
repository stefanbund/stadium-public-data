---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 07:29:41 PM PDT (2026-09-03 02:29:41 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.88** | **-0.50** | **-0.38** | **+7.72** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.36** | **-0.50** | **-0.86** | **+21.40** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.88** | **-0.50** | **-0.38** | **+7.67** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.88** | **-0.50** | **-0.38** | **+7.64** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.88** | **-0.50** | **-0.38** | **+7.68** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.88** | **-0.50** | **-0.38** | **+8.00** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.88** | **-0.50** | **-0.38** | **+7.68** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (11.79h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (3.46h old) | 09-02 16:02 |
| ✅ | **Holding Times config** | Fresh (54.77h old) | 08-31 12:43 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 19:29 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 19:29 |
| ❌ | **Live Trading Telemetry** | STALE! (0.5h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1874 recent read events).


---
## 3. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `86,466` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | 13 | 53.8% | 0 | 🟢 OK |
| `ADA-USD` | 18 | 77.8% | 0 | 🟢 OK |
| `DOGE-USD` | 83 | 65.1% | 4 | 🟢 OK |
| `ETH-USD` | 39 | 56.4% | 0 | 🟢 OK |
| `LINK-USD` | 93 | 67.7% | 0 | 🟢 OK |
| `AVAX-USD` | 76 | 64.5% | 3 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `1521210` on Live EC2 (CPU: `1.1%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **3 Orders** (`$14,992.95 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **6 Orders** (`$29,987.50 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$44,980.45 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,319,369.73 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **46.4% Complete** | `$2,680,630.27 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99953 | 5,000.0 | `$4,997.65` | `5bffe755-a291-4dab-9b77-90b0b3f8d9dd` |
| `USDT-USD` | 🟢 **BUY** | 0.99953 | 5,000.0 | `$4,997.65` | `4eab363f-6166-445b-a2df-37c1bbbc56e5` |
| `USDT-USD` | 🟢 **BUY** | 0.99953 | 5,000.0 | `$4,997.65` | `efe5bfee-d2c7-4c8d-bb4c-68b327b9acf3` |
| `USDT-USD` | 🔴 **SELL** | 0.99980 | 5,000.0 | `$4,999.00` | `3810b51b-920c-4f6d-9bb1-0c0274a5cef0` |
| `USDT-USD` | 🔴 **SELL** | 0.99954 | 5,000.0 | `$4,997.70` | `3a21549b-3bae-4f23-a616-790230569d7a` |
| `USDT-USD` | 🔴 **SELL** | 0.99954 | 5,000.0 | `$4,997.70` | `7cbdb219-c7d3-4ad1-9630-50b7d01abf8b` |
| `USDT-USD` | 🔴 **SELL** | 0.99954 | 5,000.0 | `$4,997.70` | `2dcff782-c913-4cf0-bce1-8c8b41e09852` |
| `USDT-USD` | 🔴 **SELL** | 0.99954 | 5,000.0 | `$4,997.70` | `67c51abd-66b4-4faf-8a33-d3a860dfa219` |
| `USDT-USD` | 🔴 **SELL** | 0.99954 | 5,000.0 | `$4,997.70` | `38387eac-58af-4b35-9a15-44cea225e37d` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 6515.2100 | 30000.0000 | **36515.2100** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `DOGE` | 22044.5000 | 0.0000 | **22044.5000** |
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
| `USDT-USD` | SELL | 0.99980 | 5,000.00 | `3810b51b-920c-4f6d-9bb1-0c0274a5cef0` |
| `USDT-USD` | BUY | 0.99953 | 5,000.00 | `5bffe755-a291-4dab-9b77-90b0b3f8d9dd` |
| `USDT-USD` | BUY | 0.99953 | 5,000.00 | `4eab363f-6166-445b-a2df-37c1bbbc56e5` |
| `USDT-USD` | BUY | 0.99953 | 5,000.00 | `efe5bfee-d2c7-4c8d-bb4c-68b327b9acf3` |
| `USDT-USD` | SELL | 0.99954 | 5,000.00 | `3a21549b-3bae-4f23-a616-790230569d7a` |
| `USDT-USD` | SELL | 0.99954 | 5,000.00 | `7cbdb219-c7d3-4ad1-9630-50b7d01abf8b` |
| `USDT-USD` | SELL | 0.99954 | 5,000.00 | `2dcff782-c913-4cf0-bce1-8c8b41e09852` |
| `USDT-USD` | SELL | 0.99954 | 5,000.00 | `67c51abd-66b4-4faf-8a33-d3a860dfa219` |
| `USDT-USD` | SELL | 0.99954 | 5,000.00 | `38387eac-58af-4b35-9a15-44cea225e37d` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 3.5h ago (2026-09-02 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **95.5h (3d 23h 30m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **94.5h (3d 22h 30m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  02:29:40 AM
   CPU:   5.6%  |  MEM:   6.1% (14.5GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1649249  | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 1649364  | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | -        | DISABLED        | -        | Excluded from Fee Tier
Trader AVAX-USD      | 1678643  | COOL-DOWN       | 49       | Next run in 14.1s
Trader ETH-USD       | 1678644  | COOL-DOWN       | 49       | Next run in 14.1s
Trader ADA-USD       | 1678645  | COOL-DOWN       | 49       | Next run in 14.1s
Trader DOGE-USD      | 1678646  | COOL-DOWN       | 49       | Next run in 14.1s
Trader BTC-USD       | 1678647  | COOL-DOWN       | 49       | Next run in 14.1s
Trader LINK-USD      | 1678648  | COOL-DOWN       | 49       | Next run in 14.1s
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

