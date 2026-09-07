---
title: The New Software Lifecycle
type: source
tags: [ai, software-engineering, sdlc, vibe-coding, agentic-engineering, harness, evals]
created: 2026-08-16
updated: 2026-08-16
url: https://addyosmani.com/blog/new-sdlc-vibe-coding/
author: Addy Osmani
date_published: 2026-06-16
date_ingested: 2026-08-16
sources: ["https://addyosmani.com/blog/new-sdlc-vibe-coding/"]
---

# The New Software Lifecycle / วงจรพัฒนาซอฟต์แวร์แบบใหม่

บทความของ [[addy-osmani|Addy Osmani]] (ผู้เขียนด้าน software engineering และ agent architecture) เผยแพร่เมื่อ 16 มิถุนายน 2026 และเลือกประเด็นสำคัญจาก whitepaper ของ [[google|Google]] เรื่อง *The New SDLC With Vibe Coding* มาอธิบายใหม่ แก่นไม่ได้บอกว่า AI ลบวงจรพัฒนาซอฟต์แวร์เดิมทิ้ง แต่บอกว่า **แต่ละช่วงเร็วขึ้นไม่เท่ากัน** พอ implementation ยุบจากหลายสัปดาห์เหลือไม่กี่ชั่วโมง งานที่ใช้ judgement อย่าง requirement, architecture และ verification เลยกลายเป็นคอขวดตัวใหม่ วงจรที่ว่านี้คือ software development lifecycle (SDLC) ตั้งแต่เก็บ requirement ไปจนถึงดูแลระบบหลัง deploy

บทความนี้เป็นมุมของผู้ร่วมเขียน whitepaper และยกตัวเลขหลายชุดมาแบบสรุป จึงใช้ได้ดีสำหรับเข้าใจกรอบคิด แต่ตัวเลข benchmark, productivity และ adoption ควรอ่านเป็น claim ตามแหล่ง ไม่ใช่ค่าคงที่ที่ใช้ได้กับทุกทีม

## Agent คือ model บวก harness

Addy ย้ำสมการจาก [[agent-harness-engineering|งานก่อนหน้า]] ว่า **Agent = Model + Harness**. Model เป็นเพียง engine ส่วน instruction, rule file, tool, MCP server, sandbox, orchestration, hook, memory, eval, tracing และ infrastructure คือ [[coding-harness|harness]] ที่ทำให้ engine นั้นทำงานจริง

บทความใช้สัดส่วนคร่าว ๆ ว่า model 10% และ harness 90% พร้อมยกสองกรณี: ทีมหนึ่งขยับ coding agent จากนอก top 30 ขึ้น top 5 บน Terminal-Bench 2.0 โดยเปลี่ยน harness อย่างเดียว อีกงานของ [[langchain|LangChain]] เพิ่มคะแนน 13.7 จุดด้วย system prompt, tool และ middleware รอบ model เดิม ตัวเลขเหล่านี้แสดงว่าชั้นรอบ model มี leverage สูง แต่ไม่ได้พิสูจน์ว่าสัดส่วน 10/90 เป็นกฎสากล

ข้อเสนอเชิงปฏิบัติคือ ถ้า agent ทำเรื่องแปลก ให้เช็ก harness ก่อน: tool ขาดไหม กฎหลวมไหม guardrail หายหรือ context เต็มไปด้วย noise. คำว่า “configuration failure” ตรงนี้ควรอ่านเป็น heuristic สำหรับ debug ไม่ใช่ข้อสรุปว่า model limitation ไม่มีผล

**ได้อะไร:** ทีมแก้ failure บางส่วนได้ทันทีผ่าน context, tool และ verifier โดยไม่ต้องรอ model รุ่นใหม่

## Context แบบไหนต้องอยู่ตลอด แบบไหนค่อยโหลด

บทความแบ่ง context ของ agent เป็นหกชนิด: instructions, knowledge, memory, examples, tools และ guardrails แล้วแยกวิธีส่งเป็นสองแบบ

| แบบ | ตัวอย่าง | สิ่งที่แลก |
| --- | --- | --- |
| Static context | system instruction, `AGENTS.md`, global memory, core guardrail | โหลดทุก interaction จึงเชื่อถือได้กว่า แต่จ่าย token ซ้ำและเสี่ยงกลบ signal |
| Dynamic context | skill ที่ตรงกับ task, tool result, เอกสารจาก RAG | โหลดเมื่อจำเป็นจึงประหยัดกว่า แต่ต้องมี trigger และ retrieval ที่ไว้ใจได้ |

