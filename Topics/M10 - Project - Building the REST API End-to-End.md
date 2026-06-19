---
title: Building the REST API End-to-End
area: Project
module: 10
status: todo
priority: must
effort: 6
tags:
  - java-roadmap
---

# Building the REST API End-to-End

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** must · **Est:** 6h
> **Why this matters:** This is the heart of the capstone: turning your design into a working API with
> controllers, services, and DTOs. Finishing it is the strongest signal you're job-ready.

## Learning Objectives
- Implement full CRUD across the controller/service layers.
- Use DTOs and validation.
- Wire the layers together cleanly.

## Learn
- [ ] Revisit [[M9 - Spring - Controllers and REST Endpoints]],
      [[M9 - Spring - Services and Dependency Injection]], and
      [[M9 - Spring - Validation and Error Handling]].

## Concepts
- [ ] Build each layer for your design: `@RestController` → `@Service` → (repository next topic).
- [ ] Map DTOs/records to/from your domain; validate inputs with `@Valid`.
- [ ] Return correct status codes (201 create, 200 read/update, 204 delete, 404 missing).
- [ ] Keep the controller thin; put logic in the service.
- [ ] Add the global error handling from Module 9 so failures are consistent.

## Practice
**Goal:** A working API (still in-memory persistence is fine for this step).
**Steps:**
- [ ] Implement all CRUD endpoints for your primary resource.
- [ ] Add request/response DTOs and validation.
- [ ] Exercise every endpoint with curl/Postman, including error cases.

**Record your result:**
- 

## Definition of Done
- [ ] All CRUD endpoints work with correct status codes.
- [ ] Inputs are validated and errors are consistent.
- [ ] Logic lives in the service, not the controller.

## Cheatsheet (my notes)
- 

## Related
- [[M10 - Project - Designing a Small CRUD App]]
- [[M10 - Project - Persisting with a Real Database]]
