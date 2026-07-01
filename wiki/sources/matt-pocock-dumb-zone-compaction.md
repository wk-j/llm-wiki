---
title: "Matt Pocock: Dumb Zone, Rewind, and Compaction"
type: source
tags: [ai-coding, context-management, compaction, agents, harness]
url: https://x.com/mattpocockuk/status/2071288332642812229
date_ingested: 2026-06-29
created: 2026-06-29
updated: 2026-06-29
sources: ["Matt Pocock on X - Dumb Zone, Rewind, and Compaction.md"]
---

# Matt Pocock: Dumb Zone, Rewind, and Compaction / Dumb Zone, Rewind, และ Compaction

โพสต์ X ของ [[matt-pocock|Matt Pocock]] (ผู้สอน TypeScript และคนทำ workflow สำหรับ AI coding) เสนอวิธีสั้น ๆ เพื่อให้คน "รู้สึกด้วยตัวเอง" ว่า [[dumb-zone|dumb zone]] ของ coding agent เป็นอย่างไร. แก่นคือ ถ้า agent เริ่มทำเรื่องโง่ใน session ยาว ให้ย้อนก่อนจุดพลาด แล้ว compact ก่อนลองใหม่.

โพสต์นี้ไม่ใช่ benchmark แบบเป็นทางการ. มันเป็น field heuristic สำหรับคนใช้ agent จริง. แต่มีประโยชน์เพราะมันชี้จุดที่หลายคนสับสน: context window ที่ใหญ่ไม่ได้แปลว่า active context ยังสะอาด.

## ข้อความหลัก

Matt เสนอขั้นตอน 4 ข้อ:

1. Agent ทำเรื่องโง่
2. `/rewind` กลับไปก่อนเรื่องโง่นั้น
3. `/compact` ถ้าอยู่ในจุดที่ compact ได้สมเหตุสมผล
4. รันใหม่ แล้วดูว่ามันฉลาดขึ้น

ประโยคสำคัญคือ:

> "Here's a way to get a visceral sense of the dumb zone (starts at ~120K tokens on SOTA models)... Watch it get smarter"

คำว่า **visceral** ในที่นี้หมายถึง "รู้สึกได้แบบชัดกับตัวเอง" ไม่ใช่แค่เข้าใจเป็นทฤษฎี.

## ทำไม pattern นี้ถึงเวิร์ก

ขั้นตอนนี้เวิร์กเพราะมันไม่ได้แค่ "ลองใหม่". มันเปลี่ยนคุณภาพของ context ที่ model เห็น.

พอ agent ทำพลาด transcript จะมีของเสียเพิ่มขึ้น: assumption ผิด, tool output ยาว, error log, การแก้ที่ไปผิดทาง, และคำอธิบายที่พยายามทำให้ทางผิดดูสมเหตุสมผล. ถ้าเราพิมพ์แก้ต่อใน session เดิม model ยังเห็นขยะพวกนี้อยู่.

`/rewind` ตัดกิ่งที่ผิดออกก่อน. จากนั้น `/compact` ย่อกิ่งที่เหลือให้เป็น state สั้น ๆ: อ่านอะไรแล้ว, ตัดสินใจอะไรแล้ว, งานต่อไปคืออะไร. รอบใหม่จึงไม่ได้เก่งขึ้นเพราะมี token มากขึ้น แต่เพราะเห็น **active context ที่สะอาดกว่า**.

ผลคือ: compaction เป็นเครื่องมือจัด hygiene ของ context ไม่ใช่แค่เครื่องมือประหยัด token.

## จุดที่ควร compact

reply หนึ่งสรุปเป็นภาษาสเปนว่า trick ไม่ใช่ "compact ให้มากขึ้น" แต่คือ compact ที่ **phase boundary** เหมือน save game ก่อน boss fight. ถ้า compact กลางทางเดิน agent จะตื่นขึ้นมาพร้อม state ครึ่ง ๆ กลาง ๆ.

