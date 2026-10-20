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
> **Why this matters:** Understanding the compile-then-run cycle (what `javac` and `java` actually
> do) separates "I copied code that worked" from "I know what's happening" — and makes build tools
> and error messages far less mysterious later.

## Learning Objectives
- Describe the steps from `.java` to a running program.
- Use `javac` and `java` directly and explain each.
- Explain bytecode, the JIT, and the classpath at a high level.
- Use JShell for quick experiments.

## Learn
- [ ] Read:
      [dev.java — Launching Simple Source-Code Programs](https://dev.java/learn/first-steps/first-java-code/launch-simple-source-code-programs/).
- [ ] Read:
      [dev.java — JShell, the Java Shell Tool](https://dev.java/learn/first-steps/first-java-code/jshell-tool/).
- [ ] Reference: skim the "Description" sections of the
      [`javac`](https://docs.oracle.com/en/java/javase/25/docs/specs/man/javac.html) and
      [`java`](https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html) tool docs.

## Concepts
- [ ] `javac Hello.java` → produces `Hello.class` (**bytecode**, not machine code).
- [ ] `java Hello` → the JVM loads the class, finds `main`, and executes the bytecode.
- [ ] The JVM **interprets** bytecode and **JIT-compiles** hot paths to native code at runtime —
      this is why Java is fast after "warming up".
- [ ] The **classpath** tells `java` where to find classes (`-cp`); the IDE and build tools manage
      it for you.
- [ ] Source-code launch: `java Hello.java` compiles in memory and runs in one step — no `.class`
      file left behind. *(Java 22+)* It also works for small programs spread over several source
      files.
- [ ] **JShell** is a REPL: type `2 + 3` or `"java".toUpperCase()` and see the result instantly —
      ideal for trying syntax in Module 2.

## Practice
**Goal:** See each stage explicitly.
**Steps:**
- [ ] Write the classic `Hello` (class + `main`), compile it with `javac Hello.java`, and confirm
      `Hello.class` appears.
- [ ] Run it with `java Hello`; then delete the `.class` file and run `java Hello.java` instead.
- [ ] Cause a **compile** error (remove a `;`) and a **runtime** error (`int x = 1 / 0;`) and note
      which stage reports each.
- [ ] Open `jshell`, evaluate `10 / 3`, `10 / 3.0`, and `"java".length()`, then leave with `/exit`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What does `javac` produce, and what runs it?
> `.class` files containing bytecode; the JVM (started with `java`) loads and executes them.

> [!question]- Why is Java often called "fast after warming up"?
> The JIT compiler watches which code runs often and compiles those hot paths to native machine code
> while the program runs.

> [!question]- Give an example of a compile-time error and a runtime error.
> Compile-time: a missing semicolon or a type mismatch — `javac` refuses to produce bytecode.
> Runtime: dividing an `int` by zero or a `NullPointerException` — the code compiles but fails while
> running.

> [!question]- What is the classpath?
> The list of folders and jar files where the JVM looks for classes. Build tools and the IDE set it
> for you.

> [!question]- When would you reach for JShell?
> To try a line of Java quickly — an expression, a method call, an unfamiliar API — without creating
> a file or project.

## Definition of Done
- [ ] I can run the compile + run cycle by hand and explain each command.
- [ ] I can tell a compile-time error from a runtime error.
- [ ] I can explain bytecode, the JIT, and the classpath in a sentence each.
- [ ] I've used JShell to try out code.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M1 - Foundations - Reading Errors and Using the Debugger]]
