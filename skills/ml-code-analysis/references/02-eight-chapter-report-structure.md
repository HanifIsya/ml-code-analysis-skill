# 02 — The Standard 8-Chapter Technical Report Structure

Every comprehensive Machine Learning Code Analysis produced by this skill adheres to an eight-chapter structure engineered for clarity, technical depth, and rigorous academic/professional standards.

---

## Document Layout Blueprint

```
[Cover / Title Page]
    └── Title, Subtitle, File/Line Scope Note
[Chapter 1: DAFTAR ISI]
    └── Right-aligned Dotted Leader Table of Contents (Page 1)
[Chapter 2: ALUR BACA KODE]
    └── High-level Execution Flow, Solution Space, Dimensionality
[Chapter 3: ANALISA KODE]
    ├── 1. Overview of Files, Notebooks & Datasets
    └── 2..N. Module Deep Dives (Dark Syntax Codeblocks + Logic Breakdown)
[Chapter 4: HASIL EKSEKUSI]
    └── Scenarios, Iteration Logs, Target vs Output Tables, Artifacts
[Chapter 5: DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP] (New Page Break)
    ├── 1. High-Resolution Visual Flowchart (Diagram Alur 1)
    └── 2. Step-by-Step Simulation with Real Numbers & Verified Code Snippets
[Chapter 6: EVALUASI DAN TEMUAN]
    └── Functional, Technical/Architectural, and Data Quality Findings
[Chapter 7: EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN] (New Page Break)
    ├── Metric Clarification & Domain Adaptation
    ├── Proposed Code Patches (Runnable Blocks)
    ├── Multi-Seed Empirical Validation (Baseline vs Patched)
    └── Prioritized Engineering Roadmap (P1, P2, P3)
[Chapter 8: KESIMPULAN]
    └── Final Engineering & Methodological Synthesis
```

---

## Detailed Chapter Specifications

### Title Page
- **Document Title**: `ANALISIS KODE MACHINE LEARNING`
- **Subtitle**: Clear summary of the pipeline/algorithm (e.g., `Sistem Rekomendasi Menu Makan Harian dengan Particle Swarm Optimization (PSO)` or `Pipeline Topic Modelling, Claim Extraction, Retrieval, dan NLI`).
- **Metadata Note**: Scope summary (e.g., `Empat berkas Python, 700 baris kode, 60 blok kode terverifikasi`).

### 1. DAFTAR ISI (Table of Contents)
- Placed on Page 1.
- Center-aligned heading: `DAFTAR ISI` (14 pt bold).
- Right-aligned tab stop at 6.20 inches with dot leaders (`WD_TAB_LEADER.DOTS`).
- Bold level-0 chapter entries, indented level-1 sub-chapter entries.
- Page numbers must match physical pagination.

### 2. ALUR BACA KODE (Code Reading Flow)
- Executive flow string: `module_a.py func() -> module_b.py process() -> ...`
- Quantitative complexity: Mathematical formulation of search space ($S = \prod K_i$) or state space dimension ($D$).
- Algorithmic properties: Stochastic vs Deterministic, population sizes, evaluation bounds.
- Cross-reference lead-in directing readers to Chapter 5 for visual diagrams and numerical walkthroughs.

### 3. ANALISA KODE (Code Deep-Dive)
- **1. File & Data Inventory**:
  - Table of files, line counts, classes, and roles.
  - Table of dataset sheets, record counts, feature schemas, missing values.
- **2..N. Module-by-Module Walkthrough**:
  - Header with source file name and line span.
  - Dark-mode syntax highlighted code block (`Courier New 9pt`, Pygments colored tokens).
  - Analytical breakdown:
    - Function signatures and parameters.
    - Mathematical formulation and algorithmic logic.
    - Edge cases and error handling.
  - Informational callout boxes for architectural notes or design trade-offs.

### 4. HASIL EKSEKUSI (Execution Results)
- Test scenario setup (input profile, hardware, execution parameters).
- Real iteration/training terminal logs.
- Optimization/Prediction result tables (Rank #1 vs targets, precision/recall/F1, RMSE/MAE).
- Highlighting non-discriminative metrics (e.g., fitness `inf` or loss plateaus).
- Screenshots or rendered views of generated output artifacts.

### 5. DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP
*Must start on a fresh page (`page_break_before = True`) immediately after Chapter 4.*
- **Section 1: Diagram Alur (Flowchart) Proses Visual**:
  - High-resolution visual diagram (`Diagram Alur 1`).
  - Narrative breakdown of each major pipeline stage.
- **Section 2: Contoh Pengerjaan Simpel Proses dari Awal Hingga Jadi**:
  - Concrete case study with real numerical values (e.g., Person: 65 kg, 170 cm, 25 years old).
  - Walkthrough calculating every intermediate variable step-by-step from raw input to final output.
  - Every step must be accompanied by verified source code snippets (header `file line A-B`).
  - Intermediate validation tables at critical calculation junctures.

### 6. EVALUASI DAN TEMUAN (Evaluation & Findings)
- **Tabel Temuan Fungsional**: Core feature gaps, user experience flaws.
- **Tabel Temuan Teknis**: Algorithmic bugs, random seed neglect, duplicate solutions, type casting issues.
- **Tabel Temuan Dataset**: Data skew, limited variety in sub-categories, missing boundary items.

### 7. EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN
*Must start on a fresh page (`page_break_before = True`).*
- **Metric Adaptation**: Contextualize standard metrics into domain-appropriate metrics (e.g., adapting F1 to Meal Distribution F1-WM).
- **Baseline Measurements**: Document quantitative failure modes of the current unpatched system.
- **Proposed Code Patches**: Concrete, ready-to-run code patches with line-by-line explanations.
- **Empirical Validation**: Multi-seed test comparison table (Baseline vs Patched across $\ge 5$ seeds) proving metric improvement.
- **Roadmap**: Structured P1 (Critical), P2 (Important), P3 (Enhancement) priority matrix.

### 8. KESIMPULAN (Conclusion)
- Synthesis of structural strengths and vulnerabilities.
- Verified empirical gains from proposed patches.
- Final engineering sign-off.
