---
title: How Java Compiles and Runs
area: Foundations
module: 1
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# How Java Compiles and Runs

> [!info] Topic
> **Area:** Foundations · **Module:** 1 · **Priority:** must · **Est:** 3h
> **Why this matters:** Understanding the compile-then-run cycle (and what `javac`/`java` actually
> do) is what separates "I copied code that worked" from "I know what's happening".

## Learning Objectives
- Describe the steps from `.java` to a running program.
- Use `javac` and `java` directly and explain each.
- Explain what bytecode is and where the JVM fits.

## Learn
- [ ] Read about `javac` (compiler) and `java` (launcher) in the JDK tool docs.
- [ ] Read a short explainer on bytecode and the JIT compiler (high level only).

## Concepts
- [ ] `javac Hello.java` → produces `Hello.class` (**bytecode**, not machine code).
- [ ] `java Hello` → the JVM loads the class, finds `main`, and executes the bytecode.
- [ ] The JVM **interprets** bytecode and **JIT-compiles** hot paths to native code at runtime —
      this is why Java is fast after "warming up".
- [ ] The **classpath** tells `java` where to find classes; the IDE/build tool manages it for you.
- [ ] Single-file source-code launch: `java Hello.java` can compile-and-run in one step (handy for
      quick experiments).

## Practice
**Goal:** See each stage explicitly.
**Steps:**
- [ ] Compile a program with `javac`, then open the folder and confirm the `.class` file exists.
- [ ] Run it with `java`.
- [ ] Try `java Hello.java` (one-step) and compare.
- [ ] Cause a compile error vs a runtime error and note which stage each happens in.

**Record your result:**
- 

## Definition of Done
- [ ] I can run the compile + run cycle by hand and explain each command.
- [ ] I can tell a compile-time error from a runtime error.
- [ ] I can explain what bytecode is and what the JVM does with it.

## Cheatsheet (my notes)
- 

## Related
- [[M1 - Foundations - How Programming and Java Work]]
- [[M1 - Foundations - Reading Errors and Using the Debugger]]

