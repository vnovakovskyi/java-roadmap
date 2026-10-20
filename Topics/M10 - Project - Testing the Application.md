---
title: Testing the Application
area: Project
module: 10
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Testing the Application

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** must · **Est:** 5h
> **Why this matters:** Tests turn "it worked when I clicked it" into "it provably works". A tested
> capstone — unit, web, and database tests running in CI — demonstrates exactly the discipline
> employers look for in a junior.

## Learning Objectives
- Unit-test services with mocks.
- Write slice tests for the web and data layers.
- Write an integration test against a real database with Testcontainers.

## Learn
- [ ] Revisit [[M7 - Testing - JUnit Basics]], [[M7 - Testing - Mockito and Test Doubles]], and
      [[M7 - Testing - Assertions with AssertJ]].
- [ ] Read:
      [Spring Boot — Testing Spring Boot Applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html)
      (slice tests, `@MockitoBean`).
- [ ] Read:
      [Spring Boot — Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html)
      and
      [MockMvcTester](https://docs.spring.io/spring-framework/reference/testing/mockmvc/assertj.html).

## Concepts
- [ ] **Unit** tests for service logic with mocked repositories — fast and isolated, no Spring
      context.
- [ ] **Web slice** tests: `@WebMvcTest(BookController.class)` + `MockMvcTester` to check status
      codes, JSON, validation, and security rules; replace the service with `@MockitoBean`. *(Spring
      Boot 4)* `@MockBean` from older tutorials was removed, and slice tests need their test starter
      (e.g. `spring-boot-starter-webmvc-test`, `spring-boot-starter-data-jpa-test`).
- [ ] **Data slice** tests: `@DataJpaTest` for custom queries — against real PostgreSQL via
      Testcontainers, not an in-memory database with a different SQL dialect.
- [ ] **Integration** tests: `@SpringBootTest` + `@AutoConfigureMockMvc` boot the whole app. Picking
      Testcontainers on start.spring.io generates a `TestcontainersConfiguration` with a
      `@ServiceConnection` database for you.
- [ ] Keep to the pyramid ([[M7 - Testing - Why We Test and the Test Pyramid]]); CI runs everything
      — GitHub's Linux runners have Docker, so Testcontainers just works.

## Practice
**Goal:** A meaningful test suite running in CI.
**Steps:**
- [ ] Unit-test the service for happy and error paths with a mocked repository.
- [ ] Add `@WebMvcTest`s for one controller: success, validation error (400), not found (404), and
      an unauthorized call.
- [ ] Add a `@DataJpaTest` with Testcontainers for a custom query.
- [ ] Add one `@SpringBootTest` that creates and then fetches a resource end to end; run the whole
      suite in CI.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- `@WebMvcTest` vs `@SpringBootTest`?
> `@WebMvcTest` starts only the web layer (controllers, advice, security) — fast and focused, with
> collaborators mocked. `@SpringBootTest` starts the whole application context for end-to-end
> integration tests.

> [!question]- How do you replace a bean with a mock in a Spring Boot 4 test?
> Annotate a test field with `@MockitoBean`; Spring swaps the bean in the context for a Mockito
> mock.

> [!question]- Why test against PostgreSQL in a container instead of H2?
> H2 speaks a different SQL dialect and behaves differently; a real PostgreSQL catches dialect,
> constraint, and migration problems your production database would hit.

## Definition of Done
- [ ] I have unit tests for service logic.
- [ ] I have web-slice, data-slice, and at least one end-to-end test.
- [ ] The whole suite runs green in CI.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M10 - Project - Good Habits (Logging, Config, README)]]
