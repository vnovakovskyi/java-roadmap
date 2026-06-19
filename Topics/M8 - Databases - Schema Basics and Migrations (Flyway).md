---
title: Schema Basics and Migrations (Flyway)
area: Databases
module: 8
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Schema Basics and Migrations (Flyway)

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** good · **Est:** 2h
> **Why this matters:** Production schemas change over time. Migrations version your database the way
> Git versions code — repeatable, reviewable, and safe across environments.

## Learning Objectives
- Explain why schema migrations exist.
- Write and run Flyway migrations.
- Understand versioned, ordered, immutable migration files.

## Learn
- [ ] Read the [Flyway "Getting Started"](https://flywaydb.org/documentation/) guide.
- [ ] Read how Spring Boot auto-runs Flyway on startup (preview of Module 9).

## Concepts
- [ ] Letting an ORM auto-create tables is fine for demos but not production — use migrations.
- [ ] Flyway runs **versioned** SQL files (`V1__init.sql`, `V2__add_column.sql`) in order, once each,
      tracked in a history table.
- [ ] Migrations are **immutable** once applied — fix forward with a new migration, don't edit old ones.
- [ ] Keep migrations small and reviewable; they live in version control next to the code.
- [ ] Liquibase is a common alternative; the principles are the same.

## Practice
**Goal:** Evolve a schema with migrations.
**Steps:**
- [ ] Add Flyway to a project; write `V1__create_book.sql`.
- [ ] Add `V2__add_published_year.sql` to alter the table; run and verify both applied.
- [ ] Inspect the Flyway history table.

**Record your result:**
- 

## Definition of Done
- [ ] I can write and run ordered Flyway migrations.
- [ ] I understand migrations are immutable and fixed forward.
- [ ] I know why migrations beat auto-DDL in production.

## Cheatsheet (my notes)
- 

## Related
- [[M8 - Databases - ORM Intro (JPA and Hibernate)]]
- [[M9 - Spring - Spring Data JPA and Repositories]]
