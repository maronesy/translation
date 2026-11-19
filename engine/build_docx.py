# -*- coding: utf-8 -*-
"""
Build the Word edition of a book translation (linear: each Arabic sentence
with its English beneath).

Design language (an Islamic scholarly feel):
  • Arabic set in Amiri (classical naskh), rendered right-to-left.
  • English set in EB Garamond (classical serif) directly beneath each line.
  • Deep-green / gold palette, ornamental basmala, and gilt dividers.

Usage:  python engine/build_docx.py books/<slug> [pdf pages…] [--nocover]
Output: books/<slug>/build/<basename>_Translation.docx
"""
import os
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Inches

# ----------------------------------------------------------------------------
# Palette & typography
# ----------------------------------------------------------------------------
GREEN   = RGBColor(0x0F, 0x50, 0x32)   # deep emerald  – matn (base text)
MAROON  = RGBColor(0x6E, 0x14, 0x23)   # dark maroon   – ḥāshiya (footnotes)
GOLD    = RGBColor(0x99, 0x77, 0x0A)   # muted gilt    – ornaments / numbers
INK     = RGBColor(0x22, 0x22, 0x22)   # near-black    – English body
MUTED   = RGBColor(0x6B, 0x6B, 0x6B)   # grey          – labels / captions
CREAM   = "FBF7EE"                     # parchment band fill
GREENHX = "0F5032"
GOLDHX  = "99770A"

AR_FONT = "Amiri"
EN_FONT = "EB Garamond"

from book import parse_args

# ----------------------------------------------------------------------------
# Low-level OOXML helpers
#
# NB: OOXML defines a *strict* child order for <w:pPr> and <w:rPr>. If elements
# are appended out of order, lenient viewers (Quick Look) tolerate it but strict
# ones (Word / Pages) silently drop the offending element — which is exactly how
# a mis-ordered <w:bidi> gets ignored and Arabic loses its right-to-left base
# direction. So every property below is *inserted at its schema position*.
# ----------------------------------------------------------------------------
_PPR_ORDER = [qn("w:" + t) for t in (
    "pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
    "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs",
    "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct",
    "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
    "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents",
    "suppressOverlap", "jc", "textDirection", "textAlignment",
    "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr",
    "pPrChange")]

_RPR_ORDER = [qn("w:" + t) for t in (
    "rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike",
    "dstrike", "outline", "shadow", "emboss", "imprint", "noProof",
    "snapToGrid", "vanish", "webHidden", "color", "spacing", "w", "kern",
    "position", "sz", "szCs", "highlight", "u", "effect", "bdr", "shd",
    "fitText", "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout",
    "specVanish", "oMath")]

_PBDR_ORDER = [qn("w:" + t) for t in
               ("top", "left", "bottom", "right", "between", "bar")]


def _insert_ordered(parent, el, order):
    """Insert *el* into *parent* at its schema-defined position."""
    ti = order.index(el.tag)
    for child in parent:
        if child.tag in order and order.index(child.tag) > ti:
            child.addprevious(el)
            return el
    parent.append(el)
    return el


def _child(parent, tag, order, **attrs):
    el = OxmlElement(tag)
    for k, v in attrs.items():
        el.set(qn(k), str(v))
    return _insert_ordered(parent, el, order)


def shade(paragraph, fill):
    """Give a paragraph a solid background fill."""
    pPr = paragraph._p.get_or_add_pPr()
    _child(pPr, "w:shd", _PPR_ORDER,
           **{"w:val": "clear", "w:color": "auto", "w:fill": fill})


def borders(paragraph, edges, color=GOLDHX, size=8, space=6):
    """Add cell-style borders to a paragraph. edges = e.g. ('bottom','top')."""
    pPr = paragraph._p.get_or_add_pPr()
    pbdr = pPr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = _child(pPr, "w:pBdr", _PPR_ORDER)
    for edge in edges:
        _child(pbdr, f"w:{edge}", _PBDR_ORDER,
               **{"w:val": "single", "w:sz": size, "w:space": space,
                  "w:color": color})


def rtl(paragraph):
    """Mark a paragraph's base direction as right-to-left."""
    pPr = paragraph._p.get_or_add_pPr()
    if pPr.find(qn("w:bidi")) is None:
        _child(pPr, "w:bidi", _PPR_ORDER)


