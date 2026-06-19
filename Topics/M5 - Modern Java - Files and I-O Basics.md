---
title: Files and I/O Basics
area: Modern Java
module: 5
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Files and I/O Basics

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** good · **Est:** 3h
> **Why this matters:** Reading and writing files is a constant need — configs, data, logs. The
> modern `java.nio.file` API makes the common cases simple and safe.

## Learning Objectives
- Read and write text files with `Files`/`Path`.
- Stream large files line by line.
- Handle I/O exceptions with try-with-resources.

## Learn
- [ ] Read about `java.nio.file.Files` and `Path` (Javadoc / dev.java).

## Concepts
- [ ] `Path p = Path.of("data.txt");` represents a file path.
- [ ] Small files: `Files.readString(p)` / `Files.writeString(p, text)`;
      lines: `Files.readAllLines` / `Files.write`.
- [ ] Large files: `try (var lines = Files.lines(p)) { ... }` to stream line by line (closeable).
- [ ] I/O throws **checked** `IOException` — handle it (link: [[M4 - Java APIs - Exceptions and Error Handling]]).
- [ ] Combine with the Streams API to process file contents functionally.

## Practice
**Goal:** Process a file end-to-end.
**Steps:**
- [ ] Write a few lines to a file, then read them back and print them.
- [ ] Stream a larger text file with `Files.lines` and count lines containing a keyword.
- [ ] Handle the "file does not exist" case with a clear message.

**Record your result:**
- 

## Definition of Done
- [ ] I can read/write text files with `Files`/`Path`.
- [ ] I can stream a file with try-with-resources.
- [ ] I handle `IOException` properly.

## Cheatsheet (my notes)
- 

## Related
- [[M5 - Modern Java - The Streams API]]
- [[M4 - Java APIs - Exceptions and Error Handling]]
