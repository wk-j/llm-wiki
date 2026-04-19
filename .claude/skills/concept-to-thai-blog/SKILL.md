---
name: concept-to-thai-blog
description: Convert a wiki concept page (wiki/concepts/*.md) into a Medium-style Thai blog post. Use when the user asks to "summarize concept as blog", "write blog post from concept", "Medium style Thai", or passes a concept filename and asks for a blog version.
---

# Concept → Thai Blog Post

Turn a `wiki/concepts/*.md` page into a Medium-style blog post in Thai. Output **explicit markdown syntax** (raw markdown, not rendered) so the user can paste it anywhere.

## Inputs

- The concept page path (e.g. `wiki/concepts/delegation-mindset.md`). If the user doesn't specify, ask which concept.
- Read the full concept page before writing. Also read any `[[wikilinked]]` concept/source pages referenced in the main argument — they usually contain the framing you need.

## Output format

Print the blog post to chat as a single fenced markdown block is **wrong** — print it as raw markdown directly, with these elements:

- `# Title` — hook title in Thai, punchy, Medium-style. Not a literal translation of the concept title.
- `*italic subtitle*` — one-line deck under the title, sets the promise.
- `---` separator after the deck.
- `## H2` section headings in Thai, spoken register.
- `### H3` for sub-points inside a section when the section has 2+ moves/steps.
- `> blockquote` for primary-source quotes. Keep the original-language quote verbatim inside the `>`. If it's English, add a Thai gloss as a plain paragraph right below the quote (not inside the `>`).
- `**bold**` for the single most important phrase per section — not for decoration.
- `- bulleted lists` for enumerations (criteria, steps, caveats). Keep bullets short; one line each where possible.
- Inline `code` for: product names used as identifiers (`max_tokens`), CLI flags (`--dangerously-skip-permissions`), keybindings (`Shift+Tab`), file paths.
- `---` separator before the closing sign-off paragraph.

Do **not** use:
- Emoji (unless the user asks).
- `[[wikilinks]]` — this is a blog post, not a wiki page. Strip them to plain text or drop the link entirely.
- Frontmatter.
- "TL;DR" boxes or other Medium UI chrome.

## Writing style (Thai-primary, anti-translationese)

This is the hardest part. The blog must sound like a Thai developer wrote it, not like an English post run through a translator. A failed draft reads fine to an English speaker and stilted to a Thai one.

Rules:

- **Read every paragraph aloud in your head before shipping.** If it sounds like a UI string or a textbook, rewrite it.
- **Don't translate English idioms word-by-word.** Examples of traps:
  - "reward X" → `ให้รางวัล X` ❌ → `ได้คะแนนกว่า` / `คุ้มกว่า` ✅
  - "by default" → `โดยค่าเริ่มต้น` ❌ → `ปกติ` / `เป็นปกติ` / `ก่อน` ✅
  - "built for X" → `ถูกสร้างมาเพื่อ X` ❌ (English passive) → `ถนัด X` / `ออกแบบมาให้ X` ✅
  - "silently doubling your bill" → `คูณบิลแบบเงียบ ๆ` ❌ → `ทำให้บิลพุ่งโดยที่เราไม่รู้ตัว` ✅
- **Don't use borrowed English words as Thai verbs.** Keep the English noun; use a Thai verb around it. Say `จัดการ error` not `handle error` in prose. Say `กระตุ้น event` not `trigger event`.
- **Use classifiers with English nouns** where it reads naturally: `ตัว model`, `ตัว agent`, `ตัว endpoint`.
- **Prefer spoken connectors over formal ones:** `พอ...ก็`, `กลับ...`, `เลย...`, `แต่...`, `ตรงนี้`, `ตรงที่`. Avoid `ซึ่ง` and `ที่ซึ่ง` unless nothing spoken fits.
- **Break long English compound sentences into short Thai ones.** A 40-word English sentence usually becomes 2–3 Thai sentences. Thai prose doesn't chain clauses with commas the way English does.
- **Trust the reader.** Thai tech readers are fine with embedded English technical terms. They're not fine with stilted grammar. Keep the terms, fix the grammar.
- **Loanwords when they're what Thai devs actually say:** `upgrade`, `bug`, `commit`, `merge`, `deploy`, `log`, `pipeline`. Don't force Thai equivalents nobody uses.

## Structure

Medium-style, not wiki-style. Order:

1. **Hook** — the specific problem or surprising claim. Concrete situation, not an abstract intro. E.g. "บิล token พุ่งเป็นเท่าตัวหลัง upgrade".
2. **Why the old mental model fails** — one section showing the old assumption breaking on concrete evidence.
3. **The reframe** — name the new way of thinking. A primary-source quote lands well here if the concept page has one.
4. **Moves / mechanics** — the actionable "how". 2–4 sub-points with `###` headings if there are multiple; otherwise inline.
5. **Payoff** — one short section on what the reader gets if they adopt it. Drawn from the concept page's "ได้อะไร" / "ผลคือ" line if present.
6. **When not to use it** — every good Medium post has this. Pull from the concept page's caveats section.
7. **Sign-off** — one short `---`-separated paragraph restating the core switch in different words. Not a summary bullet list.

## What to drop from the concept page

Concept pages are reference docs. Blog posts are arguments. Ruthlessly cut:

- Section headings like "ความเชื่อมโยงกับแนวคิดอื่น" (cross-links to other wiki concepts). If a link is load-bearing, weave the idea into prose without linking.
- `See also` lists.
- Frontmatter.
- Wiki bookkeeping (`ที่มา: ...` pointing to a source page — keep the author's name inline, drop the link).

## What to add that the concept page doesn't have

- **A hook.** Concept pages open with a definition; blogs open with a problem.
- **Emotional register.** Blogs can say "เสียตังค์ที่สุด", "เลิก X เถอะ", "อย่าเพิ่งด่า model". Concept pages can't.
- **Direct address to the reader** (`เรา`, `คุณ`). Concept pages stay neutral.

## Length

Aim for 400–700 Thai words of prose (not counting code blocks). If the concept page is short, keep the blog short. Don't pad.

## Handoff

After writing, ask the user if they want the draft saved somewhere (e.g. `wiki/analysis/` or a separate `drafts/` folder). Don't save it proactively — blog drafts aren't wiki content.
