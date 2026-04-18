---
title: Subagent Patterns
type: concept
tags: [ai, agents, subagents, harness, orchestration, architecture]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md, Using Claude Code Session Management & 1M Context.md, Create custom subagents - Claude Code Docs.md]
---

# Subagent Patterns / รูปแบบการใช้ subagent

*Subagent* คือ LLM ลูกที่ main agent (LLM หลักที่คุยกับเราอยู่) แตกออกไปทำงานย่อย ๆ ในหน้าต่าง context ของตัวเอง แล้วส่งเฉพาะ "สรุป" กลับมา ไม่ได้ส่ง log ดิบทั้งหมด เป็นเครื่องมือหลักอันหนึ่งสำหรับจัดการขนาด context ของ main agent ไม่ให้ล้น

หน้านี้ว่าด้วย *รูปแบบการใช้* subagent ให้ได้ประโยชน์ ไม่ใช่ mechanics การเขียนไฟล์ — mechanics อยู่ใน [[claude-code-subagents-docs]] (เอกสารทางการของ Claude Code ว่าด้วยการเขียน subagent)

[[alex-ker|Alex Ker]] (engineer ที่เขียนบทความเรื่อง "Harnesses are everything" เมื่อปี 2026) สรุปว่ารูปแบบที่ใช้ได้ผลจริงมีสองแบบ — **parallel fan-out** (เปิดหลายตัวพร้อมกัน) กับ **pipeline** (ส่งงานไหลต่อเป็นสาย) แบบแรกเน้นความกว้าง แบบหลังเน้นความลึก

## เมื่อไหร่ถึงควร delegate

ก่อนเลือกรูปแบบ ต้องตัดสินใจก่อนว่างานนี้ *ควรส่งออกไปเลยไหม* ไม่ใช่ทุกงานจะเหมาะ

เกณฑ์เดียว

> **ใช้ subagent ก็ต่อเมื่อสรุปของงานพอให้ main agent ทำต่อได้**

ถ้ารู้ตัวว่าเดี๋ยวจะย้อนกลับมาถามว่า "อันที่อ่านเมื่อกี้เกี่ยวกับเรื่องนี้ยังไง" — อย่าส่งออกไป เก็บไว้ในหน้าต่างหลัก งานที่เหมาะส่งออกคืองานที่ขั้นตอนกลางไม่ต้องมายุ่งกับ reasoning (การให้เหตุผล) ของ main agent เช่นการค้นข้อมูลที่เอาแค่ผลลัพธ์สุดท้ายกลับมา

**ได้อะไร**
- main conversation สะอาด ไม่โดน log 500 บรรทัดมากวน
- subagent อยู่ใน "smart zone" (ช่วง context ที่โมเดลยังคิดได้ดี) ของมันเอง ไม่ต้องอ่าน message ก่อนหน้าที่ไม่เกี่ยวข้อง

ดู [[claude-code-session-management]] ประกอบ — หน้านั้นจัด subagent เป็นหนึ่งในห้าทางเลือกของการจัดการ context (อีกสี่คือ continue / rewind / clear / compact)

## แบบที่ 1: Parallel fan-out (กว้าง)

แปลตรงตัวว่า "กระจายออกแบบขนาน" — main agent แตก subagent หลายตัวพร้อมกัน ตัวละหนึ่งสมมติฐาน/หนึ่งมุม แล้วรอผลกลับมารวมเอง

**เหมาะกับงานประเภทไหน:** investigation (สืบสวน) และ research (ค้นคว้า) ที่มีหลายเส้นทางให้ลอง

**ตัวอย่างจริงจาก Alex Ker** — สถานการณ์ระบบเกิด alert (เตือนว่าอะไรบางอย่างพัง) main agent ทำ research เบื้องต้นก่อน แล้วคิดสมมติฐานของ root cause (สาเหตุรากเหง้า) ขึ้นมา 3 ข้อ จากนั้นเปิด subagent ข้อละตัวให้ทำงานขนานกัน

