---
title: VoxType
type: entity
tags: [voice, asr, open-source, linux, developer-tools]
created: 2026-09-07
updated: 2026-09-07
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md]
---

# VoxType / เครื่องมือถอดเสียงเป็นข้อความใน Omarchy

VoxType เป็นเครื่องมือ dictation หรือถอดเสียงพูดเป็นข้อความ ที่ [[dhh|DHH]] บอกว่าเป็น open source และเตรียมไว้ให้ใช้ใน [[omarchy|Omarchy]] ข้อมูลในหน้านี้มาจาก [[dhh-strategies-programming-with-ai-agents-lex-clips|บทสัมภาษณ์กับ Lex Fridman]] เท่านั้น ยังไม่ได้ตรวจกับเอกสารของโครงการ

## สิ่งที่คลิปบอก

- ใช้ open model ตัวหนึ่งอยู่ข้างใน ผู้พูดจำชื่อไม่แน่ บอกว่าเป็น "Parrot model or something like that" หน้านี้จึงไม่บันทึกชื่อ model เป็นข้อเท็จจริง
- วิธีใช้คือกดค้าง F9 แล้วเริ่มพูด
- ทำงานได้ดีกับคำสั่งสั้น ๆ ซึ่งเป็นแบบที่ DHH ใช้จริง
- package **ไม่ได้ลงมาให้ในเครื่องตั้งแต่แรก** เพราะข้างในมี model ขนาดราว 150 MB ซึ่งเขาไม่อยากแบกไว้บน ISO แต่เตรียมทางให้ระบบเสนอติดตั้งเมื่อออนไลน์แล้ว

การตัดสินใจข้อสุดท้ายเป็นตัวอย่างที่ดีของ [[omakase-software|omakase software]] ที่ยังสนใจขนาด คือของที่คนส่วนใหญ่ได้ใช้ก็ลงมาให้ ของที่หนักและใช้เฉพาะกลุ่มก็ทำเป็นตัวเลือก

## ที่ต่างจาก workflow ของ Lex

VoxType ถูกใช้เป็น dictation สั่งงานสั้น ๆ ไม่ใช่ pipeline พูดยาวแบบที่ [[lex-fridman|Lex Fridman]] ใช้ ซึ่งมีชั้นทำความสะอาด transcript ต่อจากการถอดเสียง ความต่างนี้อธิบายไว้ใน [[voice-first-prompting|Voice-First Prompting]]

## See also

- [[omarchy]]
- [[dhh]]
- [[voice-first-prompting]]
- [[automatic-speech-recognition]]
- [[open-superwhisper]]
