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

## Thai-Primary Page Writing Style (Concepts, Entities, Analysis)

Concept, entity, and analysis pages are all written with Thai as the primary language. They are frequently cross-linked and should be written so a reader who hasn't seen the original source material can still follow along.

**Easy language.** Short sentences. Spoken register, not textbook. Prefer plain verbs over nominalizations. Name the thing before using an acronym. In Thai, this compounds with the translationese rule under `## Bilingual content` below.

**Enough context to stand alone.**

- Open each section with a plain-language sentence that says what the section is about and why it matters, before going into mechanics.
- The first time a term, person, tool, or acronym appears on the page, give a one-clause gloss inline — even when it's already a `[[wikilink]]`. The reader shouldn't need to click through to follow the paragraph. Example: `[[alex-ker|Alex Ker]] (engineer ที่เขียนเรื่อง harness optimization)` rather than just `[[alex-ker|Alex Ker]]`.
- Prefer concrete examples over abstract summary. "พอ alert ลั่น main agent คิดสมมติฐาน 3 ข้อ แล้วเปิด subagent ข้อละตัว" beats "main agent dispatches subagents for parallel investigation."
- Break compound English-structured sentences into shorter ones.
- At the end of each mechanics section, summarize the payoff in one line (`ได้อะไร` / `ผลคือ` / `Why this helps`). Don't make the reader derive it.

Source summaries (`wiki/sources/`) follow their own norms as they are direct summaries of a single document.

## Bilingual content (Thai + English)

**Per page type:**

- **Concept, Entity, and Analysis pages (`wiki/concepts/`, `wiki/entities/`, `wiki/analysis/`) — Thai is the primary body language.** Write narrative prose in Thai. Keep English for technical terms, proper nouns, product/tool/library names, and direct quotes from English sources. Use English glosses where they help anchor a concept.
- **Source summaries (`wiki/sources/`)** — default to English. Switch to Thai if the source is Thai, or the user asks for it.

**Always in English (tooling stability, all page types):**

- Filenames (`wiki/concepts/ai-3d-workflow.md`) — lowercase, hyphens
- Wikilink targets (`[[ai-3d-workflow]]`) — use alias for Thai display: `[[ai-3d-workflow|เวิร์กโฟลว์ AI + 3D]]` (inside tables, escape the pipe: `[[ai-3d-workflow\|เวิร์กโฟลว์ AI + 3D]]`)
- Frontmatter `title:` and `tags:`
- Entries in `wiki/index.md` (keeps the index scannable with `grep`)

**What counts as a "technical term" (stays English in Thai-primary body):**

- Product / tool / library / model names: `Blender`, `ComfyUI`, `Flux.1 Depth`, `Meshy`, `MCP`, `DLSS`, `Opus 4.7`
- Domain jargon with no established Thai rendering: `depth map`, `mesh`, `lookdev`, `block-in`, `text-to-image`, `render`, `pipeline`, `embedding`
- File extensions, CLI flags, code identifiers, API names

Thai transliterations (e.g. `เรนเดอร์`, `ไปป์ไลน์`) are fine when they read naturally; prefer whichever a Thai developer would actually say out loud.

**Body patterns:**

- **Bilingual H1** — `# AI + 3D Workflow / เวิร์กโฟลว์ AI + 3D` (English first aligns the H1 with the filename and frontmatter)
- **Thai section headings** when body is Thai-primary — e.g. `## แก่นความคิด`. Add a `/ English` suffix only where it aids navigation
- **Parenthetical gloss** on first mention — `block-in (วางโครง)` or `วางโครง (block-in)` depending on which language is primary
- **Inline gloss** after a key sentence when the other language captures it more crisply
- **Parallel prose** — a paragraph in the other language when one framing is stronger
- **Parallel table columns** (`| English | ไทย | Notes |`) — only when the table stays readable

**Write Thai that sounds spoken, not translated (avoid translationese):**

Thai-primary body should read like a Thai developer wrote it, not like an English page run through a translator. A useful test: read a paragraph aloud — if it sounds like a textbook or a UI string, rewrite it.

- **Don't translate English phrases word-by-word.** Prefer Thai-natural equivalents:
  - "by default" → `เป็นปกติ` / `ก่อน` (not `โดยค่าเริ่มต้น`)
  - "countermeasure pattern" → `วิธีแก้` (not `รูปแบบการแก้`)
  - "corrective principle" → `หลักแก้` (not `หลักการแก้ไข`)
  - "war story" → `เรื่องเล่าจากหน้างาน` (not literal translation)
  - "in narrow scope" → `ในงานตรงหน้า` / `ในเรื่องที่ทำอยู่` (not `ในขอบเขตแคบ`)
- **Don't use borrowed English words as Thai verbs.** Keep the loaned noun; use a Thai verb around it. Not `reward การตีความ` — say `ได้คะแนนมากกว่าถ้าเดาเลย`. Not `trigger event` — say `กระตุ้น/ทำให้เกิด event`. Not `handle error` in prose — say `จัดการ error`.
- **Use classifiers with English nouns** where natural: `ตัว Agent`, `ตัว model`, `ตัว endpoint` when referring to the thing itself.
- **Use Thai connectors that developers actually speak**: `พอ...ก็`, `กลับ...`, `เลย...`, `แต่...`, `ตรงนี้คือ`, `ตรงที่` — avoid formal relativization (`ซึ่ง`, `ที่ซึ่ง`) when a spoken connector fits.
- **Break long English-style compound sentences** into shorter Thai sentences. Thai prose usually doesn't chain clauses with commas the way English does. A 40-word English sentence often becomes two or three Thai sentences.
- **Reorder the sentence, don't just swap vocabulary.** Thai and English order words differently. A sentence can have perfectly Thai-native vocabulary and still read as translated because the *shape* is English. Fixing vocab is step one; restructuring the sentence is step two — equally important and easy to miss.
  - **Start with the actor/topic, not a long noun phrase.** English likes `"A heuristic from X proposing criteria for choosing model: ..."` Thai prefers `"X เสนอหลักเลือก model ว่า ..."` — actor first, verb follows quickly.
  - **Break nominalized subjects.** `"การจะได้งานที่ดีต้องมีสองอย่าง"` (noun-phrase subject, English-shaped) → `"จะให้งานออกมาดี ต้องมีสองอย่าง"` (verb-first, Thai-shaped).
  - **Prefer topic–comment over SVO clones.** Thai often names the topic, then comments on it: `"model ใหม่ที่ว่าแพง ไม่ได้แพงแค่ค่า token"` beats a direct `"ราคาของ model ใหม่ไม่ใช่แค่ค่า token"` mirror.
  - **Self-test by reading aloud.** If a Thai developer wouldn't say it that way in conversation, rewrite — even if every individual word is Thai-native.
- **Trust the reader.** Thai tech readers tolerate English technical terms embedded in Thai. What they don't tolerate is stilted grammar. Keep the terms, fix the grammar.

**Primary-source quotes:** keep verbatim in the source language and gloss alongside. Do not silently translate.

See `wiki/concepts/ai-3d-workflow.md` for a worked Thai-primary example.
