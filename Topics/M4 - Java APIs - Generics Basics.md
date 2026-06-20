---
title: Generics Basics
area: Java APIs
module: 4
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Generics Basics

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** must · **Est:** 4h
> **Why this matters:** Generics give you type safety without casting — `List<String>` instead of a
> raw `List`. You consume them constantly (collections) and will eventually write your own.

## Learning Objectives
- Read and use generic types like `List<T>`, `Map<K,V>`.
- Write a simple generic class and method.
- Explain why generics prevent a whole class of runtime errors.

## Learn
- [ ] Read: [dev.java — "Generics"](https://dev.java/learn/generics/).
- [ ] Read about type parameters and the diamond operator `<>`.

## Concepts
- [ ] A **type parameter** (`<T>`) is a placeholder filled at use site: `Box<String>`.
- [ ] Generics are compile-time: the compiler enforces types, then "erases" them — so no casts and no
      `ClassCastException` from misuse.
- [ ] Common letters: `T` type, `E` element, `K`/`V` key/value.
- [ ] **Bounded** types: `<T extends Number>` restricts what `T` can be.
- [ ] Wildcards (`? extends`, `? super`) exist for flexible APIs — recognize them; deep mastery later.

## Practice
**Goal:** Write your own generic.
**Steps:**
- [ ] Write a generic `Box<T>` with `set(T)` / `T get()`; use it with `String` and `Integer`.
- [ ] Write a generic method `<T> T firstOf(List<T> list)`.
- [ ] Try assigning the wrong type into a `List<String>` and read the compile error.

## Definition of Done
- [ ] I can use generic collections fluently.
- [ ] I can write a basic generic class and method.
- [ ] I can explain how generics catch errors at compile time.

## Next
- Next: [[M4 - Java APIs - Iteration and Sorting (Comparable and Comparator)]]
