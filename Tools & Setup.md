---
title: Tools & Setup
tags:
  - java-roadmap/meta
---

# Tools & Setup

Do this **before Module 1**. By the end you'll have Java installed, an editor open, Git working, and
both build tools ready — everything you need to write and run real Java.

> [!info] What you're installing
> 1. A **JDK** (Java 21) — the compiler + runtime. 2. An **IDE** (IntelliJ IDEA). 3. **Git** —
> version control. 4. **Maven** and **Gradle** — build tools (often bundled with the IDE).
> Back to home: [[Java Developer Roadmap - MOC]].

## 1. Install the JDK (Java 21 LTS)

Java 21 is the current Long-Term-Support release — what most jobs target. You want the **JDK**
(Java Development Kit), not just the JRE.

**Recommended: a managed install** so you can switch versions later.

- **macOS / Linux — [SDKMAN!](https://sdkman.io)** (easiest):
  ```bash
  curl -s "https://get.sdkman.io" | bash       # then restart your terminal
  sdk install java 21.0.4-tem                   # Eclipse Temurin 21 (Adoptium)
  sdk default java 21.0.4-tem
  ```
- **macOS — Homebrew** alternative: `brew install temurin@21`
- **Windows** — download the **Temurin 21 (.msi)** installer from
  [adoptium.net](https://adoptium.net), or use `winget install EclipseAdoptium.Temurin.21.JDK`.

**Verify** (this is your first checkpoint):
```bash
java -version     # should say 21.x
javac -version    # should say 21.x
```
If both print a 21 version, the JDK is installed correctly.

> [!tip] JDK vs JRE vs JVM
> The **JVM** runs Java bytecode. The **JRE** = JVM + core libraries (run only). The **JDK** = JRE +
> the compiler (`javac`) and tools (build + run). You install the JDK. Module 1 covers this in depth.

## 2. Install an IDE (IntelliJ IDEA Community)

An IDE gives you autocomplete, instant error highlighting, a debugger, and one-click run.

- Download **[IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/download/)** (free).
- Alternatives: **VS Code** + the *Extension Pack for Java*, or **Eclipse**. This roadmap shows
  IntelliJ, but any of them work.

First-run check: create a new project, make a class with a `main` method that prints `Hello`, and
click the green Run arrow. If you see `Hello` in the console, you're set.

## 3. Install Git

Git tracks your code's history; you'll use it from Module 6 and for everything after.

- **macOS:** `brew install git` (or it ships with the Xcode Command Line Tools).
- **Windows:** download **[Git for Windows](https://git-scm.com/download/win)**.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's package manager.

**Verify and set your identity:**
```bash
git --version
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

Create a free **[GitHub](https://github.com)** account too — you'll push your practice projects there.

## 4. Build tools: Maven and Gradle

Build tools compile your code, manage libraries (dependencies), run tests, and package your app.
This roadmap covers **both** (Module 6) because you'll meet both in the real world. You don't have
to master them now — just have them available.

- **Maven** — XML config (`pom.xml`), the long-time default in enterprise Java.
  - Install: `sdk install maven` · `brew install maven` · or [maven.apache.org](https://maven.apache.org/install.html)
  - Verify: `mvn -version`
- **Gradle** — concise config (`build.gradle`), faster builds, common in newer projects.
  - Install: `sdk install gradle` · `brew install gradle` · or [gradle.org](https://gradle.org/install/)
  - Verify: `gradle -version`

> [!tip] You usually don't install these per project. New projects ship a **wrapper** (`mvnw` /
> `gradlew`) that downloads the right version automatically. Installing them globally is handy for
> starting projects from scratch.

## 5. Optional but useful

- **A terminal you like** — the default is fine; iTerm2 (macOS) / Windows Terminal are nicer.
- **Postman** or **[HTTPie](https://httpie.io)** — for poking REST APIs in Module 9.
- **DBeaver** — a free GUI for databases, handy in Module 8.

## Setup checklist

- [ ] `java -version` and `javac -version` both show 21
- [ ] IntelliJ (or VS Code/Eclipse) installed; ran a Hello World
- [ ] `git --version` works; name + email configured; GitHub account created
- [ ] `mvn -version` works
- [ ] `gradle -version` works

Done? Head back to [[Java Developer Roadmap - MOC]] and start **Module 1**.

## Related
- [[Books & Resources]]
- [[_Conventions]]
