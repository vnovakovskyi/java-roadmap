---
title: Transactions and Indexes
area: Databases
module: 8
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Transactions and Indexes

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** must · **Est:** 3h
> **Why this matters:** Two ideas separate "it works on my laptop" from "it works under real load":
> **transactions** keep data consistent when something fails halfway or two users act at once, and
> **indexes** keep queries fast as tables grow. Both are standard junior interview questions.

## Learning Objectives
- Group statements into a transaction and explain ACID.
- Describe what isolation levels protect against, at a basic level.
- Explain what an index is, when it helps, and what it costs.

## Learn
- [ ] Read: [Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
      (PostgreSQL tutorial).
- [ ] Read: [Use The Index, Luke!](https://use-the-index-luke.com/) — chapter 1, "Anatomy of an SQL
      Index".
- [ ] Skim: [Introduction to Indexes](https://www.postgresql.org/docs/current/indexes-intro.html)
      and [Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
      (PostgreSQL docs).

## Concepts
- [ ] A **transaction** (`BEGIN … COMMIT`, or `ROLLBACK` to undo) makes several statements succeed
      or fail as one unit. Without `BEGIN`, each statement is its own transaction (autocommit).
- [ ] **ACID**: Atomicity (all or nothing), Consistency (constraints hold), Isolation (concurrent
      transactions don't see each other's half-done work), Durability (committed data survives
      crashes).
- [ ] Isolation levels trade safety for concurrency; PostgreSQL's default is **Read Committed**.
      Classic anomaly: the **lost update** — prevent it with `SELECT … FOR UPDATE` or optimistic
      locking (a `version` column, `@Version` in JPA).
- [ ] An **index** (usually a B-tree) is a sorted lookup structure that turns full-table scans into
      fast lookups for `WHERE`, `JOIN`, and `ORDER BY`. Costs: slower writes and extra storage —
      index what you query, not everything.
- [ ] Primary keys and `UNIQUE` constraints are indexed automatically; **foreign-key columns are
      not** in PostgreSQL — index them if you join or filter on them.
- [ ] `EXPLAIN ANALYZE` shows whether a query uses an index (`Index Scan`) or reads everything
      (`Seq Scan`).

## Practice
**Goal:** Feel atomicity, isolation, and the effect of an index.
**Steps:**
- [ ] Transfer money between two `account` rows inside a transaction; simulate a failure halfway and
      `ROLLBACK`.
- [ ] Open two `psql` sessions: change a row in one without committing and look at it from the
      other.
- [ ] Generate a million rows with `generate_series`, run `EXPLAIN ANALYZE` on a filtered query, add
      an index, and compare.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What does ACID stand for?
> Atomicity, Consistency, Isolation, Durability.

> [!question]- The app crashes after debiting one account but before crediting the other — inside a transaction. What's in the database?
> Neither change. The transaction never committed, so the database rolls it back as if it never
> happened.

> [!question]- Why not add an index to every column?
> Each index slows down inserts, updates, and deletes and takes space; unused indexes are pure cost.
> Add them for the queries you actually run.

> [!question]- Does PostgreSQL index foreign-key columns automatically?
> No — only primary keys and unique constraints. Add an index on foreign keys you join or filter on.

## Definition of Done
- [ ] I can use transactions and explain ACID.
- [ ] I can explain the lost-update problem and one way to prevent it.
- [ ] I can show the effect of an index with `EXPLAIN ANALYZE`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M8 - Databases - Connecting from Java (JDBC)]]
