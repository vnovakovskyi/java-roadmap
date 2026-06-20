---
title: var, Enhanced switch and Text Blocks
area: Modern Java
module: 5
status: todo
priority: good
effort: 2
tags:
  - java-roadmap
---

# var, Enhanced switch and Text Blocks

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** good · **Est:** 2h
> **Why this matters:** A handful of modern syntax features make Java code cleaner and are now
> standard in real codebases. Recognizing and using them keeps your code idiomatic.

## Learning Objectives
- Use `var` for local type inference appropriately.
- Use switch expressions and basic pattern matching.
- Use text blocks for multi-line strings.

## Learn
- [ ] Read about local-variable type inference (`var`), switch expressions, and text blocks on dev.java.
- [ ] Skim pattern matching for `instanceof` and `switch` (Java 21).

## Concepts
- [ ] `var x = new ArrayList<String>();` — type inferred; still static, only for locals with a clear
      initializer. Don't overuse where it hurts readability.
- [ ] **Switch expressions**: `var label = switch (day) { case SAT, SUN -> "weekend"; default -> "weekday"; };`
- [ ] **Pattern matching** `instanceof`: `if (o instanceof String s) { use s; }` — no explicit cast.
- [ ] **Text blocks**: `"""..."""` for multi-line strings (JSON, SQL, HTML) without escaping.

## Practice
**Goal:** Modernize older-style code.
**Steps:**
- [ ] Rewrite a verbose local declaration using `var` (and a case where `var` would hurt clarity).
- [ ] Convert an old `switch`+`break` into a switch expression.
- [ ] Build a multi-line JSON string with a text block.

## Definition of Done
- [ ] I use `var` where it improves clarity, not where it hides intent.
- [ ] I can write switch expressions and `instanceof` pattern matching.
- [ ] I can use text blocks for multi-line strings.

## Next
- Next: [[M5 - Modern Java - Date and Time (java.time)]]
