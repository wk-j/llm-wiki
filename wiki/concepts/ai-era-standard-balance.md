---
title: AI-era Standard Balance
type: concept
tags: [ai, productivity, standards, workflow]
created: 2026-05-25
updated: 2026-05-25
sources: [fundamental-productivity-ai-world.md]
---

# AI-era Standard Balance / สมดุลของ standard ในยุค AI

AI-era Standard Balance คือโจทย์ว่า standard เดิมยัง balance ภาระระหว่าง producer กับ consumer อยู่ไหม เมื่อ AI ทำให้ฝั่ง producer สร้าง artifact ตามฟอร์มได้ง่ายขึ้นมาก

แนวคิดนี้มาจาก [[chrisza-stuff|ChrisZa Stuff]] ใน [[fundamental-productivity-ai-world|Fundamental of productivity in AI world]] เขาชี้ว่า standard ที่ดีควรไม่ผลักภาระไปฝั่งใดฝั่งหนึ่งมากเกินไป แต่ AI เปลี่ยนต้นทุนของสองฝั่งไม่เท่ากัน

## Standard ก่อน AI ทำงานอย่างไร

ก่อน AI ทีมใช้ standard เพื่อให้คนส่งงานและคนรับงานไม่ต้องคุยกันทุกจังหวะ เช่น requirement template, UML diagram, coding convention, design spec หรือ review checklist

ถ้าทั้งสองฝ่ายรู้ standard เดียวกัน producer ก็ส่งงานตามฟอร์ม และ consumer ก็อ่านตามฟอร์มได้ องค์กรจึงพอ infer individual productivity จาก output ของแต่ละคนได้ เพราะเชื่อว่า standard กลางพอสำหรับการส่งต่อ

ผลคือ: standard ทำหน้าที่เป็น interface ระหว่างคน

## ทำไม AI ทำให้ balance เพี้ยน

AI ทำให้การ conform to standard ถูกลงมาก ถ้า template มี 4 หัวข้อ producer สามารถให้ AI สร้างเอกสาร 100 ชิ้นตามฟอร์มได้เร็ว แต่ consumer ยังต้องอ่าน ตรวจ เชื่อมกับบริบท และยอมรับความรับผิดชอบเอง

ดังนั้น standard ที่เคย fair อาจกลายเป็น standard ที่เอื้อให้ producer ผลิตล้น แต่โยนภาระให้ consumer

นี่คืออีกมุมหนึ่งของ [[acceptance-bottleneck|Acceptance Bottleneck]]: standard ที่ดีในยุค AI ต้องช่วยจุด accept ด้วย ไม่ใช่แค่ช่วยจุด produce

## Standard ใหม่ควรหน้าตาอย่างไร

standard ใหม่ควรวัดจากการลด friction ใน [[interaction-productivity|Interaction Productivity]] เช่น ช่วยให้คนรับเห็น risk ก่อน เห็น decision point ชัดขึ้น เห็น evidence ที่ต้องตรวจ และเห็นสิ่งที่อยู่นอก scope

ตัวอย่าง pattern ที่เข้าทางนี้:

- [[playback-pattern|Playback Pattern]] ที่แยก Stated, Inferred, Out-of-scope ก่อนเริ่มงาน
- [[dual-axis-code-review|Dual-Axis Code Review]] ที่แยก standards กับ spec fidelity
- [[html-artifacts|HTML Artifacts]] ที่เพิ่ม information density ให้คนอ่านเข้าใจเร็วขึ้น
- acceptance criteria ที่สั้น ชัด และตรวจได้

ได้อะไร: standard ใหม่ต้อง optimize การรับงาน ไม่ใช่ optimize การสร้างเอกสาร

## ความเชื่อมโยงกับ Process Drag

[[thorsten-ball|Ball]] ใน [[software-after-software]] เสนอ frame ใกล้กันใน [[process-drag|Process Drag]] — ritual เก่าที่เคยช่วยอาจกลายเป็นแรงต้านในยุค AI ความต่างคือ Ball เน้นที่ ritual ระดับองค์กร (planning, prioritization, review) ส่วน ChrisZa เน้นที่ standard ระดับ artifact (template, convention, checklist)

สองอันทำงานพร้อมกัน: เปลี่ยน standard อย่างเดียวไม่พอถ้า ritual ที่ใช้ standard ยังเดิม

## See also

- [[interaction-productivity]]
- [[acceptance-bottleneck]]
- [[playback-pattern]]
- [[dual-axis-code-review]]
- [[html-artifacts]]
- [[process-drag]]
- [[software-after-software]]
