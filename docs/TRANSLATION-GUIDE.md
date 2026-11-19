# Translation guide (for translators and agents)

Applies to every book in `books/`. You translate **one page of the scanned
edition** into one Python content file. Follow this exactly
so every page matches the design engine and reads consistently.

## 1. Read the page — AT HIGH RESOLUTION (mandatory)

The source is a **scanned image PDF** (no text layer). Reading the whole page at
default resolution makes the dense footnotes mushy and tempts you to *guess*.
**Do not.** The scan is clean — every ḥāshiya is fully legible when zoomed in.

Render the page into high-DPI horizontal bands and read each band:

```
python engine/hires_page.py books/<slug> <N>   # 500 dpi, 3 bands (matn + footnotes)
```

It prints PNG paths; **Read each band top-to-bottom** with the Read tool. Read
the footnote bands especially carefully. If any word is still not crisp, re-run
at higher DPI or more bands (`python engine/hires_page.py books/<slug> <N> 700 4`) and/or read
that band again — **keep zooming until you can actually read it.**

**Never reconstruct or paraphrase from a blurry glimpse.** Transcribe what is
actually on the page. Only if a word is physically damaged/torn on the page
(essentially never here) do you add an inline `# REVIEW: …` comment. A footnote
being long or dense is *not* a reason to flag it — read it.

Find **PRINTED_PAGE**: the page number printed at the bottom of the page image,
in Arabic-Indic numerals (٢٣, ٢٤, …). Copy it verbatim.

## 2. Page structure

- **Top block (above the horizontal rule)** — the main commentary text (matn).
  It carries inline footnote markers like `[١] [٢]` over specific words.
  **Convert each one into `[[N]]`** (double square brackets, Arabic-Indic
  numeral) placed **immediately after the word it sits on**, before any space or
  punctuation. The engine renders `[[N]]` as a small superscript gold reference
  number tying that word to footnote N. Example: `الْحَمْدُ[[١]] لِوَلِيِّهِ[[٢]]،`.
  The markers run 1..K in order through the main text (K = number of footnotes).
- **Below the rule** — numbered footnotes (ḥawāshī): `[١] …`, `[٢] …`.
- Sometimes **poetry** (two centred hemistichs) or **Qurʾānic verses** appear,
  in either the main text or a footnote.

Insert one `{"type": "rule"}` block between the main text and the first footnote.

A `section` block is a heading actually printed on the page (often bracketed,
e.g. `[الاسم]`, `[المُعرَب والمَبنيّ]`). Use it for such headings — it also feeds
the document's table of contents, so give a good English title.

## 3. Block schema (use these types only)

```python
{"type": "section", "ar": "...", "en": "..."}   # a heading printed on the page (rare)
{"type": "khutba",  "ar": "...", "en": "..."}   # ONLY the opening address ("أمّا بعد…" on p.24–25)
{"type": "matn",    "ar": "...", "en": "..."}   # a sentence of the main commentary text
{"type": "verse",   "ar": "...", "en": "..."}   # a line of poetry; put BOTH hemistichs in ar,
                                                #   separated by several spaces
{"type": "quran",   "ar": "...", "en": "..."}   # a Qurʾānic quotation set on its own
{"type": "rule"}                                 # the divider between matn and footnotes
{"type": "note",    "num": "١"}                 # opens footnote number ١ (Arabic-Indic)
{"type": "pair",    "ar": "...", "en": "..."}   # a sentence INSIDE the current footnote
```

- Split BOTH the main text and each footnote into **sentences** (or coherent
  clauses). Each `matn`/`pair`/`verse`/`quran` block is one Arabic sentence with
  its English translation. Keep them reasonably short — one thought each.
- A footnote = one `note` block followed by one or more `pair` blocks.

## 4. Translation style

- Faithful, scholarly English in the register of a classical grammar commentary.
  Convey the meaning precisely; do not paraphrase loosely or add commentary.
- Transliterate technical terms in ALA-LC style with macrons and dots, glossing
  on first use, e.g. *iʿrāb*, *maṣdar*, *mubtadaʾ*. Common terms:
  الكافية = al-Kāfiya · ابن الحاجب = Ibn al-Ḥājib · الكلمة = *kalima* (word) ·
  الكلام = *kalām* (speech) · الاسم = *ism* (noun) · الفعل = *fiʿl* (verb) ·
  الحرف = *ḥarf* (particle) · الإعراب = *iʿrāb* (inflection) · البناء = *bināʾ*
  (indeclinability) · المبتدأ = *mubtadaʾ* · الخبر = *khabar* · الفاعل = *fāʿil*
  · المفعول = *mafʿūl* · المصدر = *maṣdar* · الاشتقاق = *ishtiqāq* (derivation) ·
  النحو = *naḥw* (syntax) · الصرف = *ṣarf* (morphology).
- Honorifics: ﷺ → "may Allah bless him and grant him peace"; رضي الله عنه →
  "may Allah be pleased with him"; سبحانه → "Glorified is He"; تعالى →
  "the Exalted".
- Qurʾān: when the source cites e.g. «… (سورة البقرة: ٣٧)», render the citation
  as "(Qurʾān, Sūrat al-Baqara 2:37)".
- «…» guillemets in the source quote a lemma being glossed (قوله: «الحمد»). Keep
  the quoted Arabic and render "His words '…'".
- Arabic text, in books whose `book.toml` sets `diacritics = false` (Mullā
  Jāmī does): **no diacritics at all**. Do not write
  any fatḥa, ḍamma, kasra, sukūn, shadda, tanwīn or dagger alif (U+064B–U+0652,
  U+0670), even where the page prints them, and never add iʿrāb. Write هذا, ذلك,
  المعنى — not هٰذا, ذٰلك, المعنىٰ. Hamza forms (أ إ ؤ ئ آ) are letters; keep them.

## 5. Output file

Write exactly one file: `books/<slug>/pages/page_<NNN>.py` (zero-padded to
three digits, e.g. page 31 → `page_031.py`). Do not touch any other file.

Template:

```python
# -*- coding: utf-8 -*-
"""<Book title>. Source PDF page <N> (printed <PRINTED>)."""

PAGE_NUMBER = <N>
PRINTED_PAGE = "<PRINTED>"   # Arabic-Indic, as printed

BLOCKS = [
    # ... blocks in reading order ...
]
```

See `books/mulla-jami/pages/page_024.py` for a complete worked example. Match its
shape exactly. Check each file with `python engine/check_page.py books/<slug> <N>`.
The build step imports every `pages/page_*.py` automatically and orders by
`PAGE_NUMBER`, so you only need to produce a correct file.
