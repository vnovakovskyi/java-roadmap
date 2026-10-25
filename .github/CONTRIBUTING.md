# Contributing to the Java Developer Roadmap

Thank you for helping! Every improvement — a typo, a dead link, a clearer explanation, a better
resource — makes the path easier for the next learner.

## Small fixes

Typos, broken or outdated links, unclear sentences: edit the file directly on GitHub (pencil icon)
and open a pull request. That's all.

## How the vault is built

- Topic notes live in `Topics/` and follow the template in `System/_Template - Topic.md`.
- `System/_Conventions.md` defines the frontmatter values (`area`, `module`, `status`, `priority`,
  `effort`), the section order, and the stack versions the content targets.
- The **Module Index in `Home.md`** is the single source of truth for the order of topics.
- Topic files are numbered by their place in it: `M3.05 - OOP - Inheritance.md` is the 5th topic of
  Module 3. The numbers, the **Next** links, `assets/roadmap.svg`, `Roadmap.canvas`, and the topic
  list in `README.md` are **generated** from the index — don't edit them by hand.

## Adding, renaming, or reordering a topic

1. Create or edit the note in `Topics/`. A new note is named `M{module} - {Area} - {Topic}.md`;
   `build` adds its number.
2. Put it in the right place in the Module Index in `Home.md` (to reorder, move the lines). Moving a
   topic to another module? Also update its `module` and `area` and the info callout.
3. Number, regenerate and check:
   ```bash
   python3 .github/scripts/vault.py build
   python3 .github/scripts/vault.py check
   ```
   `build` renames the topic files to match the index (a new topic shifts only the topics after it in
   its module), updates every link to a renamed note, and sets the **Next** links. The same check
   runs on every pull request, together with an external link checker.

## Guidelines for content

- **Resources:** free first; prefer official docs (dev.java, docs.oracle.com, docs.spring.io) and
  well-maintained sources. Link to the exact page, not a site's home page, and say in a few words
  why it's worth reading.
- **Versions:** content targets Java 25 (LTS) and Spring Boot 4. Flag version-specific facts inline,
  e.g. *(Java 25+)* or *(Spring Boot 4)*, and avoid resources that teach outdated APIs without a
  warning.
- **Self-check:** 3–5 questions per topic; each answer is factual and fits in one to three sentences.
- **Practice:** concrete, runnable tasks — the learner should know exactly when they're done.
- Keep the tone friendly and direct, and the notes short enough to finish in a session.

Not sure whether a change fits? Open an issue first and let's talk it through.
