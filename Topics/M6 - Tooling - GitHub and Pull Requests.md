---
title: GitHub and Pull Requests
area: Tooling
module: 6
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# GitHub and Pull Requests

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** must · **Est:** 3h
> **Why this matters:** GitHub is where your code lives publicly and where teams collaborate. A clean
> profile with real projects is part of your résumé; the pull-request flow is how professional teams ship.

## Learning Objectives
- Push a local repo to GitHub and clone repos.
- Use the fork / branch / pull-request workflow.
- Write good commit messages and PR descriptions.

## Learn
- [ ] Read GitHub's "Hello World" and "About pull requests" guides.
- [ ] Read about SSH vs HTTPS auth and the remote (`origin`).

## Concepts
- [ ] **Remote**: a hosted copy (`origin`). `git push`/`git pull` sync with it.
- [ ] Typical flow: branch → commit → `push` → open a **pull request** → review → merge.
- [ ] A PR bundles a change for review: title, description, diff, discussion.
- [ ] Good commit messages: imperative summary line + why in the body.
- [ ] README, license, and a tidy commit history make a repo look professional.

## Practice
**Goal:** Ship a change via a pull request.
**Steps:**
- [ ] Create a GitHub repo and push one of your practice projects.
- [ ] Make a change on a branch, push it, and open a PR against `main`.
- [ ] Merge the PR; pull `main` locally to sync.

## Definition of Done
- [ ] I can push/clone and work with a remote.
- [ ] I can open and merge a pull request.
- [ ] I write clear commit and PR messages.

## Next
- Next: [[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]]
