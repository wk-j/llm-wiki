---
title: LLM Coding Pitfalls
type: concept
tags: [llm, coding, claude-code, workflow, meta]
created: 2026-04-14
updated: 2026-05-29
sources: [forrestchangandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls..md, llm-era-computer-engineering-nattee.md, improved-15-llms-harness-changed.md, Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md]
---

# LLM Coding Pitfalls / กับดักของ LLM ตอนเขียนโค้ด

ชุดพฤติกรรมที่ผิดพลาดที่ LLM มักทำซ้ำๆ เมื่อทำการแก้ไขโค้ด — [[andrej-karpathy]] เป็นผู้สังเกตและรวบรวมเป็นแนวทาง [[karpathy-guidelines]] เพื่อใช้เป็น skill ประเด็นสำคัญคือ กับดักเหล่านี้เป็นเรื่องของ *พฤติกรรม* ไม่ใช่ข้อจำกัดของโมเดล พูดง่ายๆ คือ โมเดลสามารถ *ทำถูกได้* แต่หากไม่ได้รับคำสั่งเพิ่มเติม มันจะเลือกทางที่ผิดก่อนเป็นปกติ

## กับดักสี่ประเภท

| กับดัก | ลักษณะอาการ | หลักการแก้ไข |
|---|---|---|
| **Hidden confusion** | เมื่อเจอคำสั่งที่กำกวมแล้วเดาเอาเองเงียบๆ แทนที่จะถาม | เปิดเผยสมมติฐาน และหากไม่แน่ใจให้ถาม |
| **Overcomplication** | ใส่ abstraction เผื่อ, ใส่ flag หรือ error handler เพื่อป้องกันสถานะที่ไม่มีทางเกิดขึ้น, เขียนโค้ด 200 บรรทัดในกรณีที่ 50 บรรทัดก็เพียงพอ | ทำเท่าที่จำเป็นเพื่อแก้ปัญหาจริงๆ |
| **Scope drift** | "ปรับปรุง" โค้ดข้างเคียง, จัดฟอร์แมตใหม่, refactor ส่วนที่ไม่เกี่ยวข้อง, ลบ dead code ที่มีอยู่ก่อน | แก้ไขแบบศัลยแพทย์ — ทุกบรรทัดต้องเชื่อมโยงกลับไปยังคำสั่งที่ได้รับ |
| **Weak success criteria** | ประกาศว่า "เสร็จแล้ว" โดยไม่ตรวจสอบ, เข้าใจว่าแค่รันผ่านก็เพียงพอ | ต้องมีเป้าหมายที่ชัดเจนและมีจุดที่สามารถตรวจสอบซ้ำได้ |

กับดักตัวที่สี่ (Weak success criteria) คือหน้าหนึ่งของปัญหา [[model-honesty|overclaiming progress]] — รีบบอกว่าเสร็จทั้งที่หลักฐานยังบาง [[anthropic|Anthropic]] ชูเรื่อง [[model-honesty|ความซื่อสัตย์]] เป็นจุดขายหลักของ [[claude-opus-4-8|Opus 4.8]] โดยบอกว่ามัน **ปล่อยให้ bug ใน code ที่ตัวเองเขียนผ่านไปโดยไม่ทักท้วง น้อยกว่ารุ่นก่อนราว 4 เท่า** — เป็นการพยายามแก้กับดักนี้ที่ระดับการฝึก ไม่ใช่แค่ที่ไฟล์คำสั่ง

## Mechanical edit failure (ไม่ใช่กับดักพฤติกรรม แต่คนมักสับสน)

[[can-boluk|Can Bölük]] เสริมอีกชั้น: model อาจ **เข้าใจงานถูกแล้ว** แต่ harness apply edit ไม่ผ่าน — `str_replace` พลาด whitespace, `apply_patch` ล้มเพราะ model ไม่คุ้น format, retry loop กิน token ทิ้ง ผู้ใช้เลยสรุปว่า "model แย่" ทั้งที่จริงคือ landing gear พัง

[[hashline|Hashline]] กับ benchmark ใน [[improved-15-llms-harness-changed]] ชี้ว่าปรับแค่ **edit tool format** อย่างเดียว ก็ดัน success rate ขึ้นได้เทียบเท่า upgrade model ในหลายเคส ดู [[edit-tool-formats]]

## สาเหตุ

