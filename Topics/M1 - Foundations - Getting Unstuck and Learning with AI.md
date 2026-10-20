---
title: Getting Unstuck and Learning with AI
area: Foundations
module: 1
status: todo
priority: must
effort: 2
tags:
  - java-roadmap
---

# Getting Unstuck and Learning with AI

> [!info] Topic
> **Area:** Foundations · **Module:** 1 · **Priority:** must · **Est:** 2h
> **Why this matters:** Being stuck is the normal state of programming — what matters is how fast
> you get unstuck. AI assistants can be a superb tutor or a crutch that quietly stops you from
> learning. Set your rules on day one.

## Learning Objectives
- Follow a repeatable routine when you're stuck.
- Ask a good question — to a person or to an AI.
- Use AI assistants to learn faster without outsourcing the learning.

## Learn
- [ ] Read: [How do I ask a good question?](https://stackoverflow.com/help/how-to-ask) (Stack
      Overflow) — the same checklist makes your AI prompts better.
- [ ] Read: [Rubber Duck Debugging](https://rubberduckdebugging.com) — two minutes, surprisingly
      effective.
- [ ] Skim: [How To Ask Questions The Smart Way](http://www.catb.org/~esr/faqs/smart-questions.html)
      — old and blunt, but timeless.

## Concepts
- [ ] The unstuck routine: (1) read the whole error message, (2) reproduce the problem in the
      smallest code you can, (3) explain it out loud line by line (rubber duck), (4) search the
      exact error text, (5) time-box — after ~30 minutes, ask.
- [ ] A good question contains: what you're trying to do, minimal code that reproduces it, the exact
      error or output, and what you already tried.
- [ ] **AI as a tutor, not a solver.** Good uses: explain an error or concept in simpler words, give
      a hint, quiz you, review code *you* wrote, compare two approaches.
- [ ] **The practice rule:** don't ask AI to write the solution to a Practice task in this roadmap.
      If you didn't struggle with it, you didn't learn it. After you've solved it yourself, "how
      could this be better?" is a great prompt.
- [ ] AI is often confidently wrong — especially about versions (it likes Java 8 style, Spring Boot
      2/3, `javax.*`). Check against the official docs linked in each topic, and run the code.
- [ ] Never paste secrets (passwords, API keys, tokens) or private company code into a public AI
      tool.

## Practice
**Goal:** Build your own unstuck routine and AI rules.
**Steps:**
- [ ] Take the bug from [[M1 - Foundations - Reading Errors and Using the Debugger]] (or make a new
      one) and write a "good question" for it: goal, minimal code, exact error, what you tried.
- [ ] Ask an AI assistant to *explain* the error without giving you the fix; fix it yourself.
- [ ] Ask it to quiz you with five questions about Module 1 and answer them without looking anything
      up.
- [ ] Write your personal AI rules (3 bullet points) at the top of this note.

## Self-check
Answer out loud or on paper first, then expand to compare.

> [!question]- What are the four parts of a good question?
> The goal, minimal code that reproduces the problem, the exact error or output, and what you
> already tried.

> [!question]- When does asking AI for code help, and when does it hurt your learning?
> It helps for explanations, hints, reviewing code you wrote, and boilerplate you already
> understand. It hurts when it solves the exercise you were meant to solve — you skip the struggle
> that builds the skill.

> [!question]- An AI answer uses `@MockBean` and `javax.persistence`. What should you suspect?
> Outdated knowledge: those belong to older Spring Boot and JPA versions. Check the current docs
> before using it.

> [!question]- What must you never paste into a public AI chat?
> Secrets (passwords, keys, tokens) and private or company code you're not allowed to share.

## Definition of Done
- [ ] I have a routine for getting unstuck and I use it before asking.
- [ ] I can write a clear question with a minimal example.
- [ ] I wrote down my AI rules: AI explains, hints, and reviews — it doesn't do my practice.
- [ ] I can answer the Self-check questions without peeking.

## Next
- Next: [[M1 - Foundations - Saving Your Work with Git]]
