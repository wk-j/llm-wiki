---
title: Artificial General Intelligence
type: concept
tags: [ai, agi, intelligence, safety, society]
created: 2026-07-15
updated: 2026-07-15
sources: [framework-frontier-ai-dawning-new-age.md]
---

# Artificial General Intelligence / ปัญญาประดิษฐ์ทั่วไป

Artificial General Intelligence หรือ **AGI** คือแนวคิดของ AI ที่ไม่ได้เก่งเฉพาะงานเดียว แต่มีความสามารถทางความคิดกว้างพอจะทำสิ่งที่มนุษย์ทำได้หลายชนิด ใน [[framework-frontier-ai-dawning-new-age|บทความของ Demis Hassabis]] นิยามแรงกว่านั้น: ระบบที่มี “ความสามารถทางความคิดทุกอย่างที่สมองมี”

นิยามนี้ยังไม่ใช่เกณฑ์วัดที่วงการตกลงร่วมกัน คำว่า “ทุกอย่าง” อาจรวม reasoning, learning, planning, creativity, social understanding, embodiment หรือความสามารถอื่นที่ benchmark ปัจจุบันยังแยกไม่ออก

## เส้นเวลาคือ forecast ไม่ใช่ fact

[[demis-hassabis|Demis Hassabis]] คาดว่า AGI อาจเหลือเวลาอีกไม่กี่ปี และเรียกยุคนี้ว่าเชิงเขาของ singularity แต่เขาก็เขียนในบทความเดียวกันว่าไม่มีใครรู้แน่ว่าจะเกิดอะไรและผู้เชี่ยวชาญเห็นต่าง

สองประโยคนี้ต้องอยู่ด้วยกัน: ผู้เขียนเชื่อว่าใกล้มาก แต่ยอมรับ uncertainty สูง. Wiki จึงไม่แปลง forecast ให้เป็นวันนับถอยหลัง

**ได้อะไร:** เวลาพูด “AGI ใกล้แล้ว” ต้องระบุว่าใครคาด จากนิยามอะไร และมีหลักฐานแบบไหน

## ทำไม AGI ต่างจาก frontier model

Frontier model คือ model ที่อยู่แนวหน้าของ capability ณ เวลาหนึ่ง และอาจแตะ threshold ความเสี่ยงบางด้านได้ โดยไม่ต้องเป็น AGI. [[frontier-ai-standards-body|ข้อเสนอ Standards Body]] จึงไม่รอให้พิสูจน์ AGI ก่อน แต่กำกับ model ที่ cyber, bio หรือ agentic capability สูงพอจะสร้างความเสียหายแล้ว

AGI เป็น claim เกี่ยวกับความกว้างของ intelligence ส่วน Frontier-class เป็นสถานะเชิงปฏิบัติสำหรับการ test และ governance. Model อาจเป็น frontier โดยยังขาดความสามารถมนุษย์อีกหลายด้าน

**ผลคือ:** นโยบายความเสี่ยงไม่ควรผูกกับคำถามเดียวว่า “นี่คือ AGI หรือยัง” เพราะ capability อันตรายบางอย่างมาก่อน AGI ได้

## วิสัยทัศน์ด้านประโยชน์

Hassabis มอง AGI เป็นเครื่องมือเร่ง science และ medicine ช่วยค้นยา พลังงานสะอาด วัสดุใหม่ productivity และ economic growth. เขาคาดไกลถึง post-scarcity ซึ่งทรัพยากรไม่ใช่ข้อจำกัดหลักของความก้าวหน้า

ตัวเลข “10 เท่าของ Industrial Revolution ที่เร็ว 10 เท่า” เป็นภาพเปรียบเทียบของผู้เขียน ไม่ใช่ projection ที่มี model เศรษฐศาสตร์รองรับใน source นี้. และแม้ผลิตของได้มากขึ้น การกระจายทรัพย์สิน อำนาจ และ access อาจยังสร้าง scarcity ทางสังคมได้

## ความเสี่ยงและโจทย์ควบคุม

AGI หรือระบบที่เข้าใกล้มันอาจเพิ่มทั้ง defensive และ offensive cyber capability. ด้าน bio/nuclear อาจตามมา. ถ้า agent ทำงานเองและ recursively self-improve ได้ ความเสี่ยงไม่ได้อยู่แค่คำตอบหนึ่งครั้ง แต่อยู่ที่ระบบซึ่งสร้าง experiment, tool use หรือ model รุ่นถัดไปเป็นลูป

ตรงนี้เชื่อม [[model-cyber-capability-emergence|ความสามารถ cyber ที่โผล่จาก intelligence ทั่วไป]], [[self-learning-agents|สามชั้นของ self-improvement]] และ [[agent-runtime-untrusted|การคุม runtime ด้วยโครงสร้าง]].

**ผลคือ:** ยิ่งระบบทั่วไปและมี agency มาก safety ต้องย้ายจาก prompt ไปอยู่ที่ evaluation, permission, containment และ governance

## หลังโจทย์เทคนิค

ต่อให้ control model ได้ สังคมยังต้องตอบว่าเศรษฐกิจ post-scarcity หน้าตาอย่างไร คนเข้าถึงประโยชน์เท่าเทียมไหม และ meaning/purpose ของมนุษย์เปลี่ยนอย่างไร Hassabis ย้ำว่า technologist ตัดสินเรื่องนี้ฝ่ายเดียวไม่ได้

## Open questions

- benchmark ชุดไหนพิสูจน์ “ทุกความสามารถของสมอง” ได้โดยไม่ลด AGI เหลือคะแนนข้อสอบ
- intelligence ทั่วไปต้องมี embodiment, memory ระยะยาว หรือ social understanding แค่ไหน
- recursive self-improvement เป็นเงื่อนไขของ AGI หรือเป็น capability แยกที่อาจมาก่อน
- ใครได้ประโยชน์จาก productivity/abundance และใครถืออำนาจเหนือ compute กับ model
- governance ควรใช้ capability threshold ใดก่อนที่นิยาม AGI จะตกลงกันได้

## See also

- [[framework-frontier-ai-dawning-new-age]]
- [[demis-hassabis]]
- [[frontier-ai-standards-body]]
- [[self-learning-agents]]
- [[model-cyber-capability-emergence]]
- [[agent-runtime-untrusted]]
