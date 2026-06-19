---
title: ORM Intro (JPA and Hibernate)
area: Databases
module: 8
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# ORM Intro (JPA and Hibernate)

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** must · **Est:** 4h
> **Why this matters:** Most Spring apps map Java objects to tables with JPA/Hibernate instead of raw
> SQL. Understanding the ORM model — and its traps — is essential before Spring Data JPA in Module 9.

## Learning Objectives
- Explain what an ORM does and the JPA/Hibernate relationship.
- Map an entity to a table with annotations.
- Recognize common ORM pitfalls.

## Learn
- [ ] Read a JPA/Hibernate intro (Baeldung "JPA introduction").
- [ ] Read about entities, the `EntityManager`, and the persistence context.

## Concepts
- [ ] **ORM** maps classes↔tables, objects↔rows. **JPA** is the specification; **Hibernate** is the
      most common implementation.
- [ ] Annotate entities: `@Entity`, `@Id`, `@GeneratedValue`, `@Column`, relationships
      (`@OneToMany`, `@ManyToOne`).
- [ ] The **persistence context** tracks managed entities; changes flush to the DB in a transaction.
- [ ] Classic pitfalls: the **N+1 query** problem, lazy-loading exceptions, and forgetting it's still
      SQL underneath — log the generated SQL.
- [ ] An ORM is a convenience, not a replacement for understanding SQL ([[M8 - Databases - SQL CRUD and Queries]]).

## Practice
**Goal:** Persist an object with JPA.
**Steps:**
- [ ] Map a `Book` entity (`@Entity`, `@Id`, `@GeneratedValue`).
- [ ] Save and load it; enable SQL logging and read the generated statements.
- [ ] Add a `@ManyToOne` relationship and observe the queries (watch for N+1).

**Record your result:**
- 

## Definition of Done
- [ ] I can map an entity and persist/load it.
- [ ] I can explain JPA vs Hibernate and the persistence context.
- [ ] I can spot the N+1 problem and know SQL still runs underneath.

## Cheatsheet (my notes)
- 

## Related
- [[M8 - Databases - Connecting from Java (JDBC)]]
- [[M9 - Spring - Spring Data JPA and Repositories]]
