# 🛡️ Unified Trading System Hourly Status & Visual Intelligence
> **Report Generated**: `2026-08-13 06:47:16 PM PDT (2026-08-14 01:47:16 UTC)`  
> **System Health**: **🟢 ALL SYSTEMS NOMINAL** | **Win Rate**: `0.0%` | **Completed Trades**: `0`

---
## 1. ⚡ Macro Volatility & Layer 1 DAW Causal Oracle
Real-time Deribit implied volatility (DVOL) proxy tracking against mathematically optimal Yield System Parameters (YSP) per asset.

| Symbol | Proxy Oracle | Live Z-Score | Optimal Limit (YSP) | Safety Margin | Live VRP | Optimal VRP (YSP) | DAW Safety Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AVAX-USD` | DVOL_BTC | **-2.15** | **-0.50** | **-1.65** | **+14.20** | 5.0 | 🟢 SAFE |
| `ETH-USD` | DVOL_ETH | **-1.10** | **-0.50** | **-0.60** | **+28.09** | 5.0 | 🟢 SAFE |
| `ADA-USD` | DVOL_BTC | **-2.15** | **-0.50** | **-1.65** | **+14.20** | 5.0 | 🟢 SAFE |
| `DOGE-USD` | DVOL_BTC | **-2.15** | **-0.50** | **-1.65** | **+14.20** | 5.0 | 🟢 SAFE |
| `BTC-USD` | DVOL_BTC | **-2.15** | **-0.50** | **-1.65** | **+14.20** | 5.0 | 🟢 SAFE |
| `LINK-USD` | DVOL_BTC | **-2.15** | **-0.50** | **-1.65** | **+14.20** | 5.0 | 🟢 SAFE |
| `SOL-USD` | DVOL_BTC | **-2.15** | **-0.50** | **-1.65** | **+14.20** | 5.0 | 🟢 SAFE |

![DVOL Market Regime](./images/dvol_regime_timeline.png)

![VRP Chart AVAX-USD](./images/vrp_chart_AVAX-USD.png)  

![VRP Chart ETH-USD](./images/vrp_chart_ETH-USD.png)  

![VRP Chart ADA-USD](./images/vrp_chart_ADA-USD.png)  

![VRP Chart DOGE-USD](./images/vrp_chart_DOGE-USD.png)  

![VRP Chart BTC-USD](./images/vrp_chart_BTC-USD.png)  

![VRP Chart LINK-USD](./images/vrp_chart_LINK-USD.png)  

![VRP Chart SOL-USD](./images/vrp_chart_SOL-USD.png)  

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
| ✅ | **Go-List JSON** | Fresh (29.44h old) | 08-12 13:21 |
| ✅ | **TimesFM Forecasts** | Fresh (2.76h old) | 08-13 16:02 |
| ✅ | **Holding Times config** | Fresh (33.13h old) | 08-12 09:39 |
| ✅ | **BTC DVOL Cache** | Fresh (0.00h old) | 08-13 18:47 |
| ✅ | **ETH DVOL Cache** | Fresh (0.01h old) | 08-13 18:47 |
| ✅ | **Live Trading Telemetry** | Fresh (0.00h old) | 08-13 18:47 |

<br>

> **Utilization Certification**: ✅ **CERTIFIED.** The Guardian Watchdog is ONLINE and EC2 traders are actively querying the freshest MLOps data artifacts (Found 1946 recent read events).


---
## 2. 📊 8-Stage Funnel Live Decision Telemetry
Layer-by-layer tick evaluation waterfall and asset-specific performance tracking.

| Funnel Filter Layer | Total Rejections | % of Rejections |
| :--- | :--- | :--- |
| Layer 1: DAW Causal Volatility Veto | `128,476` | **99.5%** |
| Layer 2A: Vol Surface Skew & VRP Gate | `0` | **0.0%** |
| Layer 2B: DVOL Directional Momentum Bias | `0` | **0.0%** |
| Layer 2C: KER Efficiency Noise Filter | `0` | **0.0%** |
| Layer 2.5: TimesFM Forecast Velocity Gate | `0` | **0.0%** |
| Layer 3: SDR Liquidity Sizing Floor | `0` | **0.0%** |
| Layer 4: SFGK Commercial Margin Gate (< 0.25%) | `605` | **0.5%** |
| Layer 5: Hawkes Microstructure Toxicity | `0` | **0.0%** |
| System: Asset Cooldown Active | `0` | **0.0%** |
| System: Asset Blacklist Gate | `0` | **0.0%** |

![8-Stage Funnel Rejection Waterfall](./images/funnel_waterfall_breakdown.png)

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
| `USD` | 0.00 | 0.00 | **0.00** |

### Open Maker Orders on the Book
| Product | Side | Limit Price | Order ID |
| :--- | :--- | :--- | :--- |
| *None* | - | - | No active maker orders |

![24-Hour Realized P&L](./images/realized_pnl_timeline.png)

---
## 4. 🤖 Foundation Model MLOps & Pipeline Orchestration
Weekly Algorithmic Mega Cap selection, Zero-shot multi-step forward return forecasts, and VSTEF parameter grid search status.

- **TimesFM Forecast DB**: 🟢 Updated 2.8h ago (2026-08-13 04:02 PM PDT)
- **Last Weekly VSTEF Optimization**: `2026-08-12 01:22:32 PM PDT`
- **Next Scheduled VSTEF Run**: `2026-08-16 07:00:00 PM PDT (Monday 02:00 UTC)` (Countdown: **72.2h (3d 0h 12m)**)
- **Promoted Parameter Gates**: $Z_{DVOL} \le -0.5$ | Holding Horizon $= 12\text{h}$

### Algorithmic Mega Cap Selection
- **Last Run (Confirmation)**: `2026-08-12 02:28:22 PM PDT`
- **Next Scheduled Run**: `2026-08-16 06:00:00 PM PDT (Monday 01:00 UTC)` (Countdown: **71.2h (2d 23h 12m)**)
- **Selected Mega Cap Universe**: `BTC, ETH, LSETH, LINK, UNI, XRP, SOL, ZEC`

![TimesFM Forecast Matrix](./images/timesfm_forecast_matrix.png)

### 📈 VSTEF Grid Search Sweep Results
Visualizing the impact of the VSTEF (Volatility-Synchronized Stop-Tightening Execution Filter) gating across the active crypto universe vs Baseline.
![Sweep ROI Comparison](./images/sweep_roi_comparison.png)
![Sweep Win Rate Scatter](./images/sweep_winrate_scatter.png)

---
## 5. 🖥️ Multi-Node Infrastructure & Watchdog Matrix
```text
================================================================================
   🛡️  SFGK FUNNEL GUARDIAN WATCHDOG (HFT ONLY) |  01:47:14 AM
   CPU:  37.4%  |  MEM:   6.3% (14.4GB / 15.4GB Free)
