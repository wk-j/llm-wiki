---
title: DeltaDB
type: entity
tags: [database, crdt, synchronization, collaboration, zed]
created: 2026-04-29
updated: 2026-08-15
sources: [zed-is-1-0.md, software-is-made-between-commits.md]
---

# DeltaDB / เดลตาดีบี

**DeltaDB** คือระบบที่ [[zed-industries|Zed Industries]] สร้างเพื่อ version worktree กับบทสนทนาที่ทำให้ code เปลี่ยนไปพร้อมกัน Source เดิม [[zed-is-1-0|Zed is 1.0]] เรียกมันว่า synchronization engine ส่วน [[software-is-made-between-commits|Software Is Made Between Commits]] เรียกกว้างขึ้นว่า version control ชนิดใหม่

สองคำนี้อาจพูดถึงคนละชั้น: CRDT เป็น engine สำหรับ sync ส่วน product ด้านบนใช้ engine นั้นสร้าง version control แต่ source ยังไม่ได้ให้ architecture ที่ยืนยันความสัมพันธ์นี้ จึงควรเก็บเป็นคำอธิบายที่น่าจะเป็น ไม่ใช่ข้อสรุป

## เทคโนโลยีเบื้องหลัง (Underlying Technology)

- **[[crdts|CRDTs (Conflict-free Replicated Data Types)]]**: ฝัง replicated worktree เพื่อให้หลายคนและหลาย agent แก้ไฟล์พร้อมกันข้ามเครื่อง แล้วรวม operation โดยไม่ทำ state สูญหาย
- **Fine-grained deltas**: แบ่งการเปลี่ยนแปลงเป็น stream ของ operation ย่อย แต่ละ delta มี identity คงที่ จึงอ้างถึง code ระหว่าง commit ได้
- **Conversation + edit**: เก็บข้อความกับ edit ที่ตามมาเคียงกัน เป็นฐานของ [[conversation-code-provenance|conversation-code provenance]]
- **Real files**: agent ใช้ไฟล์ผ่าน terminal ได้ และผู้ใช้ mount worktree ลง disk เพื่อใช้เครื่องมืออื่นได้

CRDT แก้ conflict ระดับ replica ไม่ได้รับประกันว่า edit สองชุดจะเข้ากันทางความหมาย ถ้า agent สองตัวเปลี่ยน contract เดียวกันคนละทิศ ระบบยังต้องใช้ test, review และการตัดสินใจของทีม

## ประโยชน์หลัก

1. **Shared evolving worktree**: คนและ agent เห็นและแก้ code ระหว่างที่งานยังเดิน ไม่ต้องรอ commit
2. **Stable references**: ลิงก์เกาะ delta แทน line number จึงตาม code ที่ย้ายตำแหน่งได้
3. **Bidirectional provenance**: จากบทสนทนาไปหา code ตอนนั้น/ตอนนี้ และจาก code ไปหาบทสนทนาที่สร้างหรือแตะมัน
4. **Agent continuity**: agent รุ่นหลังใช้ context เดิมและตามหาเหตุผลของผู้ทำงานก่อนหน้าได้ ตาม vision ที่ source อธิบาย

## สถานะและคำถามเปิด

[[zed-is-1-0|Zed is 1.0]] วาง DeltaDB เป็นรากฐานของ collaborative coding แล้วเมื่อ 29 เมษายน 2026 แต่บทความใหม่บอกว่า beta จะเปิดให้ early users ใน “อีกไม่กี่สัปดาห์” โดยข้อความที่ ingest ไม่มีวันเผยแพร่ชัดเจน ความต่างนี้อาจหมายถึง engine มีอยู่ภายในก่อน ส่วน product surface ยังไม่เปิด beta หรืออาจเป็นการเปลี่ยน framing; ยังสรุปไม่ได้

รายละเอียดเรื่อง access control, retention, offline recovery, performance, storage, semantic conflict, Git interoperability และวิธี “เรียก agent เก่ามาถาม” ยังไม่มีใน source นี้ Claim เรื่องความสามารถจึงเป็น first-party launch claim จนกว่าจะมีเอกสารเทคนิคหรือผลใช้จริงเพิ่ม

## ดูเพิ่ม
- [[zed]] — เครื่องมือหลักที่ใช้ DeltaDB
- [[collaborative-ai-engineering]] — แนวคิดการทำงานร่วมกันที่ DeltaDB มารองรับ
- [[conversation-code-provenance]] — การย้อนจากบทสนทนาไปหา code และย้อนกลับ
- [[software-is-made-between-commits]] — บทความเปิดตัว DeltaDB ในฐานะ version control
