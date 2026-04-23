---
title: CLAUDE.md File
type: concept
tags: [claude-code, claude-md, prompt-engineering, workflow, harness]
created: 2026-04-22
updated: 2026-04-22
sources: [cyril-xbt-claude-md-guide.md, alex-ker-harnesses-optimize.md, claude-code-subagents-docs.md]
---

# CLAUDE.md File / ไฟล์ CLAUDE.md

`CLAUDE.md` คือไฟล์ markdown ที่ [[claude-code|Claude Code]] (CLI ของ Anthropic สำหรับ coding agent) อ่านอัตโนมัติตอนเริ่ม session ถ้าเจอในโฟลเดอร์โปรเจกต์ ทำหน้าที่เป็น **persistent system prompt** ที่ติดมากับ repo — โปรเจกต์คืออะไร, stack ที่ใช้, convention การเขียนโค้ด, สิ่งที่ *ห้าม* ทำ

ไฟล์นี้คือเครื่องมือหลักที่ user ใช้ "โปรแกรม" ตัว agent โดยไม่ต้องพิมพ์ซ้ำทุก session

## ไฟล์อยู่ที่ไหนได้บ้าง

Claude Code หาไฟล์ 3 ที่ เรียงจาก specific ไป general:

| ที่ | ใช้ตอนไหน | ใช้เขียนอะไร |
|---|---|---|
| `<project>/CLAUDE.md` | อ่านตอนเริ่ม session ในโฟลเดอร์นั้น | บริบทเฉพาะโปรเจกต์ — stack, convention, กฎของงานนี้ |
| `<project>/<subdir>/CLAUDE.md` | ใน monorepo — อ่านตามโฟลเดอร์ที่กำลังทำอยู่ | บริบทเฉพาะ package/service ใน monorepo |
| `~/.claude/CLAUDE.md` | ทุก session ทุกโปรเจกต์ | preference ส่วนตัวที่ไม่เปลี่ยน — ภาษาที่ชอบ, tone, กฎสากล |

Layer สะสมกัน ทำให้เวลาเปิด project ใหม่ Claude ได้ **preference ส่วนตัว + บริบทโปรเจกต์** ทันที

## โครงไฟล์แบบ 7 ส่วน (cyrilXBT)

[[cyril-xbt|Cyril]] เสนอ template 7 หัวข้อที่กันช่องว่างที่ Claude ชอบ default ไปเอง:

1. **Project Overview** — 1–2 ย่อหน้า: โปรเจกต์ทำอะไร, user เป็นใคร, อะไรคือ priority หลัก
2. **Tech Stack** — list ชัดเจน: framework, styling, language, DB, auth, deployment, package manager, state, chart lib — อย่าคาดหวังให้ model เดา
3. **Coding Conventions** — กฎเฉพาะ: named vs default export, kebab-case vs PascalCase, arrow function, strict type, ขนาด component, co-location rule
4. **Never Do This** — hard stop สำหรับพฤติกรรม over-helpful: ห้ามติดตั้ง package เอง, ห้าม refactor ไฟล์ที่ไม่ได้สั่ง, ห้ามใส่ placeholder comment, ห้าม wrap try/catch โดยไม่บอก
5. **File Structure** — directory tree พร้อมคอมเมนต์ว่าอะไรวางตรงไหน, อะไรห้ามแตะ
6. **Current Sprint Goals** — งานที่ *กำลัง* ทำอยู่ + ระบุ **out of scope** ให้ชัด
7. **Important Context** — decision ที่ตัดทิ้งไปแล้ว, rate limit, constraint ของ infra, bug ที่เคยเจอ — กันไม่ให้ Claude เสนอทางที่เคย ruled out

ได้อะไร: พอครบ 7 ส่วน Claude ไม่ต้องเดา stack, ไม่ต้องเดา convention, และมี "รู้แล้วว่าห้าม" ที่ชัดเจน เลิกต้องเตือนซ้ำทุก session

## Global file (preference layer)

ของที่ไม่เปลี่ยนข้ามโปรเจกต์ให้ย้ายไป `~/.claude/CLAUDE.md`:

- **Defaults ส่วนตัว** — TS ก่อน JS เสมอ, `pnpm`, arrow function, explicit type
- **Communication rules** — ห้ามขึ้นต้นด้วย "Great question", ตัดน้ำให้สั้น, เขียน code ก่อนอธิบาย
- **Never สากล** — no placeholder comment, no default export, no `console.log` ใน production

Project file + global file ทำงานสองชั้นพร้อมกัน — คุณเขียน preference ตัวเองครั้งเดียว แล้วทุกโปรเจกต์ได้ไปโดยไม่ต้อง copy

## ใช้กับงานที่ไม่ใช่ code ก็ได้

Cyril ยกตัวอย่างโฟลเดอร์ content pipeline: Project Overview (ผู้อ่านระดับไหน), Writing Style Rules (ห้ามใช้ "utilize", ห้าม em dash, capitalization เพื่อเน้นอารมณ์เท่านั้น), What I Never Want, Tone

หลักเดียวกัน — กฎพฤติกรรมอัดลงไฟล์ แล้ว agent ทำตามได้ทุกครั้งโดยไม่ต้องสอนใหม่

## ความตึงกับ [[instruction-budget]]

