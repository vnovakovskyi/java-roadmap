---
title: Assertions with AssertJ
area: Testing
module: 7
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# Assertions with AssertJ

> [!info] Topic
> **Area:** Testing · **Module:** 7 · **Priority:** good · **Est:** 2h
> **Why this matters:** AssertJ's fluent assertions make tests far more readable and their failure
> messages far clearer than plain JUnit asserts. It's the de-facto assertion library in Spring projects.

## Learning Objectives
- Write fluent assertions with AssertJ.
- Assert on collections, strings, and exceptions.
- Read AssertJ's descriptive failure messages.

## Learn
- [ ] Read the [AssertJ "Getting started"](https://assertj.github.io/doc/) section.
- [ ] Add AssertJ to your test dependencies.

## Concepts
- [ ] One entry point: `assertThat(actual)` then chained, readable checks.
- [ ] Objects: `isEqualTo`, `isNotNull`, `isInstanceOf`.
- [ ] Collections: `contains`, `containsExactly`, `hasSize`, `extracting(...)`.
- [ ] Strings: `startsWith`, `contains`, `matches`.
- [ ] Exceptions: `assertThatThrownBy(() -> ...).isInstanceOf(...).hasMessageContaining(...)`.
- [ ] Failure messages describe expected vs actual clearly — a big debugging time-saver.

## Practice
**Goal:** Rewrite JUnit asserts in AssertJ.
**Steps:**
- [ ] Convert the `Calculator` test assertions from [[M7 - Testing - JUnit 5 Basics]] to AssertJ.
- [ ] Assert on a `List` with `containsExactly` and `extracting`.
- [ ] Assert an exception with `assertThatThrownBy`.

**Record your result:**
- 

## Definition of Done
- [ ] I can write fluent AssertJ assertions.
- [ ] I can assert on collections and exceptions.
- [ ] I prefer AssertJ's messages for debugging failures.

## Cheatsheet (my notes)
- 

## Related
- [[M7 - Testing - JUnit 5 Basics]]
- [[M7 - Testing - Mockito and Test Doubles]]
