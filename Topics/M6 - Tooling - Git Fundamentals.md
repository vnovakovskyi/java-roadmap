---
title: Git Fundamentals
area: Tooling
module: 6
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Git Fundamentals

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** must · **Est:** 4h
> **Why this matters:** Git is non-negotiable. Every team uses it, every job expects it, and it's how
> you save, branch, and recover your work safely. Learn the core model, not just memorized commands.

## Learning Objectives
- Initialize a repo, stage, commit, and view history.
- Work with branches and merge them.
- Undo mistakes safely.

## Learn
- [ ] Read: [Pro Git, ch. 1–3](https://git-scm.com/book/en/v2) (free).
- [ ] Do an interactive tutorial (e.g. the "Learn Git Branching" visual game).

## Concepts
- [ ] Three areas: **working directory → staging (index) → repository**. `add` stages, `commit` records.
- [ ] A commit is a snapshot + parent; **branches** are movable pointers to commits.
- [ ] Core loop: `git status`, `git add`, `git commit -m`, `git log`.
- [ ] Branching: `git switch -c feature`, `git merge`, resolving conflicts.
- [ ] Undo: `git restore` (discard changes), `git revert` (safe undo of a commit), and what *not* to
      do on shared history.
- [ ] A `.gitignore` keeps build output and secrets out of the repo.

## Practice
**Goal:** Run a realistic Git workflow locally.
**Steps:**
- [ ] `git init` a small Java project; commit it; make 3–4 commits and read `git log`.
- [ ] Create a branch, change code, merge it back to `main`.
- [ ] Deliberately create a merge conflict and resolve it.

**Record your result:**
- 

## Definition of Done
- [ ] I can stage, commit, branch, and merge confidently.
- [ ] I can resolve a merge conflict.
- [ ] I can undo changes safely with restore/revert.

## Cheatsheet (my notes)
- 

## Related
- [[Tools & Setup]]
- [[M6 - Tooling - GitHub and Pull Requests]]
