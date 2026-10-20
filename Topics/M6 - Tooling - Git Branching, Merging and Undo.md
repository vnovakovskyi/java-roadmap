---
title: Git Branching, Merging and Undo
area: Tooling
module: 6
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Git Branching, Merging and Undo

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** must · **Est:** 4h
> **Why this matters:** In Module 1 you committed straight to `main`. Teams don't: every change
> happens on a branch, gets reviewed, and is merged. Branching, resolving conflicts, and safely
> undoing mistakes are daily skills — and the core of most Git interview questions.

## Learning Objectives
- Work with branches and merge them.
- Resolve merge conflicts.
- Undo mistakes safely — and know which undo is safe on shared history.

## Learn
- [ ] Read:
      [Pro Git — Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
      (and the next section, "Basic Branching and Merging").
- [ ] Read: [Pro Git — Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things).
- [ ] Do: [Learn Git Branching](https://learngitbranching.js.org/) — the "Introduction Sequence" and
      "Ramping Up" levels.
- [ ] Bookmark: [Oh Shit, Git!?!](https://ohshitgit.com/) — plain-English fixes for common Git
      messes.

## Concepts
- [ ] A commit is a snapshot + a pointer to its parent; a **branch** is just a movable pointer to a
      commit, and `HEAD` marks where you are.
- [ ] `git switch -c feature` creates and switches; `git merge feature` brings it back — a
      **fast-forward** if `main` hasn't moved, otherwise a merge commit.
- [ ] **Conflicts** happen when both sides changed the same lines: edit the file to the result you
      want, remove the `<<<<<<<`/`>>>>>>>` markers, `git add`, commit.
- [ ] Undo, from safest to most dangerous: `git restore <file>` (discard local edits),
      `git restore --staged` (unstage), `git commit --amend` (fix the last local commit),
      `git revert <sha>` (a new commit that undoes an old one — safe on shared branches),
      `git reset` (moves the branch — local history only; `--hard` throws work away).
- [ ] `git stash` parks unfinished work; `git log --oneline --graph --all` shows the picture.
- [ ] `git rebase` replays your commits on top of another branch for a linear history — never rebase
      commits others have already pulled.

## Practice
**Goal:** Run a realistic branching workflow locally.
**Steps:**
- [ ] Create a branch, commit a change, and merge it back to `main` (fast-forward).
- [ ] Make different commits on `main` and on a branch, merge, and inspect the graph.
- [ ] Deliberately create a merge conflict and resolve it.
- [ ] Revert a commit; amend a commit message; stash and restore unfinished work.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What is a Git branch, technically?
> A lightweight, movable pointer to a commit. Creating one is instant; new commits move the pointer
> forward.

> [!question]- `git revert` vs `git reset` — which is safe on a shared branch?
> `revert` — it adds a new commit that undoes an old one, so history stays intact for everyone.
> `reset` rewrites history and should only be used on commits nobody else has.

> [!question]- What's a fast-forward merge?
> When the target branch hasn't moved since you branched off, Git simply moves its pointer forward
> to your commits — no merge commit needed.

> [!question]- How do you resolve a merge conflict?
> Open the conflicted files, edit them to the intended result, delete the conflict markers,
> `git add` them, and commit (or continue the merge).

## Definition of Done
- [ ] I can branch, merge, and read the commit graph.
- [ ] I can resolve a merge conflict.
- [ ] I can undo changes safely and know which commands rewrite history.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M6 - Tooling - GitHub and Pull Requests]]