[[progressive-disclosure|Progressive disclosure]] ทำให้ dynamic context ใช้กับ skill จำนวนมากได้ ตัว agent เห็น metadata สั้น ๆ ก่อน แล้วค่อยอ่าน instruction หรือ reference เต็มเมื่อ task ตรงกัน Addy เสนอให้ทีม review และ version เส้นแบ่ง static/dynamic เหมือน code เพราะมันกระทบทั้งคุณภาพ ความปลอดภัย และค่าใช้จ่าย

**ผลคือ:** context engineering ไม่ใช่การยัดข้อมูลให้มากที่สุด แต่คือการเลือกว่าข้อมูลไหนต้องอยู่เสมอ และข้อมูลไหนค่อยเรียกตอนต้องใช้

## Verification คือเส้นแบ่งระหว่าง vibe coding กับ engineering

เครื่องมือชุดเดียวกันใช้ทำ [[vibe-coding|vibe coding]] หรือ [[agentic-engineering|Agentic Engineering]] ก็ได้ สิ่งที่แยกสองฝั่งคือวิธีตรวจ output งานชั่วคราวที่ stake ต่ำอาจใช้การลองแล้วดู แต่ production system ต้องมี spec, test, eval และ CI/CD gate ตามความเสียหายที่อาจเกิด

บทความแยกการตรวจเป็นสองชั้น:

- **Output evaluation** — ผลสุดท้ายถูกไหม
- **Trajectory evaluation** — เส้นทางที่ agent ใช้สมเหตุผลไหม เรียก tool และทำ check ที่ควรทำครบหรือเปล่า

คำตอบที่หน้าตาถูกแต่ข้าม check สำคัญอันตรายกว่างานที่พังให้เห็นชัด Addy เลยสรุปว่า **ตั้ง quality bar ที่ eval ไม่ใช่ demo**. Demo พิสูจน์เพียงว่าครั้งหนึ่งเคยทำได้ ส่วน eval suite พร้อม rubric ใช้ดูความสม่ำเสมอและ regression ได้

**ได้อะไร:** คำว่า “เสร็จ” ต้องมีหลักฐานทั้งจากผลลัพธ์และวิธีที่ได้ผลลัพธ์มา ไม่ใช่ความมั่นใจของ agent

## แต่ละช่วงของ SDLC เปลี่ยนไม่เท่ากัน

[[ai-driven-sdlc|AI-driven SDLC]] ยังมี requirement, architecture, implementation, testing, review, deploy และ maintenance เหมือนเดิม แต่สัดส่วนเวลาและคอขวดเปลี่ยนไป

| ช่วง | สิ่งที่เปลี่ยน | สิ่งที่ยังไม่หาย |
| --- | --- | --- |
| Requirements | brief กลายเป็นบทสนทนาที่ออกทั้ง spec, user story, edge case และ prototype แรก | ต้องตัดสินว่าปัญหาไหนควรแก้และอะไรคือ success |
| Architecture | agent ช่วยสำรวจทางเลือกและลงมือหลังตัดสินใจ | tradeoff ยังพึ่ง business context ที่ model มองไม่ครบ |
| Implementation | งานเขียนย้ายไปเป็นงาน review มากขึ้น | ผลไม่สม่ำเสมอและ rework อาจกินกำไรด้านความเร็ว |
| Testing and QA | test/eval เข้าไปอยู่กลางวงรอบและป้อน failure กลับไปแก้ prompt หรือ tool | rubric, regression suite และ production monitoring ต้องมีเจ้าของ |
| Maintenance | agent ช่วยอ่าน code เก่า ทำ migration และ cleanup ที่เคยเสี่ยงหรือเสียเวลา | codebase context และ edge case ตามรอยต่อระบบยังเป็นเพดาน |

Addy วางตัวเลขที่ดูขัดกันไว้ด้วยกัน: survey บางชุดรายงาน productivity เพิ่ม 25–39% แต่การศึกษาของ METR พบว่า experienced developer ช้าลง 19% ในงานบางแบบเมื่อรวมเวลาตรวจและแก้ ทั้งคู่เกิดได้ เพราะผลขึ้นกับงาน คน harness และต้นทุน review

เพดานที่บทความเรียก **80% problem** ยังอยู่ Agent ทำ 80% แรกเร็ว แต่ 20% ท้ายมี edge case และรอยต่อที่ต้องใช้ context เฉพาะระบบ พอ implementation เร็วขึ้น specification quality กับ verification จึงไม่ได้หายไป กลับสำคัญกว่าเดิม

