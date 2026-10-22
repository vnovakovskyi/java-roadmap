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
- [ ] Read:
      [dev.java — Creating Classes](https://dev.java/learn/language/oop/classes-objects/creating-classes/)
      and
      [Creating and Using Objects](https://dev.java/learn/language/oop/classes-objects/creating-objects/).
- [ ] Alternative: [Java Programming MOOC — Part 4](https://java-programming.mooc.fi/part-4/)
      (University of Helsinki), the introduction to object-oriented programming, with exercises.

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
- [ ] Set one reference equal to another, change a field through one, and show the change through
      the other.
- [ ] Call a method on a `null` reference and read the exception message.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What's the difference between a class and an object?
> A class is the blueprint (which fields and methods exist); an object is one concrete instance
> created from it with `new`, with its own field values.

> [!question]- `Book a = new Book(); Book b = a; b.title = "X";` — what is `a.title` now?
> `"X"`. `a` and `b` are two references to the same object, so a change through one is visible
> through the other.

> [!question]- What does `null` mean, and what happens if you call a method on it?
> It means the variable refers to no object. Calling a method on it throws a `NullPointerException`.

## Definition of Done
- [ ] I can define a class and instantiate objects.
- [ ] I can explain the difference between a class and an object.
- [ ] I understand references, `null`, and aliasing.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M3 - OOP - Fields, Methods and Constructors]]
