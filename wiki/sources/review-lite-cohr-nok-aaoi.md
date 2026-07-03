---
title: Review LITE COHR NOK AAOI
type: source
tags: [investing, ai, photonics, data-center, semiconductors]
url: "https://www.youtube.com/watch?v=wCra8al221Q"
author: "คุณพ่อนักลงทุน"
created: 2026-07-03
updated: 2026-07-03
sources: [review-lite-cohr-nok-aaoi.md]
---

# Review LITE COHR NOK AAOI / รีวิว LITE COHR NOK AAOI

วิดีโอของ [[khunpho-naklongthun|คุณพ่อนักลงทุน]] (ช่อง YouTube สายลงทุนไทย) เปรียบเทียบหุ้น [[lumentum|Lumentum]] (`LITE`), [[coherent|Coherent]] (`COHR`), [[nokia|Nokia]] (`NOK`), และ [[aaoi|AAOI]] ในธีม [[photonic-interconnects|photonic interconnects]] หรือการส่งข้อมูลใน data center ผ่านแสง

แก่นของคลิปคือคำถามว่า ถ้า AI data center ต้องการส่งข้อมูลระหว่าง GPU, memory, switch, และ server เร็วขึ้นเรื่อย ๆ ใครได้ประโยชน์จริงจากคอขวดนี้ และใครยังเป็นแค่เรื่องเล่าที่ยังต้องพิสูจน์

## สรุปสั้น

- คลิปวาง [[photonic-interconnects|photonics]] เป็นคอขวดถัดจาก GPU, memory, และ CPU ใน [[ai-data-center-bottlenecks|AI data center bottlenecks]] แต่ผู้พูดยังไม่เชื่อเต็มที่ว่า photonics จะทำ margin ได้ดีเท่ากลุ่ม memory
- ห่วงโซ่ของ photonics ในคลิปเริ่มจากวัตถุดิบและ [[indium-phosphide-wafer|Indium Phosphide wafer]] ไปจนถึง laser, DSP, optical module, switch, และ data center
- คอขวดสำคัญตามคลิปคือการผลิต wafer ขนาด 6 นิ้ว เพราะช่วยเพิ่ม yield / ลดต้นทุน แต่ต้องใช้เครื่องจักร การ qualify กับลูกค้า และเวลา ramp production
- [[coherent|Coherent]] ถูกวางเป็นผู้นำตอนนี้ เพราะมี vertical integration กว้างกว่าและคลิปอ้างว่าส่งมอบ transceiver จาก 6-inch wafer แล้ว
- [[lumentum|Lumentum]] โตเร็วและ margin ดีในตัวเลขไตรมาสล่าสุดที่คลิปยกมา แต่ยังมีความเสี่ยงเรื่อง ramp โรงงาน 6-inch wafer ซึ่งผู้พูดมองว่าอาจช้าถึงปี 2028
- [[aaoi|AAOI]] เป็น high-risk/high-return ตามกรอบของคลิป เพราะเล็กกว่า ใช้เทคโนโลยี MBE ของตัวเอง และตั้งเป้ารายได้สูงมาก แต่ยังต้องพิสูจน์ว่าสเกลได้จริง
- [[nokia|Nokia]] มีฐานบริษัทใหญ่และกระแสเงินสดดีกว่า แต่ photonics เป็นแค่ส่วนหนึ่งของธุรกิจ และแผนเทคโนโลยีใหม่/โรงงานใน San Jose ยังมีความเสี่ยงเรื่องเวลา
- [[axt|AXT]] ถูกพูดถึงท้ายคลิปในฐานะผู้ผลิต substrate รายสำคัญที่น่าสนใจถ้า data center photonics โตจริง แต่มีความเสี่ยงจากการผลิต/ส่งออกจากจีน

## ห่วงโซ่การผลิต photonics

คลิปอธิบาย photonics แบบไล่ตั้งแต่ต้นน้ำถึงปลายน้ำ เพื่อไม่ให้ดูหุ้นจากชื่อธีมอย่างเดียว

ลำดับที่ผู้พูดเล่ามีประมาณนี้:

