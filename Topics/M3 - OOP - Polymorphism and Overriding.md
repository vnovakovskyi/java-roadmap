---
title: Polymorphism and Overriding
area: OOP
module: 3
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Polymorphism and Overriding

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 4h
> **Why this matters:** Polymorphism — treating different types through a common interface — is what
> makes OOP flexible and testable. It's how frameworks like Spring let you swap implementations.

## Learning Objectives
- Override methods correctly and use `@Override`.
- Explain dynamic dispatch (which method actually runs).
- Use a supertype reference to hold different subtype objects.

## Learn
- [ ] Read: [dev.java — "Polymorphism"](https://dev.java/learn/inheritance/).
- [ ] Read about `@Override`, method overriding vs overloading.

## Concepts
- [ ] **Overriding**: a subclass redefines a parent method (same signature). Mark it `@Override` so the
      compiler checks you.
- [ ] **Dynamic dispatch**: the *runtime* type decides which override runs, even via a supertype variable.
- [ ] Overriding (runtime, same signature) ≠ overloading (compile-time, different parameters).
- [ ] A `List<Animal>` can hold `Dog`s and `Cat`s and call `speak()` polymorphically.
- [ ] Program to the abstraction (supertype), not the concrete class — easier to extend and test.

## Practice
**Goal:** See dynamic dispatch in action.
**Steps:**
- [ ] Put several `Animal` subclasses in a `List<Animal>` and loop calling `speak()`.
- [ ] Add `@Override` and then deliberately mistype a method name to see the compiler catch it.
- [ ] Write a method that accepts an `Animal` and works for any subclass.

**Record your result:**
- 

## Definition of Done
- [ ] I can override methods with `@Override` and explain dynamic dispatch.
- [ ] I can distinguish overriding from overloading.
- [ ] I can write code against a supertype that works for any subtype.

## Cheatsheet (my notes)
- 

## Related
- [[M3 - OOP - Inheritance]]
- [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]]
