---
title: Gradle (Project, Dependencies, Tasks)
area: Tooling
module: 6
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Gradle (Project, Dependencies, Tasks)

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** must · **Est:** 4h
> **Why this matters:** Gradle is the other major build tool — concise, fast, and common in newer
> projects and Android. Knowing both Maven and Gradle means you can work in any Java shop.

## Learning Objectives
- Create and understand a Gradle project (`build.gradle`).
- Add dependencies and run tasks.
- Compare Gradle with Maven.

## Learn
- [ ] Do the [Gradle tutorial, part 1: "Initializing the Project"](https://docs.gradle.org/current/userguide/part1_gradle_init.html).
- [ ] Read about the dependency configurations and the wrapper.

## Concepts
- [ ] `build.gradle.kts` (Kotlin DSL — the default for new projects) or `build.gradle` (Groovy) declares
      plugins, `repositories`, `dependencies`, and the Java toolchain; `gradle init` also creates a
      version catalog (`gradle/libs.versions.toml`) that keeps library versions in one place.
- [ ] Dependency configurations: `implementation`, `api`, `testImplementation` (vs Maven scopes).
- [ ] **Tasks** are the unit of work (`build`, `test`, `run`, `jar`); Gradle caches and runs them
      incrementally — usually faster than Maven.
- [ ] The **wrapper** (`gradlew`) pins the Gradle version per project — always use it.
- [ ] Mental map to Maven: dependencies ≈ dependencies, tasks ≈ lifecycle phases, `build.gradle` ≈ `pom.xml`.

## Practice
**Goal:** Build the same kind of project with Gradle.
**Steps:**
- [ ] Create a Gradle project (IDE or `gradle init`).
- [ ] Add a `testImplementation` dependency and confirm resolution.
- [ ] Run `./gradlew build` and `./gradlew test`; locate the artifact in `build/libs`.
- [ ] Note one thing you preferred vs Maven and one you didn't.

## Definition of Done
- [ ] I can read/edit a `build.gradle.kts` and add dependencies.
- [ ] I can run Gradle tasks and use `gradlew`.
- [ ] I can map Gradle concepts to their Maven equivalents.

## Next
- Next: [[M6 - Tooling - Dependency Management and Semantic Versioning]]
