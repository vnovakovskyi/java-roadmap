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
> **Why this matters:** Polymorphism — treating different types through a common supertype — is what
> makes OOP flexible and testable. It's how frameworks like Spring let you swap implementations.

## Learning Objectives
- Override methods correctly and use `@Override`.
- Explain dynamic dispatch (which method actually runs).
- Use a supertype reference to hold different subtype objects.

## Learn
- [ ] Read:
      [dev.java — Polymorphism](https://dev.java/learn/language/oop/inheritance/polymorphism/).
- [ ] Read:
      [dev.java — Overriding and Hiding Methods](https://dev.java/learn/language/oop/inheritance/overriding/).

## Concepts
- [ ] **Overriding**: a subclass redefines a parent method (same signature). Mark it `@Override` so
      the compiler checks you.
- [ ] **Dynamic dispatch**: the *runtime* type of the object decides which override runs, even
      through a supertype variable.
- [ ] Overriding (runtime, same signature) ≠ overloading (compile-time, different parameters).
- [ ] An `Animal[]` (or, in Module 4, a `List<Animal>`) can hold `Dog`s and `Cat`s and call
      `speak()` polymorphically.
- [ ] An override may widen visibility (`protected` → `public`) but never narrow it.

## Practice
**Goal:** See dynamic dispatch in action.
**Steps:**
- [ ] Put several `Animal` subclasses in an `Animal[]` and loop over it calling `speak()`.
- [ ] Add `@Override`, then deliberately mistype a method name and see the compiler catch it.
- [ ] Write a method that accepts an `Animal` and works for any subclass — including one you add
      afterwards.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- `Animal a = new Dog(); a.speak();` — whose `speak()` runs?
> `Dog`'s. The variable's type is `Animal`, but the object's runtime type decides which override
> runs (dynamic dispatch).

> [!question]- Overriding vs overloading?
> Overriding: a subclass replaces an inherited method with the same signature; resolved at runtime.
> Overloading: same name, different parameters, in the same class; resolved at compile time.

> [!question]- Why bother with `@Override`?
> The compiler then checks that you really override something — a typo or wrong parameter type
> becomes a compile error instead of a silent new method.

## Definition of Done
- [ ] I can override methods with `@Override` and explain dynamic dispatch.
- [ ] I can distinguish overriding from overloading.
- [ ] I can write code against a supertype that works for any subtype.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]]
