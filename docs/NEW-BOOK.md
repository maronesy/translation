# Starting a new book

Read "Propose a new book" in the [README](../README.md#propose-a-new-book)
first: open a proposal issue and wait for the `book-accepted` label before
translating many pages.

## 1. Create the folder

```sh
git switch -c book/<slug>
cp -r books/_template books/<slug>
```

`<slug>` is short, lowercase, with hyphens (`sharh-al-aqaid`). It must match
`slug` in `book.toml`.

## 2. Fill in `book.toml`

| Key | Meaning |
|---|---|
| `slug` | Folder name. |
| `status` | `proposal` (sample only), `in-progress`, or `complete`. |
| `title.ar`, `title.en` | Arabic title and short English title (cover, contents, running footer). |
| `title.subtitle_en`, `title.field_en` | Cover lines, e.g. "The Commentary of X on Y", "in the science of …". |
| `author.ar`, `author.en` | Author, with death date in `en`. |
| `source.edition` | Full citation of the printed edition followed. |
| `source.pdf_offset` | Scan PDF page minus printed page. If printed page ١ is the 5th page of your PDF, the offset is 4. |
| `source.first_page`, `source.last_page` | Range of scan pages translated so far. |
| `source.missing` | Printed pages absent from your scan. |
| `source.local_scan` | Where your own scan lives, inside `source/` (git-ignored). |
| `rules.diacritics` | `false` forbids ḥarakāt, shadda, sukūn, tanwīn and dagger alif in the Arabic; the checks enforce it. |
| `output.basename` | File-name stem for the release files. |

Also fill in `README.md` (edition, rights statement, status, translators).

## 3. Translate pages

One file per scan page, `pages/page_<NNN>.py`, following
[TRANSLATION-GUIDE.md](TRANSLATION-GUIDE.md). Use the scan reader to read
dense footnotes at high resolution:

```sh
python engine/hires_page.py books/<slug> <scan page>
```

Record every doubtful or misprinted reading with a `# REVIEW:` comment and an
entry in `REVIEW-NOTES.md`, cited by book page.

## 4. Check and preview

```sh
python engine/check_page.py books/<slug>
python engine/build_manuscript.py books/<slug>
python engine/build_docx.py books/<slug>
```

The files appear in `books/<slug>/build/`. Look at every sheet: the matn in
its frame, each ḥāshiya next to the sheet carrying its marker.

## 5. Pull request

Push the branch and open a pull request titled `New book: <title>`, linking
the proposal issue. The checks attach a preview build. See
[CONTRIBUTING.md](../CONTRIBUTING.md) for what the review looks at.
