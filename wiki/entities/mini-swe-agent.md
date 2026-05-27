---
title: mini-swe-agent
type: entity
tags: [ai, agents, harness, benchmarks, coding]
created: 2026-05-27
updated: 2026-05-27
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md]
---

# mini-swe-agent

harness แบบมินิมอลที่ให้ agent ใช้แค่ **bash tool ตัวเดียว** พร้อม system prompt ร่วมกัน [[deepswe|DeepSWE]] ใช้มันรันทุก model เพื่อให้คะแนนสะท้อนความสามารถของตัว model เอง ไม่ใช่ scaffolding รอบตัวมัน (เทียบแนวคิด harness กับ [[agent-harness-engineering]] ที่ว่า Agent = Model + [[harness-engineering|Harness]])

## ข้อดี / ข้อแลก

- **ข้อดี:** แยก model ออกจากผลของ harness ได้สะอาด — ทุกค่ายเล่นบนสนามเดียวกัน
- **ข้อแลก:** ลดความสมจริง เพราะแต่ละค่ายถูกฝึกมากับเครื่องมือคนละแบบ เช่น GPT ถนัด `apply_patch` ส่วน Claude ถนัด `text_editor` การบังคับให้ทุกการแก้ผ่าน bash อย่างเดียวอาจกด model ไว้ต่ำกว่าเพดานจริง
- developer จริงก็ไม่ได้ใช้ผ่าน mini-swe-agent แต่ใช้ผ่าน harness เฉพาะอย่าง [[openai-codex|Codex CLI]], [[claude-code|Claude Code]], Cursor และ Gemini CLI — ตรงนี้คือ trade-off ที่ทีมงาน DeepSWE ยอมรับเอง

## See also

- [[deepswe]]
- [[harness-engineering]]
- [[agent-harness-engineering]]
- [[edit-tool-formats]]
