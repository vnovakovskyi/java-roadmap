---
title: Collections Overview (List, Set, Map)
area: Java APIs
module: 4
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Collections Overview (List, Set, Map)

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** must · **Est:** 5h
> **Why this matters:** Real programs juggle groups of data. The Collections Framework — `List`,
> `Set`, `Map` — is used in essentially every Java codebase. This is a core, daily skill.

## Learning Objectives
- Choose the right collection (`List` vs `Set` vs `Map`) for a problem.
- Use `ArrayList`, `HashSet`, and `HashMap` confidently.
- Iterate, add, remove, and look up elements.

## Learn
- [ ] Read: [dev.java — "The Collections Framework"](https://dev.java/learn/api/collections-framework/).
- [ ] Read the Javadoc intros for `List`, `Set`, `Map`.

## Concepts
- [ ] **List** = ordered, allows duplicates, index access (`ArrayList`). **Set** = no duplicates
      (`HashSet`; `LinkedHashSet` keeps order; `TreeSet` sorts). **Map** = key→value (`HashMap`).
- [ ] Program to the interface: `List<String> x = new ArrayList<>();`.
- [ ] `Map` essentials: `put`, `get`, `getOrDefault`, `containsKey`, `keySet`, `entrySet`,
      `computeIfAbsent`.
- [ ] Hash-based collections rely on correct `equals`/`hashCode` (see Module 3).
- [ ] Prefer `List.of(...)` / `Map.of(...)` for small immutable collections.

## Practice
**Goal:** Use each collection for a fitting task.
**Steps:**
- [ ] `List`: read words into an `ArrayList`, print them in order.
- [ ] `Set`: count the number of *unique* words.
- [ ] `Map`: build a word-frequency count with `merge`/`getOrDefault` and print the top entries.

**Record your result:**
- 

## Definition of Done
- [ ] I can pick `List`/`Set`/`Map` appropriately and justify it.
- [ ] I can do CRUD + iteration on each.
- [ ] I understand why `Map`/`Set` depend on `equals`/`hashCode`.

## Cheatsheet (my notes)
- 

## Related
- [[M2 - Core Java - Arrays]]
- [[M4 - Java APIs - Generics Basics]]
- [[M3 - OOP - equals, hashCode and toString]]
