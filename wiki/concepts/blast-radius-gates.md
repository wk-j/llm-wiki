---
title: Blast-Radius Gates
type: concept
tags: [ai, agents, harness, governance, human-in-the-loop, software-engineering]
created: 2026-09-30
updated: 2026-09-30
sources: [engineering-the-harness-thoughtworks.md, agentic-code-review-osmani.md, what-weve-learned-building-cloud-agents.md, ai-native-sdlc-playbook.md]
---

# Blast-Radius Gates / ด่านให้คนตัดสินเฉพาะเรื่องที่ลามไกล

**Blast-radius gate** คือจุดที่ harness หยุด agent แล้วขอให้คนยืนยัน เฉพาะตอนที่การตัดสินใจนั้นย้อนไม่ได้หรือกระทบวงกว้าง เรื่องอื่นปล่อยให้ agent เดินต่อด้วย default ที่ประกาศไว้ ชื่อนี้ wiki ตั้งเองจากสองหัวข้อใน [[engineering-the-harness-thoughtworks|บทความของ Thoughtworks]] คือ "selective human gates" กับ "Confirmation only for high-blast-radius decisions" (blast radius = วงของความเสียหายถ้าพลาด)

## ทำไมไม่ถามทุกเรื่อง

ส่วนนี้ตอบว่าทำไมต้องเลือกจุดถาม ถ้าให้คนกดอนุมัติทุก tool call คนจะล้า แล้วเริ่มกดผ่านโดยไม่อ่าน ถ้าไม่ถามเลย agent ก็ทำเรื่องใหญ่ไปเองโดยไม่มีใครรู้

Thoughtworks เลยวางด่านคนเป็นชั้นที่สาม คั่นระหว่าง guides (ตัวคุมก่อนลงมือ) กับ sensors (ตัวตรวจหลังลงมือ) ของ [[harness-guides-sensors]] เรื่องที่บทความยกว่าควรหยุดถาม:

- ขยาย scope ข้ามหลาย repository
- schema migration
- แก้ public API

เรื่องเสี่ยงต่ำให้เดินต่อด้วย default ที่สมเหตุสมผล

**ได้อะไร:** attention ของคนไปอยู่กับการตัดสินใจที่พลาดแล้วแก้ยาก ไม่หมดไปกับการกดยืนยันเรื่องเล็ก

## ด่านต้องรู้ก่อนว่าเรื่องนี้ใหญ่

ด่านจะลั่นได้ harness ต้องรู้ก่อนว่าผลกระทบไปถึงไหน ในตัวอย่างสาม microservice ของ Thoughtworks agent สแกน dependency graph ก่อน เจอว่า rename `discount_rate` ใน billing กระทบ checkout กับ invoicing แล้ว harness ถึงหยุดรอคน ถ้าไม่มีขั้นนี้ agent จะแก้ repo เดียว test ใน repo ผ่าน แล้วรายงานว่าเสร็จ

[[code-knowledge-graphs|Code knowledge graph]] (graph ของโค้ดที่ให้ agent ถามได้ว่าใครเรียกใช้อะไร) คือเครื่องมือที่ป้อนข้อมูลให้ด่านแบบนี้

ข้อจำกัดคือ ด่านเห็นได้แค่ dependency ที่อยู่ใน graph ถ้า consumer อยู่นอก workspace ด่านก็เงียบ แล้วความเงียบนั้นดูเหมือน "ไม่มีผลกระทบ"

**ผลคือ:** ด่านดีได้แค่เท่ากับ impact analysis ที่ป้อนมันอยู่ กฎว่า "เรื่องใหญ่ต้องถาม" อย่างเดียวไม่พอ

## คู่กับ explicit default

Gate คุมเรื่องใหญ่ ส่วนเรื่องที่เหลือต้องมี default ที่มองเห็นได้ Thoughtworks ให้ harness "ask before deciding" ตอนเจอ input ที่ไม่บังคับ ถ้า developer เลือกข้าม harness ก็บันทึกไว้ว่าข้าม

> "A default is visible and inspectable, a guess is hidden and risky."

