---
title: HTML Artifacts
type: concept
tags: [html, communication, visualization, claude-code, artifacts]
created: 2026-05-09
updated: 2026-05-09
sources: [thariq-html-effectiveness.md]
---

# HTML Artifacts / การสื่อสารผ่าน HTML Artifact

**HTML Artifacts** คือแนวคิดการใช้ไฟล์ HTML เป็นสื่อกลางหลัก (Primary Medium) ในการสื่อสารระหว่าง AI Agents และมนุษย์ แทนที่จะใช้เพียง Markdown หรือข้อความธรรมดา เพื่อเพิ่มความหนาแน่นของข้อมูลและความเข้าใจที่ตรงกัน

## แก่นความคิด
ในขณะที่ซอฟต์แวร์มีความซับซ้อนมากขึ้น แผนงานหรือเอกสาร (Specs) ในรูปแบบ Markdown มักจะอ่านยากเมื่อมีความยาวเกิน 100 บรรทัด การใช้ HTML ช่วยให้ AI สามารถ:
- **แสดงผลข้อมูลที่ซับซ้อน**: ใช้ Table, SVG (สำหรับ diagram), และ CSS เพื่อจัดกลุ่มข้อมูลให้ดูง่าย
- **สร้างความชัดเจนทางสายตา**: ใช้ Tab, Link, และ Navigation อื่นๆ เพื่อช่วยให้มนุษย์ไล่เรียงเนื้อหาได้เร็วขึ้น
- **โต้ตอบได้ (Interactivity)**: ใส่ JavaScript เพื่อให้มนุษย์สามารถปรับจูนค่าต่างๆ (เช่น slider ปรับความเร็ว animation) แล้วส่งผลลัพธ์กลับไปให้ AI

## ทำไมถึงสำคัญในยุค AI
1. **Staying in the Loop**: ช่วยให้มนุษย์ยังคง "เข้าใจ" สิ่งที่ AI กำลังทำอยู่ได้ลึกซึ้งขึ้น ลดปัญหา [[cognitive-debt]]
2. **High Information Density**: HTML สามารถบรรจุรายละเอียดได้มากกว่าในพื้นที่เท่ากัน ทำให้ลดจำนวนรอบในการถามตอบ (Turns)
3. **Sharing**: แชร์ผ่าน Browser ได้ง่าย ทำให้คนอื่นในองค์กร (ที่ไม่ใช้ CLI) สามารถร่วมตรวจสอบ Specs ได้

## การประยุกต์ใช้
- **Planning**: สร้างแผนงานที่มาพร้อม Mockup และ Flowchart ในหน้าเดียว
- **Code Review**: แสดง Diff ของโค้ดพร้อมคำอธิบาย (Annotations) และการแยกสีตามความรุนแรงของปัญหา
- **Reports**: สรุปข้อมูลจากหลายแหล่ง (Slack, Linear, Git) มาเป็น Dashboard ที่สวยงามและอ่านง่าย

## ข้อดี/ข้อเสีย
- **ข้อดี**: อ่านง่ายกว่า Markdown มาก, สื่อสารได้หลายมิติ, แชร์สะดวก
- **ข้อเสีย**: ใช้ Token เปลืองกว่า (แต่ไม่ใช่ปัญหาสำหรับ 1M Context), ใช้เวลาสร้างนานกว่า 2-4 เท่า, ตรวจสอบ Diff ใน Git ได้ยาก

## ดูเพิ่ม
- [[claude-code]]
- [[custom-editing-interfaces]]
- [[cognitive-debt]]
- [[thariq-html-effectiveness]]
