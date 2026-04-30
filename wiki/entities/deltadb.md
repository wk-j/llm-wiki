---
title: DeltaDB
type: entity
tags: [database, crdt, synchronization, collaboration, zed]
created: 2026-04-29
updated: 2026-04-29
sources: [zed-is-1-0.md]
---

# DeltaDB

**DeltaDB** คือ synchronization engine ที่พัฒนาโดย [[zed-industries]] เพื่อรองรับการทำงานร่วมกันแบบ real-time ระหว่างมนุษย์และ AI Agent ภายใน [[zed]] editor

## เทคโนโลยีเบื้องหลัง (Underlying Technology)

- **[[crdts|CRDTs (Conflict-free Replicated Data Types)]]**: ใช้เพื่อให้มั่นใจว่าข้อมูลโค้ดที่ถูกแก้ไขจากหลายแหล่ง (คนละคน หรือ คนกับ Agent) จะสามารถรวมกันได้โดยไม่เกิดความขัดแย้ง (conflict)
- **Character-level Granularity**: ติดตามการเปลี่ยนแปลงในระดับตัวอักษร ทำให้สามารถเห็นการพิมพ์ของคนอื่นหรือ Agent ได้แบบ real-time อย่างแม่นยำ

## ประโยชน์หลัก

1. **Shared Single View**: ทั้งคนและ Agent เห็น code ในสถานะเดียวกันตลอดเวลา
2. **Seamless Agent Integration**: Agent สามารถ "เข้ามา" ในไฟล์และเริ่มแก้ไขโค้ดเคียงข้างมนุษย์ได้ทันที
3. **In-Context Review**: ทีมงานสามารถคุยกับ Agent หรือรีวิวงานของ Agent ได้ในจุดที่โค้ดนั้นถูกสร้างขึ้นมาจริงๆ (Directly in context)

## สถานะ
ถูกเปิดตัวและเน้นย้ำความสำคัญในการประกาศ [[zed]] 1.0 เพื่อเป็นรากฐานของ "Collaborative Coding Environment" แห่งอนาคต

## ดูเพิ่ม
- [[zed]] — เครื่องมือหลักที่ใช้ DeltaDB
- [[collaborative-ai-engineering]] — แนวคิดการทำงานร่วมกันที่ DeltaDB มารองรับ
