---
title: Exceptions and Error Handling
area: Java APIs
module: 4
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Exceptions and Error Handling

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** must · **Est:** 4h
> **Why this matters:** Real programs hit bad input, missing files, and failing networks. Handling
> errors deliberately — instead of letting everything crash — is a defining trait of solid code.

## Learning Objectives
- Use `try`/`catch`/`finally` and try-with-resources.
- Distinguish checked vs unchecked exceptions.
- Throw and define your own exceptions sensibly.

## Learn
- [ ] Read:
      [dev.java — What Is an Exception?](https://dev.java/learn/language/annotations-exceptions/exceptions/what-is-an-exception/)
      and
      [Catching and Handling Exceptions](https://dev.java/learn/language/annotations-exceptions/exceptions/catching-handling/).
- [ ] Read:
      [dev.java — Throwing Exceptions](https://dev.java/learn/language/annotations-exceptions/exceptions/throwing/)
      and
      [Unchecked Exceptions — The Controversy](https://dev.java/learn/language/annotations-exceptions/exceptions/unchecked-exception-controversy/).

## Concepts
- [ ] `try { } catch (SpecificException e) { } finally { }`; catch specific types before general
      ones; `catch (A | B e)` handles several at once.
- [ ] **Checked** (compiler-enforced, e.g. `IOException`) vs **unchecked** (`RuntimeException` and
      subclasses, e.g. `NullPointerException`, `IllegalArgumentException`). The hierarchy:
      `Throwable` → `Exception` / `Error`.
- [ ] **Try-with-resources** auto-closes anything `AutoCloseable` (files, connections) — prefer it.
- [ ] `throw new IllegalArgumentException("...")` to signal misuse; create custom exceptions for
      your domain when it adds clarity (usually extending `RuntimeException`), and pass the original
      as the **cause**.
- [ ] Anti-patterns: swallowing exceptions (empty catch), catching `Exception` blindly, using
      exceptions for normal control flow.

## Practice
**Goal:** Handle failure paths cleanly.
**Steps:**
- [ ] Parse user input to an `int`; catch `NumberFormatException` and re-prompt.
- [ ] Open a file with try-with-resources —
      `try (var reader = Files.newBufferedReader(Path.of("notes.txt"))) { ... }` (files get a full
      topic in Module 5) — and report a missing file with a clear message.
- [ ] Write a method that throws `IllegalArgumentException` on invalid input and exercise both
      paths.
- [ ] Define `InsufficientFundsException` for a tiny bank-account class and throw it with a helpful
      message.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Checked vs unchecked exceptions — what's the difference? Give an example of each.
> The compiler forces you to catch or declare checked exceptions (`IOException`). Unchecked ones
> extend `RuntimeException` and usually signal bugs or misuse (`NullPointerException`,
> `IllegalArgumentException`).

> [!question]- What does try-with-resources guarantee?
> The resource's `close()` runs when the block ends — whether it finishes normally or throws. The
> resource must implement `AutoCloseable`.

> [!question]- What's wrong with `catch (Exception e) { }`?
> It silently swallows every error, including real bugs, so failures disappear without a trace.
> Catch specific exceptions and handle or log them.

> [!question]- When does a `finally` block run?
> Always after the `try` (and any `catch`), whether or not an exception was thrown — except if the
> JVM itself exits.

## Definition of Done
- [ ] I can use try/catch/finally and try-with-resources correctly.
- [ ] I can explain checked vs unchecked exceptions.
- [ ] I avoid swallowing exceptions and throw meaningful ones.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M4 - Java APIs - Enums]]
