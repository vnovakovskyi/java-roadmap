---
title: Mockito and Test Doubles
area: Testing
module: 7
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Mockito and Test Doubles

> [!info] Topic
> **Area:** Testing · **Module:** 7 · **Priority:** good · **Est:** 3h
> **Why this matters:** To unit-test a class in isolation you replace its collaborators with test
> doubles. Mockito is the standard tool — and it's central to testing Spring services in Module 9.

## Learning Objectives
- Explain stubs, mocks, fakes, and when to use each.
- Create mocks with Mockito and stub their behavior.
- Verify interactions, and avoid over-mocking.

## Learn
- [ ] Read the [Mockito docs](https://site.mockito.org) "How to" intro.
- [ ] Read about `@Mock`, `@InjectMocks`, `when/thenReturn`, `verify`.

## Concepts
- [ ] **Test doubles**: *stub* (canned answers), *mock* (verifies interactions), *fake* (working
      lightweight impl, e.g. in-memory repo).
- [ ] `mock(Type.class)` or `@Mock`; stub with `when(dep.call()).thenReturn(x)`.
- [ ] Verify calls: `verify(dep).save(any())`, `verify(dep, times(1))...`.
- [ ] Inject mocks into the class under test via constructor (why DI/[[M3 - OOP - Abstraction, Interfaces and Abstract Classes]] matters).
- [ ] **Over-mocking smell**: if you mock everything, you test mocks, not behavior. Mock at real
      boundaries (DB, network), prefer real objects/fakes otherwise.

## Practice
**Goal:** Unit-test a class with a mocked dependency.
**Steps:**
- [ ] Build a `OrderService` that depends on a `PaymentGateway` interface.
- [ ] Mock the gateway, stub a success and a failure, and test both paths.
- [ ] `verify` the gateway was called with the expected arguments.

**Record your result:**
- 

## Definition of Done
- [ ] I can create and stub mocks and verify interactions.
- [ ] I can explain stub vs mock vs fake.
- [ ] I avoid over-mocking and mock at sensible boundaries.

## Cheatsheet (my notes)
- 

## Related
- [[M7 - Testing - JUnit 5 Basics]]
- [[M9 - Spring - Services and Dependency Injection]]
