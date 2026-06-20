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
- [ ] Read about Bean Validation (`jakarta.validation`) annotations and `@Valid`.
- [ ] Read about `@ControllerAdvice` / `@ExceptionHandler`.

## Concepts
- [ ] Annotate DTO fields: `@NotNull`, `@NotBlank`, `@Size`, `@Email`, `@Min`/`@Max`; trigger with
      `@Valid` on the `@RequestBody`.
- [ ] Invalid input → `MethodArgumentNotValidException`; map it to a clean **400** response.
- [ ] **Global handling**: `@ControllerAdvice` + `@ExceptionHandler` centralizes error mapping.
- [ ] Return a consistent error shape (e.g. RFC 7807 `ProblemDetail`); never leak stack traces.
- [ ] Map domain failures to the right status (404 not found, 409 conflict) — reuse
      [[M4 - Java APIs - Exceptions and Error Handling]] habits.

## Practice
**Goal:** Make the API reject bad input gracefully.
**Steps:**
- [ ] Add validation annotations to the create-book DTO and `@Valid` on the endpoint.
- [ ] Add a `@ControllerAdvice` returning a consistent JSON error body.
- [ ] Test: invalid input → 400 with field errors; missing id → 404.

## Definition of Done
- [ ] I can validate request bodies and return 400 on failure.
- [ ] I handle exceptions globally with a consistent error shape.
- [ ] I map domain errors to correct status codes and never leak stack traces.

## Next
- Next: [[M9 - Spring - Configuration and Profiles]]
