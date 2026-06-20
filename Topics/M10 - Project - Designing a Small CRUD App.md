---
title: Designing a Small CRUD App
area: Project
module: 10
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Designing a Small CRUD App

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** must · **Est:** 3h
> **Why this matters:** The capstone proves you can build something real. It starts with design —
> choosing a domain, modeling data, and planning endpoints before writing code.

## Learning Objectives
- Pick a small, well-scoped domain.
- Model the entities and relationships.
- Plan the REST API and project structure.

## Learn
- [ ] Review [[M8 - Databases - Relational Concepts]] and [[M9 - Spring - HTTP and REST Fundamentals]].
- [ ] Look at one small open-source Spring Boot CRUD repo for structure ideas.

## Concepts
- [ ] Choose something you understand: a task tracker, bookshelf, recipe box, expense log.
- [ ] Keep scope tiny: 1–2 entities, full CRUD, maybe one relationship.
- [ ] Design data first (tables/entities), then endpoints (per resource), then layers
      (controller/service/repository).
- [ ] Decide DTO shapes vs entities up front.
- [ ] Write down the plan — a short README-style spec keeps you honest.

## Practice
**Goal:** Produce a one-page design.
**Steps:**
- [ ] Pick a domain and list its entities + fields + one relationship.
- [ ] Define the REST endpoints (method + path + purpose) for each resource.
- [ ] Sketch the package structure (by feature or by layer).

## Definition of Done
- [ ] I have a scoped domain with an entity model.
- [ ] I have a planned set of REST endpoints.
- [ ] I have a project structure to build into.

## Next
- Next: [[M10 - Project - Building the REST API End-to-End]]
