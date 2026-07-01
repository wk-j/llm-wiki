---
title: OpenSuperWhisper
type: entity
tags: [speech-to-text, ai, developer-tools, voice-input]
created: 2026-07-01
updated: 2026-07-01
sources: [l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# OpenSuperWhisper

**OpenSuperWhisper** คือ open-source macOS app สำหรับ speech-to-text ที่รัน Whisper local. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow ของ Kun Chen]] มันคือเครื่องมือหลักในการ prompt agent ด้วยเสียงแทน typing.

Kun ใช้เสียงเพราะ prompt ที่อธิบาย intent ยาว ๆ พูดได้เร็วกว่าพิมพ์มาก. เขายังใช้ initial prompt ของ transcription model เพื่อใส่คำศัพท์เฉพาะ เช่นชื่อ project และ tool ทำให้ระบบถอดเสียงรู้จักคำที่ใช้ประจำ. ข้อยกเว้นคือ URL และ filepath ยังควรพิมพ์เอง.

## See also

- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[agent-experience]]
- [[developer-balance]]
