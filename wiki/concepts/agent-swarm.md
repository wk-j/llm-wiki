---
title: Agent Swarm
type: concept
tags: [ai, agents, orchestration, architecture, scaling, kimi]
created: 2026-04-21
updated: 2026-04-21
sources: [Kimi K2.6 Tech Blog Advancing Open-Source Coding.md]
---

# Agent Swarm / ฝูง agent ที่แตกงานออกขนาน

**Agent Swarm** คือ pattern การทำงานของ AI ที่ไม่ได้พยายามจะทำโมเดลตัวเดียวให้ฉลาดขึ้น แต่**แตกงานออกเป็นหลายชิ้นแล้วให้ subagent ที่ตัวใหญ่เท่าเดิมจำนวนมากทำขนานกัน** คำเรียกในบล็อกของ [[moonshot-ai|Moonshot AI]] คือ "scaling out, not just up" — ขยายในแนวกว้าง ไม่ใช่ในแนวสูง

โมเดลที่ดันเรื่องนี้เป็นหลักตอนนี้คือ [[kimi-k2-6|Kimi K2.6]] ของ Moonshot AI — launch post ตั้งตัวเลขไว้ที่ **300 sub-agents ทำงาน 4,000 ขั้นตอนประสานกัน** ภายใน run เดียว (รุ่นก่อน K2.5 อยู่ที่ 100 × 1,500) ตัวเลขนี้ไม่ใช่ context window แต่เป็น **จำนวน agent + ขั้นตอน** ที่ coordinator ตัวกลางจัดการพร้อมกันได้

## ต่างกับ subagent pattern อย่างไร

หน้า [[subagent-patterns]] พูดถึงสองแบบที่ engineer ใช้ทำงานรายวัน — **parallel fan-out** (แตกหลายตัวหาสมมติฐาน) กับ **pipeline** (สายพาน review ต่อกัน) ของ [[alex-ker|Alex Ker]] Agent Swarm เป็น fan-out ตัวเดียวกันนั่นแหละ แต่**ขยายขนาดขึ้นอีกสองขั้น**

| | subagent pattern ปกติ | Agent Swarm |
|---|---|---|
| ขนาด | 3–5 subagent ต่องาน | 100–300 subagent ต่อ run |
| ใครสั่งแตก | engineer (มนุษย์) เป็นคนตัดสินใจว่าจะแตกกี่ทาง | **coordinator agent** ตัดสินใจเองตามงาน |
| ประเภท subagent | homogeneous (ตัวคล้ายกัน ทำงานต่างกัน) | **heterogeneous** — domain-specialized ต่างบทบาท สร้างเองตามต้องการ |
| รวบผลยังไง | main agent สังเคราะห์ | coordinator จัดการ lifecycle + reassign ถ้าใครพัง |
| งานที่ทำได้ | investigation / research | ผลิตงาน end-to-end (เอกสาร + เว็บ + สไลด์ + spreadsheet) ใน run เดียว |

**ได้อะไร** — งานที่ปกติต้องทำทีละอย่างตามลำดับ ทำพร้อมกันได้ สมมติต้องวิเคราะห์หุ้นเซมิคอนดักเตอร์ 100 ตัว ทำ quant strategy 5 แบบ สรุปเป็น McKinsey-style PPT — แทนที่ main agent จะไล่ทำทีละอัน coordinator แตก sub-agent ตัวหนึ่งต่อหุ้นหนึ่งตัว แล้วทำ layer วิเคราะห์ + layer เขียน + layer ทำภาพต่อยอดพร้อมกัน

## ตัวอย่างที่ Moonshot โชว์ใน K2.6 launch

งานจริงที่ยกมาประกอบ claim (เชื่อหรือไม่เชื่อแล้วแต่ผู้อ่าน — นี่คือ marketing material):

- ออกแบบ quant strategy 5 แบบข้าม 100 สินทรัพย์เซมิคอนดักเตอร์ ทำ PPT สไตล์ McKinsey เป็น reusable skill ส่งมาพร้อม spreadsheet + executive presentation
- เปลี่ยนเปเปอร์ดาราฟิสิกส์ 1 ฉบับเป็น academic skill ดูดวิธีคิดและวิธีทำ visualization แล้วผลิต paper ใหม่ 40 หน้า 7,000 คำ + dataset 20,000+ entry + กราฟ astronomy-grade 14 ชิ้น
- รับ CV หนึ่งใบ แตก sub-agent 100 ตัว ไปจับคู่กับตำแหน่งใน California 100 ที่ คืนมาเป็น dataset + resume ปรับตาม job description 100 ฉบับ
- สแกน Google Maps หาร้านค้าปลีก LA 30 ร้านที่ไม่มีเว็บทางการ สร้าง landing page รายร้าน

ธีมที่ซ้ำกันคือ **scale-out applied to knowledge work** — งานที่ output เป็น doc/asset จำนวนมาก ที่มนุษย์ทำขนานไม่ไหว

