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
    - **Mobile Log Exporter**: [`periodic_log_export.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/periodic_log_export.py)
        - *Role*: Syncs critical telemetry to Google Drive for remote monitoring via Gemini.
- **Stage 2: Intelligence & Execution**
    - **MLOps Orchestrator (Local)**: [`UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_MLOPS_WORKSPACE/orchestrator_symbol_centric.py)
        - *Mode*: `--fast-rf` (Standard Random Forest baseline for high-velocity deployment).
        - *Role*: Manages the A-Z symbol modeling loop.
    - **Hierarchical Trader**: [`UNIFIED_TRADER_WORKSPACE/trader_NN_HIERARCHICAL.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_TRADER_WORKSPACE/trader_NN_HIERARCHICAL.py)
        - *Condition*: Only starts after confirming active LOB data flow.
        - *Role*: Processes live signals through the neural hierarchy.
- **Stage 3: [Reserved]**
- **Stage 4: Visualization**
    - **Reporting Orchestrator**: [`UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/UNIFIED_REPORTING_WORKSPACE/reporting_orchestrator.py)
        - *Role*: Sequential execution of all reporting heartbeats (Accuracy, Strategy, Operations).

---

## 2. Neural Intelligence Hierarchy
The system now operates on a **3-Tier Ultra-Lean Waterfall** decision engine, optimized for high-velocity execution and alpha preservation. This stack was finalized during the `FIS_INDUSTRIAL_LEAN_v1` experiment, which proved that bypassing durational complexity leads to superior risk-adjusted returns.

1.  **Tier 0: Dynamic Volatility Governor (DVG)**
    - *Source*: `DAW_CAUSALITY_LAYER/causality_layer.py`
    - *Mechanism*: Acts as a macro-risk firewall by modulating the fused execution threshold based on the **DVOL Z-score**. 
    - *Adaptive Logic*: `Effective_Threshold = Base * (1 + max(0, Z/2))`. This ensures the "Lean Shield" tightens automatically during high-volatility exhaustion regimes.
2.  **Tier 1: Directional (Trend)**
    - *Threshold*: Configured in `global_config.json` (default 0.85).
    - *Role*: Identifies primary upward price vectors.
3.  **Tier 2: Crash (Safety)**
    - *Threshold*: Configured in `global_config.json` (default 0.35).
    - *Role*: Vetoes trades if a significant drawdown (>3%) is imminent.

> **Legacy/Retired Tiers**:
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
    - **Step 3**: Is it safe to execute? (**Crash Safety**)
4.  **Action Handoff**: Executable signal is generated only if all 3 tiers provide a "Green Light." It then hands off control to the `async_trader_rewritten.py` layer.

---

## 4. Data Architecture & Logistics
The system utilizes a unified machine model where all processing is co-located to minimize latency and synchronization overhead.

- **Primary Data Root**: `/Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/STADIUM_DATA`
- **Model Vault**: `STADIUM_DATA/MODELS` (Subdivided into Directional and Crash).
- **LOB Source Truth**: `STADIUM_DATA/GRUS-CSV-SAMPLER-DATA`
- **Hardware Bridging**: The system is designed to run entirely on the host SSD for execution speed, with scheduled backups to external volumes handled by `local_usb_backup.sh`.

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

---

## 6. Analytics & Public Telemetry
All visual intelligence is published to GitHub Pages via the **Reporting Orchestrator**.

- **Analytics Master Hub**: [View Hub](https://stefanbund.github.io/stadium-public-data/coinbase/analytics_dashboard.html)
- **Reporting Engine**: `UNIFIED_REPORTING_WORKSPACE/generate_analytics_dashboard.py`
- **Exchange Isolation**: Data is automatically siloed by exchange name (e.g., `/coinbase`, `/binance`) to allow multi-host scaling within a single repository.

---

## 7. Fleet Information System (FIS)
The industrial backtesting arm of the project, used for yield discovery and parameter hardening.

- **Workspace**: `FLEET_INFORMATION_SYSTEM/`
- **Industrial Lean Baseline**: Standardized on high-velocity Random Forest models (`--fast-rf`) to bypass compute-heavy TPOT searches during fleet-wide deployment.
- **Experiment Vault**: `FLEET_INFORMATION_SYSTEM/EXPERIMENTS/FIS_INDUSTRIAL_LEAN_v1` (The definitive system blueprint).

---

## 15. Archival Note
The legacy documentation and decommissioned tools (Pre-CCXT/Pre-DVOL) have been moved to `TECHNICAL_DEBT/`:
- [`OLD_SYSTEM_ARCHITECTURE.md`](file:///Users/stefanbund/Developer/LAPTOP_PREPROCESSOR_MODELER/TECHNICAL_DEBT/OLD_SYSTEM_ARCHITECTURE.md)
- `advanced-sdk-ts/` (Legacy Node.js LOB Sampler)
