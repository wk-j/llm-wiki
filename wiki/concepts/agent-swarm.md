---
title: Agent Swarm
type: concept
tags: [ai, agents, orchestration, architecture, scaling, kimi]
created: 2026-04-21
updated: 2026-04-23
sources: [kimi-k2-6-tech-blog]
---

# Agent Swarm / ฝูง agent ที่แตกงานออกขนาน

**Agent Swarm** คือสถาปัตยกรรมการทำงานของ AI ที่ไม่ได้มุ่งทำให้โมเดลเดียวฉลาดขึ้น (scaling up) แต่เน้น**แตกงานออกเป็นส่วนย่อยจำนวนมาก แล้วให้ sub-agent หลายร้อยตัวทำงานขนานกัน** (scaling out) คำที่ [[moonshot-ai|Moonshot AI]] ใช้ในบล็อกคือ "scaling out, not just up" — ขยายในแนวกว้าง ไม่ใช่แค่ในแนวสูง

โมเดลที่เป็นหัวหอกของแนวทางนี้คือ [[kimi-k2-6|Kimi K2.6]] ซึ่งใน launch post ระบุว่าสามารถรองรับ **sub-agent ได้ถึง 300 ตัวที่ทำงานประสานกันกว่า 4,000 ขั้นตอน** ภายใน run เดียว (เทียบกับรุ่นก่อนหน้า K2.5 ที่ 100 agent × 1,500 ขั้นตอน) ตัวเลขนี้ไม่ใช่ขนาดของ context window แต่เป็น **จำนวน agent และขั้นตอน** ที่ coordinator กลางสามารถจัดการได้พร้อมกัน

## ต่างจาก Subagent Pattern อย่างไร

หน้าที่ [[subagent-patterns]] ที่ [[alex-ker|Alex Ker]] อธิบายไว้สำหรับ engineer ทั่วไปมีสองแบบคือ **parallel fan-out** (แตก agent ไปสำรวจสมมติฐาน) และ **pipeline** (สายพาน agent สำหรับรีวิว) Agent Swarm คือการนำ fan-out pattern มา**ขยายขนาดขึ้นอีกสองระดับ**

| | Subagent Pattern ปกติ | Agent Swarm |
|---|---|---|
| **ขนาด** | 3–5 sub-agent ต่องาน | 100–300 sub-agent ต่อ run |
| **ผู้สั่งการ** | Engineer (มนุษย์) ตัดสินใจว่าจะแตกกี่ทาง | **Coordinator agent** ตัดสินใจแตกงานเองตามความเหมาะสม |
| **ประเภท Sub-agent** | Homogeneous (agent คล้ายกัน ทำงานต่างกัน) | **Heterogeneous** — agent ที่มีความเชี่ยวชาญเฉพาะทาง สร้างขึ้นตามต้องการ |
| **การรวบรวมผล** | Main agent สังเคราะห์ผลลัพธ์ | Coordinator agent จัดการ lifecycle ทั้งหมด รวมถึงการ re-assign งานหากมี agent ล้มเหลว |
| **ขอบเขตงาน** | Investigation / Research | ผลิตงาน end-to-end (เอกสาร, เว็บไซต์, สไลด์, spreadsheet) ภายใน run เดียว |

**ผลลัพธ์ที่ได้** คือ งานที่ปกติแล้วต้องทำทีละขั้นตอนตามลำดับ สามารถทำพร้อมกันได้ทั้งหมด ตัวอย่างเช่น หากต้องการวิเคราะห์หุ้นกลุ่มเซมิคอนดักเตอร์ 100 ตัว เพื่อสร้าง quant strategy 5 แบบ และสรุปผลเป็นสไลด์สไตล์ McKinsey — แทนที่ main agent จะต้องทำทีละอย่าง, coordinator agent สามารถแตก sub-agent หนึ่งตัวต่อหุ้นแต่ละตัว แล้วให้ agent layer อื่นๆ ทำการวิเคราะห์, เขียนสรุป, และสร้างภาพประกอบไปพร้อมๆ กัน

## ตัวอย่างที่ Moonshot AI นำเสนอใน K2.6 Launch

เคสที่ยกมาเพื่อแสดงศักยภาพ (ซึ่งเป็น marketing material) ได้แก่:
- **Quant Strategy:** ออกแบบ quant strategy 5 แบบสำหรับสินทรัพย์เซมิคอนดักเตอร์ 100 ตัว แล้วสร้างเป็น reusable skill พร้อมสไลด์ PPT และ spreadsheet
- **Paper Generation:** แปลงเปเปอร์ดาราศาสตร์ฟิสิกส์ 1 ฉบับให้เป็น academic skill เพื่อดูดซับวิธีคิดและสไตล์การทำ visualization แล้วนำไปสร้างเปเปอร์ใหม่ความยาว 40 หน้า (7,000 คำ) พร้อม dataset กว่า 20,000 entry และกราฟคุณภาพสูง 14 ชิ้น
- **Resume Tailoring:** รับ CV 1 ใบ แล้วแตก sub-agent 100 ตัวไปจับคู่กับตำแหน่งงาน 100 แห่งใน California พร้อมปรับแก้ resume ให้เข้ากับแต่ละ job description
- **Website Creation:** สแกน Google Maps เพื่อหาร้านค้า 30 แห่งใน LA ที่ยังไม่มีเว็บไซต์ แล้วสร้าง landing page ให้แต่ละร้าน

ธีมหลักที่เห็นซ้ำๆ คือ **การประยุกต์ใช้ scale-out กับ knowledge work** — งานที่ต้องสร้าง output จำนวนมาก ซึ่งมนุษย์ไม่สามารถทำขนานกันได้ในสเกลนี้

