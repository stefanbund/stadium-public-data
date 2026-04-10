# Crypto Forecasting System | Architecture Blueprint

This document provides a comprehensive overview of the current working system, cataloging all key components, their locations, and their roles in the multi-phase machine learning pipeline.

---

## 1. Orchestration & Logistics (`UNIFIED_MLOPS_WORKSPACE`)
The central nervous system that manages the sequential execution for each symbol. All Laboratory logic is strictly physically segregated into the `/UNIFIED_MLOPS_WORKSPACE` directory to maintain a pristine project root.

- **Guardian Watchdog**: [`guardian.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/guardian.py) [NEW]
    - *Role*: The overarching process manager daemon that maintains continuous uptime for the LOB Sampler, MLOps Orchestrator, Hierarchical Trader, and Reporting mechanisms.
    - *Staged Startup Protocol*: To prevent system-wide OOM (Out Of Memory) crashes and CPU spikes during cold boots, the Guardian implements a 3-stage initialization sequence:
        - **Stage 1 (Immediate)**: Launches the Live LOB Sampler and Mobile Log Exporter.
        - **Stage 2 (+30s)**: Launches the MLOps and Reporting Orchestrators once data flow is initialized.
        - **Stage 3 (+120s & Condition)**: Launches the Hierarchical Trader only after confirming that fresh LOB CSV data is actively being written to the `/STADIUM_DATA/GRUS-CSV-SAMPLER-DATA` directory.
    - *Memory Protection (Trader)*: The watchdog manages a "Memory Firewall" within the trader initialization loop. The trader loads symbols with a 5-second stagger and forces Garbage Collection (`gc.collect()`) after every model load. If system memory exceeds **85%**, the boot sequence pauses for 30s to allow memory to stabilize.
    - *Sampler Rotation*: Automatically restarts the Live LOB Sampler every **6 hours** to force a clean file rotation, preventing individual CSV files from exceeding optimal I/O size limits.
    - *Thermal Throttling*: Because the M4 host is fanless, the watchdog strictly limits the orchestrator sub-process to 2 parallel workers and incorporates a 20-second per-symbol sleep loop to prevent extreme CPU load and thermal-related hardware reboots.
    - *Analytics Integration*: Periodically dumps live component lifecycle data (restart counts, runtime statuses) to `guardian_status.json` for external telemetry harvesting.
    - *Twilio Alerting*: Automatically senses microservice crashes or execution freezes and natively issues SMS alerts to system admins via the Twilio REST API.
    - *Age-Based Restart Policy*: On any auto-restart, the Guardian launches the orchestrator with `--skip-existing --max-age-days 14`. This instructs the orchestrator to skip any preprocessing or modeling step whose output file was modified within the last **14 days**, preventing redundant rework. Steps older than 14 days (or missing entirely) are re-executed. This applies to **all** model types including Imbalance, which can take up to 7 days to train and is therefore only triggered once every two weeks at most. To force a full re-run of everything, pass `--max-age-days 0`.
- **Main MLOps Orchestrator**: [`UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py)
    - *Role*: The primary entry point for model training. Manages the loop across all **261 symbols**, calling preprocessors, modelers, and transfer scripts.
    - *Symbol Discovery*: Prioritizes the "Source Truth" by scanning the `GRUS-CSV-SAMPLER-DATA/symbols` directory for per-asset CSVs. This ensures 100% coverage across the alphabet (A-Z), with fallbacks to preprocessed BBP files if the source directory is unavailable.
- **Reporting Orchestrator**: [`UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py) [NEW]
    - *Role*: Consolidates all independent analytics heartbeats into a single, sequential pipeline.
    - *Sequential Efficiency*: Eliminates CPU and I/O contention by running Accuracy, Transaction, and Strategy updates one after another with a 5-second "breathing gap" between tasks. 
    - *Frequencies*: 
        - **Accuracy & Transactions**: Every 30 minutes.
        - **Strategy Performance**: Every 24 hours (to conserve thermal resources).
        - **Analytics Hub**: Refreshed automatically after every successful cycle.
- **Data Transfer**: [`UNIFIED_MLOPS_WORKSPACE/transfer.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/transfer.py)    - *Role*: Moves processed data and model artifacts between local storage and the high-volume backup volumes.
    - *Usage (Global Run)*: The watchdog handles background execution, but for isolated manual runs: `nohup ./venv/bin/python UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py --host stefans-Mac-mini.local --pull --workers 2 > logs/orchestrator_main.log 2>&1 &`
    - *Usage (Global Wipe & Restart)*: If you need to stop the pipeline, wipe all data, and start completely fresh:
      1. Kill jobs: `pkill -f 'orchestrator_symbol_centric.py'` and `pkill -f 'preprocessor'`
      2. Wipe generated crash datasets (example): `rm -rf /Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/BBP-DRAWDOWNS/*`
      3. Run the automated standard watchdog daemon: `nohup python3 guardian.py > guardian_console.log 2>&1 &`
- **Harvest-Ready Logs**: Designated as primary collectors for the Remote Stadium Harvester. Located in `/logs/`.

- **Data Transfer**: [`UNIFIED_MLOPS_WORKSPACE/transfer.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/transfer.py)    - *Role*: Moves processed data and model artifacts between local storage and the high-volume backup volumes.
- **Model Converter**: [`UNIFIED_MLOPS_WORKSPACE/model_converter.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/model_converter.py)
    - *Role*: Standardizes raw TPOT pipeline files into consistent Scikit-learn based Python modules.

---

## 2. Feature Engineering & Preprocessing
These scripts transform raw market data into the high-order feature matrices required by the AutoML optimizers. Most are physically housed within `UNIFIED_MLOPS_WORKSPACE`.

- **Dynamic Alpha Lookback Calculator**: [`UNIFIED_MLOPS_WORKSPACE/macro_onset_discovery.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/macro_onset_discovery.py) [NEW]
    - *Role*: Automatically reverse-engineers historical price surges (>1%) and crashes (<-1%) to mathematically compute the optimal `window_size` duration required to predict those events for any given asset. Replaces manual `window_size=10` static arrays with absolute precision modeling.
    - *Output Format*: `OPTIMIZED_MACRO_PARAMETERS/target_parameters.txt`
- **Directional Preprocessor**: [`UNIFIED_MLOPS_WORKSPACE/directional_preprocessor_v2.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/directional_preprocessor_v2.py)
  - **V2 Strategy**: Employs a robust strategy mirroring the Crash Predictor. It pairs high-resolution Limit Order Book (LOB) precursor anomalies against the reliable Coinbase Kline (OHLC) price stream. It scans the downstream price window and labels target events `1` if the valid structural Surge exceeds a >1.0% threshold. It utilizes the dynamic lookbacks computed by the Onset Discovery engine.
    - *Role*: Generates the base feature engineering (MACD, Bollinger Bands, ADX, VWAP) and assigns binary `[0, 1]` directional labels based on forward price action.
    - *Output Format*: `[SYMBOL]-USD-binary_binned_pipeline.csv`
