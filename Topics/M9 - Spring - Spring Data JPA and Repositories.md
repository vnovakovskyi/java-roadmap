---
title: Spring Data JPA and Repositories
area: Spring
module: 9
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Spring Data JPA and Repositories

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 4h
> **Why this matters:** Spring Data JPA removes nearly all boilerplate persistence code — you declare
> an interface and get CRUD for free. It's how most Spring apps talk to a database.

## Learning Objectives
- Define entities and `JpaRepository` interfaces.
- Use derived query methods and custom queries.
- Wire persistence into the service layer.

## Learn
- [ ] Read the Spring "Accessing Data with JPA" guide.
- [ ] Read about `JpaRepository` and derived query method naming.

## Concepts
- [ ] Map entities with JPA annotations (recap [[M8 - Databases - ORM Intro (JPA and Hibernate)]]).
- [ ] Declare `interface BookRepository extends JpaRepository<Book, Long>` — get `save`, `findById`,
      `findAll`, `delete` automatically.
- [ ] **Derived queries** from method names: `findByAuthor(String author)`, `findByTitleContaining(...)`.
- [ ] Custom queries with `@Query` (JPQL or native SQL) when names get awkward.
- [ ] Inject the repository into a `@Service`; remember the N+1 trap and enable SQL logging.

## Practice
**Goal:** Persist the CRUD app for real.
**Steps:**
- [ ] Replace the in-memory list with a `JpaRepository` backed by a database.
- [ ] Add a derived query (e.g. `findByAuthor`) and use it from the service.
- [ ] Turn on SQL logging and confirm the queries are what you expect.

## Definition of Done
- [ ] I can define entities and Spring Data repositories.
- [ ] I can write derived and custom queries.
- [ ] I wired persistence cleanly into the service layer.

## Next
- Next: [[M9 - Spring - Validation and Error Handling]]
