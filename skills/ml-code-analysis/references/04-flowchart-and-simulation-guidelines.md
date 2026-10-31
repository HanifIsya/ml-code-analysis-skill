# 04 — Flowchart & Step-by-Step Simulation Guidelines

Chapter 5 of the technical report (*DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP*) is the pedagogical core of the document. It connects theoretical architecture directly to line-by-line code execution.

---

## 1. High-Resolution Visual Flowchart (Diagram Alur 1)

### Visual Quality Requirements
- **Resolution**: High DPI (minimum 300 DPI, recommended canvas width $\ge 2400 \text{ px}$).
- **Aspect Ratio & Sizing**: Sized to fit precisely within a single A4 page with 1.0-inch margins (recommended width: $4.8 \text{ to } 5.2 \text{ inches}$, height $\le 8.0 \text{ inches}$) so that the Heading, lead-in paragraph, image, and caption all remain together on one page.
- **Typography in Flowchart**: Bold sans-serif or clean serif font, high-contrast text against node backgrounds.
- **Stage Classification**: Distinct visual styling or colors for:
  - Input/Output Data nodes.
  - Core Processing nodes.
  - Heuristic/Iterative Loops.
  - Fitness Evaluation / Loss nodes.
  - Decision / Convergence gates.

### Accompanying Narrative
Directly following the diagram, write a systematic, multi-stage narrative detailing:
1. Stage 1: Parameter Ingestion & Preprocessing.
2. Stage 2: Solution Representation & Search Space Mapping.
3. Stage 3: Optimization / Training Iteration Loop.
4. Stage 4: Convergence Checking & Objective Evaluation.
5. Stage 5: Post-Processing, Deduplication & Export Formatting.

---

## 2. Step-by-Step Numerical Simulation ("Contoh Pengerjaan Simpel")

The simulation must walk the reader through a concrete, end-to-end execution of the pipeline using real, realistic numbers from start to finish.

### Rule 1: Concrete Study Case Profile
Never use abstract variables like $X_1, X_2$. Define a real scenario:
- **For Diet / Optimization Systems**:
  - Subject: Male, 25 years old, 65 kg, 170 cm, Moderate Activity.
  - Basal Ideal Body Weight: $BBI = (170 - 100) \times 0.9 = 63 \text{ kg}$.
  - Daily Calorie Target: $2,457 \text{ kcal}$.
  - Target Nutrition Range: Carbs (276.4–399.3 g), Protein (61.4–122.9 g), Fat (54.6–68.2 g), Fiber (25–35 g).
- **For NLP / Fact Checking Pipelines**:
  - Sample Claim: *"Vaksin influenza dapat mencegah pneumonia akibat infeksi bakteri sekunder."*
  - Preprocessed tokens, TF-IDF / Embedding vector representation.
  - Retrieved evidence passage with cosine similarity $0.812$.
  - Softmax classification probabilities: Entailment 87.4%, Contradiction 8.1%, Neutral 4.5%.

### Rule 2: Walk Through Every Calculation
Show all arithmetic formulas explicitly:
1. Raw inputs $\to$ intermediate formula $\to$ calculated value.
2. Fitness function penalty calculation ($L_1$ distance, normalized deviation).
3. Velocity update equation:
   $$v_i(t+1) = w \cdot v_i(t) + c_1 r_1 (p_{\text{best}} - x_i) + c_2 r_2 (g_{\text{best}} - x_i)$$
4. Final convergence state: Penalty $= 0$, Fitness $= \infty$, RMSE $= 0.0000$.

### Rule 3: Exact Code Snippet on EVERY Step
Every single step of the simulation must be accompanied by the exact source code snippet executing that specific operation.
- Header must include exact file name and line span (e.g., `app.py line 37–48`).
- The snippet body must be 100% identical to the source file.
- The step narrative explains how the specific lines of code produced the numbers calculated in the simulation.

### Standard Step Progression Structure
| Step | Focus Area | Code Reference | Numerical Output |
|---|---|---|---|
| **Step 1** | User Input & Parameter Setup | `app.py` CLI / config lines | Captured parameter dictionary |
| **Step 2** | Requirement / Target Computation | Math / nutrition module lines | Target bounds table |
| **Step 3** | Dataset Ingestion & Index Space | Data loader / schema lines | Solution vector dimension bounds |
| **Step 4** | Particle / Sample Initialization | Random seed & init lines | Vector $X_0$ evaluation ($P = 0.2250, \text{Fit} = 4444.44$) |
| **Step 5** | Iterative Update & Movement | Velocity & position update lines | Step $t=1$ vector clipping & new position |
| **Step 6** | Convergence & Optimum Solution | Objective evaluation lines | Rank #1 solution vector, metrics zero-error |
| **Step 7** | Post-Processing, Ranking & Export | Output formatting & Excel lines | Final multi-sheet workbook generation |
