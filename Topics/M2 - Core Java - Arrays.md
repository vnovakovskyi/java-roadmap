---
title: Arrays
area: Core Java
module: 2
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# Arrays

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 3h
> **Why this matters:** Arrays are the simplest way to hold many values. They're the bridge to
> collections (Module 4) and the substrate of countless algorithms.

## Learning Objectives
- Create, fill, and read fixed-size arrays.
- Iterate arrays and handle index bounds safely.
- Use basic `Arrays` utility methods.

## Learn
- [ ] Read: [dev.java — "Arrays"](https://dev.java/learn/).
- [ ] Read the `java.util.Arrays` Javadoc (sort, fill, toString, copyOf).

## Concepts
- [ ] Declaration: `int[] nums = new int[5];` or `int[] nums = {1, 2, 3};`.
- [ ] Fixed length: `nums.length` (a field, no parentheses); indices `0 .. length-1`.
- [ ] Out-of-bounds access throws `ArrayIndexOutOfBoundsException`.
- [ ] Iterate with an index `for` (when you need `i`) or for-each (when you don't).
- [ ] `Arrays.sort`, `Arrays.toString`, `Arrays.copyOf`; 2D arrays are arrays of arrays.

## Practice
**Goal:** Manipulate arrays confidently.
**Steps:**
- [ ] Fill an array with 10 numbers and compute the sum, min, and max in one pass.
- [ ] Reverse an array in place.
- [ ] Sort an array with `Arrays.sort` and print it with `Arrays.toString`.

## Definition of Done
- [ ] I can create, fill, and iterate arrays without index errors.
- [ ] I can use `Arrays` helpers for sort/print/copy.
- [ ] I understand arrays have fixed length (and why collections exist).

## Next
- Next: [[M3 - OOP - Classes and Objects]]
