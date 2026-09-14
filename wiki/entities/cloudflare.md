---
title: Cloudflare
type: entity
tags: [cloud, developer-tools, infrastructure, agents]
created: 2026-06-29
updated: 2026-09-12
sources: ["i don't want to use your agent — @RhysSullivan.md", dillon-mulroy-ships-production-code-he-didnt-write.md]
---

# Cloudflare / Cloudflare

**Cloudflare** คือแพลตฟอร์ม cloud, edge network, security, CDN, DNS, Workers, และ developer infrastructure. ในโพสต์ [[i-dont-want-to-use-your-agent]] ของ [[rhys-sullivan|Rhys Sullivan]] Cloudflare เป็นตัวอย่าง product surface ที่กว้างมาก จน agent ที่ดีต้องมีทั้ง docs, CLI commands, และ API tools ไม่ใช่แค่ chat ใน dashboard.

## ในกรอบ BYO agent

สำหรับ [[bring-your-own-agent|BYO agent]], Cloudflare ควรทำให้ agent ภายนอกเข้าใจ product ได้ผ่าน:

- docs ที่ agent อ่านแบบเจาะ product surface ได้
- CLI commands ที่ runbook ชัด
- MCP/API tools สำหรับอ่าน config และทำ action ภายใต้ permission
- deeplink ไป dashboard เมื่อต้องตรวจของจริง

ตรงนี้ช่วย power user ใช้ agent ประจำวันของตัวเองจัดการ infra โดยไม่ต้องย้าย context เข้า dashboard chat.

## มุมจากพนักงานเรื่อง AI และการเปลี่ยนบทบาท

[[dillon-mulroy|Dillon Mulroy]] เล่าใน [[dillon-mulroy-ships-production-code-he-didnt-write|บทสัมภาษณ์กับ Jan-Niklas Wortmann]] ว่า Cloudflare ลดพนักงานราว 20% หรือประมาณ 1,100 คนใน May 2026 และสื่อสารว่า AI เป็นเหตุหลัก เขามองว่าคำอธิบายนี้จริงส่วนหนึ่ง เพราะบริษัทเปิดรับตำแหน่งชนิดอื่นจำนวนมากต่อทันที แต่ก็บอกว่า overhiring ก่อนหน้านั้นน่าจะมีส่วน

หน้านี้เก็บ claim ทั้งสองด้านไว้ ไม่สรุปว่า AI หรือ overhiring เป็นเหตุเดียว Transcript ไม่มีประกาศบริษัท รายละเอียด role ที่หายหรือเพิ่ม และ workforce data สำหรับแยกเหตุออกจากกัน

ในระดับวิธีทำงาน Dillon บอกว่า engineer ทำ QA, prototype และสำรวจ codebase ของทีมอื่นได้เร็วขึ้น ส่วน product manager สร้าง MVP เพื่อคุยกับ engineer ได้ตรงขึ้น เขาไม่ได้เสนอให้ยุบ specialization ทั้งหมด แต่เห็นว่าเส้นแบ่งระหว่าง role พร่าขึ้น

## See also

- [[bring-your-own-agent]]
- [[i-dont-want-to-use-your-agent]]
- [[model-context-protocol]]
- [[coding-harness]]
- [[dillon-mulroy-ships-production-code-he-didnt-write]]
- [[dillon-mulroy]]
- [[engineering-role-shift]]
