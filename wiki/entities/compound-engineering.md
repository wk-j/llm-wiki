---
title: Compound Engineering
type: entity
tags: [ai-tool, agent-framework, every-inc]
created: 2026-04-29
updated: 2026-04-29
sources: [compound-engineering-v3-3-0.md]
---

# Compound Engineering / คอมพาวด์ เอนจิเนียริง

Compound Engineering เป็นชุดเครื่องมือ (skills) สำหรับ AI agent ที่พัฒนาโดย [[every-inc]] เน้นไปที่การทำให้ agent ทำงานร่วมกับมนุษย์ได้อย่างมีประสิทธิภาพ ลดช่องว่างของการตีความผิด (alignment drift) และเพิ่มความเร็วในการส่งมอบงาน

## แนวคิดหลัก

เป้าหมายสูงสุดของ Compound Engineering คือการสร้าง agent ที่ **"cheaper to correct and faster to trust"** (แก้ให้ถูกได้ง่ายขึ้นและน่าไว้ใจเร็วขึ้น) ผ่านกลไกต่าง ๆ ดังนี้:

- **Show Thinking before Acting:** Agent จะหยุดเพื่อสรุปสิ่งที่เข้าใจให้ผู้ใช้ฟังก่อนจะเริ่มงานใหญ่ที่ต้องใช้เวลานาน เพื่อป้องกันการเสียเวลาไปกับสมมติฐานที่ผิด
- **[[playback-pattern|Playback Pattern]]:** การแจกแจงสิ่งที่ได้รับมอบหมายออกมาเป็น 3 ส่วน: Stated (สิ่งที่สั่ง), Inferred (สิ่งที่ agent เดาเพิ่ม), และ Out-of-scope (สิ่งที่ agent จะไม่ทำ)
- **[[grounding|Grounding]]:** การอ้างอิงหลักฐาน (evidence) ทุกครั้งที่เสนอไอเดีย เพื่อให้ผู้ใช้รู้ว่า agent ไม่ได้ "มโน" (hallucinate) ขึ้นมาเอง
- **Reducing Ceremony:** การลดการขัดจังหวะ (interruption) ในเรื่องที่ชัดเจนอยู่แล้ว โดยให้ agent ตัดสินใจแก้ไขเอง (autonomous fix) ในเคสที่เป็น obvious choices

## เครื่องมือสำคัญ (Skills)

| Skill | หน้าที่ | การอัปเดตใน v3.3.0 |
| :--- | :--- | :--- |
| `/ce-plan` | วางแผนการ implementation | ใช้ Playback Pattern ก่อนเริ่มงาน |
| `/ce-ideate` | ช่วยคิดไอเดียและแนวทางแก้ปัญหา | ถาม scoping questions ล่วงหน้าและทำ grounding |
| `/ce-doc-review` | ตรวจสอบเอกสาร | แก้ไขจุดที่ผิดให้ทันที (automated fix) สำหรับเรื่องที่ชัดเจน |
| `/ce-code-review` | ตรวจสอบโค้ด | แก้ไข finding เล็ก ๆ น้อย ๆ ให้เลย แทนที่จะแค่สร้าง ticket |

## See also

- [[every-inc]]
- [[trevin]]
- [[playback-pattern]]
