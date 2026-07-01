---
title: Git Worktrees for Parallel Agents
type: concept
tags: [ai, agents, git, isolation, parallel, orchestration, worktree]
created: 2026-06-09
updated: 2026-07-01
sources: ["Loop Engineering..md", l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Git Worktrees for Parallel Agents / worktree สำหรับ agent ขนาน

**Git worktree คือ working directory แยกบน branch ของตัวเอง ที่แชร์ประวัติ repo เดียวกัน.** มันคือวิธีให้ coding agent หลายตัวทำงานขนานกันได้โดยไม่เหยียบไฟล์ของกันและกัน — เป็นหนึ่งในห้าชิ้นส่วนของ [[loop-engineering|loop engineering]] ตามที่ [[addy-osmani|Addy Osmani]] วางไว้ในบทความ [[loop-engineering-osmani|Loop Engineering]] (2026-06-09)

## ปัญหาที่มันแก้

พอรัน agent มากกว่าหนึ่งตัวบน checkout เดียวกัน ไฟล์เริ่มชนกัน. Addy อธิบายว่ามันคือ headache เดียวกับ engineer สองคน commit ทับบรรทัดเดียวกันโดยไม่คุยกันก่อน — แต่เกิดเร็วและถี่กว่ามากเพราะ agent ทำงานพร้อมกันหลายตัว

worktree แก้ตรงจุดนี้: แต่ละ agent ได้ directory + branch ของตัวเอง → **edit ของ agent ตัวหนึ่งแตะ checkout ของอีกตัวไม่ได้เลย** แม้จะเป็น repo เดียวกัน

## ทั้งสอง tool ทำยังไง

- **Codex** — build worktree support มาในตัว ให้หลาย thread ลุย repo เดียวกันพร้อมกันได้โดยไม่ชน
- **Claude Code** — ให้ isolation เดียวกันผ่าน:
  - `git worktree` (คำสั่ง git มาตรฐาน)
  - flag `--worktree` เปิด session ใน checkout ของตัวเอง
  - setting `isolation: worktree` ติดบน subagent → helper แต่ละตัวได้ checkout *สด* ที่ **ล้างตัวเองหลังเสร็จ**

## ข้อควรระวัง — worktree ไม่ได้เพิ่ม "เพดาน" ของเรา

จุดที่ Addy เน้น และเป็นเหตุผลที่ worktree ผูกตรงเข้ากับ [[orchestration-tax|orchestration tax]]:

> the worktrees take away the mechanical collision but YOU are still the ceiling, your review bandwith decides how many you can actually run, not the tool.
> (worktree เอา *การชนกันเชิงกลไก* ออกไปก็จริง แต่ **เพดานยังคือตัวเรา** — review bandwidth ของเราเป็นตัวกำหนดว่ารันได้กี่ตัวจริง ไม่ใช่ tool)

worktree แก้ปัญหา *ระดับไฟล์* (file-level collision) ได้ แต่ไม่ได้แก้ปัญหา *ระดับมนุษย์* — คนยังต้อง review + merge ทุก branch อยู่ดี และคนมีคนเดียว. เปิด worktree ได้ 20 อันไม่ได้แปลว่า ship ได้ 20 อัน

## ได้อะไร

worktree เอา friction เชิงกลไกของการรัน agent ขนานออกไป — แต่ต้องจับคู่กับวินัยฝั่ง [[orchestration-tax|review/merge]] เสมอ ไม่งั้นแค่ย้ายคอขวดจาก "ไฟล์ชนกัน" ไปเป็น "PR กองหน้าคนรีวิว"

## Treehouse: ลดหนี้จากการคุม worktree เอง

[[kun-chen|Kun Chen]] เพิ่มปัญหาอีกชั้นใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow walkthrough]]: git worktree แก้ file collision ได้ แต่สร้าง **worktree bookkeeping debt**. คนต้องตั้งชื่อ worktree, จำว่าอันไหนใช้ทำอะไร, จำว่ามี agent รันอยู่ไหม, และ cleanup เอง.

[[treehouse|Treehouse]] คือ tool ของเขาที่ทำให้เข้า repo แล้วได้ fresh worktree ทันที. พอปิด tab มันรู้ว่า worktree ว่างและ reuse ได้. `treehouse status` ใช้ดูว่าช่องไหนยัง active.

**ได้อะไร:** parallel agent workflow ต้องแก้ทั้ง collision ของไฟล์และ collision ในหัวคน. Worktree แก้ข้อแรก, Treehouse แก้ข้อสอง.

## See also

- [[loop-engineering]]
- [[loop-engineering-osmani]]
- [[orchestration-tax]]
- [[subagent-patterns]]
- [[addy-osmani]]
- [[cognitive-surrender]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[treehouse]]
