---
title: AXI
type: entity
tags: [ai, agents, tools, agent-experience, ax]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# AXI

**AXI** คือชุด design standards และ catalog/tooling ของ [[kun-chen|Kun Chen]] สำหรับทำเครื่องมือให้เป็นมิตรกับ agent มากขึ้น. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|วิดีโอ workflow]] เขาใช้ AXI เป็นตัวอย่างของ [[agent-experience|Agent Experience]] ฝั่ง tool: output format, latency, และ token cost ของ tool มีผลต่อคุณภาพ agent โดยตรง.

Kun ยก benchmark ว่าการเข้าถึง GitHub ผ่าน MCP อาจกิน token และเวลาเยอะกว่า CLI มาก ส่วน AXI-style tool ที่ออกแบบเพื่อ agent ตั้งแต่แรกให้ cost ต่ำกว่าและ success rate ดีกว่า. ตัวอย่างหลักใน ecosystem ของเขาคือ GitHub AXI และ Chrome DevTools AXI.

**ได้อะไร:** AXI คือคำตอบฝั่ง tool design ต่อคำถามว่า "ถ้า agent เป็น user ตัวจริงของ tool เรา ควรออกแบบ I/O ยังไง".

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[agent-experience]]
- [[coding-harness]]
- [[model-context-protocol]]
- [[lavish]]
