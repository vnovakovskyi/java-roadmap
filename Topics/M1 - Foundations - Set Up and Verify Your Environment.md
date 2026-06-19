---
title: Set Up and Verify Your Environment
area: Foundations
module: 1
status: todo
priority: must
effort: 2
tags:
  - java-roadmap
---

# Set Up and Verify Your Environment

> [!info] Topic
> **Area:** Foundations · **Module:** 1 · **Priority:** must · **Est:** 2h
> **Why this matters:** You can't learn to code without a working toolchain. This topic makes sure
> Java, an IDE, and the basics are installed and provably working before you go further.

## Learning Objectives
- Have JDK 21 installed and confirmed from the command line.
- Have an IDE installed and able to run a Java file.
- Know where to look when a tool "isn't found".

## Learn
- [ ] Work through **[[Tools & Setup]]** sections 1–2 (JDK + IDE). Git and build tools come in Module 6.
- [ ] Skim what a `PATH` is (why your terminal can or can't find `java`).

## Concepts
- [ ] The JDK provides two key commands: `javac` (compile) and `java` (run).
- [ ] Your terminal finds commands via the `PATH` environment variable; a managed installer
      (SDKMAN/Homebrew) wires this up for you.
- [ ] An IDE bundles an editor, the compiler, a runner, and a debugger in one place.

## Practice
**Goal:** Prove the environment works end-to-end.
**Steps:**
- [ ] Run `java -version` and `javac -version`; confirm both report 21.
- [ ] In your IDE, create a new project and run a one-line program that prints something.
- [ ] Intentionally break it (delete a semicolon), see the error, fix it, re-run.

**Record your result:**
- 

## Definition of Done
- [ ] `java -version` and `javac -version` both show 21.
- [ ] I ran a program from the IDE and saw output.
- [ ] I completed the checklist at the bottom of [[Tools & Setup]] (JDK + IDE parts).

## Cheatsheet (my notes)
- 

## Related
- [[Tools & Setup]]
- [[M1 - Foundations - Your First Java Program]]
