---
title: Abstraction, Interfaces and Abstract Classes
area: OOP
module: 3
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Abstraction, Interfaces and Abstract Classes

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 5h
> **Why this matters:** Interfaces define contracts without dictating implementation — the backbone
> of testable, swappable, framework-friendly code. This is one of the highest-leverage OOP topics.

## Learning Objectives
- Define and implement interfaces.
- Choose between an interface and an abstract class.
- Use interfaces to decouple code (program to an interface).

## Learn
- [ ] Read: [dev.java — "Interfaces"](https://dev.java/learn/interfaces/).
- [ ] Read about abstract classes and `default` methods on interfaces.

## Concepts
- [ ] An **interface** is a contract: method signatures a class promises to provide via `implements`.
      A class can implement many interfaces.
- [ ] An **abstract class** can't be instantiated and may mix abstract + concrete methods + state; a
      class extends only one.
- [ ] Rule of thumb: interface = capability/contract (can have many); abstract class = shared base
      with state.
- [ ] Interfaces can have `default` and `static` methods.
- [ ] "Program to an interface" → swap implementations (e.g. for tests) without touching callers.

## Practice
**Goal:** Decouple with an interface.
**Steps:**
- [ ] Define `Shape` with `double area()`; implement `Circle` and `Rectangle`.
- [ ] Write a method that totals the area of a `List<Shape>` — works for any shape.
- [ ] Create a `Repository` interface and two implementations (e.g. in-memory vs fake) to feel the
      decoupling you'll use constantly in Spring.

## Definition of Done
- [ ] I can define and implement interfaces.
- [ ] I can decide between interface and abstract class with reasons.
- [ ] I can explain how interfaces enable decoupling and testing.

## Next
- Next: [[M3 - OOP - equals, hashCode and toString]]
