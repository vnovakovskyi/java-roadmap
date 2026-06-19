---
title: Choosing Collections and Big-O Basics
area: Java APIs
module: 4
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Choosing Collections and Big-O Basics

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** good · **Est:** 3h
> **Why this matters:** Picking the right data structure is a daily decision, and a basic sense of
> performance (Big-O) explains *why* one choice beats another. This is awareness, not an algorithms
> course — just enough to choose well and answer the common "why a HashMap here?" question.

## Learning Objectives
- Read Big-O notation at a high level (constant / linear / log).
- Compare the common collections by typical operation cost.
- Choose `ArrayList` vs `LinkedList` vs `HashMap` vs `HashSet` vs `TreeMap` for a task.

## Learn
- [ ] Read a gentle "Big-O for beginners" explainer (visual, not mathematical).
- [ ] Skim a Java "collection time complexity" cheat sheet.

## Concepts
- [ ] **Big-O** describes how cost grows with size *n*: `O(1)` constant, `O(log n)` logarithmic,
      `O(n)` linear, `O(n log n)`, `O(n^2)`. Use it to compare, not to micro-optimize.
- [ ] `ArrayList`: `O(1)` index access, `O(1)` amortized append, `O(n)` middle insert/search.
- [ ] `HashMap`/`HashSet`: ~`O(1)` average add/lookup (needs correct `equals`/`hashCode` —
      [[M3 - OOP - equals, hashCode and toString]]); no ordering.
- [ ] `TreeMap`/`TreeSet`: sorted, `O(log n)` operations.
- [ ] `LinkedList`: fast add/remove at ends, slow random access — rarely the right default.
- [ ] Rule of thumb: `ArrayList` for lists, `HashMap`/`HashSet` for lookups, `Tree*` when you need
      sorted order. Measure only if it actually matters.

## Practice
**Goal:** Make and justify a data-structure choice.
**Steps:**
- [ ] Given "look up users by id thousands of times", pick a structure and say why (Big-O).
- [ ] Compare searching a `List` (`contains`, `O(n)`) vs a `HashSet` (`O(1)`) for membership.
- [ ] Write one sentence per collection: when you'd reach for it.

**Record your result:**
- 

## Definition of Done
- [ ] I can read common Big-O classes and rank them.
- [ ] I can justify a collection choice by its operation costs.
- [ ] I know which structure to default to for lists vs lookups vs sorted data.

## Cheatsheet (my notes)
- 

## Related
- [[M4 - Java APIs - Collections Overview (List, Set, Map)]]
- [[M4 - Java APIs - Iteration and Sorting (Comparable and Comparator)]]
