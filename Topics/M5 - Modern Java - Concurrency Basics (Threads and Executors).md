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
- Run work on threads using `Runnable`/`Callable` and an `ExecutorService`.
- Explain race conditions and basic thread-safety.
- Use simple safe tools (`synchronized`, atomics, concurrent collections) correctly.

## Learn
- [ ] Read:
      [The Java Tutorials — Concurrency](https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html)
      (older site; the fundamentals — threads, synchronization, executors — still hold).
- [ ] Reference: the
      [`ExecutorService` Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ExecutorService.html)
      (read the usage examples).
- [ ] Optional: skim
      [`CompletableFuture`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html)
      — you'll see it in real code.

## Concepts
- [ ] A **thread** runs code independently; the JVM can run many at once. Prefer an
      **`ExecutorService`** (a thread pool) over creating raw `Thread`s.
- [ ] Submit work as `Runnable` (no result) or `Callable` (returns a value via a `Future`).
- [ ] *(Java 19+)* `ExecutorService` is `AutoCloseable`:
      `try (var pool = Executors.newFixedThreadPool(4)) { ... }` waits for the tasks and shuts the
      pool down.
- [ ] **Race condition**: two threads read-modify-write shared state without coordination
      (`count++`) → lost updates. The classic bug.
- [ ] Make it safe: minimize shared mutable state, prefer immutability
      ([[M5 - Modern Java - Records]]), or use `synchronized`, `AtomicInteger`, and concurrent
      collections (`ConcurrentHashMap`).
- [ ] **Deadlock**: two threads each hold a lock the other needs. Acquire locks in a consistent
      order.
- [ ] Deep details (the Java Memory Model, `volatile`, lock-free algorithms) are beyond junior scope
      — know they exist.

## Practice
**Goal:** Run concurrent work and feel a race condition.
**Steps:**
- [ ] Use an `ExecutorService` (in try-with-resources) to run several `Callable`s; collect results
      via `Future`.
- [ ] Increment a shared `int` from many threads without protection and observe the wrong total.
- [ ] Fix it with `AtomicInteger`, then alternatively with `synchronized`, and confirm the correct
      total.
- [ ] Replace a `HashMap` updated from several threads with a `ConcurrentHashMap` and `merge`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- `Runnable` vs `Callable`?
> `Runnable.run()` returns nothing and can't throw checked exceptions; `Callable.call()` returns a
> value (retrieved through a `Future`) and may throw.

> [!question]- Why does `count++` from two threads lose updates?
> It's three steps — read, add, write. Two threads can read the same old value and both write back
> value + 1, so one increment disappears.

> [!question]- Name three ways to make a shared counter thread-safe.
> `AtomicInteger`, a `synchronized` method or block, or avoiding sharing altogether (each task
> computes its part, combine the results at the end).

> [!question]- Why use an `ExecutorService` instead of `new Thread(...)` everywhere?
> It reuses a bounded pool of threads, gives you results and exceptions through `Future`s, and
> manages shutdown — raw threads are costly and easy to leak.

## Definition of Done
- [ ] I can run tasks on an `ExecutorService` and get results from `Future`.
- [ ] I can explain and reproduce a race condition, then fix it.
- [ ] I know the basic thread-safety tools and how to shut executors down.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M5 - Modern Java - Virtual Threads (Java 21)]]
