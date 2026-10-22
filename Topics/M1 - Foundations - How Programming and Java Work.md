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
- Explain what an LTS release is and why this roadmap uses Java 25.

## Learn
- [ ] Read:
      [dev.java — Getting Started with Java](https://dev.java/learn/first-steps/first-java-code/getting-started/)
      — the official first-steps tutorial.
- [ ] Read: [dev.java — Java Platform Evolution](https://dev.java/learn/first-steps/evolution/) —
      how Java versions and the six-month release cadence work.
- [ ] Skim:
      [Oracle Java SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
      — which versions are LTS and for how long.
- [ ] Read the JVM/JRE/JDK callout in [[Tools & Setup]].

## Concepts
- [ ] A program is a set of instructions; you write **source code** (`.java`), which gets turned
      into **bytecode** (`.class`).
- [ ] The **JVM** (Java Virtual Machine) runs bytecode. Because every platform has its own JVM, the
      same bytecode runs on Windows, macOS, and Linux — "write once, run anywhere".
- [ ] **JDK** = JRE + compiler/tools; **JRE** = JVM + libraries. You develop with the JDK.
- [ ] Compiled vs interpreted: Java compiles to bytecode, then the JVM runs (and just-in-time
      compiles) it. You don't need the deep version yet — just the picture.
- [ ] Versions: a new Java release ships every March and September; every two years one is a
      **Long-Term-Support (LTS)** release (17, 21, 25 — the next is 29 in 2027). Learn on the
      current LTS. Newer features are marked *(Java NN+)* in this vault.
- [ ] "Java" is one language and platform; builds like Eclipse Temurin, Oracle JDK, or Amazon
      Corretto are all the same OpenJDK underneath. This roadmap uses Temurin. (And Java has nothing
      to do with JavaScript.)

## Practice
**Goal:** Cement the model in your own words.
**Steps:**
- [ ] Draw a simple diagram: `your .java file → javac → .class bytecode → JVM → runs on any OS`.
- [ ] Write 3–4 sentences explaining the diagram to an imaginary non-programmer.
- [ ] Find out which Java version is the newest release and which is the newest LTS today.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What does the JVM do, and why does that make Java portable?
> It loads and runs bytecode (`.class` files). Every operating system has its own JVM, so the same
> bytecode runs unchanged on Windows, macOS, and Linux.

> [!question]- What's the difference between the JDK and the JRE?
> The JRE (JVM + core libraries) can only run Java programs. The JDK adds the compiler (`javac`) and
> developer tools — you need the JDK to write Java.

> [!question]- What is bytecode?
> An intermediate, platform-independent instruction format produced by `javac`. It isn't machine
> code: the JVM interprets it and JIT-compiles the hot parts into native code.

> [!question]- What is an LTS release, and which one does this roadmap use?
> A Long-Term-Support release that gets years of updates; one arrives every two years. This roadmap
> uses Java 25 (LTS since September 2025).

## Definition of Done
- [ ] I can explain what the JVM, JRE, and JDK each do.
- [ ] I can explain why Java runs on any operating system.
- [ ] I understand the path from source code to a running program.
- [ ] I know what LTS means and which Java version I'm learning.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M1 - Foundations - Set Up and Verify Your Environment]]
