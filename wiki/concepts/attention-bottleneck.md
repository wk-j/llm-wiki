---
title: Attention Bottleneck
type: concept
tags: [ai, agents, productivity, attention, bottleneck]
created: 2026-07-05
updated: 2026-07-05
sources: [piyalitt-codex-keynote-attention-not-token.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md, The Orchestration Tax.md]
---

# Attention Bottleneck / คอขวด attention

**Attention bottleneck** คือข้อสังเกตจาก [[peter-steinberger|Peter Steinberger]] บนเวที Codex keynote (สรุปใน [[piyalitt-codex-keynote-attention-not-token]]): พอข้อจำกัดเรื่อง **token** และ **compute** เริ่มแก้ได้ ข้อจำกัดจริงของงาน agent กลับกลายเป็น **attention** ของมนุษย์. จุดที่น่ากลัวคือ attention ไม่เหมือน token หรือ compute เพราะซื้อเพิ่มไม่ได้ง่าย ๆ

> "ตอนนี้สิ่งที่จำกัดผมมากที่สุดไม่ใช่ token หรือ compute อีกต่อไป แต่คือ attention และมันเพิ่มไม่ได้"
> — Peter Steinberger (อ้างในโพสต์ Piyalitt)

## Bottleneck ย้ายที่

Peter เล่าลำดับชัด:

| ช่วง | ข้อจำกัด | แก้ได้ไหม |
|---|---|---|
| ปีที่แล้ว | token | ซื้อ/เข้าถึงได้มากขึ้น (เขาแก้สุดขั้วด้วยการ join OpenAI) |
| ถัดมา | compute | เช่า/แยกเครื่องได้ (test box) |
| วันนี้ | attention | มีเท่าเดิมทุกวัน |

ทักษะที่คุ้มลงทุนที่สุดในยุคนี้จึงไม่ใช่แค่สั่งให้ model เก่งขึ้น แต่คือ **เลือกให้ได้ว่าจะใช้ attention ไปกับอะไร**

## อาการ: จ้อง agent ที่ไม่จำเป็นแล้ว

Peter ถามกลางเวทีว่า เรายังนั่งจ้อง agent ระหว่าง code ไหลผ่านหน้าจออยู่ไหม?

- **Model รุ่นก่อน:** การจ้องยังจำเป็น — พอเห็น agent เลี้ยวผิด ต้องกด escape ดึงกลับทันที
- **Model รุ่นล่าสุด:** เข้าใจเจตนาได้ดีขึ้นมาก จนการนั่งดู code ถูกเขียนเริ่มกลายเป็น **การเผา attention เปล่า ๆ**

ระบบที่ดีควรรบกวนเราเฉพาะจังหวะที่ **การตัดสินใจของมนุษย์สร้างความแตกต่างได้จริง** ไม่ใช่ทุก keystroke ของ agent

## ความสัมพันธ์กับ orchestration tax

[[orchestration-tax|Orchestration tax]] อธิบายภาพเดียวกันในมุม concurrency: เปิด agent ถูก แต่ปิดงาน (review/merge) แพง เพราะสุดท้ายมีมนุษย์คนเดิมเป็นคนตัดสิน. [[zack-proser|Zack Proser]] และ [[simon-willison|Simon Willison]] ให้หลักฐานหน้างานว่า agent ไม่ใช่คอขวดแล้ว — **คนต่างหาก**

Attention bottleneck ตั้งชื่อคอขวดนี้จากมุม **ทรัพยากรที่ซื้อเพิ่มไม่ได้** คือสมาธิและเวลาตัดสินใจ. ส่วน orchestration tax มองจากคิวงานที่รอ review. สองหน้าเสริมกัน:

- Orchestration tax → สถาปัตยกรรมรอบ review bandwidth
- Attention bottleneck → ออกแบบ loop ให้มนุษย์อยู่ [[inner-loop-outer-loop|outer loop]] ไม่ต้องนั่ง polling งานชั้นใน

## เชื่อมกับ unknowns

[[piyalitt-codex-keynote-attention-not-token]] เปิดโพสต์ด้วย [[thariq-shihipar|Thariq]]: ยิ่ง model เก่ง คอขวดยิ่งย้ายมาที่เราทำ unknowns ให้ชัดได้ดีแค่ไหน. Attention ที่หมดไปกับการจ้อง agent หรืออ่าน transcript ยาว ๆ คือ attention ที่ไม่ได้ใช้เคลียร์ unknowns ก่อนลงมือ และมักแพงกว่ามากเมื่อมาแก้ทีหลัง (ดู [[unknowns-matrix]])

## See also

- [[piyalitt-codex-keynote-attention-not-token]]
- [[peter-steinberger]]
- [[orchestration-tax]]
- [[inner-loop-outer-loop]]
- [[developer-balance]]
- [[unknowns-matrix]]
- [[how-to-keep-shipping-away-from-desk]]
