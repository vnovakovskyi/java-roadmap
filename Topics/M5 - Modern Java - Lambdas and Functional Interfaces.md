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
> **Why this matters:** Lambdas let you pass behavior as data — the foundation of the Streams API
> and most modern Java. They make code shorter and more expressive once they click.

## Learning Objectives
- Write lambda expressions and method references.
- Use the standard functional interfaces.
- Explain what makes an interface "functional".

## Learn
- [ ] Read:
      [dev.java — Writing Your First Lambda Expression](https://dev.java/learn/language/fp/lambdas/first-lambdas/)
      and
      [Using Lambda Expressions in Your Application](https://dev.java/learn/language/fp/lambdas/functional-interfaces/).
- [ ] Read:
      [dev.java — Writing Lambda Expressions as Method References](https://dev.java/learn/language/fp/lambdas/method-references/).
- [ ] Read:
      [dev.java — Writing and Combining Comparators](https://dev.java/learn/language/fp/lambdas/writing-comparators/).

## Concepts
- [ ] A **functional interface** has exactly one abstract method (`@FunctionalInterface`); a lambda
      is a concise implementation of it — it replaces most anonymous classes.
- [ ] Syntax: `(a, b) -> a + b`; a single expression returns implicitly, blocks use
      `{ return ...; }`.
- [ ] Standard types in `java.util.function`: `Predicate<T>` (T → boolean), `Function<T,R>`,
      `Consumer<T>`, `Supplier<T>`, `BiFunction`, `UnaryOperator`.
- [ ] **Method references**: `String::toUpperCase`, `System.out::println`, `Person::new`,
      `Person::age`.
- [ ] Lambdas can capture **effectively final** local variables only.
- [ ] Where you'll use them daily: `Comparator.comparing(Person::age).thenComparing(Person::name)`,
      `list.removeIf(...)`, `map.computeIfAbsent(...)`, `optional.map(...)`, and streams.

## Practice
**Goal:** Replace boilerplate with lambdas.
**Steps:**
- [ ] Take the `ByAge` comparator class from Module 4 and rewrite it as an anonymous class, a
      lambda, and finally `Comparator.comparing(Person::age)`.
- [ ] Use a `Predicate` with `removeIf` to drop minors, and `forEach(System.out::println)` to print.
- [ ] Count word lengths into a map with `computeIfAbsent` or `merge`.
- [ ] Write your own `@FunctionalInterface` (e.g. `Discount`) and implement it with two lambdas.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What is a functional interface?
> An interface with exactly one abstract method (default and static methods don't count). Any lambda
> or method reference with a matching shape can implement it.

> [!question]- Rewrite `(s) -> s.toUpperCase()` as a method reference.
> `String::toUpperCase`.

> [!question]- Why doesn't `int count = 0; list.forEach(x -> count++);` compile?
> Lambdas can only capture effectively final locals, and `count++` modifies one. Use a stream
> (`list.size()`, `count()`), a loop, or an `AtomicInteger`.

> [!question]- Match the interface to its shape: `Predicate`, `Function`, `Consumer`, `Supplier`.
> `Predicate<T>`: T → boolean. `Function<T,R>`: T → R. `Consumer<T>`: T → nothing. `Supplier<T>`:
> nothing → T.

## Definition of Done
- [ ] I can write lambdas and method references.
- [ ] I can use the standard functional interfaces.
- [ ] I can explain what a functional interface is.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M5 - Modern Java - The Streams API]]
