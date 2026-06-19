---
title: Maven (Project, Dependencies, Lifecycle)
area: Tooling
module: 6
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Maven (Project, Dependencies, Lifecycle)

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** must · **Est:** 4h
> **Why this matters:** Maven is the most common Java build tool in the enterprise. It compiles,
> tests, packages, and pulls in libraries. Spring Boot projects (Module 9) often use it.

## Learning Objectives
- Create and understand a Maven project (`pom.xml`).
- Add dependencies and run the build lifecycle.
- Use the Maven wrapper.

## Learn
- [ ] Read the [Maven "Getting Started" guide](https://maven.apache.org/guides/getting-started/).
- [ ] Read about the standard directory layout and the `pom.xml` anatomy.

## Concepts
- [ ] `pom.xml` declares coordinates (`groupId:artifactId:version`), dependencies, plugins, and Java version.
- [ ] Standard layout: `src/main/java`, `src/test/java`, `src/main/resources` (see
      [[M4 - Java APIs - Packages and Project Organization]]).
- [ ] **Lifecycle phases**: `validate → compile → test → package → verify → install`. Running a phase
      runs all earlier ones.
- [ ] Dependencies download from Maven Central to your local `~/.m2` cache; **scopes** (`compile`,
      `test`, `provided`) control where they apply.
- [ ] The **wrapper** (`mvnw`) pins the Maven version per project — prefer it.

## Practice
**Goal:** Build a real Maven project.
**Steps:**
- [ ] Generate a project (IDE "New Maven project" or an archetype).
- [ ] Add a dependency (e.g. AssertJ in `test` scope) and confirm it downloads.
- [ ] Run `mvn compile`, `mvn test`, and `mvn package`; find the built `.jar` in `target/`.

**Record your result:**
- 

## Definition of Done
- [ ] I can read and edit a `pom.xml` and add dependencies.
- [ ] I can run the common lifecycle phases and explain them.
- [ ] I can build a runnable artifact and use `mvnw`.

## Cheatsheet (my notes)
- 

## Related
- [[M6 - Tooling - Gradle (Project, Dependencies, Tasks)]]
- [[M6 - Tooling - Dependency Management and Semantic Versioning]]
