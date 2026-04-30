---
title: thClaws
type: entity
tags: [project, rust, ai, agent, open-source]
created: 2026-04-27
updated: 2026-04-30
sources: [thclaws-announcement-panutat.md, panutat-tejasen-thclaws-positioning.md, thclaws-marketplace-panutat.md]
---

# thClaws / โปรเจกต์แกะรอย Claude Code

**thClaws** คือโปรเจกต์ Open-source ที่เขียนด้วยภาษา Rust โดยเป็นการทำ "Clean Room Port" หรือการแกะเอา logic หัวใจหลักของ [[claude-code]] มาเขียนใหม่ เพื่อศึกษาว่าระบบ AI Agent ระดับโลกเขาสร้างกันยังไง

## จุดยืนและแนวคิด (Positioning)
thClaws วางตัวเป็น AI Application ที่พัฒนาร่วมกับผู้ใช้อย่างใกล้ชิด โดยเน้นความคล่องตัวและการแก้ปัญหาจริงที่ผลิตภัณฑ์ระดับโลก (Cloud-first) มักมองข้าม

- **Governance over Code:** [[panutat-tejasen|Panutat]] เชื่อว่าหัวใจของ Open source ในปี 2026 คือเรื่องของ Governance — "ใครเป็นคนตัดสินใจว่าจะชิปอะไร?" thClaws ไม่มี gatekeeper หรือ vendor agenda ทำให้สามารถตอบสนองต่อความต้องการของ user ได้ทันที
- **Enterprise-Ready Governance:** ในเวอร์ชัน 0.7.0 ได้เพิ่มระบบ **thClaws Marketplace** เพื่อจัดการ Skills, MCP และ Plugins โดยเน้นเรื่องความปลอดภัยและการควบคุมข้อมูลรั่วไหลผ่าน Private Marketplace สำหรับองค์กร

## ข้อมูลทางเทคนิค
- **ภาษาที่ใช้:** Rust (เน้นความเร็วและความปลอดภัย)
- **ขนาดโปรเจกต์:** ประมาณ 36,000 บรรทัด (ในขณะที่ Claude Code ตัวเต็มมี code รวมๆ กว่า 500,000 บรรทัด)
- **Host Bridge:** เทคนิคการเชื่อมต่อกับ Browser เพื่อให้ Agent สามารถสร้างและรัน Dashboard (HTML/JS) ในการแสดงผลและจัดการข้อมูลในเครื่องได้

## ส่วนประกอบสำคัญ (Harness Components)
thClaws พยายามดึงเอาส่วนที่เป็น infrastructure สำคัญออกมา:
- **Agentic Loop:** วงจรที่ทำให้ AI คิด-ทำ-แก้ จนกว่างานจะเสร็จ
- **Tool Routing & Sub-agent Dispatch:** การฉีดเครื่องมือให้ AI ใช้ และการส่งงานต่อให้ลูกน้อง (sub-agent)
- **Sandbox:** ระบบจัดการความปลอดภัย ไม่ให้ AI รัน code มั่วซั่วจนพังเครื่อง
- **[[context-compaction|Context Compaction]]:** เทคนิคการบีบอัดความจำ เพื่อให้คุยกับ AI ได้ยาวๆ โดยไม่เปลือง token
- **Agent Teams:** ระบบที่ให้ Agent หลายๆ ตัวช่วยกันทำงานเป็นทีม
- **Marketplace:** ระบบแจกจ่ายและควบคุมส่วนขยาย (Extensions)

## ประวัติการพัฒนาและฟีเจอร์เด่น
- **v0.4.0:** เพิ่ม Caret-aware editing ใน terminal
- **v0.4.2:** เพิ่ม User-defined context-window overrides
- **v0.7.0:** เปิดตัว **thClaws Marketplace** รองรับ Skills, MCP, Plugins และ Private Marketplace สำหรับองค์กร


## ดูเพิ่ม
- [[panutat-tejasen]]
- [[harness-engineering]]
- [[claude-code]]
- [[product-overhang]]
- [[open-source-governance]]
