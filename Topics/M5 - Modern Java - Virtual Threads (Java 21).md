---
title: Virtual Threads (Java 21)
area: Modern Java
module: 5
status: todo
priority: optional
effort: 2
tags:
  - java-roadmap
---

# Virtual Threads (Java 21)

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** optional · **Est:** 2h
> **Why this matters:** Virtual threads (final since Java 21) make it cheap to run huge numbers of
> concurrent tasks with plain blocking code, and they're increasingly common in modern Spring apps.
> A short, modern peek that builds on the concurrency basics.

## Learning Objectives
- Explain what a virtual thread is and how it differs from a platform thread.
- Create and run virtual threads.
- Know when they help (and that thread-safety rules still apply).

## Learn
- [ ] Read: [dev.java — Virtual Threads](https://dev.java/learn/api/virtual-threads/).
- [ ] Reference:
      [Virtual Threads](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html) (Oracle
      core libraries guide) and [JEP 444](https://openjdk.org/jeps/444).

## Concepts
- [ ] A **platform thread** maps to an OS thread (heavy, limited in number). A **virtual thread** is
      lightweight and managed by the JVM — you can have millions.
- [ ] Best for **blocking I/O-bound** work (DB calls, HTTP); not a speed-up for CPU-bound work.
- [ ] Create via `Thread.ofVirtual().start(...)` or `Executors.newVirtualThreadPerTaskExecutor()`.
      Don't pool them — one per task is the idea; limit concurrency with a `Semaphore` if a resource
      needs it.
- [ ] You keep the same blocking code style. *(Java 24+)* Blocking inside `synchronized` no longer
      pins a virtual thread ([JEP 491](https://openjdk.org/jeps/491)), so older advice to replace
      `synchronized` with `ReentrantLock` is mostly obsolete.
- [ ] In Spring Boot, one property switches request handling to virtual threads:
      `spring.threads.virtual.enabled=true`.
- [ ] **Thread-safety still applies**: virtual threads don't remove race conditions (see
      [[M5 - Modern Java - Concurrency Basics (Threads and Executors)]]). Related APIs to know by
      name: scoped values (final in Java 25) and structured concurrency (still a preview).

## Practice
**Goal:** Run tasks on virtual threads.
**Steps:**
- [ ] Launch 10,000 virtual threads that each sleep for a second; time the whole run.
- [ ] Try the same with a fixed pool of 100 platform threads and compare.
- [ ] Use `Executors.newVirtualThreadPerTaskExecutor()` to run tasks and collect results.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Platform thread vs virtual thread?
> A platform thread wraps an OS thread — expensive, so you can only have thousands. A virtual thread
> is scheduled by the JVM onto a few carrier threads — cheap, so you can have millions.

> [!question]- When do virtual threads help, and when don't they?
> They help when tasks spend most of their time waiting on I/O. They don't make CPU-heavy
> computation faster.

> [!question]- Should you put virtual threads in a pool?
> No. They're cheap to create — use one per task. If you must limit access to a resource, use a
> `Semaphore`.

## Definition of Done
- [ ] I can explain virtual vs platform threads and when each helps.
- [ ] I can create and run virtual threads.
- [ ] I understand thread-safety rules are unchanged.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M5 - Modern Java - Module Project (Bookshelf Stats and Saving)]]
