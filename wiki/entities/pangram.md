---
title: Pangram
type: entity
tags: [ai, ai-detection, company, academia]
created: 2026-08-16
updated: 2026-08-16
sources: [claude-text-watermarking-squintist.md]
---

# Pangram

บริษัททำ [[ai-text-detectors|AI text detector]] — เครื่องตรวจว่าข้อความเป็นงานเขียน AI หรือคน โดยตัดสินจากสไตล์ (neural classifier) ไม่ใช่ [[llm-text-watermarking|watermark]] ใน wiki นี้เข้ามาผ่าน [[claude-text-watermarking-squintist|วิดีโอของ Squintist]] ซึ่ง Pangram เป็นตัวละครหลักทั้งฝั่ง claim ความแม่นและฝั่งเคสพลาด

## ที่ปรากฏในแหล่ง

- **Claim ฝั่งดี:** Pangram รายงานว่าปัจจุบัน flag ชุด TOEFL essays ของ non-native writers (ชุดเดียวกับที่งาน Stanford 2023 พบ false positive เฉลี่ย 61% ใน detector 7 ตัว) เป็น**ศูนย์** — เป็นตัวเลขจาก vendor เอง
- **เคสอาจารย์:** อาจารย์สอนเขียน 25 ปี ขัดเรื่องสั้น comedy หกเดือน โดน Pangram ตัดสิน 100% AI — rule of three ของ comedy กลายเป็นสัญญาณ "เครื่องเขียน"
- **NeurIPS 2026:** Position Paper Track ใช้ Pangram scan submissions 969 ฉบับ desk-reject 178 ฉบับ (18%) โดยไม่มี appeal; ผู้ถูก reject เอา paper ของ track chair เข้า detector เดียวกัน ได้ 24–69%
- **ฝั่ง content:** Pangram เขียน blog อธิบาย humanizer (เครื่องมือล้างร่องรอย AI) และวิธีที่นักเรียนหลบ detection — อยู่ในตำแหน่งผู้เล่นใน arms race detector↔humanizer โดยตรง

## วิธีอ่าน

ความแม่นของ Pangram ทั้งขาขึ้น (zero false positives บนชุดเดิม) และขาลง (เคสอาจารย์, คะแนน paper ของ track chair) มาจากแหล่งคนละฝั่งที่ยังไม่มี audit อิสระ — เก็บทุกตัวเลขเป็น source-attributed และจำไว้ว่า failure mode เชิงโครงสร้าง (งานเขียนทางการของ non-native, งาน craft จัด) เป็นของ detector ทั้งประเภท ไม่ใช่ของ Pangram เจ้าเดียว

## See also

- [[ai-text-detectors]]
- [[claude-text-watermarking-squintist]]
- [[llm-text-watermarking]]
