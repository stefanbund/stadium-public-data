# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-05 11:32:12 AM PDT (2026-08-05 18:32:12 UTC)`  
> **System Health**: **🟢 ALL SYSTEMS NOMINAL** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) tracking and causal volatility gating against the promoted optimal threshold ($Z \le -0.5$).

| Symbol | Spot DVOL | 4h Rolling Z-Score | 14p RSI | Exhaustion Index | Vol Trend | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BTC-USD` | **34.14** | **-1.44** (≤ -0.5) | 37.8 | 20/100 (< 30) | Compression 📉 | 🟢 Approved |
| `ETH-USD` | **47.79** | **-1.90** (≤ -0.5) | 55.2 | 0/100 (< 30) | Expansion 📈 | 🟢 Approved |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

---
## 2. 📊 5-Layer Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `122,217` | **99.5%** |
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

- **TimesFM Forecast DB**: 🟢 Updated 2.9h ago (2026-08-05 08:38 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-09 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **103.5h (4d 7h 27m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

![TimesFM Forecast Matrix](./images/timesfm_forecast_matrix.png)

---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:32:09 PM
   CPU:  37.6%  |  MEM:   6.9% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 457105   | RUNNING         | -        | Continuous Websocket Feed
Trader DOT-USD       | 492404   | COOL-DOWN       | 260      | Next run in 15.0s
Trader ETH-USD       | 492405   | COOL-DOWN       | 260      | Next run in 15.0s
Trader ADA-USD       | 492406   | COOL-DOWN       | 260      | Next run in 15.0s
Trader DOGE-USD      | 492407   | COOL-DOWN       | 260      | Next run in 15.0s
Trader BTC-USD       | 492408   | COOL-DOWN       | 260      | Next run in 15.0s
Trader LTC-USD       | 492409   | COOL-DOWN       | 260      | Next run in 15.0s
Trader SOL-USD       | 492410   | COOL-DOWN       | 260      | Next run in 15.0s
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

