---
title: Cal Rueb
type: entity
tags: [people, anthropic, engineer]
created: 2026-05-04
updated: 2026-05-04
sources: [This Anthropic Engineer Uses Claude Code Differently Than Everyone Else.md]
---

# Cal Rueb / คาล รูบ

วิศวกรในทีม Applied AI ของ [[anthropic|Anthropic]] และหนึ่งในผู้ร่วมพัฒนาหลัก (core contributor) ของ [[claude-code|Claude Code]] 

Cal เริ่มต้นจากการทดลองใช้ Claude Code (ในช่วงต้นของการพัฒนา) เพื่อสร้างแอปพลิเคชันส่วนตัวในวันหยุด และพบว่ามันเปลี่ยนวิธีคิดเกี่ยวกับการเขียนโปรแกรมไปโดยสิ้นเชิง เขาใช้งานหนักจนขึ้นอันดับหนึ่งของ leaderboard ภายในบริษัท ทำให้เขาได้เข้ามาร่วมทีมพัฒนา Claude Code ในที่สุด 

หน้าที่หลักของเขาคือการดูแลเรื่องระบบ prompt (system prompts), การอธิบายเครื่องมือ (tool descriptions), และการประเมินผล (evaluation) เพื่อให้แน่ใจว่าการปรับปรุง prompt จะไม่ทำให้ประสิทธิภาพของ Claude Code ลดลง

ในฐานะวิศวกรที่ใช้งานและสร้าง Claude Code เขาเน้นย้ำเรื่องการใช้ [[agentic-search|Agentic Search]] แทนที่ RAG แบบเดิม และสนับสนุนให้ตั้งค่า `[[claude-md|CLAUDE.md]]` อย่างเหมาะสมเพื่อเป็น "หน่วยความจำ" ให้กับ agent
