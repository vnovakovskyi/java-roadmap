---
title: API Docs and Monitoring (OpenAPI and Actuator)
area: Spring
module: 9
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# API Docs and Monitoring (OpenAPI and Actuator)

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** good · **Est:** 2h
> **Why this matters:** Other developers (and future you) need to know how to call your API, and
> operations need to know whether it's healthy. OpenAPI generates interactive docs from your code;
> Actuator adds health checks and metrics — two dependencies that make a portfolio project look
> production-ready.

## Learning Objectives
- Generate OpenAPI docs and a Swagger UI for your API.
- Add health and info endpoints with Actuator.
- Expose operational endpoints safely.

## Learn
- [ ] Read: [springdoc-openapi](https://springdoc.org/) — "Getting Started".
- [ ] Read:
      [Spring Boot — Actuator](https://docs.spring.io/spring-boot/reference/actuator/index.html)
      (enabling and exposing endpoints).
- [ ] Do: the
      [Spring "Building a RESTful Web Service with Spring Boot Actuator" guide](https://spring.io/guides/gs/actuator-service/).

## Concepts
- [ ] **OpenAPI** is the standard machine-readable description of a REST API. springdoc generates it
      from your controllers: JSON at `/v3/api-docs`, interactive docs at `/swagger-ui.html`.
- [ ] Use **springdoc 3.x** with Spring Boot 4 (2.x is for Boot 3). Add `@Operation`/`@Schema`
      annotations only where the generated docs need help.
- [ ] **Actuator** (`spring-boot-starter-actuator`): `/actuator/health` (used by load balancers and
      Kubernetes probes), `/actuator/info`, `/actuator/metrics`.
- [ ] Only `health` is exposed over HTTP by default; expose more deliberately
      (`management.endpoints.web.exposure.include=health,info,metrics`). Never expose everything
      publicly — endpoints like `env` or `heapdump` can leak secrets.
- [ ] Metrics come from Micrometer and can feed Prometheus/Grafana — know the names.

## Practice
**Goal:** Document and monitor your API.
**Steps:**
- [ ] Add springdoc, open the Swagger UI, and call an endpoint from it.
- [ ] Add Actuator; check `/actuator/health`, then add build info to `/actuator/info`.
- [ ] Stop the database and watch the health status change.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What is OpenAPI and why generate it from code?
> A standard format describing endpoints, parameters, and schemas. Generating it from the code keeps
> the docs in sync with the real API and enables tools like Swagger UI and client generators.

> [!question]- Why not expose all Actuator endpoints?
> Some reveal sensitive data (environment variables, configuration, heap dumps) or allow actions.
> Expose only what you need and protect the rest.

> [!question]- What is `/actuator/health` used for in production?
> Load balancers and orchestrators (e.g. Kubernetes liveness/readiness probes) poll it to decide
> whether to send traffic to or restart an instance.

## Definition of Done
- [ ] My API has generated OpenAPI docs and a Swagger UI.
- [ ] My app exposes health and info endpoints.
- [ ] I can explain which operational endpoints are safe to expose.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M9 - Spring - Securing the API with Spring Security]]
