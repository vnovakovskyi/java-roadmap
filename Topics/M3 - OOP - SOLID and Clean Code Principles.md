---
title: SOLID and Clean Code Principles
area: OOP
module: 3
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# SOLID and Clean Code Principles

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** good · **Est:** 3h
> **Why this matters:** Knowing the syntax of OOP isn't the same as using it well. SOLID and a few
> clean-code habits are how you write classes that are easy to change and test — and they're a very
> common junior interview topic.

## Learning Objectives
- Explain each SOLID principle in plain terms with a small example.
- Apply DRY, KISS, and YAGNI when writing code.
- Recognize common "code smells" and refactor them.

## Learn
- [ ] Read a beginner-friendly SOLID overview (e.g. the Baeldung "SOLID Principles" article).
- [ ] Skim *Clean Code* (Robert C. Martin) chapters on naming and functions, or a good summary.

## Concepts
- [ ] **S**ingle Responsibility — a class should have one reason to change.
- [ ] **O**pen/Closed — open for extension, closed for modification (add behavior without editing
      existing code; interfaces help).
- [ ] **L**iskov Substitution — a subtype must be usable wherever its base type is expected.
- [ ] **I**nterface Segregation — many small, focused interfaces beat one fat one.
- [ ] **D**ependency Inversion — depend on abstractions, not concretions (sets up Spring's DI in M9).
- [ ] **DRY / KISS / YAGNI** — don't repeat yourself, keep it simple, don't build what you don't need yet.
- [ ] Clean-code basics: clear names, small functions that do one thing, few parameters, no dead code.

## Practice
**Goal:** Improve real code with the principles.
**Steps:**
- [ ] Take a class that does two jobs and split it (Single Responsibility).
- [ ] Replace a hard-coded dependency with an interface so a new variant needs no edits (Open/Closed +
      Dependency Inversion) — reuse [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]].
- [ ] Find one duplicated block and remove the duplication (DRY); rename two unclear names.

**Record your result:**
- 

## Definition of Done
- [ ] I can explain all five SOLID letters with an example.
- [ ] I applied at least two principles in a refactor.
- [ ] I can name a few code smells and how to fix them.

## Cheatsheet (my notes)
- 

## Related
- [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]]
- [[M7 - Testing - Writing Testable Code (Intro to TDD)]]
- [[M9 - Spring - Services and Dependency Injection]]