1. ผลิต substrate / wafer เช่น [[indium-phosphide-wafer|Indium Phosphide wafer]]
2. ปลูกชั้นวัสดุระดับนาโนเมตรบน wafer เพื่อให้เกิดคุณสมบัติทางแสง
3. แกะลายและกัดวงจรในโรงงานเฉพาะทาง เช่น Tower Semiconductor หรือ GlobalFoundries ตามคำกล่าวในคลิป
4. ตัด wafer เป็น die และทดสอบแต่ละชิ้น เพื่อลดของเสีย
5. ประกอบ laser เข้ากับเส้นใยแก้วนำแสง
6. รวม laser, DSP, และส่วนแปลงสัญญาณเป็น [[optical-transceivers|optical transceiver]] / module ความเร็ว 800G ถึง 1.6T
7. ติดตั้ง module เข้ากับ switch / OCS / network equipment ใน data center

**ได้อะไร:** บริษัทที่อยู่แค่ปลายน้ำอาจได้รายได้เร็ว แต่บริษัทที่คุมต้นน้ำด้วยอาจคุมต้นทุนและ margin ได้ดีกว่าเมื่อวัตถุดิบขาด

## คอขวด 6-inch Indium Phosphide wafer

[[indium-phosphide-wafer|Indium Phosphide wafer]] คือจุดที่คลิปให้ความสำคัญที่สุด เพราะมันเป็นฐานให้ laser / photonic device ส่งข้อมูลด้วยแสงได้

ผู้พูดบอกว่า 70% ของแร่หรือ supply ที่เกี่ยวข้องมาจากจีน และ [[axt|AXT]] กับ Sumitomo คุมตลาด substrate ราว 80% ตามคำกล่าวในคลิป เมื่อจีนคุมการส่งออกมากขึ้น ราคา wafer ต่อแผ่นจึงถูกเล่าว่าขึ้นจากประมาณ 1,700 ดอลลาร์เป็นประมาณ 5,000 ดอลลาร์

คลิปเปรียบเรื่องนี้กับ DRAM ใน memory cycle: ถ้าของขาดและราคาขึ้น บริษัทที่มี stock / capacity / ลูกค้าพร้อม อาจขายของแพงขึ้นและ margin ดีขึ้น แต่ถ้าต้องซื้อวัตถุดิบจากข้างนอก ต้นทุนก็พุ่งเหมือนกัน

ผู้พูดแบ่งความพร้อมของการผลิต 6-inch wafer เป็น 3 ขั้น:

1. มีเครื่องจักรและลงทุนจริง
2. เครื่องจักรผ่านการ qualify ปรับ yield และผ่านการรับรองจากลูกค้า ใช้เวลาประมาณ 18-24 เดือนตามคลิป
3. เข้า volume production ส่งของจำนวนมากได้จริง และ margin ดีขึ้นจริง

**ผลคือ:** ข่าวซื้อเครื่องหรือประกาศแผนยังไม่เท่ากับรายได้จริง ต้องดูว่าบริษัทผ่าน qualify และส่งของให้ลูกค้าได้หรือยัง

## เปรียบเทียบบริษัทตามคลิป

| บริษัท | บทบาทในเรื่องเล่า | จุดแข็งตามคลิป | ความเสี่ยง / open question |
|---|---|---|---|
| [[coherent\|Coherent]] | ผู้นำปัจจุบันใน 6-inch wafer / transceiver | vertical integration กว้าง, มีโรงงานในสหรัฐฯ/ยุโรป, คลิปอ้างว่าส่งมอบ 6-inch transceiver แล้ว, ได้เงินลงทุน/ความไว้วางใจจาก [[nvidia\|NVIDIA]] | ภาพรวมรายได้โตช้ากว่า Lumentum เพราะ segment อื่นถ่วง, FCF margin ติดลบตามตัวเลขในคลิป |
| [[lumentum\|Lumentum]] | pure play ใน photonics มากกว่า | รายได้และ margin โตเร็วในไตรมาสล่าสุดที่คลิปยกมา, net margin / operating margin ดูดีขึ้น | ramp 6-inch wafer อาจช้าถึงปี 2028; ต้องดูว่าสินค้าอื่นพยุงการโตได้ไหมระหว่างรอ capacity |
| [[aaoi\|AAOI]] | ตัวเล็ก high-risk/high-return | backlog และเป้ารายได้สูง, ใช้เทคโนโลยี MBE ของตัวเอง | MBE อาจทนร้อนดีแต่ scale 6-inch volume ยากกว่า; ต้องพิสูจน์ว่าจะส่งมอบทันและทำรายได้ตามเป้าได้จริง |
| [[nokia\|Nokia]] | บริษัทใหญ่ที่มีแผน photonic + network stack | ฐานรายได้ใหญ่, FCF ดี, ถ้าผูก DSP / photonics สำเร็จอาจลดพลังงานได้มากตามคลิป | photonics เป็นแค่ส่วนหนึ่งของธุรกิจ, operating margin ต่ำในไตรมาสล่าสุดที่คลิปยกมา, โรงงาน San Jose / timeline 2027 ยังเป็นความเสี่ยง |
| [[axt\|AXT]] | upstream substrate supplier | หนึ่งในผู้เล่น substrate ที่สำคัญต่อ Indium Phosphide | ผลิตในจีนมาก จึงเจอความเสี่ยงจาก export control / ใบอนุญาต |

