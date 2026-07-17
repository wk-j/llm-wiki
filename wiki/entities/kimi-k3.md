---
title: Kimi K3
type: entity
tags: [ai, llm, model, open-weight, coding, agents, moonshot, moe]
created: 2026-07-17
updated: 2026-07-17
sources: [kimi-k3-explained-prompt-engineering.md]
---

# Kimi K3 / คิมิ K3

Kimi K3 คือ model ของ [[moonshot-ai|Moonshot AI]] ที่วิดีโอ [[kimi-k3-explained-prompt-engineering|Kimi K3 Explained!]] วางเป็น open-weight frontier model สำหรับ agentic coding. ข้อมูลในหน้านี้มาจาก third-party explainer และ transcript ที่มีชื่อเพี้ยนหลายจุด จึงยังไม่ใช่ spec ที่ยืนยันจาก Moonshot.

## จุดที่คลิปอ้างว่าเด่น

- agentic coding, terminal work, web development และ UI design
- ขนาดรวม 3T parameters แบบ [[mixture-of-experts|MoE]]
- 896 experts และ route 16 experts ต่อ token
- native multimodal vision
- context window 1M tokens
- token efficiency ดีขึ้นจาก Kimi รุ่นก่อน แม้ราคา API ขยับขึ้นมาอยู่ระดับ frontier

ผู้พูดเรียก K3 ว่า workhorse: ไม่จำเป็นต้องคุยดีที่สุด แต่เหมาะกับการรับงาน coding หลายขั้นแล้วเดินหน้าต่อ. เขาอ้างว่า K3 เด่นบน Terminal-Bench 2.1 แต่ตามหลัง [[fable|Claude Fable 5]] ใน Humanity's Last Exam และมี hallucination rate แย่กว่า Opus 4.8.

**ได้อะไร:** K3 ถูกวางเป็น specialist ไม่ใช่ general winner. การเลือกใช้จึงต้องอิงงานและ harness จริง.

## ความต่อเนื่องจาก K2.6

หน้า [[kimi-k2-6|Kimi K2.6]] บันทึก positioning ตอนเมษายน 2026 ว่าเน้น coding และ long-horizon agents มากกว่า reasoning หรือ vision. แหล่ง K3 ยังรักษาแกน coding ไว้ แต่เพิ่ม claim ว่ามี native vision และ context 1M tokens.

นี่อาจเป็นพัฒนาการของตระกูล ไม่จำเป็นต้องเป็นข้อขัดแย้ง. อย่างไรก็ดี capability ด้าน vision กับการ “แข่งขันด้าน vision” เป็นคนละเรื่อง: มี input แบบภาพไม่ได้แปลว่าคะแนน vision ขึ้น frontier แล้ว.

## Open-weight แต่ไม่ใช่ local-friendly

คลิปเรียก K3 ว่า open-weights แต่ตอนหนึ่งพูดถึง “เมื่อ weights พร้อม” ทำให้ release status ยังไม่ชัดจาก transcript. ต่อให้ดาวน์โหลดได้จริง ขนาด 3T ก็ทำให้การ self-host อยู่ไกลเกิน consumer hardware ส่วนใหญ่.

ผลคือข้อดีด้าน privacy ขึ้นกับ deployment. องค์กรที่รันเองได้อาจเก็บข้อมูลในระบบ แต่ผู้ใช้ที่เรียกผ่าน inference provider ยังต้องส่งข้อมูลออกไปเหมือนใช้ closed API.

## ฐานสำหรับ post-training

ผู้พูดมองว่าตระกูล Kimi เป็น base ที่ ecosystem ชอบเอาไปต่อยอด และคาดว่า K3 จะเดินเส้นเดียวกัน. แต่ตัวอย่าง Cursor, Cognition/Windsurf และ Thinking Machines ใน transcript ยังต้องตรวจต้นทาง เพราะชื่อ model/บริษัทถูกถอดเสียงไม่คงที่.

นอกจากนี้การ post-train model 3T ต้องใช้ compute สูงมาก. โอกาสจึงอยู่กับองค์กรใหญ่ มากกว่าคนที่เพียงอยาก fine-tune model local.

## คำถามเปิด

- weights และ license ถูกเผยแพร่จริงหรือยัง.
- benchmark comparison ใช้ harness, effort, budget และจำนวน run เท่ากันหรือไม่.
- parameter/architecture/context claims ตรงกับ Moonshot technical report หรือไม่.
- K3 เป็น base ที่ “mid-trained” จริง หรือคำนี้เป็นการคาดเดาของ ecosystem.
- cost ต่อ task หลังรวม retry, latency และ review ยังดีกว่าคู่แข่งแค่ไหน.

## ดูเพิ่ม

- [[kimi-k3-explained-prompt-engineering]]
- [[moonshot-ai]]
- [[kimi-k2-6]]
- [[open-weight-models]]
- [[mixture-of-experts]]
- [[ai-token-economics]]
- [[fable]]
