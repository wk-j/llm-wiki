# Second Brain — LLM Wiki Schema

**Start every session by reading `hotcache.md`.** It contains a summary of the current wiki state, recent activity, and key context — so you can act immediately without browsing files. Update `hotcache.md` at the end of every session or after significant changes (ingest, major query, lint).

This is a personal knowledge base maintained by an LLM. The human curates sources and asks questions. The LLM writes and maintains all wiki content.

## Directory structure

```
raw/          # Source documents (immutable — never modify)
wiki/         # LLM-generated markdown pages
wiki/index.md # Content index — catalog of all wiki pages
wiki/log.md   # Chronological log of operations
```

## Page types

**Source summaries** (`wiki/sources/`): One page per ingested source. Frontmatter includes title, url, date_ingested, tags. Body is a structured summary with key takeaways.

**Entity pages** (`wiki/entities/`): Pages about people, organizations, products, places — anything with a proper name that appears across multiple sources.

**Concept pages** (`wiki/concepts/`): Pages about ideas, frameworks, techniques, themes — abstract topics that span sources.

**Analysis pages** (`wiki/analysis/`): Pages generated from queries — comparisons, syntheses, explorations. Valuable answers that should persist rather than disappear into chat history.

## File naming

Lowercase, hyphens for spaces: `wiki/entities/alan-kay.md`, `wiki/concepts/spaced-repetition.md`.

## Page format

Every wiki page uses this template:

```markdown
---
title: Page Title
type: source | entity | concept | analysis
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [filename1.md, filename2.md]
---

# Page Title

Content here. Use [[wikilinks]] for cross-references to other wiki pages.

## See also

- [[Related Page]]
```

## Cross-referencing

Use Obsidian-style `[[wikilinks]]` for all internal links. When creating or updating a page, add links to related pages. When updating a page, check if other existing pages should link back to it.

## Operations

### Ingest

When the user adds a source to `raw/` and asks to ingest it:

1. Read the source document fully.
2. Discuss key takeaways with the user.
3. Create a source summary page in `wiki/sources/`.
4. Create or update entity pages for notable people, orgs, products mentioned.
5. Create or update concept pages for key ideas and themes.
6. Update `wiki/index.md` with new/changed pages.
7. Append an entry to `wiki/log.md`.

A single ingest may touch many wiki pages. That's expected.

### Query

When the user asks a question:

1. Read `wiki/index.md` to find relevant pages.
2. Read those pages.
3. Synthesize an answer with `[[wikilinks]]` to relevant pages.
4. If the answer is substantial and reusable, offer to save it as an analysis page.

### Lint

When the user asks to lint or health-check the wiki:

- Flag contradictions between pages.
- Find orphan pages (no inbound links).
- Find mentioned-but-missing pages (wikilinks that point to nonexistent files).
- Suggest new questions or sources to investigate.
- Check for stale information.

## Index format (wiki/index.md)

Organized by section. Each entry: `- [[Page Name]] — one-line description`.

```markdown
# Index

## Sources
- [[source-name]] — description

## Entities
- [[entity-name]] — description

## Concepts
- [[concept-name]] — description

## Analysis
- [[analysis-name]] — description
```

## Log format (wiki/log.md)

Append-only. Each entry:

```markdown
## [YYYY-MM-DD] operation | Title
Brief description of what was done and what pages were created/updated.
```

## Conventions

- The LLM never modifies files in `raw/`.
- The LLM owns everything in `wiki/`. The human reads it; the LLM writes it.
- Keep summaries concise but complete. Prefer structured sections over walls of text.
- When new information contradicts existing wiki content, note the contradiction explicitly and update the page with the current best understanding.
- Tags should be lowercase, general enough to cluster related pages (e.g. `psychology`, `productivity`, `ai`), but specific enough to be useful.
- In markdown **tables**, escape the `|` inside wikilink aliases as `\|` (e.g. `[[claude-code\|Claude Code]]`), or drop the alias entirely (`[[claude-code]]`). An unescaped pipe inside a table cell is parsed as a column separator and breaks the row.
