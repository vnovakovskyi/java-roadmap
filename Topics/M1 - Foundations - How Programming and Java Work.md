---
title: How Programming and Java Work
area: Foundations
module: 1
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# How Programming and Java Work

> [!info] Topic
> **Area:** Foundations · **Module:** 1 · **Priority:** must · **Est:** 3h
> **Why this matters:** Before writing a line of code, you need a mental model of what a program is
> and how Java turns your text into something a computer runs. This makes everything later click.

## Learning Objectives
- Explain what a program is and what "source code" means.
- Describe the role of the JVM, JRE, and JDK and how they relate.
- Explain in one sentence why Java is "write once, run anywhere".

## Learn
- [ ] Read: [dev.java — "Getting Started"](https://dev.java/learn/getting-started/) intro.
- [ ] Watch a short "what is the JVM" explainer (any reputable 10-min video).
- [ ] Read the JVM/JRE/JDK distinction (e.g. the callout in [[Tools & Setup]]).

## Concepts
- [ ] A program is a set of instructions; you write **source code** (`.java`), which gets turned
      into **bytecode** (`.class`).
- [ ] The **JVM** (Java Virtual Machine) runs bytecode. Because every platform has its own JVM, the
      same bytecode runs on Windows, macOS, and Linux — "write once, run anywhere".
- [ ] **JDK** = JRE + compiler/tools; **JRE** = JVM + libraries. You develop with the JDK.
- [ ] Compiled vs interpreted: Java compiles to bytecode, then the JVM runs (and just-in-time
      compiles) it. You don't need the deep version yet — just the picture.

## Practice
**Goal:** Cement the model in your own words.
**Steps:**
- [ ] Draw a simple diagram: `your .java file → javac → .class bytecode → JVM → runs on any OS`.
- [ ] Write 3–4 sentences explaining the diagram to an imaginary non-programmer.

## Definition of Done
- [ ] I can explain what the JVM, JRE, and JDK each do.
- [ ] I can explain why Java runs on any operating system.
- [ ] I understand the path from source code to a running program.

## Next
- Next: [[M1 - Foundations - Set Up and Verify Your Environment]]
