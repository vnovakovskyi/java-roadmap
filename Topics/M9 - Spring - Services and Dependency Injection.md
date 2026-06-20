---
title: Services and Dependency Injection
area: Spring
module: 9
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Services and Dependency Injection

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 4h
> **Why this matters:** Dependency injection is the heart of Spring. It's how the framework wires your
> objects together — and the reason your code stays decoupled and testable (Module 7 pays off here).

## Learning Objectives
- Explain inversion of control and dependency injection.
- Use `@Service`, `@Component`, `@Repository` and constructor injection.
- Structure an app into controller → service → repository layers.

## Learn
- [ ] Read the Spring "IoC container / beans" reference intro.
- [ ] Read about constructor injection vs field injection (and why constructor wins).

## Concepts
- [ ] **IoC**: the framework creates and wires objects (beans); you declare needs, Spring supplies them.
- [ ] Stereotypes: `@Component` (generic), `@Service` (business logic), `@Repository` (data access);
      `@Configuration`/`@Bean` for manual wiring.
- [ ] **Constructor injection** (preferred): dependencies are `final`, required, and easy to mock in
      tests — connects to [[M7 - Testing - Writing Testable Code (Intro to TDD)]] and
      [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]].
- [ ] Typical layering: **Controller** (HTTP) → **Service** (logic) → **Repository** (persistence).
- [ ] Beans are singletons by default; keep them stateless.

## Practice
**Goal:** Introduce a service layer.
**Steps:**
- [ ] Extract business logic from the controller into a `@Service`.
- [ ] Inject the service into the controller via the constructor.
- [ ] Unit-test the service with a mocked dependency ([[M7 - Testing - Mockito and Test Doubles]]).

## Definition of Done
- [ ] I can explain IoC/DI and use constructor injection.
- [ ] I can split an app into controller/service/repository layers.
- [ ] My services are testable in isolation.

## Next
- Next: [[M9 - Spring - Spring Data JPA and Repositories]]
