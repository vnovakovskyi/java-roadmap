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
> than loose strings or magic numbers. They're small but they make code clearer everywhere.

## Learning Objectives
- Define and use an enum.
- Add fields and methods to an enum.
- Use enums in `switch` and as map keys.

## Learn
- [ ] Read: [dev.java — "Enums"](https://dev.java/learn/) and the `enum` Javadoc notes.

## Concepts
- [ ] `enum Status { ACTIVE, PAUSED, CLOSED }` — a type with a fixed set of constants.
- [ ] Enums can have fields, a constructor, and methods (e.g. `Planet` with mass/radius).
- [ ] Built-ins: `values()`, `name()`, `ordinal()`, `valueOf(String)`.
- [ ] Pair perfectly with modern `switch` (the compiler can warn on missing cases).
- [ ] Prefer enums over `String`/`int` constants — type-safe and self-documenting.

## Practice
**Goal:** Replace magic values with an enum.
**Steps:**
- [ ] Define an `enum Day` and loop over `values()`.
- [ ] Add a field (e.g. `isWeekend`) with a constructor and a getter.
- [ ] Use the enum in a `switch` expression returning a label.

**Record your result:**
- 

## Definition of Done
- [ ] I can define enums with fields/methods.
- [ ] I can use them in switch and collections.
- [ ] I reach for an enum instead of magic strings/numbers.

## Cheatsheet (my notes)
- 

## Related
- [[M2 - Core Java - Conditionals (if and switch)]]
- [[M4 - Java APIs - Collections Overview (List, Set, Map)]]
