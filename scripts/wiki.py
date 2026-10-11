#!/usr/bin/env python3
"""Wiki bookkeeping helpers, so agents don't have to read index.md / log.md whole.

  scripts/wiki.py stats [--hotcache]      page counts (--hotcache rewrites the stats block)
  scripts/wiki.py related TERM... [-n N]  rank pages by slug/title/tags/index/body matches
  scripts/wiki.py index-set [SLUG DESC]   insert (top of section, newest first) or replace index
                                          entries; or stdin lines "- [[slug]] — desc"; --end
                                          appends to the section instead (backfills)
  scripts/wiki.py log-append < entry.md   append one entry to wiki/log.md
  scripts/wiki.py check [--changed]       index drift, broken links, table pipes, frontmatter,
                                          slug collisions, orphans (--changed: git-dirty pages only)

Stdlib only. Run from anywhere; paths resolve from the repo root.
"""

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"
LOG = WIKI / "log.md"
HOTCACHE = ROOT / "hotcache.md"

SECTIONS = {"sources": "Sources", "entities": "Entities", "concepts": "Concepts", "analysis": "Analysis"}
SECTION_ORDER = ["Sources", "Entities", "Concepts", "Analysis"]
REQUIRED_KEYS = ["title", "type", "tags", "created", "updated"]

INDEX_LINE = re.compile(r"^- \[\[([^\]|\\]+)(?:\\?\|[^\]]*)?\]\]\s+—\s+(.*)$")
WIKILINK = re.compile(r"\[\[([^\]]+?)\]\]")
STATS_START, STATS_END = "<!-- stats:start -->", "<!-- stats:end -->"

# Model output sometimes leaks a word from another language into Thai prose
# ("การ перевірка", "補", "trả về"). CJK/Vietnamese are never expected here; Cyrillic
# only counts when a lowercase word sits outside quotes/parentheses (Cosmism pages
# quote Russian legitimately).
LEAK_ALWAYS = re.compile(r"[\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7AF\u1EA0-\u1EF9\u01A1\u01B0\u0111]")
LEAK_CYRILLIC = re.compile(r"(?<![\u0400-\u04FF])[\u0430-\u045F][\u0400-\u04FF]*")
QUOTED = re.compile(r'"[^"]*"|“[^”]*”|\([^)]*\)|`[^`]*`')


# ---------- loading ----------

class Page:
    def __init__(self, path):
        self.path = path
        self.kind = path.parent.name
        self.slug = path.stem
        self.text = path.read_text(encoding="utf-8")
        self.front, self.body, self.front_raw = split_frontmatter(self.text)

    @property
    def rel(self):
        return self.path.relative_to(ROOT).as_posix()

    @property
    def title(self):
        return self.front.get("title", "")

    @property
    def tags(self):
        return parse_list(self.front.get("tags", ""))


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text, None
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, None
    raw = text[4:end]
    front = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            front[m.group(1)] = m.group(2).strip()
    return front, text[end + 5:], raw


def parse_list(value):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [v.strip().strip("'\"") for v in value.split(",") if v.strip()]


def load_pages():
    pages = []
    for kind in SECTIONS:
        d = WIKI / kind
        if d.is_dir():
            pages.extend(Page(p) for p in sorted(d.glob("*.md")))
    return pages


def read_index():
    return read_index_lines(INDEX.read_text(encoding="utf-8").splitlines())


def read_index_lines(lines):
    """Return (lines, entries) where entries = list of (line_no, slug, desc, section)."""
    entries, section = [], None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        m = INDEX_LINE.match(line)
        if m:
            entries.append((i, m.group(1).strip(), m.group(2).strip(), section))
    return lines, entries


def link_target(raw):
    target = re.split(r"\\?\||#", raw, maxsplit=1)[0].strip()
    return target.rsplit("/", 1)[-1].removesuffix(".md")


def iter_links(text):
    """Yield (line_no, target) for every wikilink outside fenced code blocks."""
    fenced = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        for m in WIKILINK.finditer(line):
            yield n, link_target(m.group(1))


# ---------- commands ----------

def counts():
    return {kind: len(list((WIKI / kind).glob("*.md"))) if (WIKI / kind).is_dir() else 0 for kind in SECTIONS}


def cmd_stats(args):
    c = counts()
    line = (f"- **Pages:** {c['sources']} sources · {c['concepts']} concepts · "
            f"{c['entities']} entities · {c['analysis']} analysis")
    print(line)
    if args.hotcache:
        text = HOTCACHE.read_text(encoding="utf-8")
        if STATS_START not in text or STATS_END not in text:
            sys.exit(f"hotcache.md has no {STATS_START} … {STATS_END} block")
        head, rest = text.split(STATS_START, 1)
        _, tail = rest.split(STATS_END, 1)
        HOTCACHE.write_text(f"{head}{STATS_START}\n{line}\n{STATS_END}{tail}", encoding="utf-8")
        print("updated hotcache.md")


