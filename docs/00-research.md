# Research

## 1. Request

Build a **"Java Developer from Scratch" roadmap** and store it in the freshly-created, empty
repo `java-roadmap` (`/Users/vnovakovskyi/PrivateDevelopment/java-roadmap`).

Requirements expressed by the user:

- The repo should be usable **as an Obsidian vault**: someone can clone/download it, open it in
  Obsidian, and learn Java by working through it.
- It should be **inspired by the structure** of the user's existing "Java tech lead" vault — a main
  document (MOC) with intro + plan, then per-topic notes that track progress.
- Target audience is the **absolute beginner** ("from scratch") who wants to become a **good Java
  software developer** — not the senior→tech-lead audience of the source vault.
- Include a **visual picture of the path** (knowledge, tools, books) similar to the shared
  `s4kibs4mi/java-developer-roadmap` mind-map image. The image is inspiration only — it does not
  need to be replicated exactly.
- Cover "everything actually needed": knowledge, tools, and books.

## 2. Context

### The source vault (inspiration)

Located at `…/Santa_notes/Personal/Java tech lead/`. It is a polished, opinionated Obsidian study
system. Its anatomy:

| File / folder | Role |
| --- | --- |
| `Java Tech Lead — MOC.md` | Map-of-Content "home" note: intro callout, quick links, embedded live dashboard, and a Month Index (fallback navigation). Entry point for every session. |
| `_Conventions.md` | Single source of truth for how the system works: daily/weekly workflow, frontmatter property vocabulary, the "depth dial", the 5-part topic loop, file-naming rules. |
| `_Template - Topic.md` | Blank topic skeleton with frontmatter + the 5 standard sections. |
| `Weekly Log.md` | One short entry per week for momentum/reflection. |
| `Dashboard.base` | Obsidian **Bases** file: tables filtered by `status` (By Month, By Domain, In Progress, Next Up, Done). |
| `Roadmap.canvas` | Obsidian **Canvas**: 6 vertical month groups, each containing the topic file-cards, laid out left→right. The native "visual roadmap". |
| `Topics/` | 60 topic notes named `M{month} - {Domain} - {Topic}.md`. |

**Frontmatter vocabulary** (controlled values, drive the Bases dashboard):
`title`, `domain`, `month` (1–6), `week` (1–4), `status` (`todo`/`doing`/`done`),
`priority` (`must`/`stretch`), `depth` (`core`/`deep`), `effort` (hours), `tags`
(must include `java-tech-lead`).

**Topic note skeleton (the "5-part loop"):**
`🎯 Learning Objectives` → `📚 Learn` → `🔬 Internals (go deep)` → `🛠️ Exercise` →
`✅ Definition of Done`, plus `🗒️ Cheatsheet` and `🔗 Related`. A `> [!info] Unit` callout at the
top states Domain/Month/Depth/Est and "Why a Tech Lead needs this".

The structure is plan-driven (6 months, 12 h/week, ~312 h, Java 21 + Spring Boot 3) and each topic
is self-contained, hands-on, and progress-tracked.

### The target repo

`java-roadmap/` currently contains only:
- `.git/` (initialized, no commits relevant to content)
- `.idea/` (IntelliJ project metadata)
- `LICENSE` — MIT, "Copyright (c) 2026 Vadym Novakovskyi"

It is **not** under the working directory's git (working dir is `/Users/vnovakovskyi/PrivateDevelopment`,
which is itself not a repo; `java-roadmap` is its own repo). No `README.md` yet.

### The shared image

`s4kibs4mi/java-developer-roadmap` — a roadmap.sh-style **mind-map**: a central spine of stages
(Java → Gradle/Maven → SQL fundamentals → General Dev Skills → CLI / Web Frameworks / ORMs /
Databases / Caching …) with dashed branches to sub-topics, and a legend
("Personal must know" / "Good to know" / "Possibilities"). It is dense and aimed at someone who
already knows *a* language. We take its **visual style** as inspiration, not its exact content.

## 3. Problem / Opportunity

There is a high-quality study system for senior→tech-lead, but **nothing for the from-scratch
beginner**. The opportunity is to produce a **fork-and-go Obsidian vault** that takes someone with
zero programming experience to a job-ready junior Java developer, reusing the proven structure
(MOC + Conventions + Template + per-topic notes + dashboard + visual canvas) but re-pitched for
beginners.

