---
title: Kun Chen
type: entity
tags: [ai, agents, software-engineering, solo-builder]
created: 2026-06-16
updated: 2026-07-01
sources: [Agentic Code Review.md, l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Kun Chen

**Kun Chen** คืออดีต Meta L8 engineer ที่ [[addy-osmani|Addy Osmani]] ยกเป็นตัวอย่างสุดขั้วใน [[agentic-code-review|Agentic Code Review]]: solo builder ที่ใช้ agent 20-30 ตัวและ ship ประมาณ 40 PR ต่อวัน โดยแทบไม่ review code แบบ line-by-line.

สิ่งที่น่าสนใจไม่ใช่ "เลิก review แล้วรอด" แต่คือเขาย้ายงานมนุษย์ไปอยู่ก่อนโค้ดเกิด. เขาเขียน plan ละเอียดมาก ให้ agent ทำงานหลายชั่วโมงตาม plan และใช้ automated gate ชื่อ No Mistakes ตรวจงานก่อน merge. เขายังอยู่บน escalation เมื่อ agent ติด.

Addy ใช้ Kun เป็นตัวอย่างของบริบทเฉพาะ: solo builder, ไม่มีทีมใหญ่, ไม่มี legacy system หนัก, และ blast radius คนละแบบกับ enterprise. Copy workflow นี้ไปใส่ระบบใหญ่โดยไม่ปรับ risk tier จะกลายเป็นปัญหา review capacity ทันที.

ใน [[l8-principals-agentic-engineering-workflow-kun-chen|วิดีโอ walkthrough ของตัวเอง]] Kun ขยายภาพนี้จาก "คนที่ ship 40 PR/day" ให้เห็นเป็นระบบเต็ม. Stack ของเขาเริ่มจาก terminal-first setup ([[wezterm|WezTerm]] + [[tmux]] + [[neovim|Neovim]]) แล้วต่อด้วย memory files, skills, voice input ([[open-superwhisper|OpenSuperWhisper]]), agent-friendly tools ([[axi|AXI]]), planning artifact ([[lavish|Lavish]]), validation pipeline ([[no-mistakes|No Mistakes]]), long-running loop ([[good-night-have-fun|Good Night Have Fun]]), worktree manager ([[treehouse|Treehouse]]), และ meta-agent ([[first-mate|First Mate]]).

จุดที่ควรจำคือเขาไม่ได้ขายภาพ "เปิด agent เยอะแล้ว merge เลย". เขาเลื่อนงานคนไปไว้สองจุด: ตอนต้นเพื่อทำ requirement/planning ให้ชัด และตอนท้ายเพื่อใช้ judgement จาก evidence/risk. ตรงกลางปล่อย agent ทำงานยาวและตรวจตัวเองให้มากที่สุด.

## See also

- [[agentic-code-review]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[loop-engineering]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[first-mate]]
- [[no-mistakes]]
