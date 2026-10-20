---
title: Pattern Matching and Sealed Types
area: Modern Java
module: 5
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Pattern Matching and Sealed Types

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** must · **Est:** 4h
> **Why this matters:** Since Java 21, `switch` can test an object's *type and shape*, and the
> compiler can check that you've handled every case. Together with sealed interfaces and records
> this is "data-oriented programming" — the biggest change to everyday Java code since lambdas, and
> increasingly common in modern codebases and interviews.

## Learning Objectives
- Use pattern matching for `instanceof`.
- Write `switch` with type patterns, record patterns, and guards.
- Model a closed set of types with sealed interfaces and get exhaustiveness checks.

## Learn
- [ ] Read:
      [dev.java — Using Pattern Matching](https://dev.java/learn/language/fp/pattern-matching/).
- [ ] Read:
      [Sealed Classes and Interfaces](https://docs.oracle.com/en/java/javase/25/language/sealed-classes-interfaces.html)
      (Oracle language guide).
- [ ] Read:
      [Pattern Matching for switch](https://docs.oracle.com/en/java/javase/25/language/pattern-matching-switch.html)
      and
      [Record Patterns](https://docs.oracle.com/en/java/javase/25/language/record-patterns.html).

## Concepts
- [ ] `if (obj instanceof String s && !s.isBlank())` — test, cast, and bind in one step.
- [ ] `sealed interface Shape permits Circle, Rectangle {}` — only the listed types may implement
      it; each must be `final`, `sealed`, or `non-sealed` (records are implicitly `final`).
- [ ] Type patterns in `switch`: `case Circle c -> ...`. **Record patterns** deconstruct:
      `case Rectangle(double w, double h) -> w * h`.
- [ ] **Exhaustiveness**: a `switch` over a sealed type needs no `default`. Add a new subtype and
      the compiler flags every `switch` that doesn't handle it — that's the point.
- [ ] Guards: `case Circle c when c.radius() == 0 -> 0;`. `case null ->` handles `null` explicitly
      (otherwise the switch throws NPE).
- [ ] *(Java 22+)* The unnamed pattern `_` skips parts you don't need:
      `case Rectangle(var w, _) -> ...`. (Primitive types in patterns are still a preview feature —
      skip them.)

```java
sealed interface Shape permits Circle, Rectangle {}
record Circle(double radius) implements Shape {}
record Rectangle(double width, double height) implements Shape {}

double area(Shape shape) {
    return switch (shape) {
        case Circle(double r)              -> Math.PI * r * r;
        case Rectangle(double w, double h) -> w * h;
    }; // no default: the compiler knows every possible Shape
}
```

## Practice
**Goal:** Model data with sealed types and records, and process it with `switch`.
**Steps:**
- [ ] Replace an `if (x instanceof Foo) { Foo f = (Foo) x; ... }` chain with pattern matching.
- [ ] Build the `Shape` hierarchy above and an `area` method; then add `Triangle` and fix the
      compile errors it causes.
- [ ] Add a guard (`when`) case and a `case null`.
- [ ] Model a tiny command language — `sealed interface Command permits Add, Remove, Quit` with
      record subtypes — and execute commands with a pattern-matching `switch` (you'll reuse this in
      the module project).

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What does `sealed` give you that a normal interface doesn't?
> A closed, known set of implementations. That documents the design, blocks unexpected subtypes, and
> lets the compiler check that a `switch` covers every case.

> [!question]- Why is it better *not* to write `default` in a switch over a sealed type?
> Without `default`, adding a new subtype turns every unhandled `switch` into a compile error. With
> `default`, the new type silently falls into it.

> [!question]- What does `case Rectangle(double w, double h) -> w * h` do?
> It matches only `Rectangle` objects and deconstructs them, binding the record's components to `w`
> and `h`.

> [!question]- What happens when you `switch` on a `null` value without `case null`?
> It throws a `NullPointerException`.

## Definition of Done
- [ ] I can use pattern matching for `instanceof` and in `switch`.
- [ ] I can design a sealed hierarchy of records.
- [ ] I can explain exhaustiveness and why it beats a `default` branch.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M5 - Modern Java - Date and Time (java.time)]]