## มุมการเงินและกรอบลงทุน

ผู้พูดไม่ได้สรุปว่า “หุ้นเดียวชนะทุกอย่าง” แต่แยกสไตล์การลงทุน:

- ถ้าต้องการบริษัทที่รับเงินจริงและมีโรงงานส่งของแล้ว คลิปให้ [[coherent|Coherent]] เด่นสุด
- ถ้าต้องการ pure-play photonics ที่รายได้/margin โตเร็ว คลิปมอง [[lumentum|Lumentum]] น่าสนใจ แม้ capacity ยังต้องรอ
- ถ้าต้องการความเสี่ยงสูงและ upside สูง คลิปวาง [[aaoi|AAOI]] เป็นตัวเลือก แต่ต้องดูการสเกล MBE / 6-inch wafer
- ถ้าต้องการ play ที่ปลอดภัยกว่าและบริษัทใหญ่กว่า คลิปมอง [[nokia|Nokia]] มีฐานดี แต่ไม่ใช่ photonics pure play
- ถ้าต้องการต้นน้ำจริง ๆ คลิปชี้ไปที่ [[axt|AXT]] แต่ความเสี่ยงจีน/ส่งออกต้องชัดก่อน

**ได้อะไร:** theme เดียวกันไม่ได้แปลว่าหุ้นทุกตัวเหมือนกัน ต้องแยกว่าอยากได้ผู้นำที่ส่งของแล้ว, pure play ที่ margin เร่ง, ตัวเล็ก high risk, บริษัทใหญ่ defensive, หรือต้นน้ำ substrate

## ข้อควรระวัง

- Transcript เป็น auto-caption และมีคำเพี้ยนเยอะ เช่นชื่อบริษัท, คำว่า photonics, Indium Phosphide, MOCVD/MBE, transceiver, margin และตัวเลขบางช่วง จึงควรตรวจแหล่งงบ/เอกสารบริษัทก่อนใช้เป็นข้อมูลลงทุน
- ตัวเลขรายได้, margin, backlog, capex, timeline, ราคา wafer, และเงินลงทุนจาก NVIDIA ในหน้านี้เป็น **คำกล่าวจากคลิป** ไม่ใช่การยืนยันจาก filing
- คลิปเป็น investment commentary ไม่ใช่ primary source จากบริษัท และไม่ใช่คำแนะนำลงทุนของ wiki
- ความขัดแย้งสำคัญที่ควรเปิดไว้: ผู้พูดบอก photonics เป็นคอขวด AI data center แต่ก็ย้ำว่ากำไรของ photonics ในอดีตต่ำกว่า memory มาก ดังนั้น “คอขวด” ยังไม่เท่ากับ “ธุรกิจทำกำไรสูง” เสมอไป

## See also

- [[photonic-interconnects]]
- [[indium-phosphide-wafer]]
- [[optical-transceivers]]
- [[ai-data-center-bottlenecks]]
- [[coherent]]
- [[lumentum]]
- [[aaoi]]
- [[nokia]]
- [[axt]]
- [[nvidia]]
