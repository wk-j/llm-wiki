---
title: AI Engineering Skills Map
type: concept
tags: [ai, careers, skills, software-engineering, hiring]
created: 2026-08-15
updated: 2026-08-15
sources: [andrew-ng-ai-engineering-skills-map.md]
---

# AI Engineering Skills Map / แผนที่ทักษะ AI Engineering

**AI Engineering Skills Map** คือกรอบสี่ข้อที่ [[andrew-ng|Andrew Ng]] (ผู้ก่อตั้ง [[deeplearning-ai|DeepLearning.AI]]) เสนอไว้ในปี 2026 เพื่อตอบคำถามว่า developer ควรลงแรงเรียนอะไรก่อนในยุคที่ AI เปลี่ยนวิธีสร้าง software ไปจากปี 2022 อย่างสิ้นเชิง

สิ่งที่กรอบนี้พยายามแก้คือปัญหาการเลือก ข่าว AI เยอะและเสียงดัง คนเรียนเลยไม่รู้ว่าอะไรคือแกนจริงกับอะไรคือ hype แผนที่นี้จึงไม่ใช่ curriculum แต่เป็นการจัดลำดับความสำคัญ

## สี่ทักษะ

| ทักษะ | คำถามที่มันตอบ | แกนของมัน |
| --- | --- | --- |
| Building and deploying AI applications | จะทำระบบที่ output เดาไม่ได้ให้ใช้งานจริงได้ยังไง | [[evals-and-error-analysis\|eval กับ error analysis]] |
| Software engineering fundamentals | จะรู้ได้ยังไงว่ากำลังแลกอะไรกับอะไร | เห็น tradeoff และเรียกชื่อมันถูก |
| Using coding agents | จะคุม agent ให้ได้งานโดยไม่เผาเวลา/token ยังไง | รู้ว่าเมื่อไหร่แทรก เมื่อไหร่ปล่อย |
| [[shaping-the-build\|Shaping the build]] | จะตัดสินยังไงว่าควรสร้างอะไร | product sense + ownership |

ใต้ทั้งสี่ข้อมี mindset เดียวรองรับคือ **continuous learning** เพราะ best practice ขยับตลอด

## ทักษะ ไม่ใช่ตำแหน่ง

จุดที่ Ng ย้ำหนักที่สุดคือคำ เขาพูดถึง "AI engineering skills" ไม่ใช่ตำแหน่ง "AI Engineer" เพราะทักษะกว้างกว่าตำแหน่งมาก

เขาเทียบกับ cloud: ทุกวันนี้ developer ทุกคนต้องทำงานกับ cloud เป็น แต่คนที่มีตำแหน่ง "Cloud engineer" จริง ๆ มีน้อยกว่านั้นเยอะ AI ก็กำลังเดินทางเดียวกัน — full-stack, data engineer, DevOps, ML engineer จะต้องมีทักษะชุดนี้ ไม่ใช่แค่คนที่ชื่อตำแหน่งมีคำว่า AI

**ได้อะไร:** ถ้าอ่านแผนที่นี้เป็นคำอธิบายตำแหน่งเฉพาะทาง จะสรุปผิดว่า "ไม่ใช่สายฉัน" ทั้งที่มันคือพื้นฐานใหม่ของทุกสาย

## ทำไมสี่ข้อนี้ถึงต่อกันเป็นชุดเดียว

อ่านแยกจะเหมือนรายการ แต่จริง ๆ มันเป็นสายโซ่ที่ส่งต่อกัน:

1. **Shaping the build** ตัดสินว่าจะสร้างอะไรและอะไรควรอยู่ใน spec
2. **Software fundamentals** ทำให้เรารู้ว่าการสร้างแบบนั้นแลกอะไร และเรียกชื่อข้อจำกัดได้ตรงคำ
3. **Using coding agents** เอาคำที่ตรงนั้นไปสั่ง agent แล้วคุมจังหวะแทรก/ปล่อย
4. **Building and deploying AI applications** ทำให้ของที่ออกมาซึ่งมีพฤติกรรมไม่แน่นอน ยังวัดและกำกับได้ตอนขึ้น production

จะเห็นว่าถ้าขาดข้อ 2 ข้อ 3 ก็สั่งไม่ตรง และถ้าขาดข้อ 4 ของที่ agent ทำเสร็จก็ยังไม่รู้ว่าใช้ได้จริงไหม

**ผลคือ:** มันไม่ใช่เมนูให้เลือกหยิบข้อเดียว แต่เป็นวงจรที่ขาดข้อไหนแล้วข้ออื่นเสียแรงเปล่า

## ที่มาของกรอบนี้ และข้อจำกัด

ทีมของ Ng บอกว่าสังเคราะห์จาก job posting กว่า 10,000 ประกาศ, structured interview หลายสิบครั้งกับผู้เชี่ยวชาญ/hiring manager/recruiter, survey และข้อมูลออนไลน์อื่น เขาเปรียบว่า "เหมือนรัน clustering บน dataset ก้อนใหญ่" แบบไม่เป็นทางการ

ข้อจำกัดที่ควรถือไว้พร้อมกัน:

- ยังไม่มีรายงานวิธีวิจัยฉบับเต็มให้ตรวจ ตัวเลขทั้งหมดเป็น first-party claim
- คำว่า clustering เป็นการเปรียบเทียบ ไม่ใช่ประกาศว่ารัน algorithm แล้วได้ 4 cluster
- ผู้เสนอเป็นผู้ก่อตั้งองค์กรที่ขายคอร์สสอนทักษะชุดนี้พอดี

## เทียบกับหน้าอื่นใน wiki

กรอบนี้ไม่ได้พูดเรื่องใหม่หมด แต่มันรวบสิ่งที่หน้าอื่นเถียงกันมาแล้วให้อยู่ในภาพเดียว:

- [[engineering-role-shift]] บอกว่างานย้ายไปต้นน้ำกับปลายน้ำ — แผนที่ของ Ng ตั้งชื่อต้นน้ำว่า *shaping the build* และตั้งชื่อปลายน้ำฝั่ง AI ว่า *evals/error analysis*
- [[matt-pocock-software-fundamentals]] เถียงเรื่องเดียวกับข้อ 2 มาก่อน คือพื้นฐานสำคัญขึ้นไม่ใช่ลดลง
- [[agentic-engineering]] คือเนื้อของข้อ 3 ในเวอร์ชันที่ลงรายละเอียด workflow มากกว่า
- จุดที่ยังเถียงกันอยู่คือประโยค "ถ้า spec ชัด agent ก็ทำตามได้" ซึ่งชนกับ [[llm-nondeterminism]] และ [[facts-first]] ดู [[spec-driven-development]]

## ดูเพิ่ม

- [[andrew-ng-ai-engineering-skills-map]]
- [[andrew-ng]]
- [[deeplearning-ai]]
- [[evals-and-error-analysis]]
- [[shaping-the-build]]
- [[engineering-role-shift]]
- [[agentic-engineering]]
- [[skill-stacking]]
- [[knowledge-skills-wisdom]]
