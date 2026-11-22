# Instructions for AI assistants

These rules apply to any AI tool working in this repository (Claude Code,
Codex, Copilot, Cursor, Gemini or others). The person running you is a
contributor; their pull request will be reviewed by a maintainer against the
printed edition. Make exactly the change asked for, correctly, and show the
contributor what you changed so they can check it.

## The data

- Each book is in `books/<slug>/`, configured by `book.toml`.
- One file per page of the scanned edition: `books/<slug>/pages/page_NNN.py`,
  holding `PAGE_NUMBER`, `PRINTED_PAGE` and a `BLOCKS` list. The block schema
  and the translation style are in `docs/TRANSLATION-GUIDE.md`. **Read it
  before editing.** `books/mulla-jami/pages/page_024.py` is a worked example.
- **Page numbers.** People cite the *book page* printed in the edition
  (Arabic-Indic, e.g. ٣٠٥). The file is `page_<book page + pdf_offset>.py`,
  with `pdf_offset` from `book.toml`. Confirm that the file's `PRINTED_PAGE`
  equals the cited book page. A PDF page number of a release is not a file
  number: find the file by searching `pages/` for the quoted words.

## Rules for any edit

1. **Arabic comes only from the printed page.** Transcribe from the scan or a
   photo the contributor gives you — render scan pages at high resolution with
   `python engine/hires_page.py books/<slug> <scan page>` and read every band.
   If you cannot read a word with certainty, say so; never reconstruct or
   supply Arabic from memory or from another edition.
2. **Transcribe exactly what is printed.** Never correct a misprint silently.
   If the print itself is wrong, keep it and add a comment above the block:
   `# REVIEW: <what is printed>, <what is intended>; transcribed as printed`.
   The English may follow the evident sense.
3. **Respect the book's rules.** If `book.toml` has `diacritics = false`, the
   Arabic must contain no ḥarakāt, shadda, sukūn, tanwīn or dagger alif
   (U+064B–U+0652, U+0670).
4. **Change only what the task concerns.** Do not reformat, re-translate or
   "improve" other blocks. Keep the `[[N]]` markers in the main text and the
   numbered `note` blocks in step.
5. **English:** faithful, scholarly, ALA-LC transliteration, additions for
   sense in square brackets, no paraphrase. Do not add references the edition
   does not print except as `[translator’s reference: …]`.
6. **Record doubt.** A doubtful reading or rendering gets a `# REVIEW:`
   comment and an entry in `books/<slug>/REVIEW-NOTES.md`, cited by book page
   (`book p.٣٠٥ fn ٦`). Resolving one removes both.
7. **Never commit** scans, PDFs or other copyrighted files. Do not edit
   `book.toml`, `engine/`, `.github/` or licenses unless asked to.

## Procedure: a correction

1. Read the issue (or the contributor's request) and look at the photo or scan
   of the printed page.
2. Locate the page file and block(s); confirm `PRINTED_PAGE`.
3. Edit following the rules above; update `REVIEW-NOTES.md` if needed.
4. Run `python engine/check_page.py books/<slug> <file page number>`.
5. Report to the contributor, for each changed block, the old and new text and
   the evidence used. Suggest the commit message
   `<slug>: book p.<page> <where> — <what>` and `Fixes #<issue>` for the
   pull request.

## Procedure: translating new pages

1. Work one scan page at a time, top to bottom: main text, then footnotes.
2. Write `pages/page_<NNN>.py` in the schema of the guide; split text into
   sentences, each with its English.
3. Run `python engine/check_page.py books/<slug> <NNN>` after each page, and
   build a preview with `python engine/build_manuscript.py books/<slug> <NNN>`.
4. List for the contributor every uncertain reading you flagged.

## Never

- invent or "restore" Arabic you cannot see on the printed page;
- merge, approve, or push to `main`; changes reach `main` only through a
  pull request approved by a maintainer.
