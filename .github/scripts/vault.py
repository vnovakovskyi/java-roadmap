#!/usr/bin/env python3
"""Check the vault and regenerate its derived files.

The Module Index in Home.md is the single source of truth for the order of topics.

    python3 .github/scripts/vault.py check   # validate notes, links and generated files
    python3 .github/scripts/vault.py build   # regenerate roadmap.svg, Roadmap.canvas, README index

`build` rewrites:
  - assets/roadmap.svg       the visual map shown in the README
  - Roadmap.canvas           the clickable Obsidian canvas
  - README.md                the topic list between the topic-index markers
"""
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPICS = ROOT / "Topics"
HOME = ROOT / "Home.md"
README = ROOT / "README.md"
SVG = ROOT / "assets" / "roadmap.svg"
CANVAS = ROOT / "Roadmap.canvas"

AREAS = {1: "Foundations", 2: "Core Java", 3: "OOP", 4: "Java APIs", 5: "Modern Java", 6: "Tooling",
         7: "Testing", 8: "Databases", 9: "Spring", 10: "Project", 11: "Career"}
STATUSES = {"todo", "doing", "done"}
PRIORITIES = {"must", "good", "optional"}
SECTIONS = ["Learning Objectives", "Learn", "Concepts", "Practice", "Self-check", "Definition of Done", "Next"]
INDEX_START, INDEX_END = "<!-- topic-index:start -->", "<!-- topic-index:end -->"

# Shown in the two boxes at the bottom of the SVG.
TOOLS = ["JDK 25 LTS (Temurin)", "IntelliJ IDEA", "Git, GitHub & GitHub Actions", "Maven · Gradle",
         "Docker & Docker Compose", "JUnit 6 · AssertJ · Mockito · Testcontainers", "PostgreSQL · Flyway",
         "Spring Boot 4", "An AI assistant — used wisely"]
BOOKS = ["Head First Java (beginner)", "Effective Java (level-up)", "Modern Java in Action (streams)",
         "Spring Start Here, 2nd ed. (Spring)", "Grokking Algorithms, 2nd ed. (interviews)", "Pro Git (free)",
         "dev.java · Helsinki Java MOOC (free)", "Exercism Java track (free practice)"]
MODULE_COLORS = ["#0f766e", "#1d4ed8", "#6d28d9", "#be123c", "#b45309", "#0e7490", "#15803d", "#9333ea",
                 "#c2410c", "#334155", "#4d7c0f"]
PRIORITY_STYLE = {"must": ("#fef3c7", "#f59e0b"), "good": ("#ffedd5", "#fb923c"), "optional": ("#e5e7eb", "#9ca3af")}
CANVAS_COLORS = ["4", "5", "6", "2", "3", "1"]


def read_index():
    """Return [(module_no, module_title, [topic names in order])] from Home.md's Module Index."""
    text = HOME.read_text(encoding="utf-8")
    index = text.split("## Module Index", 1)[1]
    modules = []
    for line in index.splitlines():
        m = re.match(r"^### Module (\d+) — (.+)$", line)
        if m:
            modules.append((int(m.group(1)), m.group(2).strip(), []))
            continue
        m = re.match(r"^- \[\[([^\]|]+)\]\]", line)
        if m and modules:
            modules[-1][2].append(m.group(1))
    return modules


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    data, key = {}, None
    for line in m.group(1).splitlines():
        if line.startswith("  - ") and key:
            data.setdefault(key, []).append(line[4:].strip())
        elif ":" in line:
            key, _, value = line.partition(":")
            key, value = key.strip(), value.strip()
            data[key] = value if value else []
    return data


