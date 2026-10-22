---
title: Home
tags:
  - java-roadmap/meta
---

# Java Developer Roadmap — Home

> [!abstract] From zero to a job-ready junior Java developer
> No prior programming experience needed. Work through **11 modules** — from "what is a program" to
> a secured Spring Boot API and your first job search — at your own pace. A realistic target is
> **~7 months at ~10–12 h/week** (~335 h in total; the core `must` path is ~260 h).
> **Studying on your own? Start here every session:** check the Dashboard below → pick something
> from *In Progress* or *Next Up* → open the topic → work it top-to-bottom → answer its Self-check →
> set `status: done` when you meet the Definition of Done.

> [!tip] Made to be studied with the tutor
> The recommended way through this roadmap is the
> [tutor](https://github.com/vnovakovskyi/claude-learn-skills) plugin for Claude Code: it teaches
> each topic, reviews your practice, quizzes you, and keeps your progress in a workbook of its own.
> With the tutor you don't need the Dashboard below — leave the `status` fields and checkboxes here
> as they are, so `git pull` brings you roadmap updates cleanly. Setup: install the plugin, then run
> `/tutor:enroll` in this folder (see [[README]]).

## Quick links
- [[_Conventions]] — how this vault works + the frontmatter rules
- [[Tools & Setup]] — install Java 25, an IDE, Git, the build tools, and Docker (start here on day one)
- [[Books & Resources]] — recommended books and free learning resources
- [[Roadmap.canvas|Roadmap (visual)]] — the whole path as a map

> [!example] One project, seven versions: Bookshelf
> From Module 2 to Module 8 every module ends with a new version of the same app — **Bookshelf**:
> a console app (M2) → classes (M3) → collections (M4) → modern Java and files (M5) → a real build
> with CI (M6) → tests (M7) → PostgreSQL (M8). Then Module 9 teaches Spring with the same domain, and
> the Module 10 capstone is an app of your own design, built end to end.

> [!tip] Bookmark this note (right-click → Bookmark) so it's one tap away on desktop and mobile.
> Prefer a map? Open the interactive [[Roadmap.canvas|Roadmap canvas]] and click any topic.

## Live Dashboard

```base
filters:
  and:
    - file.hasTag("java-roadmap")
    - file.ext == "md"
    - note.module >= 1
properties:
  note.area:
    displayName: Area
  note.module:
    displayName: Module
  note.status:
    displayName: Status
  note.priority:
    displayName: Priority
  note.effort:
    displayName: Effort (h)
views:
  - type: table
    name: By Module
    order:
      - file.name
      - module
      - area
      - status
      - priority
      - effort
    sort:
      - property: module
        direction: ASC
  - type: table
    name: In Progress
    filters:
      and:
        - note.status == "doing"
    order:
      - file.name
      - module
      - area
      - effort
    sort:
      - property: module
        direction: ASC
  - type: table
    name: Next Up
    filters:
      and:
        - note.status == "todo"
    order:
      - file.name
      - module
      - area
      - priority
      - effort
    sort:
      - property: module
        direction: ASC
  - type: table
    name: Core Path (must)
    filters:
      and:
        - note.priority == "must"
    order:
      - file.name
      - module
      - status
      - effort
    sort:
      - property: module
        direction: ASC
  - type: table
    name: By Area
    order:
      - file.name
      - area
      - module
      - status
      - priority
      - effort
    sort:
      - property: area
        direction: ASC
      - property: module
        direction: ASC
  - type: table
    name: Done
    filters:
      and:
        - note.status == "done"
    order:
      - file.name
      - module
      - area
      - effort
    sort:
      - property: module
        direction: ASC
```

> [!note] Legend
> **status:** `todo` → `doing` → `done` · **priority:** `must` (core path) / `good` (recommended) /
> `optional` (nice extra). Short on time? Follow the **Core Path** view first and come back for the
> rest. If the Dashboard ever fails to render on a device, use the **Module Index** below — it always
> works.

---

## Module Index

> The full path, in suggested order — work modules top-to-bottom. This list always works, even if
> the Dashboard doesn't render on your device. (It's also the source of truth for the order of
> topics: `.github/scripts/vault.py` builds the visual map from it.)

### Module 1 — Foundations & Setup
- [[M1 - Foundations - How Programming and Java Work]]
- [[M1 - Foundations - Set Up and Verify Your Environment]]
- [[M1 - Foundations - Your First Java Program]]
- [[M1 - Foundations - The Command Line Basics]]
- [[M1 - Foundations - How Java Compiles and Runs]]
- [[M1 - Foundations - Reading Errors and Using the Debugger]]
- [[M1 - Foundations - Getting Unstuck and Learning with AI]]
- [[M1 - Foundations - Saving Your Work with Git]]

### Module 2 — Core Java: Syntax & Control Flow
- [[M2 - Core Java - Variables, Primitives and Types]]
- [[M2 - Core Java - Operators and Expressions]]
- [[M2 - Core Java - Strings and Basic Input-Output]]
- [[M2 - Core Java - Conditionals (if and switch)]]
- [[M2 - Core Java - Loops (for and while)]]
- [[M2 - Core Java - Methods and Parameters]]
- [[M2 - Core Java - Recursion]]
- [[M2 - Core Java - Arrays]]
- [[M2 - Core Java - Module Project (Console Bookshelf)]]

