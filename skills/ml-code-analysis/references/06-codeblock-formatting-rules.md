# 06 — Codeblock Formatting & Verification Rules

Every code snippet in the report must be strictly traceable to actual source files in the project.

---

## 1. Header Format Convention

Every codeblock in the Word document is constructed as a 2-row table. The top cell (Row 0) acts as the header bar:

### Acceptable Header Syntaxes
1. `<filename> line <start>-<end>`
   - Example: `app.py line 37-48`
2. `<filename> · <component_or_function>`
   - Example: `nutrisi.py · hitung_kebutuhan()`
3. `<filename> · line <start>-<end>`
   - Example: `pso.py · line 187-204`

### Header Visual Styling
- Background shading: `#FFFFFF` (White) or `#EAECEE` (Subtle light gray).
- Padding: Top 70 dxa, Bottom 70 dxa, Left 100 dxa, Right 100 dxa.
- The file name is styled in Times New Roman 13 pt, colored `#1155CC` (Hyperlink Blue), and underlined.
- The trailing line range or component name is in Times New Roman 13 pt, black, non-underlined.
- Alignment: Center.

---

## 2. Code Body Styling

Row 1 contains the code snippet:
- Background shading: `#121314` (Deep black/charcoal).
- Padding: Top 110 dxa, Bottom 110 dxa, Left 110 dxa, Right 110 dxa.
- Font: Courier New, 9.0 pt (or 8.5 pt for wide lines).
- Line Height: Exact `Pt(10.3)`.
- Token Colors (GitHub Dark Theme):
  - Keywords & Operators: `#FF7B72` (Coral Pink)
  - String Literals: `#A5D6FF` (Sky Blue)
  - Numeric Literals: `#79C0FF` (Light Cyan)
  - Function Names: `#D2A8FF` (Lavender Purple)
  - Built-in Types & Names: `#FFA657` (Golden Orange)
  - Comments: `#8B949E` (Slate Gray)
  - Plain Text / Identifiers: `#C9D1D9` (Light Gray)
- Every code line has a bottom border: `<w:bottom w:val="single" w:sz="4" w:space="0" w:color="21262D"/>` to create clean code-editor line divisions.

---

## 3. Strict 100% Character-by-Character Parity

**Zero Tolerance for Hallucinated or Edited Source Code:**
- The text extracted from the code block body MUST match lines `start_line` to `end_line` of the real source file character-for-character.
- Do not abbreviate code with comments like `# ... rest of function ...` inside a block that cites a line range.
- If you need to show only part of a function, specify the exact line numbers that correspond to that part (e.g., `pso.py line 192-204` rather than `pso.py line 138-283`).

---

## 4. Automated Parity Verification

Run `python scripts/verify_analysis_report.py <report.docx> <source_code_dir>` before delivering the document:

```bash
python scripts/verify_analysis_report.py "ANALISIS KODE MACHINE LEARNING - PSO.docx" "./PSO"
```

The verifier will:
1. Scan every 2-row table in the document.
2. Parse the header regex `([\w\-./\\]+\.(?:py|ipynb))\s*(?:line|[·\-])\s*(\d+)\s*[-–]\s*(\d+)`.
3. Locate the corresponding file in `source_code_dir`.
4. Compare line-by-line.
5. Exit with status code `0` only if all blocks pass with 100% parity.
