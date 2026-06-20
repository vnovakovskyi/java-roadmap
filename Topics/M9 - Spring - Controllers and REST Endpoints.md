---
title: Controllers and REST Endpoints
area: Spring
module: 9
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Controllers and REST Endpoints

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 4h
> **Why this matters:** Controllers are the front door of your API — they map HTTP requests to Java
> methods. This is where your app becomes something a client can actually call.

## Learning Objectives
- Build REST endpoints with `@RestController`.
- Map paths, methods, path variables, and request bodies.
- Return proper status codes and JSON.

## Learn
- [ ] Read the Spring Web MVC controller docs / REST service guide.
- [ ] Read about `@RequestMapping` and its shortcuts.

## Concepts
- [ ] `@RestController` + `@RequestMapping("/books")`; method mappings `@GetMapping`, `@PostMapping`,
      `@PutMapping`, `@DeleteMapping`.
- [ ] Inputs: `@PathVariable` (`/books/{id}`), `@RequestParam` (query), `@RequestBody` (JSON → object).
- [ ] Returning objects auto-serializes to JSON (Jackson); use `ResponseEntity` to control status/headers.
- [ ] Map CRUD to endpoints per [[M9 - Spring - HTTP and REST Fundamentals]] (e.g. `POST` → 201).
- [ ] Use **DTOs/records** for request/response shapes rather than exposing entities directly.

## Practice
**Goal:** A full CRUD controller.
**Steps:**
- [ ] Build `BookController` with GET (list + by id), POST, PUT, DELETE backed by an in-memory list.
- [ ] Use `@PathVariable` and `@RequestBody`; return 201 on create and 404 when missing.
- [ ] Exercise every endpoint with curl/Postman.

## Definition of Done
- [ ] I can build CRUD endpoints with the right methods and status codes.
- [ ] I can bind path variables, query params, and JSON bodies.
- [ ] I use DTOs/records for API shapes.

## Next
- Next: [[M9 - Spring - Services and Dependency Injection]]
