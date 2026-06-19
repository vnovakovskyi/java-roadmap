---
title: Configuration and Profiles
area: Spring
module: 9
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Configuration and Profiles

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** good · **Est:** 2h
> **Why this matters:** Apps run in different environments (local, test, prod) with different settings
> and secrets. Externalized config and profiles let one build run anywhere — safely.

## Learning Objectives
- Externalize configuration in `application.properties`/`.yml`.
- Use profiles for environment-specific settings.
- Inject config values and avoid hard-coding secrets.

## Learn
- [ ] Read the Spring Boot "Externalized Configuration" reference.
- [ ] Read about `@Value`, `@ConfigurationProperties`, and `@Profile`.

## Concepts
- [ ] Settings live in `application.properties`/`application.yml`, overridable by env vars and CLI args.
- [ ] **Profiles**: `application-dev.yml`, `application-prod.yml`; activate with `spring.profiles.active`.
- [ ] Inject values with `@Value("${...}")` or bind groups with `@ConfigurationProperties`.
- [ ] **Never commit secrets** — use environment variables / a secrets manager; keep them out of Git.
- [ ] Order of precedence lets you override config per environment without rebuilding.

## Practice
**Goal:** Make the app environment-aware.
**Steps:**
- [ ] Move a setting (e.g. a greeting or page size) into config and inject it with `@Value`.
- [ ] Create `dev` and `prod` profiles with different DB settings; switch with `spring.profiles.active`.
- [ ] Override a property via an environment variable and confirm it wins.

**Record your result:**
- 

## Definition of Done
- [ ] I can externalize and inject configuration.
- [ ] I can use profiles for per-environment settings.
- [ ] I keep secrets out of the repo.

## Cheatsheet (my notes)
- 

## Related
- [[M9 - Spring - Spring Boot Intro and Project Setup]]
- [[M10 - Project - Good Habits (Logging, Config, README)]]
