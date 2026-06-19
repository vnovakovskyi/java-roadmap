---
title: Good Habits (Logging, Config, README)
area: Project
module: 10
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Good Habits (Logging, Config, README)

> [!info] Topic
> **Area:** Project · **Module:** 10 · **Priority:** good · **Est:** 3h
> **Why this matters:** The difference between a toy and a portfolio piece is the finishing touches —
> useful logs, clean config, and a README that lets anyone run it. These habits get you hired.

## Learning Objectives
- Add structured, level-appropriate logging.
- Keep configuration and secrets clean.
- Write a README that lets others run the project.

## Learn
- [ ] Read about SLF4J logging and log levels.
- [ ] Look at a few well-written project READMEs for structure.

## Concepts
- [ ] Use SLF4J (`LoggerFactory.getLogger`) with levels: `error`/`warn`/`info`/`debug`; don't log
      secrets or use `System.out` in real code.
- [ ] Externalize config and keep secrets out of Git ([[M9 - Spring - Configuration and Profiles]]).
- [ ] A good README: what it is, how to run it (prereqs + commands), API overview, and tech used.
- [ ] Sensible commit history and a license make the repo look professional
      ([[M6 - Tooling - GitHub and Pull Requests]]).
- [ ] Small touches: meaningful names, no dead code, consistent formatting.

## Practice
**Goal:** Make the project presentable.
**Steps:**
- [ ] Replace any `System.out` with proper logging at sensible levels.
- [ ] Confirm no secrets are committed; document required env vars.
- [ ] Write a README that a stranger could follow to run the app.

**Record your result:**
- 

## Definition of Done
- [ ] The app logs usefully without leaking secrets.
- [ ] Config is clean and secrets are out of Git.
- [ ] The README lets someone else run the project.

## Cheatsheet (my notes)
- 

## Related
- [[M10 - Project - Testing the Application]]
- [[M10 - Project - Packaging and Running (Jar and Docker Basics)]]
