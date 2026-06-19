---
title: Writing Testable Code (Intro to TDD)
area: Testing
module: 7
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Writing Testable Code (Intro to TDD)

> [!info] Topic
> **Area:** Testing · **Module:** 7 · **Priority:** good · **Est:** 3h
> **Why this matters:** Testable code is well-designed code. Learning to write it — and trying the
> red-green-refactor TDD loop — improves your design instincts, not just your test coverage.

## Learning Objectives
- Identify what makes code hard vs easy to test.
- Apply dependency injection to enable testing.
- Practice the TDD red-green-refactor cycle once.

## Learn
- [ ] Read a short intro to TDD (red → green → refactor).
- [ ] Read about dependency injection as a testability enabler.

## Concepts
- [ ] Hard to test: hidden dependencies (`new` inside methods), static/global state, doing too much,
      side effects mixed with logic.
- [ ] Easy to test: small pure functions, dependencies passed in (DI), clear inputs/outputs.
- [ ] **DI**: pass collaborators via the constructor so tests can inject fakes/mocks (ties to Module 9's
      Spring DI).
- [ ] **TDD loop**: write a failing test (red) → minimal code to pass (green) → clean up (refactor),
      tests still green.
- [ ] Separate pure logic from I/O so the logic is trivially unit-testable.

## Practice
**Goal:** Build one feature test-first.
**Steps:**
- [ ] Pick a small function (e.g. a price-with-discount calculator).
- [ ] Write a failing test, make it pass, then refactor — repeat for 2–3 cases.
- [ ] Refactor a class with a `new`-ed dependency to take it via the constructor; test it with a mock.

**Record your result:**
- 

## Definition of Done
- [ ] I can spot and fix common testability problems.
- [ ] I use constructor injection to make code testable.
- [ ] I completed at least one red-green-refactor cycle.

## Cheatsheet (my notes)
- 

## Related
- [[M7 - Testing - Mockito and Test Doubles]]
- [[M9 - Spring - Services and Dependency Injection]]
