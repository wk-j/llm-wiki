---
title: Context Rot
type: concept
tags: [ai, context-management, claude-code, performance]
created: 2026-04-16
updated: 2026-06-29
sources: [Using Claude Code Session Management & 1M Context.md, Agent Harness Engineering.md, "New Skills! handoff, prototype, review and writing-*  Skills Changelog.md", matt-pocock-dumb-zone-compaction.md]
---

# Context Rot / Context เน่า

ข้อสังเกตที่ว่า **คุณภาพของ output จาก LLM จะลดลงเมื่อ context window ใกล้จะเต็ม** เมื่อมี token สะสมมากขึ้น, attention จะกระจายไปบนพื้นที่ที่ใหญ่ขึ้น; เนื้อหาที่เก่าและไม่เกี่ยวข้องจะรบกวนงานปัจจุบันและลดคุณภาพการให้เหตุผลที่มีประสิทธิภาพลง

## ลักษณะ

- **ค่อยเป็นค่อยไป, ไม่ใช่ทันที** การเน่าจะเริ่มก่อนถึงขีดจำกัดของ context นาน
- **ขึ้นอยู่กับงาน** งานดึงข้อมูลแบบง่ายๆ จะทนต่อ context ที่ยาวได้ดีกว่างานที่ต้องใช้เหตุผลหนักๆ
- **สำหรับโมเดล context 1M ของ [[claude-code|Claude Code]]:** จะเริ่มเห็นได้ชัดเจนที่ประมาณ 300k–400k tokens (เกณฑ์ที่ [[anthropic|Anthropic]] สังเกตเห็น) แต่ก็ไม่ใช่กฎที่ตายตัว

## ทำไมถึงสำคัญต่อการออกแบบ session

Context rot คือต้นทุนที่ซ่อนอยู่ของ session ที่ยาวนาน แม้ว่า session จะยังคงใช้งานได้ในทางเทคนิค (ยังมี token เหลือ), แต่โมเดลจะมีความสามารถลดลงเรื่อยๆ นี่คือเหตุผลที่เทคนิคการจัดการ session ([[compaction]], /rewind, subagents) มีอยู่ — ไม่ใช่แค่เพื่อหลีกเลี่ยงการชนขีดจำกัด, แต่เพื่อทำให้ active context *มีประโยชน์*อยู่เสมอ

โมเดลยังอยู่ใน **จุดที่ฉลาดน้อยที่สุด** เมื่อ autocompact ทำงาน (เพราะ context rot อยู่ในจุดที่แย่ที่สุด) สิ่งนี้ทำให้การทำ manual compaction เชิงรุก — พร้อมการชี้นำที่ชัดเจน — น่าเชื่อถือกว่าการปล่อยให้ autocompact ทำงานเอง

[[matt-pocock|Matt Pocock]] เรียกช่วงนี้แบบใช้งานจริงว่า [[dumb-zone|dumb zone]]: จุดที่ agent ยังมี context เหลือ แต่เริ่มทำเรื่องโง่เพราะ active context ปนเปื้อน. pattern `/rewind` + `/compact` ช่วยแยกให้เห็นว่า failure บางส่วนไม่ได้มาจาก model ไม่รู้เรื่อง แต่เกิดจาก transcript ที่พา model กลับไปทางผิด.

## วิธีบรรเทา

| เทคนิค | ช่วยได้อย่างไร |
|---|---|
| **/rewind** | ทิ้งความพยายามที่ล้มเหลวออกจาก context ทันที แทนที่จะสะสมไว้ |
| **/compact** (เชิงรุก) | ลดน้ำหนักก่อนที่การเน่าจะถึงจุดสูงสุด; ชี้นำบทสรุป |
| **/clear + new session** | รีเซ็ตทั้งหมด; มนุษย์เขียน brief ที่โฟกัส |
| **[[agent-handoff-documents|Handoff document]]** | เปิด session ใหม่พร้อม brief ที่เก็บ context, intent, artifact paths, และ skill ถัดไป |
| **Subagents** | งานระหว่างทางจะอยู่ใน context ใหม่; มีเพียงผลลัพธ์ที่กลับมายัง parent |
| **New session per task** | ป้องกันไม่ให้การเน่าสะสมข้ามงานที่ไม่เกี่ยวข้องกัน |

[[agent-harness-engineering]] เพิ่มเทคนิคที่อยู่ระดับ harness: **tool-call offloading**. ถ้า tool output ใหญ่มาก เช่น log ยาวหลายพันบรรทัด ให้เก็บผลเต็มไว้ใน filesystem แล้วส่งเฉพาะส่วนที่จำเป็นกลับเข้า context. วิธีนี้ต่างจาก compaction เพราะไม่ได้สรุปประวัติ chat แต่ลดปริมาณ output ดิบที่ไหลเข้า context ตั้งแต่แรก

## ดูเพิ่ม

- [[dumb-zone]]
- [[compaction]]
- [[claude-code-session-management]]
- [[claude-code]]
- [[ai-orchestrator]]
- [[agent-harness-engineering]]
- [[agent-handoff-documents]]
