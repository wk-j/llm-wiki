---
title: Amp
type: entity
tags: [product, ai, coding-agent, sourcegraph]
created: 2026-05-27
updated: 2026-05-27
sources: [software-after-software.md]
---

# Amp

Coding agent ของ [[sourcegraph|Sourcegraph]] — เป็น flagship ผลิตภัณฑ์รุ่นใหม่ที่มาแทน Cody ในยุคที่ Sourcegraph เชื่อว่า "assistant sidebar is dead" และ agent ต้องทำงานแบบ run ยาว ไม่ใช่ตอบ chat ทีละ turn

## จุดยืน

Amp ออกแบบรอบความเชื่อใน manifesto [[software-after-software]] ของ [[thorsten-ball|Thorsten Ball]]:

- หน่วยของงานคือ **delegated task** ไม่ใช่ code ที่ต้องเขียน
- agent ต้อง run ได้แม้ไม่มีคนนั่งหน้าจอ
- "An agent forced to work like a human is a wasted agent" — Amp พยายามไม่บังคับให้ agent ทำงานแบบมนุษย์

จุดต่างจาก [[claude-code|Claude Code]] หรือ [[openai-codex|Codex]] คือมาจากบ้านที่ทำ code search ระดับ enterprise มาก่อน — context retrieval ของ codebase ใหญ่เป็น asset เดิมของบริษัท

## Amp Labs

[[amp-labs|Amp Labs]] คือหน่วย R&D แนวหน้าของ Amp ใช้สำหรับทดลอง pattern ใหม่ ๆ ของการทำงานแบบ agent-first และเป็นจุดที่ Sourcegraph อยากให้ลูกค้าระดับ enterprise มาตั้ง "[[frontier-camp|frontier camp]]" ในแบบของตัวเอง

## ดูเพิ่ม

- [[sourcegraph]]
- [[amp-labs]]
- [[thorsten-ball]]
- [[software-after-software]]
- [[claude-code]]
- [[opencode]]
- [[thclaws]]