def _run(paragraph, text, *, font, size, color, bold=False, italic=False,
         arabic=False, letter_spacing=None):
    run = paragraph.add_run(text)
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    # bind the font for ascii / hAnsi / complex-script slots
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = _child(rPr, "w:rFonts", _RPR_ORDER)
    for slot in ("w:ascii", "w:hAnsi", "w:cs"):
        rFonts.set(qn(slot), font)
    if arabic:
        _child(rPr, "w:rtl", _RPR_ORDER)                       # run reads RTL
        _child(rPr, "w:szCs", _RPR_ORDER, **{"w:val": str(int(size * 2))})
        if bold:
            _child(rPr, "w:bCs", _RPR_ORDER)                   # complex bold
    if letter_spacing is not None:
        _child(rPr, "w:spacing", _RPR_ORDER,
               **{"w:val": str(letter_spacing)})
    return run


def spacing(paragraph, *, before=None, after=None, line=None):
    pf = paragraph.paragraph_format
    if before is not None:
        pf.space_before = Pt(before)
    if after is not None:
        pf.space_after = Pt(after)
    if line is not None:
        pf.line_spacing = line


# ----------------------------------------------------------------------------
# Content builders
# ----------------------------------------------------------------------------
# A footnote-reference marker in the Arabic text: [[١]] → superscript ¹ on the
# preceding word. Written directly after the word the ḥāshiya comments on.
_MARKER_RE = re.compile(r"\[\[([٠-٩]+)\]\]")


def _emit_arabic(p, text, *, size, color, bold):
    """Add Arabic runs to paragraph *p*, turning [[N]] into superscript refs."""
    pos = 0
    for m in _MARKER_RE.finditer(text):
        if m.start() > pos:
            _run(p, text[pos:m.start()], font=AR_FONT, size=size, color=color,
                 bold=bold, arabic=True)
        r = _run(p, m.group(1), font=AR_FONT, size=size, color=GOLD, bold=True,
                 arabic=True)
        _child(r._r.get_or_add_rPr(), "w:vertAlign", _RPR_ORDER,
               **{"w:val": "superscript"})
        pos = m.end()
    if pos < len(text) or pos == 0:
        _run(p, text[pos:], font=AR_FONT, size=size, color=color, bold=bold,
             arabic=True)


def add_arabic(doc, text, *, size=15, color=GREEN, bold=False, after=2):
    p = doc.add_paragraph()
    rtl(p)
    # No explicit jc: an RTL (bidi) paragraph aligns flush-right to its start
    # edge by default. This renders right-aligned in every viewer, whereas an
    # explicit jc="right" is read as the "end" side (i.e. left) in some RTL
    # implementations.
    spacing(p, before=6, after=after, line=1.5)
    _emit_arabic(p, text, size=size, color=color, bold=bold)
    return p


