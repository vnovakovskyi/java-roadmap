---
title: equals, hashCode and toString
area: OOP
module: 3
status: todo
priority: must
effort: 4
tags:
  - java-roadmap
---

# equals, hashCode and toString

> [!info] Topic
> **Area:** OOP · **Module:** 3 · **Priority:** must · **Est:** 4h
> **Why this matters:** These three `Object` methods control equality, hashing, and debugging output.
> Getting `equals`/`hashCode` wrong silently breaks `HashMap`/`HashSet` — a very common real bug.

## Learning Objectives
- Override `equals`, `hashCode`, and `toString` correctly.
- Explain the equals/hashCode contract.
- Know when to let the IDE/records generate them.

## Learn
- [ ] Read the `Object` Javadoc for `equals`, `hashCode`, `toString`.
- [ ] Read *Effective Java* items on `equals`/`hashCode` (or a Baeldung summary).

## Concepts
- [ ] `==` compares references; `equals` compares **logical equality** (you define what that means).
- [ ] **Contract:** if `a.equals(b)` then `a.hashCode() == b.hashCode()`. Break it and hash-based
      collections misbehave.
- [ ] Override both together, using the same fields.
- [ ] `toString` returns a readable representation — invaluable in logs and the debugger.
- [ ] **Records** (Module 5) auto-generate all three; the IDE can generate them for normal classes.

## Practice
**Goal:** Make value objects behave correctly in collections.
**Steps:**
- [ ] Write a `Point(x, y)` class; override `equals`, `hashCode`, `toString`.
- [ ] Put points in a `HashSet`; add a duplicate `(1,1)` and confirm the set treats them as equal.
- [ ] Break `hashCode` (return a constant or omit it) and observe the breakage; then fix it.

**Record your result:**
- 

## Definition of Done
- [ ] I can correctly override `equals`, `hashCode`, and `toString`.
- [ ] I can state the equals/hashCode contract and why it matters.
- [ ] I know records/IDE can generate these for me.

## Cheatsheet (my notes)
- 

## Related
- [[M4 - Java APIs - Collections Overview (List, Set, Map)]]
- [[M5 - Modern Java - Records]]
