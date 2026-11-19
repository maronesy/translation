# Instructions for Claude in this repository

This repository holds Arabic–English translations of classical Islamic texts.
You are usually invoked by a maintainer's `@claude` comment on a correction
issue or a pull request. Your job is to make exactly the requested change,
correctly, and hand it back for human review. You never merge.

## The data

- Each book is in `books/<slug>/`, configured by `book.toml`.
- One file per page of the scanned edition: `books/<slug>/pages/page_NNN.py`,
  holding `PAGE_NUMBER`, `PRINTED_PAGE` and a `BLOCKS` list. The block schema
  and the translation style are in `docs/TRANSLATION-GUIDE.md`. Read it before
  editing.
- **Page numbers.** Reports cite the *book page* printed in the edition
  (Arabic-Indic, e.g. ٣٠٥). The file is
  `page_<book page + pdf_offset>.py`, with `pdf_offset` from `book.toml`.
  Confirm by checking that the file's `PRINTED_PAGE` equals the reported
  book page. If a report gives only a PDF page of the manuscript edition, it
  is not a file number: find the file by searching `pages/` for the quoted
  words.

## Rules for any edit

1. **Arabic is changed only against the printed text.** A change to an Arabic
   string needs a photo or scan of the printed page in the issue or pull
   request. Download each image link in the issue body and comments
   (`curl -L -o /tmp/<name> <url>`) and read the image. If no image shows the
   passage, or you cannot read it with certainty, do not change the Arabic:
   reply asking for a photo of the printed page, and stop.
2. **Transcribe exactly what is printed.** Never correct a misprint silently.
   If the print itself is wrong, keep it and add a `# REVIEW: <what is printed>,
   <what is intended>; transcribed as printed` comment above the block. The
   English may follow the evident sense.
3. **Respect the book's rules.** If `book.toml` has `diacritics = false`, the
   Arabic must contain no ḥarakāt, shadda, sukūn, tanwīn or dagger alif
   (U+064B–U+0652, U+0670).
4. **Change only what the request concerns.** Do not reformat, re-translate or
   "improve" other blocks. Keep `[[N]]` markers and `note` blocks in step.
5. **English:** faithful, scholarly, ALA-LC transliteration, additions in
   square brackets, no paraphrase. Do not add references the edition does not
   print except as `[translator’s reference: …]`.
6. **Never guess.** If the request is ambiguous, or the requested change looks
   wrong on the evidence, say so in a reply and make no change.

## Procedure for a correction issue

1. Read the issue and all comments, and download any images.
2. Locate the page file and the block(s); confirm `PRINTED_PAGE`.
3. Make the edit following the rules above.
4. If the correction resolves an entry in `books/<slug>/REVIEW-NOTES.md`,
   remove that entry and the matching `# REVIEW` comment. If it raises a new
   doubt, add both. Cite entries by book page, e.g. `book p.٣٠٥ fn ٦`.
5. Run `python engine/check_page.py books/<slug> <file page number>` and make
   sure it passes.
6. Commit with the message `<slug>: book p.<page> <where> — <what> (fixes #<issue>)`,
   push the branch, and reply with: what you changed (old → new, for each
   block), the evidence you used, and the link to open the pull request.
   Write `Fixes #<issue>` in the suggested pull-request body.

## Procedure on a pull request

When asked to review or amend a pull request, apply the same rules. To review,
list concrete problems by file and block (wrong transcription against an
attached photo, unfaithful English, broken markers, rule violations); do not
restate what is correct.

## Never

- commit scans, PDFs or other copyrighted material;
- edit `book.toml`, the engine, workflows or licenses unless the maintainer
  explicitly asks for that change;
- merge, approve, or close issues.
