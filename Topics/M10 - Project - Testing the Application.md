---
title: Testing the Application
area: Project
module: 10
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Testing the Application

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** must · **Est:** 4h
> **Why this matters:** Tests turn "it worked when I clicked it" into "it provably works". A tested
> capstone demonstrates exactly the discipline employers look for in a junior.

## Learning Objectives
- Unit-test services with mocks.
- Write a slice/integration test for the web layer.
- Run the suite from the build tool.

## Learn
- [ ] Revisit [[M7 - Testing - JUnit 5 Basics]], [[M7 - Testing - Mockito and Test Doubles]],
      and [[M7 - Testing - Assertions with AssertJ]].
- [ ] Read about `@SpringBootTest` and `@WebMvcTest` (and Testcontainers as an optional next step).

## Concepts
- [ ] **Unit** tests for service logic with mocked repositories — fast and isolated.
- [ ] **Web slice** tests with `@WebMvcTest` + `MockMvc` to verify endpoints, status, and JSON.
- [ ] **Integration** tests with `@SpringBootTest` boot the context; use an H2 or Testcontainers DB.
- [ ] Keep to the pyramid ([[M7 - Testing - Why We Test and the Test Pyramid]]): many unit, fewer
      integration.
- [ ] Run via `mvn test` / `./gradlew test`; make tests part of your build.

## Practice
**Goal:** A meaningful test suite.
**Steps:**
- [ ] Unit-test the service for one happy path and one error path with a mocked repository.
- [ ] Add a `@WebMvcTest` for one endpoint asserting status + JSON.
- [ ] Run the whole suite from the build tool and make it green.

## Definition of Done
- [ ] I have unit tests for service logic.
- [ ] I have at least one web-layer test.
- [ ] The suite runs green from the build tool.

## Next
- Next: [[M10 - Project - Good Habits (Logging, Config, README)]]
