---
title: Date and Time (java.time)
area: Modern Java
module: 5
status: todo
priority: good
effort: 3
tags:
  - java-roadmap
---

# Date and Time (java.time)

> [!info] Topic
> **Area:** Modern Java · **Module:** 5 · **Priority:** good · **Est:** 3h
> **Why this matters:** Almost every app deals with dates, timestamps, and durations. The modern
> `java.time` API is clear and safe — and avoids the legacy `Date`/`Calendar` traps.

## Learning Objectives
- Use `LocalDate`, `LocalDateTime`, `Instant`, `Duration`, `Period`.
- Format and parse dates with `DateTimeFormatter`.
- Handle time zones at a basic level.

## Learn
- [ ] Read: [dev.java — "Date and Time"](https://dev.java/learn/) and the `java.time` Javadoc.

## Concepts
- [ ] `LocalDate` (date only), `LocalTime`, `LocalDateTime` (no zone), `Instant` (a point on the UTC
      timeline), `ZonedDateTime` (zoned).
- [ ] These types are **immutable**; methods like `plusDays` return new instances.
- [ ] `Duration` (time-based) vs `Period` (date-based) for amounts of time.
- [ ] Format/parse with `DateTimeFormatter` (e.g. ISO, or a custom pattern).
- [ ] Prefer `java.time` over the legacy `java.util.Date`/`Calendar`.

## Practice
**Goal:** Do real date math.
**Steps:**
- [ ] Compute your age in days from your birth date using `LocalDate` + `Period`/`ChronoUnit`.
- [ ] Format "now" with a custom `DateTimeFormatter`; parse it back.
- [ ] Add 90 days to today and print the result.

**Record your result:**
- 

## Definition of Done
- [ ] I can use the core `java.time` types for dates/times.
- [ ] I can format and parse with `DateTimeFormatter`.
- [ ] I know `Duration` vs `Period` and why to avoid legacy `Date`.

## Cheatsheet (my notes)
- 

## Related
- [[M2 - Core Java - Strings and Basic Input-Output]]
- [[M5 - Modern Java - Records]]
