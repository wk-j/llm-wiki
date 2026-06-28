---
title: Agent Memory Types (Semantic / Episodic / Procedural)
type: concept
tags: [ai, agents, agent-memory, context-engineering, self-learning]
created: 2026-06-26
updated: 2026-06-26
sources: [Self Learning for Agents Clearly Explained.md]
---

# Agent Memory Types / memory ของ agent มี 3 ชนิด

พอ agent เก็บ memory เป็น text นอก model (ชั้น context ดู [[three-learning-layers]]) คำถามถัดมาคือ "เก็บ *อะไร*". [[ataiiam|@ataiiam]] ใน [[self-learning-for-agents-explained]] ยืม taxonomy จาก cognitive science มาแบ่ง memory เป็น 3 ชนิด — และจุดสำคัญคือ **agent ที่เก่งขึ้นเองต้องใช้สองชนิดหลัง แต่ setup ส่วนใหญ่มีแค่ชนิดแรก**.

ใช้ตัวอย่าง support agent ที่จ่าย refund ตลอด:

- **Semantic = ข้อเท็จจริง.** "ลูกค้ารายนี้ลิมิต refund $2,000" — ความรู้คงที่ ตอบคำถามว่า *อะไรเป็นจริง*
- **Episodic = ประสบการณ์ที่ผ่านมา.** "สัปดาห์ก่อน refund ของลูกค้ารายนี้เด้ง" — เหตุการณ์ที่เคยเกิด ตอบว่า *เคยเจออะไรมา*
- **Procedural = วิธีจัดการเคส.** "ลูกค้า loyal เกินลิมิตหลังพลาดซ้ำ ๆ → อนุมัติ" — pattern การลงมือ ตอบว่า *เคสแบบนี้ทำยังไง*

## ทำไม semantic อย่างเดียวไม่พอ

semantic memory เก็บข้อเท็จจริงนิ่ง ๆ — มีประโยชน์ แต่ไม่ทำให้ agent *เก่งขึ้น*. agent อ่าน "ลิมิต $2,000" ได้ทุกรอบ แต่มันไม่เคยเรียนว่า *ควรทำยังไง* เมื่อเจอเคสที่ลิมิตไม่ครอบคลุม.

การเรียนรู้จริงอยู่ที่ episodic + procedural:

- **episodic** ให้ agent อ้างอิงเคสที่เคยเกิด แทนเริ่มจากศูนย์ทุกครั้ง
- **procedural** กลั่นเคสเหล่านั้นเป็น "วิธีทำ" ที่นำไปใช้กับเคสใหม่ที่หน้าตาเหมือนกันได้

> ได้อะไร: ความต่างระหว่าง agent ที่ "จำข้อเท็จจริงได้" กับ agent ที่ "เก่งขึ้นเรื่อย ๆ" คือ มีหรือไม่มี episodic + procedural. นี่คือเส้นแบ่งที่ทำให้ self-learning เป็นจริง.

## text เดียว ใช้ได้ 3 ขอบเขต

ข้อดีของ memory ที่เป็น text คือมันข้ามขอบเขตที่ชั้น model/harness ทำไม่ได้ — **text ก้อนเดียวกัน** ทำหน้าที่ได้สามอย่าง:

- เป็น memory ของ **agent ตัวเอง**
- เป็น preference ของ **user คนหนึ่ง**
- เป็นความรู้ของ **ทั้งทีม** (เขียนครั้งเดียว ทุกคนอ่าน)

## เชื่อมกับ procedural memory จาก user

procedural memory คือจุดที่ [[learning-from-users|การเรียนจาก user]] ลงตัวพอดี: พอ manager แก้สิ่งที่ agent พลาด (อนุมัติ refund ที่ agent ปฏิเสธ) background agent บันทึก "manager ทำอะไร + ทำไม" แล้ว agent ถัดไปอ่านมัน **เป็น procedural memory** — ครั้งหน้าเคสเหมือนกันมันอนุมัติแบบ manager แทนปฏิเสธ. การแก้ของคนกลายเป็น "วิธีทำ" ที่ติดตัว agent.

## เชื่อมกับเรื่องอื่นในวิกินี้

- **[[three-learning-layers]]** — memory types อยู่ในชั้น Context
- **[[agent-memory-filesystem]]** — Anthropic ทำ memory เป็น file system ที่ Claude อ่าน/เขียนเอง
- **[[dreaming]]** — process นอก session ที่ curate memory (รวม/ตัด/verify) ข้าม agent
- **[[hybrid-memory]]** — สถาปัตยกรรม memory ที่แยก substrate ของ machine กับ Markdown ของคน
- **[[memory-decay]]** / **[[memory-drift]]** — ปัญหา staleness และ drift ของ memory ที่สะสม
- **[[learning-from-users]]** — ที่มาของ procedural memory คุณภาพสูง

## See also

- [[self-learning-for-agents-explained]]
- [[three-learning-layers]]
- [[agent-memory-filesystem]]
- [[dreaming]]
- [[hybrid-memory]]
- [[memory-decay]]
- [[memory-drift]]
- [[learning-from-users]]
- [[self-learning-agents]]
