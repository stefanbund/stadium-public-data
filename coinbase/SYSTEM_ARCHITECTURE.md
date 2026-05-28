# Crypto Forecasting System | Unified Architecture Blueprint (CCXT Era)

This document provides a fresh, comprehensive overview of the current "DVOL-Inverse" production system. It reflects the unified machine model where sampling, modeling, and trading are co-located on the primary host, powered by CCXT for exchange-agnostic execution.

---

## 1. System Orchestration: Guardian 2.0
The [Guardian Watchdog](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/guardian.py) is the central daemon managing the system's lifecycle across four stages.

### **Staged Boot Sequence**
- **Stage 1: The Sensors**
    - **CCXT LOB Sampler**: [`UNIFIED_TRADER_WORKSPACE/ccxt_sampler.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/ccxt_sampler.py)
        - *Role*: Continuously streams Limit Order Book (LOB) depth and price data using the CCXT library.
        - *Rotation*: Automatically rotated every 6 hours to ensure file I/O efficiency.
        - *Disk Space Optimization*: Supports config-driven automated pruning (`dur_pipe.prune_old_lob_files` in `config.local.json`) to keep only the 3 most recent files, preventing file accumulation on remote servers where historical backtesting files are not needed.
    - **Mobile Log Exporter**: [`periodic_log_export.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/periodic_log_export.py)
        - *Role*: Syncs critical telemetry to Google Drive for remote monitoring via Gemini.
- **Stage 2: Intelligence & Execution**
    - **MLOps Orchestrator (Local)**: [`UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py)
        - *Mode*: `--fast-rf` (Standard Random Forest baseline for high-velocity deployment).
        - *Role*: Manages the A-Z symbol modeling loop.
    - **Mega Cap LSTM Orchestrator**: [`UNIFIED_MLOPS_WORKSPACE/orchestrator_mega_cap_lstm.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/orchestrator_mega_cap_lstm.py)
        - *Role*: Sequentially trains 100 mega-cap cryptocurrency LSTM models in a **continuous retraining state** (re-initiating immediately upon cycle completion) and automatically uploads completed models to the remote AWS EC2 production host.
    - **Hierarchical Trader**: [`UNIFIED_TRADER_WORKSPACE/trader_NN_HIERARCHICAL.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/trader_NN_HIERARCHICAL.py)
        - *Condition*: Only starts after confirming active LOB data flow.
        - *Role*: Processes live signals through the neural hierarchy.
- **Stage 3: [Reserved]**
- **Stage 4: Visualization**
    - **Reporting Orchestrator**: [`UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py)
        - *Role*: Sequential execution of all reporting heartbeats (Accuracy, Strategy, Operations).

---

## 2. Neural Intelligence Hierarchy
The system now operates on a **2-Tier Ultra-Lean Waterfall** decision engine, optimized for high-velocity execution and alpha preservation. This stack was finalized during the `FIS_INDUSTRIAL_LEAN_v1` experiment, which proved that bypassing durational complexity leads to superior risk-adjusted returns.

1.  **Tier 0: Dynamic Volatility Governor (DVG)**
    - *Source*: `DAW_CAUSALITY_LAYER/causality_layer.py`
    - *Mechanism*: Acts as a macro-risk firewall by modulating the fused execution threshold based on the **DVOL Z-score**. 
    - *Adaptive Logic*: `Effective_Threshold = Base * (1 + max(0, Z/2))`. This ensures the "Lean Shield" tightens automatically during high-volatility exhaustion regimes.
2.  **Tier 1: Directional (Trend)**
    - *Threshold*: Configured in `global_config.json` (default 0.85).
    - *Role*: Identifies primary upward price vectors.

> **Legacy/Retired Tiers**:
> - **Crash (Safety)**: Retired May 2026. Vetoed trades if a significant drawdown (>3%) was imminent.
> - **Imbalance (Tier 2)**: Retired May 2026. Superseded by the DAW Causal Gate.
> - **Markov Risk (Tier 3)**: Retired May 2026. Superseded by the DAW Causal Gate.
> - **Generalist (Tier 5)**: Retired May 2026. Bypassed in favor of the Lean stack.
> - **Specialist (Tier 6)**: Retired May 2026. Bypassed in favor of the Lean stack.