LLM ถูกเทรนบนโค้ดที่เต็มไปด้วย defensive handling, abstraction, และ commit ที่เป็นการเก็บงาน เมื่อถึงเวลาทำงานจริง มันจึงไปจับภาพ "โค้ดที่ดูดี" แทนที่จะโฟกัสกับ "โค้ดที่ตรงกับโจทย์ที่อยู่ตรงหน้า" อีกมุมหนึ่งคือ โมเดลต้องการแสดงความสามารถ ซึ่งหมายความว่ามันจะได้คะแนนมากกว่าหากเดาแล้วตอบเลย แทนที่จะถามก่อน และทำกว้างๆ แทนที่จะทำให้แม่นยำแต่แคบ

## วิธีแก้ไข

แนวทางแก้ไขใน [[karpathy-guidelines]] ไม่ได้เป็นการแก้ไขที่ตัวโมเดล แต่ใช้ไฟล์คำสั่ง (`SKLL.md`, `CLAUDE.md`, `AGENTS.md`) ที่ให้อ่านเมื่อเริ่ม session ซึ่งเป็นวิธีคิดเดียวกับที่ Karpathy ใช้ใน [[llm-knowledge-bases]] — คือการใช้ schema แบบเบาๆ ในรูปแบบ markdown เป็น "สัญญาร่วม" ที่ทั้งคนและโมเดลยึดตาม โดยไม่ต้องพึ่งพา tooling ที่ซับซ้อน

ข้อแลกเปลี่ยนคือแนวทางเหล่านี้จะผลักดันให้โมเดลทำงานอย่างระมัดระวังมากกว่ารวดเร็ว ซึ่งอาจไม่จำเป็นสำหรับ task เล็กๆ

## เรื่องเล่าจากหน้างาน — บั๊ก Authorization (Nattee, 2026-04-17)

เคสจริงจาก Ep. 2 ของ [[nattee-niparnan|Nattee Niparnan]] ขณะทำ PoC Web App เป็นภาพที่ชัดเจนว่ากับดักหลายตัวเมื่อประกอบกันแล้วอันตรายเพียงใด

-   ทุก endpoint **ผ่าน unit test** และดูเหมือนไม่มีปัญหาเมื่อพิจารณาแยกกัน
-   แต่เมื่อถึง **integration test** กลับพบว่า Buyer สามารถลบ resource ของ Seller ได้
-   สาเหตุคือไม่มีใคร — ไม่ว่าจะเป็นคนหรือ Agent — ที่มอง authorization ในระดับ **ภาพรวมของทั้งระบบ** แต่ละ endpoint ถูกสร้างขึ้นมาอย่างแยกขาดจากกัน
-   เมื่อสั่งให้แก้ไข, Agent ก็สามารถจัดการทั้งระบบได้ใน commit เดียวโดยไม่มีปัญหา

นี่คือ *scope drift* แบบกลับด้าน — ไม่ใช่ Agent ที่ออกนอกคำสั่ง แต่เป็นการ **ยึดคำสั่งที่แคบเกินไป** จนพลาด invariant ในระดับข้ามโมดูล เมื่อรวมกับ *weak success criteria* ที่ถือว่า "unit test ผ่านก็พอ" และ *hidden confusion* ที่โมเดลเลือกตีความ authorization แบบแยกส่วนโดยไม่ถาม ผลลัพธ์ที่ได้คือโค้ดที่ดูเหมือนไม่มีปัญหาเมื่อมองทีละจุด แต่กลับพังเมื่อนำมาประกอบกัน

> "Agent มันไม่รู้หรอกว่าต้องแก้เรื่องนี้ ถ้าเราไม่สั่ง" — Nattee

บทเรียนคือ failure mode ของ LLM ไม่ได้เกิดขึ้นแยกกัน ขอบเขตที่แคบ, เกณฑ์การผ่านที่หละหลวม, และการตีความ default ที่ไม่เคยถูกท้าทาย สามารถรวมกันเป็น output ที่ดูน่าเชื่อถือแต่กลับทำลาย property แบบ cross-cutting อย่างเงียบๆ ทางออกจึงไม่ใช่การไล่แก้กับดักทีละตัว แต่ต้องชวน Agent พูดคุยเกี่ยวกับภาพรวมของระบบ ไม่ใช่แค่ส่วนย่อยที่สั่ง และนี่คือเหตุผลที่ชัดเจนที่สุดว่าทำไม [[taste-paradox]] ถึงมีความสำคัญ — เราไม่สามารถรีวิว property ที่เราไม่เคยถูกสอนให้มองหาได้

## ดูเพิ่มเติม

- [[karpathy-guidelines]]
- [[model-honesty]]
- [[andrej-karpathy]]
- [[harness-engineering]]
- [[llm-knowledge-bases]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
- [[edit-tool-formats]]
- [[hashline]]
- [[improved-15-llms-harness-changed]]
