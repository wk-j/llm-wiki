---
title: Thariq Shihipar
type: entity
tags: [ai, claude-code, anthropic, engineering, html]
created: 2026-05-25
updated: 2026-07-05
sources: [thariq-html-effectiveness.md, "Using Claude Code Session Management & 1M Context.md", a-field-guide-to-fable-finding-your-unknowns.md]
---

# Thariq Shihipar / Thariq Shihipar

[[thariq-shihipar|Thariq Shihipar]] (@trq212 บน X) คือ Member of Technical Staff ในทีม [[claude-code|Claude Code]] ที่ [[anthropic|Anthropic]] ใน wiki นี้เขาเป็นผู้เขียน 3 sources:

- [[thariq-html-effectiveness|Using Claude Code: The Unreasonable Effectiveness of HTML]] — ใช้ HTML แทน Markdown เป็น output format สำหรับ agent-human communication
- [[claude-code-session-management|Using Claude Code: Session Management & 1M Context]] — จัดการ session/context: context rot, rewind, compact, subagents
- [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable: Finding Your Unknowns]] — ทำงานกับ Claude [[fable|Fable]] 5 ผ่าน frame [[map-vs-territory|map vs territory]] และ [[unknowns-matrix|unknowns 4 ช่อง]]; เขาเป็นคนตัดต่อ launch video ของ Fable ด้วย Claude Code ทั้งตัว

## แนวคิดสำคัญ

Thariq เสนอว่าเมื่อ agent ทำงานซับซ้อนขึ้น Markdown เริ่มไม่พอ เพราะ spec, plan, report และ code review ยาวจนคนไม่อ่านจริง HTML จึงช่วยเพิ่ม [[html-artifacts|information density]], visual clarity, sharing และ interaction ได้ดีกว่า

แนวคิดของเขาไม่ได้หยุดที่เอกสารสวยขึ้น แต่ไปถึง [[custom-editing-interfaces|Custom Editing Interfaces]]: ให้ Claude Code สร้าง HTML editor เฉพาะกิจที่มนุษย์ปรับค่า ลากวาง เลือก option หรือ annotate แล้ว export ผลกลับไปเป็น prompt, JSON, Markdown หรือ diff

ใน field guide ปี 2026-07 เขาขยับขึ้นอีกชั้น: พอ model แรงถึงระดับ Fable 5 คอขวดของคุณภาพงานคือความสามารถของ *ผู้ใช้* ในการเคลียร์ unknowns ของตัวเอง — HTML artifacts, brainstorm, interview, reference, implementation notes และ quiz คือชุดเครื่องมือสำหรับหา unknowns ก่อน/ระหว่าง/หลังลงมือ. [[piyalitt-codex-keynote-attention-not-token|Piyalitt]] สรุป frame นี้เป็นภาษาไทยก่อนเข้า keynote Codex (2026-07) และเชื่อมกับ [[attention-bottleneck]] ว่าทักษะที่คุ้มลงทุนคือรู้จักสิ่งที่ยังไม่รู้

## ความเกี่ยวข้องใน wiki

มุมของ Thariq เชื่อมกับ [[interaction-productivity|Interaction Productivity]] เพราะ HTML artifact ที่ดีช่วยให้ความเข้าใจข้ามจาก agent ไปหามนุษย์และจากมนุษย์กลับเข้า agent ได้เร็วขึ้น เทคนิค interview ของเขาซ้อนทับกับ [[grill-me|Grill Me]] ของ Matt Pocock และ quiz pattern ของเขาเป็นคำตอบเชิงปฏิบัติต่อ [[comprehension-debt]]

## See also

- [[thariq-html-effectiveness]]
- [[claude-code-session-management]]
- [[field-guide-to-fable-finding-unknowns]]
- [[claude-code]]
- [[html-artifacts]]
- [[custom-editing-interfaces]]
- [[map-vs-territory]]
- [[unknowns-matrix]]
- [[piyalitt-codex-keynote-attention-not-token]]
