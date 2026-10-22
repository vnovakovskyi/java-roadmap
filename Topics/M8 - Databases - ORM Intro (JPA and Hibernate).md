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
> **Why this matters:** Most Spring apps map Java objects to tables with JPA/Hibernate instead of
> writing SQL by hand. Understanding the ORM model — and its traps — is essential before Spring Data
> JPA in Module 9.

## Learning Objectives
- Explain what an ORM does and the JPA/Hibernate relationship.
- Map an entity to a table with annotations.
- Recognize the common ORM pitfalls.

## Learn
- [ ] Read: the "Introduction to Hibernate" guide linked from
      [Hibernate ORM documentation](https://hibernate.org/orm/documentation/) (current version) —
      chapters 1–3.
- [ ] Read: [The N+1 query problem](https://vladmihalcea.com/n-plus-1-query-problem/) (Vlad
      Mihalcea).

## Concepts
- [ ] **ORM** maps classes↔tables, objects↔rows. **JPA** (now *Jakarta Persistence*) is the
      specification; **Hibernate** is the most common implementation. Imports are
      `jakarta.persistence.*` — tutorials using `javax.persistence.*` are pre-2022 and outdated.
- [ ] Annotate entities: `@Entity`, `@Id`, `@GeneratedValue`, `@Column`, relationships
      (`@ManyToOne`, `@OneToMany`). Entities need a no-arg constructor and mutable state — so
      they're classes, not records.
- [ ] The **persistence context** tracks managed entities; changes are detected (dirty checking) and
      flushed to the database when the transaction commits.
- [ ] Classic pitfalls: the **N+1 query** problem (fix with a fetch join or entity graph),
      `LazyInitializationException` (accessing a lazy relation after the transaction closed), and
      forgetting it's still SQL underneath — always log the generated SQL.
- [ ] An ORM is a convenience, not a replacement for understanding SQL
      ([[M8 - Databases - SQL CRUD and Queries]]).

## Practice
**Goal:** Persist objects with JPA and watch the SQL.
**Steps:**
- [ ] Map a `Book` entity (`@Entity`, `@Id`, `@GeneratedValue`) and an `Author` with `@ManyToOne`
      from `Book`.
- [ ] Save and load books (the Hibernate guide shows a minimal setup); enable SQL logging and read
      the generated statements.
- [ ] Load all books and print each author's name — count the queries (N+1), then fix it with a
      `join fetch` query.
- [ ] Change a loaded entity inside a transaction without calling any "update" method and see the
      `UPDATE` appear.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- JPA vs Hibernate?
> JPA (Jakarta Persistence) is the standard API — annotations and interfaces. Hibernate is an
> implementation of it (the most popular one), plus extra features.

> [!question]- What is the N+1 query problem, and how do you fix it?
> Loading N entities with one query, then triggering one more query per entity for a lazy relation —
> N+1 queries in total. Fix it by fetching the relation in the first query (`join fetch`, an entity
> graph).

> [!question]- Why did changing a field produce an `UPDATE` without calling `save`?
> The entity was managed by the persistence context; dirty checking detected the change and flushed
> it when the transaction committed.

> [!question]- Why are JPA entities usually not records?
> JPA needs a no-arg constructor, mutable fields, and proxies for lazy loading; records are final
> and immutable.

## Definition of Done
- [ ] I can map an entity and persist/load it.
- [ ] I can explain JPA vs Hibernate and the persistence context.
- [ ] I can spot and fix the N+1 problem and know SQL still runs underneath.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M8 - Databases - Schema Basics and Migrations (Flyway)]]