จุดที่เหมาะ:

- หลัง research จบ ก่อน implement
- หลัง debug ได้ข้อสรุป ก่อน retry
- หลังตัดสิน architecture แล้ว ก่อนให้ agent แก้จริง
- ก่อนเปิด session ใหม่ด้วย [[agent-handoff-documents|handoff document]]

จุดที่เสี่ยง:

- ระหว่าง debug ที่ยังไม่รู้ว่า signal คืออะไร
- หลัง tool output ยาวมากแต่ยังไม่ได้แยกว่าบรรทัดไหนสำคัญ
- ตอน autocompact บังคับเพราะ context ใกล้เต็มแล้ว

## คำถามจาก replies

### 1M context แล้วยังมี dumb zone ไหม

มีได้. context window คือความจุ ส่วน dumb zone คือคุณภาพการใช้ context ในงานตรงหน้า. งานค้นข้อมูลแบบตรง ๆ อาจทน context ยาวกว่า แต่งาน coding/debugging/design ต้องเลือก signal จาก noise เยอะกว่า จึงเสื่อมก่อนเต็ม window.

ตัวเลข `~120K` ในโพสต์ควรอ่านเป็น heuristic จากประสบการณ์ ไม่ใช่กฎตายตัว. ในวิกิมีตัวเลขอีกชุดจาก [[claude-code-session-management]] ที่พูดถึง context rot แถว 300k-400k สำหรับ 1M context model. ทั้งสองอยู่ในกรอบเดียวกัน: threshold ขึ้นกับ model, harness, และชนิดงาน.

### Automatic compaction ดีขึ้นแล้วไหม

ดีขึ้นได้ โดยเฉพาะถ้า harness ทำ context management เก่งขึ้น. แต่ automatic compaction ยังมีข้อเสีย: มันมักเกิดตอน context ใกล้เต็ม ซึ่งเป็นตอนที่ model กำลังอ่าน context แย่ที่สุดพอดี. Manual compaction ที่ user บอก focus จึงยังมีค่า.

### Rewind ซ่อน bad turn หรือเอาออกจริง

ใน workflow ที่ดี `/rewind` ควรเอา bad turn ออกจาก active context จริง. ถ้าแค่ซ่อนใน UI แต่ model ยังเห็นอยู่ ก็ไม่ได้แก้ dumb zone เต็มที่.

### Durable state ช่วยอย่างไร

บาง reply เสนอ durable orchestrator หรือ tree session. แก่นเดียวกันคือ อย่าให้ transcript เป็นที่เก็บ progress หลัก. ถ้า progress อยู่ใน file, test, issue, memory, handoff, หรือ durable workflow state การฆ่า agent แล้วเริ่มใหม่จะไม่เสียของจริงมาก.

## เชื่อมกับวิกิ

- [[context-rot]] — dumb zone คืออาการเฉพาะของ context rot ใน coding session ยาว
- [[compaction]] — `/compact` เป็นวิธีลดน้ำหนักและสรุป state แต่ต้องทำถูกจังหวะ
- [[agent-handoff-documents]] — ทางเลือกที่มนุษย์เลือกเองว่าอะไรสำคัญ ก่อนส่งต่อ session ใหม่
- [[coding-harness]] — rewind, compaction, memory, และ tool-output policy เป็นงานของ harness
- [[agent-memory-types]] — durable memory ดีกว่า transcript ยาวเมื่ออยากให้ agent เก่งขึ้นข้าม session
- [[orchestration-tax]] — ถ้าใช้หลาย agent เพื่อเลี่ยง context rot แต่ไม่มี review bandwidth ปัญหาจะย้ายไปติดที่คน

## See also

- [[dumb-zone]]
- [[context-rot]]
- [[compaction]]
- [[claude-code-session-management]]
- [[agent-handoff-documents]]
- [[coding-harness]]
- [[matt-pocock]]
