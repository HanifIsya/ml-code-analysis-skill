# Example Input Specification for ML Code Analysis

This specification demonstrates the minimum context and information an analyst or AI agent should gather before conducting an in-depth machine learning code analysis.

---

## 1. Project Profile & Problem Statement
* **Project Name**: Genetic Algorithm Feature Selector for Industrial Fault Detection (`FaultGA`)
* **Objective**: Select an optimal subset of 12 features out of 120 sensor channels to maximize F1-score on rare fault events while minimizing feature acquisition latency.
* **Algorithm**: Binary Genetic Algorithm (Population: 50, Generations: 100, Tournament Selection, Two-Point Crossover, Uniform Mutation).

---

## 2. Source Code Inventory
* `main.py` (84 lines) — CLI argument parser, dataset ingestion, GA orchestrator.
* `evaluator.py` (112 lines) — Cost-sensitive fitness computation, Random Forest proxy evaluator.
* `ga_core.py` (195 lines) — Chromosome initialization, selection, crossover, bit-flip mutation.
* `exporter.py` (65 lines) — Results serialization to JSON and CSV.

---

## 3. Dataset Summary
* **Format**: `sensor_stream.csv` (10,000 rows, 122 columns).
* **Target Label**: `fault_class` (0: Normal [96%], 1: Bearing Wear [2.5%], 2: Thermal Overload [1.5%]).
* **Feature Types**: Float64 vibration frequency bands and temperatures. Missing values: None.

---

## 4. Execution Trace Sample (`run.log`)
```
[INFO] Initialized population with 50 chromosomes (Length: 120 bits)
[INFO] Generation 001/100 | Best Fitness: 0.7420 | Active Features: 48/120
[INFO] Generation 025/100 | Best Fitness: 0.8890 | Active Features: 21/120
[INFO] Generation 050/100 | Best Fitness: 0.9415 | Active Features: 14/120
[INFO] Generation 100/100 | Best Fitness: 0.9630 | Active Features: 12/120
[RESULT] Execution time: 14.2s | Memory Peak: 142MB
```
