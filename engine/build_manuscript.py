# -*- coding: utf-8 -*-
"""Manuscript-style PDF edition of a book translation.

Each source page becomes one A3 sheet laid out like a glossed manuscript: the
matn (Arabic + English) sits in a ruled central frame and the ḥawāshī
(Arabic + English) are set around it — down the side margins, across the top
and bottom bands, and diagonally in the four corners.

Reads the same `books/<slug>/pages/page_NNN.py` files as build_docx.py. The layout is done
in the browser (fonts must be measured), then printed by headless Chrome.

Usage:
    python engine/build_manuscript.py books/<slug> [pdf pages…] [--nocover] [--html-only]

Output: books/<slug>/build/<basename>_Manuscript.pdf (and the .html it is printed from).
Needs Google Chrome or Chromium; set CHROME=/path/to/binary if it is not found.
"""
import html
import os
import re
import shutil
import subprocess
import sys

from book import parse_args
from build_docx import collect_toc_entries

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")


def find_chrome():
    for c in (os.environ.get("CHROME"),
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome"), shutil.which("google-chrome-stable"),
              shutil.which("chromium"), shutil.which("chromium-browser")):
        if c and os.path.exists(c):
            return c
    sys.exit("Chrome/Chromium not found — set CHROME=/path/to/chrome")

_MARKER_RE = re.compile(r"\[\[([٠-٩]+)\]\]")
_LEMMA_RE = re.compile(r"«([^»]*)»")


def ar(text):
    """Escape Arabic text; footnote markers → red superscripts, «lemmas» → red."""
    t = html.escape(text)
    t = _LEMMA_RE.sub(r'<span class="rub">«\1»</span>', t)
    return _MARKER_RE.sub(r'<sup class="mk">\1</sup>', t)


def en(text):
    return html.escape(_MARKER_RE.sub("", text))


# ----------------------------------------------------------------------------
# Page content → HTML
# ----------------------------------------------------------------------------
def cartouche(b, anchor=None):
    aid = f' id="{anchor}"' if anchor else ""
    return (f'<div class="cartouche"{aid}><div class="c-ar" dir="rtl">'
            f'{ar(b["ar"])}</div><div class="c-en">{en(b["en"])}</div></div>')


def frame_html(blocks, sec_ids):
    out = []
    for b in blocks:
        t = b["type"]
        if t == "section":
            out.append(cartouche(b, sec_ids.pop(0) if sec_ids else None))
        elif t == "basmala":
            out.append('<div class="basmala" dir="rtl">بسم الله الرحمن '
                       'الرحيم</div>')
        elif t in ("matn", "khutba"):
            out.append(f'<div class="mp {t}"><div class="a" dir="rtl">'
                       f'{ar(b["ar"])}</div><div class="e">{en(b["en"])}</div></div>')
        elif t in ("verse", "quran"):
            out.append(f'<div class="mp {t}"><div class="a" dir="rtl">'
                       f'{ar(b["ar"])}</div><div class="e">{en(b["en"])}</div></div>')
    return "".join(out)


def notes_html(blocks):
    """Hidden pool: one .note per ḥāshiya, its sentences as .np pairs."""
    notes, cur = [], None
    for b in blocks:
        if b["type"] == "note":
            cur = {"num": b["num"], "pairs": []}
            notes.append(cur)
        elif b["type"] == "pair" and cur is not None:
            cur["pairs"].append(b)
    out = []
    for n in notes:
        pairs = "".join(
            f'<div class="np"><div class="a" dir="rtl">{ar(p["ar"])}</div>'
            f'<div class="e">{en(p["en"])}</div></div>' for p in n["pairs"])
        out.append(f'<div class="note" data-num="{n["num"]}">{pairs}</div>')
    return "".join(out)


def sheet_html(num, mod, sec_ids):
    printed = getattr(mod, "PRINTED_PAGE", str(num))
    return (
        f'<section class="sheet" data-pdf="{num}" data-printed="{printed}">'
        f'<div class="border"></div>'
        f'<div class="frame"><div class="frame-in">'
        f'{frame_html(mod.BLOCKS, sec_ids)}</div></div>'
        f'<div class="pool">{notes_html(mod.BLOCKS)}</div>'
        f'<div class="folio">{printed}</div>'
        f'</section>')


