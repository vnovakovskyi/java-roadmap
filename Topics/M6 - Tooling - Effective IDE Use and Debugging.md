---
title: Effective IDE Use and Debugging
area: Tooling
module: 6
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Effective IDE Use and Debugging

> [!info] Topic
> **Area:** Tooling · **Module:** 6 · **Priority:** good · **Est:** 3h
> **Why this matters:** Your IDE can write boilerplate, navigate huge codebases, refactor safely, and
> debug deeply. Fluency here multiplies your speed for the rest of your career.

## Learning Objectives
- Navigate code fast (search, go-to-definition, usages).
- Use refactorings (rename, extract method/variable) safely.
- Use the debugger productively (conditional breakpoints, watches, evaluate).

## Learn
- [ ] Read your IDE's productivity/keymap guide (IntelliJ: "Top productivity tips").
- [ ] Revisit [[M1 - Foundations - Reading Errors and Using the Debugger]] and go deeper.

## Concepts
- [ ] Navigation: search everywhere, go-to-class/symbol, find usages, recent files.
- [ ] **Refactorings** are AST-aware — rename updates all references; extract method/variable, inline,
      change signature.
- [ ] Code generation: constructors, getters/setters, `equals`/`hashCode`, `toString`, overrides.
- [ ] Debugger power tools: **conditional breakpoints**, watches, "evaluate expression", step
      filters, drop-frame.
- [ ] Live templates/snippets and inspections/quick-fixes cut repetitive work.

## Practice
**Goal:** Solve a task using IDE tools, not manual editing.
**Steps:**
- [ ] Use "extract method" and "rename" to refactor a messy class; confirm nothing breaks.
- [ ] Generate `equals`/`hashCode`/`toString` for a class.
- [ ] Set a **conditional** breakpoint (e.g. only when `i == 50`) and inspect state there.

**Record your result:**
- 

## Definition of Done
- [ ] I can navigate and refactor with keyboard shortcuts.
- [ ] I can generate boilerplate via the IDE.
- [ ] I can use conditional breakpoints and evaluate expressions.

## Cheatsheet (my notes)
- 

## Related
- [[M1 - Foundations - Reading Errors and Using the Debugger]]
- [[Tools & Setup]]
