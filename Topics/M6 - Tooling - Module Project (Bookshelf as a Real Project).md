---
title: Module Project (Bookshelf as a Real Project)
area: Tooling
module: 6
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Module Project (Bookshelf as a Real Project)

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** must · **Est:** 4h
> **Why this matters:** Version 5 turns Bookshelf from "a folder of .java files" into a professional
> project: a build tool, a real dependency from Maven Central, a branch-and-PR workflow, and a CI
> pipeline that checks every change.

## Learning Objectives
- Migrate an existing app to Maven (or Gradle).
- Add and use a third-party dependency.
- Work through branches, pull requests, and CI — even on a solo project.

## Learn
- [ ] Revisit [[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]] and
      [[M6 - Tooling - Continuous Integration with GitHub Actions]].
- [ ] Read: the [Jackson project](https://github.com/FasterXML/jackson) README — the standard Java
      JSON library.

## Concepts
- [ ] Standard layout (`src/main/java/bookshelf/...`), `maven.compiler.release` 25, and the wrapper.
- [ ] Your first real dependency: switch storage from CSV to JSON with **Jackson 3**
      (`tools.jackson.core:jackson-databind`). It maps records — including `LocalDate` fields — to
      JSON and back.
- [ ] Run the app with `./mvnw exec:java -Dexec.mainClass=bookshelf.app.BookshelfApp` (Gradle: the
      `application` plugin and `./gradlew run`) or from the IDE.
- [ ] Workflow: do the migration on a branch, open a PR, let CI go green, then merge — the same loop
      you'll use at work.
- [ ] README: what the app does, how to build, run, and test it, plus the CI badge.

## Practice
**Goal:** Bookshelf v5 — a buildable, CI-checked project with a real dependency.
**Steps:**
- [ ] On a branch, move the code into a Maven (or Gradle) project with the standard layout and the
      wrapper.
- [ ] Add Jackson and save/load the books as JSON (optionally keep importing the old CSV once).
- [ ] Add the CI workflow; open the PR and merge it only when the build is green.
- [ ] Write the README; commit, push, and tag `v5`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What did the build tool give you that plain `javac` didn't?
> Dependency download and versioning, a standard layout, a repeatable one-command build, test
> running, packaging, and easy CI integration.

> [!question]- Where does Jackson come from, and how does your build find it?
> From Maven Central. The build tool downloads it (and its own dependencies) into the local cache
> and puts it on the classpath.

> [!question]- What does CI check on every pull request?
> That the project compiles and its tests pass (`./mvnw -B verify`) on a clean machine.

## Definition of Done
- [ ] Bookshelf builds with `./mvnw` (or `./gradlew`) from a fresh clone.
- [ ] It saves its data as JSON through Jackson.
- [ ] CI runs on every PR; the code is tagged `v5`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M7 - Testing - Why We Test and the Test Pyramid]]
