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
> **Why this matters:** Tests let you change code without fear and prove it works. "How do you test
> your code?" is a standard junior interview question — and untested code is a liability on any
> team.

## Learning Objectives
- Explain why automated tests matter.
- Describe the test pyramid and what each layer is for.
- Recognize what makes a good vs a flaky test.

## Learn
- [ ] Read: [Martin Fowler — Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html) (short).
- [ ] Read:
      [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
      (Ham Vocke) — long; read the first half now, the rest after Module 9.

## Concepts
- [ ] Tests give a fast feedback loop, catch regressions, and document intended behavior.
- [ ] **Pyramid**: many fast **unit** tests at the base, fewer **integration** tests in the middle,
      a handful of **end-to-end** tests at the top.
- [ ] Higher layers are slower and more brittle — keep them few; push logic down to where unit tests
      can reach it.
- [ ] Good tests are fast, isolated, repeatable, self-checking, and test behavior (not
      implementation details).
- [ ] **Flaky** tests (random failures) erode trust — usually caused by time, randomness, ordering,
      shared state, or real network calls.

## Practice
**Goal:** Plan a testing approach.
**Steps:**
- [ ] For your Bookshelf app, list what you'd cover with unit vs integration vs end-to-end tests.
- [ ] Identify one piece of logic that belongs in a fast unit test, and one thing only an
      integration test can prove.
- [ ] Note two likely sources of flakiness and how you'd avoid them.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why should most tests be unit tests?
> They're fast, precise about what broke, and cheap to write and run — so you can run thousands on
> every change. Higher-level tests are slower and break for many reasons.

> [!question]- What does an integration test prove that a unit test can't?
> That parts work together for real — e.g. your SQL against an actual database, or JSON mapping
> through the web layer.

> [!question]- Name three common causes of flaky tests.
> Dependence on the current time or random values, tests that share state or depend on run order,
> and calls to real external services or networks.

## Definition of Done
- [ ] I can explain the value of automated testing.
- [ ] I can place a test at the right pyramid layer.
- [ ] I can describe what makes a test good or flaky.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M7 - Testing - JUnit Basics]]
