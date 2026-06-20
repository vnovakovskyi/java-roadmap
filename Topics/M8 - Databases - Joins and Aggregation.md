---
title: Joins and Aggregation
area: Databases
module: 8
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Joins and Aggregation

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** must · **Est:** 4h
> **Why this matters:** Real questions span multiple tables and need summaries ("orders per
> customer"). Joins and aggregation are where SQL becomes powerful — and a common interview topic.

## Learning Objectives
- Combine tables with `JOIN`.
- Summarize data with `GROUP BY` and aggregate functions.
- Filter groups with `HAVING`.

## Learn
- [ ] Read about `INNER`/`LEFT` joins and `GROUP BY` (SQLBolt lessons 6–10).

## Concepts
- [ ] `INNER JOIN` returns matching rows; `LEFT JOIN` keeps all left rows (NULLs where no match).
- [ ] Join on keys: `FROM orders o JOIN customers c ON o.customer_id = c.id`.
- [ ] Aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` collapse rows.
- [ ] `GROUP BY` buckets rows before aggregating; `HAVING` filters those groups (vs `WHERE` on rows).
- [ ] Order of evaluation: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`.

## Practice
**Goal:** Answer cross-table questions.
**Steps:**
- [ ] Join `orders` to `customers` and list each order with the customer name.
- [ ] Count orders per customer with `GROUP BY`.
- [ ] Use `HAVING` to show only customers with more than N orders.

## Definition of Done
- [ ] I can write inner and left joins.
- [ ] I can aggregate with `GROUP BY` and aggregate functions.
- [ ] I know when to use `HAVING` vs `WHERE`.

## Next
- Next: [[M8 - Databases - Connecting from Java (JDBC)]]
