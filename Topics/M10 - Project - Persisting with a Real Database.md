---
title: Persisting with a Real Database
area: Project
module: 10
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Persisting with a Real Database

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** must · **Est:** 4h
> **Why this matters:** A real app stores data that survives restarts. Swapping the in-memory store
> for a real database with Spring Data JPA and migrations is what makes the capstone production-shaped.

## Learning Objectives
- Back the app with a real database via Spring Data JPA.
- Manage the schema with migrations.
- Verify data persists across restarts.

## Learn
- [ ] Revisit [[M9 - Spring - Spring Data JPA and Repositories]] and
      [[M8 - Databases - Schema Basics and Migrations (Flyway)]].

## Concepts
- [ ] Replace the in-memory list with a `JpaRepository` and a real DB (PostgreSQL; H2 for quick local).
- [ ] Define the schema with Flyway migrations rather than auto-DDL.
- [ ] Configure the datasource via profiles ([[M9 - Spring - Configuration and Profiles]]); keep
      credentials out of Git.
- [ ] Watch the generated SQL; check for the N+1 problem on relationships.
- [ ] Restart the app and confirm data is still there.

## Practice
**Goal:** Durable persistence.
**Steps:**
- [ ] Point the app at a real database; add Flyway migrations for your tables.
- [ ] Run full CRUD through the API and confirm rows in the DB (via DBeaver/psql).
- [ ] Restart the app and verify the data survives.

## Definition of Done
- [ ] The app persists to a real database via JPA.
- [ ] The schema is created by migrations.
- [ ] Data survives restarts and credentials aren't in Git.

## Next
- Next: [[M10 - Project - Testing the Application]]
