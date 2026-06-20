---
title: SQL CRUD and Queries
area: Databases
module: 8
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# SQL CRUD and Queries

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** must · **Est:** 4h
> **Why this matters:** SQL is how you create, read, update, and delete data. Even with an ORM you
> must read and write SQL to debug, optimize, and understand what's really happening.

## Learning Objectives
- Write `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
- Filter, sort, and limit results.
- Use `WHERE` conditions confidently.

## Learn
- [ ] Do an interactive SQL tutorial (e.g. SQLBolt or Mode's SQL tutorial).
- [ ] Read the basics of your database's SQL dialect.

## Concepts
- [ ] `CREATE TABLE` defines structure; `INSERT INTO ... VALUES` adds rows.
- [ ] `SELECT cols FROM t WHERE cond ORDER BY col LIMIT n` — the workhorse query.
- [ ] `WHERE` operators: `=`, `<>`, `<`, `>`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`.
- [ ] `UPDATE ... SET ... WHERE ...` and `DELETE FROM ... WHERE ...` — **always** include `WHERE`.
- [ ] `NULL` is "unknown"; comparisons with it use `IS NULL` / `IS NOT NULL`.

## Practice
**Goal:** Run a full CRUD cycle in SQL.
**Steps:**
- [ ] Create a `book` table; insert several rows.
- [ ] Query with `WHERE`, `ORDER BY`, and `LIMIT`.
- [ ] Update one row and delete another (with a `WHERE`); verify with a `SELECT`.

## Definition of Done
- [ ] I can write all four CRUD statements.
- [ ] I can filter, sort, and limit results.
- [ ] I always scope `UPDATE`/`DELETE` with `WHERE`.

## Next
- Next: [[M8 - Databases - Joins and Aggregation]]
