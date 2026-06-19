---
title: Packaging and Running (Jar and Docker Basics)
area: Project
module: 10
status: todo
priority: optional
effort: 3
tags:
  - java-roadmap
---

# Packaging and Running (Jar and Docker Basics)

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** optional · **Est:** 3h
> **Why this matters:** Shipping means producing something runnable anywhere. Building an executable
> jar and a basic Docker image is a great finishing skill — optional for a first job, valued everywhere.

## Learning Objectives
- Build and run an executable Spring Boot jar.
- Containerize the app with a simple Dockerfile.
- Run the container locally.

## Learn
- [ ] Read the Spring "Spring Boot with Docker" guide.
- [ ] Read the basics of Docker images and containers.

## Concepts
- [ ] Spring Boot builds a self-contained **fat jar**: `mvn package` / `./gradlew bootJar`, run with
      `java -jar`.
- [ ] A **Dockerfile** describes an image: base JDK/JRE image, copy the jar, set the entrypoint.
- [ ] `docker build -t myapp .` then `docker run -p 8080:8080 myapp`.
- [ ] Pass config/secrets via environment variables at run time, not baked into the image.
- [ ] Keep images small (slim/JRE base, layered builds) — deeper hardening is beyond junior scope.

## Practice
**Goal:** Run your app as an artifact and a container.
**Steps:**
- [ ] Build the jar and run it with `java -jar`; hit an endpoint.
- [ ] Write a minimal Dockerfile, build the image, and run the container.
- [ ] Pass a config value via an environment variable to the container.

**Record your result:**
- 

## Definition of Done
- [ ] I can build and run an executable jar.
- [ ] I can containerize and run the app with Docker.
- [ ] I pass config via env vars, not baked-in.

## Cheatsheet (my notes)
- 

## Related
- [[M10 - Project - Good Habits (Logging, Config, README)]]
- [[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]]
