---
title: Shaping the Build
type: concept
tags: [ai, product, ownership, engineering, career]
created: 2026-08-15
updated: 2026-08-15
sources: [andrew-ng-ai-engineering-skills-map.md]
---

# Shaping the Build / การกำหนดรูปร่างของงานที่จะสร้าง

**Shaping the build** เป็นชื่อที่ [[andrew-ng|Andrew Ng]] ตั้งให้กับทักษะข้อที่สี่ใน [[ai-engineering-skills-map|AI Engineering Skills Map]] ใจความคือ เมื่อ coding agent ทำตาม spec ได้ดีขึ้นเรื่อย ๆ งานของวิศวกรก็ขยับไปอยู่ที่ **การตัดสินว่าอะไรควรอยู่ใน spec ตั้งแต่แรก**

> "Given a clear spec, coding agents are rapidly improving at delivering to it. Thus, our work as engineers is shifting toward deciding what should be in the spec."

## เลิกรอ design ที่เป๊ะทุก pixel

ประโยคที่ตรงที่สุดของ Ng คือ วิศวกรไม่ควรคาดหวังอีกต่อไปว่าจะได้ design ที่ละเอียดครบทุกจุดมาแล้วมีหน้าที่แค่ implement

โมเดลการทำงานเดิมคือ PM หรือ designer คิดจบ แล้วส่งต่อให้ engineer แปลงเป็น code ขั้นตอน "แปลงเป็น code" คือส่วนที่กินเวลามากที่สุด พอส่วนนั้นถูกลง สายพานก็เสียสมดุล — ถ้ายังรอ spec ที่เป๊ะจากคนอื่นเสมอ คอขวดก็แค่ย้ายไปอยู่ที่คนเขียน spec แทน

สิ่งที่ Ng เสนอคือให้วิศวกรเข้าไปร่วมกำหนด ซึ่งต้องมีสามอย่าง: **product sense**, ความเข้าใจ **business context** และความเข้าใจ **เป้าหมายของลูกค้า**

**ได้อะไร:** ความเร็วของ agent จะแปลงเป็นคุณค่าได้ก็ต่อเมื่อมีคนตัดสินได้เร็วพอ ๆ กันว่าควรสร้างอะไร

## Ownership กับ agency

อีกครึ่งของทักษะนี้ไม่ใช่เรื่อง spec แต่เป็นเรื่องความเป็นเจ้าของ Ng บอกว่า AI เปิดโอกาสให้รับผิดชอบได้มากกว่าเดิม — มองหาปัญหาและโอกาสที่น่าสนใจเอง แล้วลงมือทำอย่างรับผิดชอบ

สิ่งที่ต้องรู้เพิ่มคือวิธีดันโปรเจกต์ให้เดิน ตัวอย่างที่เขายกเป็นคำถามจังหวะ: **เมื่อไหร่ควรรีบทำ MVP ไปให้ user ลอง และเมื่อไหร่ควรช้าลงเพื่อสร้างให้รอบคอบ**

คำถามนี้ไม่มีคำตอบสำเร็จรูป มันขึ้นกับว่าความไม่รู้ก้อนใหญ่ที่สุดตอนนี้คืออะไร ถ้ายังไม่รู้ว่าคนอยากใช้ไหม การสร้างให้แน่นก็เสียเปล่า แต่ถ้ารู้แล้วว่าคนใช้แน่และของจะอยู่ยาว การรีบก็สร้างหนี้

**ผลคือ:** ทักษะนี้วัดที่การเลือกจังหวะ ไม่ใช่ที่ความขยัน

## เชื่อมกับที่ wiki นี้บันทึกไว้ก่อนหน้า

Shaping the build ไม่ใช่ความคิดใหม่หมด แต่เป็นการตั้งชื่อให้สิ่งที่หลายแหล่งพูดถึงมาก่อน:

- [[engineering-role-shift]] เรียกมันว่า "ต้นน้ำขยายตัว" — งาน requirement, architecture และการตีกรอบปัญหากินเวลามากขึ้น
- [[thorsten-ball|Thorsten Ball]] ใน [[software-after-software]] เขียนว่า engineering "shifts away from code and toward product thinking, shaping systems, judging tradeoffs, and business outcomes" ซึ่งแทบเป็นประโยคเดียวกัน
- [[unknowns-matrix]] และ [[map-vs-territory]] ของ [[thariq-shihipar|Thariq]] ให้เครื่องมือจับต้องได้ว่าจะเคลียร์ความไม่รู้ก่อนลงมืออย่างไร
- [[value-migration-from-code]] อธิบายกลไกเศรษฐศาสตร์เบื้องหลัง: พอ code ถูกลง คุณค่าย้ายไปอยู่กับการตัดสินใจ

## จุดที่ยังเถียงกันอยู่

ข้อสมมติของทักษะนี้คือ "spec ชัด → agent ทำได้" ซึ่งใน wiki นี้ยังไม่ใช่เรื่องที่ตกลงกันได้:

- [[llm-nondeterminism]] กับ [[stop-writing-specs-start-writing-facts]] เถียงว่า spec ที่เป็น prose คือคำทำนายพฤติกรรม model ไม่ใช่สัญญา เปลี่ยนรุ่น model เท่ากับเปลี่ยนตัวแปลภาษา
- [[mario-zechner|Mario Zechner]] เตือนว่า SDD ที่ไม่ระวังกลายเป็น hyper-waterfall เพราะ prose ไม่มีทางละเอียดเท่าโปรแกรมจริง ช่องว่างที่ไม่ได้เขียนไว้ agent จะเติมเองจาก pattern เฉลี่ย
- ในทางกลับกัน Ng เองก็เขียนไว้ในทักษะข้อ *using coding agents* ว่าต้องรู้ด้วยว่า **เมื่อไหร่ไม่ต้องเสียเวลาเขียน spec** ซึ่งอ่อนกว่าจุดยืน SDD เต็มรูปแบบ

wiki เก็บทั้งสองฝั่งไว้ ไม่รวบเป็นคำตอบเดียว ดู [[spec-driven-development]] สำหรับข้อโต้แย้งฉบับเต็ม

อีกคำถามที่เปิดอยู่คือฝั่งองค์กร: ถ้าวิศวกรทุกคนต้อง shape งานเอง จะเกิดอะไรกับคนที่เพิ่งเข้าวงการ [[taste-paradox]] ชี้ว่าเด็กใหม่ถูกผลักให้ตัดสินใจระดับที่ยังไม่มีประสบการณ์รองรับ และ [[ai-work-intensification]] บันทึกว่าบางที่เพิ่ม ownership แต่ไม่ได้เพิ่มเวลาหรืออำนาจตัดสินใจให้จริง

## ดูเพิ่ม

- [[andrew-ng-ai-engineering-skills-map]]
- [[ai-engineering-skills-map]]
- [[engineering-role-shift]]
- [[value-migration-from-code]]
- [[unknowns-matrix]]
- [[map-vs-territory]]
- [[spec-driven-development]]
- [[throwaway-prototyping]]
- [[taste-paradox]]
- [[software-after-software]]
