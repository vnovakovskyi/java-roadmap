---
title: Conventions
tags:
  - java-roadmap/meta
---

# Conventions & How To Use This Vault

This note explains how the **Java Developer Roadmap** works. Read it once, then mostly forget it —
the day-to-day flow is straightforward.

> [!tip] Studying with the tutor
> The roadmap is made to be studied with the
> [tutor](https://github.com/vnovakovskyi/claude-learn-skills) plugin for Claude Code. The tutor
> reads this vault as its curriculum — the Module Index in [[Home]] for the order, the topic
> sections, the Self-check questions for quizzes, the Definition of Done for finishing a topic — and
> keeps your progress in a workbook of its own. It never edits the roadmap and ignores `status` and
> checkboxes, so with the tutor, skip the daily workflow below and leave them as they are. How to
> start: [[README]].

## The daily workflow (studying on your own)

1. Open **[[Home]]** (bookmark it: right-click → Bookmark — one tap on
   desktop and mobile).
2. Look at the **Dashboard** → the `In Progress` and `Next Up` views. No dashboard? Use the
   **Module Index** in [[Home]] — it always works.
3. Open a topic note and work the sections top-to-bottom:
   **Learning Objectives → Learn → Concepts → Practice → Self-check → Definition of Done**.
4. Tick the checkboxes as you go. When you start a topic, set its `status: doing`. When you can
   honestly check every **Definition of Done** item, set `status: done`.
5. Commit your practice code to Git (from the end of Module 1 on).

That's it. Progress shows up automatically in the Dashboard.

## How the path is organized

The roadmap is split into **11 modules** (M1–M11), each a stage on the way from zero to a
job-ready junior Java developer. Work them roughly in order — later modules build on earlier ones.
Inside a module, topics are numbered in the order to study them: the path starts at **M1.01**.

| Module | Area | Focus |
| ------ | ---- | ----- |
| M1 | Foundations | How programming and Java work; setup, terminal, debugger, Git basics, learning with AI |
| M2 | Core Java | Syntax, types, control flow, methods, recursion, arrays |
| M3 | OOP | Classes, memory, encapsulation, inheritance, polymorphism, interfaces, SOLID, design patterns |
| M4 | Java APIs | Wrappers & BigDecimal, collections, generics, sorting, exceptions, enums, Optional |
| M5 | Modern Java | Lambdas, streams, records, pattern matching & sealed types, date/time, files, concurrency |
| M6 | Tooling | Git branching, GitHub & PRs, Maven, Gradle, CI, Docker, the IDE, AI assistants |
| M7 | Testing | Test pyramid, JUnit, AssertJ, Mockito, testable code |
| M8 | Databases | SQL, joins, transactions & indexes, JDBC, JPA/Hibernate, Flyway |
| M9 | Spring | HTTP/REST, Spring Boot, data, validation, config, REST clients, docs, security |
| M10 | Project | Capstone: your own CRUD app, end-to-end, tested and containerized |
| M11 | Career | Portfolio, CV, interviews, coding practice, the job search, what's next |

### The Bookshelf project

Modules 2–8 each end with a **Module Project** that grows the same app, **Bookshelf**, by one
version — from a console program with arrays (v1) to a tested, CI-checked app on PostgreSQL (v7).
Keep it in its own GitHub repository and tag every version (`v1`, `v2`, …). Module 9 teaches Spring
using the same book domain; the Module 10 capstone is then an app of your own design.

## Property vocabulary (frontmatter)

Every topic note carries these properties. **Values are controlled** — stick to the lists below or
the Dashboard views (and the vault check) will miss the note.

| Property   | Type   | Allowed values | Meaning |
| ---------- | ------ | -------------- | ------- |
| `title`    | text   | free | Display title (must equal the note's `#` heading) |
| `area`     | text   | `Foundations`, `Core Java`, `OOP`, `Java APIs`, `Modern Java`, `Tooling`, `Testing`, `Databases`, `Spring`, `Project`, `Career` | Knowledge area — one per module, see the table above |
| `module`   | number | `1`–`11` | Which module of the path |
| `status`   | text   | `todo`, `doing`, `done` | Progress state (drives the Dashboard) |
| `priority` | text   | `must`, `good`, `optional` | `must` = core path · `good` = recommended · `optional` = nice extra / for later |
| `effort`   | number | hours | Rough estimate for a beginner (~2–6h typical) |
| `tags`     | list   | must include `java-roadmap` | Used by the Dashboard filter |

> [!important] The two rules that keep the Dashboard working
> 1. Every topic note **must** include the tag `java-roadmap`.
> 2. `status` must be exactly one of `todo` / `doing` / `done` (lowercase).

## The priority tiers

- **`must`** — the **core path** (~260 h): what a junior Java developer is expected to know. The
  Dashboard's *Core Path* view lists only these. Short on time? Do these first.
- **`good`** — strongly recommended. Do them once the `must` items of a module are solid.
- **`optional`** — nice to have or a taste of something more advanced. Skip without guilt; come back later.

## The topic-note loop

Each topic note has the same shape so studying is frictionless:

1. **Learning Objectives** — what you'll be able to do afterward.
2. **Learn** — curated, free resources with direct links: what to read, watch, or do.
3. **Concepts** — the key ideas to nail.
4. **Practice** — a concrete, hands-on task. This is where the learning sticks.
5. **Self-check** — 3–5 questions with collapsible answers. Answer first, then expand to compare.
   Together they're also your interview question bank (see Module 11).
6. **Definition of Done** — the checklist that lets you mark the topic `done`.
   The note ends with a **Next** link to the following topic, so you can move straight on.

## Learning with AI

Use AI assistants as a tutor — to explain, hint, quiz, and review code *you* wrote — not to solve
the Practice tasks for you. The rules are in [[M1.07 - Foundations - Getting Unstuck and Learning with AI]];
using AI on the job is covered in [[M6.07 - Tooling - AI Coding Assistants in Your Workflow]].

## File naming

`M{module}.{position} - {Area} - {Topic}.md`, e.g. `M3.05 - OOP - Inheritance.md`, the 5th topic of
Module 3. The position is the topic's place in the **Module Index** in [[Home]], so Obsidian's file
list shows the topics in study order. All topic notes live in `Topics/`.

## Stack assumptions

*Last reviewed: October 2026.*

| Piece | Version used in this vault | Notes |
| ----- | -------------------------- | ----- |
| Java | **25 (LTS)**, Eclipse Temurin | Newer releases (26, 27) are short-term; the next LTS is 29 (Sept 2027) |
| Spring Boot | **4.x** (4.1 at review time) | Spring Framework 7, Spring Security 7, Jackson 3, Hibernate 7. Spring Boot 3.x left open-source support in June 2026 |
| Testing | **JUnit 6** (Jupiter), AssertJ, Mockito 5, Testcontainers 2 | "JUnit 5" tutorials still apply — same Jupiter API |
| Build | **Maven 3.9** (Maven 4 is a release candidate), **Gradle 9** (Kotlin DSL) | Always via the wrapper (`./mvnw`, `./gradlew`) |
| Database | **PostgreSQL 18** in Docker, Flyway | |
| IDE | **IntelliJ IDEA** (free tier) | VS Code or Eclipse work too |

Version-sensitive items are flagged inline, e.g. *(Java 25+)* or *(Spring Boot 4)*. When reading
older tutorials, expect differences — the main ones are listed in
[[M9.02 - Spring - Spring Boot Intro and Project Setup]].

## Adding or changing a topic

1. Copy **[[_Template - Topic]]** into `Topics/` as `M{module} - {Area} - {Topic}.md` (no position
   yet) and fill in the frontmatter and every section.
2. Add it to the **Module Index** in [[Home]] at the right position — that list defines the order.
   To reorder topics, move their lines there.
3. Run `python3 .github/scripts/vault.py build`. It numbers the topics by their place in the index
   (the topics after a new one in the same module shift by one, other modules stay as they are),
   updates every link to a renamed note, sets the **Next** links, and regenerates the visual map, the
   canvas, and the README index.
4. Run `python3 .github/scripts/vault.py check` — CI runs the same check on every PR.

It appears in the Dashboard automatically.