HEADPIECE = """
<svg class="headpiece" viewBox="0 0 400 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="arab" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="5.2" fill="none" stroke="#c9a54a" stroke-width="1.1"/>
      <circle cx="0" cy="0" r="5.2" fill="none" stroke="#c9a54a" stroke-width="1.1"/>
      <circle cx="20" cy="20" r="5.2" fill="none" stroke="#c9a54a" stroke-width="1.1"/>
      <circle cx="10" cy="10" r="1.5" fill="#e3c76f"/>
    </pattern>
  </defs>
  <path d="M10 148 V92 H120 C150 92 165 60 200 8 C235 60 250 92 280 92 H390 V148 Z"
        fill="#1f3a73" stroke="#b8902f" stroke-width="4"/>
  <path d="M22 140 V100 H124 C156 100 172 72 200 30 C228 72 244 100 276 100 H378 V140 Z"
        fill="url(#arab)" stroke="#e3c76f" stroke-width="1.5"/>
  <circle cx="200" cy="96" r="20" fill="#a3261c" stroke="#e3c76f" stroke-width="2.5"/>
  <circle cx="200" cy="96" r="9" fill="#e3c76f"/>
  <path d="M200 8 V-4" stroke="#b8902f" stroke-width="3"/>
</svg>"""


def cover_html(book):
    sub = html.escape(book.title("subtitle_en"))
    field = html.escape(book.title("field_en"))
    return f"""
<section class="sheet cover">
  <div class="border"></div>
  <div class="cover-in">
    {HEADPIECE}
    <div class="cartouche big"><div class="c-ar" dir="rtl">{html.escape(book.title("ar"))}</div>
      <div class="c-en">{html.escape(book.title("en"))}</div></div>
    <p class="cv1">{sub}</p>
    <p class="cv2">{field}</p>
    <div class="orn">❁ ❁ ❁</div>
    <p class="cv1">Arabic text with English translation; the ḥawāshī set in the margins</p>
    <p class="cv3">A L K A L A M</p>
    <p class="cv2">Open Translations of Classical Islamic Texts · CC BY-SA 4.0</p>
  </div>
</section>"""


TOC_PER_SHEET = 40


def toc_html(entries):
    return "".join(toc_sheet(entries[k:k + TOC_PER_SHEET], k)
                   for k in range(0, len(entries), TOC_PER_SHEET))


def toc_sheet(entries, start):
    rows = "".join(
        f'<a class="trow" href="#sec{i}"><span class="t-ar" dir="rtl">{ar(a)}</span>'
        f'<span class="t-en">{en(e)}</span><span class="t-pg">{p}</span></a>'
        for i, (e, a, p) in enumerate(entries, start))
    return f"""
<section class="sheet toc">
  <div class="border"></div>
  <div class="toc-in">
    <div class="cartouche"><div class="c-ar" dir="rtl">الفهرس</div>
      <div class="c-en">Table of Contents</div></div>
    <div class="tlist">{rows}</div>
  </div>
</section>"""


def main():
    book, which, flags = parse_args(sys.argv[1:])
    nocover = "--nocover" in flags
    pages = [(n, m) for (n, m) in book.load_pages(which) if getattr(m, "BLOCKS", [])]
    os.makedirs(book.build_dir, exist_ok=True)
    out_html = os.path.join(book.build_dir, f"{book.basename}_Manuscript.html")
    out_pdf = os.path.join(book.build_dir, f"{book.basename}_Manuscript.pdf")

    entries = collect_toc_entries(pages)
    sec_ids = [f"sec{i}" for i in range(len(entries))]
    body = []
    if not nocover:
        body.append(cover_html(book))
        if entries:
            body.append(toc_html(entries))
    for num, mod in pages:
        body.append(sheet_html(num, mod, sec_ids))

    tpl = open(os.path.join(HERE, "manuscript", "template.html"),
               encoding="utf-8").read()
    doc = (tpl.replace("{{FONTS}}", "file://" + FONTS)
              .replace("{{BODY}}", "\n".join(body)))
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(doc)
    print("Wrote", out_html)
    if "--html-only" in flags:
        return

    subprocess.run([
        find_chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--no-sandbox",
        "--allow-file-access-from-files", "--virtual-time-budget=600000",
        "--generate-pdf-document-outline",
        f"--print-to-pdf={out_pdf}", "file://" + out_html,
    ], check=True, capture_output=True)
    print("Wrote", out_pdf)
    refresh_review_notes(book, out_html)


