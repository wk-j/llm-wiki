---
title: Task Budgets
type: concept
tags: [ai, claude, anthropic, api, cost-optimization, agents]
created: 2026-04-19
updated: 2026-04-19
sources: [Whats new in Claude Opus 4.7 - Anthropic Docs.md]
---

# Task Budgets / Task Budget ของ Claude

**Task budget** คือ knob ใหม่ของ [[claude-opus-4-7|Opus 4.7]] ที่บอก model ว่า "งานนี้ตั้ง target ไว้ประมาณกี่ token ตลอด agentic loop" — ครอบคลุมทั้ง thinking, tool calls, tool results, และ final output รวมเป็นก้อนเดียว. Model เห็น countdown แบบ running เลย เอาไปใช้ตัดสินใจว่าจะเจาะลึกตรงไหน จะรีบปิดงานตอนไหน.

เป็น beta feature — ตอนใช้ต้องส่ง header `task-budgets-2026-03-13`.

## ใช้ยังไง

ใน Messages API, ใส่ field `task_budget` ใน `output_config`:

```python
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=128000,
    output_config={
        "effort": "high",
        "task_budget": {"type": "tokens", "total": 128000},
    },
    betas=["task-budgets-2026-03-13"],
    messages=[...],
)
```

Minimum = 20k tokens. ต่ำกว่านั้น model จะเริ่มตัดงานแบบไม่จบ หรือ refuse ไปเลย.

## `task_budget` ≠ `max_tokens`

ตรงนี้สำคัญมาก — คนที่มาจาก OpenAI/4.6 mindset มักสับสน:

| | `max_tokens` | `task_budget` |
|---|---|---|
| Model รู้ไหม | **ไม่** — เป็น hidden ceiling ฝั่ง API | **รู้** — model เห็น countdown |
| Scope | Per-request hard cap | ทั้ง agentic loop (หลาย turn รวมกัน) |
| ถ้าทะลุ | Truncate ตรงนั้นเลย | Model พยายามปิดงานให้จบก่อน |
| จุดประสงค์ | Hard ceiling กันบิลบาน | Advisory — ให้ model self-moderate |

พูดง่าย ๆ: `max_tokens` คือ fuse; `task_budget` คือ odometer ที่ model เห็นแล้ววางแผนได้.

## เมื่อไรควรตั้ง เมื่อไรไม่ควร

**ตั้ง** เมื่อ:
- งาน scoped ชัด เช่น "review PR นี้ภายใน 50k tokens"
- Pipeline ที่ budget ต่อ task ชัดเจน (เช่น agent ย่อยใน [[subagent-patterns|pipeline subagent]])
- อยากให้ model ทยอยสรุปเองพอใกล้หมด budget

**ไม่ตั้ง** เมื่อ:
- งาน open-ended ที่ quality สำคัญกว่า cost (เช่น refactor ใหญ่, deep research)
- ไม่รู้จริง ๆ ว่างานกินกี่ token — budget ที่คับเกินไปทำให้ model ทำงานผิว ๆ หรือ refuse

ผลคือ: `task_budget` ดีสำหรับ workload ที่ต้อง predictable spend; ปล่อยว่างสำหรับ workload ที่ต้อง predictable quality.

## ความสัมพันธ์กับ effort และ advisor

- [[effort-levels|Effort level]] คุม *intensity* ของการคิด; `task_budget` คุม *total spend*. ใช้คู่กันได้ — เช่น `effort: high` + `task_budget: 50k` = คิดเข้มข้นแต่ในงบที่กำหนด.
- ใน [[advisor-strategy|advisor strategy]] ที่ใช้ Opus เป็น judge ของ pipeline, `task_budget` เป็น lever ใหม่ที่ช่วย cap advisor-call cost โดยไม่ต้อง downgrade effort.

## See also

- [[claude-opus-4-7]]
- [[claude-opus-4-7-whats-new-docs]]
- [[effort-levels]]
- [[adaptive-thinking]]
- [[advisor-strategy]]
