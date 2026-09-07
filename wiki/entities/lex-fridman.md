---
title: Lex Fridman
type: entity
tags: [people, podcast, ai, voice]
created: 2026-09-07
updated: 2026-09-07
sources: [dhh-strategies-programming-with-ai-agents-lex-clips.md, dhh-ai-programming-setup-lex-clips.md]
---

# Lex Fridman / เจ้าของพอดแคสต์ที่คุยกับ DHH

Lex Fridman เป็นผู้ดำเนินรายการพอดแคสต์ Lex Fridman Podcast ซึ่งมีช่องคลิปสั้นชื่อ Lex Clips ใน wiki นี้เขาเข้ามาผ่านบทสัมภาษณ์ [[dhh|DHH]] สองตอน คือ [[dhh-strategies-programming-with-ai-agents-lex-clips|ตอนเรื่องวิธีทำงานกับ agent]] และ [[dhh-ai-programming-setup-lex-clips|ตอนเรื่องชุดเครื่องมือ]]

เขาไม่ได้เป็นแค่คนถาม ในสองตอนนี้เขาเล่า workflow ของตัวเองและแย้ง DHH ในบางเรื่อง จึงบันทึกเป็น entity แยก

## workflow เสียงของเขา

ส่วนที่เป็นเนื้อหาที่สุดคือวิธีป้อนโจทย์ให้ agent ด้วยเสียง เขาใช้ Plaud ซึ่งเป็นอุปกรณ์อัดเสียงติดเสื้อ กดปุ่มแล้วอัด แล้วพูดต่อเนื่องเป็นสิบ ๆ นาที บางครั้งเป็นชั่วโมง โดยปล่อยให้ช่วงที่เปลี่ยนใจกลางทางเรื่อง design อยู่ในเสียงนั้นด้วย

เสียงเข้า pipeline สองชั้น คือถอดเสียงด้วย [[elevenlabs|ElevenLabs]] แล้วให้ LLM ทำความสะอาด transcript โดยมี dictionary คำเฉพาะและ agent ที่กวาด code base มาช่วยให้ชื่อไฟล์กับชื่อ function สะกดถูก เขาบอกว่าจุดแข็งของวิธีนี้คือ prompt ไม่ตีกรอบเกินไป เพราะ agent เห็นทางที่เขาคิดทั้งหมด ดู [[voice-first-prompting|Voice-First Prompting]]

เขายอมรอ 5–10 วินาทีเพื่อให้ pipeline ทำงานเสร็จ และยอมรับว่าวิธีนี้ยังใช้กับการเขียนอีเมลไม่ดีนัก เพราะพลาดคำเล็ก ๆ แล้วต้องกลับไปแก้

## จุดที่เขาแย้ง DHH

- เรื่อง macOS: DHH บอกว่าตั้งค่า Raycast และ key binding บางส่วนต้องผ่าน GUI Lex แย้งว่ามีวิธีอ้อม ส่วน DHH เห็นว่าวิธีที่ลองยังไม่ดีพอ ทั้งสองความเห็นเก็บไว้คู่กันในหน้า source
- เรื่องระบบปฏิบัติการ: เขาใช้ Windows เพราะต้องทำงานกับ Adobe Premiere และเคยใช้ WSL เพื่อรัน Linux ภายใน Windows
- เรื่องเสียง: เขาเชื่อในการพูดยาว ส่วน DHH ชอบพิมพ์และยอมรับว่ายังไม่เคยลองพูดต่อเนื่อง 20 นาที ทั้งสองคนบอกเองว่าเป็น introvert แต่ใช้เสียงต่างกัน

## See also

- [[dhh]]
- [[dhh-strategies-programming-with-ai-agents-lex-clips]]
- [[dhh-ai-programming-setup-lex-clips]]
- [[voice-first-prompting]]
- [[elevenlabs]]
