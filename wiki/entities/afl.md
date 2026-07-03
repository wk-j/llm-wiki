---
title: AFL
type: entity
tags: [testing, fuzzing, software-quality, security]
created: 2026-07-03
updated: 2026-07-03
sources: [eternal-sloptember.md]
---

# AFL / American Fuzzy Lop

AFL (American Fuzzy Lop) คือ fuzzing tool ที่ใช้หา bug โดย generate input จำนวนมากแล้วดูว่า program crash หรือมี behavior แปลกไหม. ใน [[eternal-sloptember|The Eternal Sloptember]] ผู้เขียนใช้ AFL เป็นตัวอย่างว่าเครื่องมืออัตโนมัติที่หา bug ได้เก่งกว่า LLMs ไม่ได้ทำให้ programmer รู้สึกเสีย status

## ทำไมถูกยกมา

ผู้เขียนใช้ AFL เพื่อโต้คำอธิบายว่า programmer ต้าน AI agents เพราะ status anxiety. ถ้าปัญหาเป็นแค่ “เครื่องมือเก่งกว่าเรา” คนควรกลัว AFL ด้วย. แต่คนไม่ได้กลัว เพราะ AFL เป็น tool ที่ชัดเจน: มันหา bug แล้วให้มนุษย์ใช้ judgement ต่อ

ผลคือ: ปัญหาของ coding agents ไม่ใช่แค่ความเก่ง แต่คือความไว้ใจใน process และ output

## See also

- [[property-based-testing]]
- [[behavioral-verifier]]
- [[quality-proxy-collapse]]
- [[eternal-sloptember]]
