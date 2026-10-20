---
title: Optional and Null-Safety
area: Java APIs
module: 4
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Optional and Null-Safety

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** must · **Est:** 3h
> **Why this matters:** `NullPointerException` is the most common Java runtime error. `Optional` and
> good null habits turn "it crashed" into "I handled the missing case on purpose".

## Learning Objectives
- Explain why `null` is dangerous and how to minimize it.
- Use `Optional` to represent "maybe a value".
- Apply defensive null habits.

## Learn
- [ ] Read:
      [dev.java — Using Optionals](https://dev.java/learn/api/collections-and-streams/streams/optionals/).
- [ ] Reference: the
      [`Optional` Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Optional.html)
      (the API note at the top is the best usage advice).

## Concepts
- [ ] `null` means absence; dereferencing it throws NPE. Avoid returning `null` from methods.
- [ ] `Optional<T>` makes "no value" explicit in the type. Create with `Optional.of`, `ofNullable`,
      `empty`.
- [ ] Consume with `orElse(default)`, `orElseThrow()`, `isPresent()`/`isEmpty()`. `map`,
      `ifPresent`, and `orElseGet` take a lambda — you'll use them freely after Module 5.
- [ ] Use `Optional` mainly for **return types**; don't use it for fields, parameters, or
      collections (return an empty list instead).
- [ ] Other guards: `Objects.requireNonNull(arg, "arg")` at the start of a method; returning empty
      collections instead of `null`.

## Practice
**Goal:** Eliminate a null bug with `Optional`.
**Steps:**
- [ ] Write `Optional<User> findByName(String)` over a small map; return `Optional.empty()` when
      missing.
- [ ] At the call site, use `orElseThrow()` and `orElse(...)` instead of null checks.
- [ ] Reproduce an NPE from returning `null`, then fix it with `Optional`.
- [ ] Add `Objects.requireNonNull` to a constructor and see the clearer error message.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why return `Optional<User>` instead of a possibly-null `User`?
> The type itself tells callers the value may be missing, and the API pushes them to handle that
> case instead of forgetting a null check.

> [!question]- What does `Optional.of(null)` do?
> Throws a `NullPointerException`. Use `Optional.ofNullable(value)` when the value might be null.

> [!question]- Where shouldn't you use `Optional`?
> Fields, method parameters, and collections (return an empty collection instead). It's designed for
> return values.

> [!question]- What's wrong with `optional.get()` without checking?
> It throws `NoSuchElementException` when empty — no better than an NPE. Prefer `orElse`,
> `orElseThrow`, or `ifPresent`.

## Definition of Done
- [ ] I can use `Optional` idiomatically (no unchecked `.get()`).
- [ ] I avoid returning `null` and guard inputs.
- [ ] I can explain when *not* to use `Optional`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M4 - Java APIs - Packages and Project Organization]]
