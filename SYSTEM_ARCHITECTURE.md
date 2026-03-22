# Crypto Forecasting System | Architecture Blueprint

This document provides a comprehensive overview of the current working system, cataloging all key components, their locations, and their roles in the multi-phase machine learning pipeline.

---

## 1. Orchestration & Logistics (`UNIFIED_MLOPS_WORKSPACE`)
The central nervous system that manages the sequential execution for each symbol. All Laboratory logic is strictly physically segregated into the `/UNIFIED_MLOPS_WORKSPACE` directory to maintain a pristine project root.

- **Main Orchestrator**: [`UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py)
    - *Role*: The primary entry point. Manages the loop across all **261 symbols**, calling preprocessors, modelers, and transfer scripts.
    - *Symbol Discovery*: Prioritizes the "Source Truth" by scanning the `GRUS-CSV-SAMPLER-DATA/symbols` directory for per-asset CSVs. This ensures 100% coverage across the alphabet (A-Z), with fallbacks to preprocessed BBP files if the source directory is unavailable.
    - *Usage (Global Run)*: To execute safely in the background across all CPU workers while maintaining a log: `nohup ./venv/bin/python UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py --host stefans-Mac-mini.local --pull --workers 4 > logs/orchestrator_main.log 2>&1 &`
    - *Usage (Global Wipe & Restart)*: If you need to stop the pipeline, wipe all data, and start completely fresh:
      1. Kill jobs: `pkill -f 'orchestrator_symbol_centric.py'` and `pkill -f 'preprocessor'`
      2. Wipe generated crash datasets (example): `rm -rf /Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/BBP-DRAWDOWNS/*`
      3. Run the "Global Run" `nohup` command above.
- **Data Transfer**: [`UNIFIED_MLOPS_WORKSPACE/transfer.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/transfer.py)    - *Role*: Moves processed data and model artifacts between local storage and the high-volume backup volumes.
- **Model Converter**: [`UNIFIED_MLOPS_WORKSPACE/model_converter.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/model_converter.py)
    - *Role*: Standardizes raw TPOT pipeline files into consistent Scikit-learn based Python modules.

---

## 2. Feature Engineering & Preprocessing
These scripts transform raw market data into the high-order feature matrices required by the AutoML optimizers. Most are physically housed within `UNIFIED_MLOPS_WORKSPACE`.

- **Directional Preprocessor**: [`UNIFIED_MLOPS_WORKSPACE/directional_preprocessor_v2.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/directional_preprocessor_v2.py)
  - **V2 Strategy**: Employs a robust strategy mirroring the Crash Predictor. It pairs high-resolution Limit Order Book (LOB) precursor anomalies against the reliable Coinbase Kline (OHLC) price stream. It scans the downstream price window and labels target events `1` if the valid structural Surge exceeds a >1.0% threshold, offering superior signal consistency over legacy raw LOB MP methods.
    - *Role*: Generates the base feature engineering (MACD, Bollinger Bands, ADX, VWAP) and assigns binary `[0, 1]` directional labels based on forward price action.
    - *Output Format*: `[SYMBOL]-USD-binary_binned_pipeline.csv`
- **Crash V5 Preprocessor**: [`UNIFIED_MLOPS_WORKSPACE/crash_labeling_preprocessor_v5.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/crash_labeling_preprocessor_v5.py)
    - *Role*: Calculates the most severe crashes using grouped precursor signatures. It leverages the highly stable Coinbase Kline (OHLC) price stream for forward target verification, exclusively labeling a sequence as a Crash (`1`) if the forward `Low` drops **< -3.0%** below the entry price over the target window. This perfectly mirrors the strategy in Directional V2, deprecating the localized Limit Order Book target evaluations and old quantile binning formats.
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

- **Predictor Engine**: [`neural_network/nn_unified_predictor.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/neural_network/nn_unified_predictor.py)
    - *Architecture*: A PyTorch hierarchical wrapper employing a **4-Layer Intelligence Chain**:
        1. **Directional (Trend)**: Determines the primary price vector (Bullish/Bearish).
        2. **Crash (Safety)**: A defensive filter that suppresses signals if a >3.0% drop is imminent.
        3. **Generalist (Duration)**: Predicts the time-to-profit based on global market features.
        4. **Specialist (Efficiency)**: A high-velocity filter that prioritizes trades reaching targets in <3 hours.
    - **Bayesian Accuracy Scaling (The Beijing Logic)**: The engine dynamically adjusts decision thresholds based on the historical accuracy of each specific model. For every tier, it calculates a `Dynamic Threshold = Base Threshold * Accuracy`. If the signal probability exceeds this bar, the tier returns a "Green Light," ensuring the system only trades when local performance justifies the risk.
- **CLI Test Utility**: [`neural_network/unified_predict.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/neural_network/unified_predict.py)
    - *Usage*: `python3 neural_network/unified_predict.py --symbol <NAME>`
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
The public-facing results layer, fully automated to maintain an active historical ledger. Key scripts operate strictly within the `/UNIFIED_REPORTING_WORKSPACE` directory.

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
    - **Live Access URLs**:
        - **Accuracy Dashboard (Model Scores)**: `https://stefanbund.github.io/stadium-public-data/hourly_accuracy_dashboard.html`
        - **Strategy Performance Dashboard (Financial Alpha)**: `https://stefanbund.github.io/stadium-public-data/strategy_performance_dashboard.html`

---

## 6. Event-Driven Logging System (.JSONL)
The modern execution pipeline relies on structured JSON Lines for tracking global operations, granular preprocessor behaviors, and Neural Network inference steps.

- **JSONL Logger Utility**: [`utils/logger.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/utils/logger.py)
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

## 7. Model Repository & NN Data Transfer
The final storage location for the highly trained artifacts and Neural Network target data. The Multi-Phase Accuracy Transfer step packages data specifically for the Neural Network target host to ingest as historical priors.

- **Data Transportation**: Handled via physical USB bridge syncing.
- **Granular Accuracy CSVs**: Accuracy scores for every symbol are extracted and stored independently across three folders:
    - Directional Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DIRECTIONAL_MODEL_ACCURACY/[SYMBOL]-directional-accuracy.csv`
    - Crash Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/CRASH_MODEL_ACCURACY/[SYMBOL]-crash-accuracy.csv`
    - Durational Accuracy: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DURATIONAL_MODEL_ACCURACY/[SYMBOL]-durational-accuracy.csv`
- **Unified Neural Network JSON Metadata**: `orchestrator_symbol_centric.py` synthesizes the four independent CSV accuracies into a single isolated JSON payload for the NN Engine to parse before trading:
    - Path: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/SYMBOL_METADATA/[SYMBOL].json`
    - **Trade Duration Siloing**: To prevent conflict with existing predictors, Efficiency metadata is strictly isolated on the remote host:
      - Path: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/SYMBOL_METADATA/TRADE_DURATION/[SYMBOL].json`
    - Example Payload: `{"symbol": "BTC-USD", "accuracies": {"directional": 0.9997, "crash": 0.9534, "durational": 0.9812, "trade_duration": 0.8180}, "last_updated": "2026-03-12T12:00:00"}`

- **Compiled Joblib Modules**:
    - Directional: `/Volumes/M4_BACKUP/STADIUM-DATA-FROM-I71/MODELS/DIRECTIONAL_MODULES/`
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
    - **Tier 1**: Should I buy? (Directional)
    - **Tier 2**: Is it safe? (Crash)
    - **Tier 3**: Is it efficient? (Durational/Efficiency)
4.  **Action Handoff**: Executable signal is generated only if all tiers provide a "Green Light." It then hands off control to the Execution layer.

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
                                      [--experimental-directional-only]

Symbol-Centric Pipeline Orchestrator

optional arguments:
  -h, --help            show this help message and exit
  --symbols SYMBOLS     Comma-separated list of symbols (e.g., BTC,ETH,00)
  --host HOST           Specify remote host for data syncing/transfer.
  --pull                Sync data from remote host before processing.
  --workers WORKERS     Number of symbols to process in parallel.
  --skip-transfer       Skip remote transfer of models and digests.
  --skip-existing       Skip steps if output files already exist
  --skip-step1          Skip Step 1: Preprocessing
  --skip-step2          Skip Step 2: Data Merging
  --skip-preprocessing  Skip Step 1 and Step 2
  --purge-durational    Delete all existing files in durational data/model directories before starting.
  --experimental-directional-only
                        Launch experiment: Durational modeling using ONLY directional features.
```

---

## 10. Deployment Practices (`UNIFIED_TRADER_WORKSPACE`)
The deployment process has been modernized into a **"Dumb" Deployment Pipeline**. Because all execution and neural network inference code is now strictly grouped into `/UNIFIED_TRADER_WORKSPACE`, the deployment helper no longer cherry-picks scripts. It acts as a pure 1:1 mirror, pushing exactly what is strictly required to execute trades.

The target host requires very little pre-existing infrastructure. It does not need a pre-established virtual environment; the deployment script natively builds the environment, installs dependencies, transfers the payload, and primes the execution loop. The LOB sampler naturally lives on the target host, populating the required data folders for the trader to consume locally.

### The Bi-Directional Pipeline
The system relies on two autonomous push/pull tools to synchronize the `UNIFIED_TRADER_WORKSPACE` directory on the Development Laptop with the `UNIFIED_TRADER_DEPLOYMENT` directory on the Production Mac Mini.

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

#### 3. Reverse Sync (Pulling)
- **Tool**: `python3 UNIFIED_TRADER_WORKSPACE/sync_back_from_target.py`
- **Direction**: Mac Mini (Production) → Laptop
- **Purpose**: If immediate live bug fixes or threshold tweaks are made directly on the remote Mac Mini, executing this script on the laptop will instantly mirror the production `UNIFIED_TRADER_DEPLOYMENT` directory back down into the local `UNIFIED_TRADER_WORKSPACE`.

### Execution File Map (`UNIFIED_TRADER_WORKSPACE/`)

```text
/UNIFIED_TRADER_WORKSPACE
│── async_trader_rewritten.py     # Pure Python API executor (Limit Buys & Auto-Sells)
│── trader_NN_HIERARCHICAL.py     # The Bayesian Logic entrypoint tailing the LOB 
│── run_pause_predictor.sh        # The Executable Start Button for the Trader
│── deployment_helper.py          # The Laptop -> Mac Mini sync utility
│── sync_back_from_target.py      # The Mac Mini -> Laptop pull utility
│── config.json                   # Local override configuration
│── requirements.txt              # Shared Python dependencies
├── /neural_network/              # Bayesian Model classes
└── /utils/                       # Shared utility functions
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
        ├── CRASH_MODULES/
        ├── GENERALIST_DURATIONAL_MODULES/
        └── SPECIALIST_TRADE_DURATION_MODULES/
```

---

## 11. The Three-Pillar Operational Paradigm & Hardware Mapping
The system architecture reflects the physical segmentation of the hardware environment, ensuring compute-heavy training remains isolated from latency-sensitive trading, while entirely decoupling remote APIs from the execution brain.

### The Three Pillars

1. **Pillar I: The Laboratory (The Orchestrator)**
    - *Hardware*: Development Laptop
    - *Role*: The heavy ML-Ops engine (`orchestrator_symbol_centric.py`). Aggregates historical GRUS data, trains TPOT `.joblib` modules, generates dynamic Bayesian accuracy priors, and actively pushes these finalized "brains" via `deployment_helper.py` to the target host. It operates purely on asynchronous historical batches.

2. **Pillar II: The Sensor (LOB Sampler)**
    - *Hardware*: Mac Mini (Production)
    - *Role*: A lightweight, highly available daemon that never makes trade decisions. It sits passively, continuously streaming raw Limit Order Book (LOB) depth and price actions from the Coinbase REST/WebSocket APIs, writing the results into incredibly rapid local `.csv` files.

3. **Pillar III: The Execution Brain (The Trader)**
    - *Hardware*: Mac Mini (Production)
    - *Role*: The true intelligence of the operation (`trader_NN_HIERARCHICAL.py`). It **never** hits the internet to fetch price data. It strictly reads the `.csv` matrix continuously assembled by the Sensor. When it extracts 10 fresh rows, it triggers an inference pass through the Neural Network. If granted a "Green Light", it exclusively pings the internet via `async_trader_rewritten.py` merely to place the final actionable Limit Buy order.

This asynchronous handoff fundamentally eliminates API rate-limiting delays from the Trader's critical execution loop.

| Machine | Role | Primary Responsibility |
| :--- | :--- | :--- |
| **Development Laptop** | **The Laboratory (Orchestrator)** | AutoML Training, Preprocessing, Accuracy Reporting, Model Deployment |
| **M4 Backup (USB)** | **The Bridge/Archive** | "Gold Copy" of all modules, cross-machine sync point |
| **Mac Mini (Prod)** | **Sensor & Execution Core** | LOB Generation, Live Bayesian Inference, Real-time APIs |

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
