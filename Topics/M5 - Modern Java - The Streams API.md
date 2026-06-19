---
title: The Streams API
area: Modern Java
module: 5
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# The Streams API

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** must · **Est:** 5h
> **Why this matters:** Streams express data transformations — filter, map, reduce, group — clearly
> and without manual loops. Modern Java codebases use them everywhere; this is a must-have skill.

## Learning Objectives
- Build stream pipelines: source → intermediate ops → terminal op.
- Use `filter`, `map`, `sorted`, `collect`, `reduce`.
- Group and summarize data with `Collectors`.

## Learn
- [ ] Read: [dev.java — "The Stream API"](https://dev.java/learn/api/streams/).
- [ ] Read about `Collectors` (`toList`, `groupingBy`, `joining`, `counting`).

## Concepts
- [ ] A pipeline: `stream()` → intermediate (`filter`, `map`, `sorted`, `distinct`, `limit`) →
      terminal (`collect`, `forEach`, `count`, `reduce`, `findFirst`).
- [ ] Streams are **lazy** (intermediate ops run only when a terminal op fires) and **don't mutate**
      the source.
- [ ] `collect(Collectors.toList())`, `groupingBy(...)`, `joining(", ")` are workhorses.
- [ ] `reduce` folds elements into one value; `mapToInt(...).sum()` for numeric sums.
- [ ] Pairs naturally with `Optional` (`findFirst`) and lambdas/method references.

## Practice
**Goal:** Rewrite loops as stream pipelines.
**Steps:**
- [ ] From a `List<Person>`: collect the names of everyone over 18, sorted.
- [ ] Group people by city with `groupingBy`; count per group.
- [ ] Sum ages with `mapToInt(...).sum()`; compute the average.

**Record your result:**
- 

## Definition of Done
- [ ] I can build filter/map/collect pipelines.
- [ ] I can group and summarize with `Collectors`.
- [ ] I understand laziness and that streams don't mutate the source.

## Cheatsheet (my notes)
- 

## Related
- [[M5 - Modern Java - Lambdas and Functional Interfaces]]
- [[M4 - Java APIs - Optional and Null-Safety]]
