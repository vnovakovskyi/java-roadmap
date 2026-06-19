# Plan

## 1. Goal

Produce a complete, fork-and-go **Obsidian vault** in the `java-roadmap` repo that takes a complete
beginner to a **job-ready junior Java developer**. Anyone can clone/download the repo, open it in
Obsidian, and work through a structured, progress-tracked path covering the knowledge, tools, and
books needed. The repo also ships a **visual map** of the path (an SVG mind-map that renders on
GitHub, plus an interactive Obsidian canvas).

It reuses the proven structure of the owner's "Java tech lead" vault (home MOC + conventions +
per-topic notes + dashboard + visual canvas), re-pitched for beginners.

## 2. Background

From `docs/00-research.md`: the source vault is a clean, reusable study system —
`MOC` + `_Conventions` + `_Template - Topic` + `Topics/M{n} - {Domain} - {Topic}.md` +
`Dashboard.base` (Obsidian Bases) + `Roadmap.canvas`. Topic notes are hands-on and outcome-driven
(Objectives → Learn → Internals → Exercise → Definition of Done + Cheatsheet + Related), with
controlled frontmatter that drives the dashboard.

Confirmed scope decisions:
- **Ceiling:** job-ready junior (build a small Spring Boot CRUD app, use Git, write tests, query a DB).
- **Build tools:** Maven **and** Gradle, both covered.
- **Visual:** committed **SVG** mind-map **and** an Obsidian **`.canvas`**.

Styling decision (this request): **keep emoji minimal** — a few in the MOC/landing for warmth, but
topic-note section headers stay plain text. This intentionally differs from the emoji-heavy source.

## 3. Scope

### In Scope

- A full Obsidian vault at the repo root:
  - `README.md` — GitHub landing page: what it is, how to use as an Obsidian vault, embedded roadmap image.
  - `Java Developer Roadmap - MOC.md` — home note: intro, how-to, embedded dashboard, full Module Index.
  - `_Conventions.md` — workflow + frontmatter contract + the topic-note loop + file naming.
  - `_Template - Topic.md` — blank topic skeleton.
  - `Weekly Log.md` — momentum log.
  - `Dashboard.base` — Bases dashboard (By Module / By Area / In Progress / Next Up / Done).
  - `Books & Resources.md` — tiered, mostly-free resource list + recommended books.
  - `Tools & Setup.md` — JDK, IDE, Git, build-tool install/setup for absolute beginners.
  - `Topics/` — ~60 topic notes across 10 modules (curriculum below).
  - `Roadmap.canvas` — interactive visual, modules left→right.
  - `assets/roadmap.svg` — static visual mind-map (also referenced by README; optional PNG export).
  - `.gitignore` — ignore Obsidian workspace state and IDE cruft.
- A from-scratch → junior **curriculum** (10 modules; topic list fixed in this plan).
- Beginner-tailored frontmatter vocabulary and a graceful Markdown fallback when Bases is absent.

### Out of Scope

- Interview prep, resume coaching, LeetCode/DSA grinding, behavioral prep.
- Intermediate/senior deep-dives beyond junior readiness (GC tuning, K8s, distributed systems,
  observability stacks, advanced concurrency, reactive). These may appear as "optional / later"
  pointers only.
- Runnable Java sample projects committed to the repo (exercises are described in notes; learners
  build their own). A separate companion code repo is not part of this work.
- Auto-generated dashboards beyond what Obsidian Bases provides.
- Translations/localization.
- Publishing/marketing the repo (GitHub Pages, etc.).

## 4. Success Criteria

- **Product:** a beginner can open the vault in Obsidian, land on the MOC, understand the path from
  the visual map, pick a topic, and work it top-to-bottom with a clear Definition of Done.
- **Technical:** every topic note has valid, consistent frontmatter (controlled values) and is picked
  up by the Bases dashboard; every `[[wikilink]]` and `Related` link resolves to a real note; the
  `.canvas` references correct vault-relative paths.
- **GitHub-facing:** `README.md` renders cleanly and shows the roadmap **SVG**; the Module Index in
  the MOC works as a no-plugin fallback.
- **Quality:** consistent file naming `M{module} - {Area} - {Topic}.md`; the curriculum has no
  obvious gaps for a junior role; emoji usage is restrained.
- **Operational:** repo can be zipped/cloned and used as a vault with zero extra setup beyond
  installing Obsidian (Bases is core in current Obsidian; a fallback exists if unavailable).

