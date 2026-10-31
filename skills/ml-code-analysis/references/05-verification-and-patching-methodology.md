# 05 — Evaluation & Patching Methodology

The differentiator between an ordinary code overview and an elite technical analysis report is **critical evaluation and actionable remediation**.

A machine learning system often looks flawless on surface metrics (e.g., RMSE = 0.0000, Fitness = $\infty$, or Train Accuracy = 99.8%) while harboring deep architectural and domain flaws.

---

## 1. Uncovering Hidden Failures in ML Systems

### A. Non-Discriminative Objective Functions
* **Symptom**: Fitness returns $\infty$ (e.g., $1 / \text{penalty}$ where penalty is 0).
* **The Flaw**: Any solution that lands within loose bounds receives identical maximum fitness. The optimizer has zero incentive to differentiate between a beautifully balanced solution and an unbalanced edge solution.
* **Remedy**: Bounded continuous fitness functions with tie-breakers:
  $$\text{Fitness} = \frac{1000}{1 + \text{Penalty}} + \lambda \cdot \text{BalanceScore}$$

### B. Misapplied Evaluation Metrics
* **Symptom**: An optimization problem is judged with classification metrics (e.g., F1-score), or imbalanced classes are judged with raw accuracy.
* **The Flaw**: Measuring an algorithm against a metric it was never optimized for produces deceptive baseline scores (e.g., F1 = 0.410).
* **Remedy**: Adapt the metric to domain constraints with rigorous mathematical formulation:
  - Example: **F1 Distribusi Waktu Makan (F1-WM)** in dietary optimization, where precision measures how many meals adhere to the 25/10/30/10/25% energy distribution rule within $\pm 15\%$, and recall measures coverage.

### C. Solution Duplication & Premature Convergence
* **Symptom**: Top-100 personal bests yield only 3 to 7 unique solutions; the top 5 solutions are completely identical.
* **The Flaw**: Without diversity enforcement or deduplication in post-processing, the user receives illusory "choices".
* **Remedy**: Deduplication hash filters, diversity niching, and unique dictionary keys in the export module.

### D. Missing Seeds & Reproducibility
* **Symptom**: Different executions yield radically different outputs, or no seed is set in stochastic components (`random`, `numpy.random`, `torch.manual_seed`).
* **The Flaw**: Unreproducible research and unpredictable production behavior.

---

## 2. Crafting Concrete Code Patches

In Chapter 7 (*EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN*), do not merely suggest conceptual fixes. Provide **complete, runnable, tested code patches**.

Each patch block must include:
1. Target file and line span to replace or insert.
2. Complete code block formatted with syntax highlighting.
3. Explanation of algorithmic mechanism introduced.
4. Trade-off analysis (e.g., runtime overhead vs solution quality).

---

## 3. Multi-Seed Empirical Verification

Never report single-run anecdotal results. Run and document controlled experiments across at least 5 random seeds comparing the unpatched baseline against the patched system on identical hardware.

### Benchmark Reporting Template

| Metric | Baseline (5 seeds) | Patched System (5 seeds) | Relative Change |
|---|---:|---:|---:|
| **Domain Quality Metric (e.g., F1-WM)** | $0.410 \pm 0.225$ | $\mathbf{0.883 \pm 0.079}$ | **+115.4%** |
| **Precision** | $0.500$ | $\mathbf{1.000}$ | **+100.0%** |
| **Recall** | $0.350$ | $\mathbf{0.800}$ | **+128.6%** |
| **Numeric Deviation (RMSE)** | $0.0000$ | $0.0038$ | Trade-off ($\approx 9 \text{ kcal}$) |
| **Unique Solutions in Pool** | $7.0$ (range 3–11) | $\mathbf{27.2}$ (range 11–49) | **+288.6%** |
| **Runtime per Run** | $18.9 \text{ s}$ | $\mathbf{9.3 \text{ s}}$ | **-50.8% (Early Stopping)** |
| **Total Evaluations** | $20,100$ | $\approx 9,900$ | **-50.7%** |

---

## 4. Prioritized Engineering Roadmap

Conclude the evaluation chapter with a structured priority table:

| Priority | Patch Name | Target File | Impact | Effort |
|---|---|---|---|---|
| **P1 (Critical)** | Domain Distribution Penalty & Unique Export Key | `pso.py`, `output.py` | Eliminates menu skew and duplicate recommendations | Low |
| **P2 (High)** | Bounded Fitness with Tie-Breaker & Early Stopping | `pso.py` | Halves execution time, guarantees discriminatory ranking | Medium |
| **P3 (Medium)** | Automated Evaluation Module & Dataset Expansion | `evaluasi.py`, `dataset.xlsx` | Enables systematic regression testing and balances snack pool | Medium |
