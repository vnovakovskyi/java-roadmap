---
title: Conditionals (if and switch)
area: Core Java
module: 2
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Conditionals (if and switch)

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 3h
> **Why this matters:** Programs make decisions. `if`/`else` and `switch` are how your code branches —
> the basis of all logic.

## Learning Objectives
- Write `if` / `else if` / `else` chains and nested conditions.
- Use the ternary operator for simple choices.
- Use modern `switch` expressions.

## Learn
- [ ] Read: [dev.java — "Control Flow / branching"](https://dev.java/learn/language-basics/).
- [ ] Read about the modern `switch` expression (arrow syntax, `yield`).

## Concepts
- [ ] `if (condition) { ... } else { ... }`; conditions must be `boolean`.
- [ ] Chain with `else if`; avoid deep nesting by returning early or combining conditions.
- [ ] Ternary: `result = cond ? a : b` for compact either/or.
- [ ] Modern `switch`: `case X -> ...;` (no fall-through), can be an **expression** that returns a value.
- [ ] `switch` works on `int`, `String`, `enum`, and more; arrow form is safer than old `:` + `break`.

## Practice
**Goal:** Branch on real input.
**Steps:**
- [ ] Write a grade classifier: a score → letter grade using `if/else if`.
- [ ] Rewrite it with a `switch` expression (e.g. on a category).
- [ ] Use a ternary to print "even"/"odd" for a number.

**Record your result:**
- 

## Definition of Done
- [ ] I can write correct `if/else if/else` logic.
- [ ] I can use a modern `switch` expression that returns a value.
- [ ] I know when a ternary improves readability vs hurts it.

## Cheatsheet (my notes)
- 

## Related
- [[M2 - Core Java - Operators and Expressions]]
- [[M2 - Core Java - Loops (for and while)]]