## 5. User Stories / Use Cases

- **As a complete beginner**, I download the repo, open it as an Obsidian vault, read the MOC, look
  at the roadmap image, and start at Module 1 without prior programming knowledge.
- **As a learner mid-path**, I open the Dashboard, see "In Progress" and "Next Up", open a topic, do
  the Learn + Practice sections, tick the Definition of Done, and set `status: done`.
- **As a learner on mobile / without Bases**, the MOC Module Index still lets me navigate everything.
- **As someone choosing tools**, I open `Tools & Setup` to install the JDK, an IDE, Git, and try both
  Maven and Gradle.
- **As a browser on GitHub**, I read the README and immediately see the visual path before deciding
  to clone.
- **As the maintainer**, I copy `_Template - Topic.md`, fill the frontmatter per `_Conventions`, and
  the note appears in the dashboard automatically.

## 6. Functional Requirements

1. The vault MUST open in Obsidian with the repo root as the vault folder.
2. The MOC MUST contain: a short intro, a "start here" workflow, an embedded `Dashboard.base`, an
   embedded/linked roadmap visual, and a complete Module Index of all topic notes (fallback nav).
3. `_Conventions.md` MUST define the exact frontmatter vocabulary, allowed values, file-naming rule,
   the topic-note loop, and the daily/weekly workflow.
4. `_Template - Topic.md` MUST match the documented topic skeleton and frontmatter.
5. Each topic note MUST include frontmatter: `title`, `area`, `module`, `status`, `priority`,
   `effort`, `tags` (including `java-roadmap`), and the standard sections.
6. `Dashboard.base` MUST filter on `tag == java-roadmap` and provide views: By Module, By Area,
   In Progress, Next Up, Done.
7. `Roadmap.canvas` MUST lay out modules left→right (or top→down) with file-card links resolving to
   `Topics/…` paths relative to the vault root.
8. `assets/roadmap.svg` MUST visually represent the 10 modules and key topics/tools/books with a
   legend (must-know / good-to-know / optional), and MUST be referenced by the README.
9. `README.md` MUST explain how to use the repo as an Obsidian vault and embed the SVG.
10. `Books & Resources.md` MUST list resources tiered by priority and note which are free.
11. `Tools & Setup.md` MUST give step-by-step setup for JDK 21, an IDE, Git, Maven, and Gradle.
12. The curriculum MUST cover the 10 modules and topics specified in Phase plan below.
13. All internal links MUST resolve (no broken `[[wikilinks]]`).

## 7. Non-Functional Requirements

- **Maintainability:** controlled frontmatter values documented in one place; consistent naming;
  adding a topic = copy template + fill frontmatter.
- **Portability:** pure Markdown + Obsidian-native `.canvas`/`.base`; works on desktop and mobile;
  degrades to Module Index without Bases.
- **Accuracy / freshness:** target **Java 21 (LTS)**; prefer official/canonical and free resources;
  flag version-sensitive items inline; avoid pinning fragile book editions where avoidable.
- **Approachability:** beginner-readable language; restrained emoji; each topic small enough to
  finish in a sitting (effort estimates ~2–6h).
- **GitHub rendering:** README + SVG render without plugins; no reliance on `.canvas` for GitHub.
- **Cost:** zero — all tooling free/open; resources favor free-first.

## 8. Dependencies

- **Obsidian** (reader side) with core plugins; **Bases** for the dashboard (core in current
  Obsidian). Fallback: Module Index in the MOC.
- **Git / GitHub** for distribution (repo already initialized; MIT LICENSE present).
- No build/test toolchain in this repo (it is a content vault). Validation is via lightweight
  shell/grep checks and manual Obsidian inspection.
- External references (official Java docs, Spring guides, recommended books) — linked, not vendored.

## 9. Risks and Mitigations

- **Volume (~60 notes) → incomplete or shallow** → impact: weak product → mitigation: topic list is
  fixed in this plan; notes written in module-batched phases; each note follows the same compact loop.
- **`.canvas` paths wrong → broken cards** → impact: visual nav breaks → mitigation: generate card
  `file` paths as `Topics/<exact filename>.md` and verify against the real file list in a phase check.
- **Broken `[[wikilinks]]` / `Related`** → impact: dead links in Obsidian → mitigation: automated
  grep check that every link target exists among the topic filenames.
