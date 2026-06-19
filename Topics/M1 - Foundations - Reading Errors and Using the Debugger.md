---
title: Reading Errors and Using the Debugger
area: Foundations
module: 1
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Reading Errors and Using the Debugger

> [!info] Topic
> **Area:** Foundations · **Module:** 1 · **Priority:** must · **Est:** 4h
> **Why this matters:** You'll spend more time fixing code than writing it. Reading stack traces and
> stepping through code with a debugger is the single most valuable beginner skill — learn it now.

## Learning Objectives
- Read a compiler error and a runtime stack trace and find the line that matters.
- Set a breakpoint and step through code in the IDE.
- Inspect variable values while paused.

## Learn
- [ ] Read your IDE's debugger guide (IntelliJ: "Debug your first Java application").
- [ ] Learn to read a stack trace: exception type → message → the **top-most line in your code**.

## Concepts
- [ ] **Compile errors** stop compilation (typos, missing `;`, wrong types). Fix the first one first.
- [ ] **Runtime exceptions** (e.g. `NullPointerException`) appear as a **stack trace**; read it
      top-down and look for your own file names.
- [ ] A **breakpoint** pauses execution on a line; then you **step over / into / out** of calls.
- [ ] While paused you can inspect variables and evaluate expressions — far better than scattering
      print statements.

## Practice
**Goal:** Diagnose a bug with the debugger, not guesswork.
**Steps:**
- [ ] Write a small program with an intentional `NullPointerException` or off-by-one.
- [ ] Run it, read the stack trace, and predict the failing line.
- [ ] Set a breakpoint just before it, run in debug mode, and inspect the variables.
- [ ] Fix the bug and confirm.

**Record your result:**
- 

## Definition of Done
- [ ] I can read a stack trace and locate the offending line in my code.
- [ ] I can set a breakpoint and step through code, inspecting variables.
- [ ] I prefer the debugger over print-debugging for tricky bugs.

## Cheatsheet (my notes)
- 

## Related
- [[M1 - Foundations - How Java Compiles and Runs]]
- [[M4 - Java APIs - Exceptions and Error Handling]]
