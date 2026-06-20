---
title: Encapsulation and Access Modifiers
area: OOP
module: 3
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Encapsulation and Access Modifiers

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 3h
> **Why this matters:** Encapsulation — hiding internal state behind a controlled interface — is the
> first principle of maintainable OOP. It's also a near-guaranteed interview question.

## Learning Objectives
- Use access modifiers (`private`, `public`, `protected`, package-private) deliberately.
- Expose state safely via getters/setters with validation.
- Explain why encapsulation matters.

## Learn
- [ ] Read: [dev.java — "Encapsulation"](https://dev.java/learn/classes-objects/).
- [ ] Read about the four access levels.

## Concepts
- [ ] Make fields `private`; expose behavior through methods. Callers depend on *what*, not *how*.
- [ ] Access levels: `private` (class), package-private (no modifier), `protected` (package +
      subclasses), `public` (everywhere).
- [ ] **Getters/setters** control access and can validate (reject invalid values) or compute results.
- [ ] Encapsulation lets you change internals without breaking callers — the core of low coupling.
- [ ] Records (Module 5) reduce boilerplate for simple immutable data holders.

## Practice
**Goal:** Turn a leaky class into an encapsulated one.
**Steps:**
- [ ] Take a class with public fields and make them `private` with getters.
- [ ] Add validation in a setter (e.g. price cannot be negative) and prove it rejects bad input.
- [ ] Note which methods/fields truly need to be `public`.

## Definition of Done
- [ ] I default to `private` fields and expose only what's needed.
- [ ] I can validate input in setters.
- [ ] I can explain why encapsulation reduces coupling.

## Next
- Next: [[M3 - OOP - Inheritance]]
