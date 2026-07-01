---
title: tmux
type: entity
tags: [terminal, developer-tools, workflow, agents]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# tmux

**tmux** คือ terminal multiplexer: โปรแกรมที่ให้แยก terminal เป็น pane/window หลายช่อง และ detach/reattach session เดิมได้. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow ของ Kun Chen]] tmux คือสิ่งที่ทำให้เขาคุม editor, shell, และ agent หลายตัวได้จาก keyboard อย่างเดียว.

จุดที่สำคัญกับ agent workflow คือ session อยู่ต่อได้แม้ disconnect. Kun สามารถออกจาก tmux แล้วกลับเข้ามาเจอสถานะเดิม หรือ connect จากเครื่องอื่น/โทรศัพท์ได้. พอจับกับ [[treehouse|Treehouse]] และ [[first-mate|First Mate]] tmux กลายเป็น surface สำหรับจัด agent sessions ขนานหลายสาย.

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[wezterm]]
- [[treehouse]]
- [[first-mate]]
- [[git-worktrees]]
