---
title: Treehouse
type: entity
tags: [ai, agents, git, worktrees, workflow]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Treehouse

**Treehouse** คือ tool ของ [[kun-chen|Kun Chen]] สำหรับจัดการ git worktrees ให้ใช้กับ agent ขนานง่ายขึ้น. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|วิดีโอ workflow]] มันแก้ overhead ของการสร้าง worktree เอง: ตั้งชื่อ, จำว่าอันไหนทำอะไร, และ cleanup หลังเลิกใช้.

ผู้ใช้เข้า repo แล้วรัน `treehouse` เพื่อได้ fresh worktree ทันที. `treehouse status` แสดงว่า worktree ไหนใช้อยู่หรือ idle. เมื่อปิด tab แล้ว Treehouse รู้ว่า worktree ว่างและ reuse ได้ครั้งต่อไป.

**ได้อะไร:** [[git-worktrees|Git worktree]] แก้ file collision ระหว่าง agent. Treehouse แก้ memory/housekeeping cost ของมนุษย์ที่ต้องคุม worktree เหล่านั้น.

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[git-worktrees]]
- [[tmux]]
- [[first-mate]]
- [[orchestration-tax]]