## Document-to-Skill

ฟีเจอร์ที่น่าสนใจของ K2.6 Swarm คือ **Document-to-Skill** ซึ่งคือการโยนเอกสารคุณภาพดี (PDF, สไลด์, spreadsheet, Word) เข้าไป แล้วให้ model สกัด "structural and stylistic DNA" (โครงสร้างและสไตล์) ออกมาเก็บเป็น Skill ที่สามารถใช้ซ้ำได้

ความเชื่อมโยงกับ Swarm คือ sub-agent 300 ตัว หากทำงานโดยไม่มีสไตล์กลาง ผลลัพธ์ที่ได้จะกระจัดกระจาย การสกัด DNA จาก template ทำให้ agent ทุกตัวสามารถอ้างอิงสไตล์เดียวกันได้ ผลลัพธ์ที่ได้จากหลายสิบชิ้นจึงมีความสอดคล้องกัน (consistency)

ซึ่งแตกต่างจาก [[skills|Claude Code Skills]] ที่เป็นไฟล์ markdown และ script ที่มนุษย์ต้องเขียนขึ้นเอง แต่ K2.6 เปลี่ยนเป็นการสกัดอัตโนมัติจาก artifact ที่มีอยู่

## Claw Groups — BYO-Agents

ส่วนต่อขยายของ Swarm คือ **Claw Groups** (research preview) ซึ่งมีหลักการดังนี้:
- **Human-Agent Collaboration:** multi-agent และมนุษย์ทำงานร่วมกันใน space เดียวกันแบบ peer-to-peer ไม่ใช่แบบ master-slave
- **Heterogeneous Agents:** agent แต่ละตัวสามารถมาจากคนละเครื่อง, คนละโมเดล, มี toolkit และ memory ที่แตกต่างกันได้
- **Adaptive Coordinator:** K2.6 ทำหน้าที่เป็น **adaptive coordinator** ที่คอยจับคู่ task กับ agent ที่เหมาะสม, ตรวจจับการหยุดชะงัก (stall), re-assign งาน, และควบคุม deliverable ทั้งหมด

**ความแตกต่างจาก Swarm ปกติ** คือ Swarm ทั่วไป coordinator จะสร้าง sub-agent ขึ้นมาเองและเป็นเจ้าของทั้งหมด แต่ Claw Groups เปิดรับ agent ภายนอกเข้ามาร่วมทีม ซึ่งคล้ายกับ marketplace มากกว่า owned fleet โดย Moonshot ใช้โมเดลนี้กับทีม marketing ภายใน (เช่น Demo Makers, Benchmark Makers, Social Media ทำงานร่วมกับ K2.6)

## ข้อควรระวัง

- **Marketing vs. Measurable:** ตัวเลข 300 × 4,000 เป็นตัวเลขที่ Moonshot AI กำหนดขึ้นเอง ยังไม่มี benchmark มาตรฐานอุตสาหกรรมสำหรับเปรียบเทียบกับโมเดลอื่น
- **Latency vs. Cost:** การเปิด sub-agent 300 ตัวพร้อมกันหมายถึงการใช้ token/compute ที่เพิ่มขึ้นมหาศาล "ความเร็ว" ที่ได้มาอาจแลกกับการจ่ายที่แพงขึ้นหลายเท่า ซึ่งต้องชั่งน้ำหนักกับแนวทางอื่น เช่น [[model-choice-by-expertise]] (ถ้ามีผู้เชี่ยวชาญรีวิว, โมเดลเล็กก็อาจเพียงพอ) หรือ [[advisor-strategy]] (ใช้โมเดลแพงเฉพาะจุดตัดสินใจที่สำคัญ)
- **Oversight:** agent 300 ตัวทำงานพร้อมกัน มนุษย์ไม่สามารถติดตามได้ทันแน่นอน ทำให้ต้องกลับไปพึ่ง [[harness-engineering]] (การออกแบบ agent สำหรับรีวิว) และ [[graduated-autonomy]] (การกำหนดระดับความเป็นอิสระ L1-L4)
- **Blast Radius:** ยิ่งมี sub-agent มากเท่าไหร่ โอกาสที่ตัวใดตัวหนึ่งจะทำงานนอกขอบเขตก็ยิ่งสูงขึ้น [[agent-runtime-untrusted]] ของ APTS จึงแนะนำว่าระบบต้องถูกออกแบบให้ล้มเหลวอย่างปลอดภัย (fail-by-construction) ผ่าน sandbox และ allowlist ไม่ใช่การเชื่อใจ prompt

## ตำแหน่งในภาพใหญ่

Scale-up (โมเดลใหญ่ขึ้น) และ scale-out (agent เยอะขึ้น) ได้กลายเป็นสองแกนการพัฒนาที่แยกจากกัน [[claude-opus-4-7|Claude Opus 4.7]] เน้นการ scale-up (reasoning ลึกขึ้น, effort `xhigh`/`max`) ในขณะที่ Kimi K2.6 เน้นการ scale-out (swarm และ long-horizon) ทั้งสองแนวทางไม่ได้มาแทนที่กัน แต่เหมาะกับ workload ที่แตกต่างกัน:

- **งานที่ต้องการการคิดวิเคราะห์ลึกซึ้ง** (architecture review, debugging) — **scale-up** จะเหมาะสมกว่า
- **งานที่ต้องสร้าง output จำนวนมาก** (100 resumes, 30 landing pages) — **scale-out** จะได้เปรียบ

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
