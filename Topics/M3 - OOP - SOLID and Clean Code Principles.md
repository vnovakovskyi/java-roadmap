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
- [ ] Read:
      [Baeldung — A Solid Guide to SOLID Principles](https://www.baeldung.com/solid-principles).
- [ ] Browse: [Refactoring.Guru — Code Smells](https://refactoring.guru/refactoring/smells) (start
      with Long Method, Large Class, Duplicate Code).
- [ ] Reference: [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) —
      naming and formatting conventions most teams follow.
- [ ] Optional: *Clean Code* (Robert C. Martin) chapters on naming and functions.

## Concepts
- [ ] **S**ingle Responsibility — a class should have one reason to change.
- [ ] **O**pen/Closed — open for extension, closed for modification (add behavior without editing
      existing code; interfaces help).
- [ ] **L**iskov Substitution — a subtype must be usable wherever its base type is expected.
- [ ] **I**nterface Segregation — many small, focused interfaces beat one fat one.
- [ ] **D**ependency Inversion — depend on abstractions, not concretions (sets up Spring's DI in
      Module 9).
- [ ] **DRY / KISS / YAGNI** — don't repeat yourself, keep it simple, don't build what you don't
      need yet.
- [ ] Clean-code basics: clear names, small methods that do one thing, few parameters, no magic
      numbers, no dead code.

## Practice
**Goal:** Improve real code with the principles.
**Steps:**
- [ ] Take a class that does two jobs and split it (Single Responsibility).
- [ ] Replace a hard-coded dependency with an interface so a new variant needs no edits (Open/Closed
      + Dependency Inversion) — reuse [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]].
- [ ] Find one duplicated block and remove the duplication (DRY); rename two unclear names and
      replace a magic number with a named constant.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Explain the Single Responsibility Principle with an example.
> A class should have one reason to change. `InvoicePrinter` formats invoices; it shouldn't also
> calculate tax and save to the database — split those into separate classes.

> [!question]- Give a classic Liskov Substitution violation.
> `Square extends Rectangle`: setting a square's width also changes its height, so code that expects
> independent width and height breaks when handed a `Square`.

> [!question]- How does Dependency Inversion relate to Spring?
> High-level code depends on interfaces, and the concrete implementation is supplied from outside.
> Spring's dependency injection automates exactly that wiring.

> [!question]- Name three code smells.
> Long method, large class, duplicated code (also: magic numbers, long parameter lists, unclear
> names).

## Definition of Done
- [ ] I can explain all five SOLID letters with an example.
- [ ] I applied at least two principles in a refactor.
- [ ] I can name a few code smells and how to fix them.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M3 - OOP - Module Project (Bookshelf with Classes)]]