Key difference from the source: a beginner audience needs **true fundamentals first**
(what is a program, the CLI, variables/types, control flow, OOP), gentler pacing, and a different
"Why you need this" framing ("Why a junior developer needs this" rather than "Why a Tech Lead
needs this"). The end state is **job-ready junior**, not architect.

## 4. Target Users / Stakeholders

- **Primary user:** a complete beginner (career switcher, student, self-taught) who downloads the
  repo and uses it as their structured Java learning path.
- **Secondary user:** the repo owner (Vadym) — publishing a useful public resource; reuses his own
  conventions so it feels familiar and is maintainable.
- **Mentors / bootcamp leads** who might point learners at a single, coherent path.
- **Stakeholders for maintainability:** anyone who later adds/edits topics — they rely on the
  `_Conventions` + `_Template` contract and consistent file naming.

## 5. Current State

New project. Findings on maturity, alternatives, constraints:

- **Idea maturity:** clear and well-scoped. A concrete, proven structural template exists to copy.
- **Existing alternatives:**
  - `roadmap.sh` Java roadmap and `s4kibs4mi/java-developer-roadmap` — strong *visuals*, but a
    web/image format, not an actionable Obsidian study vault, and assume prior programming.
  - Generic "learn Java" course lists — not vault-native, no progress tracking.
  - The user's own tech-lead vault — wrong audience, but the perfect *format*.
  - **Gap:** a beginner-focused, Obsidian-native, hands-on, progress-tracked roadmap with a visual map.
- **Known constraints:**
  - Output must be plain Markdown + Obsidian-native artifacts (`.canvas`, optionally `.base`) so it
    works on desktop and mobile Obsidian with no plugins beyond core/Bases.
  - Must remain useful when viewed on **GitHub** (a `README.md` that renders, plus a committed
    **image** of the roadmap since GitHub does not render `.canvas`).
  - File naming and frontmatter must be internally consistent for any dashboard to work.

## 6. Findings

- **The vault is fully reusable as a template.** Every structural file (`MOC`, `_Conventions`,
  `_Template - Topic`, `Weekly Log`, `Dashboard.base`, `Roadmap.canvas`, `Topics/`) maps 1:1 to
  what a beginner vault needs. *Why it matters:* we can mirror the architecture and focus effort on
  beginner-appropriate content. *Source:* the seven files read under the source vault.
- **`Roadmap.canvas` is Obsidian-only and references files by vault-relative path**
  (`"Personal/Java tech lead/Topics/…"`). *Why it matters:* a copied canvas must use paths relative
  to the new vault root (e.g. `Topics/…`), and GitHub will not render it — so a separate exported
  **image (SVG/PNG)** is required for "look at it and understand the path". *Source:* `Roadmap.canvas`.
- **`Dashboard.base` depends on the Obsidian "Bases" feature** and the controlled frontmatter
  vocabulary; if frontmatter drifts, views silently miss notes. *Why it matters:* the beginner vault
  must ship its own `_Conventions` describing the exact allowed values, and a Month-Index fallback
  (the source MOC explicitly keeps a fallback "because the Dashboard may fail to render on a device").
  *Source:* `Dashboard.base`, MOC lines 25–31.
- **Topic notes are hands-on and outcome-driven** (`Exercise` + `Definition of Done`), not passive
  reading lists. *Why it matters:* the beginner version should keep this — beginners learn by
  building — but scale exercises down to beginner reach (e.g. "write a CLI calculator"), and adapt
  `🔬 Internals (go deep)` into something gentler like `🧠 Concepts to nail` for early modules.
  *Source:* GC and Testing topic notes.
- **The source is a 6-month / ~312h plan.** A from-scratch path is necessarily longer and broader at
  the base (fundamentals, OOP, tooling) and shallower at the top (no K8s/observability deep dives).
  *Why it matters:* the module/phase breakdown must be redesigned, not copied. A reasonable shape:
  phases like **Foundations → Core Java → OOP → Collections & Generics → Tooling (Git, Maven/Gradle)
  → Testing → SQL & Databases → Web/Spring Boot → Building a Real Project → Job-Readiness**.
  *Source:* MOC intro + Month Index.
- **Books and tools were requested explicitly.** The source vault embeds resources inside each
  topic's `📚 Learn`, but does not have a dedicated books/tools index. *Why it matters:* the beginner
  vault should add a **Books & Resources** note and a **Tools/Setup** note (JDK install, IDE, Git),
  since beginners need an environment before they can do anything. *Source:* user request + absence
  in source.
- **The MIT LICENSE + 2026 copyright are already present**, signalling this is intended as a public,
  shareable repo. *Why it matters:* a `README.md` with "how to use as an Obsidian vault" + the
  visual image is part of the deliverable, not optional. *Source:* `LICENSE`.

## 7. Assumptions

- **Target end state = job-ready junior Java developer** (can build a small Spring Boot CRUD app,
  use Git, write tests, query a DB), not mid/senior. *Needs validation.*
- **Java version: 21 (LTS)**, matching the source vault and current LTS practice. *Likely safe.*
- **Pacing target: ~10–12 h/week** over roughly **6–9 months** (beginner content is broader).
  Exact numbers are an assumption; the plan should state effort per topic and let the learner pace.
- **Spring Boot is the web framework of choice** (vs. the mind-map's broader CLI/web-framework menu),
  because it is the dominant junior-Java job skill. Other frameworks become "good to know".
- **Obsidian with core plugins + Bases** is the intended reader; we keep a Markdown/Month-Index
  fallback so it degrades gracefully without Bases.
- **The visual** should be a committed **SVG (and/or PNG)** so it renders on GitHub, *plus* a native
  `.canvas` for in-Obsidian navigation. The user said "like the picture" → mind-map/flow style.
- **Scope of this effort produces the full vault content**, including drafting all topic notes (not
  just scaffolding). Volume of topic notes is large; an assumption that "complete" means real,
  usable notes for every topic.

## 8. Risks

- **Scope/volume:** a from-scratch curriculum can balloon to 50–80 topic notes. Risk of either
  incomplete delivery or shallow notes. *Mitigation:* fix a phase/topic count up front and write
  genuinely useful (if concise) notes for each.
- **Content accuracy / staleness:** book editions, JDK version specifics, and tool install steps go
  stale. *Mitigation:* prefer canonical/official docs, note "as of Java 21", avoid edition-pinning
  where possible.
- **Obsidian feature dependence:** `.base` requires Bases; `.canvas` won't render on GitHub.
  *Mitigation:* Month-Index fallback in the MOC + committed image; document plugin needs in README.
- **Path correctness in `.canvas`:** wrong vault-relative paths break every card link.
  *Mitigation:* use `Topics/…` relative to vault root and verify against actual filenames.
- **Curriculum opinion risk:** "everything needed" is subjective; over-scoping (e.g. Kafka, K8s) can
  demoralize beginners, under-scoping leaves gaps. *Mitigation:* tier topics (must / good-to-know /
  later) mirroring the inspiration image's legend.
- **Maintainability:** if frontmatter vocabulary isn't pinned in `_Conventions`, future edits break
  the dashboard. *Mitigation:* ship a beginner-tailored `_Conventions` and `_Template`.
- **Link integrity:** `[[wikilinks]]` and `Related` sections must match real note titles or Obsidian
  shows broken links. *Mitigation:* generate links from the canonical file list.

## 9. Open Questions

**Resolved with the user (2026-06-19):**

1. **End state — RESOLVED:** target ceiling is **job-ready junior** (zero → can build a small Spring
   Boot CRUD app, use Git, write tests, query a DB). No interview-prep phase and no intermediate
   deep-dives beyond what junior readiness requires.
3. **Build tool — RESOLVED:** cover **both Maven and Gradle** equally/in depth.
4. **Visual format — RESOLVED:** ship **both** a committed **SVG mind-map** (renders on GitHub) and
   an interactive Obsidian **`.canvas`**.

**Still open (can be decided during planning):**

2. **Pacing/timeline:** state a cadence (e.g. "~6 months @ 10–12 h/wk") or keep open-ended with
   per-topic effort estimates only? *(Leaning: state a soft target + per-topic effort.)*
5. **Books:** any must-include titles to feature (e.g. *Head First Java*, *Effective Java*,
   *Modern Java in Action*), or leave the recommendation to the plan? *(Leaning: recommend a
   tiered list in a Books note.)*

## 10. Recommendation

**Continue to `plan`.** The problem is well understood, a proven structural template exists, and
constraints are clear. No `architecture` or `data-model` phase is needed — this is content/IA work,
not software architecture. The plan phase should lock down:

- the phase/module breakdown and topic list (the curriculum),
- the frontmatter vocabulary + file-naming for the beginner audience,
- the set of vault files to produce (MOC, `_Conventions`, `_Template`, `Weekly Log`,
  `Dashboard.base`, `Roadmap.canvas`, `Topics/*`, plus `README.md`, a **Books & Resources** note, a
  **Tools & Setup** note),
- the visual deliverable (SVG/PNG mind-map + Obsidian canvas) and its tiering legend.

Before finalizing the plan, the open questions above (especially end-state ceiling, pacing, and
build-tool focus) are worth a quick confirmation.

## 11. Next Action

Run the **plan** phase to produce `docs/01-plan.md`: a concrete curriculum (phases → topics),
the file manifest for the vault, the frontmatter contract, and the visual-map design. Optionally
answer Open Questions 1–6 first to tighten scope.
