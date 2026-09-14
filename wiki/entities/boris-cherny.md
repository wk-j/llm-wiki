---
title: Boris Cherny
type: entity
tags: [ai, claude-code, anthropic, engineering]
created: 2026-07-04
updated: 2026-09-10
sources: [a-field-guide-to-fable-finding-your-unknowns.md, "Loop Engineering..md", claude-codes-new-intent-md-rob-shocks.md, boris-cherny-cut-80-percent-claude-code-prompt.md]
---

# Boris Cherny / บอริส เชอร์นี

Boris Cherny คือ engineer ที่ [[anthropic|Anthropic]] ผู้สร้าง [[claude-code|Claude Code]] ปรากฏใน wiki นี้ผ่านหลายมุม:

- ใน [[loop-engineering-osmani|Loop Engineering ของ Addy Osmani]] เขาถูกอ้างด้วยประโยค "my job is to write loops" — คนสร้าง Claude Code เองมองงานตัวเองว่าเป็นการออกแบบ loop ที่สั่ง agent ไม่ใช่นั่ง prompt เอง (ดู [[loop-engineering]])
- ใน [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable]] [[thariq-shihipar|Thariq Shihipar]] ยกเขา (คู่กับ Jarred Sumner ผู้สร้าง Bun) เป็นตัวอย่าง agentic coder ระดับท็อป: ดู prompt แล้วรู้เลยว่าเขารู้ว่าตัวเองต้องการอะไรละเอียดแค่ไหน เพราะ in-sync ทั้งกับ codebase และพฤติกรรมของ model — คือคนที่มี [[unknowns-matrix|unknowns]] น้อย แต่ก็ยังเผื่อแผนสำหรับ unknowns เสมอ
- ใน [[claude-codes-new-intent-md-rob-shocks|คลิปของ Rob Shocks]] ภาพของ Boris ถูกใช้เปิดเรื่อง AI-Native SDLC และ Rob บอกว่า playbook มาจากทีมที่รวม Boris อยู่ด้วย แต่หน้า playbook อย่างเป็นทางการลงชื่อ Louis Claxton เป็นผู้เขียนและไม่ได้ลงเครดิต Boris จึงเก็บความเชื่อมโยงนี้เป็นคำบอกเล่าของ Rob ไม่ใช่หลักฐานว่า Boris เขียนเอกสาร
- ใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์กับ Y Combinator]] Boris พูดจากประสบการณ์ตรงของทีม Claude Code ว่าทุก model release ต้องทดสอบ harness ใหม่ ทีมลบ system prompt ของ Opus 5 ออกราว 80% ด้วย prompt ablation แล้วเพิ่มกลับเฉพาะกฎที่แก้ failure ซ้ำ ๆ ได้ เขายังวาง verification เป็นหัวใจของงานยากและอธิบาย dynamic workflows, loops และ routines ที่กระจายงานไปยัง agent จำนวนมาก

Claim เรื่อง Opus 5 ต้าน prompt injection, รันได้เป็นเดือน และ routine ทำงานเทียบเท่าวิศวกรจำนวนมากยังเป็นคำบอกเล่าของ Boris บนเวที ไม่ใช่ benchmark หรือ security proof ที่ wiki ตรวจแยกแล้ว

## See also

- [[claude-code]]
- [[anthropic]]
- [[loop-engineering]]
- [[unknowns-matrix]]
- [[field-guide-to-fable-finding-unknowns]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[ai-driven-sdlc]]
- [[boris-cherny-cut-80-percent-claude-code-prompt]]
- [[claude-opus-5]]
- [[prompt-ablation]]
- [[model-elicitation]]
