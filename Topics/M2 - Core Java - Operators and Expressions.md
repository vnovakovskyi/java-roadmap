---
title: Operators and Expressions
area: Core Java
module: 2
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Operators and Expressions

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 3h
> **Why this matters:** Operators are how you compute and compare. Subtle rules (integer division,
> precedence, short-circuiting) cause classic beginner bugs — meet them deliberately.

## Learning Objectives
- Use arithmetic, comparison, logical, and assignment operators correctly.
- Predict the result of mixed-type and integer arithmetic.
- Use operator precedence and parentheses for clarity.

## Learn
- [ ] Read: [dev.java — "Operators"](https://dev.java/learn/language-basics/).
- [ ] Read about integer division and the modulo (`%`) operator.

## Concepts
- [ ] Arithmetic: `+ - * / %`. **Integer division truncates** (`7 / 2 == 3`); use `%` for remainder.
- [ ] Comparison: `== != < > <= >=` return `boolean`. **Never use `==` to compare `String` contents.**
- [ ] Logical: `&&` `||` `!` — `&&`/`||` **short-circuit** (stop early), which matters with side effects.
- [ ] Assignment shortcuts: `+= -= *= /=`; increment/decrement `++ --` (pre vs post).
- [ ] Precedence: `*` before `+`; when in doubt, add parentheses for readability.

## Practice
**Goal:** Build intuition for the gotchas.
**Steps:**
- [ ] Compute and print `7 / 2`, `7 % 2`, `7.0 / 2` — explain the differences.
- [ ] Write a boolean expression using `&&` and `||` and test it with several inputs.
- [ ] Demonstrate pre- vs post-increment (`i++` vs `++i`) in a print statement.

**Record your result:**
- 

## Definition of Done
- [ ] I can predict integer-division and modulo results.
- [ ] I know why `==` is wrong for String content and what to use instead.
- [ ] I understand short-circuit evaluation.

## Cheatsheet (my notes)
- 

## Related
- [[M2 - Core Java - Variables, Primitives and Types]]
- [[M2 - Core Java - Conditionals (if and switch)]]
