---
title: "Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6"
source: "https://x.com/akshay_pachaar/status/2045910818450182526"
author:
  - "[[@akshay_pachaar]]"
published: 2026-04-20
created: 2026-04-20
description: "How the new xhigh effort level, adaptive thinking, and 1M context window change how you should prompt, delegate, and manage sessions with Cl..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HGSMrYgaAAAtzp_?format=jpg&name=large)

How the new **xhigh** effort level, **adaptive thinking**, and **1M context** window change how you should prompt, delegate, and manage sessions with Claude's strongest model.

You just upgraded to Claude Opus 4.7. Your prompts are the same. Your harness is the same.

But your token bill doubled, and your code review recall dropped. What happened?

Opus 4.7 is not a drop-in replacement for 4.6. It thinks differently, follows instructions more literally, spawns fewer subagents, and reasons more aggressively after every user turn.

The patterns that worked before now cost you tokens without proportional quality gains. The fix is not complicated, but it requires understanding what changed and adjusting your workflow accordingly.

Let's walk through it.

# The Delegation Mindset

The single biggest shift with Opus 4.7 is how you frame your role. Treat Claude like a capable engineer you delegate to, not a pair programmer you guide line by line.

Every user turn in an interactive session triggers reasoning overhead. With 4.6, you could spread instructions across multiple turns without much penalty.

With 4.7, that pattern inflates token usage because the model reasons deeply after each message you send. You pay for reasoning on every turn, whether the turn deserves it or not.

Three concrete changes will fix this.

- First, specify the task upfront in the first turn. Include intent, constraints, acceptance criteria, and relevant file paths. Ambiguous prompts spread across many turns reduce both token efficiency and output quality.
- Second, batch your questions. Every user message adds reasoning overhead, so give the model enough context to keep moving without checking in.
- Third, use auto mode for trusted tasks. For long-running work where you've already provided full context, [auto mode](https://code.claude.com/docs/en/permission-modes#available-modes) (Shift+Tab) cuts cycle time by removing unnecessary check-ins. It's available in research preview for Claude Code Max users.

You can also ask Claude to play a sound when it finishes a task. It will create its own hook-based notifications, so you don't have to watch it work.

