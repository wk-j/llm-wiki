---
title: thClaws Positioning - Open Source Governance
type: source
tags: [thclaws, open-source, governance, product-strategy, thai]
created: 2026-04-27
updated: 2026-04-27
sources: [facebook.com/panutat.tejasen]
---

# thClaws Positioning: Open Source ในปี 2026 / ภานุทัต เตชะเสน

โพสต์โดย [[panutat-tejasen|Panutat Tejasen]] เล่าถึงจุดยืนของ [[thclaws]] ในฐานะโปรเจกต์ Open-source ที่เน้นการตอบสนองต่อผู้ใช้อย่างรวดเร็วและการตัดสินใจที่ไร้ตัวกลาง (Governance)

## สรุปประเด็นสำคัญ

### 1. การแก้ปัญหาจากการใช้งานจริง (User-Driven Roadmap)
- ยกตัวอย่าง **Issue #30** โดย Chawasit Tengtrairatana: ปัญหา VRAM ไม่พอ (OOM) เมื่อรัน model ใหญ่บน Ollama ใน Windows
- **วิธีแก้:** เพิ่มฟีเจอร์ User-defined context-window overrides เพื่อให้ user กำหนด context window ของแต่ละ model ได้เอง
- **ความเร็ว:** แก้ไขและชิปเวอร์ชั่น 0.4.2 ภายในเวลาประมาณ 1 ชั่วโมงหลังจากได้รับแจ้งปัญหา

### 2. Open Source คือเรื่องของ Governance
- Panutat เสนอว่าสิ่งที่ทำให้ Open source แตกต่างจริงๆ ในปี 2026 ไม่ใช่แค่ "เปิด code" แต่คือ **Governance (ใครเป็นคนตัดสินใจว่าจะชิปอะไร)**
- Cloud-first products (ยักษ์ใหญ่) มักไม่ชิปฟีเจอร์ให้ user กลุ่มน้อย (เช่น คนรัน Ollama บน GPU รุ่นเก่า) แต่ thClaws ทำได้ทันที

### 3. การเก็บตก Papercut Features
- ยกตัวอย่าง **PR #22** โดย siharat-th: การทำให้ terminal รองรับ caret-aware editing (ปุ่มลูกศร, Home, End, Ctrl-A/E)
- ฟีเจอร์เล็กๆ ที่ IDE ใหญ่ๆ มักมองข้ามเพราะเน้น GUI-first แต่สำคัญมากสำหรับคนใช้ terminal (CLI-first)

### 4. จุดยืนและขั้นตอนการร่วมพัฒนา
- เจอ bug/อยากได้ feature → file issue
- มีเวลา → ส่ง PR
- ไม่มี gatekeeper, ไม่มี vendor agenda เน้นที่ codebase และคนใช้ร่วมกันพัฒนา

## Takeaways สำหรับนักพัฒนา
- **Speed is a differentiator:** การชิปฟีเจอร์รวดเร็วเพื่อแก้ปัญหาจริงคือจุดแข็งของ Open Source
- **Niche matters:** การตอบโจทย์ผู้ใช้กลุ่มเฉพาะที่ยักษ์ใหญ่ไม่สน คือโอกาสในการสร้างความแตกต่าง
- **Governance over Code:** ความโปร่งใสในการตัดสินใจดึงดูด contributor ได้ดี
