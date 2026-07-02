---
title: Domain Modeling
type: concept
tags: [ddd, software-design, modeling, architecture]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md, matt-pocock-software-fundamentals.md]
---

# Domain Modeling / การออกแบบโมเดลโดเมน

**Domain Modeling** คือการทำให้ code มีรูปทรงใกล้กับปัญหาธุรกิจจริง. ไม่ใช่แค่ตั้ง class ตาม table แต่เป็นการหา concept, rule, invariant, และภาษาที่ทีมใช้คุยกัน.

ใน wiki เดิม เรื่องนี้โผล่ผ่าน [[ubiquitous-language|Ubiquitous Language]] จาก DDD. Source ของ [[zoran-horvat|Zoran Horvat]] เพิ่มมุม implementation: ถ้า concept มีความหมาย ก็ควรมี type ของตัวเอง ไม่ใช่ถูกบีบเป็น primitive เพราะ persistence.

## Model ที่ดีบอก intent

ถ้า function รับ `decimal amount, string currency` คนอ่านต้องเดาเองว่า rule อยู่ไหน. ถ้า function รับ `Money` intent ชัดกว่า และ type นั้นอาจบังคับได้ว่า amount ห้ามติดลบหรือ currency ต้องอยู่ในชุดที่รับได้.

นี่คือเหตุผลที่ [[value-objects|value objects]] สำคัญ. มันทำให้ domain rule อยู่ใกล้ข้อมูลที่ rule นั้นปกป้อง.

**ได้อะไร:** model กลายเป็น executable vocabulary ไม่ใช่แค่กล่องใส่ field.

## ความสัมพันธ์กับ database

Domain model ไม่ได้ลอยจากโลกจริง. สุดท้ายมันต้อง save/load ได้. แต่ [[domain-model-persistence-separation]] บอกว่าอย่าให้ database schema เป็นเจ้าของภาษาใน code ตั้งแต่แรก.

ถ้าใช้ [[object-relational-mapping|ORM]] อย่าง [[entity-framework-core|EF Core]] ทีมควรออกแบบ mapping ให้ serve model เท่าที่ทำได้. ถ้า tool ไม่รองรับจริง ค่อยจด trade-off ว่าต้อง compromise ตรงไหน.

**ผลคือ:** compromise กลายเป็น decision ที่รู้ตัว ไม่ใช่นิสัย flatten ทุกอย่างอัตโนมัติ.

## See also

- [[domain-model-persistence-separation]]
- [[value-objects]]
- [[primitive-obsession]]
- [[ubiquitous-language]]
- [[strategic-vs-tactical-programming]]
