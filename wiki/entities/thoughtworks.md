---
title: Thoughtworks
type: entity
tags: [organizations, consulting, software-engineering, ai]
created: 2026-06-08
updated: 2026-09-30
sources: [harness-engineering-bockeler.md, engineering-the-harness-thoughtworks.md]
---

# Thoughtworks

Thoughtworks เป็นบริษัทที่ปรึกษา/รับพัฒนาซอฟต์แวร์ระดับโลก ที่มีชื่อในวงการเรื่องการผลักดัน practice ทางวิศวกรรม เช่น continuous integration, continuous delivery, evolutionary architecture, และ Technology Radar (รายงานประเมินเทคโนโลยี/เทคนิคเป็นรอบ ๆ) คนของ Thoughtworks หลายคนเขียนงานบน martinfowler.com ซึ่งเป็นแหล่งอ้างอิงหลักของวงการ

ใน wiki นี้ Thoughtworks ปรากฏผ่านงานของ [[birgitta-bockeler|Birgitta Böckeler]] เรื่อง [[harness-engineering-bockeler|harness engineering สำหรับคนใช้ coding agent]] บทความเล่าถึง practice ในองค์กรเอง เช่น สู้ปัญหา architecture drift ด้วย "janitor army" (agent ที่คอยเก็บกวาด) ผสมกับ custom linter และเพิ่มคุณภาพ API ด้วย agent + linter ร่วมกัน

แนวคิดหลายอย่างในบทความก็มาจากคลังของ Thoughtworks เอง: **architectural fitness function** (ดู [[harness-guides-sensors]] หมวด architecture fitness harness) และวินัยสาย [[shift-left-testing|continuous integration / keep quality left]]

## Engineering the harness (บล็อก Thoughtworks, 2026-09-29)

บทความ [[engineering-the-harness-thoughtworks|Engineering the harness]] โดย Jaya Simha Reddy Nandyala กับ Prabina Pani ใช้คำ guides กับ sensors ชุดเดียวกับ Böckeler แล้วทำเป็น pattern ที่ใช้จริง: guides ก่อนลงมือ, sensors หลังลงมือ และ [[blast-radius-gates|ด่านให้คนตัดสินเฉพาะเรื่องที่ลามไกล]] คั่นกลาง ตัวอย่างหลักคือการ rename field ที่ microservice สามตัวใช้ร่วมกัน กับ pipeline หกช่วงที่มี RED/GREEN/REFACTOR แบบ TDD อยู่ตรงกลาง

บทความลิงก์ไปงานชุดเดียวกันของ Thoughtworks ที่ wiki ยังไม่ได้ ingest เช่นเรื่อง AI coding sensors, supervisory engineering / middle loop และ human on the loop

## See also

- [[birgitta-bockeler]]
- [[harness-engineering-bockeler]]
- [[harness-guides-sensors]]
- [[shift-left-testing]]
- [[engineering-the-harness-thoughtworks]]
- [[blast-radius-gates]]
