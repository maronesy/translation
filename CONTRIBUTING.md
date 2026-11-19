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
| Fix prepared by Claude | `claude/…` (created by the action) | set by the maintainer |

- One pull request per correction or per batch of pages. Do not mix a
  correction with unrelated edits.
- Link the issue it resolves with `Fixes #<number>`.
- Pull requests are squash-merged. The squash commit message uses the pull
  request title.

## What a pull request must satisfy

1. **The checks pass** (`python engine/check_page.py books/<slug>`): every page
   loads, footnote markers match footnotes, and the book's rules hold.
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

- A pull request needs **one approving review from a maintainer** and passing
  checks before it can be merged. Maintainers do not approve their own pull
  requests; another maintainer does.
- The reviewer checks the changed sheets in the preview PDF attached to the
  pull request's checks (under *Artifacts*), and the Arabic against the
  printed page.
- New books are reviewed for: an identified edition, a clear rights
  statement, at least five consecutive sample pages that pass the checks, and
  translation quality in a spot check of those pages.

## Asking Claude for a fix (maintainers)

Comment `@claude` on an issue or pull request, for example:

> @claude fix this

> @claude book p.٣٠٥ fn ٦ — the photo above shows «يستعمل»; please correct the transcription

Claude follows [CLAUDE.md](CLAUDE.md): it reads the issue, checks the photo of
the printed page, edits only the affected blocks, runs the checks, pushes a
branch named `claude/…`, and replies with a link to open the pull request. It
will not change Arabic it cannot verify against the printed text; it will ask
instead. Its pull requests are reviewed like any other.

Only people with write access can trigger Claude. Each run uses the project's
Anthropic API key and is billed to it.

## Labels

| Label | Meaning |
|---|---|
| `correction` | A reported mistake (set by the issue form) |
| `new-book` | A book proposal (set by the issue form) |
| `book-accepted` | The proposal was accepted; the sample may be submitted |
| `needs-photo` | A photo of the printed page is needed before the Arabic can change |
| `wontfix` | Reviewed and not changed; the reason is in the issue |

## Conduct

Be courteous and specific. Discuss the text, not the person. Maintainers may
close or lock discussions that are not.
