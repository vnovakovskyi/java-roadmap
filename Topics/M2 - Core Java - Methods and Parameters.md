---
title: Methods and Parameters
area: Core Java
module: 2
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Methods and Parameters

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 4h
> **Why this matters:** Methods are how you name, reuse, and organize behavior. Writing small,
> well-named methods is the first real step toward clean code.

## Learning Objectives
- Define methods with parameters and return values.
- Understand pass-by-value (and what that means for objects).
- Use method overloading and recognize good method design.

## Learn
- [ ] Read: [dev.java — "Methods"](https://dev.java/learn/).
- [ ] Read about parameters, return types, and `void`.

## Concepts
- [ ] Signature: `returnType name(params) { ... }`; `return` produces the result (or nothing for `void`).
- [ ] Java is **pass-by-value**: the method gets a copy of the argument. For objects, the *reference*
      is copied — so you can mutate the object but can't reassign the caller's variable.
- [ ] **Overloading**: same name, different parameter lists.
- [ ] `static` methods belong to the class, not an instance (more in Module 3).
- [ ] Good methods are short, do one thing, and have descriptive names.

## Practice
**Goal:** Decompose a problem into methods.
**Steps:**
- [ ] Write `int max(int a, int b)` and `int max(int a, int b, int c)` (overload).
- [ ] Write a method that takes an array and returns its average.
- [ ] Demonstrate pass-by-value: a method that tries to reassign a parameter, proving the caller's
      variable is unchanged.

**Record your result:**
- 

## Definition of Done
- [ ] I can write methods with parameters and return values.
- [ ] I can explain pass-by-value, including for objects.
- [ ] I can refactor a long block into named methods.

## Cheatsheet (my notes)
- 

## Related
- [[M2 - Core Java - Arrays]]
- [[M3 - OOP - Fields, Methods and Constructors]]
