---
title: CLAUDE.md File
type: concept
tags: [claude-code, claude-md, prompt-engineering, workflow, harness]
created: 2026-04-22
updated: 2026-09-14
sources: [cyril-xbt-claude-md-guide.md, alex-ker-harnesses-optimize.md, claude-code-subagents-docs.md, This Anthropic Engineer Uses Claude Code Differently Than Everyone Else.md, boris-cherny-cut-80-percent-claude-code-prompt.md, ai-native-sdlc-playbook.md]
---

# CLAUDE.md File / ไฟล์ CLAUDE.md

`CLAUDE.md` คือไฟล์ markdown ที่ [[claude-code|Claude Code]] (CLI ของ Anthropic สำหรับ coding agent) อ่านโดยอัตโนมัติเมื่อเริ่ม session หากพบในโฟลเดอร์โปรเจกต์ ไฟล์นี้ทำหน้าที่เป็น **persistent system prompt** ที่มาพร้อมกับ repo เพื่อบอกรายละเอียดเกี่ยวกับโปรเจกต์ เช่น stack ที่ใช้, convention ในการเขียนโค้ด, และสิ่งที่ *ห้าม* ทำ

ไฟล์นี้เป็นเครื่องมือหลักที่ผู้ใช้ใช้ในการ "โปรแกรม" agent โดยไม่ต้องพิมพ์คำสั่งซ้ำทุกครั้งที่เริ่ม session ใหม่

## ตำแหน่งของไฟล์

Claude Code จะค้นหาไฟล์นี้ใน 3 ตำแหน่ง โดยเรียงลำดับจากเฉพาะเจาะจงที่สุดไปหาทั่วไปที่สุด:

| ตำแหน่ง | การใช้งาน | เนื้อหา |
|---|---|---|
| `<project>/CLAUDE.md` | อ่านเมื่อเริ่ม session ในโฟลเดอร์นั้น | บริบทเฉพาะของโปรเจกต์ — stack, convention, กฎของงานนี้ |
| `<project>/<subdir>/CLAUDE.md` | ใน monorepo — อ่านตามโฟลเดอร์ที่กำลังทำงานอยู่ | บริบทเฉพาะของ package/service ใน monorepo |
| `~/.claude/CLAUDE.md` | ทุก session ทุกโปรเจกต์ | ค่า voorkeur ส่วนตัวที่ไม่เปลี่ยนแปลง — ภาษาที่ชอบ, tone, กฎสากล |

การทำงานแบบ layer นี้ทำให้เมื่อเปิดโปรเจกต์ใหม่ Claude จะได้รับทั้ง **ค่า voorkeur ส่วนตัว + บริบทของโปรเจกต์** ในทันที

## โครงสร้างไฟล์ 7 ส่วน (ตามคำแนะนำของ cyrilXBT)

[[cyril-xbt|Cyril]] ได้เสนอ template 7 หัวข้อเพื่อป้องกันไม่ให้ Claude ตัดสินใจเองในเรื่องสำคัญ:

1.  **Project Overview** — 1–2 ย่อหน้า: อธิบายว่าโปรเจกต์ทำอะไร, user คือใคร, และ priority หลักคืออะไร
2.  **Tech Stack** — รายการที่ชัดเจน: framework, styling, ภาษา, ฐานข้อมูล, auth, deployment, package manager, state management, charting library — อย่าคาดหวังให้ model เดาเอง
3.  **Coding Conventions** — กฎเฉพาะ: named vs default export, kebab-case vs PascalCase, arrow function, strict type, ขนาดของ component, co-location rule
4.  **Never Do This** — ข้อห้ามที่ชัดเจนสำหรับพฤติกรรมที่ over-helpful: ห้ามติดตั้ง package เอง, ห้าม refactor ไฟล์ที่ไม่ได้สั่ง, ห้ามใส่ placeholder comment, ห้าม wrap try/catch โดยไม่แจ้ง
5.  **File Structure** — แสดง directory tree พร้อมคอมเมนต์ว่าอะไรควรอยู่ที่ไหน และส่วนไหนห้ามแก้ไข
6.  **Current Sprint Goals** — งานที่ *กำลัง* ทำอยู่ และระบุ **out of scope** ให้ชัดเจน
7.  **Important Context** — การตัดสินใจที่เคยทำไปแล้ว, rate limit, ข้อจำกัดของ infrastructure, bug ที่เคยเจอ — เพื่อป้องกันไม่ให้ Claude เสนอทางที่เคยถูกปฏิเสธไปแล้ว

**ข้อดี:** เมื่อมีครบ 7 ส่วน Claude ไม่ต้องเดา stack หรือ convention และมี "ข้อห้าม" ที่ชัดเจน ทำให้ไม่ต้องคอยเตือนซ้ำๆ ในทุก session