---

## 3. Live Inference & Workflow
1.  **Buffer Management**: The predictor fetches minimal recent context from the exchange API or local cache.
2.  **In-Memory Calculation**: Indicators (RSI, EMAs, ATR) are computed instantly within the agent's memory space.
3.  **Hierarchical Evaluation (Lean Stack)**:
    - **Step 1**: Does the macro regime allow for alpha? (**DAW Gate**)
    - **Step 2**: Should I buy? (**Directional Trend**)
4.  **Action Handoff**: Executable signal is generated only if both active tiers provide a "Green Light." It then hands off control to the `async_trader_rewritten.py` layer.

### The Brain vs. The Hands (Role Separation)
An important distinction in the architecture is the strict separation of responsibilities between `trader_NN_HIERARCHICAL.py` (The Brain) and `async_trader.py` (The Hands).

- **The Brain: `trader_NN_HIERARCHICAL.py` (The Orchestrator)**
  - **Data Intake & Modeling:** Continuously monitors live market data, calculates technical indicators (ATR, RSI, etc.), and feeds them into machine learning models for predictions.
  - **Risk Management:** Applies strict waterfall logic—checking the DAW Causality volatility firewall, ensuring trend confidence, and verifying the symbol isn't blacklisted.
  - **Capital Allocation:** Checks the live USD account balance, classifies the coin as a Mega Cap or Mid Cap, and calculates the exact dollar size and dynamic profit target (e.g., using ATR).
  - **Delegation:** Once it decides exactly *what* to do, it launches `async_trader.py` and hands it the specific execution instructions.

- **The Hands: `async_trader.py` (The Execution Engine)**
  - **Broker Interface:** Receives the symbol, dollar amount, and profit target from the Orchestrator, logs into the exchange API, and submits the Limit Buy order.
  - **Order Management:** Waits for the Buy order to be filled. Once filled, it mathematically calculates the take-profit price and submits the Sell order.
  - **Safety Protocols:** Handles retries for API errors and monitors the 4-hour "Circuit Breaker." If a Sell order sits for too long, it cancels it and executes an emergency liquidation.
  - **Telemetry:** Records the exact profit, latency, and success into the CSV logs and triggers the reporting scripts.

By splitting these roles, the system is highly efficient—the heavy machine learning loop never gets paused or delayed while waiting for a slow exchange API to fill a trade.

---

## 4. Data Architecture & Logistics
The system utilizes a unified machine model where all processing is co-located to minimize latency and synchronization overhead.

- **Primary Data Root**: `/Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/STADIUM_DATA`
- **Model Vault**: `STADIUM_DATA/MODELS` (Subdivided into Directional; Crash is legacy).
- **LOB Source Truth**: `/Volumes/M4_BACKUP/GRUS-CSV-SAMPLER-DATA`
- **Hardware Bridging**: The system is designed to run entirely on the host SSD for execution speed, with scheduled backups to external volumes handled by `local_usb_backup.sh`.
- **Telemetry Sync**:
  - **Local to Data Science Host**: Hourly synchronization of critical local MLOps runtime logs to the centralized data science host (`okx-ml.local`) is managed by the Guardian Watchdog calling `scripts/sync_logs_to_ml_host.sh`.
  - **EC2 to Reporting Workspace**: Because the active trader and LOB sampler now run in the cloud on EC2, logs (`trading_bot.log`, `executions_log.csv`, and audit logs) are dynamically pulled from the remote host (`98.93.0.208`) to local (`logs/remote`) via `scripts/pull_remote_logs.sh` at the start of each execution loop inside the Reporting Workspace (`generate_ledger_data.py`).
  - **Preferred Markets Upload**: Upon regeneration of `preferred_markets.json` by the local MLOps script (`yield_stability_profiler.py`), the file is automatically transferred via rsync/SSH to the production Amazon instance (`98.93.0.208`) at `/opt/hft_trader/FLEET_INFORMATION_SYSTEM/preferred_markets.json` using the local SSH private key (`hft-trader-key.pem`), keeping the AWS trader in sync with local MLOps asset selection.
  - **Continuous LSTM Model Upload**: Immediately upon successful completion of each individual symbol training cycle inside the Mega Cap LSTM Orchestrator, the new `.pt` model is uploaded using the local private key (`hft-trader-key.pem`) to the remote EC2 instance (`98.93.0.208`) under `/opt/hft_trader/STADIUM_DATA/MODELS/CORE_MODULES/`, keeping the cloud neural network synchronized with local model retraining in real time.

