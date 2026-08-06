# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-06 01:00:05 PM PDT (2026-08-06 20:00:05 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) tracking and causal volatility gating against the promoted optimal threshold ($Z \le -0.5$).

| Symbol | Spot DVOL | 4h Rolling Z-Score | 14p RSI | Exhaustion Index | Vol Trend | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | **34.94** | **+1.85** (≤ -0.5) | 19.2 | 20/100 (< 30) | Compression 📉 | 🔴 DAW Vetoed |
| `ETH-USD` | **47.88** | **+0.03** (≤ -0.5) | 19.1 | 0/100 (< 30) | Expansion 📈 | 🔴 DAW Vetoed |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

---
## 2. 📊 5-Layer Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `123,094` | **99.5%** |
| Layer 2.5: TimesFM Forecast Gate | `0` | **0.0%** |
| Layer 3: SDR Liquidity Filter | `0` | **0.0%** |
| Layer 4: SFGK Execution Horizon Gate | `605` | **0.5%** |
| Layer 5: Hawkes Microstructure Toxicity | `0` | **0.0%** |

![5-Layer Funnel Rejection Waterfall](./images/funnel_waterfall_breakdown.png)

### Active Universe Performance & Drift Matrix
| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `ADA-USD` | 532 | 100.0% | 0 | 🟢 OK |
| `AVAX-USD` | 532 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 532 | 100.0% | 0 | 🟢 OK |
| `SOL-USD` | 458 | 99.1% | 2 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.

### Active Wallet Balances
| Currency | Available | Hold | Total Balance |
| :--- | :--- | :--- | :--- |
| `CBETH` | 0.9734 | 0.0000 | **0.9734** |
| `CRV` | 0.0500 | 0.0000 | **0.0500** |
| `ADA` | 13260.3378 | 0.0000 | **13260.3378** |
| `DOGE` | 0.1000 | 0.0000 | **0.1000** |
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
| `LIT` | 0.0085 | 0.0000 | **0.0085** |

### Open Maker Orders on the Book
| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |

![24-Hour Realized P&L](./images/realized_pnl_timeline.png)

---
## 4. 🤖 Foundation Model MLOps & TimesFM 2.0
Zero-shot multi-step forward return forecasts and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 5.0h ago (2026-08-06 08:00 AM PDT)
- **Last Weekly VSTEF Optimization**: `Never`
- **Next Scheduled VSTEF Run**: `2026-08-09 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **78.0h (3d 5h 59m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

![TimesFM Forecast Matrix](./images/timesfm_forecast_matrix.png)

---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:39:23 PM
   CPU:   0.5%  |  MEM:   6.5% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 457105   | RUNNING         | -        | Continuous Websocket Feed
Trader DOT-USD       | 494955   | COOL-DOWN       | 281      | Next run in 9.9s
Trader ETH-USD       | 494956   | COOL-DOWN       | 281      | Next run in 9.9s
Trader ADA-USD       | 494957   | COOL-DOWN       | 281      | Next run in 9.9s
Trader DOGE-USD      | 494958   | COOL-DOWN       | 281      | Next run in 9.9s
Trader BTC-USD       | 494959   | COOL-DOWN       | 281      | Next run in 9.9s
Trader LTC-USD       | 494960   | COOL-DOWN       | 281      | Next run in 9.9s
Trader SOL-USD       | 494961   | COOL-DOWN       | 281      | Next run in 9.9s
================================================================================
```

---
## 6. ⚠️ Actionable Error & Incident Radar (Last 60m)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:33:04,785 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:33:40,215 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:34:15,222 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:34:50,446 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:35:25,742 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:36:00,809 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:36:35,903 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
logs/watchdog_Trader_SOL_USD.log:2026-08-05 17:37:11,198 - ERROR - [SOL-USD] Error loading API keys: API Keys retrieved are empty.
```
</details>

