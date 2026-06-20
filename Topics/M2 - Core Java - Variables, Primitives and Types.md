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
> **Why this matters:** Java is statically typed — every value has a type. Getting variables and
> types right is the foundation for literally everything else.

## Learning Objectives
- Declare and initialize variables with the correct type.
- Name the 8 primitive types and when to use each.
- Explain the difference between primitives and reference types.

## Learn
- [ ] Read: [dev.java — "Using Variables"](https://dev.java/learn/language-basics/) and primitive types.
- [ ] Read about `int` vs `long`, `double` vs `float`, `char`, `boolean`.

## Concepts
- [ ] Primitives: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean` — hold values
      directly.
- [ ] Reference types (e.g. `String`, arrays, objects) hold a reference to data on the heap.
- [ ] Declaration vs initialization vs assignment; `final` makes a variable a constant.
- [ ] `var` (Java 10+) infers the type from the right-hand side — convenient, still statically typed.
- [ ] Integer/floating overflow and precision: why money should not be a `double`.

## Practice
**Goal:** Get a feel for types and their limits.
**Steps:**
- [ ] Declare one variable of each primitive type and print them.
- [ ] Trigger an `int` overflow (add 1 to `Integer.MAX_VALUE`) and observe the result.
- [ ] Compare `0.1 + 0.2` printed as a `double`; note it isn't exactly `0.3`.

## Definition of Done
- [ ] I can declare correctly typed variables and use `final` and `var` appropriately.
- [ ] I can name the primitive types and pick the right one.
- [ ] I can explain primitives vs reference types.

## Next
- Next: [[M2 - Core Java - Operators and Expressions]]
