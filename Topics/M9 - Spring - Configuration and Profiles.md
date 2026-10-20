---
title: Configuration and Profiles
area: Spring
module: 9
status: todo
priority: must
effort: 2
tags:
  - java-roadmap
---

# Configuration and Profiles

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 2h
> **Why this matters:** Apps run in different environments (local, test, prod) with different
> settings and secrets. Externalized config and profiles let one build run anywhere — safely.

## Learning Objectives
- Externalize configuration in `application.properties`/`.yml`.
- Use profiles for environment-specific settings.
- Inject config values and keep secrets out of the code.

## Learn
- [ ] Read:
      [Spring Boot — Externalized Configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html)
      (property sources order, relaxed binding, `@ConfigurationProperties`).
- [ ] Read:
      [Spring Boot — Profiles](https://docs.spring.io/spring-boot/reference/features/profiles.html).
- [ ] Read: [The Twelve-Factor App — Config](https://12factor.net/config) (one page).

## Concepts
- [ ] Settings live in `application.properties`/`application.yml`, overridable by environment
      variables and command-line arguments.
- [ ] **Profiles**: `application-dev.yml`, `application-prod.yml`; activate with
      `spring.profiles.active`.
- [ ] Bind groups of settings to a record with `@ConfigurationProperties("bookshelf")`;
      `@Value("${…}")` for single values.
- [ ] Relaxed binding: the env var `SPRING_DATASOURCE_URL` sets `spring.datasource.url`.
- [ ] **Never commit secrets** — pass them as environment variables or use a secrets manager.

## Practice
**Goal:** Make the app environment-aware.
**Steps:**
- [ ] Move a setting (e.g. default page size) into a `@ConfigurationProperties` record.
- [ ] Create `dev` and `prod` profiles with different settings; switch with
      `spring.profiles.active`.
- [ ] Override the datasource URL via an environment variable and confirm it wins.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- A property is set in `application.properties` and as an environment variable. Which wins?
> The environment variable — it has higher precedence, so you can override packaged defaults without
> rebuilding.

> [!question]- Which environment variable sets `spring.datasource.password`?
> `SPRING_DATASOURCE_PASSWORD` (upper case, dots become underscores).

> [!question]- `@Value` vs `@ConfigurationProperties`?
> `@Value` injects a single value; `@ConfigurationProperties` binds a whole group of related
> settings to a typed (and validatable) object — better for anything beyond one or two values.

## Definition of Done
- [ ] I can externalize and inject configuration.
- [ ] I can use profiles for per-environment settings.
- [ ] I keep secrets out of the repository.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M9 - Spring - Calling Other APIs with RestClient]]
