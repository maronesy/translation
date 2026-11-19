# -*- coding: utf-8 -*-
"""Build preview files for a pull request (used by .github/workflows/check.yml).

Usage: python engine/ci_preview.py <base git ref>

For each book touched by the pull request, builds the Word and manuscript
editions of only the changed pages (or of the whole book if its book.toml or
the engine changed) into books/<slug>/build/, and checks those pages.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    base = sys.argv[1]
    changed = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"],
                             cwd=ROOT, check=True, capture_output=True,
                             text=True).stdout.split()
    engine_changed = any(f.startswith("engine/") for f in changed)
    books = {}
    for f in changed:
        m = re.match(r"books/([^/_][^/]*)/(.*)", f)
        if not m:
            continue
        slug, rest = m.groups()
        pages = books.setdefault(slug, set())
        p = re.match(r"pages/page_(\d+)\.py$", rest)
        if p and os.path.exists(os.path.join(ROOT, f)):
            pages.add(p.group(1).lstrip("0"))
        elif rest == "book.toml":
            pages.add("ALL")
    if engine_changed and "mulla-jami" not in books:
        books["mulla-jami"] = {"ALL"}        # exercise the engine on the reference book
    if not books:
        print("No book pages changed; nothing to preview.")
        return
    for slug, pages in sorted(books.items()):
        sel = [] if "ALL" in pages or engine_changed else sorted(pages, key=int)
        if not os.path.exists(os.path.join(ROOT, "books", slug, "book.toml")):
            continue
        if not sel and not ("ALL" in pages or engine_changed):
            continue                          # only notes/README changed
        target = os.path.join("books", slug)
        print(f"== {slug}: {'whole book' if not sel else 'pages ' + ' '.join(sel)}")
        for script in ("build_docx.py", "build_manuscript.py"):
            subprocess.run([sys.executable, os.path.join("engine", script), target,
                            *sel, "--nocover"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
