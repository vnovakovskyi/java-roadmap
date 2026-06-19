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
> tables, keys, and relationships is the foundation for SQL, JDBC, and JPA in the rest of this module.

## Learning Objectives
- Explain tables, rows, columns, and data types.
- Use primary and foreign keys to model relationships.
- Describe one-to-many and many-to-many relationships.

## Learn
- [ ] Read an intro to relational databases (e.g. the PostgreSQL tutorial's basics).
- [ ] Install PostgreSQL (or use Docker / H2) and a GUI like DBeaver — see [[Tools & Setup]].

## Concepts
- [ ] A **table** holds rows (records); each **column** has a type (`int`, `varchar`, `timestamp`, …).
- [ ] A **primary key** uniquely identifies a row; a **foreign key** references another table's PK.
- [ ] Relationships: one-to-many (a customer has many orders), many-to-many (via a join table).
- [ ] **Normalization** reduces duplication; **constraints** (`NOT NULL`, `UNIQUE`, FK) enforce integrity.
- [ ] SQL vs NoSQL in one line: relational gives structure + integrity + joins; you'll focus on relational.

## Practice
**Goal:** Model a small domain.
**Steps:**
- [ ] Design tables for `customer` and `order` with a one-to-many relationship.
- [ ] Add primary keys and a foreign key; mark required columns `NOT NULL`.
- [ ] Sketch how you'd model a many-to-many (e.g. `student`–`course`) with a join table.

**Record your result:**
- 

## Definition of Done
- [ ] I can model data as tables with keys and relationships.
- [ ] I can explain one-to-many and many-to-many.
- [ ] I understand primary/foreign keys and constraints.

## Cheatsheet (my notes)
- 

## Related
- [[M8 - Databases - SQL CRUD and Queries]]
- [[M8 - Databases - Joins and Aggregation]]
