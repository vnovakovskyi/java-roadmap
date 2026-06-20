---
title: Records
area: Modern Java
module: 5
status: todo
priority: must
effort: 2
tags:
  - java-roadmap
---

# Records

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** must · **Est:** 2h
> **Why this matters:** Records (Java 16+) remove the boilerplate of data classes — no more
> hand-written getters, `equals`, `hashCode`, `toString`. You'll use them for DTOs and value objects.

## Learning Objectives
- Define a record and use its generated members.
- Know when a record fits (and when it doesn't).
- Add validation via a compact constructor.

## Learn
- [ ] Read: [dev.java — "Records"](https://dev.java/learn/records/).

## Concepts
- [ ] `record Point(int x, int y) {}` auto-generates a constructor, accessors (`x()`, `y()`),
      `equals`, `hashCode`, and `toString`.
- [ ] Records are **immutable** and `final`; they can't extend classes (but can implement interfaces).
- [ ] **Compact constructor** for validation: `public Point { if (x < 0) throw ...; }`.
- [ ] Great for DTOs, value objects, and method return groupings; not for mutable entities.
- [ ] Compare with the hand-written class from [[M3 - OOP - equals, hashCode and toString]] — same
      behavior, far less code.

## Practice
**Goal:** Replace a boilerplate class with a record.
**Steps:**
- [ ] Convert a small data class (e.g. `Money(amount, currency)`) to a record.
- [ ] Add validation in the compact constructor and test it rejects bad input.
- [ ] Put records in a `Set` and confirm value-based equality "just works".

## Definition of Done
- [ ] I can define records and use generated accessors/equals/toString.
- [ ] I can validate with a compact constructor.
- [ ] I know when a record is the right tool.

## Next
- Next: [[M5 - Modern Java - var, Enhanced switch and Text Blocks]]
