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
- [ ] Read: [dev.java — "Exceptions"](https://dev.java/learn/exceptions/).
- [ ] Read about try-with-resources and the exception hierarchy (`Throwable` → `Exception`/`Error`).

## Concepts
- [ ] `try { } catch (SpecificException e) { } finally { }`; catch specific types before general ones.
- [ ] **Checked** (compiler-enforced, e.g. `IOException`) vs **unchecked** (`RuntimeException`, e.g.
      `NullPointerException`, `IllegalArgumentException`).
- [ ] **Try-with-resources** auto-closes things like files/connections — prefer it.
- [ ] `throw new IllegalArgumentException("...")` to signal misuse; create custom exceptions for your
      domain when it adds clarity.
- [ ] Anti-patterns: swallowing exceptions (empty catch), catching `Exception` blindly, using
      exceptions for normal control flow.

## Practice
**Goal:** Handle failure paths cleanly.
**Steps:**
- [ ] Parse user input to an `int`; catch `NumberFormatException` and re-prompt.
- [ ] Read a file with try-with-resources; handle the file-not-found case with a clear message.
- [ ] Write a method that throws `IllegalArgumentException` on invalid input and test both paths.

## Definition of Done
- [ ] I can use try/catch/finally and try-with-resources correctly.
- [ ] I can explain checked vs unchecked exceptions.
- [ ] I avoid swallowing exceptions and throw meaningful ones.

## Next
- Next: [[M4 - Java APIs - Enums]]
