---
title: Agent Client Protocol (ACP) / โปรโตคอล ACP
type: concept
tags: [ai, protocol, coding, automation, standard]
created: 2026-04-25
updated: 2026-04-26
sources: [zed-acp-protocol.md, agent-client-protocol-docs.md]
---

# Agent Client Protocol (ACP) / โปรโตคอล ACP

**Agent Client Protocol (ACP)** คือมาตรฐานเปิด (open standard) สำหรับการสื่อสารระหว่าง AI Agent กับ Code Editor (IDE) พัฒนาโดย [[zed-industries|Zed Industries]] และ [[jetbrains|JetBrains]] เพื่อแก้ปัญหาความกระจัดกระจายของเครื่องมือ AI ในปัจจุบัน

## แก่นความคิด (Core Concepts)

1.  **Universal Adapter:** ทำหน้าที่เป็นตัวกลางให้ AI Agent ตัวใดก็ได้สามารถทำงานร่วมกับ Editor ตัวใดก็ได้ที่รองรับ ACP (คล้ายกับที่ [[tree-sitter|LSP]] ทำกับภาษาโปรแกรม)
2.  **Interactive Workflow:** แทนที่จะเป็นการคุยผ่าน Chat แล้ว copy โค้ดมาวาง ACP ช่วยให้ Agent สามารถเสนอการแก้ไขโค้ดได้โดยตรง (live proposals) พร้อมระบบ Diff ที่ผู้ใช้กด Accept/Reject ได้เป็นบรรทัด
3.  **Brain Swapping:** ผู้ใช้สามารถเปลี่ยนโมเดล AI หรือ Agent "สมอง" ที่ใช้อยู่ได้โดยไม่ต้องเปลี่ยนวิธีใช้งานหรือเปลี่ยน Editor
4.  **Standardized Messaging:** ใช้ JSON-RPC 2.0 ในการรับส่งข้อมูลผ่าน `stdio` (สำหรับ local) หรือ WebSocket/HTTP (สำหรับ remote)

## รายละเอียดทางเทคนิค (Technical Details)

- **MCP Alignment:** ACP ถูกออกแบบมาให้ใช้งานร่วมกับ [[model-context-protocol|Model Context Protocol (MCP)]] ได้ โดยมีการ re-use JSON representations จาก MCP ในจุดที่ทำได้
- **Markdown-first:** ข้อมูลที่เป็นตัวอักษรจะใช้ Markdown เป็นหลักเพื่อให้แสดงผลได้อย่างสวยงามในทุก Editor
- **Permission-based:** Editor จะเป็นคนคุมสิทธิ์การเข้าถึง File System หรือ Terminal โดย Agent ต้องขออนุญาตก่อนทำงานที่สำคัญ
- **Session-centric:** รองรับการทำงานหลาย Session พร้อมกัน มีระบบ Cancellation และ Streaming updates

## ระบบนิเวศ (Ecosystem)

- **Editors:** Zed (Native), JetBrains (IntelliJ, PyCharm), Neovim, Emacs
- **Agents:** Gemini CLI (Reference Implementation), Claude Code, GitHub Copilot CLI
- **SDKs:** รองรับทั้ง TypeScript, Python, Rust, Java และ Kotlin

## See also

- [[model-context-protocol|Model Context Protocol (MCP)]]
- [[zed-industries|Zed Industries (ทีมผู้สร้าง)]]
- [[coding-harness|เครื่องมือช่วยเขียนโค้ด (Coding Harness)]]
