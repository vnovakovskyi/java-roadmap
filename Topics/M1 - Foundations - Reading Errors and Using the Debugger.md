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
- [ ] Read: [dev.java — Debugging in Java](https://dev.java/learn/validate/debugging/).
- [ ] Do:
      [IntelliJ IDEA — Debug your first Java application](https://www.jetbrains.com/help/idea/debugging-your-first-java-application.html)
      (VS Code: [Debugging Java](https://code.visualstudio.com/docs/java/java-debugging)).
- [ ] Learn to read a stack trace: exception type → message → the **top-most line in your own
      code**.

## Concepts
- [ ] **Compile errors** stop compilation (typos, missing `;`, wrong types). Fix the first one first
      — later ones are often side effects.
- [ ] **Runtime exceptions** (e.g. `NullPointerException`) appear as a **stack trace**; read it
      top-down and look for your own file names and line numbers.
- [ ] Modern `NullPointerException` messages name the culprit ("because `name` is null") — read the
      whole message.
- [ ] A **breakpoint** pauses execution on a line; then you **step over / into / out** of calls.
- [ ] While paused you can inspect variables and evaluate expressions — far better than scattering
      print statements.

## Practice
**Goal:** Diagnose a bug with the debugger, not guesswork.
**Steps:**
- [ ] Write a small program with an intentional `NullPointerException` or off-by-one error.
- [ ] Run it, read the stack trace, and predict the failing line before opening the file.
- [ ] Set a breakpoint just before it, run in debug mode, and inspect the variables.
- [ ] Fix the bug and confirm.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- A stack trace starts with `Exception in thread "main" java.lang.NullPointerException` and lists ten lines. Which line do you look at first?
> The first line that points to your own code (your class names and files). Frames from the JDK or
> libraries show where the failure surfaced, not why.

> [!question]- There are twelve compile errors. Where do you start?
> With the first one. Later errors are often caused by it — fix, recompile, repeat.

> [!question]- What's the difference between step over and step into?
> Step over runs the current line (including any method call on it) and stops at the next line; step
> into enters the method being called so you can follow it.

> [!question]- Why prefer the debugger over print statements for a tricky bug?
> You can pause anywhere, inspect every variable, and evaluate expressions without editing and
> re-running the code.

## Definition of Done
- [ ] I can read a stack trace and locate the offending line in my code.
- [ ] I can set a breakpoint and step through code, inspecting variables.
- [ ] I reach for the debugger instead of print-debugging for tricky bugs.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M1 - Foundations - Getting Unstuck and Learning with AI]]