def sheet_map(out_html):
    """Laid-out sheets: book page → [(PDF page, footnote numbers, matn text)]."""
    dom = subprocess.run([
        find_chrome(), "--headless=new", "--disable-gpu", "--no-sandbox",
        "--allow-file-access-from-files", "--virtual-time-budget=600000",
        "--dump-dom", "file://" + out_html,
    ], check=True, capture_output=True, text=True).stdout
    m = {}
    for sec in dom.split("<section ")[1:]:
        tag = sec[:sec.index(">")]
        printed = re.search(r'data-printed="([^"]+)"', tag)
        sheet = re.search(r'data-sheet="(\d+)"', tag)
        if not (printed and sheet):
            continue
        cut = sec.find('class="pool"')
        notes = set(re.findall(r'class="nb[^"]*">([٠-٩]+)</span>', sec[:cut]))
        notes |= set(re.findall(r'class="note" data-num="([٠-٩]+)"', sec[cut:]))
        f0 = sec.find('class="frame-in"')
        frame = re.sub(r"<sup[^>]*>.*?</sup>|<[^>]+>", "", sec[f0:cut]) if f0 >= 0 else ""
        m.setdefault(printed.group(1), []).append((int(sheet.group(1)), notes, frame))
    return m


def _pdf_ref(pages):
    pages = sorted(set(pages))
    return f"PDF p. {pages[0]}" if len(pages) == 1 else f"PDF pp. {pages[0]}–{pages[-1]}"


_REF = re.compile(r"(?:PDF pp?\. [0-9–]+ \()?(?:book )?pp?\.(?P<a>[٠-٩]+)"
                  r"(?:–(?P<b>[٠-٩]+))?\)?")


def refresh_review_notes(book, out_html):
    """Write build/<basename>_Review-Notes.md: a copy of REVIEW-NOTES.md whose
    book-page references ("book p.٣٠٥") also give the PDF page of this build's
    manuscript edition. A reference to a footnote points at the sheet carrying
    it; one to the matn, at the sheet whose frame contains the quoted words.
    The committed REVIEW-NOTES.md keeps book pages only, which never change."""
    path = os.path.join(book.dir, "REVIEW-NOTES.md")
    if not os.path.exists(path):
        return
    m = sheet_map(out_html)
    s = open(path, encoding="utf-8").read()
    out, last = [], 0
    hits = list(_REF.finditer(s))
    for i, mt in enumerate(hits):
        a, b = mt.group("a"), mt.group("b")
        out.append(s[last:mt.start()])
        last = mt.end()
        if b:                                       # a range of book pages
            pages = [x[0] for k in (a, b) for x in m.get(k, [])]
            out.append(f"{_pdf_ref(pages)} (book pp.{a}–{b})" if pages
                       else f"book pp.{a}–{b}")
            continue
        sheets = m.get(a)
        if not sheets:
            out.append(f"book p.{a}")
            continue
        # What this reference is about: the text up to the next reference.
        end = hits[i + 1].start() if i + 1 < len(hits) else len(s)
        ctx = s[mt.end():end].split("\n")[0]
        pick = set()
        if len(sheets) > 1:
            for fn in re.findall(r"fn\.? ([٠-٩]+)", ctx):
                pick |= {n for n, notes, _ in sheets if fn in notes}
            if "matn" in ctx or not pick:
                for q in re.findall(r"«([^«»]{3,})", ctx):
                    q = q.split("»")[0]
                    pick |= {n for n, _, fr in sheets if q in fr}
        pages = sorted(pick) or [x[0] for x in sheets]
        out.append(f"{_pdf_ref(pages)} (book p.{a})")
    out.append(s[last:])
    dest = os.path.join(book.build_dir, f"{book.basename}_Review-Notes.md")
    open(dest, "w", encoding="utf-8").write("".join(out))
    print("Wrote", dest)


if __name__ == "__main__":
    main()
