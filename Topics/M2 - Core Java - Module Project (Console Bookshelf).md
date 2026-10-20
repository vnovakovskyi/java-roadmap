---
title: Module Project (Console Bookshelf)
area: Core Java
module: 2
status: todo
priority: must
effort: 5
tags:
  - java-roadmap
---

# Module Project (Console Bookshelf)

> [!info] Topic
> **Area:** Core Java · **Module:** 2 · **Priority:** must · **Est:** 5h
> **Why this matters:** Exercises teach pieces; projects teach how the pieces fit. This is version 1
> of **Bookshelf**, a small app you'll grow through the roadmap — classes in Module 3, collections
> in 4, streams and files in 5, a real build in 6, tests in 7, and a database in 8.

> [!tip] About the Bookshelf project
> Keep it in its own GitHub repository (`bookshelf`). Every module ends with a new version — tag
> each one (`git tag v1`, then `git push --tags`) so you can see how it grew. There's no reference
> solution on purpose: if it works and you can explain it, it's right.

## Learning Objectives
- Combine variables, strings, input, conditionals, loops, methods, and arrays in one program.
- Structure a program as small, well-named methods.
- Handle invalid input without crashing.

## Learn
- [ ] Revisit [[M2 - Core Java - Methods and Parameters]] and [[M2 - Core Java - Arrays]].
- [ ] Skim the "Practice" sections of this module — every piece you need is there.

## Concepts
- [ ] A **menu loop**: show options, read a choice, act on it, repeat until the user quits.
- [ ] One method per action: `addBook`, `listBooks`, `searchByTitle`, `markAsRead`.
- [ ] Data in parallel arrays — `String[] titles`, `String[] authors`, `boolean[] read` — plus an
      `int count`, with a fixed capacity (e.g. 100). It will feel clumsy; that's the point. Classes
      and collections fix it later.
- [ ] Validate input: empty titles, unknown menu options, an out-of-range book number, a full shelf.

```text
=== Bookshelf ===
1) Add  2) List  3) Search  4) Mark as read  0) Quit
> 1
Title: Clean Code
Author: Robert C. Martin
Added (1/100).
```

## Practice
**Goal:** A working console app that manages a reading list.
**Steps:**
- [ ] Create a `bookshelf` repository with a `Bookshelf.java` (compact source file or classic
      class).
- [ ] Implement the menu loop and `0) Quit`.
- [ ] Implement add, list (numbered, with a ✓ for books you've read), and case-insensitive search by
      title.
- [ ] Implement mark-as-read by number; reject invalid numbers with a friendly message.
- [ ] Extra: show "X of Y read" and the number of books per author.
- [ ] Commit as you go, push, and tag the result `v1`.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Why split the program into methods instead of writing one long `main`?
> Each method has one job and a name that says what it does, so the code is easier to read, test,
> and change — and `main` reads like a table of contents.

> [!question]- What happens when the shelf is full, and how does your program handle it?
> The arrays have a fixed size, so adding past capacity would throw
> `ArrayIndexOutOfBoundsException`; the program must check `count` first and tell the user.

> [!question]- Which part of this design is the most painful, and what will fix it?
> The parallel arrays and the fixed capacity. Classes (Module 3) bundle a book's data into one
> object, and collections (Module 4) grow automatically.

## Definition of Done
- [ ] The app runs from the terminal and survives bad input.
- [ ] Each menu action lives in its own small method.
- [ ] The code is on GitHub, tagged `v1`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M3 - OOP - Classes and Objects]]
