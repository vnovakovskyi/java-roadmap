---
title: Inheritance
area: OOP
module: 3
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Inheritance

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 4h
> **Why this matters:** Inheritance lets classes share and specialize behavior. Used well it removes
> duplication; used poorly it creates fragile hierarchies — knowing the difference is key.

## Learning Objectives
- Create a subclass with `extends` and reuse/override behavior.
- Use `super` to call the parent constructor and methods.
- Recognize when composition is better than inheritance.

## Learn
- [ ] Read: [dev.java — "Inheritance"](https://dev.java/learn/inheritance/).
- [ ] Read about `super`, `Object` as the root class, and `final` classes/methods.

## Concepts
- [ ] `class Dog extends Animal` — `Dog` inherits accessible fields/methods of `Animal`.
- [ ] Every class ultimately extends `Object`.
- [ ] `super(...)` calls the parent constructor (must be first); `super.method()` calls the parent's version.
- [ ] **Is-a** vs **has-a**: use inheritance for genuine "is-a"; otherwise prefer **composition**.
- [ ] `final` prevents overriding/extension; deep hierarchies are a smell.

## Practice
**Goal:** Build a small hierarchy and feel its trade-offs.
**Steps:**
- [ ] Create `Animal` with a `speak()` method and subclasses `Dog`/`Cat` that override it.
- [ ] Give `Animal` a constructor and call it from a subclass via `super`.
- [ ] Rewrite one relationship using composition (a field) instead of inheritance and compare.

## Definition of Done
- [ ] I can create subclasses and use `super` correctly.
- [ ] I can explain "is-a vs has-a" and when to prefer composition.
- [ ] I understand `Object` is the root of all classes.

## Next
- Next: [[M3 - OOP - Polymorphism and Overriding]]