- **Bases unavailable on a device** → impact: no dashboard → mitigation: Module Index fallback,
  documented in `_Conventions` and MOC.
- **SVG won't render or looks cluttered** → impact: poor first impression → mitigation: keep the SVG
  structured (module columns + legend), test rendering on GitHub before finalizing.
- **Curriculum opinion (over/under-scope)** → impact: demotivating → mitigation: tier topics
  (must / good / optional) so the critical path is obvious; keep advanced topics as optional pointers.
- **Frontmatter drift breaks dashboard** → impact: missing rows → mitigation: single documented
  vocabulary + an automated frontmatter-key check across `Topics/`.

## Proposed curriculum (10 modules)

Areas (controlled): `Foundations`, `Core Java`, `OOP`, `Java APIs`, `Modern Java`, `Tooling`,
`Testing`, `Databases`, `Spring`, `Project`.

- **M1 — Foundations & Setup** (area: Foundations): How programming works & how Java runs (JVM/JDK/JRE);
  Install JDK 21 & an IDE; The command line basics; Your first Java program; How Java compiles & runs
  (javac/java); Reading errors & using the debugger.
- **M2 — Core Java: Syntax & Control Flow** (Core Java): Variables, primitives & types; Operators &
  expressions; Strings & basic I/O; Conditionals (if/switch); Loops (for/while); Methods & parameters;
  Arrays.
- **M3 — Object-Oriented Programming** (OOP): Classes & objects; Fields, methods & constructors;
  Encapsulation & access modifiers; Inheritance; Polymorphism & overriding; Abstraction, interfaces &
  abstract classes; `equals`, `hashCode` & `toString`.
- **M4 — Essential Java APIs** (Java APIs): Collections overview (List/Set/Map); Generics basics;
  Iteration & sorting (Comparable/Comparator); Exceptions & error handling; Enums; `Optional` &
  null-safety; Packages & project organization.
- **M5 — Modern Java** (Modern Java): Lambdas & functional interfaces; The Streams API; Records;
  `var`, enhanced switch & text blocks; Date & time (`java.time`); Files & I/O basics.
- **M6 — Tooling & Workflow** (Tooling): Git fundamentals; GitHub & pull requests; Maven (project,
  dependencies, lifecycle); Gradle (project, dependencies, tasks); Dependency management & semantic
  versioning; Effective IDE use & debugging.
- **M7 — Testing** (Testing): Why we test & the test pyramid; JUnit 5 basics; Assertions with AssertJ;
  Mockito & test doubles; Writing testable code (intro TDD).
- **M8 — Databases & SQL** (Databases): Relational concepts; SQL CRUD & queries; Joins & aggregation;
  Connecting from Java (JDBC); ORM intro (JPA/Hibernate); Schema basics & migrations (Flyway).
- **M9 — Web Development with Spring Boot** (Spring): HTTP & REST fundamentals; Spring Boot intro &
  project setup; Controllers & REST endpoints; Services & dependency injection; Spring Data JPA &
  repositories; Validation & error handling; Configuration & profiles.
- **M10 — Putting It Together: Capstone** (Project): Designing a small CRUD app; Building the REST API
  end-to-end; Persisting with a real database; Testing the application; Good habits (logging, config,
  README); Packaging & running (jar/Docker basics, optional).

Approx. 6 topics × 10 modules ≈ 60 notes. `priority` tiers each as `must` / `good` / `optional`.
A soft pacing target of **~6 months at ~10–12 h/week** is stated in the MOC, with per-topic `effort`.

## 10. Implementation Phases

> No app build/test toolchain exists (content vault). "Automated" checks are lightweight shell
> validations run from the repo root. Manual checks are done in Obsidian / on GitHub.

### Phase 1: Vault scaffolding & conventions

**Goal:** Stand up the skeleton: home note, conventions, template, weekly log, gitignore.

**Files/modules likely affected:** `README.md` (initial), `Java Developer Roadmap - MOC.md`,
`_Conventions.md`, `_Template - Topic.md`, `Weekly Log.md`, `.gitignore`.

**Changes:** Create the home MOC (intro, workflow, dashboard/visual placeholders, empty Module Index
to be filled later), the conventions doc (frontmatter contract + naming + topic loop), the topic
template, a weekly log, and a `.gitignore` (ignore `.obsidian/workspace*`, `.idea/`, `.DS_Store`).