def load_topics():
    topics = {}
    for path in sorted(TOPICS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        topics[path.stem] = {"path": path, "text": text, "fm": frontmatter(text)}
    return topics


def check():
    errors = []
    modules = read_index()
    topics = load_topics()
    order = [name for _, _, names in modules for name in names]

    if [m for m, _, _ in modules] != list(range(1, len(modules) + 1)):
        errors.append("Home.md: module headings must be numbered 1..N in order")
    for name in order:
        if name not in topics:
            errors.append(f"Home.md lists a topic that doesn't exist: {name}")
    for name in topics:
        if order.count(name) != 1:
            errors.append(f"{name}: must appear exactly once in the Home.md Module Index (found {order.count(name)})")

    for i, name in enumerate(order):
        if name not in topics:
            continue
        t, fm = topics[name]["text"], topics[name]["fm"]
        module = next(m for m, _, names in modules if name in names)
        where = f"Topics/{name}.md"
        try:
            fm_module, effort = int(fm.get("module", "")), int(fm.get("effort", ""))
        except ValueError:
            errors.append(f"{where}: module and effort must be numbers"); continue
        if fm_module != module:
            errors.append(f"{where}: module {fm_module} but listed under Module {module} in Home.md")
        area = AREAS.get(module)
        if fm.get("area") != area:
            errors.append(f"{where}: area must be '{area}' for module {module}")
        if not name.startswith(f"M{module} - {area} - "):
            errors.append(f"{where}: file name must start with 'M{module} - {area} - '")
        if fm.get("status") not in STATUSES:
            errors.append(f"{where}: status must be one of {sorted(STATUSES)}")
        if fm.get("priority") not in PRIORITIES:
            errors.append(f"{where}: priority must be one of {sorted(PRIORITIES)}")
        if "java-roadmap" not in fm.get("tags", []):
            errors.append(f"{where}: tags must include java-roadmap")
        if f"\n# {fm.get('title')}\n" not in t:
            errors.append(f"{where}: the H1 heading must equal the title property")
        info = (f"> **Area:** {fm.get('area')} · **Module:** {fm_module} · "
                f"**Priority:** {fm.get('priority')} · **Est:** {effort}h")
        if info not in t:
            errors.append(f"{where}: the info callout doesn't match the frontmatter (expected: {info})")
        headings = re.findall(r"^## (.+)$", t, re.M)
        if headings != SECTIONS:
            errors.append(f"{where}: sections must be {SECTIONS}, found {headings}")
        expected = f"[[{order[i + 1]}]]" if i + 1 < len(order) else "[[Home]]"
        if expected not in t.split("## Next", 1)[-1]:
            errors.append(f"{where}: the Next link must point to {expected}")

    notes = {p.stem for p in ROOT.rglob("*.md") if ".git" not in p.parts} | {"Roadmap.canvas"}
    for path in [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".github" not in p.parts] + [CANVAS]:
        prose = re.sub(r"```.*?```|`[^`\n]*`", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[\[([^\]|#]*)", prose):
            if target.strip() and target.strip() not in notes:
                errors.append(f"{path.relative_to(ROOT)}: unresolved link [[{target}]]")

    for path, content in generated(modules, topics).items():
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            errors.append(f"{path.relative_to(ROOT)} is out of date — run: python3 .github/scripts/vault.py build")

    for e in errors:
        print("✗", e)
    print(f"{'FAILED' if errors else 'OK'}: {len(order)} topics in {len(modules)} modules, {len(errors)} problem(s)")
    return 1 if errors else 0


def build():
    modules, topics = read_index(), load_topics()
    for path, content in generated(modules, topics).items():
        path.write_text(content, encoding="utf-8")
        print("wrote", path.relative_to(ROOT))
    return 0


def generated(modules, topics):
    rows = [(m, title, [(n, topics[n]["fm"]) for n in names if n in topics]) for m, title, names in modules]
    return {SVG: render_svg(rows), CANVAS: render_canvas(rows), README: render_readme(rows)}


def totals(rows):
    items = [fm for _, _, ts in rows for _, fm in ts]
    hours = sum(int(fm["effort"]) for fm in items)
    core = sum(int(fm["effort"]) for fm in items if fm["priority"] == "must")
    return len(items), hours, core


def render_svg(rows):
    font = 'font-family="Segoe UI, Helvetica, Arial, sans-serif"'
    esc = lambda s: html.escape(s, quote=True)
    count, hours, core = totals(rows)
    out, y = [], 156
    for m, title, ts in rows:
        color = MODULE_COLORS[(m - 1) % len(MODULE_COLORS)]
        out.append(f'<rect x="40" y="{y}" width="1160" height="38" rx="8" fill="{color}"/>')
        out.append(f'<text x="56" y="{y + 24}.0" font-size="16" font-weight="700" fill="#ffffff" {font}>'
                   f'M{m}  —  {esc(title)}</text>')
        y += 46
        for name, fm in ts:
            fill, stroke = PRIORITY_STYLE[fm["priority"]]
            out.append(f'<rect x="64" y="{y}" width="1136" height="22" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
            out.append(f'<text x="80" y="{y + 14}.0" font-size="13.5" fill="#1f2937" {font}>{esc(fm["title"])}</text>')
            out.append(f'<text x="1186" y="{y + 14}.0" text-anchor="end" font-size="12" fill="#64748b" {font}>{fm["effort"]}h</text>')
            out.append(f'<rect x="50" y="{y + 3}" width="6" height="16" rx="2" fill="{color}"/>')
            y += 26
        y += 26
    y += 4
    boxes = []
    for x, heading, items in [(40, "Tools you'll set up & use", TOOLS), (630, "Recommended books & free resources", BOOKS)]:
        h = 46 + 22 * (len(items) - 1) + 18
        boxes.append(f'<rect x="{x}" y="{y}" width="570" height="{h}" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>')
        boxes.append(f'<text x="{x + 16}" y="{y + 24}" font-size="15" font-weight="700" fill="#0f172a" {font}>{esc(heading)}</text>')
        for i, item in enumerate(items):
            boxes.append(f'<text x="{x + 16}" y="{y + 46 + 22 * i}" font-size="13" fill="#334155" {font}>•  {esc(item)}</text>')
    height = y + 46 + 22 * (max(len(TOOLS), len(BOOKS)) - 1) + 18 + 24
    legend_x = 110
    legend = []
    for label, key, width in [("Must know", "must", 145), ("Good to know", "good", 172), ("Optional / later", "optional", 0)]:
        fill, stroke = PRIORITY_STYLE[key]
        legend.append(f'<rect x="{legend_x}" y="112" width="22" height="18" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        legend.append(f'<text x="{legend_x + 30}" y="126" font-size="13" fill="#334155" {font}>{label}</text>')
        legend_x += width
    head = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 {height}" {font}>',
        f'<rect x="2" y="2" width="1236" height="{height - 4}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>',
        f'<text x="620.0" y="54" text-anchor="middle" font-size="30" font-weight="700" fill="#0f172a" {font}>Java Developer Roadmap</text>',
        f'<text x="620.0" y="84" text-anchor="middle" font-size="14" fill="#475569" {font}>From zero programming experience to a '
        f'job-ready junior Java developer  ·  {len(rows)} modules  ·  {count} topics  ·  ~{hours} h (core path ~{core} h)</text>',
        f'<text x="40" y="126" font-size="13" font-weight="700" fill="#334155" {font}>Legend:</text>',
        f'<text x="1200" y="126" text-anchor="end" font-size="12" fill="#64748b" {font}>numbers = estimated hours</text>',
    ]
    return "\n".join(head + legend + out + boxes + ["</svg>"]) + "\n"


def render_canvas(rows):
    count, hours, core = totals(rows)
    nodes = [{"id": "intro", "type": "text",
              "text": "# Java Developer Roadmap\nFrom zero to a job-ready junior Java developer — "
                      f"{len(rows)} modules, {count} topics, ~{hours} h.\nWork left to right, top to bottom. "
                      "Click any card to open that topic. Open [[Home]] for the live dashboard.",
              "x": 0, "y": -240, "width": 1200, "height": 170, "color": "4"}]
    for m, title, ts in rows:
        x, color = (m - 1) * 460, CANVAS_COLORS[(m - 1) % len(CANVAS_COLORS)]
        nodes.append({"id": f"group{m}", "type": "group", "label": f"M{m} — {title}",
                      "x": x, "y": 0, "width": 430, "height": 80 + 70 * len(ts), "color": color})
        for i, (name, fm) in enumerate(ts):
            nodes.append({"id": f"m{m}c{i}", "type": "text", "text": f"[[{name}|{fm['title']}]]",
                          "x": x + 15, "y": 60 + 70 * i, "width": 400, "height": 56, "color": color})
    return json.dumps({"nodes": nodes, "edges": []}, indent="\t", ensure_ascii=False) + "\n"


def render_readme(rows):
    text = README.read_text(encoding="utf-8")
    if INDEX_START not in text or INDEX_END not in text:
        return text
    lines = [INDEX_START, ""]
    for m, title, ts in rows:
        hours = sum(int(fm["effort"]) for _, fm in ts)
        lines.append(f"<details><summary><b>M{m} — {html.escape(title)}</b> · {len(ts)} topics · ~{hours} h</summary>")
        lines.append("")
        for name, fm in ts:
            link = "Topics/" + urllib.parse.quote(name + ".md")
            lines.append(f"- [{fm['title']}]({link}) — {fm['priority']} · {fm['effort']} h")
        lines += ["", "</details>"]
    lines += ["", INDEX_END]
    before, rest = text.split(INDEX_START, 1)
    after = rest.split(INDEX_END, 1)[1]
    return before + "\n".join(lines) + after


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "check"
    sys.exit({"check": check, "build": build}.get(command, lambda: print(__doc__) or 2)())
