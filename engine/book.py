# -*- coding: utf-8 -*-
"""A book project: its `book.toml` settings and its page files.

Every book lives in `books/<slug>/` with:
    book.toml          metadata (titles, edition, page range, rules)
    pages/page_NNN.py  one file per source-PDF page (see docs/TRANSLATION-GUIDE.md)
    REVIEW-NOTES.md    readings to check against the printed edition
    source/            the contributor's own scan (never committed)
Built files go to `books/<slug>/build/` (never committed).
"""
import glob
import importlib.util
import os
import sys
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Book:
    def __init__(self, path):
        path = os.path.abspath(path)
        if not os.path.isfile(os.path.join(path, "book.toml")):
            sys.exit(f"{path}: no book.toml — pass a book folder, e.g. books/mulla-jami")
        self.dir = path
        with open(os.path.join(path, "book.toml"), "rb") as f:
            self.cfg = tomllib.load(f)
        self.slug = self.cfg["slug"]
        self.pages_dir = os.path.join(path, "pages")
        self.build_dir = os.path.join(path, "build")
        self.basename = self.cfg.get("output", {}).get("basename", self.slug)
        self.offset = self.cfg["source"].get("pdf_offset", 0)
        self.diacritics_allowed = self.cfg.get("rules", {}).get("diacritics", True)

    def title(self, key, default=""):
        return self.cfg.get("title", {}).get(key, default)

    def scan_path(self):
        return os.path.join(self.dir, self.cfg["source"].get("local_scan", "source/scan.pdf"))

    def page_file(self, n):
        return os.path.join(self.pages_dir, f"page_{n:03d}.py")

    def page_numbers(self):
        return sorted(int(os.path.basename(f)[5:8]) for f in
                      glob.glob(os.path.join(self.pages_dir, "page_*.py")))

    def load_pages(self, which=None):
        """[(pdf_page, module)] in page order; `which` limits to a set of pages."""
        pages = []
        for n in self.page_numbers():
            if which and n not in which:
                continue
            spec = importlib.util.spec_from_file_location(f"page_{n:03d}", self.page_file(n))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            pages.append((n, mod))
        return pages


def parse_args(argv):
    """`<book dir> [pdf pages…] [--flags]` → (Book, set of pages or None, flags)."""
    pos = [a for a in argv if not a.startswith("--")]
    flags = {a for a in argv if a.startswith("--")}
    if not pos:
        sys.exit("usage: <script> books/<slug> [pdf pages…] [--flags]")
    book = Book(pos[0])
    which = {int(a) for a in pos[1:] if a.isdigit()} or None
    return book, which, flags
