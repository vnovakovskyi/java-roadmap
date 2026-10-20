---
title: Validation and Error Handling
area: Spring
module: 9
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Validation and Error Handling

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 3h
> **Why this matters:** APIs must reject bad input and return clear, consistent errors. Sloppy
> validation and stack-trace responses are a hallmark of amateur services — and a security risk.

## Learning Objectives
- Validate request bodies with Bean Validation.
- Return consistent error responses.
- Handle exceptions globally.

## Learn
- [ ] Read:
      [Spring Framework — Java Bean Validation](https://docs.spring.io/spring-framework/reference/core/validation/beanvalidation.html).
- [ ] Read:
      [Controller Advice](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-advice.html)
      and
      [Error Responses](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html)
      (`ProblemDetail`).

## Concepts
- [ ] Add `spring-boot-starter-validation`, then annotate DTO fields: `@NotNull`, `@NotBlank`,
      `@Size`, `@Email`, `@Min`/`@Max`; trigger with `@Valid` on the `@RequestBody`.
- [ ] Invalid input → `MethodArgumentNotValidException`; map it to a clean **400** with the field
      errors.
- [ ] **Global handling**: `@RestControllerAdvice` + `@ExceptionHandler` centralizes error mapping.
- [ ] Return a consistent error shape — `ProblemDetail`, the RFC 9457 "problem details" format (it
      replaced RFC 7807). `spring.mvc.problemdetails.enabled=true` makes Spring's own errors use it
      too. Never leak stack traces.
- [ ] Map domain failures to the right status (404 not found, 409 conflict) — reuse
      [[M4 - Java APIs - Exceptions and Error Handling]] habits.

## Practice
**Goal:** Make the API reject bad input gracefully.
**Steps:**
- [ ] Add validation annotations to the create-book DTO and `@Valid` on the endpoint.
- [ ] Add a `@RestControllerAdvice` that returns `ProblemDetail` bodies.
- [ ] Throw a `BookNotFoundException` from the service and map it to 404 in one place.
- [ ] Test: invalid input → 400 with field errors; missing id → 404; duplicate ISBN → 409.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Your `@NotBlank` annotation is ignored. What are the two usual causes?
> `spring-boot-starter-validation` isn't on the classpath, or the parameter lacks `@Valid`.

> [!question]- Which status for: invalid JSON field, unknown id, duplicate unique value?
> 400 Bad Request, 404 Not Found, 409 Conflict.

> [!question]- Why handle exceptions in a `@RestControllerAdvice` instead of in each controller?
> One place defines how every error maps to a status and body, so responses are consistent and
> controllers stay focused on the happy path.

## Definition of Done
- [ ] I can validate request bodies and return 400 on failure.
- [ ] I handle exceptions globally with a consistent `ProblemDetail` shape.
- [ ] I map domain errors to correct status codes and never leak stack traces.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M9 - Spring - Configuration and Profiles]]
