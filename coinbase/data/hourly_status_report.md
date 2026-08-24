---
layout: default
---

# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-23 11:29:24 PM PDT (2026-08-24 06:29:24 UTC)`  
> **System Health**: **🟡 DEGRADED / RESTRICTED** | **Win Rate**: `0.0%` | **Completed Trades**: `0`


> 🖼️ **[View Detailed Visual Intelligence & 3-Tier Profiling Graphs](./visual_intelligence.html)**

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **+0.70** | **-0.50** | **+1.20** | **+3.59** | 5.0 | 🔴 DAW VETOED |
| `ETH-USD` | DVOL_ETH | **+0.36** | **-0.50** | **+0.86** | **+20.19** | 5.0 | 🔴 DAW VETOED |
| `ADA-USD` | DVOL_BTC | **+0.70** | **-0.50** | **+1.20** | **+3.82** | 5.0 | 🔴 DAW VETOED |
| `DOGE-USD` | DVOL_BTC | **+0.70** | **-0.50** | **+1.20** | **+4.02** | 5.0 | 🔴 DAW VETOED |
| `BTC-USD` | DVOL_BTC | **+0.70** | **-0.50** | **+1.20** | **+4.04** | 5.0 | 🔴 DAW VETOED |
| `LINK-USD` | DVOL_BTC | **+0.70** | **-0.50** | **+1.20** | **+3.79** | 5.0 | 🔴 DAW VETOED |
| `SOL-USD` | DVOL_BTC | **+0.70** | **-0.50** | **+1.20** | **+4.04** | 5.0 | 🔴 DAW VETOED |



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
| ❌ | **Go-List JSON** | STALE! (28.1h old) | Limit 5.5h |
| ✅ | **TimesFM Forecasts** | Fresh (0.74h old) | 08-23 22:44 |
| ❌ | **Holding Times config** | STALE! (62.4h old) | Limit 4.5h |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-23 23:29 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-23 23:29 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-23 23:29 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 0 recent read events).


---
## 2. 📊 3-Tier Fused Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Tier 1: Macro Volatility Tensor Gate (Omega_macro) | `29,454` | **100.0%** |
| Tier 2: Unified Transport & Directional Engine | `0` | **0.0%** |
| Tier 3: Continuous Hawkes-SFGK Pricer (HAS-Pricer) | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |
| Legacy / Unknown Veto | `0` | **0.0%** |



### Active Universe Performance & Drift Matrix

| Asset | Trades | Win Rate | Loss Streak | Status |
| :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | 12 | 100.0% | 0 | 🟢 OK |
| `LINK-USD` | 12 | 83.3% | 0 | 🟢 OK |
| `DOGE-USD` | 10 | 100.0% | 0 | 🟢 OK |
| `ADA-USD` | 13 | 92.3% | 0 | 🟢 OK |
| `SOL-USD` | 6 | 100.0% | 0 | 🟢 OK |
| `BTC-USD` | 3 | 66.7% | 1 | 🟢 OK |
| `ETH-USD` | 5 | 80.0% | 0 | 🟢 OK |

---
## 3. 💰 Coinbase Treasury, Balances & Active Orders
Live balance sheet and open maker liquidity positions from Coinbase CDP.


### Open Maker Orders on the Book

| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| `ACH-USD` | SELL | 0.005507 | `a0d2e243-42b4-4df5-bd23-118f45998df8` |
| `AVAX-USD` | SELL | 7.518 | `f50639b0-d520-4461-961b-d87b88603fc5` |
| `DOGE-USD` | SELL | 0.09287 | `07f5c08a-d2c0-4ed8-91a5-7946d105e783` |
| `ADA-USD` | SELL | 0.22154 | `1ab7ef34-9f8d-429f-8f99-ac0a875c6a74` |
| `ADA-USD` | SELL | 0.22053 | `539cf25c-4aa9-40da-82fe-af93457912c2` |
| `LINK-USD` | SELL | 11.558 | `8a082dea-8547-4f42-ac87-24fc89fd7bfb` |



---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 0.7h ago (2026-08-23 10:44 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-05 09:22:38 AM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-30 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **163.5h (6d 19h 30m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-22 07:25:41 PM PDT`
- **Next Scheduled Run**: `2026-08-30 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **162.5h (6d 18h 30m)**)
- **Selected Mega Cap Universe**: `BTC, BCH, AVAX, ETH, ALGO, ADA, LTC, DOGE, AAVE, LINK, DOT, HBAR`



### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.



---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  06:29:21 AM
   CPU:  12.0%  |  MEM:   7.0% (14.3GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1874980  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1898552  | RUNNING         | 34       | Evaluating Funnel/Polling Order
Trader ETH-USD       | 1909934  | RUNNING         | 87       | Evaluating Funnel/Polling Order
Trader ADA-USD       | 1901690  | RUNNING         | 63       | Evaluating Funnel/Polling Order
Trader DOGE-USD      | 1909829  | COOL-DOWN       | 73       | Next run in 14.6s
Trader BTC-USD       | 1909751  | COOL-DOWN       | 115      | Next run in 4.1s
Trader LINK-USD      | 1902670  | RUNNING         | 73       | Evaluating Funnel/Polling Order
Trader SOL-USD       | 1909752  | COOL-DOWN       | 115      | Next run in 4.1s
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
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.15s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:06:36 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.49s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.14s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 06:08:22 [WARNING] [async_sfgk_trader.py:_execute_api_call:213] [DOGE-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.24s... | Error: 429 Client Error: Too Many Requests 
logs/watchdog_Trader_DOGE_USD.log:2026-08-23 18:20:15 [ERROR] [async_sfgk_trader.py:fetch_live_state:527] [DOGE-USD] CRITICAL: Failed to fetch DVOL from oracle or check dependencies: Extra data: line 12 column 2 (char 339) (Fail-Closed)
logs/watchdog_Trader_DOGE_USD.log:    raise JSONDecodeError("Extra data", s, end)
logs/watchdog_Trader_DOGE_USD.log:json.decoder.JSONDecodeError: Extra data: line 12 column 2 (char 339)
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

