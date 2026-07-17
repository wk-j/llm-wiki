---
title: Open-weight Models
type: concept
tags: [ai, open-source, deepseek, philosophy, deployment]
created: 2026-04-27
updated: 2026-07-17
sources: [deepseek-wikipedia.md, Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md, chinas-models-no-longer-need-western-hardware.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md, framework-frontier-ai-dawning-new-age.md, kimi-k3-explained-prompt-engineering.md]
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

[[longcat-2-0|LongCat 2.0]] เพิ่มคำถามอีกชั้น: open-weight มีความหมายแค่ไหนถ้า model ใหญ่ขึ้นจนการรันจริงต้องพึ่ง hardware/software stack เฉพาะทาง. วิดีโอ [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]] บอกว่า weights ของ LongCat จะตามมา แต่ในช่วงคลิปยังเป็น "coming soon" จึงควรแยกสถานะ **ประกาศจะปล่อย** ออกจาก **ปล่อย weights จริงแล้ว**.

[[mario-zechner|Mario Zechner]] เพิ่มมุม local inference ใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]]. เขามองว่า local AI ยัง setup ยากและไม่เหมาะทุกงาน แต่ model เล็กเริ่มพอแล้วสำหรับ application ที่ขอบเขตชัด เช่น toy robot สำหรับเด็กที่ใช้ speech-to-text, text-to-speech, และ LLM เล็กบน MacBook M1. ตัวเลขที่เขาเล่า: pipeline หนึ่งกิน unified memory ราว 14GB และให้ประสบการณ์ดีพอสำหรับ chatbot + camera + motor.

บทเรียนคือ open-weight/local model ไม่ต้องชนะ frontier model ทุกมิติ. ถ้า task ต้องการ latency, privacy, หรือ cost control และ quality threshold ไม่สูงเท่างาน coding ยาก ๆ local model ก็เริ่มมีที่ทางจริง.

## Kimi K3: เปิด weights ไม่ได้แปลว่ารัน local ง่าย

[[kimi-k3-explained-prompt-engineering|วิดีโอ Kimi K3]] เสนอกรณีตรงข้ามกับ model local ขนาดเล็ก. ผู้พูดเรียก [[kimi-k3|K3]] ว่า open-weight frontier model ด้าน agentic coding แต่บอกว่าขนาด 3T parameters ใหญ่เกิน consumer hardware. ผู้ใช้ทั่วไปจึงน่าจะเรียกผ่าน inference provider มากกว่ารันเอง.

ตรงนี้แยกประโยชน์ของ open-weight ออกเป็นสองระดับ:

- คนทั่วไปได้ประโยชน์ทางอ้อม เมื่อบริษัทอื่นเอา base ไป post-train หรือทำ product ต่อ
- องค์กรที่มี compute มากอาจ self-host เพื่อคุม data และปรับ weights เอง

แต่ release status ยังไม่ชัดจากแหล่งนี้ เพราะ title/description เรียก open-weights ขณะที่ transcript พูดถึง “เมื่อ weights พร้อม”. จึงต้องแยก **ประกาศว่าจะเปิด**, **เผย license**, และ **ดาวน์โหลด weights ได้จริง**.

**ผลคือ:** openness ลดข้อจำกัดด้านสิทธิ์และการต่อยอดได้ แต่ไม่ได้ลบข้อจำกัดด้าน hardware, serving cost หรือ privacy เมื่อยังต้องพึ่ง provider.

## ถ้า open-weight ข้ามเส้น Frontier-class

[[framework-frontier-ai-dawning-new-age|กรอบของ Demis Hassabis]] เสนอว่า [[frontier-ai-standards-body|การประเมิน Frontier AI]] ควรใช้กับ model ที่ข้าม capability threshold ไม่ว่าจะ open หรือ closed และมาจากประเทศใด Board ควรมีตัวแทน open source ส่วน model ที่ยังไม่ถึง frontier threshold จาก startup/academia ได้รับการยกเว้น.

หลักนี้ดูเท่าเทียม แต่บังคับใช้ไม่เหมือนกัน. Closed API มีเจ้าของคุม release และ patch หลังพบ vulnerability. Open-weight model ถูกดาวน์โหลด, fork, fine-tune และ deploy นอกเขตอำนาจได้. คำถามจึงไม่ใช่แค่ว่าต้อง test หรือไม่ แต่ test ที่จุดไหน—ก่อนปล่อย weights, ก่อน deploy ระบบใหญ่ หรือทั้งสองจุด.

อีกความตึงคือ threshold cliff. ถ้าข้ามเส้นแล้ว compliance cost กระโดด ผู้พัฒนาอาจไม่เปิด weights, ลดการเผยข้อมูล หรือปรับ model ให้อยู่ใต้เกณฑ์. กติกาที่ตั้งใจปกป้อง open ecosystem อาจทำให้ open model frontier น้อยลงได้.

**ผลคือ:** risk-tiering ตาม capability เป็นจุดเริ่มที่ดี แต่ governance ต้องยอมรับว่า weights ที่แพร่แล้วเรียกคืนไม่ได้เหมือนปิด API.

## Why this helps / ผลคือ

- **Democratization:** ช่วยให้เทคโนโลยี AI ระดับโลกเข้าถึงได้ง่ายขึ้น ไม่ถูกผูกขาดโดยยักษ์ใหญ่เพียงไม่กี่ราย
- **Innovation:** เกิดการต่อยอดในชุมชนนักพัฒนาอย่างรวดเร็ว เพราะใครๆ ก็เอาไปทดลองได้
- **Private deployment:** องค์กรที่มี code/data อ่อนไหวสามารถรัน model ใน infra ตัวเองได้ โดยเฉพาะงาน routing, summarization, validation ที่เกิดบ่อยใน agent pipeline

## See also

- [[deepseek]]
- [[open-source-governance]]
- [[mellum2]]
- [[focal-models]]
- [[longcat-2-0]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
- [[frontier-ai-standards-body]]
- [[framework-frontier-ai-dawning-new-age]]
- [[kimi-k3]]
- [[kimi-k3-explained-prompt-engineering]]
