---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-09-02 08:23:10 AM PDT (2026-09-02 15:23:10 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+9.04** | -1.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-0.56** | **-0.50** | **-0.06** | **+23.39** | -1.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+9.02** | -1.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+6.64** | -1.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+9.34** | -1.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+8.97** | -1.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.44** | **-0.50** | **+0.06** | **+9.34** | -1.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (0.68h old) | 09-02 07:42 |
| ✅ | **TimesFM Forecasts** | Fresh (0.33h old) | 09-02 08:03 |
| ✅ | **Holding Times config** | Fresh (0.68h old) | 09-02 07:42 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 09-02 08:23 |
| ✅ | **ETH DVOL Cache** | Fresh (0.00h old) | 09-02 08:23 |
| ❌ | **Live Trading Telemetry** | STALE! (0.7h old) | Limit 0.1h |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1740 recent read events).


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
| `ADA-USD` | 7 | 71.4% | 0 | 🟢 OK |
| `DOGE-USD` | 81 | 66.7% | 2 | 🟢 OK |
| `ETH-USD` | 36 | 58.3% | 0 | 🟢 OK |
| `LINK-USD` | 86 | 69.8% | 0 | 🟢 OK |
| `AVAX-USD` | 70 | 68.6% | 1 | 🟢 OK |
| `SOL-USD` | 27 | 77.8% | 1 | 🟢 OK |

---
## 4. 🚜 Continuous U/U Liquidity Reservoir & Peg Farmer (USDT-USD)
Operational telemetry of the high-velocity stablecoin market-making and VIP fee tier acceleration engine (`uu_farmer_v2.py`).

| Metric | Live State | Details / Configuration |
| :--- | :--- | :--- |
| **Daemon Engine** | 🟢 RUNNING | PID `896883` on Live EC2 (CPU: `1.1%`, RAM: `0.2%`) |
| **Target Peg Pair** | `USDT-USD` | Dynamic Top-of-Book Post-Only Maker liquidity |
| **Tranche Order Sizing** | `$5,000.00 USD` | Multi-block continuous capital rotation |
| **HFT Reserve Floor** | `$15,000.00 USD` | Unencumbered liquid USD strictly reserved for 0ms volatile strikes |
| **Priority Interrupt Mode** | 🟢 ACTIVE FARMING (NON_UU_EMERGENT=False) | Instantly cancels U/U buys when volatile trade enters |
| **Active BUY Tranches** | **2 Orders** (`$9,993.70 USD`) | Resting Limit Bids pegged to Best Bid |
| **Active SELL Tranches** | **8 Orders** (`$39,975.55 USDT`) | Resting Limit Asks pegged to Best Ask |
| **Total Deployed U/U Capital** | **`$49,969.25 USD`** | Active bidirectional turnover liquidity pool |
| **Rolling 30-Day Volume** | **`$2,257,751.81 USD`** | **VIP 2** (Maker: **0.05%** / 5 bps, Taker: **0.10%**) |
| **Next Tier Milestone (VIP 3)** | **45.2% Complete** | `$2,742,248.19 USD` to reach $5,000,000.00 threshold |


### Active U/U Maker Tranches on the Book

| Pair | Side | Limit Price | Tranche Size | Est. Value | Order ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `USDT-USD` | 🟢 **BUY** | 0.99937 | 5,000.0 | `$4,996.85` | `9bbf7559-af4f-41b2-8533-21f17f3d51e9` |
| `USDT-USD` | 🟢 **BUY** | 0.99937 | 5,000.0 | `$4,996.85` | `010b51d3-a3cb-4305-b3e7-010430ef3e76` |
| `USDT-USD` | 🔴 **SELL** | 0.99945 | 5,000.0 | `$4,997.25` | `b601a783-a153-457b-8672-e969189e061f` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `0bf3d867-febe-4739-8867-78907dcd3f79` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `ee7023b7-fc4f-4a89-a718-43a644dae208` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `8c8e0683-e00a-469c-b029-935816dbea43` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `27e51a15-52ad-4494-b1cc-a1fd2f1ad29a` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `92706a14-487b-4277-95cd-cc792c2e1441` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `153d7f30-c3a6-43fb-bef7-ef4b4a83bfbf` |
| `USDT-USD` | 🔴 **SELL** | 0.99938 | 5,000.0 | `$4,996.90` | `79c6d485-dd27-4417-8f3b-39c3cd06d58b` |


---
## 5. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `USDT` | 5500.0700 | 36349.6300 | **41849.7000** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 0.0000 | 4794.4264 | **4794.4264** |
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
| `ADA-USD` | SELL | 0.19694 | 4,794.43 | `1a849f8f-34fc-4ef3-8b31-35e889eb15bc` |
| `LINK-USD` | SELL | 11.15200 | 100.45 | `18653ff0-08d8-4efb-9818-fc503a036c9d` |
| `AVAX-USD` | SELL | 7.17600 | 179.70 | `d4b37958-5c0e-4240-b2a2-6d32bae0d26e` |
| `USDT-USD` | SELL | 0.99945 | 5,000.00 | `b601a783-a153-457b-8672-e969189e061f` |
| `USDT-USD` | BUY | 0.99937 | 5,000.00 | `9bbf7559-af4f-41b2-8533-21f17f3d51e9` |
| `USDT-USD` | BUY | 0.99937 | 5,000.00 | `010b51d3-a3cb-4305-b3e7-010430ef3e76` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `0bf3d867-febe-4739-8867-78907dcd3f79` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `ee7023b7-fc4f-4a89-a718-43a644dae208` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `8c8e0683-e00a-469c-b029-935816dbea43` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `27e51a15-52ad-4494-b1cc-a1fd2f1ad29a` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `92706a14-487b-4277-95cd-cc792c2e1441` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `153d7f30-c3a6-43fb-bef7-ef4b4a83bfbf` |
| `USDT-USD` | SELL | 0.99938 | 5,000.00 | `79c6d485-dd27-4417-8f3b-39c3cd06d58b` |



---
## 6. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.3h ago (2026-09-02 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-31 12:42:56 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-09-06 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **106.6h (4d 10h 36m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-09-02 07:42:22 AM PDT`
- **Next Scheduled Run**: `2026-09-06 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **105.6h (4d 9h 36m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 7. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  03:23:11 PM
   CPU:   5.7%  |  MEM:   7.0% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 896789   | RUNNING         | -        | Continuous Websocket Feed
MAO Daemon           | 896881   | RUNNING         | -        | Oracle Yield Analysis
U/U Farmer           | 896883   | RUNNING         | -        | Volume Farmer
Trader AVAX-USD      | 929579   | RUNNING         | 67       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 983991   | COOL-DOWN       | 179      | Next run in 29.8s
Trader ADA-USD       | 923179   | RUNNING         | 54       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 984086   | COOL-DOWN       | 39       | Next run in 0.0s
Trader BTC-USD       | 983661   | COOL-DOWN       | 188      | Next run in 19.3s
Trader LINK-USD      | 930844   | RUNNING         | 62       | Evaluating Funnel/Polling Order
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

