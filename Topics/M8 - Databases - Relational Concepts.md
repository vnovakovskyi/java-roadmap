---
title: Relational Concepts
area: Databases
module: 8
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Relational Concepts

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** must · **Est:** 3h
> **Why this matters:** Almost every backend stores data in a relational database. Understanding
> tables, keys, and relationships is the foundation for SQL, JDBC, and JPA in the rest of this
> module.

## Learning Objectives
- Explain tables, rows, columns, and data types.
- Use primary and foreign keys to model relationships.
- Describe one-to-many and many-to-many relationships.

## Learn
- [ ] Read: the [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html), Part I
      ("Getting Started") — the official, concise intro.
- [ ] Alternative: the [Neon PostgreSQL Tutorial](https://neon.com/postgresql/tutorial) — many
      small, example-driven pages.
- [ ] Set up: run PostgreSQL in Docker ([[M6 - Tooling - Docker Basics for Developers]]) and connect
      with a GUI like [DBeaver](https://dbeaver.io/) or the IDE's database tool.

## Concepts
- [ ] A **table** holds rows (records); each **column** has a type (`bigint`, `text`/`varchar`,
      `numeric`, `boolean`, `date`, `timestamptz`, …).
- [ ] A **primary key** uniquely identifies a row (e.g.
      `id bigint generated always as identity primary key`); a **foreign key** references another
      table's primary key.
- [ ] Relationships: one-to-many (a customer has many orders), many-to-many (via a join table such
      as `enrollment(student_id, course_id)`).
- [ ] **Normalization** reduces duplication; **constraints** (`NOT NULL`, `UNIQUE`, `CHECK`, foreign
      keys) let the database enforce integrity.
- [ ] SQL vs NoSQL in one line: relational gives structure, integrity, and joins; NoSQL stores trade
      some of that for flexibility or scale. This roadmap focuses on relational.

## Practice
**Goal:** Model a small domain.
**Steps:**
- [ ] Start PostgreSQL in Docker and connect to it with a GUI tool.
- [ ] Design tables for `customer` and `order` with a one-to-many relationship; add primary keys, a
      foreign key, and `NOT NULL` where required.
- [ ] Model a many-to-many (e.g. `student`–`course`) with a join table.
- [ ] Try to insert an order for a customer that doesn't exist and read the error.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Primary key vs foreign key?
> A primary key uniquely identifies each row of its table. A foreign key is a column that must match
> a primary key in another (or the same) table, linking rows together.

> [!question]- How do you model a many-to-many relationship?
> With a join table holding two foreign keys (e.g. `student_id`, `course_id`), usually with a
> composite primary key or unique constraint on the pair.

> [!question]- Why normalize a schema?
> To store each fact once: no duplicated data that can drift out of sync, and smaller, simpler
> updates.

## Definition of Done
- [ ] I can model data as tables with keys and relationships.
- [ ] I can explain one-to-many and many-to-many.
- [ ] I understand primary/foreign keys and constraints.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M8 - Databases - SQL CRUD and Queries]]
