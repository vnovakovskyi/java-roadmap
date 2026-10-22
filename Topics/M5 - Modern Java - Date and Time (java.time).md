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
- [ ] Read:
      [dev.java — The Date Time API Overview](https://dev.java/learn/api/date-time-regex/date-time/intro/).
- [ ] Read:
      [dev.java — Period and Duration](https://dev.java/learn/api/date-time-regex/date-time/period-duration/),
      [Parsing and Formatting](https://dev.java/learn/api/date-time-regex/date-time/parsing-formatting/),
      and
      [Time Zone and Offset](https://dev.java/learn/api/date-time-regex/date-time/zoneid-zone-offset/).

## Concepts
- [ ] `LocalDate` (date only), `LocalTime`, `LocalDateTime` (no zone), `Instant` (a point on the UTC
      timeline), `ZonedDateTime` (with a zone).
- [ ] These types are **immutable**; methods like `plusDays` return new instances.
- [ ] `Duration` (time-based: hours, seconds) vs `Period` (date-based: years, months, days);
      `ChronoUnit.DAYS.between(a, b)` for differences.
- [ ] Format/parse with `DateTimeFormatter` — ISO formats by default, or a pattern like
      `"dd.MM.yyyy"` (`MM` = month, `mm` = minutes).
- [ ] Store moments as `Instant`/UTC; convert to a user's time zone only for display. Avoid the
      legacy `java.util.Date`/`Calendar`.

## Practice
**Goal:** Do real date math.
**Steps:**
- [ ] Compute your age in days from your birth date using `LocalDate` and `ChronoUnit`.
- [ ] Format "now" with a custom `DateTimeFormatter`; parse it back.
- [ ] Add 90 days to today and print the result.
- [ ] Show the same `Instant` in two different time zones.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- Which type would you use to record when an order was placed, and why?
> `Instant` (or a UTC timestamp): it's an unambiguous moment, independent of the server's or user's
> time zone.

> [!question]- `Duration` vs `Period`?
> `Duration` measures time-based amounts (hours, minutes, seconds); `Period` measures date-based
> amounts (years, months, days).

> [!question]- `date.plusDays(1);` — why didn't `date` change?
> `java.time` objects are immutable; the method returns a new date. Assign it:
> `date = date.plusDays(1);`.

> [!question]- In a pattern, what's the difference between `MM` and `mm`?
> `MM` is the month; `mm` is minutes — mixing them up is a classic bug.

## Definition of Done
- [ ] I can use the core `java.time` types for dates and times.
- [ ] I can format and parse with `DateTimeFormatter`.
- [ ] I know `Duration` vs `Period` and why to avoid legacy `Date`.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M5 - Modern Java - Files and I-O Basics]]
