---
title: Concurrency Basics (Threads and Executors)
area: Modern Java
module: 5
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Concurrency Basics (Threads and Executors)

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** must · **Est:** 5h
> **Why this matters:** Servers handle many requests at once, so real Java runs concurrently. You
> don't need to be an expert, but a junior must understand threads, how to run work on a pool, and
> why shared mutable state is dangerous. This is core knowledge and a frequent interview topic.

## Learning Objectives
- Run work on threads using `Runnable` and an `ExecutorService`.
- Explain race conditions and basic thread-safety.
- Use simple safe tools (`synchronized`, atomics, concurrent collections) correctly.

## Learn
- [ ] Read a beginner concurrency intro (e.g. Baeldung "Java concurrency" overview).
- [ ] Read about `ExecutorService`, `Future`, and `Callable`.

## Concepts
- [ ] A **thread** runs code independently; the JVM can run many at once. Prefer an
      **`ExecutorService`** (a thread pool) over creating raw `Thread`s.
- [ ] Submit work as `Runnable` (no result) or `Callable` (returns a `Future`).
- [ ] **Race condition**: two threads touch shared mutable state without coordination → corrupted
      results. The classic bug.
- [ ] Make it safe: minimize shared mutable state, prefer immutability
      ([[M5 - Modern Java - Records]]), use `synchronized`, `java.util.concurrent.atomic`
      (e.g. `AtomicInteger`), or concurrent collections (`ConcurrentHashMap`).
- [ ] Always **shut down** an executor; beware deadlocks (two locks waited on in opposite order).
- [ ] Deep details (the Java Memory Model, locks, `CompletableFuture`) are beyond junior — know the
      basics and that they exist.

## Practice
**Goal:** Run concurrent work and feel a race condition.
**Steps:**
- [ ] Use an `ExecutorService` to run several tasks; collect results via `Future`.
- [ ] Increment a shared `int` from many threads without protection and observe the wrong total.
- [ ] Fix it with `AtomicInteger` (or `synchronized`) and confirm the correct total.

## Definition of Done
- [ ] I can run tasks on an `ExecutorService` and get results from `Future`.
- [ ] I can explain and reproduce a race condition, then fix it.
- [ ] I know basic thread-safety tools and to shut executors down.

## Next
- Next: [[M5 - Modern Java - Virtual Threads (Java 21)]]