## Global File (Preference Layer)

สำหรับสิ่งที่ไม่เปลี่ยนแปลงข้ามโปรเจกต์ ควรย้ายไปไว้ที่ `~/.claude/CLAUDE.md`:

-   **Defaults ส่วนตัว** — ใช้ TS ก่อน JS เสมอ, `pnpm`, arrow function, explicit type
-   **Communication rules** — ห้ามขึ้นต้นด้วย "Great question", สื่อสารให้สั้นกระชับ, เขียน code ก่อนอธิบาย
-   **Never สากล** — no placeholder comment, no default export, no `console.log` ใน production

การทำงานร่วมกันของ project file และ global file ทำให้คุณสามารถตั้งค่า voorkeur ของตัวเองเพียงครั้งเดียว และทุกโปรเจกต์จะนำไปใช้โดยอัตโนมัติ

## การประยุกต์ใช้นอกเหนือจากงานโค้ด

Cyril ได้ยกตัวอย่างการใช้กับ content pipeline: Project Overview (ระดับความรู้ของผู้อ่าน), Writing Style Rules (ห้ามใช้คำว่า "utilize", ห้ามใช้ em dash, ใช้ capitalization เพื่อเน้นอารมณ์เท่านั้น), What I Never Want, Tone

หลักการเดียวกันคือ: บันทึกกฎพฤติกรรมลงในไฟล์ แล้ว agent จะสามารถปฏิบัติตามได้ทุกครั้งโดยไม่ต้องสอนใหม่

## ความขัดแย้งกับ [[instruction-budget]]

มีความเห็นที่ไม่ตรงกันระหว่างคำแนะนำของ Cyril และ [[alex-ker|Alex Ker]] ซึ่งควรทำความเข้าใจก่อนนำ template ยาวๆ มาใช้:

| ประเด็น | Cyril (ตาม guide นี้) | Alex Ker ([[instruction-budget]]) |
|---|---|---|
| **ขนาดไฟล์** | ครบ 7 ส่วน, "Never" list สามารถยาวได้ | **minimal requirements** เท่านั้น |
| **กฎพฤติกรรม** | ใส่ใน CLAUDE.md โดยตรง | ย้ายไปเป็น skill แยก แล้วดึงมาใช้ด้วย [[progressive-disclosure]] |
| **เป้าหมาย** | ป้องกันไม่ให้ Claude ทำสิ่งที่ผู้ใช้ไม่ชอบซ้ำ | อยู่ภายใต้ "dumb zone" (~ vài trăm instructions) |
| **ความเสี่ยง** | หากยาวเกินไป model อาจเริ่มพลาด rule | หากสั้นเกินไป model อาจจะ default เองบ่อยครั้ง |

**ทั้งสองเห็นตรงกันว่า**: ไฟล์ควร **เขียนโดยคน ไม่ใช่ LLM generate** (อ้างอิงจากงานวิจัยของ ETH ที่ Alex Ker กล่าวถึง) และต้อง *specific ไม่ใช่ vague* (เช่น "write clean code" ไม่มีประโยชน์)

**จุดที่แตกต่าง**: Cyril ยอมจ่าย rule cost เพื่อแลกกับ correction savings ในขณะที่ Alex Ker กังวลเกี่ยวกับ attention budget ที่จะถูกใช้ไป โดยเฉพาะเมื่อรวม global, project, และ subdir CLAUDE.md เข้ากับ skill/MCP description ทั้งหมด

### วิธีการนำไปใช้

-   สำหรับ model ระดับ frontier (Opus 4.7), template 7 ส่วนของ Cyril มักจะไม่เกิน budget หากแต่ละส่วนไม่ยาวเกินไป
-   ระวัง "Never Do This" ที่ยาวขึ้นเรื่อยๆ — เมื่อถึงจุดหนึ่ง ควรย้ายกฎที่ใช้เฉพาะบางงานไปเป็น skill
-   ถ้า Claude เริ่มพลาด rule ที่เขียนไว้อย่างชัดเจน นั่นเป็นสัญญาณว่า instruction budget เต็ม ไม่ใช่ว่าไฟล์ "เขียนไม่ชัดเจนพอ" — อย่าเพิ่มกฎ แต่ให้ย้ายไปเป็น skill แทน

## ข้อผิดพลาดที่พบบ่อย (จาก Cyril)

