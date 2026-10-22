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
> **Why this matters:** The capstone proves you can build something real on your own — this time in
> a domain *you* choose, without step-by-step instructions. It starts with design: choosing a
> domain, modeling data, and planning endpoints before writing code.

## Learning Objectives
- Pick a small, well-scoped domain.
- Model the entities and relationships.
- Plan the REST API, project structure, and quality bar.

## Learn
- [ ] Review [[M8 - Databases - Relational Concepts]] and
      [[M9 - Spring - HTTP and REST Fundamentals]].
- [ ] Explore [Spring PetClinic](https://github.com/spring-projects/spring-petclinic) — the official
      sample app — for structure ideas.

## Concepts
- [ ] Choose something you understand: a task tracker, recipe box, workout log, expense tracker,
      event sign-ups.
- [ ] Keep the scope tiny: 2–3 entities, full CRUD on one, at least one relationship. Write user
      stories ("As a user I can…") and cut everything that isn't needed for a first version.
- [ ] Design data first (tables/entities), then endpoints (per resource), then layers
      (controller/service/repository) and packages.
- [ ] Decide request/response DTO shapes separately from entities.
- [ ] Set the quality bar up front: validation, consistent errors, security, tests, CI, Docker
      Compose, README.
- [ ] Write it down — a one-page spec in the README keeps you honest.

## Practice
**Goal:** Produce a one-page design.
**Steps:**
- [ ] Pick a domain and write 5–8 user stories.
- [ ] List entities, fields, and relationships; sketch the tables.
- [ ] Define the REST endpoints (method + path + success/error statuses) for each resource.
- [ ] Sketch the package structure and create the repository with the spec in its README.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why keep the capstone scope so small?
> A small app you finish — tested, secured, documented — demonstrates far more than a big one
> abandoned halfway. You can always add features later.

> [!question]- Why design the data model before the endpoints?
> The data and its relationships drive everything else: endpoints, validation, and queries follow
> from it. Changing tables late is much more expensive than changing a controller.

> [!question]- Why plan DTOs separately from entities?
> The API contract (what clients send and receive) and the persistence model change for different
> reasons; keeping them separate lets each evolve without breaking the other.

## Definition of Done
- [ ] I have a scoped domain with user stories and an entity model.
- [ ] I have a planned set of REST endpoints with statuses.
- [ ] I have a repository with the spec in its README.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M10 - Project - Building the REST API End-to-End]]
