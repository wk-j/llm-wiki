---
title: Object-Relational Mapping
type: concept
tags: [database, orm, persistence, software-design]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md]
---

# Object-Relational Mapping / ORM

**Object-Relational Mapping (ORM)** คือชั้นที่ map object ใน application กับ table/row/column ใน relational database. ใน source นี้ [[zoran-horvat|Zoran Horvat]] พูดถึง ORM ในฐานะแรงต้านที่ทำให้ทีมยอม flatten [[domain-modeling|domain model]] เป็น primitive.

## แรงต้านของ ORM

ORM ต้องรู้ว่าจะสร้าง object อย่างไร, track change อย่างไร, map nested structure อย่างไร, และแปล query expression เป็น SQL ได้แค่ไหน. ถ้า tool ทำให้เรื่องพวกนี้ยาก ทีมมักเลือกทางง่าย: model กลายเป็น property primitive ที่เหมือน column.

ตรงนี้ practical แต่มีต้นทุน. พอ model แบนลง ความหมายของ domain ต้องย้ายไปอยู่ใน service, helper, validator, หรือ convention.

**ผลคือ:** persistence ง่ายขึ้น แต่ domain language ใน code อ่อนลง.

## มุมของ Horvat

Horvat ไม่ได้บอกว่า ORM ไม่มีข้อจำกัด. เขาบอกว่าอย่า assume เร็วเกินไปว่าข้อจำกัดนั้นบังคับให้ model ต้องแย่. [[entity-framework-core|EF Core]] ในตัวอย่างของเขารองรับ complex properties, value conversions, private constructor, และ query translation พอให้ [[value-objects|value objects]] อยู่ใน model ได้.

นี่คือมุม [[domain-model-persistence-separation]]: ORM ควรเป็น adapter ระหว่าง object กับ database ไม่ใช่เจ้าของรูปทรง domain.

**ได้อะไร:** ใช้ ORM เป็นเครื่องมือ ไม่ใช่ให้ ORM เขียนภาษาธุรกิจแทนเรา.

## See also

- [[entity-framework-core]]
- [[domain-model-persistence-separation]]
- [[primitive-obsession]]
- [[value-objects]]
