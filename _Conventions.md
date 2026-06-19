---
title: Conventions
tags:
  - java-roadmap/meta
---

# Conventions & How To Use This Vault

This note explains how the **Java Developer Roadmap** works. Read it once, then mostly forget it —
the day-to-day flow is straightforward.

## The daily workflow

1. Open **[[Java Developer Roadmap - MOC]]** (bookmark it: right-click → Bookmark — one tap on
   desktop and mobile).
2. Look at the **Dashboard** → the `In Progress` and `Next Up` views. No dashboard? Use the
   **Module Index** in the MOC — it always works.
3. Open a topic note and work the sections top-to-bottom:
   **Learning Objectives → Learn → Concepts → Practice → Definition of Done**.
4. Tick the checkboxes as you go. When you start a topic, set its `status: doing`. When you can
   honestly check every **Definition of Done** item, set `status: done`.

That's it. Progress shows up automatically in the Dashboard.

## How the path is organized

The roadmap is split into **10 modules** (M1–M10), each a stage on the way from zero to a
job-ready junior Java developer. Work them roughly in order — later modules build on earlier ones.

| Module | Area | Focus |
| ------ | ---- | ----- |
| M1 | Foundations | How programming and Java work; install and run your first program |
| M2 | Core Java | Syntax, types, control flow, methods, arrays |
| M3 | OOP | Classes, objects, inheritance, polymorphism, interfaces, SOLID & clean code |
| M4 | Java APIs | Collections, generics, exceptions, enums, Optional |
| M5 | Modern Java | Lambdas, streams, records, date/time, files, concurrency basics |
| M6 | Tooling | Git, GitHub, Maven, Gradle, the IDE |
| M7 | Testing | JUnit 5, AssertJ, Mockito, testable code |
| M8 | Databases | SQL, JDBC, JPA/Hibernate, migrations |
| M9 | Spring | HTTP/REST, Spring Boot, building & securing a REST API |
| M10 | Project | Capstone: a full CRUD app, end-to-end |

## Property vocabulary (frontmatter)

Every topic note carries these properties. **Values are controlled** — stick to the lists below or
the Dashboard views will miss the note.

| Property   | Type   | Allowed values | Meaning |
| ---------- | ------ | -------------- | ------- |
| `title`    | text   | free | Display title |
| `area`     | text   | `Foundations`, `Core Java`, `OOP`, `Java APIs`, `Modern Java`, `Tooling`, `Testing`, `Databases`, `Spring`, `Project` | Knowledge area |
| `module`   | number | `1`–`10` | Which module of the path |
| `status`   | text   | `todo`, `doing`, `done` | Progress state (drives the Dashboard) |
| `priority` | text   | `must`, `good`, `optional` | `must` = essential · `good` = good to know · `optional` = nice extra / for later |
| `effort`   | number | hours | Rough estimate (~2–6h typical) |
| `tags`     | list   | must include `java-roadmap` | Used by the Dashboard filter |

> [!important] The two rules that keep the Dashboard working
> 1. Every topic note **must** include the tag `java-roadmap`.
> 2. `status` must be exactly one of `todo` / `doing` / `done` (lowercase).

## The priority tiers

You do not have to do everything. Tiers tell you what matters:

- **`must`** — core path. Do these; a junior developer is expected to know them.
- **`good`** — strongly recommended. Do them once the `must` items in a module are solid.
- **`optional`** — nice to have or a taste of something more advanced. Skip without guilt; come back later.

## The topic-note loop

Each topic note has the same shape so studying is frictionless:

1. **Learning Objectives** — what you'll be able to do afterward.
2. **Learn** — curated, mostly-free resources: what to read or watch.
3. **Concepts** — the key ideas to nail (and, later in the path, a "going deeper" layer).
4. **Practice** — a concrete, hands-on task. This is where the learning sticks.
5. **Definition of Done** — the checklist that lets you mark the topic `done`.
   Plus a **Cheatsheet** (your own distilled notes) and **Related** links.

## File naming

`M{module} - {Area} - {Topic}.md`, e.g. `M3 - OOP - Inheritance.md`. All topic notes live in
`Topics/`.

## Stack assumptions

Content targets **Java 21 (LTS)**. The web module uses **Spring Boot 3.x**. Build-tool topics cover
both **Maven** and **Gradle**. Version-sensitive items are flagged inline.

## Adding a new topic

Copy **[[_Template - Topic]]**, drop the copy in `Topics/`, and fill in the frontmatter. It appears
in the Dashboard automatically.
