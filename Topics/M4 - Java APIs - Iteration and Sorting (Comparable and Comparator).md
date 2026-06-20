---
title: Iteration and Sorting (Comparable and Comparator)
area: Java APIs
module: 4
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# Iteration and Sorting (Comparable and Comparator)

> [!info] Topic
> **Area:** Java APIs · **Module:** 4 · **Priority:** must · **Est:** 4h
> **Why this matters:** Sorting and ordering data is an everyday task. Knowing `Comparable` vs
> `Comparator` lets you order objects any way you need — and it sets up the Streams API in Module 5.

## Learning Objectives
- Iterate collections (for-each, iterator, `forEach`).
- Make a class sortable with `Comparable`.
- Sort flexibly with `Comparator` (including by multiple keys).

## Learn
- [ ] Read the `Comparable` and `Comparator` Javadocs.
- [ ] Read about `List.sort`, `Collections.sort`, and `Comparator.comparing`.

## Concepts
- [ ] **`Comparable<T>`**: a class's *natural* order via `compareTo` (returns −/0/+).
- [ ] **`Comparator<T>`**: an external/alternate order — pass it to `sort`.
- [ ] Build comparators fluently: `Comparator.comparing(Person::age).thenComparing(Person::name)`;
      `.reversed()` to flip.
- [ ] Iteration options: for-each (default), `Iterator` (when removing during iteration), `forEach`.
- [ ] `compareTo`/`compare` must be consistent with `equals` to avoid surprises in sorted sets/maps.

## Practice
**Goal:** Order objects two different ways.
**Steps:**
- [ ] Give `Person(name, age)` a natural order by name via `Comparable`.
- [ ] Sort a `List<Person>` by age using a `Comparator`, then by age-then-name.
- [ ] Reverse the order with `.reversed()`.

## Definition of Done
- [ ] I can implement `Comparable` for natural ordering.
- [ ] I can sort with a `Comparator`, including multi-key and reversed.
- [ ] I can choose the right iteration approach.

## Next
- Next: [[M4 - Java APIs - Exceptions and Error Handling]]