def add_english(doc, text, *, size=11.5, color=INK, italic=False, indent=0.18,
                after=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.left_indent = Inches(indent)
    spacing(p, before=0, after=after, line=1.28)
    _run(p, text, font=EN_FONT, size=size, color=color, italic=italic)
    return p


def add_centre_ornament(doc, text, *, size=16, color=GOLD, before=10, after=10):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(p, before=before, after=after)
    _run(p, text, font=AR_FONT, size=size, color=color, arabic=True)
    return p


def add_centre_arabic(doc, text, *, size=15, color=GREEN, bold=False, after=2):
    """Centred Arabic line — used for poetry hemistichs and Qurʾānic verses."""
    p = doc.add_paragraph()
    rtl(p)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(p, before=6, after=after, line=1.4)
    _emit_arabic(p, text, size=size, color=color, bold=bold)
    return p


def add_centre_english(doc, text, *, size=11, color=MUTED, after=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(p, before=0, after=after, line=1.25)
    _run(p, text, font=EN_FONT, size=size, color=color, italic=True)
    return p


def section_header(doc, ar, en):
    # English eyebrow above
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(cap, before=8, after=1)
    _run(cap, en.upper(), font=EN_FONT, size=10.5, color=GOLD, letter_spacing=44)
    # Arabic title in emerald, framed by gold rules (legible in every viewer)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rtl(p)
    borders(p, ("top", "bottom"), color=GOLDHX, size=6, space=6)
    spacing(p, before=2, after=14, line=1.0)
    _run(p, ar, font=AR_FONT, size=20, color=GREEN, bold=True, arabic=True)


def basmala(doc):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rtl(p)
    spacing(p, before=10, after=2, line=1.0)
    _run(p, "بسم الله الرحمن الرحيم", font=AR_FONT, size=22, color=GREEN,
         arabic=True)
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(cap, before=0, after=12)
    _run(cap, "In the name of Allah, the All-Merciful, the Most Compassionate",
         font=EN_FONT, size=11, color=MUTED, italic=True)


def divider(doc):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(p, before=8, after=8)
    _run(p, "۞     ❁     ۞", font=AR_FONT, size=13, color=GOLD)


_AR_DIGITS = set("٠١٢٣٤٥٦٧٨٩")


def note_header(doc, num):
    p = doc.add_paragraph()
    rtl(p)  # flush-right by RTL default (see add_arabic)
    borders(p, ("top",), color="E4D9BE", size=6, space=2)
    spacing(p, before=14, after=4, line=1.0)
    is_numbered = bool(num) and all(ch in _AR_DIGITS for ch in str(num))
    if is_numbered:
        # Wrap the ornate parentheses + number in a Left-to-Right embedding
        # (U+202A … U+202C). These ornate parens are NOT bidi-mirrored, so in an
        # RTL run their order flips (rendering ")١(" ); forcing LTR here pins
        # them to the correct "﴾ ١ ﴿" in every viewer.
        label = "‪" + f"﴾ {num} ﴿" + "‬"   # LRE … PDF
        _run(p, label, font=AR_FONT, size=15, color=GOLD, bold=True, arabic=True)
        _run(p, "   حاشية", font=AR_FONT, size=12, color=MAROON, arabic=True)
    else:
        # A footnote whose text continues from the previous page.
        _run(p, "‪﴾ ⋯ ﴿‬", font=AR_FONT, size=15, color=GOLD, bold=True,
             arabic=True)
        _run(p, "   تتمة الحاشية من الصفحة السابقة", font=AR_FONT, size=11,
             color=MAROON, arabic=True)


# ----------------------------------------------------------------------------
# Cover / running header / footer
# ----------------------------------------------------------------------------
def build_cover(doc, book):
    for _ in range(3):
        doc.add_paragraph()

    def band(text, size, color, arabic=False, bold=False, before=0, after=0,
             ls=None):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if arabic:
            rtl(p)
        spacing(p, before=before, after=after, line=1.0)
        _run(p, text, font=(AR_FONT if arabic else EN_FONT), size=size,
             color=color, bold=bold, arabic=arabic, letter_spacing=ls)
        return p

    band("۞", 26, GOLD, before=0, after=6)
    band("A L K A L A M", 13, GOLD, ls=80, after=2)
    band("Open Translations of Classical Islamic Texts", 11, MUTED, after=40)

    band(book.title("ar"), 40, GREEN, arabic=True, bold=True, after=6)
    band(book.title("en"), 20, INK, after=2)
    if book.title("subtitle_en"):
        band(book.title("subtitle_en"), 12.5, MUTED, after=2)
    if book.title("field_en"):
        band(book.title("field_en"), 12.5, MUTED, after=34)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(p, before=0, after=6)
    _run(p, "❁     ❁     ❁", font=AR_FONT, size=14, color=GOLD)

    band("Arabic text with English translation", 12, INK, after=2)
    band("Licensed CC BY-SA 4.0", 11, MUTED, after=30)


def set_page(section):
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.15)
    section.right_margin = Inches(1.15)


def add_running_footer(section, book):
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _run(p, f"{book.title('en')}  ·  Alkalam", font=EN_FONT, size=9, color=MUTED)


# ----------------------------------------------------------------------------
# Page rendering
# ----------------------------------------------------------------------------
def render_block(doc, b):
    t = b["type"]
    if t == "section":
        section_header(doc, b["ar"], b["en"])
    elif t == "basmala":
        basmala(doc)
    elif t == "khutba":            # author's opening address — emphasised
        add_arabic(doc, b["ar"], size=16, color=GREEN, bold=True, after=2)
        add_english(doc, b["en"], size=12.5, color=INK, after=10)
    elif t == "matn":              # main commentary text (above the rule)
        add_arabic(doc, b["ar"], size=15, color=GREEN, bold=False, after=2)
        add_english(doc, b["en"], size=12, color=INK, after=10)
    elif t == "verse":            # a line of poetry (hemistichs, centred)
        add_centre_arabic(doc, b["ar"], size=15, color=GREEN, after=2)
        add_centre_english(doc, b["en"], size=11, color=MUTED, after=10)
    elif t == "quran":            # a Qurʾānic quotation, set apart & centred
        add_centre_arabic(doc, b["ar"], size=16, color=GREEN, bold=True, after=2)
        add_centre_english(doc, b["en"], size=11, color=MUTED, after=10)
    elif t == "pair":              # a sentence inside a footnote (ḥāshiya)
        add_arabic(doc, b["ar"], size=13, color=MAROON, after=2)
        add_english(doc, b["en"], size=11.5, color=INK, after=11)
    elif t == "note":
        note_header(doc, b["num"])
    elif t == "rule":
        divider(doc)


def page_heading(doc, page_no, printed, break_before=False):
    p = doc.add_paragraph()
    if break_before:
        p.paragraph_format.page_break_before = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(p, before=0, after=2)
    _run(p, f"— Page {printed} —", font=EN_FONT, size=11, color=GOLD,
         letter_spacing=30)
    borders(p, ("bottom",), color="E4D9BE", size=6, space=4)


def _no_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        borders.append(el)
    tblPr.append(borders)


def build_toc(doc, entries):
    """Render a bilingual table of contents from (en, ar, printed) entries."""
    # Heading (same style as a section header, on its own page)
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.page_break_before = True
    spacing(cap, before=8, after=1)
    _run(cap, "TABLE OF CONTENTS", font=EN_FONT, size=10.5, color=GOLD,
         letter_spacing=44)
    h = doc.add_paragraph()
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rtl(h)
    borders(h, ("top", "bottom"), color=GOLDHX, size=6, space=6)
    spacing(h, before=2, after=16, line=1.0)
    _run(h, "الفهرس", font=AR_FONT, size=20, color=GREEN, bold=True,
         arabic=True)

    # A borderless 2-column table: titles on the left, page number on the right.
    # Tables render reliably in every viewer (unlike custom tab leaders).
    table = doc.add_table(rows=len(entries), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    _no_table_borders(table)
    for row, (en, ar, printed) in zip(table.rows, entries):
        title_cell, page_cell = row.cells
        title_cell.width = Inches(5.5)
        page_cell.width = Inches(0.7)
        page_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

        a = title_cell.paragraphs[0]
        rtl(a)
        spacing(a, before=8, after=0, line=1.1)
        _run(a, ar, font=AR_FONT, size=14, color=GREEN, bold=True, arabic=True)
        e = title_cell.add_paragraph()
        spacing(e, before=0, after=8, line=1.0)
        e.paragraph_format.left_indent = Inches(0.12)
        _run(e, en, font=EN_FONT, size=11, color=MUTED, italic=True)

        pg = page_cell.paragraphs[0]
        pg.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        _run(pg, printed, font=EN_FONT, size=12, color=GOLD, bold=True)


def collect_toc_entries(pages):
    entries = []
    for num, mod in pages:
        printed = getattr(mod, "PRINTED_PAGE", str(num))
        for b in getattr(mod, "BLOCKS", []):
            if b["type"] == "section":
                entries.append((b["en"], b["ar"], printed))
    return entries


def main():
    book, which, flags = parse_args(sys.argv[1:])
    nocover = "--nocover" in flags
    doc = Document()

    # base styles
    normal = doc.styles["Normal"]
    normal.font.name = EN_FONT
    normal.font.size = Pt(11.5)

    set_page(doc.sections[0])
    add_running_footer(doc.sections[0], book)

    if not nocover:
        build_cover(doc, book)

    pages = [(n, m) for (n, m) in book.load_pages(which) if getattr(m, "BLOCKS", [])]

    if not nocover:
        toc = collect_toc_entries(pages)
        if toc:
            build_toc(doc, toc)

    for i, (num, mod) in enumerate(pages):
        printed = getattr(mod, "PRINTED_PAGE", str(num))
        break_before = (i > 0) or (not nocover)
        page_heading(doc, num, printed, break_before=break_before)
        for b in mod.BLOCKS:
            render_block(doc, b)

    os.makedirs(book.build_dir, exist_ok=True)
    out = os.path.join(book.build_dir, f"{book.basename}_Translation.docx")
    doc.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    main()
