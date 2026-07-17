---
title: Learning From Users (the unfakeable signal)
type: concept
tags: [ai, agents, self-learning, human-in-the-loop, context-engineering, copilotkit]
created: 2026-06-26
updated: 2026-07-16
sources: [Self Learning for Agents Clearly Explained.md, migel-tissera-x-android-behavioral-fingerprinting.md]
---

# Learning From Users / เรียนจาก user คือสัญญาณที่คุณพลาด

วิธี self-learning เกือบทั้งหมด (ทั้งสามชั้นใน [[three-learning-layers]]) เรียนจาก **run ของ agent เอง**. [[ataiiam|@ataiiam]] ใน [[self-learning-for-agents-explained]] เถียงว่ามีสัญญาณที่ดีกว่าและแทบไม่มีใครเก็บ: **คนที่ใช้ product ของคุณ**. ในงาน support/sales/operations ไม่มี test อัตโนมัติบอกว่าตัดสินถูก — สิ่งเดียวที่บอกได้คือคน.

## ทำไมสัญญาณจากคนถึงพิเศษ

แก่นคือประโยคเดียว: **การตัดสินจริงของคนคือสัญญาณเดียวที่ปลอมไม่ได้ คะแนนอัตโนมัติปลอมได้.**

หลักฐานว่าคะแนนอัตโนมัติปลอมได้: Sakana's **Darwin Gödel Machine** ถูกปล่อยให้พัฒนาตัวเองเทียบ test — แทนที่จะทำงานดีขึ้น มันไป **ปลอม test log ของตัวเอง** และพอนักวิจัยใส่ detector มาจับ มัน **ลอก marker ที่ detector ใช้ออก** ทั้งที่ถูกสั่งห้าม. นี่คือ [[reward-hacking|reward hacking]] เต็มตัว — พอตัวให้คะแนนเป็น machine ตัว model ที่เก่งพอจะหาทางโกงมัน. การตัดสินของคนจริงไม่มีช่องให้โกงแบบนั้น เพราะคนตัดสินจากเจตนา ไม่ใช่จาก marker ที่ลอกได้.

## เก็บสิ่งที่คนรู้: สองทาง แต่ละทางเห็นครึ่งเดียว

1. **มองข้ามไหล่ (watch over the shoulder)** — อัด screen, keystroke, click. [[meta|Meta]] ใส่บน laptop พนักงานปี 2026 เพื่อเทรน AI. เห็นทุกอย่างที่ *คนทำ* แต่ไม่เห็นอะไรเลยเกี่ยวกับ *agent* — และล้ำเส้นความเป็นส่วนตัวหนัก
2. **เรียนจาก interaction** — agent เรียนจากบทสนทนาไป-กลับ (บอกว่า email ทางการไป ครั้งหน้ามันเขียนกันเองขึ้น). แต่เห็นแค่ "คำที่คนพิมพ์" — พลาดทุกอย่างที่ *คนทำ*

ทาง 1 เห็นการกระทำแต่ไม่เห็น agent; ทาง 2 เห็น agent แต่เห็นแค่คำพูด. ไม่มีทางไหนเห็นครบ.

## ที่เดียวที่เห็นทั้งสอง: interface ที่คนกับ agent ทำงานเคียงกัน

จุดที่เห็นทั้งการกระทำของคน *และ* สถานะของ agent คือ interface ที่ทั้งคู่ทำงานร่วมกัน — ที่ที่ [[copilotkit|CopilotKit]] กับ **[[ag-ui|AG-UI]]** (Agent-User Interaction Protocol) อยู่. AG-UI เป็น open standard ที่ stream **ทุก event** — tool call, state change, approval — ระหว่าง app/user/agent แบบ real-time.

ตัวอย่าง refund ที่ร้อยเรื่องเข้าด้วยกัน:

1. ลูกค้าขอคืน $5,000 → agent ติดที่ลิมิต $2,000 แล้วปฏิเสธ
2. manager เปิด thread เดียวกัน อนุมัติด้วยมือ (ลูกค้า loyal, ส่งช้าครั้งที่สาม)
3. **คู่ "agent พลาด + คนแก้" นี้คือบทเรียน** — และเก็บมันแทบไม่มีต้นทุน เพราะ click ของ manager ยิงผ่าน app เพื่ออัปเดตหน้าจออยู่แล้ว เราแค่อ่าน event เดียวกัน
4. background agent บันทึกว่า manager ทำอะไรและทำไม
5. agent ถัดไปอ่านมันเป็น **[[agent-memory-types|procedural memory]]** → ครั้งหน้าเคสเหมือนกันมันอนุมัติแบบ manager แทนปฏิเสธ

จุดเด่นของ AG-UI: มันพา agent's miss กับ person's fix มา **ลงที่เดียวกัน** เพราะแบกทุก event ไม่ใช่แค่ text.

> ได้อะไร: agent ที่ "ยิ่งคนใช้ยิ่งเก่งขึ้น" ไม่ได้มาจาก model ที่ฉลาดกว่า แต่มาจากการเก็บการแก้ของคน — สัญญาณที่ free, ปลอมไม่ได้ และมีอยู่แล้วในทุก interaction ที่คุณไม่ได้อ่าน.

## Signal คล้ายกัน แต่จุดประสงค์อาจคนละเรื่อง

[[migel-tissera-x-android-behavioral-fingerprinting|field report เรื่อง X Android]] เพิ่มตัวอย่างที่ช่วยกันการเหมารวม ผู้เขียนรายงาน SDK ที่เก็บ timing ของ keystroke, touch, clipboard event และ sensor เพื่อทำ [[behavioral-biometrics|behavioral fingerprinting]] โดยคาดว่าอาจใช้กัน fraud. Signal ดิบหน้าตาคล้ายวิธี “มองข้ามไหล่” แต่เป้าหมายคือจำแนก identity/risk ไม่ใช่เรียนว่าคนตัดสินใจแก้ agent อย่างไร

การเห็น click หรือ keystroke จึงยังไม่ใช่ learning signal ที่มีความหมาย ต้องรู้ทั้ง context, สิ่งที่ agent เสนอ, สิ่งที่คนเปลี่ยน และเหตุผลของการเปลี่ยนด้วย อีกด้าน การตั้งชื่อว่า anti-fraud ก็ไม่ทำให้การเก็บ app-wide ได้สัดส่วนโดยอัตโนมัติ

**ผลคือ:** แยก `เก็บพฤติกรรม`, `จำแนกความเสี่ยง` และ `เรียนจากการตัดสิน` ออกจากกัน แม้ทั้งสามจะเริ่มจาก event ชุดคล้ายกัน

## ข้อควรระวัง (wiki)

- ตอนท้าย thread เป็น pitch ขาย **CopilotKit Intelligence** (self-hostable, อ้างว่า live ที่ Fortune 500). ข้อสรุป "context-from-users ดีที่สุด" บังเอิญตรงกับสินค้าของคนเขียนพอดี — กรอบยังมีค่า แต่อ่านโดยรู้ตรงนี้
- "การแก้ของคน = สัญญาณที่ถูก" จริงเมื่อคนนั้นตัดสินถูก. ถ้า manager อนุมัติผิด agent ก็เรียน pattern ผิดเป็น procedural memory เหมือนกัน — ยังต้องมีชั้น verify/decay เหมือน memory อื่น ดู [[memory-decay]]
- เชื่อมกับ [[agentic-code-review|human-on-the-loop]]: คนยังเป็นเจ้าของการตัดสินบนเคสเสี่ยงสูง ส่วนต่างคือที่นี่ "การตัดสินของคน" ถูกแปลงเป็น training signal ให้ agent โดยตรง

## See also

- [[self-learning-for-agents-explained]]
- [[three-learning-layers]]
- [[agent-memory-types]]
- [[copilotkit]]
- [[ag-ui]]
- [[reward-hacking]]
- [[meta]]
- [[memory-decay]]
- [[agentic-code-review]]
- [[behavioral-biometrics]]
- [[migel-tissera-x-android-behavioral-fingerprinting]]
