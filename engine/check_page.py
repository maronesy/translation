# -*- coding: utf-8 -*-
"""Check a book's page files. CI runs this on every pull request.

Usage:
    python engine/check_page.py books/<slug>              # every page
    python engine/check_page.py books/<slug> 305 306      # some PDF pages

A page passes when:
  • it loads, PAGE_NUMBER matches its file name, and PRINTED_PAGE is set;
  • every block has a known type, and text blocks have both "ar" and "en";
  • the footnote markers [[١]]…[[K]] in the main text match the numbered notes
    ١…K (an unnumbered carried-over note, num "" or "…", is allowed);
  • if the book's `book.toml` sets `rules.diacritics = false`, the file has no
    Arabic diacritics (U+064B–U+0652, U+0670).
Exit code 1 if any page fails.
"""
import re
import sys

from book import parse_args

DIAC = re.compile("[ً-ْٰ]")
DIG = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
TYPES = {"section", "basmala", "khutba", "matn", "verse", "quran", "rule", "note", "pair"}
NEEDS_TEXT = {"section", "khutba", "matn", "verse", "quran", "pair"}


def check(book, n):
    errs = []
    try:
        mod = book.load_pages({n})[0][1]
    except Exception as e:                      # syntax error, bad import…
        return [f"does not load: {e}"], 0, 0
    if getattr(mod, "PAGE_NUMBER", None) != n:
        errs.append(f"PAGE_NUMBER is {getattr(mod, 'PAGE_NUMBER', None)}, file name says {n}")
    if not getattr(mod, "PRINTED_PAGE", None):
        errs.append("PRINTED_PAGE missing")
    blocks = getattr(mod, "BLOCKS", [])
    for i, b in enumerate(blocks):
        t = b.get("type")
        if t not in TYPES:
            errs.append(f"block {i}: unknown type {t!r}")
        elif t in NEEDS_TEXT and not (b.get("ar") and b.get("en")):
            errs.append(f"block {i} ({t}): needs both 'ar' and 'en'")
    marks = sorted(int(x.translate(DIG)) for b in blocks
                   if b.get("type") in ("matn", "section", "verse", "quran", "khutba")
                   for x in re.findall(r"\[\[([٠-٩]+)\]\]", b.get("ar", "")))
    nums = [int(b["num"].translate(DIG)) for b in blocks
            if b.get("type") == "note" and b.get("num") not in ("", "…")]
    if not marks == nums == list(range(1, len(nums) + 1)):
        errs.append(f"markers {marks} do not match notes {nums}")
    if not book.diacritics_allowed:
        d = len(DIAC.findall(open(book.page_file(n), encoding="utf-8").read()))
        if d:
            errs.append(f"{d} Arabic diacritics (this book forbids them)")
    return errs, len(marks), len(nums)


def main():
    book, which, _ = parse_args(sys.argv[1:])
    pages = sorted(which) if which else book.page_numbers()
    bad = 0
    for n in pages:
        errs, k, m = check(book, n)
        if errs:
            bad += 1
            for e in errs:
                print(f"FAIL {book.slug} page {n}: {e}")
        elif which:
            print(f"ok   {book.slug} page {n}: markers {k}, notes {m}")
    print(f"{book.slug}: {len(pages) - bad}/{len(pages)} pages pass")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
