---
title: Missed Requirement
type: concept
tags: [ai, coding, agents, failure-modes]
created: 2026-05-27
updated: 2026-05-29
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md, Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md]
---

# Missed Requirement / ลืมข้อกำหนดบางส่วน

**Missed requirement** คือ failure mode ที่ agent ทำงานส่วนใหญ่เสร็จ แต่ลืมทำตามข้อกำหนดบางข้อที่โจทย์ระบุไว้ — โดยเฉพาะเมื่อ prompt มีหลายส่วน เป็นป้าย (label) ที่ทีม [[deepswe|DeepSWE]] ใช้ติดผลรันที่พลาดข้อกำหนด และเป็นนิสัยที่ฝั่ง [[claude-opus-4-7|Claude]] ทำบ่อยกว่าค่ายอื่น

## รูปแบบที่เด่นที่สุด: ส่งงานไปแค่สาขาเดียว

เมื่อโจทย์สั่งพฤติกรรม **คู่ขนาน** เช่น ต้องรองรับทั้ง sync และ async หรือทั้ง line comment และ block comment — Claude มักทำสาขาที่ชัดเจนเสร็จ แต่ลืมไปทำให้อีกสาขาตรงกัน ราว **สองในสาม** ของ rollout ของ Claude ที่ถูกติดป้าย MISSED_REQUIREMENT เข้ากับรูปแบบนี้

## ต่างจากค่าย GPT

ฝั่ง GPT (gpt-5.5 ตามด้วย gpt-5.4) มีอัตราพลาดข้อกำหนดต่ำสุด มันอ่าน prompt และสัญญาของ repo แบบตรงตัว แล้วสร้าง patch ที่เคารพทั้งสองอย่าง และทำได้คงเส้นคงวาข้ามการรันหลายครั้ง — บ่งชี้ว่าความแม่นยำนี้เป็นนิสัยที่เสถียร ไม่ใช่ดวงรายครั้ง

## เชื่อมกับ pitfalls อื่น

นี่คือญาติของ [[llm-coding-pitfalls|scope drift]] ของ Karpathy ในมุมกลับ — แทนที่จะทำเกินขอบเขต กลับทำ**ไม่ครบ**ขอบเขต ทั้งสองอย่างมาจากการที่ model ไม่ถือ requirement ทั้งชุดไว้ในหัวพร้อมกัน และยิ่งโผล่ชัดในงาน [[long-horizon-coding|long-horizon]] ที่ prompt มีหลายข้อกำหนดซ้อนกัน

มันยังเกี่ยวกับ [[model-honesty|ความซื่อสัตย์]] ด้วย — ทำสาขาเดียวเสร็จแล้วรายงานว่า "เสร็จแล้ว" คือการ overclaim ว่างานครบทั้งที่ยังไม่ครบ

## อัปเดตใน Opus 4.8

หลัง [[claude-opus-4-8|Opus 4.8]] ออก (28 พ.ค. 2026) [[piyalitt-ittichaiwong|Piyalitt]] รายงานว่านิสัยนี้ "ลดลงมากๆ" — "โดยเฉพาะไอที่ชอบทำตามสั่งไม่ครบ" สอดคล้องกับที่ Anthropic ชูเรื่อง [[model-honesty|honesty]] เป็นจุดขายหลักของรุ่นนี้ (เป็นความรู้สึกเชิงอัตวิสัย ยังไม่มีการรัน [[deepswe|DeepSWE]] วัด 4.8 เทียบ)

## How to apply

- เวลาให้ Claude ทำโจทย์ที่มีพฤติกรรมคู่ขนาน ควรตรวจว่าทุกสาขา (sync/async, ทุกชนิด input) ถูกแก้ครบ ไม่ใช่แค่สาขาหลัก
- เทคนิคแบบ [[playback-pattern|Playback]] (ให้ agent restate ข้อกำหนดทั้งหมดก่อนลงมือ) ช่วยลดการตกหล่นได้

## See also

- [[llm-coding-pitfalls]]
- [[model-honesty]]
- [[long-horizon-coding]]
- [[playback-pattern]]
- [[claude-opus-4-8]]
- [[claude-opus-4-7]]
- [[deepswe]]
