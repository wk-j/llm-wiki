---
title: "Claude Codes New INTENT.MD, What is It?"
type: source
author: Rob Shocks
url: https://www.youtube.com/watch?v=LoMOPj-lO8U
date_ingested: 2026-09-09
tags: [ai, software-engineering, sdlc, intent, specs, agents, governance]
created: 2026-09-09
updated: 2026-09-09
sources: ["https://www.youtube.com/watch?v=LoMOPj-lO8U", "https://claude.com/blog/the-ai-native-sdlc-playbook"]
---

# Claude Codes New INTENT.MD, What is It? / intent.md ใน AI-Native SDLC คืออะไร

[[rob-shocks|Rob Shocks]] (ผู้ทำเนื้อหาและคอร์สเรื่อง AI-assisted product development) อธิบาย *The AI-Native SDLC Playbook* ของ [[anthropic|Anthropic]] ผ่านวงจร Plan, Design, Build, Test, Deploy และ Maintain แก่นของคลิปคือ agent ทำให้ช่วงเขียน code สั้นลงแล้ว แต่ขั้นที่อยู่รอบ code ยังเดินด้วยความเร็วของคน ถ้าทีมเปลี่ยนแค่เครื่องมือเขียน code คอขวดก็จะย้ายไปกองที่ requirement, review, test และ deployment gate

หน้านี้สรุป transcript ช่วง 0:00-16:02 ที่ผู้ใช้ส่งมา วันที่เผยแพร่คลิปยังตรวจไม่ได้ ส่วน playbook ต้นทางเผยแพร่เมื่อ 21 สิงหาคม 2026 และหน้าอย่างเป็นทางการระบุ Louis Claxton เป็นผู้เขียน Rob เปิดคลิปโดยโยง playbook เข้ากับ [[boris-cherny|Boris Cherny]] และทีม Claude Code แต่หน้าอย่างเป็นทางการไม่ได้ให้ Boris เป็นผู้เขียน จึงเก็บข้อความนั้นเป็น framing ของวิดีโอ ไม่ใช้แทนเครดิตต้นทาง

## Code เร็วขึ้น แต่ process ยังเท่าเดิม (0:00-1:23)

SDLC แบบเดิมมีหกช่วง: วางแผน ออกแบบ สร้าง ทดสอบ deploy และดูแลหลังขึ้น production เมื่อก่อนช่วง build มักกินทั้งเวลาและเงินมากที่สุด พอ coding agent ย่นช่วงนี้ลง ขั้นที่เหลือเลยกลายเป็นส่วนใหญ่ของเวลาทั้งหมด

> "code is no longer the bottleneck, it's your process"
>
> คอขวดไม่ใช่ code แล้ว แต่อยู่ที่วิธีส่งงานและตัดสินใจรอบ code

Rob จึงอ่าน playbook นี้ว่าเป็นการเอา agent เข้าไปช่วยทุกช่วง ไม่ใช่แค่สร้าง diff ให้เร็วขึ้น แต่การช่วยแต่ละช่วงต้องมี artifact และ gate ของตัวเอง ไม่ได้แปลว่าปล่อย agent วิ่งจากไอเดียถึง production โดยไม่มีคนดู

**ผลคือ:** ถ้าทีมเร่ง build อย่างเดียว งานจะไปค้างหน้า review และ deploy แทน

## intent.md เก็บคำของคนต้นเรื่องก่อนผ่าน handoff (1:24-4:36)

จุดเริ่มคือให้ agent สัมภาษณ์คนที่มีปัญหาหรือไอเดียซ้ำ ๆ จน scope, ผู้ใช้, constraint และภาพของความสำเร็จชัดขึ้น คนคนนี้เรียกว่า originator อาจเป็นลูกค้า product manager หรือ developer ก็ได้ ไม่จำเป็นต้องเป็น specialist

Agent สรุปบทสนทนาเป็น [[intent-md|`intent.md`]] ซึ่งเป็น proto-spec ที่คนกับเครื่องอ่านต่อได้ Rob ใช้คำจาก playbook ว่า "human-readable and machine-actionable" แล้วเน้นว่า originator ต้องกลับมาแก้สิ่งที่ agent เข้าใจผิดก่อนส่งให้ product owner จัดลำดับหรือรับเข้ากระบวนการ

Rob เสนอให้เก็บไฟล์ในโฟลเดอร์ `intent/` และใช้รูปแบบชื่อที่ทีมตกลงร่วมกัน เขาเองเรียกขั้นนี้ว่า discovery และมี skill ของตัวเอง แต่ย้ำว่าไม่ควรเปลี่ยน workflow ไปมาบ่อย เพราะคน agent และ skill ต้องรู้ว่าจะรับส่งงานกันตรงไหน