สองอย่างนี้ทำงานด้วยกัน เรื่องใหญ่หยุดรอคน เรื่องเล็กเดินต่อ แต่ทุกทางเลือกถูกบันทึกให้ย้อนดูได้

## ญาติของ review tier และ hook แบบ ask

แนวคิดนี้ใกล้กับ [[agentic-code-review]] ที่ [[addy-osmani|Addy Osmani]] ให้แบ่ง tier ของ review ตาม blast radius (bug กระทบใคร: ไม่มีใคร ผู้ใช้จริง เงิน privacy หรือ security) ต่างกันที่จังหวะ review tier ตรวจหลังโค้ดเขียนเสร็จ ส่วน blast-radius gate ขวางไว้ก่อน agent ลงมือทำเรื่องใหญ่

ใน [[policy-as-code-for-agents]] hook ที่ตอบ `ask` ได้ ก็คือกลไกเดียวกันในระดับ tool call ส่วน [[graduated-autonomy]] เป็นการเลื่อนเส้นของด่านพวกนี้ตามระดับความไว้ใจที่ agent ได้มา (อันหลังนี้ wiki โยงเอง แหล่งไม่ได้พูดถึงกัน)

**ได้อะไร:** ถามเรื่องเดียวกันได้สามจังหวะ ก่อนลงมือ (gate) ตอนเรียก tool (hook) และหลังเขียนเสร็จ (review tier) ทีมควรเลือกจังหวะที่จับได้ถูกที่สุด ไม่ใช่ใส่ทุกจังหวะ

## เรื่องที่ยังไม่ลงรอย: หยุดรอคน หรือปล่อยให้ agent ตัดสิน

[[cursor|Cursor]] เล่าใน [[what-weve-learned-building-cloud-agents]] ว่าย้าย logic multi-repo ออกจาก harness แล้ว แค่บอก repo layout กับเปิด tool สำหรับ branch และ PR ให้ agent ตัดสินเอง และเตือนว่า cloud agent ที่รอ permission อาจนั่งรอเป็นชั่วโมงกว่าคนจะกลับมาดู ([[orchestration-tax]])

Thoughtworks กลับใส่ blocking gate ไว้ใน harness ตอนผลกระทบข้าม repo

สองแหล่งอาจถูกคนละบริบท Cursor ห่วงต้นทุนของการหยุด (agent ว่างงาน คนเป็นคอขวด) ส่วน Thoughtworks ห่วงต้นทุนของการพลาด (production พังเงียบ ๆ ข้าม service) ไม่มีแหล่งไหนวัดเทียบกัน wiki เลยยังไม่ตัดสินว่าฝั่งไหนเป็นค่าเริ่มที่ดีกว่า

ทางกลางที่พอคิดได้ (wiki สังเคราะห์เอง ไม่ใช่ข้อเสนอของแหล่ง): ให้ agent เตรียม branch หรือ PR ข้าม repo ได้เอง แต่ย้ายด่านไปไว้ตอน merge หรือ deploy แทนการหยุดก่อนเริ่มงาน

## จุดที่ควรระวัง

- **ด่านเยอะไปก็กลับไปกดผ่าน** ถ้าทุกเรื่องถูกนับว่า high-blast-radius คนจะล้าแบบเดิม
- **ด่านไม่ได้แทน sensor** คนอนุมัติ scope แล้ว ก็ยังต้องรัน test ข้าม service เพื่อตรวจว่าแก้ครบจริง Thoughtworks เองก็รัน multi-service test suite หลังอนุมัติ
- **คนที่กดต้องเข้าใจสิ่งที่อนุมัติ** ถ้าไม่มีใครอ่าน plan ก่อนกด ด่านก็เหลือแค่ปุ่ม Enter แบบใน [[teepagorn-claude-code-adoption-nobody-reading|เคส voxium]] ดู [[comprehension-debt]]

## See also

- [[engineering-the-harness-thoughtworks]]
- [[harness-guides-sensors]]
- [[code-knowledge-graphs]]
- [[agentic-code-review]]
- [[policy-as-code-for-agents]]
- [[graduated-autonomy]]
- [[orchestration-tax]]
- [[what-weve-learned-building-cloud-agents]]
- [[comprehension-debt]]
- [[thoughtworks]]
