---
title: pi
type: entity
tags: [product, tool, agents, terminal, typescript]
created: 2026-04-28
updated: 2026-07-04
sources: [mario-zechner-pi-agent.md, building-pi-world-of-slop.md, improved-15-llms-harness-changed.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md]
---

# pi (pi.dev) / ไพ

**pi** เป็น terminal-based coding agent ที่พัฒนาโดย [[mario-zechner]] เน้นความเรียบง่าย (Minimalism) และความสามารถในการดัดแปลง (Extensibility) สูงสุด โดยถูกสร้างขึ้นเพื่อเป็นทางเลือกให้กับ [[claude-code]] ที่เริ่มมีความซับซ้อนมากเกินไป

## จุดเด่น (Core Features)

- **Minimal Core**: เริ่มต้นด้วยเครื่องมือเพียง 4 อย่าง (read, write, edit, bash) และ system prompt ที่สั้นมาก
- **[[tree-structured-sessions]]**: เก็บประวัติงานแบบเป็นกิ่ง (Branching) ช่วยให้สลับบริบทหรือลองผิดลองถูกได้โดยไม่เสีย context หลัก
- **Hot-reloading Extensions**: ผู้ใช้สามารถเขียน tool หรือ UI เสริมด้วย TypeScript และโหลดเข้าสู่ระบบได้ทันทีโดยไม่ต้องปิดโปรแกรม
- **No Hidden Context**: ไม่มีการฉีดข้อมูลหรือเบื้องหลังใดๆ ที่ผู้ใช้มองไม่เห็น (เช่น MCP หรือ sub-agents ที่รันลอยๆ) ทุกอย่างต้องโปร่งใสและตรวจสอบได้
- **Full Cost Tracking**: มีการคำนวณต้นทุน (Token cost) อย่างละเอียดในทุกขั้นตอน
- **Self-modifying Extensions**: pi ship documentation และ example code ให้ agent อ่าน เพื่อให้ agent เขียน extension ของตัวเองได้ เช่น subagent support, plan mode, MCP, custom compaction, custom provider, tool ใหม่, หรือ UI ใหม่

## ปรัชญาการออกแบบ

pi ยึดถือแนวคิด [[malleable-tools]] ซึ่งมองว่าเครื่องมือควรปรับตัวตาม Developer ไม่ใช่ให้ Developer ปรับตัวตามเครื่องมือ ฟีเจอร์ที่ซับซ้อนอื่นๆ (เช่น Web search, Multi-agent) ถูกออกแบบให้สร้างผ่านระบบ Extension แทนที่จะฝังไว้ในตัวโปรแกรมหลัก

ใน [[building-pi-world-of-slop|Building pi in a World of Slop]], Mario ย้ำว่า pi ไม่ได้ต้องชนะด้วย feature list แต่ต้องทำให้ผู้ใช้ "เอา control กลับมา" จาก harness ที่ซ่อน context หรือเปลี่ยน behavior ตาม release โดยผู้ใช้มองไม่เห็น

ใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]], เหตุผลนี้ชัดขึ้นจากมุม workflow: Mario บอกว่า [[claude-code|Claude Code]] เปลี่ยน harness ถี่มาก ทั้ง system prompt, tool definitions, และ hidden reminders. ถ้า workflow ผู้ใช้ผูกกับ prompt template / slash command / skill ของตัวเอง การเปลี่ยนใต้เท้าแบบนี้ทำให้เครื่องมือรู้สึกไม่ stable. pi จึงพยายามเป็น core เล็กที่ผู้ใช้เห็นและแก้ control surface ได้เอง.

## วิธีใช้จริงของ Mario

Mario ไม่ได้ใช้ pi เป็นกองทัพ agent ที่วิ่งเองทั้งหมด. Workflow หลักคือให้ agent อ่าน issue และ source ที่เกี่ยวข้องก่อน แล้วเสนอ analysis กับทางเลือก. จากนั้นเขาเข้า code เอง, reproduce เองเมื่อจำเป็น, ใช้ agent เป็น rubber duck, นิยาม interface/module/test ด้วยตัวเองให้ชัด แล้วค่อยให้ agent implement.

หลัง implement เขา review diff และ annotate line ที่ต้องแก้ผ่าน extension ของ pi. งาน core mechanics จะถูกอ่านละเอียดเหมือน review คนจริง. งาน prototype อาจ vibe code ได้ แต่ถ้าเริ่มมี value เขาจะกลับมา refactor โดยนิยาม boundary เองก่อน.

**ผลคือ:** pi ในมือ Mario ไม่ใช่เครื่องมือแทน judgement. มันเป็นเครื่องมือเร่ง analysis, exploration, และ implementation หลังคนวาง guardrail แล้ว.

## Fork และการทดลอง harness

[[oh-my-pi|oh-my-pi]] ของ [[can-boluk|Can Bölük]] เป็น fork ที่หยิบ pi มาเป็นฐานสำหรับทดลอง harness แบบ model-agnostic — รวม [[hashline|Hashline]] edit tool และ react-edit-benchmark; ดู [[improved-15-llms-harness-changed]]

## ดูเพิ่ม

- [[mario-zechner]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
- [[oh-my-pi]]
- [[can-boluk]]
- [[tree-structured-sessions]]
- [[malleable-tools]]
- [[terminalbench]]
