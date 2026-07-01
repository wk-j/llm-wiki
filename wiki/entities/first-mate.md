---
title: First Mate
type: entity
tags: [ai, agents, orchestration, meta-harness, workflow]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# First Mate

**First Mate** คือ meta-agent ของ [[kun-chen|Kun Chen]] ที่รับคำสั่งระดับสูงจากคน แล้วจัดการ agent sessions, worktrees, และ validation pipeline ให้. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|วิดีโอ workflow]] มันคือก้าวจาก "คุยกับ agent ทีละตัว" ไปเป็น "คุยกับผู้ช่วยที่คุม crew ให้".

ตัวอย่างในคลิปคือสั่งให้ทำงานเดียวกันข้ามสาม repo. First Mate แยกงานเป็นสาม task, เปิด tmux tabs, เรียก [[treehouse|Treehouse]] เพื่อสร้าง worktrees, รัน coding agents, แล้วใช้ [[no-mistakes|No Mistakes]] gate จนพร้อม PR. ระหว่างนั้นยัง triage issue ใหม่และเปิดงานเพิ่มได้.

First Mate จึงเป็น personal [[meta-harness|meta-harness]]: ไม่ได้แทน Claude Code/Codex/OpenCode แต่คุม workflow เหนือ harness เหล่านั้นอีกชั้น.

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[meta-harness]]
- [[treehouse]]
- [[no-mistakes]]
- [[tmux]]
- [[orchestration-tax]]