มีจุดไม่ตรงกันที่สำคัญระหว่างคำแนะนำของ Cyril กับ [[alex-ker|Alex Ker]] — ต้องเข้าใจก่อนจะ copy template ยาว ๆ มาใช้:

| ประเด็น | Cyril (guide นี้) | Alex Ker ([[instruction-budget]]) |
|---|---|---|
| ขนาดไฟล์ | 7 ส่วนครบ, "Never" list ยาวได้ | **minimal requirements** เท่านั้น |
| กฎพฤติกรรมละเอียด | ใส่ใน CLAUDE.md ตรง ๆ | ย้ายไป skill แยก ดึงมาด้วย [[progressive-disclosure]] |
| เป้าหมาย | Claude ไม่ทำสิ่งที่ user เกลียดซ้ำ | อยู่ใต้ "dumb zone" (~few hundred instructions) |
| ความเสี่ยง | ถ้ายาวเกิน model เริ่ม miss rule | ถ้าสั้นเกิน model default ไปเองบ่อย |

**ทั้งคู่เห็นตรงกันที่**: ไฟล์ควร **คนเขียน ไม่ใช่ LLM generate** (ETH research ที่ Alex Ker อ้าง), ต้อง *specific ไม่ใช่ vague* ("write clean code" ใช้ไม่ได้)

**จุดที่ต่าง**: Cyril ยอมจ่าย rule cost แลก correction savings — Alex Ker ห่วง attention budget ที่โดนกิน โดยเฉพาะเมื่อรวม global + project + subdir CLAUDE.md กับ skill/MCP description ทั้งหมด

### How to apply

- สำหรับ model ระดับ frontier (Opus 4.7) template 7 ส่วนของ Cyril มักจะยังไม่ชน budget ถ้าแต่ละส่วนไม่ยาวเว่อ
- ระวัง "Never Do This" ที่พองขึ้นเรื่อย ๆ — ถึงจุดหนึ่งควร promote กฎที่ใช้เฉพาะงานบางประเภทไปเป็น skill
- ถ้า Claude เริ่ม miss rule ที่เขียนชัดแล้ว นั่นคือสัญญาณ instruction budget ตัน ไม่ใช่ว่าไฟล์ "เขียนไม่ชัดพอ" — อย่ารีบเพิ่มกฎ ให้ย้ายไป skill แทน

## ข้อผิดพลาดที่เจอบ่อย (Cyril)

1. **vague เกินไป** — "เขียน code ให้สะอาด" ไม่ช่วยอะไร; "named export, kebab-case, no default export" ช่วยทันที
2. **เขียนครั้งเดียวไม่อัปเดต** — ทุก decision ใหญ่ที่ตัดทางเลือกออก ต้องลงไฟล์ — ไม่งั้น Claude เสนอทางเดิมซ้ำ
3. **เอา goal ไปใส่ที่ไม่ใช่ Current Sprint** — CLAUDE.md คือ briefing document ไม่ใช่ TODO list; goal เปลี่ยนทุกสัปดาห์ ส่วนที่เหลือควรนิ่ง
4. **ข้ามส่วน NEVER** — ส่วนที่คุ้มสุดสำหรับ dev มีประสบการณ์ เพราะคุณรู้อยู่แล้วว่าเกลียดอะไร
5. **ไม่มี global file** — เสียเวลา rewrite preference ตัวเองทุกโปรเจกต์

## ประกอบกับ slash commands

ขั้นต่อไปคือแยก **project-wide context** (CLAUDE.md) ออกจาก **task-specific workflow** (slash commands ใน `.claude/commands/*.md`)

ตัวอย่าง `.claude/commands/new-component.md`:

```text
สร้าง React component ใหม่ตามสเปค:
- TypeScript functional
- Named export เท่านั้น
- Tailwind
- ประกาศ Props interface ก่อน component
- วางใน src/components/features/ เว้นแต่สั่งเป็นอื่น
- File name เป็น kebab-case
ถามชื่อกับวัตถุประสงค์ก่อนเริ่มเขียน
```

พอพิมพ์ `/new-component` Claude ได้ spec เต็มทันที — และ spec นี้ไม่ต้องอยู่ใน CLAUDE.md หลัก (กิน budget เปล่า ๆ ถ้าไม่ได้ทำ component ทุกวัน) นี่คือ [[progressive-disclosure]] ที่ harness layer

## ตำแหน่งในภาพรวม

CLAUDE.md เป็น **instance หนึ่งของ [[coding-harness]] configuration** — มันคือ knob หลักที่ user ใช้ปรับพฤติกรรม agent ผ่าน Claude Code โดยไม่ต้องแก้ tool, model, หรือ runtime

- [[instruction-budget]] — ขีดจำกัดที่ CLAUDE.md ต้องอยู่ใต้
- [[progressive-disclosure]] — กลไกที่ช่วยให้ไฟล์สั้นลงได้โดยไม่เสียความสามารถ
- [[coding-harness]] — CLAUDE.md + slash commands + skills + MCP = harness รวม
- subagent frontmatter ([[subagent-patterns]]) — `.claude/agents/*.md` เป็นอีก instance ของ pattern เดียวกัน: markdown file ที่ harness อ่านตอน runtime

## See also

- [[claude-code]]
- [[cyril-xbt]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[cyril-xbt-claude-md-guide]]
- [[alex-ker-harnesses-optimize]]