def cmd_related(args):
    terms = [t.casefold() for t in args.terms]
    _, entries = read_index()
    descs = {slug: desc for _, slug, desc, _ in entries}
    scored = []
    for p in load_pages():
        slug, title = p.slug.casefold(), p.title.casefold()
        tags = " ".join(p.tags).casefold()
        desc = descs.get(p.slug, "").casefold()
        body = p.body.casefold()
        score, hit = 0, 0
        for t in terms:
            s = (6 * (t in slug) + 4 * (t in title) + 4 * (t in tags)
                 + 2 * (t in desc) + min(body.count(t), 5))
            score += s
            hit += s > 0
        if score:
            scored.append((score + 3 * hit, p))
    scored.sort(key=lambda x: (-x[0], x[1].slug))
    for score, p in scored[: args.n]:
        desc = descs.get(p.slug, p.title)
        if len(desc) > 110:
            desc = desc[:110] + "…"
        print(f"{score:3d}  {p.kind}/{p.slug}  — {desc}")
    if not scored:
        print("no matches")


def cmd_index_set(args):
    if args.slug:
        if not args.desc:
            sys.exit("usage: index-set SLUG DESC")
        items = [(args.slug, " ".join(args.desc))]
    else:
        items = []
        for line in sys.stdin.read().splitlines():
            if not line.strip():
                continue
            m = INDEX_LINE.match(line.strip())
            if not m:
                sys.exit(f"not an index line: {line}")
            items.append((m.group(1).strip(), m.group(2).strip()))

    by_slug = defaultdict(list)
    for p in load_pages():
        by_slug[p.slug].append(p)

    lines, _ = read_index()
    for slug, desc in items:
        found = by_slug.get(slug)
        if not found:
            sys.exit(f"no page wiki/*/{slug}.md — create it before indexing")
        if len(found) > 1:
            sys.exit(f"slug collision for {slug}: {', '.join(p.rel for p in found)}")
        section = SECTIONS[found[0].kind]
        new_line = f"- [[{slug}]] — {desc}"

        _, entries = read_index_lines(lines)
        existing = [e for e in entries if e[1] == slug and e[3] == section]
        if existing:
            lines[existing[0][0]] = new_line
            print(f"replaced  {section}: {slug}")
            continue
        header = f"## {section}"
        if header not in lines:
            insert_section(lines, header)
        start = lines.index(header) + 1
        pos = start
        if args.end:
            pos = next((i for i in range(start, len(lines)) if lines[i].startswith("## ")), len(lines))
            while pos > start and not lines[pos - 1].strip():
                pos -= 1
        lines.insert(pos, new_line)
        print(f"added     {section}: {slug}")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def insert_section(lines, header):
    """Add a missing section header in SECTION_ORDER position."""
    name = header[3:]
    later = SECTION_ORDER[SECTION_ORDER.index(name) + 1:]
    for i, line in enumerate(lines):
        if line.startswith("## ") and line[3:].strip() in later:
            lines[i:i] = [header, ""]
            return
    if lines and lines[-1].strip():
        lines.append("")
    lines.append(header)


def cmd_log_append(args):
    entry = sys.stdin.read().strip()
    if not re.match(r"^## \[\d{4}-\d{2}-\d{2}\] \S+ \| .+", entry):
        sys.exit("entry must start with '## [YYYY-MM-DD] operation | Title'")
    text = LOG.read_text(encoding="utf-8").rstrip("\n")
    LOG.write_text(f"{text}\n\n{entry}\n", encoding="utf-8")
    print(f"appended: {entry.splitlines()[0]}")


def changed_paths():
    out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--", "wiki"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    paths = set()
    for line in out.splitlines():
        path = line[3:].split(" -> ")[-1].strip().strip('"')
        paths.add(path)
    return paths


def head_text(rel):
    """File content at HEAD, or '' for a new file."""
    r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def yaml_risk(key, value):
    """Flag plain scalars that strict YAML (Quartz's js-yaml) is likely to reject."""
    if not value or value[0] in "[{" or value[0] in "\"'" and value[-1:] == value[0]:
        return None
    if value[0] in "\"'":
        return "unbalanced quote"
    if value[0] in "@`%&*!|>":
        return f"starts with reserved '{value[0]}'"
    if ": " in value or value.endswith(":"):
        return "contains ': ' — quote the value"
    if " #" in value:
        return "contains ' #' (comment) — quote the value"
    return None


