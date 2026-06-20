---
title: HTTP and REST Fundamentals
area: Spring
module: 9
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# HTTP and REST Fundamentals

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 3h
> **Why this matters:** Web backends speak HTTP. Before touching Spring you need the vocabulary —
> methods, status codes, JSON, REST — or the framework will feel like magic.

## Learning Objectives
- Explain the HTTP request/response model.
- Use HTTP methods and status codes correctly.
- Describe what makes an API "RESTful".

## Learn
- [ ] Read an HTTP basics primer (MDN "An overview of HTTP").
- [ ] Read a short "REST API design" intro.

## Concepts
- [ ] A request has a **method**, URL, headers, and (often) a body; a response has a **status code**,
      headers, and body.
- [ ] Methods: `GET` (read), `POST` (create), `PUT`/`PATCH` (update), `DELETE` (remove).
- [ ] Status families: `2xx` success, `4xx` client error (400, 401, 404), `5xx` server error.
- [ ] **REST**: resources at URLs (`/books`, `/books/1`), methods as verbs, stateless requests,
      usually **JSON** bodies.
- [ ] Tools to call APIs: `curl`, HTTPie, Postman.

## Practice
**Goal:** Explore HTTP hands-on.
**Steps:**
- [ ] Use `curl`/HTTPie to `GET` a public JSON API and inspect status + headers + body.
- [ ] Identify which method and status code each CRUD operation should use.
- [ ] Sketch the REST endpoints for a `book` resource.

## Definition of Done
- [ ] I can explain HTTP requests, responses, and status codes.
- [ ] I can map CRUD to HTTP methods.
- [ ] I can design RESTful endpoints for a resource.

## Next
- Next: [[M9 - Spring - Spring Boot Intro and Project Setup]]
