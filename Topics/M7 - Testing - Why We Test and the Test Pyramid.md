---
title: Why We Test and the Test Pyramid
area: Testing
module: 7
status: todo
priority: must
effort: 2
tags:
  - java-roadmap
---

# Why We Test and the Test Pyramid

> [!info] Topic
> **Area:** Testing · **Module:** 7 · **Priority:** must · **Est:** 2h
> **Why this matters:** Tests let you change code without fear and prove it works. "Can you write
> tests?" is a standard junior interview question — and untested code is a liability on any team.

## Learning Objectives
- Explain why automated tests matter.
- Describe the test pyramid and what each layer is for.
- Recognize what makes a good vs flaky test.

## Learn
- [ ] Read a short "test pyramid" explainer (Martin Fowler's article).
- [ ] Read about unit vs integration vs end-to-end tests.

## Concepts
- [ ] Tests give a fast feedback loop, catch regressions, and document intended behavior.
- [ ] **Pyramid**: many fast **unit** tests at the base, fewer **integration** tests in the middle,
      a handful of **end-to-end** tests at the top.
- [ ] Higher layers are slower and more brittle — keep them few; push logic down to unit tests.
- [ ] Good tests: fast, isolated, deterministic, readable, and test behavior (not implementation).
- [ ] **Flaky** tests (random failures) erode trust — usually caused by time, randomness, ordering, or
      shared state.

## Practice
**Goal:** Plan a testing approach.
**Steps:**
- [ ] For a small app idea, list what you'd cover with unit vs integration vs e2e tests.
- [ ] Identify one piece of logic that belongs in a fast unit test.
- [ ] Note one likely source of flakiness and how you'd avoid it.

**Record your result:**
- 

## Definition of Done
- [ ] I can explain the value of automated testing.
- [ ] I can place a test at the right pyramid layer.
- [ ] I can describe what makes a test good or flaky.

## Cheatsheet (my notes)
- 

## Related
- [[M7 - Testing - JUnit 5 Basics]]
- [[M7 - Testing - Writing Testable Code (Intro to TDD)]]