### Module 3 — Object-Oriented Programming
- [[M3 - OOP - Classes and Objects]]
- [[M3 - OOP - Fields, Methods and Constructors]]
- [[M3 - OOP - Memory Basics (Stack, Heap and Garbage Collection)]]
- [[M3 - OOP - Encapsulation and Access Modifiers]]
- [[M3 - OOP - Inheritance]]
- [[M3 - OOP - Polymorphism and Overriding]]
- [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]]
- [[M3 - OOP - equals, hashCode and toString]]
- [[M3 - OOP - SOLID and Clean Code Principles]]
- [[M3 - OOP - Design Patterns (the Essential Few)]]
- [[M3 - OOP - Module Project (Bookshelf with Classes)]]

### Module 4 — Essential Java APIs
- [[M4 - Java APIs - Wrapper Types, Autoboxing and BigDecimal]]
- [[M4 - Java APIs - Collections Overview (List, Set, Map)]]
- [[M4 - Java APIs - Choosing Collections and Big-O Basics]]
- [[M4 - Java APIs - Generics Basics]]
- [[M4 - Java APIs - Iteration and Sorting (Comparable and Comparator)]]
- [[M4 - Java APIs - Exceptions and Error Handling]]
- [[M4 - Java APIs - Enums]]
- [[M4 - Java APIs - Optional and Null-Safety]]
- [[M4 - Java APIs - Packages and Project Organization]]
- [[M4 - Java APIs - Module Project (Bookshelf with Collections)]]

### Module 5 — Modern Java
- [[M5 - Modern Java - Lambdas and Functional Interfaces]]
- [[M5 - Modern Java - The Streams API]]
- [[M5 - Modern Java - Records]]
- [[M5 - Modern Java - var, Enhanced switch and Text Blocks]]
- [[M5 - Modern Java - Pattern Matching and Sealed Types]]
- [[M5 - Modern Java - Date and Time (java.time)]]
- [[M5 - Modern Java - Files and I-O Basics]]
- [[M5 - Modern Java - Concurrency Basics (Threads and Executors)]]
- [[M5 - Modern Java - Virtual Threads (Java 21)]]
- [[M5 - Modern Java - Module Project (Bookshelf Stats and Saving)]]

### Module 6 — Tooling & Workflow
- [[M6 - Tooling - Git Branching, Merging and Undo]]
- [[M6 - Tooling - GitHub and Pull Requests]]
- [[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]]
- [[M6 - Tooling - Gradle (Project, Dependencies, Tasks)]]
- [[M6 - Tooling - Dependency Management and Semantic Versioning]]
- [[M6 - Tooling - Effective IDE Use and Debugging]]
- [[M6 - Tooling - AI Coding Assistants in Your Workflow]]
- [[M6 - Tooling - Continuous Integration with GitHub Actions]]
- [[M6 - Tooling - Docker Basics for Developers]]
- [[M6 - Tooling - Module Project (Bookshelf as a Real Project)]]

### Module 7 — Testing
- [[M7 - Testing - Why We Test and the Test Pyramid]]
- [[M7 - Testing - JUnit Basics]]
- [[M7 - Testing - Assertions with AssertJ]]
- [[M7 - Testing - Mockito and Test Doubles]]
- [[M7 - Testing - Writing Testable Code (Intro to TDD)]]
- [[M7 - Testing - Module Project (Testing the Bookshelf)]]

### Module 8 — Databases & SQL
- [[M8 - Databases - Relational Concepts]]
- [[M8 - Databases - SQL CRUD and Queries]]
- [[M8 - Databases - Joins and Aggregation]]
- [[M8 - Databases - Transactions and Indexes]]
- [[M8 - Databases - Connecting from Java (JDBC)]]
- [[M8 - Databases - ORM Intro (JPA and Hibernate)]]
- [[M8 - Databases - Schema Basics and Migrations (Flyway)]]
- [[M8 - Databases - Module Project (Bookshelf on PostgreSQL)]]

### Module 9 — Web Development with Spring Boot
- [[M9 - Spring - HTTP and REST Fundamentals]]
- [[M9 - Spring - Spring Boot Intro and Project Setup]]
- [[M9 - Spring - Controllers and REST Endpoints]]
- [[M9 - Spring - Services and Dependency Injection]]
- [[M9 - Spring - Spring Data JPA and Repositories]]
- [[M9 - Spring - Validation and Error Handling]]
- [[M9 - Spring - Configuration and Profiles]]
- [[M9 - Spring - Calling Other APIs with RestClient]]
- [[M9 - Spring - API Docs and Monitoring (OpenAPI and Actuator)]]
- [[M9 - Spring - Securing the API with Spring Security]]

### Module 10 — Putting It Together: Capstone
- [[M10 - Project - Designing a Small CRUD App]]
- [[M10 - Project - Building the REST API End-to-End]]
- [[M10 - Project - Persisting with a Real Database]]
- [[M10 - Project - Testing the Application]]
- [[M10 - Project - Good Habits (Logging, Config, README)]]
- [[M10 - Project - Packaging and Running (Jar and Container Image)]]

### Module 11 — Getting Hired
- [[M11 - Career - Building Your Portfolio and GitHub Profile]]
- [[M11 - Career - Writing a Developer CV]]
- [[M11 - Career - Preparing for Technical Interviews]]
- [[M11 - Career - Coding Interview Practice (Algorithms Basics)]]
- [[M11 - Career - The Job Search]]
- [[M11 - Career - What's Next After the Roadmap]]
