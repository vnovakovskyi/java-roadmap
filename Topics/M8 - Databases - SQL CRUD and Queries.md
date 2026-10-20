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
- Use `WHERE` conditions and `NULL` correctly.

## Learn
- [ ] Do: [SQLBolt](https://sqlbolt.com/) lessons 1–5 and 13–18 — interactive, in the browser.
- [ ] Read: [The SQL Language](https://www.postgresql.org/docs/current/tutorial-sql.html)
      (PostgreSQL tutorial, chapter 2) and run the examples in your own database.

## Concepts
- [ ] `CREATE TABLE` defines structure; `INSERT INTO ... VALUES` adds rows.
- [ ] `SELECT cols FROM t WHERE cond ORDER BY col LIMIT n` — the workhorse query. Avoid `SELECT *`
      in application code.
- [ ] `WHERE` operators: `=`, `<>`, `<`, `>`, `LIKE` / `ILIKE`, `IN`, `BETWEEN`, `IS NULL`.
- [ ] `UPDATE ... SET ... WHERE ...` and `DELETE FROM ... WHERE ...` — **always** include `WHERE`
      (and run it as a `SELECT` first).
- [ ] `NULL` is "unknown": `NULL = NULL` isn't true — use `IS NULL` / `IS NOT NULL`.
- [ ] `LIMIT ... OFFSET ...` pages through results (you'll use it for paginated APIs).

## Practice
**Goal:** Run a full CRUD cycle in SQL.
**Steps:**
- [ ] Create a `book` table; insert several rows.
- [ ] Query with `WHERE`, `ORDER BY`, and `LIMIT`; find books whose title contains a word
      (case-insensitive).
- [ ] Update one row and delete another (with a `WHERE`); verify with a `SELECT`.
- [ ] Page through the books two at a time with `LIMIT`/`OFFSET`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What happens if you run `DELETE FROM book;` without a `WHERE`?
> Every row in the table is deleted. Always write the `WHERE` first — and preview it as a `SELECT`.

> [!question]- Why does `WHERE published_year = NULL` return nothing?
> Comparing with `NULL` yields unknown, never true. Use `WHERE published_year IS NULL`.

> [!question]- How do you get the 10 most recently added books?
> `SELECT ... FROM book ORDER BY created_at DESC LIMIT 10;`

## Definition of Done
- [ ] I can write all four CRUD statements.
- [ ] I can filter, sort, limit, and page results.
- [ ] I always scope `UPDATE`/`DELETE` with `WHERE`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M8 - Databases - Joins and Aggregation]]