- **Imbalance Preprocessor (The Micro-Confirmation Layer)**: [`UNIFIED_MLOPS_WORKSPACE/imbalance_preprocessor.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/imbalance_preprocessor.py) [NEW]
    - *Role*: Calculates absolute `queue_imbalance_ratio` and `capital_imbalance_ratio` directly from raw Level-2 Bid/Ask metrics. This tier verifies if localized order-book momentum physically supports the Directional model's macro-prediction, serving as a primary alpha filter.
    - *Output Format*: `[SYMBOL]-USD-imbalance-data.csv`
- **Crash V5 Preprocessor**: [`UNIFIED_MLOPS_WORKSPACE/crash_labeling_preprocessor_v5.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/crash_labeling_preprocessor_v5.py)
    - *Role*: Calculates the most severe crashes using grouped precursor signatures. It leverages the highly stable Coinbase Kline (OHLC) price stream for forward target verification, exclusively labeling a sequence as a Crash (`1`) if the forward `Low` drops **< -3.0%** below the entry price over the target window.
    - *Output Format*: `[SYMBOL]-USD-drawdown-precursor-data.csv`
- **Unified Durational V2 Preprocessor (The Generalist)**: [`forecaster/unified_durational_preprocessor_v2.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/forecaster/unified_durational_preprocessor_v2.py)
    - *Role*: Synthesizes and merges the preceding models into a master feature matrix across **all** market events. It computes high-order technical indicators (EMAs, RSI, MACD, Cyclical Time) to predict the exact *duration* before a profitable target is hit for any symbol.
    - *Context*: Prepares the broad market feature space for the general Durational modeling tier.
    - *Output Format*: `[SYMBOL]_unified_v2_durational_data.csv`
- **Trade Duration Generator (The Elite Specialist Filter)**: [`UNIFIED_MLOPS_WORKSPACE/trade_duration_generator.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/trade_duration_generator.py)
    - *Role*: The fourth modeling phase. It performs a **strict "All Clear" filter**, stripping away all timestamps except those where the Directional model is bullish AND the Crash model is safe.
    - *Efficiency Strategy*: Optimizes for capital turnover by isolating trades that reach target in **under 3 hours**. This trains the "Efficiency" model to pass on slow-moving trades even if they are eventually profitable.
    - *Output Format*: `[SYMBOL]-USD-trade-duration-data.csv`

---

## 3. Neural Network & Hierarchical Inference
The latest evolution of the system, located in the dedicated `neural_network/` folder.

- **Predictor Engine**: [`UNIFIED_TRADER_WORKSPACE/neural_network/nn_unified_predictor.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/neural_network/nn_unified_predictor.py)
    - *Architecture*: A PyTorch hierarchical wrapper employing a **5-Layer Intelligence Chain**:
        1. **Directional (Trend)**: Determines the primary macro-price vector (Bullish/Bearish).
        2. **Imbalance (Micro-Confirmation)**: Investigates explicit queue ratio order-flow to physically validate the Directional hypothesis.
        3. **Crash (Safety)**: A defensive filter that suppresses signals if a >3.0% drop is imminent.
        4. **Generalist (Duration)**: Predicts the broad market time-to-profit matrix.
        5. **Specialist (Efficiency)**: A high-velocity filter that prioritizes trades reaching targets in <3 hours.
    - **Bayesian Accuracy Scaling (The Beijing Logic)**: The engine dynamically adjusts decision thresholds based on the historical accuracy of each specific model. For every tier, it calculates a `Dynamic Threshold = Base Threshold * Accuracy`. If the signal probability exceeds this bar, the tier returns a "Green Light," ensuring the system only trades when local performance justifies the risk.
- **CLI Test Utility**: [`UNIFIED_TRADER_WORKSPACE/neural_network/unified_predict.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/neural_network/unified_predict.py)
    - *Usage*: `python3 UNIFIED_TRADER_WORKSPACE/neural_network/unified_predict.py --symbol <NAME>`
    - *Role*: Validates the unified signal for any symbol in the roster.

---

## 4. Modeling & Accuracy Stats
Tools for generating models and monitoring performance. The pipeline writes deduplicated, rolling target scores to a dedicated tracking repository.

- **Unified Modeler**: [`UNIFIED_MLOPS_WORKSPACE/unified_modeler.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/unified_modeler.py)
    - *Role*: Executes AutoML (TPOT) optimization for all three tiers.
- **Stats Aggregator**: [`calc_stats.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/calc_stats.py)
    - *Role*: Computes global Average and Median accuracy from the modeling logs.