**Success criteria — Automated:**
- [x] `ls` shows all five vault files + `.gitignore` at repo root.
- [x] `grep -l "java-roadmap" _Conventions.md _Template\ -\ Topic.md` finds the tag contract.
- [x] `_Template - Topic.md` contains every frontmatter key listed in FR-5.

**Success criteria — Manual:**
- [ ] Opening the repo as an Obsidian vault shows the MOC as a readable home note.
- [ ] Conventions read clearly to a beginner; no leftover tech-lead framing.

> Pause for user confirmation before Phase 2.

### Phase 2: Resource notes (Books & Tools)

**Goal:** Beginner can set up their environment and knows what to read.

**Files/modules likely affected:** `Tools & Setup.md`, `Books & Resources.md`.

**Changes:** Step-by-step setup (JDK 21, IDE, Git, Maven, Gradle, verify install) and a tiered,
free-first resource list with recommended books.

**Success criteria — Automated:**
- [ ] Both files exist and link back to the MOC (`grep` finds `[[Java Developer Roadmap - MOC]]`).

**Success criteria — Manual:**
- [ ] Setup steps are followable on macOS by a beginner; commands are correct for JDK 21.
- [ ] Resource tiers (must/good/optional) and free vs. paid are clear.

> Pause for user confirmation before Phase 3.

### Phase 3: Topic notes — Modules 1–3 (Foundations, Core Java, OOP)

**Goal:** Write all topic notes for the first three modules.

**Files/modules likely affected:** `Topics/M1 - Foundations - *.md`, `Topics/M2 - Core Java - *.md`,
`Topics/M3 - OOP - *.md`.

**Changes:** One note per topic following the template (Objectives → Learn → Concepts → Practice →
Definition of Done → Cheatsheet → Related), with valid frontmatter.

**Success criteria — Automated:**
- [ ] Every new file matches naming `M{1..3} - {Area} - {Topic}.md`.
- [ ] `grep -L "tags:" Topics/M[123]*` returns nothing (all have frontmatter).
- [ ] A frontmatter-key check confirms `title/area/module/status/priority/effort/tags` in each.

**Success criteria — Manual:**
- [ ] Notes are beginner-appropriate and self-contained; exercises are doable.
- [ ] `Related` links point to real notes (or notes planned in later phases).

> Pause for user confirmation before Phase 4.

### Phase 4: Topic notes — Modules 4–5 (Java APIs, Modern Java)

**Goal:** Write all topic notes for modules 4–5.

**Files/modules likely affected:** `Topics/M4 - Java APIs - *.md`, `Topics/M5 - Modern Java - *.md`.

**Changes:** As Phase 3, for these modules.

**Success criteria — Automated:**
- [ ] Naming + frontmatter checks pass for `Topics/M[45]*`.

**Success criteria — Manual:**
- [ ] Streams/lambdas/records explained at beginner depth; exercises runnable.

> Pause for user confirmation before Phase 5.

### Phase 5: Topic notes — Modules 6–7 (Tooling, Testing)

**Goal:** Write all topic notes for modules 6–7, including both Maven and Gradle.

**Files/modules likely affected:** `Topics/M6 - Tooling - *.md`, `Topics/M7 - Testing - *.md`.

**Changes:** As before; ensure Maven and Gradle each get a dedicated, comparable note.

**Success criteria — Automated:**
- [ ] Naming + frontmatter checks pass for `Topics/M[67]*`.
- [ ] Both a Maven and a Gradle note exist.

**Success criteria — Manual:**
- [ ] Git, Maven, Gradle, JUnit notes are accurate and beginner-followable.

> Pause for user confirmation before Phase 6.

### Phase 6: Topic notes — Modules 8–10 (Databases, Spring, Capstone)

**Goal:** Write all topic notes for modules 8–10.

**Files/modules likely affected:** `Topics/M8 - Databases - *.md`, `Topics/M9 - Spring - *.md`,
`Topics/M10 - Project - *.md`.

**Changes:** As before; the capstone notes tie earlier modules into one CRUD app.

**Success criteria — Automated:**
- [ ] Naming + frontmatter checks pass for `Topics/M(8|9|10)*`.

**Success criteria — Manual:**
- [ ] Spring Boot CRUD path is coherent end-to-end; capstone references prior modules.

> Pause for user confirmation before Phase 7.

### Phase 7: Dashboard + MOC Module Index wiring

**Goal:** Make the dashboard live and the MOC fully navigable.

**Files/modules likely affected:** `Dashboard.base`, `Java Developer Roadmap - MOC.md`.

