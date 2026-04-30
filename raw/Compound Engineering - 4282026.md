---
title: "Compound Engineering - 4/28/2026"
source: "https://x.com/trevin/status/2049199159073550790"
author:
  - "[[@trevin]]"
published: 2026-04-29
created: 2026-04-29
description: "We shipped v3.3.0. This release does 2 things: it makes the agent show its thinking before acting, and it interrupts you less while doing re..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HHA3llgbkAAOZbH?format=jpg&name=large)

We shipped [v3.3.0](https://github.com/EveryInc/compound-engineering-plugin). This release does 2 things: it makes the agent show its thinking before acting, and it interrupts you less while doing real work.

## Show me what you think I asked for, before you spend 10 minutes on it

> **"You keep using that word. I do not think it means what you think it means."**— Inigo Montoya, The Princess Bride

In an earlier version of **/ce-plan**, the skill could happily spend 5+ minutes producing a polished implementation plan built on one or two incorrect assumptions, and you'd have no idea. By the time the doc lands, those wrong assumptions are baked into a dozen places: painful to fix, and easy to miss entirely.

The marquee change lives in **/ce-brainstorm** and **/ce-plan**. Both skills now pause before doing real work and play back what they heard you ask for. Tell **/ce-plan** to "add OAuth login to the mobile app," and the skill comes back with three short lists:

1. what you literally said (Stated)
2. what it's quietly assuming you also want (Inferred: Google and GitHub providers, a callback handler, user-table changes)
3. what it's deliberately leaving alone (Out-of-scope: existing email login, two-factor).

You scan the bullets, correct the misreads in chat, and the skill keeps going. The cost of catching scope drift drops from "rerun the whole skill" to "edit a bullet."

The same shift shows up in **/ce-ideate**, where it used to chase the wrong interpretation on minimal prompts. The skill now figures out when to ask scoping questions up front, and tags every surviving idea with its grounding: direct evidence in your code, external prior art, or reasoned argument. The goal is to push the agent to be specifically wrong or specifically right. Less hedging, no speculation without a basis. ce-ideate is still one of my most used skills these days across my projects and this change has made it even better.

## Stop creating ceremony where the agent's judgment is good enough

A lot of recent work has been making the skills quieter, and making them better when they do need to interrupt you.

**/ce-doc-review** was relentless about asking for your input, even when there was only one obvious choice. It's now much better at applying fixes automatically and grouping related issues together, so the attention it does ask for goes toward decisions that genuinely need it.

**/ce-code-review** used to defer most fixable findings to your ticket tracker — also overboard in most cases. It now fixes more of them automatically, so you don't carry weight forward unnecessarily.

The goal of this release: make the agent cheaper to correct and faster to trust.

[https://github.com/EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)