---
title: The Command Line Basics
area: Foundations
module: 1
status: todo
priority: must
effort: 3
tags:
  - java-roadmap
---

# The Command Line Basics

> [!info] Topic
> **Area:** Foundations · **Module:** 1 · **Priority:** must · **Est:** 3h
> **Why this matters:** Real Java work — building, running, Git, Docker — happens in a terminal. You
> don't need to be an expert, but you must be comfortable navigating and running commands.

## Learning Objectives
- Navigate the filesystem (list, change directory, see where you are).
- Create, move, and delete folders and files from the terminal.
- Run a Java program from the terminal and read its output and errors.

## Learn
- [ ] Read (macOS/Linux):
      [The Command Line for Beginners](https://ubuntu.com/tutorials/command-line-for-beginners) —
      written for Ubuntu, works almost unchanged on macOS.
- [ ] Read (Windows):
      [PowerShell 101 — Getting Started](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started).
- [ ] Optional: [MIT Missing Semester — The Shell](https://missing.csail.mit.edu/2020/course-shell/)
      for a deeper intro.

## Concepts
- [ ] The shell has a **current directory**; paths are relative to it unless they are absolute
      (start with `/` or a drive letter).
- [ ] `.` = here, `..` = up one level, `~` = your home directory.
- [ ] Core commands: `pwd`, `ls` (`dir`), `cd`, `mkdir`, `cat` (`type`), `cp`, `mv`, `rm`. `rm` has
      no undo.
- [ ] Commands print output and return an **exit status** (0 = success); errors print to the screen.
- [ ] Tab-completion and the up-arrow (command history) save enormous time.
- [ ] `java Hello.java` compiles and runs a single source file in one step — no IDE needed.

## Practice
**Goal:** Run Java from the terminal — no IDE.
**Steps:**
- [ ] Make a folder `java-practice`, `cd` into it, and create `Hello.java` with any text editor.
- [ ] Run it straight from source: `java Hello.java`.
- [ ] Introduce a typo, run it again, and read the error in the terminal; fix it.
- [ ] Using only the terminal: create a folder, copy a file into it, rename it, list it, and delete
      it.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What's the difference between `cd docs` and `cd /docs`?
> `cd docs` is relative — a `docs` folder inside the current directory. `cd /docs` is absolute — a
> `docs` folder at the filesystem root.

> [!question]- What do `.`, `..`, and `~` mean?
> The current directory, the parent directory, and your home directory.

> [!question]- How can you tell a command failed?
> It prints an error and returns a non-zero exit status (on macOS/Linux, `echo $?` shows the last
> one).

> [!question]- Why be careful with `rm`?
> It deletes immediately — there is no trash bin to restore from.

## Definition of Done
- [ ] I can navigate folders and create, move, and delete files from the terminal.
- [ ] I ran a Java program from the command line without the IDE.
- [ ] I can read a command's error output.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M1 - Foundations - How Java Compiles and Runs]]
