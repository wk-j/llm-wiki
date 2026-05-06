---
title: Agentic Search
type: concept
tags: [claude-code, search, workflow, agents]
created: 2026-05-04
updated: 2026-05-04
sources: [This Anthropic Engineer Uses Claude Code Differently Than Everyone Else.md]
---

# Agentic Search / การค้นหาแบบ Agentic

Agentic Search คือวิธีการที่ AI agent ทำความเข้าใจและค้นหาข้อมูลใน codebase โดยใช้เครื่องมือพื้นฐานบน terminal (เช่น `grep`, `glob`, `find`) ในลักษณะเดียวกับที่วิศวกรที่เป็นมนุษย์ทำเมื่อเข้าไปในโปรเจกต์ใหม่ แทนที่จะใช้การสร้าง index (indexing) หรือระบบ RAG (Retrieval-Augmented Generation) แบบดั้งเดิม

## แก่นความคิด

แนวคิดหลักคือการ "ให้ agent ค้นหาเอง" โดย agent จะลงมือทำเป็นลูป:
1. ใช้คำสั่งค้นหาคร่าวๆ
2. อ่านผลลัพธ์
3. วิเคราะห์ว่า "ฉันยังต้องรู้อะไรอีกไหม?"
4. ทำการค้นหาที่เจาะจงขึ้นตามผลลัพธ์ก่อนหน้า

วิธีนี้ทำให้ agent สามารถสำรวจ codebase ได้อย่างเป็นธรรมชาติ ยืดหยุ่น และไม่จำเป็นต้องสร้าง infrastructure หนักๆ เพื่อ index โค้ดทั้งหมดก่อนใช้งาน

## การนำไปใช้ใน Claude Code

[[claude-code|Claude Code]] ถูกออกแบบมาให้เป็น "pure agent" ที่พึ่งพา Agentic Search อย่างเต็มที่ [[cal-rueb|Cal Rueb]] อธิบายว่าแทนที่ผู้ใช้จะสั่งให้แก้บั๊กทันที วิธีที่ดีที่สุดคือการให้ Claude Code ทำตัวเป็น "thought partner" โดยสั่งให้มันค้นหา (search around) ทำความเข้าใจปัญหา และเสนอแผนการแก้ไข (plan) ออกมาก่อน 2-3 ทางเลือกโดยยังไม่ต้องเขียนไฟล์ใดๆ

ผลคือผู้ใช้สามารถตรวจสอบแผนได้ว่า agent เข้าใจบริบทถูกต้องจากการค้นหาหรือไม่ ก่อนที่จะปล่อยให้ลงมือแก้โค้ดจริงๆ

## See also
- [[claude-code]]
- [[coding-harness]]
