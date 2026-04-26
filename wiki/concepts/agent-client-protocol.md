---
title: Agent Client Protocol (ACP) / โปรโตคอล ACP
type: concept
tags: [ai, protocol, coding, automation, standard]
created: 2026-04-25
updated: 2026-04-25
sources: [zed-acp-protocol.md]
---

# Agent Client Protocol (ACP) / โปรโตคอล ACP

**Agent Client Protocol (ACP)** คือมาตรฐานเปิด (open standard) สำหรับการสื่อสารระหว่าง AI Agent กับ Code Editor (IDE) พัฒนาโดย [[zed-industries|Zed Industries]] เพื่อแก้ปัญหาความกระจัดกระจายของเครื่องมือ AI ในปัจจุบัน

## แก่นความคิด (Core Concepts)

1.  **Universal Adapter:** ทำหน้าที่เป็นตัวกลางให้ AI Agent ตัวใดก็ได้สามารถทำงานร่วมกับ Editor ตัวใดก็ได้ที่รองรับ ACP (คล้ายกับที่ [[tree-sitter|LSP]] ทำกับภาษาโปรแกรม)
2.  **Interactive Workflow:** แทนที่จะเป็นการคุยผ่าน Chat แล้ว copy โค้ดมาวาง ACP ช่วยให้ Agent สามารถเสนอการแก้ไขโค้ดได้โดยตรง (live proposals) พร้อมระบบ Diff ที่ผู้ใช้กด Accept/Reject ได้เป็นบรรทัด
3.  **Brain Swapping:** ผู้ใช้สามารถเปลี่ยนโมเดล AI หรือ Agent "สมอง" ที่ใช้อยู่ได้โดยไม่ต้องเปลี่ยนวิธีใช้งานหรือเปลี่ยน Editor
4.  **Standardized Messaging:** ใช้ JSON-RPC ในการรับส่งข้อมูล ทำให้ง่ายต่อการสร้าง Agent ใหม่ๆ มาเชื่อมต่อ

## ทำไมถึงสำคัญ (Why it matters)

- **ลด Fragmentation:** ไม่ต้องเขียนปลั๊กอินแยกสำหรับทุก Editor
- **AI as First-Class Citizen:** AI ไม่ได้เป็นแค่แชทข้างหน้าจอ แต่เข้ามาเป็นส่วนหนึ่งของสภาพแวดล้อมการทำงาน (IDE DNA)
- **Open Ecosystem:** ป้องกันปัญหา Editor Lock-in ทำให้ผู้ใช้มีอิสระในการเลือกใช้เครื่องมือ AI ที่ดีที่สุด

## See also

- [[model-context-protocol|Model Context Protocol (MCP)]]
- [[zed-industries|Zed Industries (ทีมผู้สร้าง)]]
- [[coding-harness|เครื่องมือช่วยเขียนโค้ด (Coding Harness)]]
