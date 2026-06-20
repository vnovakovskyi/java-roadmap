---
title: Lambdas and Functional Interfaces
area: Modern Java
module: 5
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Lambdas and Functional Interfaces

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** must · **Est:** 4h
> **Why this matters:** Lambdas let you pass behavior as data — the foundation of the Streams API and
> most modern Java. They make code shorter and more expressive once they click.

## Learning Objectives
- Write lambda expressions and method references.
- Use the standard functional interfaces.
- Explain what makes an interface "functional".

## Learn
- [ ] Read: [dev.java — "Lambda Expressions"](https://dev.java/learn/lambdas/).
- [ ] Read about `java.util.function` (`Function`, `Predicate`, `Consumer`, `Supplier`).

## Concepts
- [ ] A **functional interface** has exactly one abstract method (`@FunctionalInterface`); a lambda
      is a concise implementation of it.
- [ ] Syntax: `(a, b) -> a + b`; single expression returns implicitly, blocks use `{ return ...; }`.
- [ ] Standard types: `Predicate<T>` (T→boolean), `Function<T,R>`, `Consumer<T>`, `Supplier<T>`,
      `BiFunction`.
- [ ] **Method references**: `String::toUpperCase`, `System.out::println`, `Person::new`.
- [ ] Lambdas can capture effectively-final local variables.

## Practice
**Goal:** Replace boilerplate with lambdas.
**Steps:**
- [ ] Sort a list with a `Comparator` lambda, then with a method reference.
- [ ] Use `Predicate` to filter a list and `Consumer` with `forEach` to print it.
- [ ] Write your own `@FunctionalInterface` and implement it with a lambda.

## Definition of Done
- [ ] I can write lambdas and method references.
- [ ] I can use the standard functional interfaces.
- [ ] I can explain what a functional interface is.

## Next
- Next: [[M5 - Modern Java - The Streams API]]
