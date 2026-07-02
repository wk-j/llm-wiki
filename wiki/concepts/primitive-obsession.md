---
title: Primitive Obsession
type: concept
tags: [software-design, ddd, code-smell, domain-modeling]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md]
---

# Primitive Obsession / ติด primitive มากเกินไป

**Primitive Obsession** คือ code smell ที่ใช้ primitive เช่น `string`, `decimal`, `int`, หรือ raw GUID แทน concept ที่ควรมีชื่อและกฎของตัวเอง. โพสต์ของ [[zoran-horvat|Zoran Horvat]] ยกเรื่องนี้ในบริบท ORM: พอ persistence ทำยาก ทีมก็ flatten ทุกอย่างให้เป็น primitive.

## อาการ

ตัวอย่างง่าย ๆ คือระบบมีเงิน เวลา และ identifier แต่ code กระจายเป็น `decimal`, `string`, `DateTime`, `Guid` เต็มไปหมด. แต่ละจุดต้องจำเองว่า:

- amount ต้องห้ามติดลบไหม
- currency code valid หรือไม่
- timestamp ต้องเป็น UTC หรือ local
- GUID นี้เป็น `OrderId`, `CustomerId`, หรือ `InvoiceId`

ถ้าไม่มี type แยก compiler ช่วยกันการสลับผิดไม่ได้.

**ผลคือ:** bug หลายตัวไม่ใช่ algorithm ผิด แต่เป็นการส่งค่าถูกชนิดภาษาแต่ผิดชนิดธุรกิจ.

## วิธีแก้

ทางแก้ใน DDD คือสร้าง [[value-objects|value objects]] หรือ wrapper types สำหรับ concept ที่มีความหมาย. `Money`, `Currency`, `OrderId`, `UtcTimestamp` ทำให้ rule อยู่ใกล้ข้อมูล และชื่อ type บอก intent ทันที.

Horvat เชื่อมเรื่องนี้กับ [[entity-framework-core|EF Core]] ว่า persistence ไม่จำเป็นต้องบังคับให้กลับไปใช้ primitive ใน model. Mapping layer อาจ unwrap ตอน save และ rebuild ตอน read ได้.

**ได้อะไร:** code ยาวขึ้นเล็กน้อย แต่ domain safety และ readability ดีขึ้นมาก.

## See also

- [[value-objects]]
- [[domain-modeling]]
- [[domain-model-persistence-separation]]
- [[object-relational-mapping]]