1.  **Vague เกินไป** — "เขียนโค้ดให้สะอาด" ไม่ช่วยอะไร; "named export, kebab-case, no default export" ช่วยได้ทันที
2.  **เขียนครั้งเดียวแล้วไม่อัปเดต** — ทุกการตัดสินใจสำคัญที่ตัดทางเลือกออกไป ควรบันทึกลงในไฟล์ — มิฉะนั้น Claude อาจเสนอทางเดิมซ้ำ
3.  **ใส่ goal ผิดที่** — CLAUDE.md เป็น briefing document ไม่ใช่ TODO list; goal เปลี่ยนทุกสัปดาห์ แต่ส่วนที่เหลือควรคงที่
4.  **ข้ามส่วน NEVER** — เป็นส่วนที่คุ้มค่าที่สุดสำหรับนักพัฒนาที่มีประสบการณ์ เพราะคุณรู้ว่าคุณไม่ชอบอะไร
5.  **ไม่มี global file** — ทำให้ต้องเสียเวลาเขียน voorkeur ของตัวเองใหม่ทุกโปรเจกต์

## การทำงานร่วมกับ Slash Commands

ขั้นตอนต่อไปคือการแยก **project-wide context** (CLAUDE.md) ออกจาก **task-specific workflow** (slash commands ใน `.claude/commands/*.md`)

ตัวอย่าง `.claude/commands/new-component.md`:
```text
สร้าง React component ใหม่ตามสเปค:
- TypeScript functional
- Named export เท่านั้น
- Tailwind
- ประกาศ Props interface ก่อน component
- วางใน src/components/features/ เว้นแต่จะสั่งเป็นอย่างอื่น
- File name เป็น kebab-case
- ถามชื่อและวัตถุประสงค์ก่อนเริ่มเขียน
```
เมื่อพิมพ์ `/new-component`, Claude จะได้รับ spec ทั้งหมดทันที — และ spec นี้ไม่จำเป็นต้องอยู่ใน CLAUDE.md หลัก (ซึ่งจะกิน budget โดยไม่จำเป็นถ้าไม่ได้สร้าง component ทุกวัน) นี่คือ [[progressive-disclosure]] ที่ harness layer

## ตำแหน่งในภาพรวม

CLAUDE.md เป็น **instance หนึ่งของการตั้งค่า [[coding-harness]]** — เป็นปุ่มปรับหลักที่ผู้ใช้ใช้ในการปรับเปลี่ยนพฤติกรรมของ agent ผ่าน Claude Code โดยไม่ต้องแก้ไข tool, model, หรือ runtime

-   [[instruction-budget]] — ข้อจำกัดที่ CLAUDE.md ต้องอยู่ภายใต้
-   [[progressive-disclosure]] — กลไกที่ช่วยให้ไฟล์สั้นลงโดยไม่สูญเสียความสามารถ
-   [[coding-harness]] — CLAUDE.md + slash commands + skills + MCP = harness ทั้งหมด
-   subagent frontmatter ([[subagent-patterns]]) — `.claude/agents/*.md` เป็นอีก instance หนึ่งของ pattern เดียวกัน: markdown file ที่ harness อ่านตอน runtime

## การอัปเดตไฟล์เมื่อโมเดลเปลี่ยนไป

[[cal-rueb|Cal Rueb]] แนะนำว่าเมื่อมีการเปลี่ยนไปใช้โมเดลรุ่นใหม่ที่ฉลาดขึ้นและทำตามคำสั่งได้ดีขึ้น (เช่น การเปลี่ยนผ่านสู่รุ่น 4.0 หรือ [[claude-opus-4-7|Opus 4.7]]) เป็นช่วงเวลาที่ดีที่จะกลับมาทบทวนไฟล์ `CLAUDE.md` กฎหลายอย่างที่เคยต้องเขียนเพื่อป้องกันไม่ให้โมเดลเก่าทำผิด (เช่น การห้ามเขียนคอมเมนต์ซ้ำซ้อน) อาจไม่จำเป็นอีกต่อไป การลบกฎที่ไม่จำเป็นออกจะช่วยลดการใช้ [[instruction-budget]] ลงได้

[[boris-cherny|Boris Cherny]] ไปไกลกว่านั้นใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์กับ Y Combinator]]: เขาแนะนำให้ลองลบ `CLAUDE.md`, skills และ hooks ทุกหกเดือน ดูว่า model รุ่นใหม่ทำอะไรได้เอง แล้วเพิ่มกลับเมื่อเห็นมันพลาดเรื่องเดิมซ้ำ ๆ วิธีนี้สอดคล้องกับ [[prompt-ablation|prompt ablation]] ที่ทีม Claude Code ใช้ตัด system prompt ของ Opus 5 ออกราว 80%