**Changes:** Author `Dashboard.base` (views: By Module, By Area, In Progress, Next Up, Done) filtered
on the `java-roadmap` tag; populate the MOC Module Index with `[[wikilinks]]` to every topic.

**Success criteria — Automated:**
- [ ] Every `Topics/*.md` filename appears exactly once in the MOC Module Index (link-coverage check).
- [ ] No `[[link]]` in the MOC lacks a matching file.

**Success criteria — Manual:**
- [ ] In Obsidian, the embedded Dashboard renders and lists notes; views filter correctly.
- [ ] Module Index works as a fallback with Bases disabled.

> Pause for user confirmation before Phase 8.

### Phase 8: Visual map (SVG + Canvas)

**Goal:** Ship the "picture of the path".

**Files/modules likely affected:** `assets/roadmap.svg` (and optional `roadmap.png`),
`Roadmap.canvas`, `README.md` (embed image), MOC (link/embed visual).

**Changes:** Create a structured SVG mind-map (10 module columns/branches, key topics/tools/books, a
legend must/good/optional) and an Obsidian `Roadmap.canvas` with module groups and file-cards using
`Topics/…` paths. Embed the SVG in README and link it from the MOC.

**Success criteria — Automated:**
- [ ] `Roadmap.canvas` is valid JSON; every `file` path resolves to an existing `Topics/*.md`.
- [ ] `README.md` references `assets/roadmap.svg`.

**Success criteria — Manual:**
- [ ] SVG renders on GitHub and reads clearly (modules + legend legible).
- [ ] Canvas opens in Obsidian; cards link to the right notes left→right.

> Pause for user confirmation before Phase 9.

### Phase 9: Final wiring, README polish & verification

**Goal:** Tie everything together and verify the whole vault.

**Files/modules likely affected:** `README.md`, MOC, any link fixes across `Topics/`.

**Changes:** Finalize README (intro, how-to-use-as-vault, image, structure, contributing/LICENSE
note); run the full link/frontmatter validation; fix any broken links.

**Success criteria — Automated:**
- [ ] Repo-wide link check: zero unresolved `[[wikilinks]]`.
- [ ] Repo-wide frontmatter check: all `Topics/*.md` carry the full key set + `java-roadmap` tag.

**Success criteria — Manual:**
- [ ] Fresh clone opens cleanly as an Obsidian vault; MOC → visual → first topic flow works.
- [ ] README renders correctly on GitHub with the roadmap image.
- [ ] (Optional) initial git commit made when the user asks.

> Pause for user confirmation. Done.

## 11. Testing Strategy

- **Structural validation (automated, shell):** frontmatter-key presence + controlled values across
  `Topics/`; file-naming pattern; `[[wikilink]]` resolution; `Roadmap.canvas` JSON validity and path
  resolution; README references the SVG.
- **Rendering (manual):** open the vault in Obsidian (desktop) — MOC, embedded Bases dashboard,
  canvas, and a few topic notes; confirm the SVG renders on GitHub.
- **Beginner-usability (manual):** sanity-read Module 1 + Tools & Setup as if brand new; confirm a
  learner could actually start.
- **Optional linters:** if available, run `markdownlint`/`remark` for consistency (not required).

## 12. Rollout / Migration Strategy

Not a deployed system. "Rollout" = committing to the `java-roadmap` repo (only when the user asks)
and the repo being clone/download-ready as a vault. No data migration. If git operations are
requested, branch first per repo conventions.

## 13. Documentation Updates

The deliverable *is* documentation. Within the repo:
- `README.md` (GitHub-facing usage + visual).
- `_Conventions.md` (the system's own how-to).
- `docs/00-research.md` (exists) and `docs/01-plan.md` (this file) remain as process records.
- Keep `docs/` separate from vault content so it doesn't clutter the learner experience.

## 14. Open Questions

All blocking questions are resolved. Non-blocking defaults adopted (override anytime):
- **Pacing:** state a soft "~6 months @ ~10–12 h/week" in the MOC + per-topic `effort`. *(default)*
- **Books:** recommend a tiered list (e.g. *Head First Java* for absolute beginners; *Effective Java*
  as a level-up; official Spring guides) in `Books & Resources.md`. *(default)*
- **Module/topic count:** ~60 notes across 10 modules as listed. *(default — can trim/extend)*
- **Emoji:** minimal, per this request. *(default)*
