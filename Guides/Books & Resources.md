---
title: Books & Resources
tags:
  - java-roadmap/meta
---

# Books & Resources

A curated, **free-first** list. You do **not** need to read all of this — each topic note links the
specific resource you need at that moment. This page is the big-picture reference.

> [!info] How to use this
> Pick **one** primary book or course to follow alongside the path, lean on the free official docs
> for detail, and use videos when a concept won't click from text. Tiers: **must** = core,
> **good** = recommended, **optional** = when you want more. Back to home: [[Home]].

> [!warning] Check the version
> Many books, articles, and videos target older versions (Java 8–17, Spring Boot 2–3). The ideas
> mostly hold; the details often don't. This vault targets **Java 25** and **Spring Boot 4** — see
> *Stack assumptions* in [[_Conventions]].

## Books

### For the absolute beginner (pick one as your main companion)
- **Head First Java, 3rd ed.** — Sierra, Bates & Gee (covers Java 17). *(must)* The friendliest
  on-ramp; visual, hands-on, assumes nothing. The best companion for Modules 1–5.
- **Java: A Beginner's Guide** — Herbert Schildt (latest edition). *(optional)* A more traditional,
  thorough alternative if Head First's style isn't for you.

### Level-up (read after you can write basic classes)
- **Effective Java, 3rd ed.** — Joshua Bloch. *(good)* The book that teaches you to write *good*
  Java. Older than modern features, but its advice still holds — revisit items as you finish
  Modules 3–5 and 7.
- **Modern Java in Action** — Urma, Fusco & Mycroft. *(good)* The deep treatment of lambdas and
  streams (pairs with Module 5).
- **Grokking Algorithms, 2nd ed.** — Aditya Bhargava. *(good)* An illustrated, gentle intro to
  algorithms and data structures — ideal before coding interviews (Module 11).
- **The Pragmatic Programmer, 20th anniversary ed.** — Thomas & Hunt. *(optional)* Habits and
  judgment of a professional developer.

### Spring and data
- **Spring Start Here, 2nd ed.** — Laurențiu Spilcă. *(good)* The gentlest Spring intro, updated for
  Spring Boot 4 / Spring Framework 7 (in Manning early access; the 1st ed. targets Spring Boot 2).
- **Spring in Action, 6th ed.** — Craig Walls. *(optional)* Thorough, but written for Spring Boot 2 —
  the concepts hold, many code details have changed.
- **High-Performance Java Persistence** — Vlad Mihalcea. *(optional, later)* JPA/Hibernate and SQL
  performance in depth.

### Reference / later
- **Java Concurrency in Practice** — Goetz et al. *(optional)* The classic on threads; beyond junior
  scope and older than virtual threads, but still the reference on thread-safety.

## Free official documentation (your default detail source)
- **[Dev.java](https://dev.java/learn/)** — Oracle's official, modern Java tutorials. *(must)*
- **[Java 25 API docs (Javadoc)](https://docs.oracle.com/en/java/javase/25/docs/api/)** — look up any
  class or method. *(must — learn to read these early)*
- **[Java Language Updates (Java 25)](https://docs.oracle.com/en/java/javase/25/language/index.html)** —
  records, pattern matching, sealed classes, compact source files, and more. *(good)*
- **[The Java Tutorials](https://docs.oracle.com/javase/tutorial/)** — older (Java 8) but comprehensive
  on fundamentals like concurrency and JDBC. *(good)*
- **[Spring Boot reference](https://docs.spring.io/spring-boot/)** and **[Spring Guides](https://spring.io/guides)** —
  the official docs and short how-tos. *(must for M9–M10)*
- **[Baeldung](https://www.baeldung.com)** — a huge library of practical Java/Spring articles. Check
  which Spring Boot version an article uses. *(good)*

## Free courses & video
- **[University of Helsinki — Java Programming MOOC](https://java-programming.mooc.fi)** *(must-try)* —
  free, complete, exercise-driven; an excellent structured companion for Modules 1–5.
- **[Java (official YouTube channel)](https://www.youtube.com/@java)** *(good)* — news and deep dives
  from the Java team at Oracle.
- **[Dan Vega](https://www.youtube.com/@danvega)** *(good)* — clear, current Spring Boot videos.
- **[Spring Developer](https://www.youtube.com/@SpringSourceDev)** *(good)* — the official Spring channel.
- **[Amigoscode](https://www.youtube.com/@amigoscode)** and **[Java Brains](https://www.youtube.com/@Java.Brains)**
  *(good)* — beginner-friendly Java and Spring explainers (some videos target older versions).

## Practice & community
- **[Exercism — Java track](https://exercism.org/tracks/java)** *(must)* — guided exercises with
  mentor feedback. Great for Modules 2–5.
- **[CodingBat — Java](https://codingbat.com/java)** *(good)* — tiny problems to drill syntax and recursion.
- **[NeetCode Roadmap](https://neetcode.io/roadmap)** *(good)* — structured algorithm practice for Module 11.
- **[Advent of Code](https://adventofcode.com/)** *(optional)* — fun yearly puzzles; great Java practice.
- **[r/learnjava](https://www.reddit.com/r/learnjava/)** and its wiki *(good)* — ask questions, read the FAQ.
- **[Stack Overflow](https://stackoverflow.com)** — search first; you'll live here.
- **[Java User Groups](https://dev.java/community/jugs/)** *(good)* — local meetups; the best place to
  meet developers (and hear about jobs).

## Tooling references
- **[SDKMAN!](https://sdkman.io)**, **[Adoptium/Temurin](https://adoptium.net)** — installing Java.
- **[Maven](https://maven.apache.org/guides/)** and **[Gradle](https://docs.gradle.org)** user guides.
- **[Pro Git book](https://git-scm.com/book/en/v2)** *(good, free)* — the definitive Git reference.
- **[Docker docs](https://docs.docker.com/get-started/)** — containers and Compose.

## Related
- [[Tools & Setup]]
- [[_Conventions]]
