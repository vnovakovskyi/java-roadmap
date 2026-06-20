---
title: Dependency Management and Semantic Versioning
area: Tooling
module: 6
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Dependency Management and Semantic Versioning

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** good · **Est:** 2h
> **Why this matters:** Real apps stand on dozens of libraries. Understanding versions, transitive
> dependencies, and conflicts saves you from "works on my machine" and mysterious runtime errors.

## Learning Objectives
- Read and reason about version numbers (semver).
- Understand transitive dependencies and conflicts.
- Find and pick library versions responsibly.

## Learn
- [ ] Read [semver.org](https://semver.org) (it's short).
- [ ] Read how Maven/Gradle resolve transitive dependencies and conflicts.

## Concepts
- [ ] **Semantic versioning** `MAJOR.MINOR.PATCH`: major = breaking, minor = features, patch = fixes.
- [ ] **Transitive dependencies**: your library's dependencies become yours too.
- [ ] Conflicts: two libs want different versions of the same dependency; the build tool picks one
      (Maven "nearest wins", Gradle "highest wins") — inspect with `mvn dependency:tree` /
      `gradle dependencies`.
- [ ] A **BOM** (bill of materials, e.g. Spring Boot's) aligns a set of versions for you.
- [ ] Don't blindly upgrade majors; read changelogs. Watch for known vulnerabilities.

## Practice
**Goal:** Inspect and tame the dependency graph.
**Steps:**
- [ ] Print the dependency tree of a project and find a transitive dependency.
- [ ] Identify a version conflict (or force one) and resolve it.
- [ ] Look up a popular library on Maven Central and read its version history.

## Definition of Done
- [ ] I can interpret semver and decide if an upgrade is risky.
- [ ] I can read a dependency tree and resolve a conflict.
- [ ] I understand transitive dependencies and BOMs.

## Next
- Next: [[M6 - Tooling - Effective IDE Use and Debugging]]
