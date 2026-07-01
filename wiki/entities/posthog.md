---
title: PostHog
type: entity
tags: [analytics, product, developer-tools, agents]
created: 2026-06-29
updated: 2026-06-29
sources: ["i don't want to use your agent — @RhysSullivan.md"]
---

# PostHog / PostHog

**PostHog** คือ product analytics และ product OS สำหรับ event tracking, feature flags, experiments, session replay, และ growth analysis. ในโพสต์ [[i-dont-want-to-use-your-agent]] ของ [[rhys-sullivan|Rhys Sullivan]] PostHog เป็นตัวอย่าง product ที่ agent ภายนอกควร query data และพา user กลับไปดู UI ได้.

## ในกรอบ BYO agent

สำหรับ [[bring-your-own-agent|BYO agent]], PostHog ควรเปิด product expertise เป็น primitive เช่น:

- query tools สำหรับ event และ funnel data
- schema/resource ที่บอกว่าแต่ละ event แปลว่าอะไร
- deeplink ไป dashboard, chart, replay, หรือ cohort
- skills ที่ช่วยคิดเรื่อง activation, retention, experiment, และ growth

ผลคือ agent ของผู้ใช้ช่วยวิเคราะห์ product ใน context ของ repo, roadmap, และ notes ส่วนตัวได้ แล้วค่อยเปิด PostHog UI ตอนต้องดูภาพหรือยืนยันข้อมูล.

## See also

- [[bring-your-own-agent]]
- [[i-dont-want-to-use-your-agent]]
- [[model-context-protocol]]
- [[agent-experience]]
