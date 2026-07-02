---
title: Agentic Search
type: concept
tags: [claude-code, search, workflow, agents]
created: 2026-05-04
updated: 2026-07-03
sources: [anthropic-engineer-claude-code, why-im-against-claude-codes-grep-only-retrieval.md]
---

# Agentic Search / การค้นหาแบบ Agentic

Agentic Search คือวิธีการที่ AI agent ทำความเข้าใจและค้นหาข้อมูลใน codebase โดยใช้เครื่องมือพื้นฐานบน terminal (เช่น `grep`, `glob`, `find`) ในลักษณะเดียวกับที่วิศวกรที่เป็นมนุษย์ทำเมื่อเข้าไปในโปรเจกต์ใหม่ แทนที่จะใช้การสร้าง index (indexing) หรือระบบ RAG (Retrieval-Augmented Generation) แบบดั้งเดิม

ชื่อนี้ใน wiki นี้หมายถึง **agent ค้น codebase เอง** ไม่ใช่ consumer AI search แบบ [[perplexity|Perplexity]] หรือ Google AI Overviews. ถ้าพูดถึง product ที่ตอบคำถามพร้อม citation ให้ดู [[answer-engine|answer engine]] และ [[ai-search-economics|AI search economics]]

## แก่นความคิด

แนวคิดหลักคือการ "ให้ agent ค้นหาเอง" โดย agent จะลงมือทำเป็นลูป:
1. ใช้คำสั่งค้นหาคร่าวๆ
2. อ่านผลลัพธ์
3. วิเคราะห์ว่า "ฉันยังต้องรู้อะไรอีกไหม?"
4. ทำการค้นหาที่เจาะจงขึ้นตามผลลัพธ์ก่อนหน้า

วิธีนี้ทำให้ agent สามารถสำรวจ codebase ได้อย่างเป็นธรรมชาติ ยืดหยุ่น และไม่จำเป็นต้องสร้าง infrastructure หนักๆ เพื่อ index โค้ดทั้งหมดก่อนใช้งาน

## การนำไปใช้ใน Claude Code

[[claude-code|Claude Code]] ถูกออกแบบมาให้เป็น "pure agent" ที่พึ่งพา Agentic Search อย่างเต็มที่ [[cal-rueb|Cal Rueb]] อธิบายว่าแทนที่ผู้ใช้จะสั่งให้แก้บั๊กทันที วิธีที่ดีที่สุดคือการให้ Claude Code ทำตัวเป็น "thought partner" โดยสั่งให้มันค้นหา (search around) ทำความเข้าใจปัญหา และเสนอแผนการแก้ไข (plan) ออกมาก่อน 2-3 ทางเลือกโดยยังไม่ต้องเขียนไฟล์ใดๆ

## ข้อจำกัดและคำวิจารณ์ (The Critique)

แม้ Agentic Search จะยืดหยุ่น แต่ก็ถูกวิจารณ์จากสาย [[semantic-retrieval]] (เช่น ทีม [[milvus]]) ในเรื่องประสิทธิภาพเมื่อใช้กับ codebase ขนาดใหญ่:

- **Token Bloat:** การที่ agent ต้อง "ลองผิดลองถูก" ด้วย grep มักจบลงด้วยการดึง code ที่ไม่เกี่ยวข้องจำนวนมากเข้าสู่ context window ทำให้สิ้นเปลือง token
- **Time Tax:** ลูปการค้นหาแบบ "Twenty Questions" (ถาม-ตอบซ้ำๆ) ใช้เวลานานและมีค่าใช้จ่าย API สูงกว่าการค้นหาครั้งเดียวใน vector database
- **Keyword Blindness:** หากหาคำไม่ตรงเป๊ะ (เช่น หา "auth" แต่ในโค้ดใช้ "verify_session") Agentic Search อาจหาไม่เจอเลย

ทางแก้ที่ถูกเสนอคือการใช้ **Hybrid Search** หรือการเสริมด้วย [[semantic-retrieval]] เพื่อให้ agent เข้าถึง context ที่ถูกต้องได้แม่นยำขึ้นในครั้งเดียว

## See also
- [[claude-code]]
- [[coding-harness]]
- [[semantic-retrieval]]
- [[token-optimization]]
- [[answer-engine]]
- [[ai-search-economics]]