**ได้อะไร:** ความหมายจากคนต้นเรื่องมีที่อยู่แบบ versioned ก่อนจะผ่าน backlog, user story และการส่งต่อหลายมือ

## จาก intent ไป spec แล้วไป plan (4:38-8:22)

เมื่อ product owner รับ `intent.md` แล้ว ขั้น Design ใช้ agent สร้าง `spec.md` โดยโหลด policy ขององค์กร เช่น brand, security, compliance และ UX ผ่าน `AGENTS.md`, guideline หรือ skill Rob บอกตรง ๆ ว่าไม่มีวิธีเดียวที่เหมาะกับทุกทีม บางทีมใช้ plan mode ปกติ บางทีมสร้าง skill เฉพาะเพื่อให้ spec มีรูปแบบเดิมทุกครั้ง

ตอนเข้า Build วิศวกรส่ง `intent.md` กับ `spec.md` ให้ Claude Code, Cursor หรือ Codex แล้วให้สร้าง `plan.md` แผนควรบอกไฟล์ที่จะเปลี่ยน ลำดับงาน risk, constraint และหลักฐานที่จะใช้ตัดสินว่าสำเร็จ วิศวกรต้องซักแผนต่อ เช่นถามว่า change นี้ทำอะไรพังได้บ้าง จนคนที่ไม่เคยเห็นบทสนทนาเดิมอ่าน `plan.md` แล้วลงมือได้

เอกสารเหล่านี้รวมเป็น [[artifact-chain|artifact chain]] แต่ละ agent อาจเริ่มด้วย context ใหม่ จึงต้องรับเจตนาและการตัดสินใจผ่านไฟล์ ไม่ควรหวังว่า conversation เดิมจะตามข้าม session ไปเอง

`intent.md → spec.md → plan.md → diff + tests → PR + review → incident record`

**ผลคือ:** handoff ไม่ต้องพึ่งความจำของ session เดิม และ Git history กลายเป็นร่องรอยว่าใครขออะไร ใครแก้ และใครอนุมัติ

## Build เร็วได้เมื่อขอบเขตกับ permission ชัด (8:23-10:59)

Rob เห็นด้วยกับ auto mode เมื่อทีมมี environment ที่ล็อกไว้แล้ว มี permission และรายการ tool, web source, package ที่อนุญาตชัด เขาไม่ได้เสนอให้เปิดสิทธิ์กว้างตั้งแต่วันแรก แต่ให้ค่อย ๆ สะสม policy จากสิ่งที่ทีมยอมรับว่า agent ทำได้

Hooks ทำหน้าที่บังคับกฎระหว่างทำงาน เช่นกันไม่ให้แตะบางโฟลเดอร์ ห้ามใช้ package ที่ยังไม่ผ่าน หรือบังคับให้แก้ `plan.md` เมื่อ implementation เปลี่ยน Worktree ช่วยแยก agent หลายตัวที่ทำงานพร้อมกัน ส่วน subagent ใช้แตกงานที่ไม่ขึ้นต่อกัน

ตรงนี้มีเงื่อนไขสำคัญ: การเพิ่ม agent พร้อมกันเพิ่ม output และ blast radius ด้วย ถ้า permission, test และ review capacity ไม่โตตาม ความเร็วช่วง build จะสร้างงานค้างให้คนมากกว่าเดิม

## Test และ eval ต้องป้อน feedback กลับไปหา agent (11:00-12:23)

เป้าหมายคือให้ agent ทดสอบให้มากก่อนถึงมือ engineer หรือ QA ทั้ง unit test, lint, build, end-to-end test และ visual check ผ่าน Playwright หรือ browser tool ผลทดสอบต้องกลับเข้า loop เพื่อให้ agent แก้ ไม่ใช่จบเป็นรายงานที่รอคนอ่านอย่างเดียว

Rob แยก `eval` ออกจาก test ทั่วไปตรงที่ eval ใช้วัด workflow ของ agent โดยตรง เขายกตัวอย่างการเก็บ issue ราว 20 เคสพร้อม expected outcome แล้วรันใหม่เมื่อเปลี่ยน model, skill หรือวิธีทำงานหลัก เพื่อดูว่า lifecycle regress หรือไม่ ตัวเลข 20 เป็นตัวอย่างในคลิป ไม่ใช่มาตรฐานขั้นต่ำ

**ได้อะไร:** ทีมเห็นผลเสียของการเปลี่ยน model หรือ skill ก่อนปล่อยให้ workflow ใหม่ทำงานจริงวงกว้าง

## Review, deployment gate และ maintenance (12:24-15:23)

หลัง build กับ test agent เปิด PR จาก branch หรือ worktree ของตัวเอง แล้ว reviewer อีก instance ตรวจเทียบกับ policy และ security rule หากเจอปัญหา agent ฝั่ง implement อาจรับ comment ไปแก้ต่อได้ แต่ deterministic CI, branch protection และ permission gate ยังต้องคั่นก่อน merge หรือ production deploy

