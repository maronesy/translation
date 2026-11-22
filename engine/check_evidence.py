# -*- coding: utf-8 -*-
"""The "Evidence" check for pull requests (.github/workflows/evidence.yml).

No check can compare the Arabic with the printed page — the repository holds
no scans — so this one requires the evidence a reviewer needs to do so:

  • If a pull request changes the Arabic ("ar") of a page that already exists
    on the base branch, a photo of the printed page must be in the pull
    request description or in an issue it fixes ("Fixes #N").
  • If it changes any page file at all, the description must tick
      "I checked every changed line against the printed page myself"
    and one of the two "AI tools" boxes.
New page files (a book batch) need the ticked boxes but no photo: their
translator works from their own scan, and reviewers spot-check them.
Pull requests that change no page files pass.

Usage (in CI): PR_BODY="…" GITHUB_TOKEN=… GITHUB_REPOSITORY=owner/repo \
               python engine/check_evidence.py origin/main
Page files are parsed, not executed.
"""
import ast
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = re.compile(r"^books/([^/_][^/]*)/pages/page_(\d+)\.py$")
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]+\)|<img\b|https://github\.com/user-attachments/assets/"
                   r"|\.(?:png|jpe?g|gif|webp|heic)\b", re.I)
VERIFIED = re.compile(r"-\s*\[[xX]\]\s*I checked every changed line against the printed page myself")
AI_BOX = re.compile(r"-\s*\[[xX]\]\s*(?:No AI tool was used|An AI tool was used)")
FIXES = re.compile(r"\b(?:fix(?:es|ed)?|close[sd]?|resolve[sd]?)\s+#(\d+)", re.I)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def arabic_of(source):
    """The list of 'ar' strings in a page file's BLOCKS, read without running it."""
    if source is None:
        return None
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "BLOCKS" for t in node.targets):
            return [b.get("ar", "") for b in ast.literal_eval(node.value)]
    return []


def file_at(ref, path):
    try:
        return git("show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None                                  # absent at that ref


def issue_texts(numbers):
    """Bodies and comments of the linked issues (public API; token if given)."""
    repo, token = os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN")
    texts = []
    for n in numbers:
        for url in (f"https://api.github.com/repos/{repo}/issues/{n}",
                    f"https://api.github.com/repos/{repo}/issues/{n}/comments?per_page=100"):
            req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                       **({"Authorization": f"Bearer {token}"} if token else {})})
            try:
                data = json.load(urllib.request.urlopen(req, timeout=20))
            except Exception as e:
                print(f"  (could not read issue #{n}: {e})")
                continue
            for item in data if isinstance(data, list) else [data]:
                texts.append(item.get("body") or "")
    return texts


def main():
    base = sys.argv[1]
    body = os.environ.get("PR_BODY", "") or ""
    changed = [f for f in git("diff", "--name-only", f"{base}...HEAD").split() if PAGE.match(f)]
    if not changed:
        print("No page files changed: no evidence needed.")
        return

    arabic_changed, new_pages = [], []
    for f in changed:
        old, new = file_at(base, f), file_at("HEAD", f)
        if old is None:
            new_pages.append(f)
        elif new is None or arabic_of(old) != arabic_of(new):
            arabic_changed.append(f)
    print(f"Page files changed: {len(changed)} "
          f"({len(new_pages)} new, {len(arabic_changed)} with changed Arabic)")
    for f in arabic_changed:
        print(f"  Arabic changed: {f}")

    problems = []
    if not VERIFIED.search(body):
        problems.append('Tick "I checked every changed line against the printed page myself" '
                        "in the pull request description.")
    if not AI_BOX.search(body):
        problems.append('Tick one of the "AI tools" boxes in the pull request description.')
    if arabic_changed:
        issues = sorted(set(FIXES.findall(body)), key=int)
        sources = [body] + issue_texts(issues)
        if not any(IMAGE.search(t) for t in sources):
            where = f" or in issue {', '.join('#' + n for n in issues)}" if issues else ""
            problems.append("This pull request changes Arabic in existing pages. Attach a photo of the "
                            f"printed page to the pull request description{where} "
                            "(drag the image into the text box), then save the description.")
    if problems:
        print("\nEvidence missing:")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print("Evidence present.")


if __name__ == "__main__":
    main()
