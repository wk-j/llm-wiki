---
title: Zed Industries
type: entity
tags: [company, editor, tech, open-source]
created: 2026-04-25
updated: 2026-08-15
sources: [zed-acp-protocol.md, zed-is-1-0.md, software-is-made-between-commits.md]
---

# Zed Industries

**Zed Industries** คือทีมพัฒนาที่อยู่เบื้องหลัง [[zed]], โค้ดเอดิเตอร์ (Code Editor) ประสิทธิภาพสูงที่เขียนด้วยภาษา [[rust]] ซึ่งเน้นความเร็วและการทำงานร่วมกัน (collaboration) ก่อตั้งโดยทีมผู้สร้าง [[atom]] และ [[vscode|Electron]] (Nathan Sobo และคณะ)

## ผลงานสำคัญ (Key Achievements)

- **[[zed]] 1.0**: ประกาศเปิดตัวเวอร์ชัน 1.0 อย่างเป็นทางการเมื่อวันที่ 29 เมษายน 2026 รองรับทั้ง macOS, Windows และ Linux
- **Agent Client Protocol (ACP):** ผู้ริเริ่มมาตรฐานเปิด [[agent-client-protocol|ACP]] ร่วมกับ [[jetbrains|JetBrains]] เพื่อเชื่อมต่อ AI Agent เข้ากับ IDE
- **[[gpui]]**: พัฒนา UI framework ประสิทธิภาพสูงที่ใช้ GPU ในการวาดภาพ
- **[[deltadb]]**: สร้างระบบ sync ข้อมูลที่ใช้ [[crdts]] เพื่อรองรับการทำงานร่วมกันระหว่างมนุษย์และ AI Agent

## DeltaDB และ collaboration ก่อน commit

ใน [[software-is-made-between-commits|Software Is Made Between Commits]] บริษัทวาง [[deltadb|DeltaDB]] เป็น version control สำหรับงานที่เกิดระหว่าง commit ไม่ได้เก็บแค่ snapshot แต่เก็บ operation ย่อย บทสนทนากับ edit และ shared worktree ที่คนกับ agent แก้พร้อมกันได้

บทความของ [[nathan-sobo|Nathan Sobo]] ยังวิจารณ์ PR ในฐานะพื้นที่หลักของ collaboration แต่ไม่ได้เสนอให้เลิก Git หรือ CI เขาวางสองอย่างหลังไว้เป็นชั้นตรวจและเชื่อมกับโลกภายนอก ส่วน conversation กับ code ควรอยู่ด้วยกันตั้งแต่งานยังไม่เสร็จ

## See also

- [[agent-client-protocol|Agent Client Protocol (ACP)]]
- [[rust|ภาษา Rust (ที่ใช้พัฒนา Zed)]]
- [[helix|Helix (เอดิเตอร์คู่แข่งที่เน้นความเร็วเช่นกัน)]]
- [[nathan-sobo]]
- [[conversation-code-provenance]]