คำแนะนำนี้ไม่หักล้างเคส DHH ด้านล่างที่เขียนกฎแล้ว agent ยังพลาด เพราะสองกรณีตอบคนละ failure ถ้า model ทำได้เอง กฎนั้นอาจลบได้ ถ้ายังพลาดซ้ำ ให้เก็บกฎหรือย้ายไปเป็น linter/test ที่บังคับได้จริง ส่วน hook ที่ทำหน้าที่เป็น security gate ไม่ควรถูกลบพร้อม behavioral instruction โดยไม่ทดสอบความเสี่ยงแยก

## เรื่องเล่าจากหน้างาน — เขียนกฎไว้แล้วยังต้องเตือนซ้ำ

[[dhh|DHH]] เล่าใน [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์กับ Lex Fridman]] ว่าเขามีข้อห้ามเรื่อง early exit อยู่ใน `AGENTS.md` ของ [[omarchy|Omarchy]] คือห้าม agent เขียน bash เป็น precondition แล้ว exit ต่อกันเป็นชั้น ๆ แต่ agent ยังทำอยู่ และเขาต้องเตือนให้กลับไปอ่านไฟล์ทุกครั้งที่จับได้

> "I have to smack the agents over the back of the head every single time I catch it and remind it to look at the agents MD file."

`AGENTS.md` เป็นไฟล์คนละชื่อกับ `CLAUDE.md` แต่ทำหน้าที่เดียวกัน คือกฎประจำ repo ที่ agent อ่านตอนเริ่มงาน ข้อสังเกตนี้จึงใช้ได้กับทั้งสองไฟล์

สิ่งที่ควรเรียนจากเรื่องนี้ไม่ใช่ "ไฟล์คำสั่งไม่มีประโยชน์" แต่คือกฎที่เป็นรสนิยมด้าน style มักถูกละเลยง่ายกว่ากฎที่มีเครื่องตรวจ ถ้าเรื่องนั้นสำคัญจริงและตรวจอัตโนมัติได้ ควรย้ายไปเป็น linter หรือ test แทนที่จะฝากไว้กับข้อความในไฟล์อย่างเดียว ต่อกับ [[instruction-budget]] ตรงที่กฎยิ่งเยอะ โอกาสที่แต่ละข้อจะถูกทำตามยิ่งเจือจาง

## `CLAUDE.md` ใน AI-Native SDLC ของ Anthropic

[[ai-native-sdlc-playbook|Playbook ของ Anthropic]] วาง `CLAUDE.md` ไว้เป็น "ความรู้ของทีมที่ version ได้" ในช่วง Build เก็บ convention ของ repo คำสั่ง build โครงสถาปัตยกรรม และความผิดพลาดที่เจอบ่อย

เอกสารให้กฎดูแลไฟล์ไว้สองข้อ

- **พลาดเรื่องเดิมสองครั้ง ให้เขียนลงไฟล์** ไม่ใช่เขียนทุกอย่างที่นึกออกไว้ก่อน finding จาก code review รอบสองก็เข้าเกณฑ์เดียวกัน
- **ยาวไม่เกินหนึ่งหน้า** เพราะทุก session ที่เปิดใหม่ต้องอ่านไฟล์นี้ทั้งไฟล์ ความยาวจึงเป็นต้นทุนคงที่ เรื่องเดียวกับ [[instruction-budget]]

Playbook เพิ่มสิ่งที่คำแนะนำทั่วไปมักไม่พูดถึงอีกสองเรื่อง ทุกครั้งที่แก้ `CLAUDE.md` ต้องรัน eval เพราะไฟล์นี้เป็น config ที่เปลี่ยนพฤติกรรมทุก session พร้อมกัน และต้อง gate การ merge ไว้ที่ pass rate ส่วนตัววัดที่เสนอคือเวลาที่คนใหม่ในทีมใช้กว่าจะ merge PR แรกได้ ถ้าไฟล์ช่วยให้เข้าใจ repo เร็วขึ้น เวลานี้ก็ควรลดลง

**ได้อะไร:** ไฟล์นี้เลิกเป็นที่กอง prompt ส่วนตัว แล้วกลายเป็น artifact ที่มีเกณฑ์เพิ่ม มีเพดานความยาว และมี regression test

## ดูเพิ่มเติม

-   [[cal-rueb]]
-   [[claude-code]]
-   [[cyril-xbt]]
-   [[instruction-budget]]
-   [[progressive-disclosure]]
-   [[coding-harness]]
-   [[subagent-patterns]]
-   [[cyril-xbt-claude-md-guide]]
-   [[alex-ker-harnesses-optimize]]
-   [[dhh-strategies-programming-with-ai-agents-lex-clips]]
-   [[make-it-simpler]]
-   [[prompt-ablation]]
-   [[boris-cherny-cut-80-percent-claude-code-prompt]]
- [[ai-native-sdlc-playbook]]
- [[policy-as-code-for-agents]]
