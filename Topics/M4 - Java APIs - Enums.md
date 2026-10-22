---
title: Enums
area: Java APIs
module: 4
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Enums

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** good · **Est:** 2h
> **Why this matters:** Enums model a fixed set of values (states, roles, days) safely — far better
> than loose strings or magic numbers. They're small, but they make code clearer everywhere.

## Learning Objectives
- Define and use an enum.
- Add fields and methods to an enum.
- Use enums in `switch` and as map keys.

## Learn
- [ ] Read: [dev.java — Enums](https://dev.java/learn/language/oop/classes-objects/enums/).

## Concepts
- [ ] `enum Status { ACTIVE, PAUSED, CLOSED }` — a type with a fixed set of constants.
- [ ] Enums can have fields, a constructor, and methods (e.g. `Planet` with mass and radius).
- [ ] Built-ins: `values()`, `name()`, `ordinal()`, `valueOf(String)`.
- [ ] Pair perfectly with `switch` expressions — the compiler checks you covered every constant.
- [ ] `EnumMap` and `EnumSet` are compact, fast collections for enum keys.
- [ ] Prefer enums over `String`/`int` constants — type-safe and self-documenting. Never store
      `ordinal()` anywhere: reordering the constants changes it.

## Practice
**Goal:** Replace magic values with an enum.
**Steps:**
- [ ] Define an `enum Day` and loop over `values()`.
- [ ] Add a field (e.g. `weekend`) with a constructor and a getter.
- [ ] Use the enum in a `switch` expression returning a label (no `default` needed when every
      constant is covered).
- [ ] Count tasks per status with an `EnumMap<Status, Integer>`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why use an enum instead of `String` constants like `"ACTIVE"`?
> The compiler only allows valid values, typos can't compile, IDEs autocomplete them, and `switch`
> can check you handled every case.

> [!question]- Can an enum have fields and methods?
> Yes — each constant can carry data passed to a constructor, and the enum can define methods (even
> abstract ones each constant implements).

> [!question]- What does `Status.valueOf("active")` do when the constant is `ACTIVE`?
> Throws `IllegalArgumentException` — `valueOf` is case-sensitive and must match the constant name
> exactly.

> [!question]- Why shouldn't you persist `ordinal()`?
> It's the constant's position; adding or reordering constants changes it and corrupts stored data.
> Store `name()` instead.

## Definition of Done
- [ ] I can define enums with fields and methods.
- [ ] I can use them in `switch` and collections.
- [ ] I reach for an enum instead of magic strings or numbers.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M4 - Java APIs - Optional and Null-Safety]]
