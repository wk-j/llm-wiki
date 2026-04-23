---
title: "How to Build a CLAUDE.md File That Makes Claude Code Actually Listen to You - FULL GUIDE"
source: "https://x.com/cyrilXBT/status/2046589854776009208"
author:
  - "[[@cyrilXBT]]"
published: 2026-04-21
created: 2026-04-22
description: "Most people using Claude Code are doing it wrong.They open a new project, start typing prompts, and wonder why Claude keeps forgetting the r..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HGYtGHKb0AAIRw3?format=jpg&name=large)

## Most people using Claude Code are doing it wrong.

They open a new project, start typing prompts, and wonder why Claude keeps forgetting the rules, ignoring their stack, or writing code that looks nothing like what they asked for. The problem is not Claude.

The problem is you never told Claude who you are, what you are building, or how you want it to behave.

That is what a CLAUDE.md file is for.

This is the single most underrated feature in Claude Code. Once you understand it, you will never go back to raw prompting. This guide covers everything: what a CLAUDE.md file is, why it matters, how to structure it, and the exact templates I use for my own projects.

Let us get into it.

![Image](https://pbs.twimg.com/media/HGZ7vuNb0AA-Qt8?format=jpg&name=large)

## What Is a CLAUDE.md File?

When you run Claude Code inside a project folder, it automatically looks for a file called CLAUDE.md in the root of that directory.

If it finds one, it reads the entire file before doing anything else.

Think of it as a persistent system prompt that travels with your project. Every time you start a session, Claude already knows:

- What the project is
- What stack you are using
- What coding conventions you follow
- What it should never do
- What your goals are

This is the difference between a junior dev who needs constant hand-holding and a senior dev who gets it from day one.

One file. Permanent context. Zero repeated instructions.

## Why Most People Skip This (And Why That Is Expensive)

Here is what happens when you do not use a CLAUDE.md file.

You spend the first 5 minutes of every session re-explaining your project. Claude writes code using the wrong framework. It uses naming conventions you hate. It adds comments you never asked for. It suggests packages you already decided against three weeks ago.

You correct it. It forgets. You correct it again.

That is not a productivity tool. That is a very fast typist who needs babysitting.

A CLAUDE.md file eliminates almost all of this. It is the difference between Claude acting like a first-day hire and Claude acting like someone who has been on your team for months.

The time investment to write a good CLAUDE.md is 20 to 30 minutes.

The time you get back is EVERY session after that.

## Where to Put the File

Claude Code checks for CLAUDE.md in three places:

1. **Project root** — The main one. Claude reads this at the start of every session inside that folder.
2. **Subdirectories** — If you have a monorepo, you can have a CLAUDE.md in each subfolder. Claude reads the relevant one based on where you are working.
3. **Your home directory** — A global ~/.claude/CLAUDE.md that applies to ALL your projects. Great for personal preferences that never change.

For most people, start with the project root. Add a global one once you know your permanent preferences.

## The Anatomy of a High-Performance CLAUDE.md

Here is the structure I use. Each section serves a specific purpose. Do not skip sections. Every missing piece is a gap where Claude will default to its own judgment.

1\. Project Overview

Start with a plain-English description of what the project is. One or two paragraphs. No fluff.

\## Project Overview This is a crypto signal bot dashboard built with Next.js and Tailwind. It scans 98 trading pairs every 58 seconds using RSI, MACD, and Bollinger Bands and displays live signals in a dark-mode UI. The target user is a retail crypto trader who wants clean, fast signals without noise. Speed and clarity are the two non-negotiable priorities.

Claude now knows the domain, the user, and the priorities. Every decision it makes will be filtered through this context.

2\. Tech Stack

Be explicit. List everything.

\## Tech Stack - Framework: Next.js 14 (App Router) - Styling: Tailwind CSS only — no CSS modules, no styled-components - Language: TypeScript strict mode - Database: Supabase (Postgres) - Auth: Supabase Auth - Deployment: Vercel - Package manager: pnpm - State: Zustand - Charts: Recharts

If you leave this out, Claude will make assumptions. Sometimes right. Often wrong.

3\. Coding Conventions

This is where most CLAUDE.md files fall short. You need to be specific about how you write code, not just what you use.

```text
## Coding Conventions

- Use named exports for all components — no default exports
- File names use kebab-case: signal-card.tsx, not SignalCard.tsx
- Component names use PascalCase
- All functions use arrow function syntax
- No var — only const and let
- Prefer early returns over nested conditionals
- Add JSDoc comments only for exported utility functions
- Never use any — always type explicitly
- Keep components under 150 lines — extract if larger
- Co-locate types with the file that uses them unless shared across 3+ files
```

This is the stuff Claude gets wrong constantly without guidance. Write it once. Never correct it again.

4\. What Claude Should NEVER Do

This section is underused and it is one of the most powerful.

```text
## Never Do This

- Never install a new package without asking me first
- Never rewrite a component I did not ask you to touch
- Never use useEffect for data fetching — use React Query
- Never add console.log statements to production code
- Never use inline styles
- Never suggest switching the framework or database
- Never add placeholder comments like "// TODO: implement this"
- Never use emojis in code comments
- Never wrap everything in a try/catch without telling me
```

Claude is helpful by nature. Sometimes TOO helpful. It will refactor things you did not ask it to refactor. It will add error handling you did not want. It will suggest a different approach mid-task.

The NEVER section puts hard stops on this behavior.

5\. File Structure

Show Claude how your project is organized.

```text
## File Structure

src/
  app/              # Next.js App Router pages
  components/       # Shared UI components
    ui/             # Primitive components (buttons, inputs, etc.)
    features/       # Feature-specific components
  lib/              # Utility functions and helpers
  hooks/            # Custom React hooks
  stores/           # Zustand stores
  types/            # Shared TypeScript types
  styles/           # Global styles only

Do not create new top-level folders without asking.
Do not put components in /app — only pages and layouts go there.
```

6\. Current Goals

This is the section most people forget. Tell Claude what you are actively working on RIGHT NOW.

```text
## Current Sprint Goals

- Build the signal card component with RSI, MACD, and BB indicators
- Connect to Supabase real-time for live updates
- Add a filter bar to sort signals by strength and timeframe
- Optimize for mobile — the dashboard must be fully usable on phone

Not working on authentication this sprint. Do not suggest auth-related changes.
```

This keeps Claude focused. Without it, Claude will happily solve problems you are not trying to solve right now.

7\. Context and Background

Add anything else Claude needs to know about the project history, decisions already made, or constraints.

```text
## Important Context

- We already tried using Socket.io for real-time — it caused memory leaks on Vercel.
  We switched to Supabase real-time. Do not suggest Socket.io.
- The Binance API rate limit is 1200 requests per minute per IP.
  Always account for this when writing fetch logic.
- The bot currently runs on a $6/month VPS. Keep dependencies lean.
- This project started as a personal tool and is now a paid product on Gumroad.
  Code quality matters — this is not a throwaway script.
```

This section prevents Claude from suggesting things you already ruled out. It saves you from repeating yourself across sessions.

## A Full CLAUDE.md Template You Can Copy

Here is a complete template ready to customize for your own projects.

\# CLAUDE.md ## Project Overview \[Describe what the project does in 2 to 3 sentences. Who is it for? What problem does it solve?\] ## Tech Stack - Framework: \[e.g. Next.js 14 App Router\] - Styling: \[e.g. Tailwind CSS\] - Language: \[e.g. TypeScript\] - Database: \[e.g. Supabase\] - Auth: \[e.g. Supabase Auth\] - Deployment: \[e.g. Vercel\] - Package manager: \[e.g. pnpm\] - State management: \[e.g. Zustand\] ## Coding Conventions - \[List your naming conventions\] - \[List your syntax preferences\] - \[List your component structure rules\] - \[List your commenting rules\] - \[List your typing rules\] ## Never Do This - Never install packages without asking - Never rewrite files I did not ask you to touch - \[Add your specific restrictions\] ## File Structure \[Paste your directory tree here and annotate each folder\] ## Current Goals \[List what you are actively building this week or this sprint\] \[List what is explicitly OUT OF SCOPE right now\] ## Important Context \[Anything Claude needs to know about past decisions, constraints, or gotchas\] ## Communication Style - Be direct. Skip the preamble. - If you are unsure about something, ask before writing code. - When you make a change, tell me what you changed and why in one sentence. - Flag anything that looks like a potential bug or architectural issue, even if I did not ask.

## The Global CLAUDE.md: Your Personal Preferences Layer

Once you have used project-level CLAUDE.md files for a while, you will notice patterns. Conventions you want in EVERY project. Preferences that are just how you code.

That is what the global CLAUDE.md is for.

Create it here:

mkdir -p ~/.claude touch ~/.claude/CLAUDE.md

Then fill it with your universal preferences:

\# Global CLAUDE.md — Cyril's Defaults ## My Defaults Across All Projects - I prefer TypeScript over JavaScript always - I use pnpm as my package manager - I write arrow functions not function declarations - I prefer explicit types over inferred ones in function signatures - Keep responses concise — I do not need lengthy explanations unless I ask - If something I asked for is technically possible but a bad idea, tell me first ## Communication Rules - Do not start responses with "Great question" or "Certainly" - Be direct and skip filler sentences - When writing code, write the code first and explain after if needed - Do not suggest I read documentation unless you cannot answer the question ## Things I Never Want - Placeholder comments in code - Console.log in any code I will deploy - Unsolicited refactors of things I did not ask about - Default exports in React components

This runs in the background for every project. Combined with a project-level CLAUDE.md, Claude operates with two layers of context at all times.

## Advanced: Using CLAUDE.md for Non-Code Projects

CLAUDE.md is not just for code.

If you are using Claude Code for writing, research, or content workflows, you can use the same file to set behavioral rules for those contexts.

Here is an example for a content project:

\# CLAUDE.md — Content Operations ## Project Overview This folder contains my article pipeline for cyrilXBT. I write about AI tools, crypto trading, and productivity for solo builders. My audience is intermediate to advanced. They do not need hand-holding. ## Writing Style Rules - Write in first person - Use short punchy sentences - Avoid the word "utilize" — use "use" - Avoid "leverage" as a verb - No em dashes - No bullet points in articles unless it is a list that genuinely needs them - Capitalization is used for emotional emphasis — LIKE THIS — not randomly - Conversational but never casual to the point of being sloppy ## What I Never Want in My Articles - Phrases like "in today's fast-paced world" - Passive voice where active voice works - Filler intros that take more than 2 sentences to get to the point - Conclusions that just summarize what I already said ## Tone Direct. Opinionated. Personal. Written like someone who has actually done the thing. Not a tutorial robot. Not a corporate blog. A real person sharing what works.

Now Claude writes in your voice from the first sentence. Every time.

## Common Mistakes People Make With CLAUDE.md

**Mistake 1: Being too vague**

Bad: "Write clean code."

Good: "Use named exports, kebab-case file names, and no default exports."

Vague instructions are better than nothing but they still leave too much to interpretation. Be specific.

**Mistake 2: Writing it once and never updating it**

Your project evolves. Your CLAUDE.md should evolve with it. Any time you make a major architectural decision or rule out an approach, add it to the file.

I update mine at the end of every sprint.

**Mistake 3: Putting goals in instead of context**

Your CLAUDE.md is not a to-do list. It is a briefing document. Goals are fine in the Current Sprint section but the rest of the file should be stable context that does not change week to week.

**Mistake 4: Forgetting the NEVER section**

This is the most valuable section for experienced developers. You already know what you hate. Write it down. Claude will stop doing it.

**Mistake 5: Not having a global one**

If you are only using project-level files, you are re-writing the same preferences across every project. Spend 20 minutes on your global CLAUDE.md and you never have to write those preferences again.

## The Real Unlock: CLAUDE.md + Custom Commands

Once your CLAUDE.md is solid, the next level is combining it with Claude Code slash commands.

Claude Code lets you create custom commands in .claude/commands/ as markdown files. Each file becomes a reusable command you can call with /command-name.

For example, create .claude/commands/new-component.md:

Create a new React component with the following requirements: - TypeScript functional component - Named export only - Tailwind for styling - Props interface defined above the component - Place in src/components/features/ unless I specify otherwise - File name in kebab-case Ask me for the component name and purpose before writing anything.

Now type /new-component and Claude already knows the full spec.

Your CLAUDE.md handles the project-wide context.

Your slash commands handle the task-specific workflows.

Together they turn Claude Code into something that actually feels like a senior dev on your team.

## Final Thoughts

The developers getting the most out of Claude Code are not the ones with the cleverest prompts.

They are the ones who invested 30 minutes up front to write a CLAUDE.md that does the prompting for them.

Stop explaining yourself every session.

Write the file. Lock in the context. Let Claude work.

That is it.

If this helped you, follow me on X at [@cyrilXBT](https://x.com/@cyrilXBT). I post about building with AI, crypto, and how to actually use these tools to ship faster.