---
title: HTTP and REST Fundamentals
area: Spring
module: 9
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# HTTP and REST Fundamentals

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 4h
> **Why this matters:** Web backends speak HTTP. Before touching Spring you need the vocabulary —
> methods, status codes, headers, JSON, REST — or the framework will feel like magic.

## Learning Objectives
- Explain the HTTP request/response model.
- Use HTTP methods and status codes correctly.
- Describe what makes an API "RESTful".

## Learn
- [ ] Read:
      [MDN — An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview).
- [ ] Reference: MDN
      [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
      and
      [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status).
- [ ] Read:
      [Web API design best practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
      (Microsoft) — resource naming, methods, status codes.
- [ ] Read:
      [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)
      (Martin Fowler) — the steps from RPC-style to "real" REST.
- [ ] Tools: the [curl tutorial](https://curl.se/docs/tutorial.html) or
      [HTTPie](https://httpie.io/docs/cli).

## Concepts
- [ ] A request has a **method**, URL, headers, and (often) a body; a response has a **status
      code**, headers, and body. Headers like `Content-Type` and `Accept` say what format the body
      is in.
- [ ] Methods: `GET` (read), `POST` (create), `PUT` (replace), `PATCH` (partial update), `DELETE`
      (remove), plus `HEAD` (headers only) and `OPTIONS` (which methods are allowed — browsers send
      it as the CORS "preflight").
- [ ] **Safe** methods change nothing (`GET`, `HEAD`, `OPTIONS`). **Idempotent** methods have the
      same *effect* on the server however often you repeat them (`GET`, `PUT`, `DELETE`, …) — the
      response may differ (a second `DELETE` can return 404). `POST` and `PATCH` are not guaranteed
      to be idempotent.
- [ ] Status families: `2xx` success (200, 201 Created, 204 No Content), `4xx` client error (400,
      401, 403, 404, 409), `5xx` server error.
- [ ] **REST**: resources at URLs (`/books`, `/books/1`), methods as verbs, stateless requests,
      usually **JSON** bodies. Its formal constraints: client–server, stateless, cacheable, uniform
      interface, layered system, and the optional code-on-demand.
- [ ] **Richardson Maturity Model**: level 0 — one URL, everything via `POST` (RPC style); level 1 —
      separate resources; level 2 — resources + proper methods and status codes (most real-world
      "REST" APIs, and what you'll build); level 3 — hypermedia (HATEOAS: responses contain links to
      the next possible actions).
- [ ] Practice APIs like [JSONPlaceholder](https://jsonplaceholder.typicode.com/) let you experiment
      without writing a server.

## Practice
**Goal:** Explore HTTP hands-on.
**Steps:**
- [ ] Use `curl -i` (or HTTPie) to `GET` a JSONPlaceholder resource and inspect status, headers, and
      body.
- [ ] Send a `POST` with a JSON body and a `Content-Type` header; read the 201 response.
- [ ] Sketch the REST endpoints (method + path + success status) for a `book` resource.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- 401 vs 403?
> 401 Unauthorized: you're not authenticated (no or bad credentials). 403 Forbidden: you're
> authenticated but not allowed to do this.

> [!question]- What does "idempotent" mean, and which methods are?
> Repeating the request has the same effect on the server as doing it once (the response may
> differ). `GET`, `HEAD`, `OPTIONS`, `PUT`, and `DELETE` are idempotent; `POST` and `PATCH` aren't
> guaranteed to be.

> [!question]- What are the levels of the Richardson Maturity Model, and where do most APIs sit?
> 0: one endpoint, everything via POST; 1: resources; 2: resources with proper HTTP methods and
> status codes; 3: hypermedia links (HATEOAS). Most APIs — including the ones in this roadmap — are
> level 2.

> [!question]- `PUT` vs `PATCH`?
> `PUT` replaces the whole resource with the request body; `PATCH` changes only the fields sent.

> [!question]- What status should a successful create return?
> `201 Created`, ideally with a `Location` header pointing to the new resource.

## Definition of Done
- [ ] I can explain HTTP requests, responses, headers, and status codes.
- [ ] I can map CRUD to HTTP methods and statuses.
- [ ] I can design RESTful endpoints for a resource.
- [ ] I can explain safe vs idempotent methods and the Richardson Maturity Model.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M9 - Spring - Spring Boot Intro and Project Setup]]