**ผลคือ:** AI ไม่ได้เร่งทุก phase เท่ากัน มันย้ายเวลาจากการพิมพ์ code ไปไว้ที่การกำหนดโจทย์ ตัดสิน tradeoff และพิสูจน์ว่างานถูก

## Context และ routing คือคันโยกทางการเงิน

บทความเปรียบเทียบต้นทุนรวมของสองแนวทาง Vibe coding เริ่มถูก แต่สะสม prompting tax, token burn, maintenance และ security cleanup ส่วน Agentic Engineering ลงทุนก่อนกับ schema, test และ structured context แล้วลด rework ต่อ feature ในระยะยาว

ตัวเลข “vibe coding แพงกว่า 3–10 เท่าต่อ feature หลังจุดตัด” เป็นภาพประกอบ ไม่ใช่ค่าที่วัดได้ตายตัว ประเด็นที่ใช้ต่อได้คือ **อายุของ code และ total cost of ownership สำคัญกว่าความเร็ว demo**. งาน routine ควร route ไป model เล็ก งาน reasoning ยากค่อยใช้ model ใหญ่ และไม่ควรส่ง repo 100,000 token เข้าไปทุก prompt

ตรงนี้ต่อกับ [[orchestration-tax|orchestration tax]]: ค่า model ไม่ใช่ต้นทุนทั้งหมด ยังมีเวลาของคนที่ต้องตรวจ รวมงาน และแก้ความเข้าใจที่หลุดไปด้วย

**ได้อะไร:** context policy กับ model routing เป็นทั้ง architecture decision และ cost policy

## จาก prototype ไป production agent ใน workflow เดียว

ส่วนท้ายมองว่า terminal workflow เดิมเริ่มครอบตั้งแต่ scaffold, eval ไปจน deploy agent ที่มี memory, permission และ observability. บทความใช้ Google Agents CLI (เครื่องมือ command line ของ [[google-cloud|Google Cloud]] สำหรับวงจรสร้างและ deploy agent) เป็นตัวอย่าง: coding agent รับคำสั่งสร้าง support agent, สร้าง eval set, รัน และ deploy ไป Agent Engine ผ่าน workflow เดียว โดยใช้ MCP เป็นมาตรฐานต่อ tool และ A2A เป็นมาตรฐานส่งงานระหว่าง agent

ผู้ใช้สลับสองบทบาท:

- **Conductor** — คุมแบบ real-time ใน IDE เหมาะกับ exploration และ code ที่ยังไม่เข้าใจ
- **Orchestrator** — ส่ง goal แบบ async แล้วค่อย review เหมาะกับ migration, test generation หรืองานที่ spec ชัด

นี่เป็นภาพทิศทางของ product ecosystem มากกว่าหลักฐานว่า prototype ทุกตัวพร้อมขึ้น production โดยไม่ rewrite. แม้คำสั่งเดียวจะซ่อนขั้นตอน deploy ได้ แต่ permission, eval coverage, observability และ ownership ยังต้องออกแบบอยู่

## ตัวเลขและคำกล่าวที่ควรอ่านอย่างระวัง

- สัดส่วน model 10% / harness 90% เป็น rough split ของ paper ไม่ใช่ measurement สากล
- productivity +25–39% และ METR -19% พูดถึงคน งาน และวิธีวัดต่างกัน จึงไม่ควรเฉลี่ยรวมเป็นคำตอบเดียว
- ต้นทุน vibe coding 3–10 เท่าต่อ feature ถูกระบุเองว่าเป็นภาพประกอบ
- ตัวเลขต้นปี 2026 ว่า developer มืออาชีพ 85% ใช้ coding agent เป็นประจำ, 51% ใช้ทุกวัน และ code ใหม่ราว 41% มาจาก AI ไม่มี methodology อยู่ในบทความย่อนี้
- ประโยค “generation is mostly solved” เป็น thesis ของผู้เขียน แต่ยังตึงกับ 80% problem, ผล METR และข้อยอมรับว่า architecture/verification ยังช้า

## See also

- [[ai-driven-sdlc]]
- [[addy-osmani]]
- [[google]]
- [[google-cloud]]
- [[coding-harness]]
- [[context-engineering]]
- [[progressive-disclosure]]
- [[evals-and-error-analysis]]
- [[vibe-coding]]
- [[agentic-engineering]]
- [[spec-driven-development]]
- [[orchestration-tax]]
- [[agentic-code-review]]