- แต่ละ subagent ไปลุย log / trace / metric (ข้อมูลรันไทม์สามแบบที่ engineer ใช้ดีบัก) ของสมมติฐานตัวเอง
- main agent รอ summary 3 ก้อนกลับมา แล้วค่อยสังเคราะห์เป็นข้อสรุป
- main agent ไม่เคยต้องแบก log ดิบหลายร้อยบรรทัดไว้ใน context ตัวเอง

**ได้อะไร**
- **เร็วขึ้น** — ค้นพร้อมกัน 3 ทาง เสร็จไวกว่าค้นทีละทาง
- **context ไม่ปนกัน** — noise (ข้อมูลขยะ) ของแต่ละทางแยกกันอยู่คนละหน้าต่าง

Alex Ker เล่าว่าเคยทำ prototype ทำนองนี้ตอนอยู่ [[baseten|Baseten]] (บริษัท AI infra ที่เขาเคยทำงาน) — ชื่อโครงการ `gpt-oss-swarm` ตอน OpenAI ปล่อย gpt-oss-120b

รูปแบบเดียวกันใช้ได้เวลาอยากเทียบ output ของโมเดลหลายตัว — เช่นเปิด thread คุยกับ MiniMax M2.5 คู่กับ GLM-5 ดูว่าใครตอบดีกว่า

## แบบที่ 2: Pipeline (ลึก)

แปลว่า "สายพาน" — งานชิ้นเดียวไหลผ่าน subagent หลายตัวเรียงเป็นลำดับ แต่ละตัวมองงานด้วย lens (เลนส์, มุมมอง) ที่ต่างกัน แล้วส่งต่อพร้อมความเห็นของตัวเอง

**เหมาะกับงานประเภทไหน:** review, evaluate, audit — งานที่อยากเอางานเดิมไปส่องในหลายมุม แทนที่จะลองหลายเส้นทาง

**ตัวอย่างจริงจาก Alex Ker** — feature หนึ่งที่ทีมกำลังจะสร้าง ให้ไหลผ่านคนสามบทบาทตามลำดับ

1. **UX designer** — มองเรื่อง user experience ว่าใช้งานจริงโอเคไหม
2. **Architect** — มองเรื่อง technical feasibility ว่าทำได้จริงไหมในระบบเดิม
3. **Devil's advocate** — บทบาทคนค้าน ลองท้าสมมติฐานของสองขั้นแรก

แต่ละขั้นรับ output ของขั้นก่อนหน้ามาเพิ่ม analysis ของตัวเอง main agent ได้ evaluation ที่มีหลายมุมซ้อนกัน **โดยไม่ต้องแบกทั้งสามมุมพร้อมกันในหัวตัวเอง**

**ได้อะไร** — เหมาะเป็นพิเศษกับระบบที่ output ไม่ deterministic (ไม่แน่นอน รันหลายครั้งคำตอบไม่ซ้ำ) อย่าง LLM เพราะเป็นการตรวจสลับมุมมอง ลดโอกาสหลุดจุดบอด

ต่อยอดได้ถ้าอยากมั่นใจขึ้น — เอา frontier model (โมเดลตัวท็อปของยุคนั้น เช่น Opus) มาเป็น judge รวบคำตอบของแต่ละขั้นให้ออกมาเป็น output สุดท้าย

### เทียบกับ Panutat

Pipeline ตรงนี้คือแบบเดียวกันกับ [[harness-engineering]] ของ [[panutat-tejasen|Panutat Tejasen]] (อาจารย์/practitioner ไทยที่เสนอแนวคิดเรื่อง curriculum สำหรับยุค AI) — เขาเรียง Code Review Agent → Test Generator → Security Audit → E2E ต่างกันแค่มุมที่มอง

- **Alex Ker** มองจาก productivity รายวัน — pipeline เป็น design pattern ของ subagent ที่ใช้ทำงาน
- **Panutat** มองจาก pedagogy (การสอน) — pipeline คือสิ่งที่หลักสูตรต้องสอน เพราะมนุษย์ตรวจ code ตามไม่ทัน agent แล้ว

เรื่องเดียวกัน มองจากคนละชั้น

## เทียบสองแบบ