def cmd_check(args):
    pages = load_pages()
    problems = 0

    def report(title, rows):
        nonlocal problems
        if rows:
            problems += len(rows)
            print(f"\n{title} ({len(rows)})")
            for r in rows:
                print(f"  {r}")

    # --changed: only pages dirty in git, and only problems they introduce
    # (links/lines already present at HEAD are the lint backlog, not this change)
    scope = None
    if args.changed:
        scope = changed_paths()
        print(f"checking {len([p for p in pages if p.rel in scope])} changed page(s) + global index")
    in_scope = [p for p in pages if scope is None or p.rel in scope]
    old = {p.rel: head_text(p.rel) for p in in_scope} if args.changed else {}
    old_links = {rel: {t.casefold() for _, t in iter_links(text)} for rel, text in old.items()}
    old_lines = {rel: set(text.splitlines()) for rel, text in old.items()}

    # slug collisions across folders make [[slug]] ambiguous
    by_slug = defaultdict(list)
    for p in pages:
        by_slug[p.slug.casefold()].append(p)
    report("slug collisions (same filename in two folders)",
           [", ".join(p.rel for p in ps) for ps in by_slug.values()
            if len(ps) > 1 and any(p in in_scope for p in ps)])

    # index drift
    _, entries = read_index()
    indexed = Counter((slug, sec) for _, slug, _, sec in entries)
    report("pages missing from index",
           [p.rel for p in in_scope if (p.slug, SECTIONS[p.kind]) not in indexed])
    known = {(p.slug, SECTIONS[p.kind]) for p in pages}
    slugs = {p.slug for p in pages}
    report("index entries without a page",
           [f"{sec}: {slug}" for (slug, sec) in indexed if slug not in slugs])
    report("index entries in the wrong section",
           [f"{sec}: {slug}" for (slug, sec) in indexed if slug in slugs and (slug, sec) not in known])
    report("duplicate index entries", [f"{sec}: {slug}" for (slug, sec), n in indexed.items() if n > 1])

    # broken wikilinks
    targets = {p.stem.casefold() for p in WIKI.rglob("*.md")}
    broken = []
    for p in in_scope:
        for n, t in iter_links(p.text):
            if t and t.casefold() not in targets and t.casefold() not in old_links.get(p.rel, ()):
                broken.append(f"{p.rel}:{n}  [[{t}]]")
    report("broken wikilinks", broken)

    # unescaped pipes inside table rows
    pipes = []
    for p in in_scope:
        for n, line in enumerate(p.text.splitlines(), 1):
            if line in old_lines.get(p.rel, ()):
                continue
            if line.lstrip().startswith("|") and re.search(r"\[\[[^\]]*(?<!\\)\|[^\]]*\]\]", line):
                pipes.append(f"{p.rel}:{n}")
    report("unescaped | in wikilink inside table row", pipes)

    # frontmatter
    fm = []
    for p in in_scope:
        if p.front_raw is None:
            fm.append(f"{p.rel}: missing frontmatter")
            continue
        missing = [k for k in REQUIRED_KEYS if k not in p.front]
        if p.kind == "sources" and "date_ingested" in p.front:  # older source schema
            missing = [k for k in missing if k not in ("created", "updated")]
        if missing:
            fm.append(f"{p.rel}: missing {', '.join(missing)}")
        for k, v in p.front.items():
            risk = yaml_risk(k, v)
            if risk:
                fm.append(f"{p.rel}: {k}: {risk}")
    report("frontmatter problems", fm)

    # leaked foreign-language words
    leaks = []
    for p in in_scope:
        fenced = False
        for n, line in enumerate(p.body.splitlines(), 1):
            if line.lstrip().startswith("```"):
                fenced = not fenced
            if fenced or line in old_lines.get(p.rel, ()):
                continue
            m = LEAK_ALWAYS.search(line) or LEAK_CYRILLIC.search(QUOTED.sub("", line))
            if m:
                leaks.append(f"{p.rel}  …{line[max(0, m.start() - 25):m.end() + 15].strip()}…")
    report("leaked foreign-script words (CJK/Vietnamese/Cyrillic)", leaks)

    # orphans: no inbound links except from index/log
    inbound = Counter()
    for p in pages:
        for _, t in iter_links(p.text):
            if t.casefold() != p.slug.casefold():
                inbound[t.casefold()] += 1
    report("orphans (no inbound links outside index/log)",
           [p.rel for p in in_scope if inbound[p.slug.casefold()] == 0 and not old.get(p.rel)])

    print("\nOK" if problems == 0 else f"\n{problems} problem(s)")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("stats")
    s.add_argument("--hotcache", action="store_true")
    s.set_defaults(func=cmd_stats)

    s = sub.add_parser("related")
    s.add_argument("terms", nargs="+")
    s.add_argument("-n", type=int, default=20)
    s.set_defaults(func=cmd_related)

    s = sub.add_parser("index-set")
    s.add_argument("slug", nargs="?")
    s.add_argument("desc", nargs="*")
    s.add_argument("--end", action="store_true")
    s.set_defaults(func=cmd_index_set)

    s = sub.add_parser("log-append")
    s.set_defaults(func=cmd_log_append)

    s = sub.add_parser("check")
    s.add_argument("--changed", action="store_true")
    s.set_defaults(func=cmd_check)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
