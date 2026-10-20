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
> first principle of maintainable OOP. Immutability takes it one step further and removes whole
> classes of bugs. Both are near-guaranteed interview topics.

## Learning Objectives
- Use access modifiers (`private`, `public`, `protected`, package-private) deliberately.
- Expose state safely via methods with validation.
- Design a simple immutable class and explain why it's safer.

## Learn
- [ ] Read:
      [Controlling Access to Members of a Class](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
      (Java Tutorials — older site, still accurate).
- [ ] Read:
      [dev.java — More on Classes](https://dev.java/learn/language/oop/classes-objects/more-on-classes/)
      (the `final` and access parts).
- [ ] Optional: *Effective Java*, items 15–17 ("minimize accessibility", "minimize mutability").

## Concepts
- [ ] Make fields `private`; expose behavior through methods. Callers depend on *what*, not *how*.
- [ ] Access levels: `private` (class), package-private (no modifier), `protected` (package +
      subclasses), `public` (everywhere).
- [ ] **Getters/setters** control access and can validate (reject invalid values) or compute results
      — but don't generate a setter for every field by reflex.
- [ ] **Immutability**: `private final` fields, everything set in the constructor, no setters, and
      copies of mutable internals (defensive copies). Immutable objects are thread-safe and easy to
      reason about.
- [ ] Encapsulation lets you change internals without breaking callers — the core of low coupling.
      Records (Module 5) make immutable data classes a one-liner.

## Practice
**Goal:** Turn a leaky class into an encapsulated, then immutable, one.
**Steps:**
- [ ] Take a class with public fields and make them `private` with getters.
- [ ] Add validation (e.g. price cannot be negative) and prove it rejects bad input.
- [ ] Make a `Money(amount, currency)` class immutable; "changing" it returns a new object
      (`plus(...)`).
- [ ] Give a class an internal `int[]` and a getter that returns it; show a caller can modify your
      internals, then fix it with `Arrays.copyOf`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Order the four access levels from most to least restrictive.
> `private` → package-private (no modifier) → `protected` → `public`.

> [!question]- Why prefer `private` fields with methods over `public` fields?
> The class keeps control: it can validate, compute, or change its internal representation later
> without breaking any caller.

> [!question]- What makes a class immutable?
> All fields `private final`, set once in the constructor, no setters, no methods that modify state,
> and no leaking references to mutable internals (return copies).

> [!question]- A getter returns your internal array directly. What's the risk?
> Callers can modify the array and silently change your object's state. Return a copy (or, later, an
> unmodifiable collection).

## Definition of Done
- [ ] I default to `private` fields and expose only what's needed.
- [ ] I can validate input before changing state.
- [ ] I can write an immutable class and explain why it's safer.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M3 - OOP - Inheritance]]
