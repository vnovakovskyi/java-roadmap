---
title: Fields, Methods and Constructors
area: OOP
module: 3
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Fields, Methods and Constructors

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 4h
> **Why this matters:** Fields hold an object's state, methods give it behavior, and constructors
> set it up correctly. This is the anatomy of every class you'll write.

## Learning Objectives
- Add fields, instance methods, and constructors to a class.
- Use `this` to disambiguate fields from parameters.
- Distinguish instance vs `static` members.

## Learn
- [ ] Read: [dev.java — "Defining classes / constructors"](https://dev.java/learn/classes-objects/).
- [ ] Read about `this`, `static`, and default field values.

## Concepts
- [ ] **Fields** = instance state; **methods** = behavior that can read/modify fields.
- [ ] A **constructor** has the class's name and no return type; it initializes a new object.
- [ ] Constructor **overloading** + `this(...)` to chain constructors; a no-arg default exists only
      if you write no constructor.
- [ ] `this.field = field` resolves a name clash between a field and a parameter.
- [ ] `static` fields/methods belong to the class (shared); instance members belong to each object.

## Practice
**Goal:** Build a properly initialized class.
**Steps:**
- [ ] Give `Book` a constructor that requires title and author; add a `static` counter of books created.
- [ ] Add an instance method that mutates a field (e.g. `markAsRead()`).
- [ ] Create several books and print the static count.

**Record your result:**
- 

## Definition of Done
- [ ] I can write fields, methods, and constructors and use `this`.
- [ ] I can explain instance vs static members.
- [ ] I understand constructor chaining and the default constructor rule.

## Cheatsheet (my notes)
- 

## Related
- [[M3 - OOP - Classes and Objects]]
- [[M3 - OOP - Encapsulation and Access Modifiers]]
