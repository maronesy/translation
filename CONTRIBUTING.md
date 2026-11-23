# Contributing

The [README](README.md) gives the step-by-step procedures for reporting a
mistake, fixing one, and proposing a book. This file sets out the rules that
pull requests are reviewed against.

## Branches and pull requests

| Change | Branch name | Pull request title |
|---|---|---|
| Correction | `fix/<book>-p<book page>-<short>` | `<book>: book p.<page> — <what>` |
| New book (proposal and sample) | `book/<slug>` | `New book: <title>` |
| Further pages of a book | `book/<slug>-pp<first>-<last>` | `<book>: book pp.<first>–<last>` |
| Engine, docs, workflows | `engine/<short>`, `docs/<short>` | short description |

- One pull request per correction or per batch of pages. Do not mix a
  correction with unrelated edits.
- Link the issue it resolves with `Fixes #<number>`.
- **Merge method.** Corrections, docs and engine changes are
  **squash-merged**: one commit on `main`, titled with the pull request title.
  Batches of new pages are **merged with a merge commit** when their commits
  are tidy (one per page or per few pages, with clear messages), so a single
  page can later be traced or reverted; otherwise they are squash-merged too.
  Rebase-merging is not used.

## What a pull request must satisfy

1. **The checks pass.** *Check pages* (`python engine/check_page.py
   books/<slug>`): every page loads, footnote markers match footnotes, and
   the book's rules hold. *Evidence* (`engine/check_evidence.py`): when page
   files change, the description ticks "I checked every changed line against
   the printed page myself" and one AI-tools box; when Arabic in existing
   pages changes, a photo of the printed page is in the description or the
   linked issue. New pages of a book batch need the boxes, not a photo per
   page.
2. **The Arabic is what the edition prints.** A change to the Arabic must be
   supported by the printed page: a photo in the issue or pull request, or the
   reviewer's own copy. Misprints are kept as printed and marked with a
   `# REVIEW: …` comment above the block; the English may follow the evident
   sense, with the reading noted.
3. **The English is faithful.** It renders what the Arabic says, in the
   register and transliteration of [docs/TRANSLATION-GUIDE.md](docs/TRANSLATION-GUIDE.md).
   Additions needed for sense go in square brackets. Nothing is added that the
   text does not say; a reference the edition does not print (e.g. a Qurʾān
   verse number) is marked `[translator’s reference: …]`.
4. **Uncertainty is recorded.** A doubtful reading or rendering gets a
   `# REVIEW:` comment and an entry in the book's `REVIEW-NOTES.md`, cited by
   book page (`book p.٣٠٥ fn ٦`). Resolving such an item removes both.
5. **No scans or other copyrighted files** are committed.

## Review

- A pull request needs **approving reviews from two reviewers** (maintainers)
  and passing checks before it can be merged; it is merged only if both agree
  with the change. Only maintainers can merge. A maintainer's own pull request
  needs two other reviewers.
- The reviewer checks the changed sheets in the preview PDF attached to the
  pull request's checks (under *Artifacts*), and the Arabic against the
  printed page.
- New books are reviewed for: an identified edition, a clear rights
  statement, at least five consecutive sample pages that pass the checks, and
  translation quality in a spot check of those pages.

## AI-assisted contributions

Any AI tool may be used; the project neither requires nor provides one.

- The tool must follow [AGENTS.md](AGENTS.md); point it there before it edits.
- You, not the tool, are the author. Check every changed line against the
  printed page before you open the pull request.
- Say in the pull-request template which tool you used and for what.
- Pull requests that show signs of unverified machine output — Arabic that
  does not match the print, silently "corrected" misprints, paraphrase,
  unrelated edits — are closed.

## Labels

| Label | Meaning |
|---|---|
| `correction` | A reported mistake (set by the issue form) |
| `confirmed` | A maintainer has checked the report; anyone may submit the fix |
| `new-book` | A book proposal (set by the issue form) |
| `book-accepted` | The proposal was accepted; the sample may be submitted |
| `needs-photo` | A photo of the printed page is needed before the Arabic can change |
| `wontfix` | Reviewed and not changed; the reason is in the issue |

## Conduct

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md)
(Contributor Covenant 2.1). Report problems to souhayl@alkalam.org.
