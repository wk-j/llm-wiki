---
title: ElevenLabs
type: entity
tags: [company, voice, asr, tts, ai]
created: 2026-09-07
updated: 2026-09-07
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md]
---

# ElevenLabs / บริษัท model ด้านเสียง

ElevenLabs เป็นบริษัท AI ด้านเสียง ใน wiki นี้เข้ามาผ่าน [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์ DHH กับ Lex Fridman]] ซึ่ง [[lex-fridman|Lex Fridman]] บอกว่าเขาใช้ ElevenLabs ถอดเสียงพูดเป็นข้อความใน workflow ของตัวเอง

> "I use 11 Labs for transcription. They're probably the best speech to text model."
>
> คำว่า "11 Labs" ใน transcript คือ ElevenLabs และประโยคนี้เป็นความเห็นของผู้พูด ไม่ใช่ผล benchmark

สิ่งที่ควรอ่านคู่กันคือ Lex บอกในประโยคถัดไปเองว่า **ยังมีคำผิดอยู่** เขาจึงต้องมีชั้น LLM ทำความสะอาด transcript ต่อ โดยใช้ dictionary คำเฉพาะและรายการคำที่กวาดมาจาก code base ดู [[voice-first-prompting|Voice-First Prompting]] และ [[keyword-biasing|Keyword Biasing]]

หน้านี้เก็บเฉพาะสิ่งที่คลิปพูดถึง ยังไม่มีข้อมูลเรื่อง model, ราคา, หรือ API ของบริษัทใน wiki

## See also

- [[voice-first-prompting]]
- [[lex-fridman]]
- [[automatic-speech-recognition]]
- [[word-error-rate]]
- [[keyword-biasing]]
