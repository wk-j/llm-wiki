---
title: Agent Development Environment
type: concept
tags: [ai, agents, cloud-agents, environment, harness, infrastructure]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md]
---

# Agent Development Environment / "Environment คือตัวสินค้า"

ข้อสรุปที่ [[cursor|Cursor]] เน้นที่สุดจากหนึ่งปีของการทำ [[cloud-agents|cloud agent]] คือ: **ปัจจัยเดียวที่กำหนดคุณภาพงานของ cloud agent มากที่สุด คือการที่มันมี development environment ครบเหมือน developer จริง** — มี dependency, tool, network ที่ใช้รันและ verify งานได้.

> "the single biggest factor in cloud agent output quality is ensuring it has a full development environment, like a developer has."

ในคำของ [[matt-pocock-4-ai-terms|Matt Pocock]] (Model / Harness / Environment / Agent) นี่คือการบอกว่า **environment สำคัญพอ ๆ กับ model** — ไม่ใช่แค่กล่องที่ agent ไปรันอยู่เฉย ๆ.

## ทำไมเรื่องนี้มองข้ามง่าย

ตอนรัน local agent เราไม่ต้องคิดเรื่องนี้เลย เพราะ agent **ยืม environment ที่ทำงานอยู่แล้วบน laptop ไปใช้ฟรี** — dependency ติดตั้งไว้แล้ว, network เข้าได้อยู่แล้ว, credential อยู่ในเครื่องอยู่แล้ว.

บนคลาวด์ต้องประกอบใหม่ทั้งหมดจากศูนย์ และที่ยากคือ **บอกได้ยากว่าประกอบครบหรือยัง**.

## อาการพังที่อันตราย: คุณภาพตกแบบเงียบ ๆ

จุดที่ Cursor ย้ำคือ environment ไม่ครบ **ไม่ทำให้ crash หรือขึ้น error**. สัญญาณเดียวมักเป็น **คุณภาพงานที่ค่อย ๆ แย่ลงแบบจับยาก**.

> "Instead of a crash or an error message, often the only indication is a subtle degradation in output quality. You might not notice it at first, or if you do, you might chalk it up to the model."

ผลที่ตามมาคือ **คนไปโทษ model** ทั้งที่ต้นเหตุจริงคือ agent ไม่มี environment ที่จะรันหรือ verify งานของตัวเองได้.

เมื่อปีก่อนเรื่องนี้ยังไม่สำคัญมาก เพราะ model ยังใช้ environment ได้ไม่เต็มที่อยู่แล้ว. แต่พอ model ฉลาดขึ้น **environment กลายเป็นตัวตัดสินว่า model จะทำงานได้เต็มศักยภาพหรือไม่** — capability เพิ่มแต่ถูก environment ที่ไม่ครบบังไว้.

## "Full environment" ต้องสร้าง infra อะไรบ้าง

- เครื่องมือให้ user สร้าง agent environment ได้ดีขึ้น
- วิธี **hibernate และ resume VM** ระหว่าง message อย่างมีประสิทธิภาพ
- pipeline สำหรับ **checkpoint / restore / fork VM image** แบบเร็วและทนทาน
- การเชื่อม harness กับ client ให้แน่น เพื่อให้ทั้ง agent และคน interpret และโต้ตอบกับ environment ได้

## "Enterprise IT สำหรับ agent"

พอ cloud agent รับงานมากขึ้น มันต้องการ **network access แบบควบคุมได้** — สร้าง PR, ดึง dependency, ทำ research. สุดท้าย Cursor เลยกลายเป็นต้องสร้างสิ่งที่เหมือนแผนก IT ขององค์กร แต่ทำให้ agent:

- **secret redaction** — กลบความลับไม่ให้รั่วเข้า log/output
- **network policy** — คุมว่า agent ออกเน็ตไปไหนได้บ้าง
- **credential management** — จัดการ key/token ให้ agent ใช้ได้อย่างปลอดภัย

**ได้อะไร:** ก่อนจะสรุปว่า "model นี้ทำงานไม่ดี" ให้เช็คก่อนว่า environment ครบไหม — มันคือตัวแปรที่ถูกมองข้ามบ่อยที่สุดและกระทบคุณภาพมากที่สุด. ต่อยอดเป็นแนวคิด [[self-healing-environments|self-healing environment]] ที่อยากให้ agent ตรวจและซ่อม environment ของตัวเองได้.

## See also

- [[cloud-agents]]
- [[what-weve-learned-building-cloud-agents]]
- [[cursor]]
- [[self-healing-environments]]
- [[matt-pocock-4-ai-terms]]
- [[coding-harness]]
- [[durable-execution]]