## Document-to-Skill

ส่วนที่น่าสนใจของ K2.6 Swarm คือคำว่า **Skill** — เอา PDF / สไลด์ / spreadsheet / Word doc คุณภาพดีโยนเข้าไป โมเดลจะดูด "structural and stylistic DNA" (โครงสร้าง + สไตล์) ออกมาเก็บเป็น Skill ที่ใช้ซ้ำได้

ทำไมเชื่อมกับ Swarm — เพราะ sub-agent 300 ตัวถ้าสไตล์ไม่ตรงกัน output จะดูไม่เป็นชุดเดียวกัน การดึง DNA จาก template ให้ทุกตัว reference ทำให้ output หลายสิบชิ้นมี consistency

เทียบ [[skills|Claude Code Skills]] ซึ่งเป็น markdown + script ที่คนเขียนเอง — Moonshot ขยับเป็น auto-extract จาก artifact แทน

## Claw Groups — BYO-Agents

ส่วนต่อขยายของ Swarm คือ **Claw Groups** (research preview) หลักการ:

- multi-agent + มนุษย์ ทำงานในสเปซเดียวกันแบบ peer ไม่ใช่ master-slave
- agent แต่ละตัวมาจากคนละเครื่อง คนละโมเดล คนละ toolkit คนละ memory — ไม่ต้องเหมือนกัน
- K2.6 ทำหน้าที่ **adaptive coordinator** — จับคู่ task กับ agent ตาม skill/tool, ตรวจจับ stall, re-assign, คุม deliverable ตั้งแต่เริ่มจนจบ

**ต่างกับ Swarm ปกติยังไง** — Swarm ปกติ coordinator สร้าง sub-agent ขึ้นมาเอง ตัวเองเป็นเจ้าของทั้งหมด Claw Groups รับ agent จากภายนอกมาร่วม — คล้าย marketplace มากกว่า owned fleet Moonshot ใช้โมเดลนี้กับทีม marketing ภายใน (Demo Makers, Benchmark Makers, Social Media, Video Makers ทำงานร่วมกัน K2.6 ควบ)

## ข้อควรระวัง

- **Marketing vs measurable** — 300 × 4000 เป็นตัวเลขที่ Moonshot ตั้งเอง ไม่มี benchmark มาตรฐานของอุตสาหกรรมสำหรับเทียบกับโมเดลอื่น
- **Latency vs cost** — เปิด 300 sub-agent พร้อมกันแปลว่าใช้ token/compute แบบก้าวกระโดด "เร็ว" ได้ด้วยการยอมจ่ายแพงหลายเท่า ไม่ใช่ด้วยการคิดเร็วขึ้น ต้องชั่งกับ [[model-choice-by-expertise]] (ถ้า domain expert รีวิวได้ โมเดลเล็กก็พอ) และ [[advisor-strategy]] (ใช้โมเดลแพงเฉพาะจุดตัดสินใจ)
- **Oversight** — 300 ตัวทำพร้อมกัน มนุษย์ตามไม่ทันแน่ กลับไปเชื่อมกับ [[harness-engineering]] (Panutat) ว่าต้องออกแบบ review agent เป็น layer — และ [[graduated-autonomy]] ของ OWASP APTS ว่าต้องมี L1–L4 ชัด ไม่ใช่ปล่อย autonomous ทั้งหมด
- **การตั้ง blast radius** — จำนวน sub-agent ยิ่งเยอะ โอกาสที่ตัวใดตัวหนึ่งจะทำอะไรนอก scope ยิ่งสูง — [[agent-runtime-untrusted]] ของ APTS บอกว่าต้อง fail-by-construction (sandbox + allowlist นอกโมเดล) ไม่ใช่ trust-by-prompt

## ที่อยู่ในภาพใหญ่

Scale-up (โมเดลใหญ่ขึ้น) vs scale-out (agent เยอะขึ้น) กลายเป็นสองแกนแยกกัน — [[claude-opus-4-7|Claude Opus 4.7]] ดัน scale-up (reasoning ลึกกว่า, effort xhigh/max) ส่วน Kimi K2.6 ดัน scale-out (swarm + long-horizon) ไม่ใช่ว่าแบบไหนชนะแบบไหน — เป็นคนละ workload

- **งานที่ต้องคิดลึก ตัดสินใจยาก** (architecture review, debugging ที่รากซ่อน) — scale-up ชนะ
- **งานที่ output กระจายเป็นจำนวนมาก** (100 resume, 30 landing page, 14 chart) — scale-out ชนะ

## See also

- [[subagent-patterns]]
- [[kimi-k2-6]]
- [[moonshot-ai]]
- [[harness-engineering]]
- [[advisor-strategy]]
- [[graduated-autonomy]]
- [[agent-runtime-untrusted]]
- [[model-choice-by-expertise]]
- [[claude-opus-4-7]]
