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
> methods and turn Java objects into JSON. This is where your app becomes something a client can
> actually call.

## Learning Objectives
- Build REST endpoints with `@RestController`.
- Map paths, methods, path variables, query parameters, and request bodies.
- Return proper status codes and JSON.

## Learn
- [ ] Read:
      [Spring Framework — Annotated Controllers](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller.html)
      (mappings and handler method arguments).
- [ ] Read: [Spring Boot — JSON](https://docs.spring.io/spring-boot/reference/features/json.html)
      (how Jackson is configured).
- [ ] Do: the [Building REST services with Spring](https://spring.io/guides/tutorials/rest/)
      tutorial.

## Concepts
- [ ] `@RestController` + `@RequestMapping("/books")`; method mappings `@GetMapping`,
      `@PostMapping`, `@PutMapping`, `@DeleteMapping`.
- [ ] Inputs: `@PathVariable` (`/books/{id}`), `@RequestParam` (`?author=…`), `@RequestBody` (JSON →
      object).
- [ ] Returned objects become JSON via **Jackson 3**; records work out of the box. Annotations like
      `@JsonProperty`/`@JsonIgnore` still come from `com.fasterxml.jackson.annotation`.
- [ ] `ResponseEntity` controls status and headers: `ResponseEntity.created(location).body(dto)` for
      201, `ResponseEntity.noContent()` for 204.
- [ ] Use **DTOs/records** for request and response shapes rather than exposing entities directly.

## Practice
**Goal:** A full CRUD controller.
**Steps:**
- [ ] Build `BookController` with GET (list + by id), POST, PUT, DELETE, backed by an in-memory
      `Map`.
- [ ] Use `@PathVariable`, `@RequestParam` (filter by author), and `@RequestBody`.
- [ ] Return 201 with a `Location` header on create, 204 on delete, and 404 when a book is missing.
- [ ] Exercise every endpoint with curl or HTTPie.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- `@PathVariable` vs `@RequestParam` vs `@RequestBody`?
> Path variable: part of the URL path (`/books/42`). Request param: query string (`?author=Bloch`).
> Request body: the JSON payload, converted to an object.

> [!question]- Why use DTOs instead of returning entities?
> DTOs decouple the API from the database model: you control exactly which fields are exposed and
> accepted, avoid leaking internals, and can change either side independently.

> [!question]- How does a returned record turn into JSON?
> Spring's message converter hands it to Jackson, which serializes its components to JSON fields
> based on the `Accept` header (JSON by default).

## Definition of Done
- [ ] I can build CRUD endpoints with the right methods and status codes.
- [ ] I can bind path variables, query params, and JSON bodies.
- [ ] I use DTOs/records for API shapes.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M9 - Spring - Services and Dependency Injection]]
