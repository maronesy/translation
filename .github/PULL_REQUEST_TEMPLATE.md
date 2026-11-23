## What this changes

<!-- e.g. "mulla-jami: book p.305 fn 6 — restore printed «يتسعمل», add REVIEW note" -->

Fixes #

## Type

- [ ] Correction
- [ ] New book (proposal and sample pages)
- [ ] Further pages of a book
- [ ] Engine / docs / workflows

## Photo of the printed page

<!-- Required if this changes Arabic in existing pages (the "Evidence" check
     fails without it), unless the linked issue already has one. Drag the
     image of the printed passage here. -->

## AI tools

<!-- Tick one. The "Evidence" check requires it when page files change. -->

- [ ] No AI tool was used
- [ ] An AI tool was used: <!-- tool, model and version (e.g. "Claude Code, Claude Opus 5.5"), and for what (transcription, translation, checking) -->

## Checklist

<!-- The "Evidence" check requires the box "I checked every changed line…"
     to be ticked when page files change. -->

- [ ] `python engine/check_page.py books/<slug>` passes
- [ ] Arabic changes match the printed edition (photo attached here or in the issue)
- [ ] Misprints are kept as printed with a `# REVIEW:` comment and a `REVIEW-NOTES.md` entry
- [ ] Only the affected blocks were edited
- [ ] I checked every changed line against the printed page myself
- [ ] No scans or other copyrighted files are included
- [ ] I agree to license my contribution to `books/` under CC BY-SA 4.0
