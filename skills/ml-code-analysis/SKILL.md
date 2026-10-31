---
name: ml-code-analysis
description: "Perform comprehensive, publication-grade Machine Learning and AI code analysis. Inspects source code, datasets, execution logs, and mathematical models to produce rigorous Word (.docx) technical reports featuring verified codeblocks, architectural flowcharts, step-by-step numerical simulations, critical evaluations, runnable patches, and empirical benchmark tables."
license: MIT
author: Hanif Isya Annafi
---

# Machine Learning Code Analysis & Technical Report Generator Skill

This skill guides AI agents in conducting comprehensive, academic- and enterprise-grade code analyses of Machine Learning, Deep Learning, Optimization, and Data Science systems.

It produces a complete, beautifully formatted Microsoft Word (`.docx`) deliverable adhering strictly to the publication standard established in `hasil akhir docs/`.

---

## When to Invoke This Skill

Invoke this skill whenever the user asks to:
- Analyze, review, audit, or break down a Machine Learning codebase, pipeline, or repository.
- Produce a comprehensive technical report or Word (.docx) document analyzing ML code (e.g. PSO, Genetic Algorithms, Deep Learning, NLP, Classification, Recommendation Systems).
- Explain code line-by-line with exact line numbers and syntax-highlighted blocks.
- Generate an architectural flowchart and a step-by-step concrete numerical simulation ("Contoh Pengerjaan Simpel") of the pipeline.
- Evaluate algorithm performance, uncover hidden metric pitfalls (e.g. F1-score misalignments, non-discriminative fitness), and propose verified code patches.

---

## Crucial Prerequisites & Input Validation

Before beginning the analysis, verify that the following materials are accessible in the workspace:
1. **Source Code**: Python scripts (`.py`), orchestration modules, or Jupyter Notebooks (`.ipynb`).
2. **Dataset Schemas**: The dataset files (`.xlsx`, `.csv`) or sample rows with complete column dictionaries.
3. **Execution Logs**: Terminal logs, training traces, iteration outputs, or metric histories.
4. **Domain Objectives**: The problem definition, formulas (e.g. Harris-Benedict, BBI, Cosine Similarity, Loss), and evaluation goals.

*Reference: Read `references/01-prerequisites-and-input-checklist.md` for the complete checklist. If any essential component is missing, ask the user before guessing.*

---

## The Standard 8-Chapter Report Architecture

The final Word document must feature the following standard structure:

1. **Title Page**: Clean centered title (`ANALISIS KODE MACHINE LEARNING`), subtitle, and metadata note.
2. **DAFTAR ISI (Page 1)**: Centered `DAFTAR ISI` 14pt bold, right-aligned tab stops at 6.20 inches with dotted leaders (`WD_TAB_LEADER.DOTS`) and verified physical page numbers.
3. **ALUR BACA KODE**: High-level execution flow graph, solution space / parameter dimension calculation, architectural overview.
4. **ANALISA KODE**:
   - Section 1: File and dataset inventory tables.
   - Sections 2..N: Module-by-module line-by-line walkthrough with dark syntax-highlighted code blocks (header: `filename line A-B`, blue underlined file name).
5. **HASIL EKSEKUSI**: Test scenario parameters, console/iteration logs, metrics summary tables, artifact screenshots.
6. **DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP** *(Starts on a fresh page immediately after Chapter 5)*:
   - **Section 1: Diagram Alur (Flowchart) Proses Sistem**: High-resolution visual flowchart (`Diagram Alur 1`), accompanied by a multi-stage narrative.
   - **Section 2: Contoh Pengerjaan Simpel Proses dari Awal Hingga Jadi**: Concrete numerical study case (real numbers). Calculates every intermediate step from input to output. Accompanied by verified source code snippets (header `file line A-B`) on **every single step**.
7. **EVALUASI DAN TEMUAN**: Tabular summary of Functional Findings, Technical / Algorithmic Findings, and Dataset Quality Findings.
8. **EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN** *(Starts on a fresh page)*:
   - Domain metric clarification (e.g., adapting standard F1 to domain constraints such as F1-WM).
   - Baseline empirical measurements documenting failure modes.
   - Concrete, runnable code patches.
   - Controlled multi-seed empirical comparison table (Baseline vs Patched across $\ge 5$ seeds).
   - Structured priority roadmap (P1, P2, P3).
9. **KESIMPULAN**: Final technical synthesis and conclusions.

*Reference: Read `references/02-eight-chapter-report-structure.md`.*

---

## Step-by-Step Execution Workflow

