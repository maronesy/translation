# Maintainer guide

## One-time setup

1. **Create the repository** (public) and push this project to `main`.
2. **Protect `main`** — *Settings → Branches → Add branch ruleset* (or *branch
   protection rule*) for `main`:
   - Require a pull request before merging, with **2 approvals**;
   - Dismiss stale approvals when new commits are pushed;
   - Require review from Code Owners;
   - Require status checks to pass: **Check pages** and **Evidence** (each
     can be added once it has run at least once), with branches up to date;
   - Block force pushes and deletions;
   - Do not allow bypassing the above (so maintainers' own changes are reviewed too).

   Two reviewers must approve each pull request, and GitHub does not let
   anyone approve their own. The project therefore needs at least two
   reviewers with write access, listed in `CODEOWNERS` (three, for reviewers'
   own pull requests). Until there are enough, the repository admin can merge
   through the ruleset's bypass, set to "For pull requests only" so that
   direct pushes to `main` stay blocked.
3. **Merging** — in the ruleset, allow the **Merge** and **Squash** methods
   (not Rebase); in *Settings → General → Pull Requests* enable
   "Automatically delete head branches". Use squash for corrections, docs and
   engine changes, and a merge commit for tidy batches of new pages.
4. **Code owners** — `.github/CODEOWNERS` lists the maintainers (currently
   `@maronesy`); add each new maintainer there.
5. **Actions** — *Settings → Actions → General → Workflow permissions*: "Read
   and write permissions" (the release workflow creates releases).
6. **Labels** — create `correction`, `confirmed`, `new-book`,
   `book-accepted`, `needs-photo`, `wontfix`.

## Adding a reviewer

1. Check the application (sent to souhayl@alkalam.org) against the criteria
   in the README, "Become a reviewer": reads classical Arabic and English, has
   taught the book or one at its level, holds an *ijāza* or degree.
2. Invite the applicant: *Settings → Collaborators → Add people*, by GitHub
   username, with the **Write** role.
3. Once they accept, add their username to `.github/CODEOWNERS` by pull
   request (`*  @maronesy @newreviewer`).
4. To remove a reviewer, take their username out of `CODEOWNERS` and remove
   them under *Settings → Collaborators*.

## Handling a correction issue

1. Check the report against the printed edition. For an Arabic change, a
   photo of the printed page must be in the issue; if it is not, add
   `needs-photo` and ask for one.
2. If the report is right, label it `confirmed`. Anyone may then submit the
   fix as a pull request; a maintainer may also prepare it (by hand or with an
   AI tool of their choice — the project runs none).
3. Review the pull request: wait for **Check pages**, **Evidence** and
   **Build preview**. The Evidence log lists every page whose Arabic changed;
   compare each changed Arabic string with the photo, and check the changed
   sheet in the preview artifact. A passing Evidence check only means the
   photo and boxes are there — looking at them is the review.
4. Approve and squash-merge. The issue closes through `Fixes #…`, and the
   release workflow publishes a new build.
5. If the report is wrong, explain why, label `wontfix`, and close.

## Reviewing AI-assisted pull requests

Review them like any other, with extra attention to the Arabic: compare every
changed Arabic string with the printed page, look for silently corrected
misprints, and for edits outside the stated scope. Close pull requests that
show unverified machine output.

## Reviewing a new book

Check the proposal issue was accepted, the edition is identified, the rights
statement is credible, the sample is at least five consecutive pages, the
checks pass, and a spot check of the sample against the edition finds the
Arabic exact and the English faithful.

## Releases

Every merge to `main` that touches `books/` or `engine/` builds all books and
publishes a release named `Build <n>` with each book's PDF, Word file and
review notes. To rebuild without a change, run the **Release** workflow by
hand (*Actions → Release → Run workflow*). Old releases can be deleted.
