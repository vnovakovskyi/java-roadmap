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
- [ ] Read: [dev.java — Introducing Generics](https://dev.java/learn/language/fp/generics/intro/).
- [ ] Skim: [dev.java — Wildcards](https://dev.java/learn/language/fp/generics/wildcards/) and
      [Type Erasure](https://dev.java/learn/language/fp/generics/type-erasure/) — recognize them;
      mastery comes later.

## Concepts
- [ ] A **type parameter** (`<T>`) is a placeholder filled at the use site: `Box<String>`.
- [ ] Generics are compile-time: the compiler enforces types, then **erases** them — so no casts and
      no `ClassCastException` from misuse.
- [ ] Common letters: `T` type, `E` element, `K`/`V` key/value.
- [ ] **Bounded** types: `<T extends Number>` restricts what `T` can be.
- [ ] Generics work with reference types only — `List<Integer>`, never `List<int>` (autoboxing
      bridges the gap).
- [ ] Wildcards (`? extends`, `? super`) exist for flexible APIs — recognize them; deep mastery
      later.

## Practice
**Goal:** Write your own generic.
**Steps:**
- [ ] Write a generic `Box<T>` with `set(T)` / `T get()`; use it with `String` and `Integer`.
- [ ] Write a generic method `<T> T firstOf(List<T> list)`.
- [ ] Write `<T extends Comparable<T>> T maxOf(List<T> list)` and use it with numbers and strings.
- [ ] Try assigning the wrong type into a `List<String>` and read the compile error.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why use `List<String>` instead of a raw `List`?
> The compiler checks every element is a `String` — no casts, and type mistakes become compile
> errors instead of runtime `ClassCastException`s.

> [!question]- What is type erasure?
> Generic type information exists only at compile time. At runtime `List<String>` and
> `List<Integer>` are both just `List`, so you can't do `new T()` or `instanceof List<String>`.

> [!question]- What does `<T extends Number>` mean?
> `T` may be `Number` or any subtype (`Integer`, `Double`, …), so you can call `Number` methods like
> `doubleValue()` on it.

> [!question]- Why can't you write `List<int>`?
> Type parameters must be reference types. Use `List<Integer>`; autoboxing converts between `int`
> and `Integer`.

## Definition of Done
- [ ] I can use generic collections fluently.
- [ ] I can write a basic generic class and method.
- [ ] I can explain how generics catch errors at compile time.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M4 - Java APIs - Iteration and Sorting (Comparable and Comparator)]]
