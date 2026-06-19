---
title: JUnit 5 Basics
area: Testing
module: 7
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# JUnit 5 Basics

> [!info] Topic
> **Area:** Testing · **Module:** 7 · **Priority:** must · **Est:** 4h
> **Why this matters:** JUnit 5 is the standard Java testing framework. Writing and running unit
> tests is an everyday skill you'll use in every project from here on.

## Learning Objectives
- Write and run JUnit 5 tests.
- Use lifecycle and assertion methods.
- Use parameterized tests and exception assertions.

## Learn
- [ ] Read the [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/) (writing tests).
- [ ] Add JUnit 5 to a Maven and a Gradle project (`test` scope / `testImplementation`).

## Concepts
- [ ] `@Test` marks a test; the **Arrange–Act–Assert** structure keeps tests readable.
- [ ] Lifecycle: `@BeforeEach`/`@AfterEach`, `@BeforeAll`/`@AfterAll`.
- [ ] Assertions: `assertEquals`, `assertTrue`, `assertThrows`, `assertAll`.
- [ ] `@ParameterizedTest` runs one test over many inputs; `@DisplayName` for readable names.
- [ ] Name tests for behavior ("returns_zero_for_empty_list") and keep one logical assert per test.

## Practice
**Goal:** Test real logic with JUnit 5.
**Steps:**
- [ ] Write a `Calculator` and test `add`/`divide`, including the divide-by-zero case with `assertThrows`.
- [ ] Add a `@ParameterizedTest` covering several input pairs.
- [ ] Run the tests from the IDE and from the command line (`mvn test` / `./gradlew test`).

**Record your result:**
- 

## Definition of Done
- [ ] I can write, name, and run JUnit 5 tests.
- [ ] I can use lifecycle hooks and `assertThrows`.
- [ ] I can write a parameterized test.

## Cheatsheet (my notes)
- 

## Related
- [[M7 - Testing - Assertions with AssertJ]]
- [[M7 - Testing - Why We Test and the Test Pyramid]]
