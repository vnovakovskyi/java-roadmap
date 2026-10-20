---
title: Module Project (Bookshelf on PostgreSQL)
area: Databases
module: 8
status: todo
priority: good
effort: 4
tags:
  - java-roadmap
---

# Module Project (Bookshelf on PostgreSQL)

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** good · **Est:** 4h
> **Why this matters:** Version 7 moves Bookshelf from a JSON file into a real database — and proves
> the interface you created back in Module 3 was worth it: a `JdbcBookStorage` slots in without
> touching the rest of the app.

## Learning Objectives
- Back an existing app with PostgreSQL via JDBC.
- Manage the schema with Flyway.
- Keep configuration and credentials out of the code.

## Learn
- [ ] Revisit [[M8 - Databases - Connecting from Java (JDBC)]],
      [[M8 - Databases - Schema Basics and Migrations (Flyway)]], and
      [[M6 - Tooling - Docker Basics for Developers]].

## Concepts
- [ ] A `compose.yaml` that starts PostgreSQL for development.
- [ ] Flyway runs at startup through its Java API:
      `Flyway.configure().dataSource(url, user, password).load().migrate()`.
- [ ] `JdbcBookStorage implements BookStorage` with `PreparedStatement`s; multi-step operations in
      one transaction.
- [ ] Connection settings come from environment variables (e.g. `BOOKSHELF_DB_URL`), never
      hard-coded.
- [ ] `InMemoryBookStorage` stays — it's now a fast fake for unit tests.
- [ ] Optional: an integration test of `JdbcBookStorage` against a real PostgreSQL started by
      [Testcontainers](https://testcontainers.com/guides/).

## Practice
**Goal:** Bookshelf v7 — data in PostgreSQL, schema under version control.
**Steps:**
- [ ] Add `compose.yaml`, the PostgreSQL driver, and Flyway; write `V1__create_book.sql`.
- [ ] Implement `JdbcBookStorage` and switch the app to it based on configuration.
- [ ] Read connection settings from environment variables; document them in the README.
- [ ] Optional: test `JdbcBookStorage` with Testcontainers in CI.
- [ ] Commit, push, and tag `v7`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Which parts of Bookshelf changed when you added the database?
> A new `JdbcBookStorage`, the startup wiring (Flyway, connection settings), and the build file. The
> menu, commands, and stats code didn't change — they only know `BookStorage`.

> [!question]- Why read the database URL and password from environment variables?
> So the same build runs anywhere (laptop, CI, production) and credentials never end up in Git.

> [!question]- How can you test `JdbcBookStorage` without a shared database?
> Start a throwaway PostgreSQL container per test run with Testcontainers, so the tests are isolated
> and repeatable — locally and in CI.

## Definition of Done
- [ ] Bookshelf stores its data in PostgreSQL through JDBC.
- [ ] The schema is created by Flyway migrations.
- [ ] Credentials come from the environment; the code is tagged `v7`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M9 - Spring - HTTP and REST Fundamentals]]
