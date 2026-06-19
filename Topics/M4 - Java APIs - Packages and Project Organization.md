---
title: Packages and Project Organization
area: Java APIs
module: 4
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Packages and Project Organization

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** good · **Est:** 2h
> **Why this matters:** As programs grow past one file, you need structure. Packages and a sensible
> layout keep code navigable — and they're exactly what build tools (Module 6) expect.

## Learning Objectives
- Organize classes into packages and use `import`.
- Understand the standard Maven/Gradle source layout.
- Apply basic structuring conventions (by feature vs by layer).

## Learn
- [ ] Read: [dev.java — "Packages"](https://dev.java/learn/).
- [ ] Skim the standard `src/main/java` project layout (preview of Module 6).

## Concepts
- [ ] A **package** is a namespace: `package com.example.app;` maps to folders `com/example/app/`.
- [ ] `import` brings in classes from other packages; same-package classes need no import.
- [ ] Reverse-domain naming (`com.yourname.project`) avoids clashes.
- [ ] Standard layout: source in `src/main/java`, tests in `src/test/java`, resources in
      `src/main/resources`.
- [ ] Organize **by feature** (e.g. `orders`, `users`) or **by layer** (`controller`, `service`,
      `repository`); be consistent.

## Practice
**Goal:** Split a one-file program into packages.
**Steps:**
- [ ] Move classes into 2–3 packages with proper `package`/`import` statements.
- [ ] Recreate the `src/main/java/...` folder structure.
- [ ] Make a class package-private and confirm it isn't visible from another package.

**Record your result:**
- 

## Definition of Done
- [ ] I can create packages and import across them.
- [ ] I know the standard source/test/resources layout.
- [ ] I can argue for a by-feature or by-layer structure.

## Cheatsheet (my notes)
- 

## Related
- [[M3 - OOP - Encapsulation and Access Modifiers]]
- [[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]]
