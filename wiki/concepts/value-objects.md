---
title: Value Objects
type: concept
tags: [ddd, domain-modeling, types, software-design]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md]
---

# Value Objects / อ็อบเจกต์ที่นิยามด้วยค่า

**Value Objects** คือ object ที่ความหมายอยู่ที่ค่าข้างใน ไม่ใช่ identity แยกของตัวเอง. `Money(100, THB)` เท่ากับ `Money(100, THB)` อีกตัวได้ ถ้าค่ากับ rule เหมือนกัน.

ในโพสต์ของ [[zoran-horvat|Zoran Horvat]] value objects คือทางออกจาก [[primitive-obsession|Primitive Obsession]]. แทนที่จะปล่อยให้ amount เป็น `decimal`, currency เป็น `string`, และ identifier เป็น raw GUID เราให้แต่ละ concept มี type ของตัวเอง.

## ทำไมต้องแยกเป็น type

Value object ทำให้ rule อยู่กับข้อมูล. `Currency` ตรวจ code ได้. `Amount` ตรวจ range ได้. `OrderId` กันการส่ง GUID คนละชนิดผิดช่องได้. `UtcTimestamp` กันเวลาที่ไม่ใช่ UTC ได้.

ถ้าใช้ primitive ทั้งหมด rule เหล่านี้ต้องไปอยู่ที่อื่น. แล้วคนเขียน code ต้องจำเองว่าค่าไหนห้ามใช้กับค่าไหน.

**ได้อะไร:** type system ช่วย guard domain rule แทนความจำคน.

## Persistence ไม่ควรทำให้ value object หาย

ข้อโต้แย้งปกติคือ value object เก็บ database ยาก. Horvat บอกว่า tooling สมัยใหม่ช่วยได้. Nested value objects อาจ map เป็น flat columns ด้วย complex properties. Wrapper type ที่ถือค่าเดียวอาจใช้ value converter เพื่อ unwrap/write และ rebuild/read.

ตรงนี้เชื่อมกับ [[domain-model-persistence-separation]]: ใน database อาจยังเป็น scalar ได้ แต่ใน domain ไม่จำเป็นต้องเป็น scalar.

**ผลคือ:** schema ยัง practical ส่วน model ยัง expressive.

## See also

- [[zoran-horvat-domain-model-persistence]]
- [[domain-modeling]]
- [[domain-model-persistence-separation]]
- [[primitive-obsession]]
- [[entity-framework-core]]
