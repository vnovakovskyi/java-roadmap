---
title: Virtual Threads (Java 21)
area: Modern Java
module: 5
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Virtual Threads (Java 21)

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** good · **Est:** 2h
> **Why this matters:** Virtual threads (finalized in Java 21) make it cheap to run huge numbers of
> concurrent tasks, and they're increasingly the default in modern Spring apps. A short, modern peek
> that builds on the concurrency basics.

## Learning Objectives
- Explain what a virtual thread is and how it differs from a platform thread.
- Create and run virtual threads.
- Know when they help (and that thread-safety rules still apply).

## Learn
- [ ] Read the Java 21 virtual threads intro (JEP 444 summary or a beginner article).
- [ ] Read how Spring Boot 3.2+ can run on virtual threads with a single property.

## Concepts
- [ ] A **platform thread** maps to an OS thread (heavy, limited in number). A **virtual thread** is
      lightweight and managed by the JVM — you can have millions.
- [ ] Best for **blocking I/O-bound** work (DB calls, HTTP); not a speed-up for CPU-bound work.
- [ ] Create via `Thread.ofVirtual().start(...)` or `Executors.newVirtualThreadPerTaskExecutor()`.
- [ ] You usually keep the same blocking code style — the JVM handles the rest.
- [ ] **Thread-safety still applies**: virtual threads don't remove race conditions (see
      [[M5 - Modern Java - Concurrency Basics (Threads and Executors)]]).

## Practice
**Goal:** Run tasks on virtual threads.
**Steps:**
- [ ] Launch a few thousand virtual threads that each sleep briefly; note how cheap it is.
- [ ] Use `Executors.newVirtualThreadPerTaskExecutor()` to run tasks and collect results.
- [ ] (Optional) Flip a Spring Boot app to virtual threads via `spring.threads.virtual.enabled=true`.

**Record your result:**
- 

## Definition of Done
- [ ] I can explain virtual vs platform threads and when each helps.
- [ ] I can create and run virtual threads.
- [ ] I understand thread-safety rules are unchanged.

## Cheatsheet (my notes)
- 

## Related
- [[M5 - Modern Java - Concurrency Basics (Threads and Executors)]]
- [[M9 - Spring - Spring Boot Intro and Project Setup]]
