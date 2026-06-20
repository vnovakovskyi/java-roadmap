---
title: Home
tags:
  - java-roadmap/meta
---

# Java Developer Roadmap — Home

> [!abstract] From zero to a job-ready junior Java developer
> No prior programming experience needed. Work through **10 modules** — Foundations to a full
> Spring Boot project — at your own pace. A realistic target is **~6 months at ~10–12 h/week**,
> but go faster or slower; the path is the same.
> **Start here every session:** check the Dashboard below → pick something from *In Progress* or
> *Next Up* → open the topic → work it top-to-bottom → tick the boxes → set `status: done` when you
> meet the Definition of Done.

## Quick links
- [[_Conventions]] — how this vault works + the frontmatter rules
- [[Tools & Setup]] — install Java, an IDE, Git, Maven and Gradle (start here on day one)
- [[Books & Resources]] — recommended books and free learning resources
- [[Roadmap.canvas|Roadmap (visual)]] — the whole path as a map

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
      - property: area
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
> **status:** `todo` → `doing` → `done` · **priority:** `must` (essential) / `good` (recommended) /
> `optional` (nice extra). If the Dashboard ever fails to render on a device, use the **Module
> Index** below — it always works.

---

## Module Index (fallback navigation)

> The full path, in suggested order. Work modules top-to-bottom. This list always works, even if the
> Dashboard doesn't render on your device.

### Module 1 — Foundations & Setup
- [[M1 - Foundations - How Programming and Java Work]]
- [[M1 - Foundations - Set Up and Verify Your Environment]]
- [[M1 - Foundations - The Command Line Basics]]
- [[M1 - Foundations - Your First Java Program]]
- [[M1 - Foundations - How Java Compiles and Runs]]
- [[M1 - Foundations - Reading Errors and Using the Debugger]]

### Module 2 — Core Java: Syntax & Control Flow
- [[M2 - Core Java - Variables, Primitives and Types]]
- [[M2 - Core Java - Operators and Expressions]]
- [[M2 - Core Java - Strings and Basic Input-Output]]
- [[M2 - Core Java - Conditionals (if and switch)]]
- [[M2 - Core Java - Loops (for and while)]]
- [[M2 - Core Java - Methods and Parameters]]
- [[M2 - Core Java - Arrays]]

### Module 3 — Object-Oriented Programming
- [[M3 - OOP - Classes and Objects]]
- [[M3 - OOP - Fields, Methods and Constructors]]
- [[M3 - OOP - Encapsulation and Access Modifiers]]
- [[M3 - OOP - Inheritance]]
- [[M3 - OOP - Polymorphism and Overriding]]
- [[M3 - OOP - Abstraction, Interfaces and Abstract Classes]]
- [[M3 - OOP - equals, hashCode and toString]]
- [[M3 - OOP - SOLID and Clean Code Principles]]

### Module 4 — Essential Java APIs
- [[M4 - Java APIs - Collections Overview (List, Set, Map)]]
- [[M4 - Java APIs - Choosing Collections and Big-O Basics]]
- [[M4 - Java APIs - Generics Basics]]
- [[M4 - Java APIs - Iteration and Sorting (Comparable and Comparator)]]
- [[M4 - Java APIs - Exceptions and Error Handling]]
- [[M4 - Java APIs - Enums]]
- [[M4 - Java APIs - Optional and Null-Safety]]
- [[M4 - Java APIs - Packages and Project Organization]]

### Module 5 — Modern Java
- [[M5 - Modern Java - Lambdas and Functional Interfaces]]
- [[M5 - Modern Java - The Streams API]]
- [[M5 - Modern Java - Records]]
- [[M5 - Modern Java - var, Enhanced switch and Text Blocks]]
- [[M5 - Modern Java - Date and Time (java.time)]]
- [[M5 - Modern Java - Files and I-O Basics]]
- [[M5 - Modern Java - Concurrency Basics (Threads and Executors)]]
- [[M5 - Modern Java - Virtual Threads (Java 21)]]

### Module 6 — Tooling & Workflow
- [[M6 - Tooling - Git Fundamentals]]
- [[M6 - Tooling - GitHub and Pull Requests]]
- [[M6 - Tooling - Maven (Project, Dependencies, Lifecycle)]]
- [[M6 - Tooling - Gradle (Project, Dependencies, Tasks)]]
- [[M6 - Tooling - Dependency Management and Semantic Versioning]]
- [[M6 - Tooling - Effective IDE Use and Debugging]]

### Module 7 — Testing
- [[M7 - Testing - Why We Test and the Test Pyramid]]
- [[M7 - Testing - JUnit 5 Basics]]
- [[M7 - Testing - Assertions with AssertJ]]
- [[M7 - Testing - Mockito and Test Doubles]]
- [[M7 - Testing - Writing Testable Code (Intro to TDD)]]

### Module 8 — Databases & SQL
- [[M8 - Databases - Relational Concepts]]
- [[M8 - Databases - SQL CRUD and Queries]]
- [[M8 - Databases - Joins and Aggregation]]
- [[M8 - Databases - Connecting from Java (JDBC)]]
- [[M8 - Databases - ORM Intro (JPA and Hibernate)]]
- [[M8 - Databases - Schema Basics and Migrations (Flyway)]]

### Module 9 — Web Development with Spring Boot
- [[M9 - Spring - HTTP and REST Fundamentals]]
- [[M9 - Spring - Spring Boot Intro and Project Setup]]
- [[M9 - Spring - Controllers and REST Endpoints]]
- [[M9 - Spring - Services and Dependency Injection]]
- [[M9 - Spring - Spring Data JPA and Repositories]]
- [[M9 - Spring - Validation and Error Handling]]
- [[M9 - Spring - Configuration and Profiles]]
- [[M9 - Spring - Securing the API with Spring Security]]

### Module 10 — Putting It Together: Capstone
- [[M10 - Project - Designing a Small CRUD App]]
- [[M10 - Project - Building the REST API End-to-End]]
- [[M10 - Project - Persisting with a Real Database]]
- [[M10 - Project - Testing the Application]]
- [[M10 - Project - Good Habits (Logging, Config, README)]]
- [[M10 - Project - Packaging and Running (Jar and Docker Basics)]]
