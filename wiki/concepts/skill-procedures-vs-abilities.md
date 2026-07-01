---
title: Skills — Procedures vs Abilities
type: concept
tags: [ai-skill, agents, context-window, prompting, pocock]
created: 2026-06-21
updated: 2026-07-01
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md", "i don't want to use your agent — @RhysSullivan.md", l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Skills: Procedures vs Abilities / สกิลแบบ "เราสั่ง" vs "model หยิบเอง"

**[[matt-pocock|Matt Pocock]] แยก agent skill เป็นสองชนิดตามว่า "ใครเป็นคนเรียกใช้": procedures (เราสั่งเอง) กับ abilities (model หยิบไปใช้เอง).** เป็นกรอบช่วยตัดสินใจว่าจะเขียน skill แบบไหน และจะให้ model คุมแค่ไหน

## สองชนิด

| ชนิด | ใครเรียก | ตัวอย่าง |
|---|---|---|
| **Procedure** | **เราสั่งเอง** — invoke เพื่อให้ model ทำตามขั้นตอน | [[grill-me\|grill me]], 2prd (เขียน PRD), workflow ที่เราคุมลำดับ |
| **Ability** | **model หยิบไปใช้เอง** ระหว่างทำงาน | ไฟล์ coding standards (เช่น "เขียน React ห้ามใช้ useEffect ให้ใช้อย่างอื่น") |

ตัวอย่าง ability: agent กำลังเขียน React อยู่ มันรู้ตัวว่าต้องเช็คว่าเราชอบเขียนแบบไหน เลยดึง ability "React coding standards" มาอ่านเอง แล้วทำตาม. เราไม่ได้สั่ง — model ตัดสินใจหยิบเอง

## ทำไม Matt ชอบ procedures

> "I don't want to delegate my thinking to the model... I've always preferred to me personally be in control because I know my skills, I know my abilities."

1. **อยากเป็นคนคุม** — Matt ชอบขับเอง: สั่ง grill me → เขียน PRD → แตกเป็น issue. ไม่อยากยกการคิดให้ model
2. **เหตุผลเชิงเทคนิค: ทุก skill leak description เข้า context window** — มี 100 skill ก็ leak 100 บรรทัดคำอธิบายเข้าไปทุก session กิน context ฟรี ๆ. แก้ได้ด้วย `disable model invocation: true` → skill นั้นเรียกได้เฉพาะ user และ **ไม่ leak description** เข้า context

แนวคิดที่ลึกกว่านั้น: Matt อยากให้ความรู้ส่วนใหญ่ **อยู่ในหัวคน (developer) ไม่ใช่ในหัว AI** — คนเป็นคนขับ ถือพวงมาลัย

## ทางตรงข้าม: superpowers

[[superpowers|superpowers]] (skill repo ดังของ [[superpowers|Obra]]) เลือกทางตรงข้าม — ออกแบบให้ **model เป็นคนคุม** (หยิบ ability เอง) มากกว่า. ไม่ใช่ผิด แค่คนละปรัชญา: ขึ้นกับว่าเราอยากเป็นคนขับ หรืออยากให้ model ขับ

## เชื่อมกับ knowledge/skills/wisdom

ของที่ตื่นเต้นในยุคนี้คือเราเอา **knowledge + skills** (ดู [[knowledge-skills-wisdom]]) มามัดเป็น procedure ที่ reuse และแจกทีมได้ — เหมือนดึง function ที่ซ้ำสามรอบออกมาเป็น shared function. ทุกคนในทีม plan แบบเดียวกันและช่วยกันปรับ skill นั้น = ยกพื้นของทั้งทีม

## Product skills สำหรับ agent ของผู้ใช้

[[rhys-sullivan|Rhys Sullivan]] เสนอใน [[i-dont-want-to-use-your-agent]] ว่า product company ควรปล่อย skill ที่ทำให้ [[bring-your-own-agent|agent ของผู้ใช้]] กลายเป็น expert ใน product นั้น. แบบนี้ skill ไม่ได้อยู่แค่ใน repo ของทีม dev แต่กลายเป็น product surface.

ตัวอย่าง: [[linear|Linear]] อาจให้ procedure สำหรับแตก problem ใหญ่เป็น ticket; [[cloudflare|Cloudflare]] อาจให้ procedure ที่ผูก docs กับ CLI commands; [[posthog|PostHog]] อาจให้ procedure สำหรับวิเคราะห์ funnel แล้ว deeplink กลับ dashboard.

ตรงนี้ procedure/ability ยังเป็นคำถามเดิม: skill บางตัวควรให้ user เรียกเองเพราะเปลี่ยน workflow ชัดเจน, บางตัวควรให้ model หยิบเองเมื่อเจอ product context. สิ่งที่สำคัญคือ description ต้องไม่บวมจนกิน context ฟรี.

## คำแนะนำ: เริ่มจาก blank slate

Matt แนะนำให้ลบ skill / plugin / MCP / `CLAUDE.md` / `AGENTS.md` ทิ้งหมดก่อน แล้วดูว่า agent ทำอะไรในโหมดเปล่า ๆ — เพราะคนส่วนใหญ่ทำ context window บวมด้วย instruction เกินจำเป็น. จากนั้นค่อย layer **procedures ที่เราเลือกเอง** กลับเข้าไปทีละอัน

## มุม Kun Chen: skill เป็นที่เก็บ context แบบมีเงื่อนไข

[[kun-chen|Kun Chen]] ใช้ skill เพื่อลด project memory bloat ใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow walkthrough]]. ตัวอย่างของเขาคือ E2E testing instructions: จำเป็นมากตอน agent แก้โค้ด แต่ไร้ประโยชน์ตอนคนแค่ถามคำถาม. ถ้าใส่ไว้ใน memory file มันกิน token ทุก session. ถ้าแยกเป็น skill agent จะโหลดเฉพาะตอนต้องใช้.

เขายังเตือนว่า skill จากอินเทอร์เน็ตไม่ควรถูกติดตั้งเพราะ popular. Skill มีอำนาจสั่ง agent รันคำสั่งบนเครื่องได้ และบาง skill ที่ดูดังอาจทำให้ผลลัพธ์แย่ลงหรือใช้ token เพิ่มขึ้น.

**ได้อะไร:** skill ควรถูกมองเป็น executable procedure/context ไม่ใช่ markdown ที่ไม่มีผลข้างเคียง. ยิ่ง skill มีอำนาจมาก ยิ่งต้องผ่าน trust และ evaluation.

## ดูเพิ่ม

- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[grill-me]]
- [[knowledge-skills-wisdom]]
- [[teach-skill]]
- [[superpowers]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[bring-your-own-agent]]
- [[i-dont-want-to-use-your-agent]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[kun-chen]]
- [[progressive-disclosure]]
