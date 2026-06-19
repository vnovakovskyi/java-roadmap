---
title: Securing the API with Spring Security
area: Spring
module: 9
status: todo
priority: good
effort: 4
tags:
  - java-roadmap
---

# Securing the API with Spring Security

> [!info] Topic
> **Area:** Spring · **Module:** 9 · **Priority:** good · **Est:** 4h
> **Why this matters:** A real API can't be wide open. A junior is expected to understand
> authentication vs authorization, lock down endpoints, and know where tokens like JWT fit. This is
> the security baseline for the capstone — beginner depth, not a full auth server.

## Learning Objectives
- Explain authentication vs authorization.
- Add Spring Security and protect endpoints.
- Understand where JWT / token auth fits (at an overview level).

## Learn
- [ ] Read the Spring "Securing a Web Application" guide.
- [ ] Read a beginner overview of authentication vs authorization and of JWT.

## Concepts
- [ ] **Authentication** = who you are; **authorization** = what you're allowed to do.
- [ ] Adding `spring-boot-starter-security` secures everything by default — you then configure what's
      public vs protected via a `SecurityFilterChain` bean.
- [ ] Start simple: HTTP Basic or form login with in-memory users and roles; restrict by path/role.
- [ ] Never store plaintext passwords — hash them (e.g. BCrypt via `PasswordEncoder`).
- [ ] **JWT / token auth** (overview): the client sends a signed token per request; the server
      validates it (stateless). Implementing a full JWT flow is beyond junior scope — understand the idea.
- [ ] Keep secrets out of code/config ([[M9 - Spring - Configuration and Profiles]]).

## Practice
**Goal:** Lock down the capstone API.
**Steps:**
- [ ] Add Spring Security; confirm endpoints now require auth.
- [ ] Configure a `SecurityFilterChain`: make `GET /public` open, protect the rest; add an in-memory
      user with a role and a BCrypt-encoded password.
- [ ] Test: anonymous request → 401/redirect; authenticated request → 200. Write down how you'd
      swap to JWT later.

**Record your result:**
- 

## Definition of Done
- [ ] I can explain authentication vs authorization.
- [ ] I can add Spring Security and protect/expose specific endpoints.
- [ ] I can hash passwords and explain where JWT fits.

## Cheatsheet (my notes)
- 

## Related
- [[M9 - Spring - Controllers and REST Endpoints]]
- [[M9 - Spring - Validation and Error Handling]]
- [[M9 - Spring - Configuration and Profiles]]