![Image](https://pbs.twimg.com/media/HGQ7xuBagAAJyjW?format=jpg&name=large)

# The 5 Effort Levels and Why xhigh Is the New Default

Opus 4.7 introduces **xhigh**, a new effort level between high and max. It's now the default for Claude Code.

If you're an existing user who never manually set your effort level, you've been auto-upgraded to xhigh.

Here's how the five tiers break down.

- **low** is for latency-sensitive, tightly scoped work. The model won't go above and beyond, but it still outperforms Opus 4.6 at the same effort level.
- **medium** fits cost-sensitive tasks where you're willing to trade intelligence for speed.
- **high** balances intelligence and cost. It's a good pick for concurrent sessions or budget-conscious work without a large quality drop.
- **xhigh** is the default and the sweet spot for coding and agentic tasks. You get strong autonomy and intelligence without the runaway token usage that max can produce.
- **max** squeezes out extra performance on genuinely hard problems, but with diminishing returns. It's more prone to overthinking, so use it deliberately for eval ceiling testing or extremely intelligence-sensitive work.

> One practical tip: you can toggle effort mid-task. Start at xhigh for the complex design phase, drop to high for straightforward implementation, and bump to max for a tricky debugging session. This gives you fine-grained control over token spend.

Opus 4.7 respects effort levels more strictly than 4.6, so if a task at low or medium feels under-thought, raise the effort instead of prompting around it.

![Image](https://pbs.twimg.com/media/HGQ80yKbQAArzVt?format=jpg&name=large)

# Adaptive Thinking Replaces Fixed Budgets

If you were using Extended Thinking with budget\_tokens on Opus 4.6, that's gone. Opus 4.7 uses adaptive thinking instead.

The difference matters. With fixed budgets, you allocated a set number of thinking tokens upfront, and the model used them whether it needed to or not.

With adaptive thinking, the model decides when and how much to think at each step.

Simple queries get fast responses, complex reasoning steps get deep thought, and steps that don't benefit from thinking skip it entirely.

Over a long agentic run, this adds up to faster responses and lower token usage compared to a blanket thinking budget.

The migration is straightforward:

```python
# Before (Opus 4.6 with extended thinking)
client.messages.create(
    model="claude-opus-4-6",
    max_tokens=64000,
    thinking={"type": "enabled", "budget_tokens": 32000},
    messages=[{"role": "user", "content": "..."}],
)

# After (Opus 4.7 with adaptive thinking)
client.messages.create(
    model="claude-opus-4-7",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "xhigh"},
    messages=[{"role": "user", "content": "..."}],
)
```

You can still steer the thinking rate with prompts. To get more thinking, try something like "Think carefully and step-by-step before responding; this problem is harder than it looks."

To get less thinking, use "Prioritize responding quickly rather than thinking deeply. When in doubt, respond directly."

If you're running at max or xhigh effort, set a large max output token budget (start at 64k) so the model has room to think and act across subagents and tool calls.

![Image](https://pbs.twimg.com/media/HGRfzEdaIAAdPTz?format=jpg&name=large)

# Behavior Changes That Will Bite You

Opus 4.7 ships with several default behavior changes that will catch you off guard if you've tuned your prompts or harnesses for 4.6. Let's go through them.

## Response length

Opus 4.7 calibrates response length to task complexity. Simple lookups get short answers, open-ended analysis gets long ones.

If your use case depends on a specific length or style, state it explicitly. Positive examples of the voice you want work better than negative "don't do this" instructions.

## Fewer tool calls

The model calls tools less often and reasons more. This produces better results in many cases.

But if you need more aggressive tool use for search or file reading, provide explicit guidance about when and why tools should be used. Raising effort to high or xhigh also increases tool usage.

## Fewer subagents

Opus 4.7 is more judicious about delegating to subagents. If your workflow benefits from parallel fan-out, spell it out clearly:

> "Do not spawn a subagent for work you can complete directly in a single response. Spawn multiple subagents in the same turn when fanning out across items or reading multiple files."

## More literal instruction following

This is the change most likely to break existing setups. Opus 4.7 interprets prompts more literally, especially at lower effort levels.

It won't silently generalize an instruction from one item to another, and it won't infer requests you didn't make. The upside is precision and less thrash.

The downside is that if you need an instruction applied broadly, you must state the scope explicitly. For example: "Apply this formatting to every section, not just the first one."

## Tone shift

Opus 4.7 is more direct and opinionated, with less validation-forward phrasing and fewer emoji than 4.6's warmer style. If your product relies on a specific voice, re-evaluate your style prompts against the new baseline.

## Code Review

Opus 4.7 is meaningfully better at finding bugs. It shows 11 percentage points better recall on Anthropic's hardest bug-finding eval based on real PRs, with higher precision too.

But here's the catch. If your review harness says "only report high-severity issues" or "be conservative," Opus 4.7 follows that instruction more faithfully than 4.6 did.

It may investigate code just as thoroughly, identify bugs, then not report findings it judges below your stated bar. Precision rises, but measured recall drops.

The fix is to separate finding from filtering:

> Report every issue you find, including ones you are uncertain about or consider low-severity. Do not filter for importance or confidence at this stage. Your goal here is coverage: it is better to surface a finding that later gets filtered out than to silently drop a real bug. For each finding, include your confidence level and an estimated severity so a downstream filter can rank them.

If you need single-pass filtering, be concrete about where the bar is rather than using qualitative terms. For example: "Report any bugs that could cause incorrect behavior, a test failure, or a misleading result; only omit pure style or naming preferences."

# Session Management with 1M Context

Claude Code now has a 1 million token context window. That's enough to build a full-stack app from scratch in a single session.

But more context doesn't always mean better results. Context rot is real.

As the context grows, attention spreads across more tokens. Older, irrelevant content starts to distract from the current task, and the model gets less intelligent as its context window fills up.

Lost in the middle effect:

![Image](https://pbs.twimg.com/media/HGRhSkgakAED0Md?format=jpg&name=large)

You have five options at every turn.

- **Continue** means sending another message. Use this when everything in the window is still relevant.
- **Rewind** (double-Esc) jumps you back to a previous message to re-prompt from there. Failed attempts get dropped from context, which is often better than typing "that didn't work, try X instead," because you keep the useful file reads while dropping the failed approach.
- **/compact** with a hint summarizes the session and keeps going. It's lossy but low effort, and you can steer it with instructions like /compact focus on the auth refactor, drop the test debugging.
- **/clear** starts a fresh session. You write down what matters yourself, giving you zero rot and full control.
- **Subagents** delegate work that generates lots of intermediate output. The subagent gets its own fresh context window, and only the final result comes back.

![Image](https://pbs.twimg.com/media/HGRhvG0agAAyH1d?format=jpg&name=large)

The mental test is simple: will you need the tool output again, or just the conclusion? If just the conclusion, use a subagent.

# What causes bad auto-compaction

Auto-compaction fires when you're nearing the context limit. The problem is that this is exactly when the model is at its least intelligent point due to context rot.

A common failure looks like this: autocompact fires after a long debugging session and summarizes the investigation. Your next message references something that was dropped from the summary.

With one million context, you have more time to **compact proactively** with a description of what matters. Don't wait for auto-compaction to kick in.

# Prompting Techniques That Still Matter

Several foundational prompting techniques remain effective with Opus 4.7, and you shouldn't abandon them just because the model is smarter.

- Use XML tags to structure complex prompts. Wrap instructions, context, examples, and inputs in their own tags (<instructions>, <context>, <input>) to reduce misinterpretation.
- Give Claude a role in the system prompt. Even a single sentence focuses behavior and tone.
- Use 3-5 examples wrapped in <example> tags, covering edge cases and varying enough that the model doesn't pick up unintended patterns.
- Put longform data at the top of your prompt, above your query. Queries at the end can improve response quality by up to 30% on complex, multi-document inputs.
- Ground responses in quotes. For long document tasks, ask Claude to quote relevant parts before carrying out its task.

# Controlling tool use

Opus 4.7 calls tools less frequently by default. To increase tool use, raise effort or add explicit guidance: "Use \[tool\] when it would enhance your understanding of the problem."

Parallel tool calling is a strength worth leaning into. The model will run multiple searches, read several files at once, and execute bash commands in parallel.

You can boost parallel execution to near 100% with explicit guidance in XML tags.

# Overthinking mitigation

At higher effort levels, Opus 4.7 can think extensively, inflating thinking tokens. Add this prompt to keep it focused:

> "When you're deciding how to approach a problem, choose an approach and commit to it. Avoid revisiting decisions unless you encounter new information that directly contradicts your reasoning."

# Agentic Systems: State, Safety, and Multi-Window Workflows

For long-horizon agentic work, Opus 4.7 excels at state tracking across extended sessions. A few patterns make it even more effective.

**Multi-context window workflows** let you use the first context window to set up a framework (write tests, create setup scripts), then use future windows to iterate on a todo list. Have the model create tests in a structured format like tests.json and setup scripts like [init.sh](https://init.sh/) so fresh context windows can pick up where the last one left off.

**State management** works best when you match the format to the data. Use JSON for structured data like test results and task status, freeform text for progress notes, and git for checkpoints that can be restored.

**Balancing autonomy and safety** requires some guidance. Without it, Opus 4.7 may take actions that are hard to reverse, like deleting files or force-pushing.

Add a reversibility prompt to keep it in check:

> "You are encouraged to take local, reversible actions like editing files or running tests, but for actions that are hard to reverse or affect shared systems, ask the user before proceeding."

**Reducing overengineering** is also worth doing explicitly. Opus 4.7 can create extra files, add unnecessary abstractions, or build flexibility that wasn't requested.

Add guidance like: "Only make changes that are directly requested or clearly necessary. A bug fix doesn't need surrounding code cleaned up."

**Minimizing hallucinations** comes down to forcing investigation before answering: "Never speculate about code you have not opened. If the user references a specific file, you MUST read the file before answering."

![Image](https://pbs.twimg.com/media/HGRjMIPa4AEloYp?format=jpg&name=large)

# Migration Checklist

If you're moving from Opus 4.6 to 4.7, here's what to update.

1. Switch to adaptive thinking by replacing thinking: {type: "enabled", budget\_tokens: N} with thinking: {type: "adaptive"}.
2. Set effort to xhigh, which is the new default for coding work, and set max output tokens to 64k at xhigh or max effort.
3. Update code review prompts to separate finding from filtering so you preserve recall.
4. Reduce user turns by front-loading context into the first message, and add explicit subagent guidance so the model knows when to fan out.
5. Specify design preferences concretely rather than relying on generic instructions to override the house style.
6. Migrate away from prefilled responses. Starting with Claude 4.6 models, prefilled responses on the last assistant turn are deprecated, and on Mythos Preview they return a 400 error.

# Computer use

Computer use works across resolutions up to a new maximum of 2576px or 3.75MP. Sending images at 1080p provides the best balance of performance and cost.

For cost-sensitive workloads, 720p or 1366x768 are strong lower-cost options.

# The Bottom Line

Opus 4.7 rewards upfront specification and punishes incremental, multi-turn prompting. The model is more capable, more literal, and more autonomous than 4.6.

Give it a well-specified task, set effort to xhigh, and let it run. The developers who will get the most out of this model are the ones who stop guiding it step by step and start delegating like they would to a senior engineer.

Try this today: take your next coding task, write a single detailed prompt with intent, constraints, and acceptance criteria, and send it in one turn at xhigh. Compare the result and token usage to your old multi-turn pattern.

The difference will speak for itself.

**References:**

- [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)
- [https://x.com/trq212/status/2044548257058328723?s=20](https://x.com/trq212/status/2044548257058328723?s=20)

That's a wrap!

If you enjoyed reading this:

Find me →[@akshay\_pachaar](https://x.com/@akshay_pachaar) ✔️

Every day, I share tutorials and insights on AI, Machine Learning, and vibe coding best practices.