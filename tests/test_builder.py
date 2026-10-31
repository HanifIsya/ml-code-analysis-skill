# -*- coding: utf-8 -*-
"""
Unit Tests for ML DOCX Builder
==============================
Tests document creation, typography settings, table non-splitting,
codeblock generation, and callouts.
"""

import os
import sys
import tempfile
import unittest
import docx

# Ensure scripts directory is on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from ml_docx_builder import MLReportDocx

class TestMLDocxBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = MLReportDocx()

    def test_document_setup(self):
        sec = self.builder.doc.sections[0]
        # A4 width is 8.27 in, height is 11.69 in
        self.assertAlmostEqual(sec.page_width.inches, 8.27, places=2)
        self.assertAlmostEqual(sec.page_height.inches, 11.69, places=2)
        self.assertAlmostEqual(sec.left_margin.inches, 1.0, places=2)
        self.assertAlmostEqual(sec.right_margin.inches, 1.0, places=2)

    def test_add_headings_and_paragraphs(self):
        p1 = self.builder.h1("TEST CHAPTER")
        self.assertTrue(p1.paragraph_format.page_break_before)
        self.assertTrue(p1.paragraph_format.keep_with_next)

        p2 = self.builder.h2("Sub-chapter")
        self.assertFalse(p2.paragraph_format.page_break_before)
        self.assertTrue(p2.paragraph_format.keep_with_next)

        para = self.builder.para("Sample text paragraph")
        self.assertEqual(para.text, "Sample text paragraph")

    def test_callout_box(self):
        tbl = self.builder.callout("Insight Title", ["Line 1", "Line 2"])
        self.assertEqual(len(tbl.rows), 1)
        self.assertEqual(len(tbl.columns), 1)
        # Check cantSplit
        trPr = tbl.rows[0]._tr.get_or_add_trPr()
        has_cantsplit = any(child.tag.endswith("cantSplit") for child in trPr)
        self.assertTrue(has_cantsplit)

    def test_code_block(self):
        sample_code = "def add(a, b):\n    return a + b"
        tbl = self.builder.code_block("math_utils.py line 1-2", sample_code)
        self.assertEqual(len(tbl.rows), 2)
        # Check cantSplit on rows
        for row in tbl.rows:
            trPr = row._tr.get_or_add_trPr()
            has_cantsplit = any(child.tag.endswith("cantSplit") for child in trPr)
            self.assertTrue(has_cantsplit)

    def test_data_table(self):
        headers = ["Col A", "Col B"]
        rows = [["Val 1", "Val 2"], ["Val 3", "Val 4"]]
        tbl = self.builder.data_table(headers, rows, [2.0, 2.0])
        self.assertEqual(len(tbl.rows), 3)
        # Verify tblHeader on row 0
        r0_pr = tbl.rows[0]._tr.get_or_add_trPr()
        has_tblheader = any(child.tag.endswith("tblHeader") for child in r0_pr)
        self.assertTrue(has_tblheader)

    def test_save_and_reopen(self):
        with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tf:
            temp_path = tf.name

        try:
            self.builder.add_title_page("TEST TITLE", "Subtitle")
            self.builder.h1("CH1")
            self.builder.para("Body paragraph")
            self.builder.save(temp_path)

            self.assertTrue(os.path.exists(temp_path))
            doc = docx.Document(temp_path)
            self.assertTrue(len(doc.paragraphs) > 0)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == "__main__":
    unittest.main()