================================================================================
SERVICE              | PID      | STATUS          | RESTARTS | INFO
--------------------------------------------------------------------------------
L3 Consumer          | 1951000  | RUNNING         | -        | Continuous Websocket Feed
Trader AVAX-USD      | 1959730  | COOL-DOWN       | 26       | Next run in 14.8s
Trader ETH-USD       | 1959731  | COOL-DOWN       | 26       | Next run in 14.8s
Trader ADA-USD       | 1959732  | COOL-DOWN       | 26       | Next run in 14.8s
Trader DOGE-USD      | 1959733  | COOL-DOWN       | 26       | Next run in 14.8s
Trader BTC-USD       | 1959734  | COOL-DOWN       | 26       | Next run in 14.8s
Trader LINK-USD      | 1959735  | COOL-DOWN       | 26       | Next run in 14.8s
Trader SOL-USD       | 1959736  | COOL-DOWN       | 26       | Next run in 14.8s
================================================================================
```

---
## 6. ☀️ Mac Mini Day Trader Intelligence
**Day Trader Watchdog Status**: 🟢 ONLINE

Error reading recommendations: name 'pd' is not defined

---
## 7. ⚠️ Actionable Error & Incident Radar (Last 10h)
<details>
<summary><b>Click to expand raw incident logs</b></summary>

```text
logs/watchdog_Trader_LINK_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_LINK_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_LINK_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_LINK_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_LINK_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background
logs/watchdog_Trader_LINK_USD.log:2026-08-13 22:30:02,947 - ERROR - HTTP Error: 502 Server Error: Bad Gateway <html>
logs/watchdog_Trader_LINK_USD.log:    <style>@font-face{font-display:swap;font-family:CoinbaseDisplay;src:url(data:font/woff2;base64,d09GMgABAAAAAJ64ABAAAAAB1EgAAJ5UAAEIMQAAAAAAAAAAAAAAAAAAAAAAAAAAG4GJWhylHAZgAI5UCIFwCZdiEQgKhN1EhJpmATYCJAOZTAuMagAEI
logs/watchdog_Trader_LINK_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_LINK_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_LINK_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_LINK_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_LINK_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background
logs/watchdog_Trader_LINK_USD.log:2026-08-13 22:30:02,979 - WARNING - [LINK-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.36s... | Error: 502 Server Error: Bad Gateway <html>
logs/watchdog_Trader_LINK_USD.log:    <style>@font-face{font-display:swap;font-family:CoinbaseDisplay;src:url(data:font/woff2;base64,d09GMgABAAAAAJ64ABAAAAAB1EgAAJ5UAAEIMQAAAAAAAAAAAAAAAAAAAAAAAAAAG4GJWhylHAZgAI5UCIFwCZdiEQgKhN1EhJpmATYCJAOZTAuMagAEI
logs/watchdog_Trader_LINK_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_LINK_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_LINK_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_LINK_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_LINK_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background
logs/watchdog_Trader_SOL_USD.log:2026-08-13 22:24:18 - coinbase.RESTClient - ERROR - HTTP Error: 502 Server Error: Bad Gateway <html>
logs/watchdog_Trader_SOL_USD.log:    <style>@font-face{font-display:swap;font-family:CoinbaseDisplay;src:url(data:font/woff2;base64,d09GMgABAAAAAJ64ABAAAAAB1EgAAJ5UAAEIMQAAAAAAAAAAAAAAAAAAAAAAAAAAG4GJWhylHAZgAI5UCIFwCZdiEQgKhN1EhJpmATYCJAOZTAuMagAEIA
logs/watchdog_Trader_SOL_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_SOL_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_SOL_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_SOL_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_SOL_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background-
logs/watchdog_Trader_SOL_USD.log:2026-08-13 22:24:18,844 - ERROR - HTTP Error: 502 Server Error: Bad Gateway <html>
logs/watchdog_Trader_SOL_USD.log:    <style>@font-face{font-display:swap;font-family:CoinbaseDisplay;src:url(data:font/woff2;base64,d09GMgABAAAAAJ64ABAAAAAB1EgAAJ5UAAEIMQAAAAAAAAAAAAAAAAAAAAAAAAAAG4GJWhylHAZgAI5UCIFwCZdiEQgKhN1EhJpmATYCJAOZTAuMagAEIA
logs/watchdog_Trader_SOL_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_SOL_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_SOL_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_SOL_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_SOL_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background-
logs/watchdog_Trader_SOL_USD.log:2026-08-13 22:24:18,853 - WARNING - [SOL-USD] Coinbase API Call Exception (Attempt 1/5). Func: get_product | Sleeping 1.27s... | Error: 502 Server Error: Bad Gateway <html>
logs/watchdog_Trader_SOL_USD.log:    <style>@font-face{font-display:swap;font-family:CoinbaseDisplay;src:url(data:font/woff2;base64,d09GMgABAAAAAJ64ABAAAAAB1EgAAJ5UAAEIMQAAAAAAAAAAAAAAAAAAAAAAAAAAG4GJWhylHAZgAI5UCIFwCZdiEQgKhN1EhJpmATYCJAOZTAuMagAEIA
logs/watchdog_Trader_SOL_USD.log:    <div id="cloudflare-error" style="display:none;">::CAPTCHA_BOX:: ::IM_UNDER_ATTACK_BOX:: <div class="cf-error-details cf-error-502">
logs/watchdog_Trader_SOL_USD.log:  <p>The web server reported a bad gateway error.</p>
logs/watchdog_Trader_SOL_USD.log:    <li>Error reference number: 502</li>
logs/watchdog_Trader_SOL_USD.log:</div> ::CLOUDFLARE_ERROR_1000S_BOX:: ::ALWAYS_ONLINE_NO_COPY_BOX::</div>
logs/watchdog_Trader_SOL_USD.log:    <div class="cds-large-llfbhh8 cds-light-l1k3tbpe" style="--foreground:rgb(var(--gray100));--foreground-muted:rgb(var(--gray60));--background:rgb(var(--gray0));--background-alternate:rgb(var(--gray5));--background-
```
</details>

