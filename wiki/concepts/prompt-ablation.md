---
title: Prompt Ablation
type: concept
tags: [ai, prompts, evals, harness, experimentation]
created: 2026-09-10
updated: 2026-09-10
sources: [boris-cherny-cut-80-percent-claude-code-prompt.md]
---

# Prompt Ablation / ทดลองลบคำสั่งออก

**Prompt ablation** คือการลบ system prompt หรือ instruction ออก แล้ววัดว่าพฤติกรรมของ model เปลี่ยนอย่างไร วิธีนี้ตอบคำถามว่าแต่ละบรรทัดช่วยจริง ขวาง model หรือไม่มีผล แทนการถือว่ากฎเก่าทุกข้อยังจำเป็นเพราะเคยมีคนเขียนไว้

[[boris-cherny|Boris Cherny]] อธิบายใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์กับ Y Combinator]] ว่าทีม [[claude-code|Claude Code]] เริ่มจากลบ system prompt ทั้งก้อน แล้วนำกลับทีละบรรทัดพร้อม eval เมื่อ [[claude-opus-5|Opus 5]] ออก วิธีนี้ทำให้ทีมตัด prompt ออกราว 80% และพบใน simple-mode experiment ว่า model บางครั้งดูฉลาดขึ้นเมื่อไม่มีคำสั่งเดิมคอยกำกับ

## วิธีใช้

1. เก็บ baseline จาก task และ failure ที่เป็นตัวแทนของงานจริง
2. ลบ prompt, tool description หรือ scaffold ที่ต้องการทดสอบ
3. รัน eval เดิมหลายรอบ ไม่ตัดสินจากตัวอย่างเดียว
4. เทียบทั้ง outcome, tool trajectory, cost และ safety behavior
5. เพิ่มกลับเฉพาะส่วนที่แก้ failure ซ้ำ ๆ ได้โดยไม่ทำให้ด้านอื่นถอย

ควรทดสอบทีละกลุ่มหรือทีละบรรทัดเพื่อให้รู้สาเหตุ แต่ interaction ระหว่างกฎก็สำคัญ บรรทัดหนึ่งอาจไม่มีผลลำพังแต่มีผลเมื่ออยู่กับอีกบรรทัด

**ได้อะไร:** prompt เปลี่ยนจากเอกสารสะสมความกลัว มาเป็นชิ้นส่วนของ harness ที่มีหลักฐานรองรับ

## อะไรควรลบก่อน และอะไรไม่ควรเหมารวม

เป้าหมายแรกคือข้อความที่ชดเชยพฤติกรรมของ model รุ่นเก่า เช่นบังคับลำดับคิดละเอียดหรือเตือน style ที่รุ่นใหม่ทำได้เองแล้ว ไม่ใช่ลบ permission boundary, sandbox, test หรือ audit log เพียงเพราะมันอยู่รอบ model เหมือนกัน

ใน product จริง prompt ยังมีหน้าที่กำหนด UX และ contract ที่ผู้ใช้คาดหวัง การทดลองพบว่า model ฉลาดขึ้นเมื่อ prompt สั้นลง ไม่ได้แปลว่า product ควรเหลือ prompt ว่าง

## ความสัมพันธ์กับ eval และ harness ratchet

[[harness-ratchet|Harness ratchet]] บอกให้เปลี่ยน failure ที่เกิดซ้ำเป็น rule, hook หรือ test. Prompt ablation เป็นแรงต้านอีกด้าน: เมื่อ model เปลี่ยน ต้องย้อนถามว่า ratchet ตัวไหนยังจับ failure จริง ตัวไหนกลายเป็นน้ำหนักถ่วง

[[evals-and-error-analysis|Eval]] จึงทำงานสองทาง:

- บอกว่าควรเพิ่ม control เมื่อ failure เดิมเกิดซ้ำ
- บอกว่าควรถอด control เมื่อไม่มีประโยชน์หรือทำให้ capability ลดลง

**ผลคือ:** harness เรียนรู้ได้โดยไม่โตทางเดียว

## See also

- [[coding-harness]]
- [[instruction-budget]]
- [[claude-md]]
- [[harness-ratchet]]
- [[evals-and-error-analysis]]
- [[model-elicitation]]
- [[claude-code]]
- [[claude-opus-5]]
