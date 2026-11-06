# Open Quantitative Research Series: High-Frequency Digital Asset Microstructure & Causal Inference

Welcome to the public quantitative research library of the **Autonomous Causal Fleet Architecture** ([`LAPTOP_PREPROCESSOR_MODELER`](https://github.com/stefanbund/stadium-public-data)). 

This series documents the mathematical formulations, econometric models, and empirical production telemetry behind our high-frequency algorithmic market-making engine deployed across AWS EC2 and dedicated data-science nodes.

---

## Published Whitepapers

| Paper | Focus Stream | Core Econometric & Microstructure Concepts | Full Text |
| :--- | :--- | :--- | :---: |
| **Paper 1** | **Cross-Venue Causal Interplay (Derivatives $\to$ Spot)** | Lead-Lag SVAR, Garbade-Silber Information Shares, Cross-Venue Basis Dislocation ($\text{Basis}_{\text{bps}}$), Robinson Double Machine Learning (DML) Macro Beta Deconfounding | [**Read Paper 1**](paper_1_cross_venue_causal_transmission.md) |
| **Paper 2** | **Isolated Spot Microstructure (Coinbase Advanced Trade)** | Cont-Stoikov Multi-Level Order Flow Imbalance (OFI), Poisson Queue Position Estimation (QPE), Easley-de Prado VPIN Flow Toxicity, Pure Maker Retention Mandate | [**Read Paper 2**](paper_2_coinbase_spot_microstructure.md) |

---

## Architectural Synthesis: The Two-Tier Decision Hierarchy

Our production system decomposes market making into a strict, two-tiered causal hierarchy:

```
                           [ REAL-TIME RAW DATA INGESTION ]
                                          │
            OKX Trade & L2 Books5 Stream (Perps)   Coinbase Ticker & L2 Depth (Spot)
                                          │
                                          ▼
                ┌───────────────────────────────────────────────────┐
                │        TIER 1: MACRO CAUSAL DEFENSE GATES         │
                │        (Paper 1: Cross-Venue Causal Transmission) │
                └───────────────────────────────────────────────────┘
                                          │
                 • Is Offshore Perp Basis Dislocated? (|Basis| > 3.5 bps)
                 • Is Local Altcoin OFI Confounded by BTC Beta? (DML Residual <= 0.10)
                 • Are Hawkes Cascades Active? (Jump Intensity J_down > 2.5)
                                          │
                                 [ PASSED ALL GATES ]
                                          │
                                          ▼
                ┌───────────────────────────────────────────────────┐
                │      TIER 2: COINBASE SPOT MICROSTRUCTURE SNIPER  │
                │      (Paper 2: Passive Liquidity Provision)       │
                └───────────────────────────────────────────────────┘
                                          │
                 • Is Local Coinbase OFI Positive? (OFI_5s >= +0.50)
                 • Is Queue Ratio Favorable? (QR <= 0.40, Low V_ahead)
                 • Is Order Flow Non-Toxic? (VPIN < 0.61, Kyle's Lambda < 0.08)
                 • Does Conditional Alpha Exceed Fee Hurdle? (Pillar 5 Counterfactual)
                                          │
                                 [ PASSED ALL GATES ]
                                          │
                                          ▼
                      [ SUBMIT PASSIVE POST_ONLY LIMIT BUY ]
                      [ POST IMMEDIATE RESTING SELL AT TARGET (+28 bps) ]
```

---

## Production Verification & Reproducibility

All empirical performance figures cited across these papers are derived directly from live production runs supervised by `guardian_causal.py` on AWS EC2 node `44.200.49.112`.

To audit or reproduce these findings locally:
1. **Fleet Information System (FIS) Experiment Registry**:
   * Inspect [`FLEET_INFORMATION_SYSTEM/EXPERIMENTS/experiment_registry.csv`](../FLEET_INFORMATION_SYSTEM/EXPERIMENTS/experiment_registry.csv) for discrete tournament logs.
2. **Double Machine Learning Weight Extraction**:
   * Review the Robinson DML deconfounder in [`FLEET_INFORMATION_SYSTEM/CAUSAL_ENGINE/dml_deconfounder.py`](../FLEET_INFORMATION_SYSTEM/CAUSAL_ENGINE/dml_deconfounder.py).
3. **Execution Engine Invariant Test Suite**:
   * Run the local preflight verification suite:
     ```bash
     python3 test_execution_engine.py
     python3 test_causal_inference_engine.py
     ```

---

## Connect via Twitter / X

Real-time **Causal Microstructure Weather Reports** are broadcast continuously via our automated reporting daemon, providing live readings of:
* Cross-Venue Basis Dislocation
* Downward Jump Intensity ($J_{\text{down}}$)
* Realized Micro-Volatility
* Active Causal Barrier Interceptions

Follow the live stream: [**@QuantWeatherHFT**](https://x.com)
