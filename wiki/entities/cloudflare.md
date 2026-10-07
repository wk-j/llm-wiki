---
title: Cloudflare
type: entity
tags: [cloud, developer-tools, infrastructure, agents]
created: 2026-06-29
updated: 2026-10-07
sources: ["i don't want to use your agent — @RhysSullivan.md", dillon-mulroy-ships-production-code-he-didnt-write.md, what-is-codemode-armin-ronacher.md]
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

## Code Mode และ MCP server ของ Cloudflare

[[armin-ronacher|Armin Ronacher]] ให้เครดิต Cloudflare ว่าเป็นคนตั้งชื่อ [[codemode|Codemode]] (ใน [[what-is-codemode-armin-ronacher|What is Codemode]] ลิงก์ไปบล็อก "Code Mode" ของ Cloudflare) คือให้ LLM เขียน code เรียก tool แทนการยิง tool call ทีละครั้ง

MCP server ของ Cloudflare ทำ Codemode ไว้ใน server เอง: client ส่ง JavaScript เป็น string เข้า tool `execute` แล้ว code นั้นเรียก `cloudflare.request` ต่อ Armin มองว่าเป็นทางแก้ขัดที่เข้าใจได้ เพราะ harness ส่วนมากยังไม่มี Codemode แต่พอใช้ใน [[pi-agent|Pi]] ที่มี Codemode อยู่แล้ว ก็กลายเป็น Codemode ซ้อน Codemode: JSON escape สองชั้น model เล็กสับสน และ code ชั้นในเรียก tool ชั้นนอกไม่ได้

**ผลคือ:** แนวทางเดียวกันที่ช่วย harness ที่ไม่มี Codemode กลับเป็นภาระให้ harness ที่มี

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
- [[codemode]]
- [[what-is-codemode-armin-ronacher]]
