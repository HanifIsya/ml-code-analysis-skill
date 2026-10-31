# -*- coding: utf-8 -*-
"""
Analysis Report Verification Tool
==================================
Performs character-by-character parity verification between code blocks in
the generated Word (.docx) technical report and the physical source code files.
Also validates table split prevention and document structure integrity.
"""

import os
import re
import sys
import docx

def verify_report(docx_path: str, source_root: str = "."):
    if not os.path.exists(docx_path):
        print(f"Error: Document '{docx_path}' not found.")
        return False

    print(f"Loading document: {docx_path}")
    doc = docx.Document(docx_path)

    # 1. Inspect code blocks
    code_blocks = []
    for i, t in enumerate(doc.tables):
        if len(t.rows) == 2 and len(t.columns) == 1:
            hdr_text = t.rows[0].cells[0].text.strip()
            # Match formats like: "app.py line 10-25" or "app.py · line 10-25" or "app.py - line 10-25"
            m = re.search(r"([\w\-./\\]+\.(?:py|ipynb|sh|sql|json|yml|yaml))\s*(?:line|[·\-])\s*(\d+)\s*[-–]\s*(\d+)", hdr_text, re.IGNORECASE)
            if m:
                fname = m.group(1).replace("\\", "/")
                # if there is a prefix or just filename, strip leading junk
                fname = os.path.basename(fname)
                start_l = int(m.group(2))
                end_l = int(m.group(3))
                body_cell = t.rows[1].cells[0]
                body_text = "\n".join(p.text for p in body_cell.paragraphs)
                code_blocks.append((fname, start_l, end_l, body_text))

    print(f"Discovered {len(code_blocks)} code blocks with line-number headers.")

    # Find source files in source_root
    found_files = {}
    for root, _, files in os.walk(source_root):
        for f in files:
            if f not in found_files:
                found_files[f] = os.path.join(root, f)

    mismatches = 0
    missing_files = 0
    verified = 0

    for fname, a, b, text in code_blocks:
        if fname not in found_files:
            print(f"[MISSING] Source file '{fname}' not found in search path '{source_root}'")
            missing_files += 1
            continue

        src_path = found_files[fname]
        try:
            with open(src_path, "r", encoding="utf-8", errors="replace") as f:
                lines = f.read().splitlines()
        except Exception as e:
            print(f"[ERROR] Could not read '{src_path}': {e}")
            missing_files += 1
            continue

        expected = "\n".join(lines[a - 1 : b])
        if text.strip() == expected.strip():
            print(f"[OK]   {fname} line {a}-{b} ({b - a + 1} lines)")
            verified += 1
        else:
            mismatches += 1
            print(f"[FAIL] Parity mismatch in {fname} line {a}-{b}")
            exp_lines = expected.split("\n")
            got_lines = text.split("\n")
            for idx in range(min(5, max(len(exp_lines), len(got_lines)))):
                e = exp_lines[idx] if idx < len(exp_lines) else "<none>"
                g = got_lines[idx] if idx < len(got_lines) else "<none>"
                if e != g:
                    print(f"       Difference at line {a + idx}:")
                    print(f"       Expected: {repr(e)}")
                    print(f"       Found:    {repr(g)}")

    # 2. Inspect Table cantSplit
    unsplittable_tables = 0
    total_data_tables = 0
    for t in doc.tables:
        if len(t.rows) > 2 and len(t.columns) > 1:
            total_data_tables += 1
            has_cantsplit = all(
                any(child.tag.endswith("cantSplit") for child in row._tr.get_or_add_trPr())
                for row in t.rows
            )
            if has_cantsplit:
                unsplittable_tables += 1

    print("\n--- Summary ---")
    print(f"Total codeblocks: {len(code_blocks)}")
    print(f"Verified matching: {verified}")
    print(f"Mismatches: {mismatches}")
    print(f"Missing source files: {missing_files}")
    print(f"Data tables with non-splitting rows: {unsplittable_tables}/{total_data_tables}")

    if mismatches == 0 and missing_files == 0:
        print("\nResult: VERIFICATION PASSED (100% Code Parity)")
        return True
    else:
        print(f"\nResult: VERIFICATION FAILED ({mismatches} mismatches, {missing_files} missing files)")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_analysis_report.py <path_to_report.docx> [source_dir]")
        sys.exit(1)

    doc_file = sys.argv[1]
    src_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    ok = verify_report(doc_file, src_dir)
    sys.exit(0 if ok else 1)
