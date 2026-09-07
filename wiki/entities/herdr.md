---
title: Herdr
type: entity
tags: [ai, agents, terminal, developer-tools]
created: 2026-09-06
updated: 2026-09-07
sources: [dhh-ai-programming-setup-lex-clips.md, dhh-strategies-programming-with-ai-agents-lex-clips.md, "https://github.com/herdrdev/herdr"]
---

# Herdr / เครื่องมือคุม agent ใน terminal

Herdr เป็นเครื่องมือสำหรับจัดการ coding agent ใน terminal โดย [repository ของโครงการ](https://github.com/herdrdev/herdr) อธิบายว่าเป็น runtime ที่ agent ทำงานอยู่ภายใน

## บทบาทใน setup ของ DHH

[[dhh|DHH]] ผู้สร้าง Ruby on Rails เล่าใน [[dhh-ai-programming-setup-lex-clips|บทสัมภาษณ์กับ Lex Fridman]] ว่าเริ่มใช้ tmux เพื่อแบ่งหน้าจอเป็นหลายงาน แล้วเปลี่ยนมาใช้ Herdr เมื่อต้องตาม agent บนหลายเครื่อง เขาอธิบายสั้น ๆ ว่าเหมือน tmux ที่เพิ่มสถานะ agent และเสียงแจ้งเตือนเมื่องานเสร็จหรือต้องการคำตอบ

เขามี Herdr แยกบนแต่ละเครื่อง คลิปไม่ได้อธิบายว่ามี dashboard กลางหรือรวมงานข้ามเครื่องอย่างไร จึงไม่ถือว่า Herdr จัดการการรวม code ให้โดยอัตโนมัติ

ผลคือ คนตามจังหวะที่ต้องตัดสินใจได้ง่ายขึ้น แต่ยังมี [[attention-bottleneck|Attention Bottleneck]] หรือขีดจำกัดของสมาธิและเวลาที่คนมีให้แต่ละงาน

## ลงมาให้ในเครื่องเลย

ใน [[dhh-strategies-programming-with-ai-agents-lex-clips|คลิปอีกตอน]] DHH ไล่รายการโปรแกรมที่ [[omarchy|Omarchy]] ลงมาให้ตั้งแต่แรก แล้วมี Herdr อยู่ในนั้นคู่กับ Neovim, tmux, OBS และ Kdenlive

นี่เป็นตัวอย่างของ [[omakase-software|omakase]] ที่จับต้องได้ คนที่ลง Omarchy ได้เครื่องมือคุม agent มาพร้อมเครื่อง ไม่ต้องไปหาลงเอง

## See also

- [[dhh-ai-programming-setup-lex-clips]]
- [[dhh]]
- [[tailscale]]
- [[attention-bottleneck]]
- [[orchestration-tax]]
- [[omarchy]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
