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
- Read user input and print formatted output.
- Compare strings correctly.

## Learn
- [ ] Read:
      [dev.java — Strings](https://dev.java/learn/language/constructs/numbers-strings/strings/) and
      [String Builders](https://dev.java/learn/language/constructs/numbers-strings/string-builders/).
- [ ] Reference: the
      [`String` Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html)
      — learn to look methods up here.
- [ ] Reference:
      [`IO`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/IO.html) (Java
      25) and
      [`Scanner`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Scanner.html)
      for console input.

## Concepts
- [ ] `String`s are **immutable**: methods like `toUpperCase()` return a *new* string.
- [ ] Compare content with `.equals()` / `.equalsIgnoreCase()`, **not** `==` (which compares
      references).
- [ ] Useful methods: `length`, `charAt`, `substring`, `indexOf`, `contains`, `replace`, `split`,
      `strip`, `isBlank`, `repeat`.
- [ ] Build strings in loops with `StringBuilder` — `+=` creates a new string every time.
- [ ] Output: `IO.println` / `System.out.println`; formatting with `String.format`,
      `"...".formatted(...)`, or `printf` (`"%s is %d%n"`).
- [ ] Input: *(Java 25+)* `IO.readln("Name: ")` prints a prompt and reads a whole line. The classic
      way is `new Scanner(System.in)`. Either way, read **whole lines** and convert them:
      `Integer.parseInt(line)`.

## Practice
**Goal:** A small interactive console program.
**Steps:**
- [ ] Ask the user's name and age with `IO.readln`, convert the age, and print a formatted greeting.
- [ ] Take a sentence and print its length, uppercase version, and word count (`split("\\s+")`).
- [ ] Show that `"a".equals(new String("a"))` is true while `==` is false.
- [ ] Build the string `"1,2,3,…,10"` with a `StringBuilder` in a loop.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- You call `name.toUpperCase();` and `name` doesn't change. Why?
> Strings are immutable: the method returns a new String. Assign it: `name = name.toUpperCase();`.

> [!question]- When should you use a `StringBuilder`?
> When you build a string piece by piece, especially in a loop — `+=` would create a new String
> object on every iteration.

> [!question]- How do you read a number the user types?
> Read a line and parse it: `int age = Integer.parseInt(IO.readln("Age: "));`. Bad input throws
> `NumberFormatException` — handling it comes in Module 4.

> [!question]- Why does `scanner.nextLine()` return an empty string right after `scanner.nextInt()`?
> `nextInt()` leaves the line break in the input; the next `nextLine()` reads that empty remainder.
> Reading whole lines and parsing them avoids the problem.

## Definition of Done
- [ ] I can read console input and print formatted output.
- [ ] I use `.equals()` for string comparison and can explain why.
- [ ] I know strings are immutable and when to use `StringBuilder`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M2 - Core Java - Conditionals (if and switch)]]