---

## 5. Operational Control & Configuration
- **Global Config**: [`global_config.json`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/global_config.json)
    - The single source of truth for all paths, thresholds, and exchange-specific parameters.
- **Shared Library**: [`shared_lib/config_loader.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/shared_lib/config_loader.py)
    - Dynamically resolves paths and injects environment secrets (Twilio, GitHub PAT).
- **Command Wrapper Suite**:
    - `scripts/start_guardian.sh`: Launches the system.
    - `scripts/stop_guardian.sh`: Safe shutdown.
    - `scripts/status.sh`: System health snapshot.

### **Deployment & Post-Deployment Verification**
- **Deployment Helper**: [`UNIFIED_TRADER_WORKSPACE/deployment_helper.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/deployment_helper.py)
    - *Role*: Handles code/config sync, builds virtual environments, and sets execution flags.
- **Certification Verifier**: [`scripts/deployment_verifier.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/scripts/deployment_verifier.py)
    - *Role*: Automatically executes on the remote host post-deploy to certify system integrity (checking for credentials/key leaks, virtual environment health, LSTM and Directional model availability, and AWS Secrets Manager integration).

---

## 6. Analytics & Public Telemetry
All visual intelligence is compiled and published via the system reporting scripts.

- **Legacy GitHub Pages Hub**: [View Hub](https://stefanbund.github.io/stadium-public-data/coinbase/analytics_dashboard.html) (Updates siloed by exchange name, e.g., `/coinbase`).
- **Modern Unified Dashboard (metastadium.web.app)**: Hosted on Google Firebase.
  - **Reporting Workspace**: Managed inside [`MODERN_REPORTING_WORKSPACE/`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/MODERN_REPORTING_WORKSPACE/) and governed by `orchestrator.py` on a 15-minute run cycle.
  - **Dynamic Compilation**: Computes and updates `dashboard_data.json` (via `generate_data.py`), `ledger_data.json` (via `generate_ledger_data.py`), and `landscape_data.json` (via `generate_data.py`).
  - **Market Volatility & NN Audits**: Regenerates live DVOL oracle metrics and parses the last 200 neural network evaluations to dynamically refresh the Go-List tree hierarchy and DVG regime status on the website's Market Landscape page (`landscape.html`) on every update cycle.

---

## 7. Fleet Information System (FIS)
The industrial backtesting arm of the project, used for yield discovery and parameter hardening.

- **Workspace**: `FLEET_INFORMATION_SYSTEM/`
- **Industrial Lean Baseline**: Standardized on high-velocity Random Forest models (`--fast-rf`) to bypass compute-heavy TPOT searches during fleet-wide deployment.
- **Experiment Vault**: `FLEET_INFORMATION_SYSTEM/EXPERIMENTS/FIS_INDUSTRIAL_LEAN_v1` (The definitive system blueprint).

---

## 8. Operational Workflows
The system defines standard operational workflows inside `.agents/workflows/` to simplify diagnostics, auditing, and deployment.

- **Market Landscape View**: [`.agents/workflows/market_landscape.md`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/.agents/workflows/market_landscape.md)
  - *Utility*: Runs `summarize_market_landscape.py` to query the live DVOL Oracle (Z-score, trend, RSI) and parse the last 200 neural network evaluations to diagnose execution pauses.
- **Summarize Recent Trades**: [`.agents/workflows/summarize_recent.md`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/.agents/workflows/summarize_recent.md)
  - *Utility*: Aggregates trade statuses (PASS/FAIL/PENDING) per symbol to see live execution history.

---

## 15. Archival Note
The legacy documentation and decommissioned tools (Pre-CCXT/Pre-DVOL) have been moved to `TECHNICAL_DEBT/`:
- [`OLD_SYSTEM_ARCHITECTURE.md`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/TECHNICAL_DEBT/OLD_SYSTEM_ARCHITECTURE.md)
- `advanced-sdk-ts/` (Legacy Node.js LOB Sampler)

