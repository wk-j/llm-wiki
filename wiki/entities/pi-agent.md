---
title: pi
type: entity
tags: [product, tool, agents, terminal, typescript]
created: 2026-04-28
updated: 2026-05-03
sources: [mario-zechner-pi-agent.md, building-pi-world-of-slop.md]
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

## ดูเพิ่ม

- [[mario-zechner]]
- [[tree-structured-sessions]]
- [[malleable-tools]]
- [[terminalbench]]