| | Parallel fan-out | Pipeline |
|---|---|---|
| โครงสร้าง | หลายตัว ทำขนาน | ตัวเดียว ไหลต่อเป็นสาย |
| เน้นที่ | กว้าง — สำรวจหลายสมมติฐาน | ลึก — เพิ่มมุมมองต่องานเดิม |
| เหมาะกับ | Alert investigation, หา root cause หลายทาง, เทียบ output หลายโมเดล | Design review, ประเมิน proposal, audit feature |
| ข้อดีเรื่อง context | แยก noise ของแต่ละทางไม่ให้ปนกัน | แต่ละขั้นไม่ต้องรู้ว่าขั้นถัดไปจะมองยังไง |
| รวบผลยังไง | main agent ตั้งใจสังเคราะห์เอง | ขั้นสุดท้าย (หรือ judge) รวบให้ |

## จุดที่เชื่อมกับเรื่องอื่น

- **[[advisor-strategy]]** (pattern ที่จับคู่โมเดลเล็กถูกกับโมเดลใหญ่แพง) อยู่คนละระดับกับ subagent pattern ไม่ใช่ pipeline แต่เป็นคู่ executor ตัวเล็ก + advisor ตัวใหญ่ เรียก advisor เฉพาะตอนเจอจุดตัดสินใจยาก ใช้ร่วมกันได้ — main agent ใน fan-out อาจเป็น executor ที่เรียก advisor ตอนสังเคราะห์ข้อสรุป
- **[[ai-orchestrator]]** — เลือกรูปแบบไหนเมื่อไหร่ นั่นคืองานของ orchestrator (คนคุมวงทั้งระบบ) ตัวจริง
- **[[context-rot]]** (ปรากฏการณ์โมเดลโง่ลงเมื่อ context ยาวขึ้น) — subagent ไม่ได้มีไว้เท่ ๆ มันเกิดขึ้นมาเพราะหน้าต่างหลักต้องคุมไม่ให้โตเกินจุดที่โมเดลเริ่มเสียคุณภาพ

## ลงมือจริงใน Claude Code

สองแบบข้างบนเป็นเรื่องของ *ควรใช้เมื่อไหร่* — ส่วนวิธีเขียน subagent จริงอยู่ใน [[claude-code-subagents-docs]] (เอกสารทางการของ Claude Code) สรุปเฉพาะส่วนที่โยงกับ pattern

- **Fan-out** ตรงกับตัว `Explore` ที่ติดมากับ Claude Code อยู่แล้ว (ใช้ Haiku ซึ่งเป็นโมเดลเล็กเร็วราคาถูกของ Anthropic, อ่านอย่างเดียว) เปิดหลายตัวพร้อมกัน แต่ละตัวไปค้นของตัวเอง แล้วส่ง summary กลับ
- **Pipeline** ไม่มีตัวสำเร็จ ต้องเขียนเองเป็น markdown ไฟล์ใน `.claude/agents/` (ตัว reviewer / architect / devil's advocate) แล้ว commit เข้า git ให้ทั้งทีมใช้ได้
- ตั้ง `model: haiku` ต่อขั้นให้ถูก — ขั้นไหนสำคัญค่อยปล่อย `inherit` (ใช้โมเดลเดียวกับ main session) หรือ `opus` (ตัวท็อป) รูปแบบนี้คือ [[advisor-strategy]] ในอีกรูปหนึ่ง
- `memory: project` ช่วยให้ subagent แต่ละตัวสะสม pattern ของ repo (โค้ดเบส) ไว้ข้าม session ในไฟล์ `MEMORY.md` ของตัวเอง — ใช้ไปนาน ๆ ตัว reviewer จะเริ่มจำ convention ของโค้ดเบสได้เอง
- subagent ซ้อน subagent ไม่ได้ — ถ้าต้อง nested (ซ้อนหลายชั้น) จริง ให้ใช้ [[skills|Skills]] (แพ็กเกจ prompt/instruction ที่ reuse ได้) หรือ chain จาก main thread แทน

## See also

- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[claude-code-subagents-docs]]
- [[coding-harness]]
- [[harness-engineering]]
- [[claude-code-session-management]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
- [[context-rot]]
- [[compaction]]
- [[panutat-tejasen]]
