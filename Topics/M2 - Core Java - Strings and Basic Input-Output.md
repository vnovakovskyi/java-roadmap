---
title: Strings and Basic Input-Output
area: Core Java
module: 2
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Strings and Basic Input-Output

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 4h
> **Why this matters:** Almost every program reads input and produces text output. Strings are
> everywhere, and a few rules (immutability, equality) trip up nearly every beginner.

## Learning Objectives
- Create and manipulate `String`s using common methods.
- Read user input with `Scanner` and print formatted output.
- Compare strings correctly.

## Learn
- [ ] Read: [dev.java — "Strings"](https://dev.java/learn/) and the `String` Javadoc.
- [ ] Read about `Scanner` for console input.

## Concepts
- [ ] `String`s are **immutable**: methods like `toUpperCase()` return a *new* string.
- [ ] Compare content with `.equals()` / `.equalsIgnoreCase()`, **not** `==` (which compares references).
- [ ] Useful methods: `length`, `charAt`, `substring`, `indexOf`, `contains`, `replace`, `split`,
      `trim`/`strip`, `isBlank`.
- [ ] Build strings efficiently in loops with `StringBuilder`.
- [ ] Output: `System.out.println`, `printf`/`String.format` for formatting; text blocks (`"""`)
      for multi-line text.

## Practice
**Goal:** A small interactive console program.
**Steps:**
- [ ] Use `Scanner` to ask the user's name and age, then print a formatted greeting.
- [ ] Take a sentence and print its length, uppercase version, and word count (`split`).
- [ ] Show that `"a".equals("a")` is true but `==` may be unreliable for built strings.

## Definition of Done
- [ ] I can read console input and print formatted output.
- [ ] I use `.equals()` for string comparison and can explain why.
- [ ] I know strings are immutable and when to use `StringBuilder`.

## Next
- Next: [[M2 - Core Java - Conditionals (if and switch)]]
