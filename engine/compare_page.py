# -*- coding: utf-8 -*-
"""Score a page file produced by an AI model (or a person) against the
reviewed page file in the repository — the calibration test in the README
("Choosing a model").

Usage:
    python engine/compare_page.py books/<slug> <scan page> <candidate.py>

<candidate.py> is a page file in the same format, made from the same scan
page without looking at the repository's version. Reports:
  • Arabic word accuracy (diacritics ignored), and every differing word;
  • whether the footnote markers and notes match the reference;
  • whether misprints flagged `# REVIEW` in the reference were kept as
    printed (a model that "corrects" them silently fails this);
  • forbidden diacritics, if the book forbids them.
The English is not scored: read it against the reference yourself.
Files are parsed, not executed.
"""
import ast
import difflib
import re
import sys

from book import Book

DIAC = re.compile("[ً-ْٰ]")
MARK = re.compile(r"\[\[([٠-٩]+)\]\]")


def blocks_of(path):
    src = open(path, encoding="utf-8").read()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "BLOCKS" for t in node.targets):
            return src, ast.literal_eval(node.value)
    sys.exit(f"{path}: no BLOCKS list")


def words(blocks):
    text = " ".join(b.get("ar", "") for b in blocks)
    text = DIAC.sub("", MARK.sub(" ", text))
    return re.findall(r"[؀-ۿ]+", text)


def structure(blocks):
    marks = [m for b in blocks if b.get("type") != "pair" for m in MARK.findall(b.get("ar", ""))]
    notes = [b.get("num") for b in blocks if b.get("type") == "note"]
    return marks, notes


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    book = Book(sys.argv[1])
    ref_src, ref = blocks_of(book.page_file(int(sys.argv[2])))
    cand_src, cand = blocks_of(sys.argv[3])

    rw, cw = words(ref), words(cand)
    sm = difflib.SequenceMatcher(a=rw, b=cw, autojunk=False)
    same = sum(size for _, _, size in sm.get_matching_blocks())
    print(f"Arabic words: reference {len(rw)}, candidate {len(cw)}, "
          f"matching {same} ({100 * same / max(len(rw), 1):.1f}% of the reference)")
    diffs = [(op, " ".join(rw[i1:i2]), " ".join(cw[j1:j2]))
             for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    for op, a, b in diffs[:40]:
        print(f"  {op:8} reference «{a}»  →  candidate «{b}»")
    if len(diffs) > 40:
        print(f"  … and {len(diffs) - 40} more differences")

    rm, rn = structure(ref)
    cm, cn = structure(cand)
    print("Footnote markers and notes:", "match" if (rm, rn) == (cm, cn)
          else f"DIFFER (reference {len(rm)} markers / {len(rn)} notes, "
               f"candidate {len(cm)} / {len(cn)})")

    flagged = re.findall(r"#\s*REVIEW:?[^\n]*?«([^»]+)»", ref_src)
    cand_text = DIAC.sub("", " ".join(b.get("ar", "") for b in cand))
    kept = [w for w in flagged if DIAC.sub("", w) in cand_text]
    if flagged:
        print(f"Misprints flagged in the reference kept as printed: {len(kept)}/{len(flagged)}")
        for w in flagged:
            if w not in kept:
                print(f"  not found as printed: «{w}» (silently corrected or misread?)")

    if not book.diacritics_allowed:
        d = len(DIAC.findall(" ".join(b.get("ar", "") for b in cand)))
        print("Forbidden diacritics:", d)
    print("English: not scored — compare it with the reference by reading.")


if __name__ == "__main__":
    main()
