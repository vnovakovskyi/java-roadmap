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
> **Why this matters:** Production schemas change over time. Migrations version your database the
> way Git versions code — repeatable, reviewable, and safe across environments.

## Learning Objectives
- Explain why schema migrations exist.
- Write and run Flyway migrations.
- Understand versioned, ordered, immutable migration files.

## Learn
- [ ] Read:
      [Quickstart — How Flyway Works](https://documentation.red-gate.com/fd/quickstart-how-flyway-works-184127223.html).
- [ ] Read:
      [Flyway — Migrations](https://documentation.red-gate.com/flyway/flyway-concepts/migrations)
      (naming and versioning rules).

## Concepts
- [ ] Letting an ORM auto-create tables (`ddl-auto`) is fine for demos but not production — use
      migrations, and let Hibernate only `validate` the schema.
- [ ] Flyway runs **versioned** SQL files (`V1__init.sql`, `V2__add_column.sql`) in order, once
      each, tracked in the `flyway_schema_history` table.
- [ ] Migrations are **immutable** once applied — fix forward with a new migration, never edit an
      old one.
- [ ] Keep migrations small and reviewable; they live in version control next to the code
      (`src/main/resources/db/migration`).
- [ ] For PostgreSQL also add the `flyway-database-postgresql` module. *(Spring Boot 4)*
      Auto-running migrations at startup needs `spring-boot-starter-flyway` — start.spring.io adds
      both when you pick Flyway.
- [ ] Liquibase is a common alternative; the principles are the same.

## Practice
**Goal:** Evolve a schema with migrations.
**Steps:**
- [ ] Add Flyway to a project; write `V1__create_book.sql`.
- [ ] Add `V2__add_published_year.sql` to alter the table; run and verify both applied.
- [ ] Inspect `flyway_schema_history`, then edit `V1` and see Flyway refuse to run (checksum
      mismatch) — revert the edit.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why not let Hibernate create the schema in production?
> It can't express careful changes (renames, data migrations), isn't reviewable, and can destroy
> data. Migrations are explicit, versioned, and repeatable.

> [!question]- You need to fix a mistake in `V3__add_index.sql`, which already ran in production. What do you do?
> Write a new migration (`V4__…`) that corrects it. Applied migrations are immutable — editing them
> breaks the checksum and the history.

> [!question]- How does Flyway know which migrations have run?
> It records each applied version and checksum in the `flyway_schema_history` table.

## Definition of Done
- [ ] I can write and run ordered Flyway migrations.
- [ ] I understand migrations are immutable and fixed forward.
- [ ] I know why migrations beat auto-DDL in production.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M8 - Databases - Module Project (Bookshelf on PostgreSQL)]]
