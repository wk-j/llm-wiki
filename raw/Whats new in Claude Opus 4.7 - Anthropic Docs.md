# What's new in Claude Opus 4.7

Source: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7.md
Fetched: 2026-04-19

---

Overview of new features, breaking changes, and behavior changes in Claude Opus 4.7.

Claude Opus 4.7 is Anthropic's most capable generally available model to date. Highly autonomous; strong on long-horizon agentic work, knowledge work, vision, and memory.

## New model

| Model | API model ID | Description |
|:------|:-------------|:------------|
| Claude Opus 4.7 | `claude-opus-4-7` | Most capable GA model for complex reasoning and agentic coding |

Supports 1M token context window, 128k max output tokens, adaptive thinking, and same tools/platform features as Opus 4.6.

## New features

### High-resolution image support
- Max image resolution increased to 2576 px / 3.75 MP (from 1568 px / 1.15 MP).
- Coordinates now 1:1 with actual pixels (no scale-factor math).
- High-res images use more tokens; downsample if fidelity unnecessary.
- Also improved: low-level perception (pointing, measuring, counting), image localization (bounding boxes).

### New `xhigh` effort level
- Start with `xhigh` for coding/agentic; use minimum `high` for most intelligence-sensitive use cases.
- Messages API only; Claude Managed Agents handles effort automatically.

### Task budgets (beta)
- Advisory token target across the full agentic loop (thinking + tool calls + tool results + final output).
- Model sees a running countdown and prioritizes accordingly.
- Beta header: `task-budgets-2026-03-13`.
- Config: `output_config.task_budget = {"type": "tokens", "total": N}`.
- Minimum: 20k tokens.
- Not a hard cap — advisory, model-aware. Distinct from `max_tokens` (hard per-request cap, not shown to model).
- For open-ended quality-critical work, do not set a task budget.

Example:
```python
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=128000,
    output_config={
        "effort": "high",
        "task_budget": {"type": "tokens", "total": 128000},
    },
    messages=[...],
    betas=["task-budgets-2026-03-13"],
)
```

## Breaking changes (Messages API only; Managed Agents unaffected)

### Extended thinking budgets removed
- `thinking: {"type": "enabled", "budget_tokens": N}` → 400 error.
- Adaptive thinking is the only thinking-on mode; outperforms extended thinking in internal evals.
- Migration: replace with `thinking = {"type": "adaptive"}` + `output_config = {"effort": "high"}`.
- Adaptive thinking is OFF by default on 4.7. Must opt in explicitly.

### Sampling parameters removed
- Setting `temperature`, `top_p`, or `top_k` to any non-default value → 400 error.
- Migration: omit entirely; use prompting to guide behavior.
- `temperature=0` never guaranteed identical outputs anyway.

### Thinking content omitted by default
- Thinking blocks still appear in stream, but `thinking` field is empty unless caller opts in.
- Silent change; no error.
- Slight latency improvement.
- Opt-in: `thinking = {"type": "adaptive", "display": "summarized"}` (or "omitted" default).
- Note: if product streams reasoning to users, the new default appears as a long pause before output. Use `"display": "summarized"` to restore visible progress.

### Updated token counting
- New tokenizer contributes to improved performance.
- Same text uses roughly 1x–1.35x as many tokens (up to ~35% more, varies by content).
- `/v1/messages/count_tokens` returns different numbers than for 4.6.
- Recommendation: update `max_tokens` to give headroom, including compaction triggers.
- 1M context at standard API pricing; no long-context premium.

## Capability improvements

### Knowledge work
- .docx redlining and .pptx editing — better at producing/self-checking tracked changes and slide layouts.
- Charts and figure analysis — improved programmatic tool-calling with image-processing libs (e.g. PIL); pixel-level data transcription.
- Recommendation: if existing prompts have mitigations like "double-check the slide layout before returning", try removing and re-baselining.

### Memory
- Better at writing and using file-system-based memory.
- Agents with scratchpads, notes files, or structured memory stores should improve at jotting notes and leveraging them in future tasks.
- Client-side memory tool available for managed scratchpad.

### Vision
See High-resolution image support above.

## Behavior changes (not API breaking; may need prompt updates)

- More literal instruction following, particularly at lower effort levels. Won't silently generalize from one item to another or infer un-asked requests.
- Response length calibrates to perceived task complexity, not fixed verbosity.
- Fewer tool calls by default; uses reasoning more. Raising effort increases tool usage.
- More direct, opinionated tone; less validation-forward phrasing and fewer emoji than Opus 4.6.
- More regular progress updates during long agentic traces. If scaffolding forces interim status messages, try removing it.
- Fewer subagents spawned by default. Steerable through prompting.
- Real-time cybersecurity safeguards: prohibited/high-risk topic requests may be refused. Legitimate security work → Cyber Verification Program.

## Migration

See "Migrating to Claude Opus 4.7" doc. Claude API skill (Claude Code / Agent SDK) can apply migration steps automatically.
