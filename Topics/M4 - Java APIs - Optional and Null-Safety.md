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
- [ ] Read the `Optional` Javadoc and a short "Optional best practices" article (Baeldung).

## Concepts
- [ ] `null` means absence; dereferencing it throws NPE. Avoid returning `null` from methods.
- [ ] `Optional<T>` makes "no value" explicit in the type. Create with `Optional.of`, `ofNullable`,
      `empty`.
- [ ] Consume with `isPresent`/`get` (avoid), better: `orElse`, `orElseGet`, `orElseThrow`, `map`,
      `ifPresent`.
- [ ] Use `Optional` mainly for **return types**; don't use it for fields or parameters.
- [ ] Other guards: `Objects.requireNonNull`, returning empty collections instead of `null`.

## Practice
**Goal:** Eliminate a null bug with `Optional`.
**Steps:**
- [ ] Write `Optional<User> findByName(String)` over a small map; return `empty()` when missing.
- [ ] Use `orElseThrow` and `map` at the call site instead of null checks.
- [ ] Reproduce an NPE from returning `null`, then fix it with `Optional`.

**Record your result:**
- 

## Definition of Done
- [ ] I can use `Optional` idiomatically (no `.get()` without checking).
- [ ] I avoid returning `null` and guard inputs.
- [ ] I can explain when *not* to use `Optional`.

## Cheatsheet (my notes)
- 

## Related
- [[M4 - Java APIs - Exceptions and Error Handling]]
- [[M5 - Modern Java - The Streams API]]
