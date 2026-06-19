---
title: Spring Boot Intro and Project Setup
area: Spring
module: 9
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Spring Boot Intro and Project Setup

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** must · **Est:** 3h
> **Why this matters:** Spring Boot is the dominant Java web framework and the single most in-demand
> skill for junior Java jobs. Getting a project running is the gateway to everything else here.

## Learning Objectives
- Generate and run a Spring Boot project.
- Understand starters, auto-configuration, and the project layout.
- Know what the embedded server and main class do.

## Learn
- [ ] Use [start.spring.io](https://start.spring.io) to generate a project (Web, Spring Data JPA, a DB driver).
- [ ] Read the [Spring "Building a RESTful Web Service" guide](https://spring.io/guides/gs/rest-service/).

## Concepts
- [ ] Spring Boot = Spring + sensible defaults + embedded server; you run a normal `main` and it boots
      a web app.
- [ ] **Starters** (`spring-boot-starter-web`, `-data-jpa`) pull in curated dependency sets.
- [ ] **Auto-configuration** wires beans based on what's on the classpath.
- [ ] Layout: `@SpringBootApplication` main class, `application.properties`/`.yml`, `src/main/resources`.
- [ ] Build/run with Maven or Gradle ([[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]] /
      [[M6 - Tooling - Gradle (Project, Dependencies, Tasks)]]).

## Practice
**Goal:** Boot a running app.
**Steps:**
- [ ] Generate a project and run it; confirm the server starts on port 8080.
- [ ] Add a trivial `/hello` endpoint and hit it from the browser/curl.
- [ ] Find and skim the auto-config report (run with `--debug`).

**Record your result:**
- 

## Definition of Done
- [ ] I can generate, run, and explain a Spring Boot project.
- [ ] I understand starters and auto-configuration.
- [ ] I can add a basic endpoint and call it.

## Cheatsheet (my notes)
- 

## Related
- [[M9 - Spring - HTTP and REST Fundamentals]]
- [[M9 - Spring - Controllers and REST Endpoints]]