Rob อธิบาย human review ว่าอยู่ตรง gate สำคัญ ทีมอาจลดจำนวนคนในงานที่ criticality ต่ำได้ แต่ release ที่เสี่ยงยังต้องมีผู้มีอำนาจอนุมัติ จึงไม่ใช่สูตร "AI review แล้ว auto-merge ทุกอย่าง"

ช่วง Maintain เป็นภาพที่ไกลที่สุด Alert, ticket, Slack message หรือ schedule อาจเรียก agent ให้ตรวจ log วินิจฉัย แล้วเขียน `intent.md` ใหม่กลับเข้าต้นวงจร Playbook อย่างเป็นทางการระบุเพิ่มว่า trigger ควรเป็น deterministic control band และ agent ทำได้เฉพาะ route ที่ gate ไว้ เช่นเปิด PR หรือเรียก runbook ที่อนุมัติแล้ว ไม่ควรมี production credential ติดตัวเป็นปกติ

**ผลคือ:** maintenance เปลี่ยนจากรอคนเริ่มสืบ มาเป็นให้ระบบเตรียม diagnosis กับข้อเสนอไว้ก่อน ส่วนการตัดสินใจที่เสี่ยงยังรอคน

## สิ่งที่ทีมทั่วไปควรหยิบไปใช้ก่อน (15:24-16:02)

Rob ไม่แนะนำให้ทิ้ง workflow เดิมทั้งหมดเพื่อทำตาม playbook เขามองว่า Superpowers, BMAD, loop, graph orchestration หรือระบบที่ทีมสร้างเองอาจตอบโจทย์อยู่แล้ว สิ่งที่ควรหยิบไปก่อนมีสี่อย่าง

1. คุยกับ originator แล้วเก็บ `intent.md` ที่เจ้าตัวตรวจเอง
2. ทำ artifact แต่ละชิ้นให้มี owner, version และเกณฑ์รับต่อ
3. ให้ test, lint และ eval เป็น feedback ที่ agent รันเองได้
4. เพิ่ม autonomy ตาม criticality โดยวาง human review กับ deployment gate ในจุดที่ย้อนกลับยาก

ประโยคปิดของคลิปคือไม่มี one-size-fits-all จำนวนคน จำนวน agent และระดับ autonomy ต้องตามงาน ทีม และความเสียหายถ้าพลาด

## ข้อจำกัดและเรื่องที่ยังตอบไม่ได้

- คลิปเป็นคำอธิบายชั้นสอง Rob ผสมเนื้อหาจาก playbook กับ workflow ที่เขาสอนเอง บางรายละเอียดจึงเป็นคำแนะนำของ Rob ไม่ใช่ข้อกำหนดของ Anthropic
- ช่วง Neon เป็นโฆษณาที่ผู้พูดเปิดเผย และคลิปยังโปรโมตคอร์ส Switch Dimension กับ Molten OS ของเขาเอง คำแนะนำเรื่อง tool และ skill จึงมีผลประโยชน์ทางการค้าอยู่ด้วย
- `intent.md` ลดการสูญเสียความหมายระหว่าง handoff แต่ยังเป็น prose ที่ agent ต้องตีความ จึงไม่ปิด [[intent-gap]] และไม่แทน test, schema, invariant หรือ human judgement
- Artifact ที่ versioned สร้าง audit trail ได้ แต่ถ้า `intent.md`, `spec.md`, `plan.md` และ code เปลี่ยนไม่พร้อมกัน chain จะกลายเป็นเอกสารหลายชิ้นที่ขัดกันเอง
- คำว่า autonomous maintenance ในคลิปฟังกว้างกว่ารายละเอียดต้นทาง Playbook ยังวาง deterministic detection, permission tier, PR gate และ human triage ไว้ จึงเป็น gated autonomy มากกว่าการให้ agent ดูแล production เองเต็มรูปแบบ
- Playbook บอกให้คนอนุมัติ artifact ที่ใช้ judgement แต่ก็ต้องการลดขั้นตอนที่วิ่งด้วยความเร็วคน จุดสมดุลระหว่าง throughput กับ accountability ยังต้องหาแยกในแต่ละองค์กร

## See also

- [[rob-shocks]]
- [[anthropic]]
- [[claude-code]]
- [[boris-cherny]]
- [[intent-md]]
- [[artifact-chain]]
- [[ai-driven-sdlc]]
- [[spec-driven-development]]
- [[plan-mode-as-prompting]]
- [[agentic-code-review]]
- [[evals-and-error-analysis]]
- [[intent-gap]]
- [[the-new-software-lifecycle]]
