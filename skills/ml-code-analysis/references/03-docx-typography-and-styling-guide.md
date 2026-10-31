# 03 — Word (.docx) Typography & Styling Guide

To produce clean, publication-grade Word documents matching the benchmark deliverables in `hasil akhir docs/`, adhere strictly to these typography and layout rules.

---

## Page Geometry & Standards

| Parameter | Standard Value | XML / Python Setting |
|---|---|---|
| **Paper Size** | A4 (210 × 297 mm) | `sec.page_width = Inches(8.27)`, `sec.page_height = Inches(11.69)` |
| **Margins** | Normal (1.0 inch / 2.54 cm) | `left = right = top = bottom = Inches(1.0)` |
| **Header / Footer Distance** | 0.5 inch (1.27 cm) | `sec.header_distance = Inches(0.5)`, `sec.footer_distance = Inches(0.5)` |
| **Body Font** | Times New Roman | `font.name = "Times New Roman"` |
| **Code Font** | Courier New | `font.name = "Courier New"` |
| **Body Size & Spacing** | 12 pt, 1.15 line, 6 pt after | `line_spacing = 1.15`, `space_after = Pt(6)` |
| **Body Alignment** | Justified | `alignment = WD_ALIGN_PARAGRAPH.JUSTIFY` |

---

## Headings Hierarchy

1. **Heading 1**:
   - Size: 14 pt, Bold.
   - Spacing: 16 pt before, 6 pt after, 1.15 line spacing.
   - Page Break: `page_break_before = True` (except document title).
   - Paragraph flag: `keep_with_next = True`.
2. **Heading 2**:
   - Size: 13 pt, Bold.
   - Spacing: 16 pt before, 6 pt after, 1.15 line spacing.
   - Paragraph flag: `keep_with_next = True`.
3. **Heading 3**:
   - Size: 13 pt, Bold.
   - Spacing: 14 pt before, 4 pt after, 1.15 line spacing.
   - Paragraph flag: `keep_with_next = True`.

---

## Table of Contents (DAFTAR ISI) Styling

- Placed on Page 1.
- Tab stop set at 6.20 inches, right-aligned, with dot leader (`WD_TAB_LEADER.DOTS`).
- Level 0 entries: Times New Roman 11.5 pt, Bold, left indent 0.
- Level 1 entries: Times New Roman 11.5 pt, Regular, left indent 0.30 inch.
- Spacing: 0 pt before, 5 pt after, 1.1 line spacing.

---

## Dark Syntax Highlighted Code Blocks

Every codeblock is rendered as a 2-row × 1-column table to ensure pristine layout and border control:

```
┌─────────────────────────────────────────────────────────────┐
│              app.py · line 37–48 (Centered, Blue)           │  <- Row 0: White/Light, 13pt TNR
├─────────────────────────────────────────────────────────────┤
│ 1: def main():                                              │  <- Row 1: #121314 Dark Fill,
│ 2:     user_input = get_user_profile()                      │     Courier New 9pt,
│ 3:     targets = compute_nutrition(user_input)              │     Pygments Syntax Highlighting
└─────────────────────────────────────────────────────────────┘
```

- **Header Row**:
  - Fill: `#FFFFFF` or `#EAECEE`.
  - Padding: Top/Bottom 70 dxa, Left/Right 100 dxa.
  - Text: Filename underlined with `#1155CC`, followed by line span in black.
  - Alignment: Center.
- **Body Row**:
  - Fill: `#121314` (Deep Dark Theme).
  - Padding: Top/Bottom 110 dxa, Left/Right 110 dxa.
  - Monospace font: Courier New 9.0 pt or 8.5 pt.
  - Line height: Exact `Pt(10.3)`.
  - Line separator: Bottom border `#21262D` sz 4 on each code paragraph.
- **Table Constraints**:
  - Outer border: `#000000` sz 8 (or `#8A8A8A` sz 4).
  - Width: 6.268 inches.
  - Non-split property: `w:cantSplit` on all rows.

---

## Visual Callout Boxes

- Formed as a 1-row × 1-column table.
- Shading: `#F2F4F7`.
- Borders: Left border thick (`#7BA4D0`, sz 24 / 3pt); top, right, bottom thin (`#7BA4D0`, sz 4).
- Cell margins: Top/Bottom 100 dxa, Left/Right 140 dxa.
- Title: Times New Roman 11 pt, Bold, Deep Navy (`#154360`).
- Content: Times New Roman 10.5 pt, Slate Gray (`#2C3E50`), line spacing 1.12.
- `w:cantSplit` appended to row.

---

## Data Tables & Splitting Prevention

1. **Header Row (Row 0)**:
   - Shading: `#D9E2F3` (Soft Navy tint).
   - Font: Times New Roman 9.0 pt, Bold, Centered.
   - Repeating header XML: `<w:tblHeader/>`.
2. **Data Rows**:
   - Font: Times New Roman 8.8 pt, Regular.
   - Cell Margins: Top/Bottom 45 dxa, Left/Right 80 dxa.
   - Table borders: Single `#8A8A8A` sz 4.
3. **No-Splitting Enforcement**:
   - Every single row (`_tr`) must have `<w:cantSplit/>`.
   - All cells except the last row must have `keep_with_next = True` on their paragraphs to prevent trailing orphan rows.
4. **Captions**:
   - Placed **above** the table.
   - Centered: `Tabel N. Judul Tabel`.
   - `Tabel N.` in bold, description in regular.
   - `keep_with_next = True` on caption paragraph.

---

## Typographic Rules
- Use standard hyphens `-` with spaces ` - ` or middle dots ` · ` for separators. Avoid stray em-dashes `\u2014` and en-dashes `\u2013` where plain hyphenation is required by linters.
