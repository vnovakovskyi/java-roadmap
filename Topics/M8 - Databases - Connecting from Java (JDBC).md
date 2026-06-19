---
title: Connecting from Java (JDBC)
area: Databases
module: 8
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Connecting from Java (JDBC)

> [!info] Topic
> **Area:** Databases · **Module:** 8 · **Priority:** good · **Est:** 3h
> **Why this matters:** JDBC is the low-level API every Java database tool sits on — including JPA.
> Doing it once by hand demystifies what frameworks do for you and teaches the critical safety habits.

## Learning Objectives
- Connect to a database and run queries from Java.
- Use `PreparedStatement` to avoid SQL injection.
- Manage resources and read results safely.

## Learn
- [ ] Read a JDBC quick-start (e.g. the dev.java / Baeldung JDBC intro).
- [ ] Add your database's JDBC driver as a dependency.

## Concepts
- [ ] `DriverManager.getConnection(url, user, pass)` opens a `Connection`.
- [ ] **Always** use `PreparedStatement` with `?` parameters — string-concatenated SQL invites
      **SQL injection**.
- [ ] `ResultSet` iterates query rows; read columns by name/index.
- [ ] Close everything — use try-with-resources ([[M4 - Java APIs - Exceptions and Error Handling]]).
- [ ] In real apps a connection pool (e.g. HikariCP) manages connections; frameworks set this up.

## Practice
**Goal:** Talk to a database without a framework.
**Steps:**
- [ ] Connect and `SELECT` rows into Java objects, printing them.
- [ ] Insert a row with a `PreparedStatement` using parameters.
- [ ] Show why a concatenated query is dangerous, then fix it with parameters.

**Record your result:**
- 

## Definition of Done
- [ ] I can connect, query, and read results via JDBC.
- [ ] I always use `PreparedStatement` for parameters.
- [ ] I close resources with try-with-resources.

## Cheatsheet (my notes)
- 

## Related
- [[M8 - Databases - Joins and Aggregation]]
- [[M8 - Databases - ORM Intro (JPA and Hibernate)]]