### Phase 1: Ingestion & Inventory
1. Explore all project files in the workspace (`glob`, `read`).
2. Catalog all source files, line counts, classes, functions, and import dependencies.
3. Inspect dataset files: sheet names, row/column counts, column types, missing values, and value ranges.
4. Calculate the total solution space or state space dimension:
   $$S = \prod_{k=1}^K N_k$$

### Phase 2: Execution & Output Trace Analysis
1. Inspect runtime logs or execute the pipeline with a controlled seed to record stdout/stderr.
2. Record initial objective scores, iteration improvements, and final convergence metrics.
3. Identify metric anomalies (e.g., fitness $= \infty$, RMSE $= 0.0000$, loss saturation, or duplicate solutions).

### Phase 3: Drafting the Concrete Numerical Simulation
1. Define a realistic case study (e.g., Subject: Male, 25 years old, 65 kg, 170 cm, Sedang).
2. Manually or programmatically compute the exact numerical value of each intermediate variable across 7 steps:
   - Step 1: User input CLI parsing.
   - Step 2: Target requirements calculation (formulas, upper/lower bounds).
   - Step 3: Mapping dataset items to vector indices.
   - Step 4: Initial candidate evaluation (penalty, fitness value).
   - Step 5: Iterative update (velocity, position clipping).
   - Step 6: Convergence state and zero-error verification.
   - Step 7: Post-processing, ranking, and Excel workbook export.
3. Extract exact source code lines for each step from the project files. Verify line numbers.

### Phase 4: High-Resolution Flowchart Generation
1. Formulate the pipeline architecture into a structured diagram.
2. Render the flowchart as a high-resolution PNG image ($\ge 2400 \text{ px}$ width, 300 DPI) using Matplotlib, Graphviz, or Mermaid rendering.
3. Scale the image in Word to $4.8 \times 7.9 \text{ inches}$ so the heading, intro, image, and caption fit on a single A4 page.

### Phase 5: Critical Evaluation & Patching
1. Formulate domain-adapted metrics if standard metrics are misleading.
2. Create runnable code patches addressing identified technical flaws (e.g., penalty additions, tie-breakers, early stopping, deduplication keys).
3. Benchmark the baseline vs the patched code across at least 5 seeds on identical hardware. Tabulate results.

### Phase 6: Document Compilation (`scripts/ml_docx_builder.py`)
1. Use `scripts/ml_docx_builder.py` to assemble the Word document:
   ```python
   from ml_docx_builder import MLReportDocx

   builder = MLReportDocx()
   builder.add_title_page("ANALISIS KODE MACHINE LEARNING", "Sub-title", "Scope note")
   # DAFTAR ISI
   builder.add_toc_header()
   builder.add_toc_entry(0, "ALUR BACA KODE", 2)
   # ...
   # Add Chapters
   builder.h1("ALUR BACA KODE")
   # ...
   builder.save("ANALISIS KODE MACHINE LEARNING - REPORT.docx")
   ```
2. Ensure all formatting rules are strictly applied:
   - A4 page with 1.0 inch margins.
   - Times New Roman 12 pt, 1.15 line spacing, 6 pt space after, justified body.
   - Headings 14/13/13 pt bold with `keep_with_next`.
   - Dark syntax highlighted code blocks with `cantSplit`.
   - Data tables with soft navy header (`#D9E2F3`), cell padding, repeating header, and `cantSplit`.
   - Callout boxes with thick left accent border.
   - Centered page number footer.

### Phase 7: Verification Harness (`scripts/verify_analysis_report.py`)
Run the automated verification script:
```bash
python scripts/verify_analysis_report.py "output_report.docx" "<source_code_dir>"
```
Ensure:
- 100% of code snippets match source files character-for-character.
- Zero table splits across pages.
- TOC page numbers reflect actual pagination.

---

## References Directory Index

For in-depth guidelines on specific tasks, consult the modular references:
- `references/01-prerequisites-and-input-checklist.md` — Mandatory files, datasets, and context needed before analysis.
- `references/02-eight-chapter-report-structure.md` — Detailed chapter-by-chapter outline.
- `references/03-docx-typography-and-styling-guide.md` — Word XML nodes, styles, margins, and palette.
- `references/04-flowchart-and-simulation-guidelines.md` — High-resolution flowcharts and 7-step numerical simulation.
- `references/05-verification-and-patching-methodology.md` — Metric auditing, patch engineering, and multi-seed benchmarking.
- `references/06-codeblock-formatting-rules.md` — Code block headers, syntax coloring, and parity verifier.
