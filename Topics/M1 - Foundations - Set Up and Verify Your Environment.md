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
> **Why this matters:** Before any coding, your toolchain must actually work. The full install guide
> lives in **[[Tools & Setup]]** — this topic is the quick **verify** step: confirm Java and your
> IDE run, and learn enough to fix a "command not found".

> [!tip] Where to install
> Do the installs in **[[Tools & Setup]]** (sections 1–2: JDK + IDE). Come back here to verify. Git
> and the build tools come later in Module 6.

## Learning Objectives
- Confirm JDK 21 is installed and runs from the command line.
- Confirm your IDE can run a Java file.
- Know where to look when a tool "isn't found".

## Learn
- [ ] Finish **[[Tools & Setup]]** sections 1–2 (JDK + IDE) if you haven't yet.
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

## Definition of Done
- [ ] `java -version` and `javac -version` both show 21.
- [ ] I ran a program from the IDE and saw output.
- [ ] I completed the checklist at the bottom of [[Tools & Setup]] (JDK + IDE parts).

## Next
- Next: [[M1 - Foundations - The Command Line Basics]]
