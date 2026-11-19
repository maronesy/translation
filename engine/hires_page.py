# -*- coding: utf-8 -*-
"""Render a source PDF page at high DPI and slice it into overlapping horizontal
bands, so the dense Arabic ḥawāshī are fully legible when read.

Usage:
    python engine/hires_page.py books/<slug> <pdf_page> [dpi] [nbands]

Needs your own copy of the book's scan at the path given by `local_scan` in
books/<slug>/book.toml (scans are never committed), and poppler's `pdftoppm`.

Defaults: dpi=500, nbands=3. Writes PNG bands to a temp dir and prints their
absolute paths (read them top-to-bottom). Read every band; never guess a word —
if a band is still unclear, re-run with a higher dpi (e.g. 700) or more bands.
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image

from book import Book


def main():
    book = Book(sys.argv[1])
    page = int(sys.argv[2])
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 500
    nbands = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    PDF = book.scan_path()
    if not os.path.exists(PDF):
        sys.exit(f"scan not found: {PDF}\nPut your own copy of the edition there "
                 f"(see books/{book.slug}/source/README.md).")

    out = os.path.join(tempfile.gettempdir(), f"hires_{book.slug}")
    os.makedirs(out, exist_ok=True)
    base = os.path.join(out, f"p{page}")
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(page), "-l",
                    str(page), PDF, base], check=True)
    src = next(os.path.join(out, f) for f in os.listdir(out)
               if f.startswith(f"p{page}-") and f.endswith(".png"))
    img = Image.open(src)
    W, H = img.size
    overlap = int(H / nbands * 0.12)
    print(f"page {page}: {W}x{H} @ {dpi}dpi -> {nbands} bands")
    for k in range(nbands):
        y0 = max(0, int(H * k / nbands) - overlap)
        y1 = min(H, int(H * (k + 1) / nbands) + overlap)
        p = f"{base}_band{k}.png"
        img.crop((0, y0, W, y1)).save(p)
        print(p)


if __name__ == "__main__":
    main()
