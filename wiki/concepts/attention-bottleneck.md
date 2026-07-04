---
title: Attention Bottleneck
type: concept
tags: [ai, agents, productivity, attention, bottleneck]
created: 2026-07-05
updated: 2026-07-05
sources: [piyalitt-codex-keynote-attention-not-token.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md, The Orchestration Tax.md]
---

# Attention Bottleneck / คอขวด attention

**Attention bottleneck** คือข้อสังเกตจาก [[peter-steinberger|Peter Steinberger]] บนเวที Codex keynote (สรุปใน [[piyalitt-codex-keynote-attention-not-token]]): พอแก้ข้อจำกัด **token** (ด้วยการเข้าไปทำงานที่ OpenAI) และ **compute** (ด้วย test box แยกเครื่อง) แล้ว ข้อจำกัดหลักของวันนี้กลายเป็น **attention** — และต่างจากสองอย่างแรกตรงที่ **เพิ่มไม่ได้**

> "ตอนนี้สิ่งที่จำกัดผมมากที่สุดไม่ใช่ token หรือ compute อีกต่อไป แต่คือ attention และมันเพิ่มไม่ได้"
> — Peter Steinberger (อ้างในโพสต์ Piyalitt)

## Bottleneck ย้ายที่

Peter เล่าลำดับชัด:

| ช่วง | ข้อจำกัด | แก้ได้ไหม |
|---|---|---|
| ปีที่แล้ว | token | ซื้อ/เข้าถึงได้มากขึ้น (เขาแก้สุดขั้วด้วยการ join OpenAI) |
| ถัดมา | compute | เช่า/แยกเครื่องได้ (test box) |
| วันนี้ | attention | มีเท่าเดิมทุกวัน |

ทักษะที่คุ้มลงทุนที่สุดในยุคนี้จึงกลายเป็น **การตัดสินใจว่าจะใช้ attention ไปกับอะไร** — ไม่ใช่การสั่งให้ model เก่งขึ้นอย่างเดียว

## อาการ: จ้อง agent ที่ไม่จำเป็นแล้ว

Peter ถามกลางเวที: เรายังนั่งจ้อง agent ระหว่าง code ไหลผ่านหน้าจออยู่ไหม?

- **Model รุ่นก่อน:** พฤติกรรมนี้จำเป็น — เห็น agent เลี้ยวผิดต้องกด escape ดึงกลับ
- **Model รุ่นล่าสุด:** เข้าใจเจตนาได้ดีขนาดที่การนั่งดู code ถูกเขียนกลายเป็น **การเผา attention เปล่า ๆ**

ระบบที่ดีต้องรบกวนเราเฉพาะจังหวะที่ **การตัดสินใจของมนุษย์สร้างความแตกต่างได้จริง** — ไม่ใช่ทุก keystroke ของ agent

## ความสัมพันธ์กับ orchestration tax

[[orchestration-tax|Orchestration tax]] อธิบายภาพเดียวกันในมุม concurrency: เปิด agent ถูก ปิดงาน (review/merge) แพง เพราะมีมนุษย์คนเดียว. [[zack-proser|Zack Proser]] และ [[simon-willison|Simon Willison]] ให้หลักฐานหน้างานว่า agent ไม่ใช่คอขวดแล้ว — **คนต่างหาก**

Attention bottleneck เป็นการตั้งชื่อใหม่จากมุม **ทรัพยากรที่ซื้อเพิ่มไม่ได้** (สมาธิ/เวลาตัดสินใจ) แทนมุม queue ก่อน review. สองหน้าเสริมกัน:

- Orchestration tax → สถาปัตยกรรมรอบ review bandwidth
- Attention bottleneck → ออกแบบ loop ให้มนุษย์อยู่ [[inner-loop-outer-loop|outer loop]] ไม่ polling inner loop

## เชื่อมกับ unknowns

[[piyalitt-codex-keynote-attention-not-token]] เปิดโพสต์ด้วย [[thariq-shihipar|Thariq]]: ยิ่ง model เก่ง คอขวดยิ่งย้ายมาที่เรา clarify unknowns ได้ดีแค่ไหน. Attention ที่เผาไปกับการจ้อง agent หรืออ่าน transcript ยาว ๆ คือ attention ที่ไม่ได้ใช้เคลียร์ unknowns ก่อนลงมือ — ซึ่งแพงกว่ามากตอนแก้ทีหลัง (ดู [[unknowns-matrix]])

## See also

- [[piyalitt-codex-keynote-attention-not-token]]
- [[peter-steinberger]]
- [[orchestration-tax]]
- [[inner-loop-outer-loop]]
- [[developer-balance]]
- [[unknowns-matrix]]
- [[how-to-keep-shipping-away-from-desk]]
