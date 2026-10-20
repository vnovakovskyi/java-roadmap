---
title: Module Project (Bookshelf with Collections)
area: Java APIs
module: 4
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Module Project (Bookshelf with Collections)

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** must · **Est:** 5h
> **Why this matters:** Version 3 of Bookshelf swaps hand-made arrays for the Collections Framework
> and adds proper error handling. Because the menu depends on the `BookStorage` interface, you'll
> replace the storage without rewriting the app — the payoff of Module 3.

## Learning Objectives
- Replace arrays with the right collections.
- Model fixed sets of values with enums and missing values with `Optional`.
- Handle errors with meaningful exceptions.

## Learn
- [ ] Revisit [[M4 - Java APIs - Collections Overview (List, Set, Map)]],
      [[M4 - Java APIs - Optional and Null-Safety]], and
      [[M4 - Java APIs - Exceptions and Error Handling]].

## Concepts
- [ ] Give each book a numeric `id`; `InMemoryBookStorage implements BookStorage` keeps a
      `Map<Long, Book>` (fast lookup by id) — `findAll()` now returns a `List<Book>`.
- [ ] `enum Genre` and `enum ReadingStatus { WANT_TO_READ, READING, FINISHED }` replace the old
      `boolean read`.
- [ ] `Optional<Book> findById(long id)`; the app turns an empty result into a friendly message.
- [ ] `BookNotFoundException` (unchecked) for "update a book that doesn't exist"; invalid input
      never crashes the app.
- [ ] List sorted by title or by author using comparators.
- [ ] Packages: `bookshelf.model`, `bookshelf.storage`, `bookshelf.app`.
- [ ] Optional: a `BigDecimal price` per book and the total value of your shelf.

## Practice
**Goal:** Bookshelf v3 — collections, enums, Optional, and exceptions.
**Steps:**
- [ ] Introduce ids, `Genre`, and `ReadingStatus`; update `Book`.
- [ ] Implement `InMemoryBookStorage` with a `Map` and switch the app over to it.
- [ ] Add `findById` with `Optional` and a "change status" command that uses it.
- [ ] Add sorting options and filtering by genre or status.
- [ ] Split the code into packages; commit, push, and tag `v3`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why key the storage by id in a `Map` instead of searching a `List`?
> Lookups by id become average `O(1)` instead of scanning every book — and ids stay stable even if
> titles change.

> [!question]- What happens when the user asks for an id that doesn't exist, and which class decides that?
> The storage returns `Optional.empty()`; the app (menu layer) decides how to tell the user. The
> storage doesn't print anything.

> [!question]- Which classes changed when you replaced the array storage, and which didn't?
> The new storage class, the line that creates it, and the spots that used `Book[]` changed; the
> menu logic itself, written against `BookStorage`, stayed the same.

## Definition of Done
- [ ] Bookshelf v3 uses collections, enums, `Optional`, and custom exceptions.
- [ ] Bad input and unknown ids are handled gracefully.
- [ ] The code is organized in packages and tagged `v3` on GitHub.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M5 - Modern Java - Lambdas and Functional Interfaces]]
