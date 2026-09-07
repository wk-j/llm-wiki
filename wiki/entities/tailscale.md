---
title: Tailscale
type: entity
tags: [networking, developer-tools, remote-work, agents]
created: 2026-09-06
updated: 2026-09-06
sources: [dhh-ai-programming-setup-lex-clips.md, "https://tailscale.com/docs/concepts/tailnet"]
---

# Tailscale / เครือข่ายส่วนตัวสำหรับเชื่อมเครื่องต่างสถานที่

Tailscale เชื่อมอุปกรณ์และทรัพยากรเป็นเครือข่ายส่วนตัวที่เรียกว่า **tailnet** ตามคำอธิบายใน [Tailscale Docs](https://tailscale.com/docs/concepts/tailnet) คำนี้เป็นชื่อเครือข่าย ไม่ใช่ Telnet ตามที่ transcript ของคลิปถอดเสียงไว้

## บทบาทใน setup ของ DHH

[[dhh|DHH]] ผู้สร้าง Ruby on Rails เล่าใน [[dhh-ai-programming-setup-lex-clips|บทสัมภาษณ์เรื่องชุดเครื่องมือ AI]] ว่าใช้ Tailscale เพื่อเข้าถึงเครื่องใน Malibu และ Copenhagen จากโทรศัพท์ แล้วต่อ GL.iNet Comet ซึ่งเป็น KVM สำหรับควบคุมหน้าจอและอุปกรณ์รับข้อมูลของเครื่องจากระยะไกลให้กับ mini PC ที่มีอยู่

ใน setup นี้ Tailscale เชื่อมเครือข่าย Comet ช่วยควบคุมเครื่อง และ [[herdr|Herdr]] ช่วยตาม agent session เป็นคนละหน้าที่กัน ไม่ได้หมายความว่า Tailscale รัน model หรือจัดการรวม code จาก agent

ผลคือ DHH เพิ่มเครื่องมาทำงานได้สะดวกขึ้น ก่อนจะไปติดที่ [[attention-bottleneck|Attention Bottleneck]] หรือเวลาที่เขามีสำหรับตัดสินใจให้แต่ละงาน คลิปเป็นเรื่องเล่าการใช้งาน ไม่ได้ให้รายละเอียด network policy หรือผลทดสอบการเชื่อมต่อทุกสภาพแวดล้อม

## See also

- [[dhh-ai-programming-setup-lex-clips]]
- [[dhh]]
- [[herdr]]
- [[attention-bottleneck]]
