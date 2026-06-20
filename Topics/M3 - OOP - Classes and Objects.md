---
title: Classes and Objects
area: OOP
module: 3
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Classes and Objects

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 4h
> **Why this matters:** Java is object-oriented to the core. Understanding classes (blueprints) and
> objects (instances) is the mental shift from "scripts" to real Java programs.

## Learning Objectives
- Define a class and create objects from it with `new`.
- Distinguish a class from its instances.
- Understand references, `null`, and object identity.

## Learn
- [ ] Read: [dev.java — "Classes and Objects"](https://dev.java/learn/classes-objects/).
- [ ] Read about the `new` keyword and object references.

## Concepts
- [ ] A **class** describes state (fields) and behavior (methods); an **object** is a concrete
      instance created with `new`.
- [ ] Object variables hold a **reference** (an address), not the object itself.
- [ ] `null` means "no object"; calling a method on `null` throws `NullPointerException`.
- [ ] Two references can point to the same object (aliasing) or to equal-but-separate objects.
- [ ] Each object has its own copy of instance fields.

## Practice
**Goal:** Model something real as a class.
**Steps:**
- [ ] Write a `Book` class with fields (title, author, pages) and a method `describe()`.
- [ ] Create two `Book` objects and call `describe()` on each.
- [ ] Set one reference equal to another and show they point to the same object.

## Definition of Done
- [ ] I can define a class and instantiate objects.
- [ ] I can explain the difference between a class and an object.
- [ ] I understand references, `null`, and aliasing.

## Next
- Next: [[M3 - OOP - Fields, Methods and Constructors]]
