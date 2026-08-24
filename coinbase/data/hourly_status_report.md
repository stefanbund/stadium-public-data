---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-24 12:47:52 PM PDT (2026-08-24 19:47:52 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.md)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-0.33** | **-0.50** | **+0.17** | **-5.72** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **-1.82** | **-0.50** | **-1.32** | **+9.33** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **-0.33** | **-0.50** | **+0.17** | **-5.72** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **-0.33** | **-0.50** | **+0.17** | **-5.72** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **-0.33** | **-0.50** | **+0.17** | **-5.78** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **-0.33** | **-0.50** | **+0.17** | **-5.72** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **-0.33** | **-0.50** | **+0.17** | **-5.78** | 5.0 | 🔴 DAW VETOED |



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
| ✅ | **Go-List JSON** | Fresh (0.04h old) | 08-24 12:45 |
| ✅ | **TimesFM Forecasts** | Fresh (4.74h old) | 08-24 08:03 |
| ❌ | **Holding Times config** | STALE! (75.8h old) | Limit 17.8h |
| ✅ | **BTC DVOL Cache** | Fresh (0.01h old) | 08-24 12:47 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-24 12:47 |
| ✅ | **Live Trading Telemetry** | Fresh (0.01h old) | 08-24 12:47 |

<br>

> **Utilization Certification**: 🔴 **FAILED.** Guardian watchdog offline, unable to certify utilization.


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `40,345` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | 22 | 90.9% | 0 | 🟢 OK |
| `LINK-USD` | 28 | 89.3% | 0 | 🟢 OK |
| `DOGE-USD` | 22 | 86.4% | 1 | 🟢 OK |
| `ADA-USD` | 31 | 90.3% | 0 | 🟢 OK |
| `SOL-USD` | 6 | 100.0% | 0 | 🟢 OK |
| `BTC-USD` | 3 | 66.7% | 1 | 🟢 OK |
| `ETH-USD` | 11 | 81.8% | 1 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `LINK-USD` | SELL | 11.735 | `f3afa462-6fbc-4d29-ad9b-8e1db4c8fb4e` |
| `DOGE-USD` | SELL | 0.09233 | `60d899b5-20f6-418d-8d95-8e76b7fca1e2` |
| `AVAX-USD` | SELL | 7.655 | `0e0da8e9-65c3-40f9-bc10-7ca89cfec5cb` |
| `ETH-USD` | SELL | 2514.95 | `dd05ead3-9b5a-497a-ac26-256d87814b6f` |
| `ADA-USD` | SELL | 0.22067 | `1f0fb426-0404-4acc-b5d6-738ceb352479` |
| `ETH-USD` | SELL | 2477.01 | `692335b5-fa56-42f1-8a4c-de724007a342` |
| `LINK-USD` | BUY | 11.523 | `a8cd91af-b0a3-426f-a673-6daf89c51f48` |
| `AVAX-USD` | BUY | 7.512 | `a90a3078-8c18-4d6b-b207-68245b7a2324` |
| `DOGE-USD` | BUY | 0.08894 | `e96d645a-054d-417e-9138-337ced614ac4` |
| `ADA-USD` | BUY | 0.21904 | `735cf17a-dd00-47b2-b812-3b3f72dc0a80` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 4.7h ago (2026-08-24 08:03 AM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-24 01:12:31 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **150.2h (6d 6h 12m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-24 12:47:59 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **149.2h (6d 5h 11m)**)
- **Selected Mega Cap Universe**: `BTC, ADA, ETH, DOGE, SUI, XRP, SOL, ZEC`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  07:47:50 PM
   CPU:   3.5%  |  MEM:   7.1% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 2582693  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 2583412  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader ETH-USD       | 2584575  | COOL-DOWN       | 4        | Next run in 4.2s
Trader ADA-USD       | 2584103  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 2584104  | RUNNING         | 3        | Evaluating Funnel/Polling Order
Trader BTC-USD       | 2584576  | COOL-DOWN       | 4        | Next run in 4.2s
Trader LINK-USD      | 2583417  | RUNNING         | 1        | Evaluating Funnel/Polling Order
Trader SOL-USD       | 2584577  | COOL-DOWN       | 4        | Next run in 4.2s
================================================================================
```

---
## 6. ☀️ Mac Mini Day Trader Intelligence & PnL
**Guardian Watchdog Status**: 🟢 ONLINE

### 💰 Cumulative PnL Dashboards
| Environment | Total Trades | Win Rate | Net PnL (USD) |
| :--- | :--- | :--- | :--- |
| **LIVE EC2** | 0 | N/A | **$+0.00** |
| **SHADOW (Paper)** | 0 | N/A | **$+0.00** |

---
## 7. ⚠️ Actionable Error & Incident Radar (Last 10h)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 18:20:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [DOGE-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_DOGE_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_DOGE_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_DOGE_USD.log:2026-08-24 08:35:42 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.17s... | Error: ('Connection aborted.', ConnectionResetErr
logs/watchdog_Trader_ETH_USD.log:2026-08-23 07:45:04 [ERROR] [async_sfgk_trader.py:fetch_live_state:492] [ETH-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 328) (Fail-Closed)
logs/watchdog_Trader_ETH_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_ETH_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 328)
logs/watchdog_Trader_ETH_USD.log:2026-08-23 07:49:57 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.26s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 08:52:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.34s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 08:52:35 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 09:26:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.42s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 22:09:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-23 22:09:23 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_ETH_USD.log:2026-08-24 05:05:07 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.46s... | Error: 502 Server Error: Bad Gateway <html>
logs/watchdog_Trader_ETH_USD.log:    <style>@font-face{font-display:swap;font-family:CoinbaseDisplay;src:url(data:font/woff2;base64,d09GMgABAAAAAJ64ABAAAAAB1EgAAJ5UAAEIMQAAAAAAAAAAAAAAAAAAAAAAAAAAG4GJWhylHAZgAI5UCIFwCZdiEQgKhN1EhJpmATYCJAOZTAuMagAEIA
logs/watchdog_Trader_ETH_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_ETH_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_ETH_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_ETH_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_ETH_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background-
logs/watchdog_Trader_ETH_USD.log:2026-08-24 08:35:39 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [ETH-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_order | Sleeping 1.39s... | Error: ('Connection aborted.', ConnectionResetError
logs/watchdog_Trader_LINK_USD.log:2026-08-23 08:52:34 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.23s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-23 09:26:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.35s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_LINK_USD.log:2026-08-23 18:20:16 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [LINK-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_LINK_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_LINK_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_SOL_USD.log:2026-08-23 04:08:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.43s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 04:08:20 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.11s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.18s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_SOL_USD.log:2026-08-23 07:14:47 [WARNING] [async_sfgk_trader.py:_safe_requests_get:249] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.14s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
logs/watchdog_Trader_SOL_USD.log:2026-08-23 16:48:07 [ERROR] [async_sfgk_trader.py:fetch_live_state:492] [SOL-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 13 column 1 (char 339) (Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_SOL_USD.log:json.decoder.JSONDecodeError: Extra data: line 13 column 1 (char 339)
logs/watchdog_Trader_SOL_USD.log:2026-08-23 18:20:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [SOL-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_SOL_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_SOL_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
logs/watchdog_Trader_SOL_USD.log:2026-08-24 04:03:44 [WARNING] [async_sfgk_trader.py:_safe_requests_get:249] [SOL-USD] requests.get Exception (Attempt 1/5). Sleeping 1.50s... | Error: HTTPSConnectionPool(host='api.exchange.coinbase.com', port=443): R
```
</details>

