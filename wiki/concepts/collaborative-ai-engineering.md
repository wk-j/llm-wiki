---
title: Collaborative AI Engineering
type: concept
tags: [ai, engineering, collaboration, team, agents]
created: 2026-04-28
updated: 2026-08-15
sources: [maggie-appleton-collaborative-ai-engineering.md, software-is-made-between-commits.md]
---

# Collaborative AI Engineering / วิศวกรรม AI แบบร่วมมือกัน

**Collaborative AI Engineering** คือแนวคิดการพัฒนาซอฟต์แวร์ที่เปลี่ยนจากการใช้ AI Agent เพื่อเพิ่มผลิตภาพรายบุคคล (Individual Productivity) ไปสู่การสร้างระบบที่ Agent และมนุษย์หลายคนสามารถทำงานร่วมกันอย่างสอดประสาน

## ปัญหาของแนวทางปัจจุบัน (The Solo Story)

[[maggie-appleton]] ชี้ให้เห็นว่าเครื่องมือ AI ในปัจจุบัน (เช่น [[claude-code|Claude Code]], Terminal-based agents) มักเป็น "Single Player" ซึ่งนำไปสู่ปัญหา:
- **Duplicate Work**: ต่างคนต่างสั่ง Agent ทำงานที่ซ้ำซ้อนกัน
- **Conflicting Changes**: Agent ของแต่ละคนแก้ไข code ในจุดที่ขัดแย้งกันโดยไม่มีใครรู้
- **Coordination Debt**: หนี้จากการประสานงานที่เพิ่มขึ้นเมื่อ Agent สร้าง code ปริมาณมหาศาลออกมาเร็วเกินกว่าที่คนจะอ่านทัน

## เสาหลักของความร่วมมือ

1. **Shared Context**: ทุกคนในทีมและ Agent ต้องเห็นข้อมูลชุดเดียวกัน ตั้งแต่ประวัติการคุย ไปจนถึงสถานะของระบบ
2. **Alignment-First**: เน้นการตกลงกันว่า "จะสร้างอะไร" (Should we build) ก่อนจะเริ่ม "ลงมือสร้าง" (Implementation)
3. **Proactive Summarization**: การใช้ Agent ช่วยดึงประเด็นสำคัญจากการทำงานของคนอื่นมาสรุปให้ฟัง ([[team-pulse]]) เพื่อรักษาจังหวะการทำงานของทีม

## เครื่องมือและเทคโนโลยีที่เกี่ยวข้อง

- **[[zed]]**: Editor ที่ออกแบบมาเพื่อการทำงานร่วมกันระหว่าง "คน + AI Agent" โดยเฉพาะ
- **[[deltadb]]**: ระบบ Sync ที่ใช้ [[crdts]] เพื่อให้คนและ Agent เห็นสถานะโค้ดเดียวกันในระดับตัวอักษร
- **[[ace]]**: ระบบที่เน้นการประสานงานระหว่างมนุษย์และ Agent

## DeltaDB: ร่วมมือระหว่างที่ code ยังเปลี่ยน

[[software-is-made-between-commits|Software Is Made Between Commits]] เพิ่มกลไกที่ชัดขึ้นให้แนวคิดนี้ [[deltadb|DeltaDB]] เก็บทุก operation พร้อมบทสนทนาที่ทำให้เกิด edit และให้คนกับ agent หลายตัวแก้ shared worktree ข้ามเครื่องได้ การอ้างอิงเกาะ delta ไม่ใช่ line number จึงตาม code ได้แม้ย้ายตำแหน่ง

นี่ทำให้ shared context ไม่ได้หมายถึงแค่ทุกคนอ่านเอกสารชุดเดียวกัน แต่หมายถึงทุกคนย้อนจาก code ไปหาเหตุผล และจากเหตุผลไปหา code ณ เวลานั้นได้ผ่าน [[conversation-code-provenance|conversation-code provenance]]

อย่างไรก็ดี source เป็น product vision จาก Zed ยังไม่มีหลักฐานเปรียบเทียบว่ารูปแบบนี้ลด duplicate work, semantic conflict หรือ review burden ได้จริงแค่ไหน CRDT รวม operation ได้ แต่ไม่ได้ทำให้ decision ของหลาย agent ตรงกันเอง

**ได้อะไร:** DeltaDB เสนอ infrastructure สำหรับ shared context แบบต่อเนื่อง ส่วนโจทย์ alignment, validation และ governance ยังต้องแก้ในชั้น workflow

## ดูเพิ่ม

- [[ace]] — เครื่องมือที่สร้างตามแนวคิดนี้
- [[alignment-bottleneck]] — เหตุผลที่ต้องเน้นการร่วมมือกัน
- [[vibecoded-slop]] — ผลลัพธ์ของการทำลายความร่วมมือเพื่อเน้นความเร็ว
- [[conversation-code-provenance]] — ที่มาสองทางระหว่างบทสนทนากับ code
- [[software-is-made-between-commits]] — product thesis ของ Zed เรื่อง collaboration ก่อน commit
