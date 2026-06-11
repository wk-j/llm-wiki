---
title: Open-weight Models
type: concept
tags: [ai, open-source, deepseek, philosophy, deployment]
created: 2026-04-27
updated: 2026-06-05
sources: [deepseek-wikipedia.md, Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md]
---

# Open-weight Models / โอเพนเวต โมเดล

รูปแบบการเผยแพร่ AI model ที่เปิดให้คนทั่วไปดาวน์โหลดตัว "สมอง" (Weights/Parameters) ไปรันเองได้ แต่ไม่ได้เปิดเผยขั้นตอนการสร้าง (Training Data/Code) ทั้งหมดเหมือน Open Source จริงๆ

## แก่นความคิด

ในโลก AI มีขั้วตรงข้ามคือ **Closed Source** (เช่น GPT-4 ที่เราคุยได้แค่ผ่าน API) และ **Open Source** (ที่เปิดหมดทุกอย่าง)

**Open-weight** คือจุดกึ่งกลางที่บริษัทอย่าง **[[deepseek|DeepSeek]]** หรือ Meta (Llama) เลือกใช้:
- **ข้อดี:** นักพัฒนาสามารถนำไปติดตั้งใน server ตัวเอง, ปรับแต่ง (Fine-tune), หรือใช้งานแบบ offline ได้โดยไม่ต้องกังวลเรื่องความเป็นส่วนตัว
- **ข้อจำกัด:** เราไม่รู้แน่ชัดว่าเขาเอาข้อมูลอะไรมาสอน AI บ้าง และอาจจะมีเงื่อนไขการใช้งานเชิงพาณิชย์แฝงอยู่

[[mellum2|Mellum2]] ของ [[jetbrains|JetBrains]] เติมอีกกรณีหนึ่ง: model เปิดภายใต้ Apache 2.0 และถูก pitch สำหรับ private/local deployment โดยตรง ใช้กับ code และข้อมูลภายในองค์กรได้โดยไม่ต้องส่งทุกอย่างไป closed API

ตรงนี้ทำให้ open-weight/open-source model กลายเป็นเรื่อง architecture ของระบบ AI ด้วย ไม่ใช่แค่เรื่องอุดมการณ์ ถ้า model ทำหน้าที่เป็น [[focal-models|focal model]] ใน pipeline ที่เรียกถี่มาก การ self-host อาจคุมทั้ง cost, latency, และ privacy ได้ดีกว่า

## Why this helps / ผลคือ

- **Democratization:** ช่วยให้เทคโนโลยี AI ระดับโลกเข้าถึงได้ง่ายขึ้น ไม่ถูกผูกขาดโดยยักษ์ใหญ่เพียงไม่กี่ราย
- **Innovation:** เกิดการต่อยอดในชุมชนนักพัฒนาอย่างรวดเร็ว เพราะใครๆ ก็เอาไปทดลองได้
- **Private deployment:** องค์กรที่มี code/data อ่อนไหวสามารถรัน model ใน infra ตัวเองได้ โดยเฉพาะงาน routing, summarization, validation ที่เกิดบ่อยใน agent pipeline

## See also

- [[deepseek]]
- [[open-source-governance]]
- [[mellum2]]
- [[focal-models]]