- **Accuracy Tracking Directory**: `accuracy_reports/`
    - Contains the deduplicated performance strings for the global roster. These files are automatically synchronized with the `stadium-public-data` repository via `push_accuracy_csvs_to_gh.py`.
    - **Live Access URLs**:
      - [Directional Accuracy Report (GitHub)](https://github.com/stefanbund/stadium-public-data/blob/main/directional_accuracy_summary.csv)
      - [Crash Accuracy Report (GitHub)](https://github.com/stefanbund/stadium-public-data/blob/main/crash_accuracy_summary.csv)
      - [Durational Accuracy Report (GitHub)](https://github.com/stefanbund/stadium-public-data/blob/main/durational_accuracy_summary.csv)
      - [Trade Duration (Efficiency) Accuracy Report (GitHub)](https://github.com/stefanbund/stadium-public-data/blob/main/trade_duration_accuracy_summary.csv) [NEW]

---

## 5. Visualization & Reporting (`UNIFIED_REPORTING_WORKSPACE`)
The public-facing results layer, fully automated to maintain an active historical ledger. Key scripts operate strictly within the `/UNIFIED_REPORTING_WORKSPACE` directory and are managed by the **Reporting Orchestrator**.

- **Reporting Orchestrator**: [`UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py) [NEW]
    - *Role*: The central driver for all visual analytics. It replaces multiple background loops with a single sequential heartbeat to prevent I/O contention on the fanless host.
- **Accuracy Dashboard Generator**: [`UNIFIED_REPORTING_WORKSPACE/generate_hourly_accuracy_report.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/generate_hourly_accuracy_report.py)
    - *Role*: Aggregates model accuracy scores from `logs/archive/` and `logs/` to generate the primary Accuracy Dashboard (Bar charts & Histograms).
- **Crash Visualizer**: [`UNIFIED_REPORTING_WORKSPACE/visualize_crashes.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/visualize_crashes.py)
    - *Role*: Interactive tool to map drawdowns and precursors against price action.
    - *Note*: This chart confirms the integrity of the supervised labeling process by visually aligning detected drops with ground-truth labels.
    - *Usage*: `python3 UNIFIED_REPORTING_WORKSPACE/visualize_crashes.py --drawdown-csv [path_to_csv] --symbol [SYMBOL]`
- **Jupyter Notebook Builder**: [`UNIFIED_REPORTING_WORKSPACE/run_notebooks.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/run_notebooks.py)
    - *Role*: Mass-generates interactive, symbol-specific `ffn` (Financial function library) backtesting notebooks.
    - *Execution*: Modifies and executes `durational_analysis_template.ipynb` for every symbol that successfully completed V4 crash processing.
    - *Target Dest*: Outputs all final `.ipynb` artifacts into the organized `ANALYSIS_NOTEBOOKS/` directory for direct data science review.
- **Efficiency Analysis Runner**: [`UNIFIED_REPORTING_WORKSPACE/run_efficiency_analysis.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/run_efficiency_analysis.py) [NEW]
    - *Role*: Specialized bulk executor for the high-velocity strategy.
    - *Execution*: Injects symbol names into the `efficiency_analysis_template.ipynb` and executes the FFN backtest headlessly across all 179 symbols.
    - *Target Dest*: `EFFICIENCY_ANALYSIS_REPORTS/` (Individual executed notebooks).
- **FFN Performance Aggregator (Strategy Yield Dashboard)**: [`UNIFIED_REPORTING_WORKSPACE/aggregate_ffn_stats.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/aggregate_ffn_stats.py)
    - *Role*: A cross-market quantitative summarizer generating interactive reporting focused on financial returns rather than ML scores.
    - *Execution*: Iterates through the entire portfolio, simulates equity curves, and harvests `Total Return` ffn statistics.
    - *Features*:
        - **Robust Outlier Management**: Uses an **IQR-based filter** (Q3 + 5x IQR) to identify extreme anomalies (e.g., symbols with >200,000% returns), which are moved to a footer to preserve the chart's scale.
        - **Logarithmic Scaling**: Employs a **Log-Y axis** to visualize diversity across multiple orders of magnitude.
    - *Target Dest*: Mints `ANALYSIS_NOTEBOOKS/aggregate_returns.csv` and an interactive `plotly` HTML scatterplot (`ANALYSIS_NOTEBOOKS/total_returns_scatter.html`) with embedded transparency footnotes.
- **Strategy Performance Aggregator**: [`UNIFIED_REPORTING_WORKSPACE/aggregate_strategy_performance.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/aggregate_strategy_performance.py) [NEW]
    - *Role*: Parses simulated `ffn` metrics (Total Return, Sharpe Ratio, Max Drawdown) from the Bayesian target notebooks.
    - *Execution*: Automatically triggered point-in-time at the conclusion of the NN Orchestrator sweep.
    - *Target Dest*: `NN_EFFICIENCY_ANALYSIS_REPORTS/strategy_performance_summary.csv`
- **Strategy Performance Dashboard Generator**: [`UNIFIED_REPORTING_WORKSPACE/generate_strategy_performance_dashboard.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/generate_strategy_performance_dashboard.py) [NEW]
    - *Role*: Compiles the CSV digest into a vibrant, dark-themed interactive HTML/CSS layout utilizing Chart.js dynamics.
    - *Execution*: Triggered autonomously sequentially after the aggregator.
    - *Target Dest*: `strategy_performance_dashboard.html`
- **Strategy Dashboard Deployer**: [`UNIFIED_REPORTING_WORKSPACE/push_strategy_dashboard_to_gh.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/push_strategy_dashboard_to_gh.py) [NEW]
    - *Role*: Authenticates against the GitHub REST API using a PAT to stream the final dashboard directly to the public web server, natively bypassing the need for a local repository clone.
    - *Execution*: The absolute final automated deployment step of the orchestrator's backend sweep.
- **Architecture Documentation Sync**: [`UNIFIED_REPORTING_WORKSPACE/push_architecture_to_gh.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/push_architecture_to_gh.py) [NEW]
    - *Role*: Duplicates the PAT REST API logic to push raw updates to the `SYSTEM_ARCHITECTURE.md` blueprint directly to the public mirror, ensuring researchers always observe the active state.
    - *Execution*: `python3 UNIFIED_REPORTING_WORKSPACE/push_architecture_to_gh.py`
- **Trader Operations Dashboard Generator**: [`UNIFIED_TRADER_WORKSPACE/generate_operations_dashboard.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/generate_operations_dashboard.py) [NEW]
    - *Role*: Automatically ingests live executed trades from Python `executions_log.csv` and renders them into an interactive dark-themed HTML monitoring frontend on the production host.
    - *Execution*: Triggered natively at the conclusion of any limit-order transaction executed by the Neural Network.
- **Trader Operations Deployer**: [`UNIFIED_TRADER_WORKSPACE/push_operations_dashboard_to_gh.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/push_operations_dashboard_to_gh.py) [NEW]
    - *Role*: Transmits the live Operations Dashboard state directly from the isolated Mac Mini to GitHub Pages via REST without requiring a full code clone.
- **Transaction Analysis Suite**: [`UNIFIED_REPORTING_WORKSPACE/TRANSACTION_ANALYSIS/`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/TRANSACTION_ANALYSIS/) [NEW]
    - **Backtest Engine**: [`analyze_approved_signals.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/TRANSACTION_ANALYSIS/analyze_approved_signals.py)
        - *Role*: Parses historical `trading_bot.log` files for `TRADE APPROVED` events and fetches forward yfinance candle data to determine +1.01% hit/miss outcomes. Evaluates the full trade lifecycle without a time-window bottleneck.
    - **Dashboard Generator**: [`generate_transaction_dashboard.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/TRANSACTION_ANALYSIS/generate_transaction_dashboard.py)
        - *Role*: Mints a 5-panel interactive Chart.js dashboard showing entry price vs outcome, signal timelines, and a "Trades In Waiting" live-price tracker.
    - **Transaction Deployer**: [`push_transaction_dashboard_to_gh.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/TRANSACTION_ANALYSIS/push_transaction_dashboard_to_gh.py)
        - *Role*: Automatically streams the analysis artifacts (HTML, CSV, JSON) to the public GitHub repository.
- **Analytics Master Hub Generator**: [`UNIFIED_REPORTING_WORKSPACE/generate_analytics_dashboard.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/generate_analytics_dashboard.py) [NEW]
    - *Role*: The primary entry point for global intelligence. Mints a premium, dark-themed master dashboard that embeds the Strategy, Accuracy, and Transaction dashboards via iframes.
    - *Execution*: Triggered automatically by the **Reporting Orchestrator** at the conclusion of every sub-component update cycle.
- **System Infrastructure Monitor**: [`UNIFIED_REPORTING_WORKSPACE/generate_system_status_dashboard.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/generate_system_status_dashboard.py) [NEW]
    - *Role*: Visualizes the health of the multi-host network. Aggregates local `guardian_status.json` and remote Mac Mini telemetry (CPU, RAM, MLOps log tail) into a side-by-side dashboard embedded in the Master Hub.
    - *Remote Fetcher*: Powered by `scripts/remote_status_fetcher.py` via SSH.
    - *Execution*: Triggered automatically every 10 minutes by the Reporting Orchestrator.
- **Shared GitHub Publication Utility**: [`shared_lib/github_pusher.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/shared_lib/github_pusher.py) [NEW]
    - *Role*: Centralizes all GitHub REST API logic. Key features include automatic `exchange_name` subfolder pathing, PAT-based authentication, and standardized blob préparation.
    - *Scaling*: Allows new hosts to publish to unique directories (e.g., `/coinbase`, `/binance`) without code duplication.
- **Live Access URLs (Exchange: Coinbase)**:
    - **Analytics Master Hub (Primary)**: [View Analytics Hub](https://stefanbund.github.io/stadium-public-data/coinbase/analytics_dashboard.html) [NEW]
    - **System Architecture (Public Blueprint)**: [View Blueprint](https://github.com/stefanbund/stadium-public-data/blob/main/SYSTEM_ARCHITECTURE.md)
    - **Accuracy Dashboard (Model Scores)**: [View Dashboard](https://stefanbund.github.io/stadium-public-data/coinbase/hourly_accuracy_dashboard.html)
    - **Strategy Performance Dashboard (Backtested Strategy Alpha)**: [View Dashboard](https://stefanbund.github.io/stadium-public-data/coinbase/strategy_performance_dashboard.html)
    - **Transaction Analysis Dashboard (Approved Signals)**: [View Dashboard](https://stefanbund.github.io/stadium-public-data/coinbase/transaction_analysis_dashboard.html)
    - **Trader Operations Dashboard (Live Trades)**: [View Dashboard](https://stefanbund.github.io/stadium-public-data/coinbase/operations_dashboard.html)

---

## 6. Event-Driven Logging System (.JSONL)
The modern execution pipeline relies on structured JSON Lines for tracking global operations, granular preprocessor behaviors, and Neural Network inference steps.

- **JSONL Logger Utility**: [`shared_lib/logger.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/shared_lib/logger.py)
    - *Role*: A centralized utility exposing `JsonlLogger(log_path, name)`. It automatically captures UTC timestamps, standard log levels (`INFO`, `WARNING`, `ERROR`), and structured attribute dictionaries under the `data` payload.
- **Architectural Integration**:
    - **Orchestration**: `orchestrator_symbol_centric.py` tracks the lifecycle wrapper (e.g., `EVENT_PIPELINE_START`, `EVENT_REMOTE_SYNC_START`, `EVENT_SYMBOL_SUCCESS`).
    - **Preprocessing**: `directional_preprocessor_v2.py` and `crash_labeling_preprocessor_v5.py` emit events for data ingestion anomalies, threshold selection, and process skips via `EVENT_PREP_COMPLETE` and `EVENT_PREP_ERROR`.
    - **Neural Network Inference**: The `UnifiedHierarchicalPredictor` relies on the schema to trace exact probability outputs at every tier:
        - `EVENT_MODEL_LOAD_STATUS`: Captures success/failure of fetching `.joblib` models.
        - `EVENT_METADATA_LOAD`: Validates the ingestion of Bayesian correctness priors.
        - `EVENT_INFERENCE_TIER`: Details the raw probability versus the dynamic target (e.g., `{"tier": "Directional", "prob": 0.17, "target": 0.97, "passed": false}`).
        - `EVENT_INFERENCE_DECISION`: Emits `TRADE APPROVED` or `TRADE REJECTED`.

---

## 7. Telemetry & Log Harvesting (Remote Harvesting Model)
The system has moved away from client-side "push" scripts (`METASTADIUM-SYNC-client`). Instead, the infrastructure utilizes a **Centralized Harvesting** model where the Meta Stadium remotely harvests telemetry from the production host. 

### **Primary Telemetry Harvest Points**
The following absolute paths are designated as the source "Harvest Points" for the remote collector:

1.  **MLOPS Orchestrator**: `logs/orchestrator_main.log`
    - *Role*: Monitoring the health and progress of the A-Z symbol pipeline.
2.  **Pipeline Events**: `UNIFIED_MLOPS_WORKSPACE/logs/events.jsonl`
    - *Role*: Structured telemetry for every preprocessing and modeling decision.
3.  **Neural Trader Logs (JSONL)**: `UNIFIED_TRADER_WORKSPACE/logs/trading_bot.log`
    - *Role*: Tracking live hierarchical probability hits and 5-tier waterfall decisions natively in clean JSON.
4.  **Trader Runtime Logs (Standard Console)**: `UNIFIED_TRADER_WORKSPACE/logs/trader_runtime.log`
    - *Role*: Captures Python stdout, tracebacks, environment warnings, and raw console output avoiding log corruption.
5.  **Trade Execution Ledger**: `UNIFIED_TRADER_WORKSPACE/logs/executions_log.csv`
    - *Role*: Real-time ledger of limit-buy fills and target-sell placement.


---

## 16. Mobile Operations & Log Synchronization [NEW]

To facilitate remote system monitoring via Google Gemini on mobile devices, the system implements a dedicated log synchronization layer.

- **Log Export Engine**: [`export_logs_gdrive.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/export_logs_gdrive.py)
    - *Role*: Aggregates the five most critical telemetry files (Orchestrator log, Events JSONL, Trading Bot log, Trader Runtime log, and Execution Ledger) and copies them into the Google Drive cloud synchronization folder.
    - *Mechanism*: Performs a `shutil.copy2` to preserve timestamps and handles path discovery for macOS Google Drive mounts (both Legacy and Modern CloudStorage).
    - *Gemini Context*: Mints a `system_summary.txt` file within the destination folder to provide a high-level status "snapshot" for LLM context injection.
- **Periodic Exporter Daemon**: [`periodic_log_export.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/periodic_log_export.py)
    - *Role*: A recurring execution wrapper that triggers the export engine every 30 minutes.
    - *Integration*: Managed directly by the [Guardian Watchdog](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/guardian.py), ensuring the mobile-ready logs are always current.

---

## 17. Model Repository & NN Data Transfer
The final storage location for the highly trained artifacts and Neural Network target data. The Multi-Phase Accuracy Transfer step packages data specifically for the Neural Network target host to ingest as historical priors.

- **Data Transportation**: Handled via physical USB bridge syncing.
- **Granular Accuracy CSVs**: Accuracy scores for every symbol are extracted and stored independently across folders:
    - Directional Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DIRECTIONAL_MODEL_ACCURACY/[SYMBOL]-directional-accuracy.csv`
    - Imbalance Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/IMBALANCE_MODEL_ACCURACY/[SYMBOL]-imbalance-accuracy.csv`
    - Crash Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/CRASH_MODEL_ACCURACY/[SYMBOL]-crash-accuracy.csv`
    - Durational Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DURATIONAL_MODEL_ACCURACY/[SYMBOL]-durational-accuracy.csv`
- **Unified Neural Network JSON Metadata**: `orchestrator_symbol_centric.py` synthesizes the independent CSV accuracies into a single isolated JSON payload for the NN Engine to parse before trading:
    - Path: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/SYMBOL_METADATA/[SYMBOL].json`
    - **Trade Duration Siloing**: To prevent conflict with existing predictors, Efficiency metadata is strictly isolated on the remote host:
      - Path: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/SYMBOL_METADATA/TRADE_DURATION/[SYMBOL].json`
    - Example Payload: `{"symbol": "BTC-USD", "accuracies": {"directional": 0.9997, "imbalance": 0.9650, "crash": 0.9534, "durational": 0.9812, "trade_duration": 0.8180}, "last_updated": "2026-03-23T12:00:00"}`

- **Compiled Joblib Modules**:
    - Directional: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DIRECTIONAL_MODULES/`
    - Imbalance: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/IMBALANCE_MODULES/`
    - Crash: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/CRASH_MODULES/`
    - Durational: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DURATIONAL_MODULES/`

---

## 8. Live Inference & Asynchronous Execution Architecture

This section distinguishes between the **Batch Preprocessing** lifecycle (Training), the **Live Feature Generation** lifecycle (Inference), and the **Actual Trade Execution**.

### Training vs. Real-Time Execution
*   **Batch Preprocessing (Training)**: Scripts like `unified_durational_preprocessor_v2.py` are designed for historical data science. They process years of data in large blocks to generate static `.csv` training files. This is I/O intensive and unsuitable for live low-latency trading.
*   **Live Feature Generation (Inference)**: The Live Trading Agent (e.g., `trader_NN_HIERARCHICAL.py`) bypasses disk-based scripts. Instead, it maintains a small in-memory buffer of recent price data (e.g., last 200 hours) to compute features on the fly.

### The Inference Workflow
1.  **Buffer Management**: The predictor fetches minimal recent context from the exchange API or local cache.
2.  **In-Memory Calculation**: Indicators (RSI, EMAs, ATR) are computed instantly within the agent's memory space using streamlined math functions.
3.  **Hierarchical Evaluation**: The resulting "current state" vector is passed sequentially through the `UnifiedHierarchicalPredictor`:
    - **Tier 1**: Should I buy? (Directional Trend)
    - **Tier 2**: Are the micro order-books supporting this? (Imbalance Queue Ratio)
    - **Tier 3**: Is it safe to execute? (Crash Safety)
    - **Tier 4**: What is the general market speed limit? (Durational)
    - **Tier 5**: Does this pass my algorithmic mandate? (Specialist Efficiency)
4.  **Action Handoff**: Executable signal is generated only if all 5 tiers provide a "Green Light." It then hands off control to the Execution layer.

### Asynchronous Execution Engine
The final step in translating inferences into real-world orders is handled by the unified Python executor.

- **Python Asynchronous Base Trader**: [`JS-TRADER-REWRITE/async_trader_rewritten.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/JS-TRADER-REWRITE/async_trader_rewritten.py)
    - *Role*: The dedicated trade execution layer. Fully replaces the legacy Node.js `async_trader.js` framework. It consumes signals generated by the hierarchical predictor and interfaces directly with the Coinbase Advanced Trade (CDP) API using JWT authentication.
    - *Architecture*: Non-blocking asynchronous polling (`asyncio`) ensures rapid order fill detection. 
    - *Mechanics*: Places a Limit Buy, polls execution status until filled, computes a dynamic precision-adjusted 1.01x output Target Limit Sell, and logs the fully realized cycle to `executions_log.csv`. Includes comprehensive precision scaling to prevent API rejection errors.

---

## 9. Command Line Interface Reference

The central orchestrator (`orchestrator_symbol_centric.py`) takes several arguments to control the pipeline flow. Here is the latest execution guide:

```text
usage: orchestrator_symbol_centric.py [-h] [--symbols SYMBOLS] [--host HOST] [--pull] [--workers WORKERS] [--skip-transfer]
                                      [--skip-existing] [--skip-step1] [--skip-step2] [--skip-preprocessing] [--purge-durational]
                                      [--experimental-directional-only] [--start-at START_AT] [--max-age-days MAX_AGE_DAYS]

Symbol-Centric Pipeline Orchestrator

optional arguments:
  -h, --help            show this help message and exit
  --symbols SYMBOLS     Comma-separated list of symbols (e.g., BTC,ETH,00)
  --host HOST           Specify remote host for data syncing/transfer.
  --pull                Sync data from remote host before processing.
  --workers WORKERS     Number of symbols to process in parallel.
  --skip-transfer       Skip remote transfer of models and digests.
  --skip-existing       Skip steps if output files already exist (used with --max-age-days for time-based skipping)
  --skip-step1          Skip Step 1: Preprocessing
  --skip-step2          Skip Step 2: Data Merging
  --skip-preprocessing  Skip Step 1 and Step 2
  --purge-durational    Delete all existing files in durational data/model directories before starting.
  --experimental-directional-only
                        Launch experiment: Durational modeling using ONLY directional features.
  --start-at START_AT   Start processing from this symbol (alphabetically).
  --max-age-days MAX_AGE_DAYS
                        Skip steps whose output files were modified within this many days (default: 14).
                        Requires --skip-existing. Set to 0 to force redo everything regardless of age.
                        Governs all model types including Imbalance (which takes ~7 days to train).
```

> **Guardian Default Command**: `python3 -u orchestrator_symbol_centric.py --workers 2 --skip-existing --experimental-directional-only --max-age-days 14`

---

## 10. Deployment Practices (`UNIFIED_TRADER_WORKSPACE`)

**[UPDATE] The system has transitioned away from a distributed server model. The LOB Sampler and Neural Trader now run directly on the primary host machine. Remote syncs are no longer required for deployment.**

All execution and neural network inference code is strictly grouped into `/UNIFIED_TRADER_WORKSPACE`. Because the trader now executes natively alongside the orchestrator, it directly consumes models from the shared `M4_BACKUP` hardware bridge without the need for active network synchronization.

### Legacy Bi-Directional Pipeline (Deprecated)
*Note: The following push/pull pipeline was previously used to synchronize the `UNIFIED_TRADER_WORKSPACE` directory on the Development Laptop with the `UNIFIED_TRADER_DEPLOYMENT` directory on a Production Mac Mini. Ensure you are executing trader scripts locally instead of syncing them.*

#### 1. Forward Sync (Deploying)
- **Tool**: `python3 UNIFIED_TRADER_WORKSPACE/deployment_helper.py`
- **Direction**: Laptop → Mac Mini (Production)
- **Purpose**: Ships new Python Trader logic and neural network updates to the live execution server.
- **Start Button Hook**: During deployment, the script automatically applies `chmod +x` to `run_pause_predictor.sh`, granting it execution privileges on the remote machine so the user can immediately launch the trader.
- **Key Operations**:
    1. **Dependency Audit**: Verifies that the remote `requirements.txt` matches the local development workspace and updates the remote `venv` dynamically.
    2. **Codebase Mirror**: Securely `rsync`s the entire `UNIFIED_TRADER_WORKSPACE` subset to the target host.
    3. **Intelligence Sync (Bypassed)**: It intentionally ignores Intelligence Modules (`*.joblib`) during code-sync, as heavy model artifacts are asynchronously transferred by the main ML Orchestrator.

#### 2. The "Start Button" (Execution)
- **Script**: `UNIFIED_TRADER_WORKSPACE/run_pause_predictor.sh`
- **Action**: Acts as the primary entry point for the trader on the target host. Once deployed, the user executes this bash script to bootstrap the Python trader.
- **Direct Launch Command**: Alternatively, to launch the trader manually while ensuring that standard output and internal JSON telemetry streams do not fight for the same file, use the split-stream root command:
  ```bash
  nohup ./venv/bin/python3 UNIFIED_TRADER_WORKSPACE/trader_NN_HIERARCHICAL.py > UNIFIED_TRADER_WORKSPACE/logs/trader_runtime.log 2>&1 &
  ```

#### 3. Reverse Sync (Pulling)
- **Tool**: `python3 UNIFIED_TRADER_WORKSPACE/sync_back_from_target.py`
- **Direction**: Mac Mini (Production) → Laptop
- **Purpose**: If immediate live bug fixes or threshold tweaks are made directly on the remote Mac Mini, executing this script on the laptop will instantly mirror the production `UNIFIED_TRADER_DEPLOYMENT` directory back down into the local `UNIFIED_TRADER_WORKSPACE`.

#### 4. Pre-Flight Validation [NEW]
- **Tool**: `python3 UNIFIED_TRADER_WORKSPACE/preflight_validator.py`
- **Purpose**: Rigorous "Green Light" check before pushing code. It compares the `config.json` against the `TRADER_SYSTEM_MANIFEST.json` and performs deep audits on environment, paths, and tiers.
- **Key Checks**:
    - **Manifest Audit**: Confirms all 5 hierarchical thresholds are defined and aligned.
    - **Tier Integrity**: Validates existence of both `.py` and `.joblib` files for each tier.
    - **Inference Dry Run**: Executes a mock Bayesian pass for a sample symbol (e.g., BICO) to confirm all models load into VRAM successfully.
- **Usage**: `./venv/bin/python UNIFIED_TRADER_WORKSPACE/preflight_validator.py UNIFIED_TRADER_WORKSPACE/`

### Execution File Map (`UNIFIED_TRADER_WORKSPACE/`)

```text
/UNIFIED_TRADER_WORKSPACE
│── async_trader_rewritten.py        # Pure Python API executor (Limit Buys & Auto-Sells)
│── trader_NN_HIERARCHICAL.py        # The Bayesian Logic entrypoint tailing the LOB 
│── generate_operations_dashboard.py # Live HTML operations dashboard compiler
│── push_operations_dashboard_to_gh.py # GitHub REST API publisher for live trade telemetry
│── run_pause_predictor.sh           # The Executable Start Button for the Trader
│── deployment_helper.py             # The Laptop -> Mac Mini sync utility
│── sync_back_from_target.py         # The Mac Mini -> Laptop pull utility
│── config.json                      # Local override configuration
│── requirements.txt                 # Shared Python dependencies
├── /neural_network/                 # Bayesian Model classes
└── /utils/                          # Shared utility functions
```  ```bash
          python deployment_helper.py --audit-only
          ```
        - **Full Deployment (Sync)**: Executes audits first, then synchronizes all code and intelligence modules.
          ```bash
          python deployment_helper.py

### Production File System Map
For the Neural Network trader to run successfully on a remote host, the following robust directory structure is established automatically around a fully isolated container:

```text
[PRODUCTION_HOST_ROOT]/
│
├── UNIFIED_TRADER_DEPLOYMENT/      # CODE & EXECUTION ENGINE ROOT
│   ├── venv/                       # Autogenerated Python Virtual Environment
│   ├── config.json                 # Master Configuration File
│   ├── requirements.txt
│   ├── trader_NN_HIERARCHICAL.py
│   ├── deployment_helper.py
│   ├── JS-TRADER-REWRITE/
│   │   └── async_trader_rewritten.py  # Asynchronous Python execution daemon
│   ├── neural_network/
│   └── utils/
│
└── STADIUM-DATA-FROM-I71/          # ESTABLISHED DATA & MODULE ROOT
    └── MODELS/                     # Intelligence modules live here
        ├── DIRECTIONAL_MODULES/
        ├── IMBALANCE_MODULES/
        ├── CRASH_MODULES/
        ├── GENERALIST_DURATIONAL_MODULES/
        └── SPECIALIST_TRADE_DURATION_MODULES/
```

---

## 11. The Three-Pillar Operational Paradigm & Hardware Mapping
The system architecture reflects the physical segmentation of the hardware environment, ensuring compute-heavy training remains isolated from latency-sensitive trading, while entirely decoupling remote APIs from the execution brain.

### The Three Pillars (Unified Machine Model)

1. **Pillar I: The Laboratory (The Orchestrator)**
    - *Hardware*: Primary Machine (Laptop)
    - *Storage Context*: **USB-Centric**. Heavy archival data and intelligence modules are primarily stored on the `/Volumes/M4_BACKUP` high-capacity drive to preserve laptop internal SSD health.
    - *Role*: The heavy ML-Ops engine (`orchestrator_symbol_centric.py`). Aggregates historical GRUS data, trains TPOT `.joblib` modules, and generates dynamic Bayesian accuracy priors. It operates over vast historical batches.

2. **Pillar II: The Sensor (LOB Sampler)**
    - *Hardware*: Primary Machine (Laptop)
    - *Storage Context*: **Internal-Centric**. The sensor streams explicitly to fast local storage.
    - *Role*: A lightweight daemon streaming raw Limit Order Book (LOB) depth and price actions from the Coinbase REST/WebSocket APIs, writing results into incredibly rapid local `.csv` files.

3. **Pillar III: The Execution Brain (The Trader)**
    - *Hardware*: Primary Machine (Laptop)
    - *Role*: The true intelligence of the operation (`trader_NN_HIERARCHICAL.py`). It continuously parses the LOB CSV matrix created by the Sensor and triggers inference passes through the Neural Network using the localized `M4_BACKUP` module paths. If granted a "Green Light", it exclusively pings the internet via `async_trader_rewritten.py` to place actionable Limit Buy orders.
    - *Runtime Reliability*: To maintain I/O stability, the sampler is **rotated every 6 hours** by the Guardian, ensuring the trader's data ingestion remains lightning-fast.

### Hardware Bridging: The `{data_root_i71}` Strategy
Historically, the system utilized a **Dynamic Path Variable** (`data_root_i71`) within `config.json` to handle sync mappings across a network. Since the system evaluates directly on the primary host, this bridge now strictly resolves directly to `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71`.

| Machine | Role | Primary Responsibility |
| :--- | :--- | :--- |
| **Primary Host** | **The Omniscient Core** | Modeling, Tracking, LOB Sampling, and Live Trade Execution |
| **M4 Backup (USB)** | **The Vault** | "Gold Copy" of all modules and data buffers |

---

## 12. The Accuracy Lifecycle
Accuracy is the "Fuel" for the Bayesian Predictor. It flows through the system in four distinct phases:

1. **Phase 1: Generation**: `unified_modeler.py` executes TPOT runs and writes raw performance metrics to standard out and logs.
2. **Phase 2: Consolidation**: `calc_stats.py` and `push_accuracy_csvs_to_gh.py` extract per-symbol scores into global CSV ledgers.
3. **Phase 3: Injection**: `orchestrator_symbol_centric.py` synthesizes these CSVs into `SYMBOL_METADATA` JSON payloads (located in `/MODELS/SYMBOL_METADATA/`).
4. **Phase 4: Scaling**: The `nn_unified_predictor.py` parses these JSON files at runtime. It applies the "Beijing Logic" to scale base thresholds by the actual historical fidelity of the active module.

---

## 13. Operational Best Practices
To maintain the high fidelity of the 4-layer system, follow this daily workflow:

1. **Morning Audit**: Run `python deployment_helper.py --audit-only` to ensure the Mac Mini and your Laptop are still synchronized after any overnight modeling runs.
2. **Intelligence Sync**: If the audit shows missing modules, run the full sync to push the latest `.joblib` files to the production host.
3. **Threshold Review**: Periodically check the **Accuracy Dashboard** (GitHub Pages). If a symbol's accuracy has significantly shifted, adjust the "Beijing" thresholds in `config.json` accordingly.
4. **Log Grooming**: Monitor `logs/orchestrator_main.log` on the Laptop to ensure the Symbol-Centric loop is proceeding through the A-Z roster without interruptions.

---

## 14. Model Training Caveats & Portfolio Maturity [NEW]
The "Waterfall" hierarchical logic requires a complete 5-layer stack of `.joblib` models for a trade to be authorized. For some symbols, you may observe "Missing Model" warnings (e.g., `Imbalance model not found`) or early decision exits despite a passing Directional signal.

### Common Reasons for Model Gaps
- **Event Scarcity (Volatility Threshold)**: The Imbalance and Crash preprocessors only extract training data when they detect a definitive "Event" (e.g., a >1% surge or >3% crash) preceded by reliable LOB precursors. Low-volatility assets may trade sideways for days, failing to produce enough "Precursor -> Result" pairs for the AutoML engine to train on.
- **Asset Maturity (Sampling History)**: New assets added to the LOB Sampler (e.g., `FLOCK`, `CORECHAIN`, `LOKA`) require a minimum threshold of historical context. If a symbol has only been sampled for 24–72 hours, it may not have encountered enough significant market cycles to populate the `BBP-IMBALANCE` or `BBP-DRAWDOWNS` training sets.
- **Strict Filtering (Short-Circuit Logic)**: In the hierarchical engine (`nn_unified_predictor.py`), if any mandatory tier is missing for a symbol, the system defaults to a `False` decision. This is a safety feature to ensure trades are only executed on assets with a fully verified and specialized intelligence stack.

### Resolution Strategy
- **Continued Sampling**: Allow the LOB sampler to continue gathering history. As time passes, more high-resolution "Surge/Crash" events will naturally occur and be captured for these symbols.
- **Periodic Retraining Sweeps**: Retraining the `imbalance_preprocessor.py` for the whole portfolio every few days allows the system to "discover" newly matured symbols that now have enough history for high-fidelity modeling.

---

## 15. Machine Migration & Remote Synchronization (RSYNC) [NEW]

The system is designed for seamless migration between MacOS workstations (e.g., migrating from an M4 Laptop to another Mac) using `rsync` instead of Git. This workflow prioritizes data economy and path portability.

### 15.1 Path Portability & Rationalization
- **Dynamic Root Detection**: The [Guardian Watchdog](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/guardian.py) and core scripts have been refactored to use dynamic path resolution (`os.path.abspath(__file__)`). This ensures the workspace remains functional regardless of the default username or absolute path on the target machine.
- **Workspace Economy**: To minimize transfer time, the migration utilizes a strict exclusion policy defined in `.rsync_exclude`. This skips massive log files, local virtual environments, and temporary caches.

### 15.2 Deployment Artifacts
- **Deployment Manifest**: [`deployment_manifest.json`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/deployment_manifest.json)
    - *Role*: A system-level blueprint for Antigravity or a human admin. It defines the required directory structure, essential environment variables (Twilio SID/Tokens), and the Python dependency stack.
- **Dependency Map**: [`requirements.txt`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/requirements.txt)
    - *Role*: A consolidated list of all Python packages and versions required to rebuild the environment on the target Mac.
- **Rsync Exclude List**: [`.rsync_exclude`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/.rsync_exclude)
    - *Role*: Filters out `venv/`, `__pycache__`, and `watchdog_*.log` files to ensure a lean, fast synchronization.

### 15.3 Migration Procedure (Step-by-Step)

1. **Perform the Initial Sync**:
   Execute the following command from the project root on the source machine:
   ```bash
   rsync -avz --progress --exclude-from='.rsync_exclude' ./ user@remote-mac:~/Developer/LAPTOP_PREPROCESSOR_MODELER
   ```
2. **Setup the Virtual Environment**:
   On the target machine, initialize a fresh environment to ensure architecture compatibility:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Verify Configuration**:
   Update `config.json` if the external data volume (`data_root_i71`) is mounted at a different location. Or if the new exchange uses a different suffix (e.g., `-USDT`).
4. **Launch the Watchdog**:
   ```bash
   python3 guardian.py
   ```

### 15.4 Symbol & Exchange Adaptation
The MLOps pipeline is designed to be **symbol-agnostic**. When deploying to a machine sampling a new exchange (e.g., with different symbol names or suffixes like `-USDT`):
- **Retraining Required**: The Bayesian accuracy priors and `.joblib` models from the previous exchange will not be valid for the new data distribution. A full retraining sweep is necessary.
- **Config Update**: Update the `quote_currency_suffix` in `config.json` to match the new exchange's naming convention.
- **Data Integrity**: Ensure the new sampler produces CSVs that match the expected schema (Timestamp, Price, LOB levels).

### 15.5 Workspace Maintenance
Legacy scripts and test files have been moved to `SCRIPTS_ARCHIVE/` to maintain a clean project root, facilitating easier navigation on the new host.

---

## 18. System Productization & Centralized Control [NEW]

The system has transitioned into a "Productized" state, prioritizing stability, secret security, and centralized management. This phase eliminated fragmented configurations and ad-hoc execution scripts.

### 18.1 Centralized Configuration (`shared_lib/`)
- **Main Config Reference**: [`global_config.json`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/global_config.json)
    - *Role*: The single source of truth for all system paths, hardware offsets, and trading thresholds.
- **Config Loader**: [`shared_lib/config_loader.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/shared_lib/config_loader.py)
    - *Role*: A robust Python class that performs recursive path resolution (translating `{project_root}` into absolute paths) and deep merging of local overrides.
- **Secret Injection**: The loader natively parses the [`.env`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/.env) file at runtime, injecting sensitive credentials (Twilio, GitHub PAT) into the environment without them ever being written to disk in a plain-text config.

### 18.2 Operational Wrapper Scripts (`scripts/`)
To reduce cognitive load and ensure consistent execution, the system is now managed via a suite of robust bash wrappers:

1. **The Startup Engine**: [`scripts/start_guardian.sh`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/scripts/start_guardian.sh)
    - Launches the primary `guardian.py` watchdog in the background.
2. **The Kill Switch**: [`scripts/stop_guardian.sh`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/scripts/stop_guardian.sh)
    - Safely terminates the watchdog and all managed child processes (Sampler, Orchestrator, Trader) using SIGINT/SIGKILL waterfalls.
3. **The Health Monitor**: [`scripts/status.sh`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/scripts/status.sh)
    - Displays a live snapshot of system resource usage (CPU/RAM) and individual microservice status.

### 18.3 Improved Data Resiliency
- **Shared Data Loader**: Integrated into `trader_NN_HIERARCHICAL.py`. Replaces multiple redundant file-readers with a single memory-mapped tail observer, drastically reducing I/O contention on the host SSD.
- **Type-Safety Enforcement**: Implements robust numeric conversion (`pd.to_numeric`) for all LOB metrics, preventing the "unsupported operand type" crashes previously caused by infrequent malformed CSV rows.

---

## 19. Multi-Exchange Visualization Scaling & Shared Publication Layer [NEW]

To facilitate scaling the network across multiple hosts and duplicate services, the system implements a dynamic folder-based deployment model on GitHub.

### 19.1 The Exchange Suffix Strategy
- **Configuration Source**: `global_config.json` → `exchange_name` (e.g., `"coinbase"`, `"binance"`).
- **Directory Isolation**: All visualization assets (.html, .csv, .json) are published to a sub-directory named after the active exchange. This ensures that duplicate services running on different machines can contribute to a single repository without overwriting each other's data.

### 19.2 The Shared GitHub Pusher
- **Location**: [`shared_lib/github_pusher.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/shared_lib/github_pusher.py)
- **Automatic Pathing**: The utility automatically detects the `exchange_name` from the global config and prefixes all repository paths. A developer only needs to specify the filename (e.g., `dashboard.html`), and the pusher resolves it to `coinbase/dashboard.html`.

### 19.3 Analytics Master Hub
- **Unified Viewing**: The `analytics_dashboard.html` serves as a "Mission Control" center. It leverages iframes with relative pathing to embed the specialized Strategy, Accuracy, and Transaction dashboards.
- **Portability**: Because it uses relative paths, the Master Hub remains fully functional regardless of which exchange subfolder it is deployed in, allowing for instant "Whitelabel" dashboard duplication across the network.
