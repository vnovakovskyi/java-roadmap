---
title: Variables, Primitives and Types
area: Core Java
module: 2
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Variables, Primitives and Types

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 4h
> **Why this matters:** Java is statically typed — every value has a type. Getting variables, types,
> and conversions right is the foundation for literally everything else.

## Learning Objectives
- Declare and initialize variables with the correct type.
- Name the 8 primitive types and when to use each.
- Explain the difference between primitives and reference types.
- Convert between numeric types and predict what a cast does.

## Learn
- [ ] Read:
      [dev.java — Creating Variables and Naming Them](https://dev.java/learn/language/constructs/basics/variables/).
- [ ] Read:
      [dev.java — Creating Primitive Type Variables](https://dev.java/learn/language/constructs/basics/primitive-types/).
- [ ] Read:
      [dev.java — Using the Var Type Identifier](https://dev.java/learn/language/constructs/basics/using-var/).
- [ ] Tip: keep `jshell` open while you read and try every example.

## Concepts
- [ ] Primitives: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean` — they hold
      values directly. Defaults to reach for: `int`, `long`, `double`, `boolean`.
- [ ] Reference types (`String`, arrays, objects) hold a reference to data on the heap.
- [ ] Declaration vs initialization vs assignment; `final` makes a variable a constant. Naming:
      `camelCase` for variables, `UPPER_SNAKE_CASE` for constants.
- [ ] `var` (Java 10+) infers the type from the right-hand side — convenient, and still statically
      typed.
- [ ] **Casting**: widening is automatic (`int` → `long` → `double`); narrowing needs an explicit
      cast and can lose data — `(int) 3.99` is `3`, `(byte) 200` is `-56`.
- [ ] Overflow wraps around silently; floating point is imprecise (`0.1 + 0.2` ≠ `0.3`) — that's why
      money is never a `double` (use `BigDecimal`, Module 4).
- [ ] **Scope**: a variable exists only inside the `{ }` block where it's declared.

## Practice
**Goal:** Get a feel for types and their limits.
**Steps:**
- [ ] Declare one variable of each primitive type and print them.
- [ ] Trigger an `int` overflow (add 1 to `Integer.MAX_VALUE`) and observe the result.
- [ ] Print `0.1 + 0.2` as a `double`; note it isn't exactly `0.3`.
- [ ] Cast `9.99` to `int` and `300` to `byte`; explain both results.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Name the 8 primitive types.
> `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.

> [!question]- What is `(int) 3.99`?
> `3`. Narrowing casts truncate toward zero; they don't round (use `Math.round` for that).

> [!question]- What happens when you add 1 to `Integer.MAX_VALUE`?
> It silently wraps around to `Integer.MIN_VALUE` (-2147483648). No exception — use `long` or
> `Math.addExact` when overflow matters.

> [!question]- Why shouldn't money be stored in a `double`?
> Binary floating point can't represent most decimal fractions exactly, so rounding errors creep in
> and accumulate. Use `BigDecimal` (or whole cents in a `long`).

> [!question]- Does `var x = 5;` make `x` dynamically typed?
> No. The compiler infers `int` once; `x` stays an `int` and can never hold a `String`.

## Definition of Done
- [ ] I can declare correctly typed variables and use `final` and `var` appropriately.
- [ ] I can name the primitive types and pick the right one.
- [ ] I can explain primitives vs reference types and predict what a cast does.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M2 - Core Java - Operators and Expressions]]
