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
- [ ] Read:
      [dev.java — Storing Data Using the Collections Framework](https://dev.java/learn/api/collections-and-streams/collections-framework/intro/).
- [ ] Read:
      [Lists](https://dev.java/learn/api/collections-and-streams/collections-framework/lists/),
      [Sets](https://dev.java/learn/api/collections-and-streams/collections-framework/sets/),
      [Maps](https://dev.java/learn/api/collections-and-streams/collections-framework/maps/)
      (dev.java).
- [ ] Read:
      [Creating Data with the Collections Factory Methods](https://dev.java/learn/api/collections-and-streams/collections-framework/factory-methods/)
      (`List.of`, `Map.of`).

## Concepts
- [ ] **List** = ordered, allows duplicates, index access (`ArrayList`). **Set** = no duplicates
      (`HashSet`; `LinkedHashSet` keeps insertion order; `TreeSet` sorts). **Map** = key→value
      (`HashMap`, `LinkedHashMap`, `TreeMap`).
- [ ] Program to the interface: `List<String> names = new ArrayList<>();`.
- [ ] `Map` essentials: `put`, `get`, `getOrDefault`, `containsKey`, `keySet`, `values`, `entrySet`,
      `merge`.
- [ ] Hash-based collections rely on correct `equals`/`hashCode` (Module 3).
- [ ] `List.of(...)` / `Map.of(...)` create small **immutable** collections (no `add`, no `null`s);
      wrap in `new ArrayList<>(...)` when you need to modify.
- [ ] *(Java 21+)* **Sequenced collections**: `getFirst()`, `getLast()`, `reversed()`,
      `addFirst(...)` work on lists, `LinkedHashSet`, `LinkedHashMap`, and more.

## Practice
**Goal:** Use each collection for a fitting task.
**Steps:**
- [ ] `List`: read words into an `ArrayList`, print them in order, then `getFirst()`/`getLast()`.
- [ ] `Set`: count the number of *unique* words.
- [ ] `Map`: build a word-frequency count with `getOrDefault` (or `merge`) and print each word with
      its count.
- [ ] Try `List.of("a").add("b")` and read the exception.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Describe `List`, `Set`, and `Map` in one line each.
> `List`: ordered sequence with duplicates and index access. `Set`: no duplicates. `Map`: unique
> keys, each mapped to a value.

> [!question]- What happens on `List.of(1, 2, 3).add(4)`?
> `UnsupportedOperationException` — `List.of` returns an immutable list. Copy it into an `ArrayList`
> to modify.

> [!question]- What's the iteration order of `HashSet`, `LinkedHashSet`, and `TreeSet`?
> `HashSet`: no guaranteed order. `LinkedHashSet`: insertion order. `TreeSet`: sorted order.

> [!question]- How do you get the last element of a list in Java 21+?
> `list.getLast()` (before: `list.get(list.size() - 1)`).

## Definition of Done
- [ ] I can pick `List`/`Set`/`Map` appropriately and justify it.
- [ ] I can add, remove, look up, and iterate on each.
- [ ] I understand why `Map`/`Set` depend on `equals`/`hashCode`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M4 - Java APIs - Choosing Collections and Big-O Basics]]
