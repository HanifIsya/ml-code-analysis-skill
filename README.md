# Machine Learning Code Analysis Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills.sh](https://img.shields.io/badge/skills.sh-standard-blueviolet)](https://skills.sh)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Deliverable: Word DOCX](https://img.shields.io/badge/deliverable-DOCX%20(Publication%20Grade)-2b579a.svg)](#output-deliverable-structure)

Universal AI agent skill for comprehensive **Machine Learning, Deep Learning, and Heuristic Code Analysis**. 

Audits codebases, extracts mathematical models, renders high-resolution architecture flowcharts, computes step-by-step numerical simulations, uncovers hidden metric flaws, formulates runnable patches, and compiles publication-grade Microsoft Word (`.docx`) technical reports matching exact institutional standards.

---

## Table of Contents
1. [Overview & Philosophy](#overview--philosophy)
2. [Prerequisites: Minimum Required Files (Bahan Wajib)](#prerequisites-minimum-required-files-bahan-wajib)
3. [Installation](#installation)
4. [Output Deliverable Structure (8 Chapters)](#output-deliverable-structure-8-chapters)
5. [Document Styling & Visual Standards](#document-styling--visual-standards)
6. [Automated Verification Harness](#automated-verification-harness)
7. [Repository Layout](#repository-layout)
8. [Privacy & Confidentiality Guarantee](#privacy--confidentiality-guarantee)
9. [License](#license)

---

## Overview & Philosophy

Most automated code reviews generate brief, superficial summaries that overlook algorithmic nuances, edge-case bottlenecks, and deceptive metrics.

This skill instructs AI agents to conduct **deep architectural audits** and construct comprehensive, multi-chapter Word deliverables. It guarantees:
- **100% Code Block Parity**: Every code snippet cited in the document is verified character-by-character against actual source code files with exact line numbers.
- **Concrete Numerical Walkthroughs**: Replaces abstract variable explanations with real-world case simulations calculating every intermediate arithmetic step.
- **Critical Metric Remediation**: Uncovers misleading evaluations (such as non-discriminative fitness functions or unadapted classification metrics) and provides tested, benchmarked code patches.
- **Enterprise Word Formatting**: Automatically styles A4 geometry, non-splitting data tables (`cantSplit`), dark syntax-highlighted code blocks, visual callouts, and dotted-leader Tables of Contents.

---

## Prerequisites: Minimum Required Files (Bahan Wajib)

To ensure the AI produces an accurate, exhaustive report without hallucinations or conceptual misunderstandings, the workspace **must contain the following minimum materials** before running the analysis:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   MINIMUM PREREQUISITE CHECKLIST                       │
├────────────────────────────────┬───────────────────────────────────────┤
│ 1. Executable Source Code       │ Python scripts (.py) or Notebooks     │
│ 2. Dataset Samples & Schema    │ Excel (.xlsx) / CSV / Data Dictionary │
│ 3. Runtime Logs / Traces       │ Console output, iteration traces      │
│ 4. Domain & Math Objectives    │ Guidelines, formulas, constraints     │
│ 5. Output Artifacts (Optional) │ Generated Excel, models, plots        │
└────────────────────────────────┴───────────────────────────────────────┘
```

### 1. Complete Executable Source Code
* **What to provide:**
  - All primary Python scripts (`.py`), orchestration modules, and utility files.
  - Sequentially numbered Jupyter Notebooks (`.ipynb`) if the pipeline was developed in notebooks (e.g., `01_prepro.ipynb`, `02_model.ipynb`, `03_eval.ipynb`).
* **Why it is required:**
  - The analysis performs line-by-line inspection. Every code block in the generated document has headers formatted as `<file> line <start>-<end>` (e.g., `pso.py line 187–204`).
* **Risk if missing:** Hallucinated function signatures, fabricated variables, and verification failures.

### 2. Dataset Samples, Schema & Data Dictionaries
* **What to provide:**
  - The dataset files (`.xlsx`, `.csv`, `.parquet`, `.json`).
  - If the dataset is large or confidential, provide a representative sample (50–100 rows) alongside a complete data dictionary (column name, data type, physical unit, nullability).
* **Why it is required:**
  - The AI must calculate the combinatorial search space ($S = \prod N_k$), check class balance, and understand feature boundaries.
* **Risk if missing:** Wrong assumptions about feature distributions and impossible simulation values.

### 3. Execution Logs & Experiment Traces
* **What to provide:**
  - Actual console output logs (`run_log.txt`, terminal recordings).
  - Optimizer iteration logs (e.g., fitness scores per 50 iterations, early stopping logs).
  - Random seed information.
* **Why it is required:**
  - Reports empirical performance rather than theoretical speculation. Highlights whether the algorithm saturated or reached non-discriminative fitness (`inf`).
* **Risk if missing:** Speculative claims about execution time, memory footprint, and convergence rates.

### 4. Domain Context & Mathematical Formulation
* **What to provide:**
  - Objective function formulas (Loss, Multi-Objective Fitness, Penalty weights).
  - Domain constraints (e.g., in nutrition: Harris-Benedict, Broca, macronutrient ratios 25/10/30/10/25%; in NLP: NLI entailment thresholds; in finance: risk tolerances).
* **Why it is required:**
  - Standard ML metrics (such as raw F1 or RMSE) can be completely misleading without domain adaptation.
* **Risk if missing:** Evaluating an optimization engine as if it were a text classifier.

### 5. Output Artifacts (Recommended)
* **What to provide:**
  - Generated files (e.g., `hasil_rekomendasi.xlsx`, prediction CSVs, saved plot images).
* **Why it is required:**
  - Used for visual artifact tables, screenshots, and verifying export integrity.

---

## Installation

### Option 1: Universal Agent Skill (`skills.sh` - Recommended)
Install directly into any compatible agent harness (Antigravity, Claude Code, Cursor, Codex) using the standard skills CLI:

```bash
npx skills add HanifIsya/ml-code-analysis-skill
```

To install globally for all agents:
```bash
npx skills add HanifIsya/ml-code-analysis-skill -g --all
```

### Option 2: Claude Code Plugin
Add this repository as a marketplace source, then install:

```bash
# 1. Add marketplace
claude plugin marketplace add HanifIsya/ml-code-analysis-skill

# 2. Install plugin
claude plugin install ml-code-analysis-skill@hanifisya-ml
```

Reload plugins with `/reload-plugins`. The skill will be available as `/ml-code-analysis`.

### Option 3: Manual Clone into Agent Directory
Clone the repository and copy the skill into your agent's skills directory:

**For Antigravity / Cursor:**
```bash
git clone https://github.com/HanifIsya/ml-code-analysis-skill.git
# Copy into workspace skills directory
cp -r ml-code-analysis-skill/skills/ml-code-analysis .agent/skills/
```

**For Claude Code:**
```bash
# macOS / Linux
cp -r ml-code-analysis-skill/skills/ml-code-analysis ~/.claude/skills/

# Windows PowerShell
Copy-Item -Recurse ml-code-analysis-skill\skills\ml-code-analysis "$env:USERPROFILE\.claude\skills\"
```

### Option 4: Standalone Python Generator
The Python document builder engine works independently without LLM dependencies:

```bash
git clone https://github.com/HanifIsya/ml-code-analysis-skill.git
cd ml-code-analysis-skill
pip install -r scripts/requirements.txt
```

---

## Output Deliverable Structure (8 Chapters)

Every technical analysis document generated by this skill adheres to the rigorous 8-chapter blueprint established in institutional deliverables:

| Chapter | Title | Focus & Core Content |
|---|---|---|
| **Cover** | `ANALISIS KODE MACHINE LEARNING` | Formal title, subtitle, file inventory, and line count metadata. |
| **Bab 1** | `DAFTAR ISI` *(Halaman 1)* | Right-aligned tab stop (6.20 in) with dot leaders (`WD_TAB_LEADER.DOTS`) and verified page numbers. |
| **Bab 2** | `ALUR BACA KODE` | Program call graph, pipeline execution order, and combinatorial search space ($S \approx 2.20 \times 10^{23}$). |
| **Bab 3** | `ANALISA KODE` | File inventory tables, dataset schema breakdown, and module deep-dives with dark syntax-highlighted code blocks (`filename line A-B`). |
| **Bab 4** | `HASIL EKSEKUSI` | Test scenarios, iteration logs, target vs actual nutrient/metric tables, output spreadsheet screenshots. |
| **Bab 5** | `DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP` *(New Page)* | **1. High-Res Flowchart (`Diagram Alur 1`)**: Visual 300 DPI architecture diagram.<br/>**2. Contoh Pengerjaan Simpel**: Step-by-step concrete numerical simulation (7 steps) using real patient/user inputs, computing all intermediate values, with verified code snippets on **every step**. |
| **Bab 6** | `EVALUASI DAN TEMUAN` | Tabular classification of Functional Findings, Technical/Code Quality Findings, and Dataset Quality Findings. |
| **Bab 7** | `EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN` *(New Page)* | Domain metric adaptation (e.g., F1-WM), baseline measurement, ready-to-run code patches, multi-seed comparative benchmark ($\ge 5$ seeds), and P1–P3 priority matrix. |
| **Bab 8** | `KESIMPULAN` | Executive technical synthesis, empirical performance gains, and architectural sign-off. |

---

## Document Styling & Visual Standards

The Python engine (`scripts/ml_docx_builder.py`) enforces strict Word XML typography standards:

* **Page Geometry**: Standard A4 Paper (8.27 × 11.69 in) with 1.0 inch (25.4 mm) margins on all four sides.
* **Typography**: Times New Roman 12 pt body, 1.15 line spacing, 6 pt space after, justified alignment.
* **Headings**: Heading 1 (14 pt bold, `page_break_before`), Heading 2 & 3 (13 pt bold), with `keep_with_next = True` to eliminate orphan headings.
* **Dark Code Blocks**: 2-row table structure.
  - Header: Centered, white/light shading, blue underlined filename (`#1155CC`) + line span.
  - Body: `#121314` dark fill, Courier New 9 pt monospace font, GitHub Dark Pygments token highlighting, and bottom line borders (`#21262D`).
* **Callout Boxes**: 1×1 table, `#F2F4F7` background, thick `#7BA4D0` left accent border (3 pt / 24 sz), navy bold title, slate body text.
* **Data Tables**: Centered, `#D9E2F3` soft navy header, subtle `#8A8A8A` borders, repeating table headers (`<w:tblHeader/>`), and strict non-splitting rows (`<w:cantSplit/>`).
* **Dynamic Footers**: Centered "Halaman `<PAGE>`" dynamic Word field.

---

## Automated Verification Harness

Before finalizing any report, run the included verification script:

```bash
python scripts/verify_analysis_report.py "ANALISIS KODE MACHINE LEARNING - PSO.docx" "./PSO_extracted/PSO"
```

The verification tool checks:
1. **Line-Number Parity**: Validates that every code block with header `file.py line A-B` matches the actual physical lines in the source code file character-by-character.
2. **Table Integrity**: Asserts that every data table and callout has `cantSplit` set on all rows.
3. **Pagination Integrity**: Detects heading discrepancies against the Table of Contents.

---

## Repository Layout

```
ml-code-analysis-skill/
├── .claude-plugin/
│   ├── plugin.json                    # Claude Code plugin manifest
│   └── marketplace.json               # Marketplace registration
├── skills/
│   └── ml-code-analysis/
│       ├── SKILL.md                   # Core agent skill instructions
│       └── references/                # Modular technical reference guides
│           ├── 01-prerequisites-and-input-checklist.md
│           ├── 02-eight-chapter-report-structure.md
│           ├── 03-docx-typography-and-styling-guide.md
│           ├── 04-flowchart-and-simulation-guidelines.md
│           ├── 05-verification-and-patching-methodology.md
│           └── 06-codeblock-formatting-rules.md
├── scripts/
│   ├── ml_docx_builder.py             # Reusable Word DOCX generation library
│   ├── verify_analysis_report.py      # Automated code parity & layout verifier
│   └── requirements.txt               # python-docx, pygments, pillow
├── examples/
│   ├── sample_input_spec.md           # Template for project input specifications
│   └── build_sample_report.py         # Runnable end-to-end report demo
├── tests/
│   └── test_builder.py                # Builder unit test suite
├── .gitignore
├── LICENSE                            # MIT License
├── README.md                          # Documentation & usage guide
└── SKILL.md                           # Root skill file for universal discovery
```

---

## Privacy & Confidentiality Guarantee

This skill and repository strictly observe **zero-data-leakage principles**:
- All analysis scripts and docx builders execute entirely within the local environment.
- No user source code, proprietary datasets, private documents, or intermediate files are ever tracked or published.
- `.gitignore` is pre-configured to strictly exclude all `.docx`, `.xlsx`, `.zip`, `.pdf`, `.png`, and temporary files.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Developed with precision by **Hanif Isya Annafi** ([@HanifIsya](https://github.com/HanifIsya)).
