---
title: JetBrains
type: entity
tags: [company, software, ide, jetbrains, acp, ai]
created: 2026-04-26
updated: 2026-06-05
sources: [Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md]
---

# JetBrains

**JetBrains** เป็นบริษัทซอฟต์แวร์ที่เชี่ยวชาญด้านการสร้างเครื่องมือสำหรับนักพัฒนา โดยเฉพาะ Integrated Development Environments (IDEs) เช่น IntelliJ IDEA, PyCharm, และ WebStorm

## ความเกี่ยวข้องกับ AI และ ACP

- **Agent Client Protocol (ACP):** เป็นผู้ร่วมพัฒนามาตรฐานเปิด [[agent-client-protocol|ACP]] ร่วมกับ [[zed-industries|Zed Industries]] เพื่อรองรับ AI Agent ใน IDE ของตน
- **AI Assistant:** มีบริการ AI ของตัวเองที่ฝังอยู่ใน IDE ต่างๆ
- **[[mellum2|Mellum2]]:** เปิด model 12B ภายใต้ Apache 2.0 สำหรับ routing, summarization, RAG, subagent, และ private AI deployment ใน workflow ของ software engineering ดู [[mellum2-goes-open-source]]

## มุมใหม่จาก Mellum2

Mellum2 ทำให้ JetBrains ขยับจาก editor/protocol ไปแตะ model layer โดยตรงด้วย แนวคิดที่บริษัทชูคือ [[focal-models|focal model]]: model เฉพาะทางที่เร็วและคุมต้นทุนได้ สำหรับขั้นตอนถี่ ๆ ในระบบ AI แทนที่จะใช้ frontier model ทำทุกอย่าง

**ผลคือ:** JetBrains กำลังวางตัวเป็นผู้ทำทั้ง IDE surface, agent protocol, และ model เฉพาะงานสำหรับ developer workflow

## ผลิตภัณฑ์หลัก

- IntelliJ IDEA (Java/Kotlin)
- PyCharm (Python)
- WebStorm (JavaScript/TypeScript)
- Fleet (Next-generation IDE)

## See also

- [[agent-client-protocol]]
- [[mellum2]]
- [[focal-models]]
