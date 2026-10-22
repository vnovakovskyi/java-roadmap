---
title: Module Project (Bookshelf with Classes)
area: OOP
module: 3
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Module Project (Bookshelf with Classes)

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 5h
> **Why this matters:** Version 2 of Bookshelf replaces parallel arrays with real objects. You'll
> feel why OOP exists: data and behavior live together, and an interface lets you swap how books are
> stored — which pays off in Module 8, when the storage becomes a database.

## Learning Objectives
- Turn a procedural program into collaborating classes.
- Encapsulate data and validate it in one place.
- Depend on an interface so the storage can be replaced later.

## Learn
- [ ] Revisit [[M3 - OOP - Encapsulation and Access Modifiers]] and
      [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]].
- [ ] Look back at your `v1` code and list everything that belongs to "a book".

## Concepts
- [ ] `Book` class: private fields (`title`, `author`, `read`), a constructor that rejects blank
      values (`throw new IllegalArgumentException("Title is required")`), `markAsRead()`, and
      `equals`/`hashCode`/`toString` based on title + author.
- [ ] `BookStorage` interface: `add(Book)`, `findAll()`, `findByTitle(String)` — returning `Book[]`
      for now.
- [ ] `ArrayBookStorage implements BookStorage`: an array plus a count that **grows** when full
      (`Arrays.copyOf` to double the size) — no more fixed capacity. That's what `ArrayList` does
      inside.
- [ ] The menu code (`BookshelfApp`) depends only on `BookStorage`, never on `ArrayBookStorage` —
      program to an interface.
- [ ] Optional: an `EBook extends Book` with a file size that overrides `toString`.

## Practice
**Goal:** Bookshelf v2 — same features, object-oriented design.
**Steps:**
- [ ] Create `Book` with validation and the three `Object` methods.
- [ ] Define `BookStorage` and implement `ArrayBookStorage` with a growing array.
- [ ] Rewrite the menu to use `BookStorage`; refuse duplicates using `equals`.
- [ ] Check every field and method: does it need to be `public`?
- [ ] Commit, push, and tag `v2`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why does the menu depend on `BookStorage` instead of `ArrayBookStorage`?
> So the storage can be replaced — by a collection-based one in Module 4, a database in Module 8, or
> a fake in tests — without touching the menu code.

> [!question]- How does your storage grow, and which standard class works the same way?
> When the array is full, it's copied into one twice as big with `Arrays.copyOf`. `ArrayList` does
> exactly this internally.

> [!question]- Where is "a book must have a title" enforced, and why there?
> In the `Book` constructor — the one place every book passes through — so an invalid `Book` can
> never exist.

## Definition of Done
- [ ] Bookshelf v2 works like v1 but is built from `Book`, `BookStorage`, and an implementation.
- [ ] Invalid books can't be created.
- [ ] The code is on GitHub, tagged `v2`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M4 - Java APIs - Wrapper Types, Autoboxing and BigDecimal]]
