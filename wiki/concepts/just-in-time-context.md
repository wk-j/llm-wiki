---
title: Just-in-Time Context
type: concept
tags: [ai, prompt-engineering, context-management, efficiency]
created: 2026-04-28
updated: 2026-04-28
sources: [ryan-lopopolo-harness-engineering.md]
---

# Just-in-Time Context / บริบทแบบมาเมื่อจำเป็น

กลยุทธ์การจัดการ [[context-window]] ของ Agent โดยการไม่ส่งคำสั่ง (Instruction) ทั้งหมดลงไปล่วงหน้า แต่จะส่งให้เมื่อ Agent ต้องการหรือทำผิดพลาดเท่านั้น — เสนอโดย [[ryan-lopopolo]] (OpenAI, 2026)

## ปัญหา: Context Overload
การใส่คำสั่งจำนวนมากลงใน prompt ตั้งแต่แรก (Frontloading) มีข้อเสียคือ:
- **Noise**: Agent อาจสับสนกับคำสั่งที่ยังไม่ถึงเวลาใช้
- **Cost**: เปลือง token ในทุกๆ turn ของบทสนทนา
- **Attention**: ความสามารถในการโฟกัสของโมเดลลดลงเมื่อ context ยาวเกินไป

## วิธีการ (The JIT Approach)
1. **Let the Agent Cook**: ปล่อยให้ Agent เริ่มทำงานตามความเข้าใจเบื้องต้น
2. **Trigger-based Injection**: ใช้ระบบภายนอก (Harness) คอยดักจับสถานะ:
   - **Lint Failure**: เมื่อ Agent เขียนโค้ดผิด pattern ให้พ่น error message ที่มีคำสั่งที่ถูกต้องแนบไปด้วย
   - **Test Failure**: เมื่อรัน test ไม่ผ่าน ให้ส่งเอกสารวิธีแก้ (Remediation steps) กลับไป
   - **Reviewer Agent**: เมื่อ Agent ส่ง PR ให้ใช้ Agent อีกตัว (Persona) เข้ามาพ่นคอมเมนต์พร้อม context เฉพาะเรื่อง (เช่น Security context)
3. **Self-Healing**: Agent จะได้รับ context ใหม่เฉพาะจุดที่มันทำพลาด และทำการแก้ไขตามข้อมูลที่เพิ่งได้รับ (Just-in-Time)

## payoff (ผลที่ได้)
- **Efficiency**: ประหยัด token และรักษา context window ให้สะอาดที่สุด
- **Reliability**: Agent ได้รับข้อมูลที่เจาะจงกับปัญหาหน้างาน ทำให้แก้ปัญหาได้แม่นยำกว่าการอ่านคู่มือเล่มหนาตั้งแต่ต้น

## ดูเพิ่ม
- [[harness-engineering]]
- [[ryan-lopopolo]]
- [[context-rot]]
- [[compaction]]
