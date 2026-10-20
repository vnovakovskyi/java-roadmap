---
title: Loops (for and while)
area: Core Java
module: 2
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Loops (for and while)

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 4h
> **Why this matters:** Loops let you repeat work — iterate over data, retry, accumulate. They're
> half of all the algorithms you'll ever write.

## Learning Objectives
- Write `for`, `while`, and `do-while` loops.
- Use the enhanced for-each loop over arrays.
- Control loops with `break` and `continue` and avoid infinite loops.

## Learn
- [ ] Read:
      [dev.java — Control Flow Statements](https://dev.java/learn/language/constructs/basics/controlling-flow/)
      (the loop parts).
- [ ] Practice: [CodingBat — Warmup-1](https://codingbat.com/java/Warmup-1) and a few
      [Exercism Java exercises](https://exercism.org/tracks/java/exercises).

## Concepts
- [ ] `for (init; condition; update)` — best when you know the count or need an index.
- [ ] `while (condition)` — repeat until a condition changes; `do-while` runs at least once.
- [ ] **For-each**: `for (var item : items)` — cleanest for going through every element.
- [ ] `break` exits the loop; `continue` skips to the next iteration.
- [ ] Nested loops multiply work (a loop inside a loop over *n* items runs *n²* times).
- [ ] Off-by-one errors and infinite loops are the classic bugs — check your bounds and your update
      step.

## Practice
**Goal:** Drill iteration patterns.
**Steps:**
- [ ] Print the numbers 1–10 with a `for` loop; then only the even ones using `continue`.
- [ ] Sum the numbers 1–100 in a loop and print the total.
- [ ] Read numbers from the user until they type `0` (a `while` loop), then print the count and
      average.
- [ ] Print a multiplication table (1–9) with nested loops.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What's wrong with `for (int i = 0; i <= arr.length; i++)`?
> Off-by-one: the last valid index is `arr.length - 1`, so `<=` reads past the end and throws
> `ArrayIndexOutOfBoundsException`. Use `<`.

> [!question]- When do you pick `do-while` over `while`?
> When the body must run at least once — e.g. show a menu, then decide whether to repeat.

> [!question]- What's the difference between `break` and `continue`?
> `break` leaves the loop entirely; `continue` skips the rest of the current iteration and moves on
> to the next one.

> [!question]- How many times does `for (int i = 10; i > 0; i -= 3)` run?
> Four times: `i` = 10, 7, 4, 1.

## Definition of Done
- [ ] I can choose between `for`, `while`, and for-each appropriately.
- [ ] I can use `break`/`continue` correctly.
- [ ] I can spot and fix an off-by-one or infinite loop.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M2 - Core Java - Methods and Parameters]]
