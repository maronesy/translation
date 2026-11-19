# Maintainer guide

## One-time setup

1. **Create the repository** (public) and push this project to `main`.
2. **Protect `main`** — *Settings → Branches → Add branch ruleset* (or *branch
   protection rule*) for `main`:
   - Require a pull request before merging, with **1 approval**;
   - Dismiss stale approvals when new commits are pushed;
   - Require review from Code Owners;
   - Require status checks to pass: **Check pages**;
   - Block force pushes and deletions;
   - Do not allow bypassing the above (so maintainers' own changes are reviewed too).
3. **Merging** — *Settings → General → Pull Requests*: allow squash merging
   only; enable "Automatically delete head branches".
4. **Code owners** — replace `@OWNER` in `.github/CODEOWNERS` with the
   maintainers' GitHub usernames.
5. **Claude** —
   - install the Claude GitHub App on the repository:
     https://github.com/apps/claude (or run `/install-github-app` in Claude Code);
   - add the repository secret `ANTHROPIC_API_KEY` (*Settings → Secrets and
     variables → Actions*). Usage is billed to that key;
   - only users with write access can trigger Claude; keep write access to
     maintainers.
6. **Actions** — *Settings → Actions → General → Workflow permissions*: "Read
   and write permissions" (the release workflow creates releases).
7. **Labels** — create `correction`, `new-book`, `book-accepted`,
   `needs-photo`, `wontfix`.
8. Replace `OWNER/REPO` in `README.md` with the real path.

## Handling a correction issue

1. Check the report against the printed edition. For an Arabic change, a
   photo of the printed page must be in the issue; if it is not, add
   `needs-photo` and ask for one.
2. If the report is right, comment `@claude fix this` (add any precision, e.g.
   which reading to adopt). Claude replies with what it changed and a link to
   open the pull request.
3. Open the pull request from the link. Wait for **Check pages** and **Build
   preview**; download the preview artifact and look at the changed sheet.
4. Approve and squash-merge. The issue closes through `Fixes #…`, and the
   release workflow publishes a new build.
5. If the report is wrong, explain why, label `wontfix`, and close.

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
