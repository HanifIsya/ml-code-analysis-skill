# -*- coding: utf-8 -*-
"""
ML DOCX Builder
================
High-quality Word (.docx) document generator engineered for Machine Learning
code analysis reports, technical whitepapers, and academic audits.

Matches publication-grade formatting standards:
- A4 Paper with standard 1.0 inch (25.4 mm) margins.
- Times New Roman typography with 1.15 line spacing and justified alignment.
- Table of Contents with right-aligned page numbers and dotted tab leaders.
- High-contrast dark syntax-highlighted code blocks with line-number headers.
- Visual callout boxes with solid accent borders.
- Bordered data tables with non-splitting rows and repeating headers.
- Centered figures and captions.
- Dynamic Word page number footers.
"""

import os
import re
from typing import List, Tuple, Optional, Any

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from pygments import lex
from pygments.lexers import PythonLexer, guess_lexer
from pygments.token import Comment, Keyword, Literal, Name, Operator, Text

# Typography defaults
FONT_FAMILY = "Times New Roman"
MONO_FAMILY = "Courier New"

# Syntax highlighting dark palette (VS Code / GitHub Dark style)
C_PLAIN = "C9D1D9"
C_KEYWORD = "FF7B72"
C_STRING = "A5D6FF"
C_NUMBER = "79C0FF"
C_BUILTIN = "FFA657"
C_FUNC = "D2A8FF"
C_COMMENT = "8B949E"


class MLReportDocx:
    """Document builder orchestrator."""

    def __init__(self):
        self.doc = docx.Document()
        self._configure_document()

    def _configure_document(self):
        """Sets A4 dimensions, margins, and default paragraph styles."""
        sec = self.doc.sections[0]
        sec.page_width = Inches(8.27)
        sec.page_height = Inches(11.69)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.header_distance = Inches(0.5)
        sec.footer_distance = Inches(0.5)

        # Base Normal style
        normal = self.doc.styles["Normal"]
        normal.font.name = FONT_FAMILY
        normal.font.size = Pt(12)
        normal.paragraph_format.space_after = Pt(6)
        normal.paragraph_format.line_spacing = 1.15
        normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT_FAMILY)

        # Base Headings
        for name, size, before, after in [
            ("Heading 1", 14, 16, 6),
            ("Heading 2", 13, 16, 6),
            ("Heading 3", 13, 14, 4),
        ]:
            st = self.doc.styles[name]
            st.font.name = FONT_FAMILY
            st.font.size = Pt(size)
            st.font.bold = True
            st.font.color.rgb = RGBColor(0, 0, 0)
            st.paragraph_format.space_before = Pt(before)
            st.paragraph_format.space_after = Pt(after)
            st.paragraph_format.line_spacing = 1.15
            st.paragraph_format.keep_with_next = True

        # Footer with dynamic page numbering
        footer = sec.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.paragraph_format.space_before = Pt(0)
        fp.paragraph_format.space_after = Pt(0)
        r = fp.add_run("Halaman ")
        r.font.name = FONT_FAMILY
        r.font.size = Pt(9)

        fld_begin = OxmlElement("w:fldChar")
        fld_begin.set(qn("w:fldCharType"), "begin")
        instr = OxmlElement("w:instrText")
        instr.set(qn("xml:space"), "preserve")
        instr.text = " PAGE "
        fld_sep = OxmlElement("w:fldChar")
        fld_sep.set(qn("w:fldCharType"), "separate")
        t = OxmlElement("w:t")
        t.text = "1"
        fld_end = OxmlElement("w:fldChar")
        fld_end.set(qn("w:fldCharType"), "end")

        for el in (fld_begin, instr, fld_sep, t, fld_end):
            run = fp.add_run()
            run.font.name = FONT_FAMILY
            run.font.size = Pt(9)
            run._r.append(el)

    # ───────────────────────── Structure & Text ─────────────────────────

    def add_title_page(self, title: str, subtitle: str, metadata_note: str = ""):
        """Adds a professional cover title and subtitle."""
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(26)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(title)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(15)
        r.font.bold = True

        q = self.doc.add_paragraph()
        q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        q.paragraph_format.space_before = Pt(0)
        q.paragraph_format.space_after = Pt(14)
        r = q.add_run(subtitle)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(11)
        r.font.italic = True

        if metadata_note:
            n = self.doc.add_paragraph()
            n.alignment = WD_ALIGN_PARAGRAPH.CENTER
            n.paragraph_format.space_before = Pt(0)
            n.paragraph_format.space_after = Pt(20)
            r = n.add_run(metadata_note)
            r.font.name = FONT_FAMILY
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    def add_toc_header(self, title: str = "DAFTAR ISI"):
        """Adds the Table of Contents header."""
        t = self.doc.add_paragraph()
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        t.paragraph_format.space_before = Pt(4)
        t.paragraph_format.space_after = Pt(16)
        r = t.add_run(title)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(14)
        r.font.bold = True

    def add_toc_entry(self, level: int, label: str, page_num: int, first: bool = False):
        """Adds a line entry in the Table of Contents with dotted leader."""
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0 if not first else 2)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.1
        if level >= 1:
            p.paragraph_format.left_indent = Inches(0.30 * level)
        p.paragraph_format.tab_stops.add_tab_stop(
            Inches(6.20), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS
        )
        r = p.add_run(f"{label}\t{page_num}")
        r.font.name = FONT_FAMILY
        r.font.size = Pt(11.5)
        r.font.bold = (level == 0)
        return p

    def h1(self, text: str, page_break: bool = True):
        """Main Chapter heading (Heading 1)."""
        p = self.doc.add_paragraph(style="Heading 1")
        p.paragraph_format.page_break_before = page_break
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(14)
        r.font.bold = True
        return p

    def h2(self, text: str):
        """Sub-section heading (Heading 2)."""
        p = self.doc.add_paragraph(style="Heading 2")
        p.paragraph_format.page_break_before = False
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(13)
        r.font.bold = True
        return p

    def h3(self, text: str):
        """Sub-subsection heading (Heading 3)."""
        p = self.doc.add_paragraph(style="Heading 3")
        p.paragraph_format.page_break_before = False
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(13)
        r.font.bold = True
        return p

    def para(
        self,
        text: str = "",
        bold: bool = False,
        italic: bool = False,
        align: Any = WD_ALIGN_PARAGRAPH.JUSTIFY,
        before: float = 0,
        after: float = 6,
        size: float = 12,
        color: Optional[Tuple[int, int, int]] = None,
        keep_with_next: bool = False,
    ):
        """Adds a styled text paragraph."""
        p = self.doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = 1.15
        if keep_with_next:
            p.paragraph_format.keep_with_next = True
        if text:
            r = p.add_run(text)
            r.font.name = FONT_FAMILY
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.italic = italic
            if color:
                r.font.color.rgb = RGBColor(*color)
        return p

    def bullet(self, text: str, level: int = 0):
        """Adds a bullet list item."""
        p = self.doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.30 + 0.25 * level)
        p.paragraph_format.first_line_indent = Inches(-0.18)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.12
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(text)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(11.5)
        return p

    def numbered(self, number: int, text: str, bold_lead: Optional[str] = None):
        """Adds a numbered list paragraph."""
        p = self.doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.32)
        p.paragraph_format.first_line_indent = Inches(-0.32)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r0 = p.add_run(f"{number}. ")
        r0.font.name = FONT_FAMILY
        r0.font.size = Pt(12)
        r0.font.bold = True
        if bold_lead:
            rb = p.add_run(bold_lead)
            rb.font.name = FONT_FAMILY
            rb.font.size = Pt(12)
            rb.font.bold = True
        r = p.add_run(text)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(12)
        return p

    # ───────────────────────── Visual Components ─────────────────────────

    def callout(
        self,
        title: str,
        lines: List[str],
        fill: str = "F2F4F7",
        border_color: str = "7BA4D0",
    ):
        """
        Creates an elegant callout box with a thick left accent border.
        """
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        _shade_cell(cell, fill)
        _cell_margins(cell, top=100, bottom=100, left=140, right=140)

        # Thick left border, thin top/bottom/right
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'</w:tcBorders>'
        )
        cell._tc.get_or_add_tcPr().append(tcBorders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title)
        r.font.name = FONT_FAMILY
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x15, 0x43, 0x60)

        for line in lines:
            q = cell.add_paragraph()
            q.paragraph_format.space_before = Pt(2)
            q.paragraph_format.space_after = Pt(3)
            q.paragraph_format.line_spacing = 1.12
            q.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            rr = q.add_run(line)
            rr.font.name = FONT_FAMILY
            rr.font.size = Pt(10.5)
            rr.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)

        tbl.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        self._add_spacing(6)
        return tbl

    def code_block(self, header: str, code: str):
        """
        Creates a dark-mode syntax highlighted codeblock.
        Header shows file name + line range with blue underline.
        Body contains Pygments lexed tokens with Courier New monospace font.
        """
        tbl = self.doc.add_table(rows=2, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        _set_table_borders(tbl, color="000000", sz="8")

        # Header Row
        hdr = tbl.cell(0, 0)
        _shade_cell(hdr, "FFFFFF")
        _cell_margins(hdr, top=70, bottom=70, left=100, right=100)
        p = hdr.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.keep_with_next = True

        sep_pattern = re.search(r"(\s+[·\-]\s+)", header)
        if sep_pattern:
            sep = sep_pattern.group(1)
            parts = header.split(sep, 1)
            fname, rest = parts[0], sep + parts[1]
        else:
            fname = header
            rest = ""

        r0 = p.add_run(fname)
        r0.font.name = FONT_FAMILY
        r0.font.size = Pt(13)
        r0.font.color.rgb = RGBColor(0x11, 0x55, 0xCC)
        r0.underline = True

        if rest:
            r1 = p.add_run(rest)
            r1.font.name = FONT_FAMILY
            r1.font.size = Pt(13)
            r1.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            r1.underline = False

        # Body Row
        body = tbl.cell(1, 0)
        _shade_cell(body, "121314")
        _cell_margins(body, top=110, bottom=110, left=110, right=110)

        first = body.paragraphs[0]
        first._p.getparent().remove(first._p)

        tokens_lines = _highlight_python(code)
        for tokens in tokens_lines:
            q = body.add_paragraph()
            q.alignment = WD_ALIGN_PARAGRAPH.LEFT
            q.paragraph_format.space_before = Pt(0)
            q.paragraph_format.space_after = Pt(0)
            q.paragraph_format.line_spacing = Pt(10.3)

            pPr = q._p.get_or_add_pPr()
            pBdr = parse_xml(
                f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="0" w:color="21262D"/></w:pBdr>'
            )
            pPr.append(pBdr)

            if not tokens:
                r = q.add_run(" ")
                r.font.name = MONO_FAMILY
                r.font.size = Pt(9.0)
                continue

            for text, color in tokens:
                r = q.add_run(text)
                r.font.name = MONO_FAMILY
                r.font.size = Pt(9.0)
                r.font.color.rgb = RGBColor.from_string(color)

        for row in tbl.rows:
            row.cells[0].width = Inches(6.268)

        _prevent_table_split(tbl)
        self._add_spacing(6)
        return tbl

    def table_caption(self, number: int, text: str):
        """Adds a standardized table caption."""
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r0 = p.add_run(f"Tabel {number}.")
        r0.font.name = FONT_FAMILY
        r0.font.size = Pt(10)
        r0.font.bold = True
        r1 = p.add_run(" " + text)
        r1.font.name = FONT_FAMILY
        r1.font.size = Pt(10)
        return p

    def data_table(
        self,
        headers: List[str],
        rows: List[List[Any]],
        col_widths: List[float],
        col_aligns: Optional[List[Any]] = None,
        header_shade: str = "D9E2F3",
        font_size: float = 8.8,
        header_font_size: float = 9.0,
    ):
        """
        Creates a publication-grade data table with cell padding,
        subtle borders, cantSplit rows, and repeating header.
        """
        tbl = self.doc.add_table(rows=1 + len(rows), cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        _set_table_borders(tbl, color="8A8A8A", sz="4")

        aligns = col_aligns or [WD_ALIGN_PARAGRAPH.LEFT] * len(headers)

        # Header Row
        for j, text in enumerate(headers):
            cell = tbl.cell(0, j)
            _shade_cell(cell, header_shade)
            _cell_margins(cell, top=55, bottom=55, left=80, right=80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            r = p.add_run(str(text))
            r.font.name = FONT_FAMILY
            r.font.size = Pt(header_font_size)
            r.font.bold = True

        # Data Rows
        for i, row in enumerate(rows, 1):
            for j, val in enumerate(row):
                cell = tbl.cell(i, j)
                _cell_margins(cell, top=45, bottom=45, left=80, right=80)
                p = cell.paragraphs[0]
                p.alignment = aligns[j]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                r = p.add_run(str(val))
                r.font.name = FONT_FAMILY
                r.font.size = Pt(font_size)

        # Set Column Widths
        for row in tbl.rows:
            for j, w in enumerate(col_widths):
                row.cells[j].width = Inches(w)

        _prevent_table_split(tbl)
        self._add_spacing(6)
        return tbl

    def figure(
        self,
        img_path: str,
        width_inches: float,
        number: int,
        caption: str,
        is_diagram: bool = False,
    ):
        """Adds a centered figure or diagram with caption."""
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        p.add_run().add_picture(img_path, width=Inches(width_inches))

        cap = self.doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.space_before = Pt(2)
        cap.paragraph_format.space_after = Pt(10)

        label_prefix = f"Diagram Alur {number}." if is_diagram else f"Gambar {number}."
        r0 = cap.add_run(label_prefix)
        r0.font.name = FONT_FAMILY
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r1 = cap.add_run(" " + caption)
        r1.font.name = FONT_FAMILY
        r1.font.size = Pt(9.5)
        r1.font.italic = True
        r1.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        return cap

    def _add_spacing(self, points: float = 6):
        sp = self.doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(0)
        sp.paragraph_format.line_spacing = Pt(points)

    def save(self, filepath: str):
        """Saves the completed docx file."""
        self.doc.save(filepath)
        print(f"Report saved successfully: {filepath}")


# ───────────────────────── Internal XML Helpers ─────────────────────────

def _shade_cell(cell, color_hex: str):
    cell._tc.get_or_add_tcPr().append(
        parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    )

def _cell_margins(cell, top: int = 45, bottom: int = 45, left: int = 80, right: int = 80):
    cell._tc.get_or_add_tcPr().append(
        parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{top}" w:type="dxa"/>'
            f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
            f'<w:left w:w="{left}" w:type="dxa"/>'
            f'<w:right w:w="{right}" w:type="dxa"/></w:tcMar>'
        )
    )

def _set_table_borders(table, color: str = "8A8A8A", sz: str = "4"):
    table._tbl.tblPr.append(
        parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'</w:tblBorders>'
        )
    )

def _prevent_table_split(table):
    """Enforces cantSplit on all rows and tblHeader on row 0."""
    for i, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        if i == 0:
            trPr.append(OxmlElement("w:tblHeader"))
        if i < len(table.rows) - 1:
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.keep_with_next = True

def _token_color(ttype):
    if ttype in Comment:
        return C_COMMENT
    if ttype in Keyword or ttype in Operator:
        return C_KEYWORD
    if ttype in Name.Function:
        return C_FUNC
    if ttype in Name.Builtin:
        return C_BUILTIN
    if ttype in Literal.String:
        return C_STRING
    if ttype in Literal.Number:
        return C_NUMBER
    return C_PLAIN

def _highlight_python(code: str):
    lines = [[]]
    for ttype, value in lex(code, PythonLexer()):
        color = _token_color(ttype)
        parts = value.split("\n")
        for k, part in enumerate(parts):
            if k > 0:
                lines.append([])
            if part:
                lines[-1].append((part, color))
    merged = []
    for line in lines:
        out = []
        for text, color in line:
            if out and out[-1][1] == color:
                out[-1] = (out[-1][0] + text, color)
            else:
                out.append((text, color))
        merged.append(out)
    while merged and not "".join(t for t, _ in merged[-1]):
        merged.pop()
    return merged
