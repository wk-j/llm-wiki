---
title: Liquidation Discovery
type: concept
tags: [finance, markets, leverage, liquidation, liquidity]
created: 2026-07-30
updated: 2026-07-30
sources: [jrt-desk-kospi-liquidation-discovery.md]
---

# Liquidation Discovery / ราคาที่ค้นพบผ่านการบังคับขาย

Liquidation discovery คือช่วงที่ราคาตลาดถูกกำหนดโดยคนที่ “ต้องขายตอนนี้” มากกว่าคนที่กำลังถกกันว่าสินทรัพย์ควรมีมูลค่าเท่าไร

คำนี้มาจาก [[jrt-desk-kospi-liquidation-discovery|บทวิเคราะห์ KOSPI ของ JRT Desk]] ใช้อธิบายวันที่ margin call, forced liquidation และการปรับ hedge ของ leveraged ETF ทำงานพร้อมกัน

## ต่างจาก price discovery ปกติอย่างไร

Price discovery ปกติคือผู้ซื้อกับผู้ขายเอาข้อมูล ความคาดหวัง และ valuation มาแลกกัน แต่ละฝ่ายเลือกเวลาและราคาได้พอสมควร

Liquidation discovery มี deadline เข้ามาบังคับ:

| คำถาม | Price discovery ปกติ | Liquidation discovery |
|---|---|---|
| ใครตั้งราคา | ผู้ซื้อและผู้ขายที่เลือกเทรด | ฝั่งที่ต้องปิดหรือลด position |
| เวลา | รอได้ถ้ายังไม่พอใจราคา | ต้องทำตามเกณฑ์ภายในวันนี้หรือช่วง rebalance |
| เหตุผล | มุมมองต่อมูลค่าและอนาคต | หลักประกัน, mandate, risk limit หรือสัญญา |
| ฝั่งตรงข้าม | อาจพร้อมรับของ | รอราคาที่ต่ำกว่าได้ |

จุดชี้ขาดคือความไม่สมมาตรของเวลา Forced seller ต้องขายวันนี้ แต่ value buyer รอพรุ่งนี้ได้ ราคาเลยอาจหลุดจากการถกเรื่องมูลค่าพื้นฐานชั่วคราว

## วงจรที่ทำให้แรงขายขยายตัว

วงจรพื้นฐานมีสี่ชั้น:

1. ราคาลงจนชน collateral หรือ risk threshold
2. Broker, fund หรือระบบ hedge ส่งคำสั่งขาย
3. คำสั่งขายกดราคาให้ลงต่อ
4. Position ชุดถัดไปชน threshold แล้วเริ่มรอบใหม่

แต่ละคนอาจทำถูกตามหน้าที่ Broker ป้องกันหนี้ กองทุนรักษา leverage ตาม prospectus และผู้ลงทุนลดความเสี่ยงก่อนโดนบังคับ พอทุกคนทำพร้อมกัน การกระทำที่สมเหตุสมผลเฉพาะจุดกลับทำให้ทั้งระบบไม่เสถียร

ผลคือ ความเสี่ยงไม่ได้อยู่แค่ที่ “ใครคิดผิด” แต่อยู่ที่กติกาหลายชุดสั่งให้ทุกคนทำทางเดียวกันในเวลาเดียวกัน

## วิธีตรวจว่าตลาดกำลังเจอกลไกนี้หรือไม่

อย่าเริ่มจากกราฟอย่างเดียว ให้ทำ forced-flow map:

1. **Actor:** ใครมีโอกาสถูกบังคับให้เทรด เช่น บัญชี margin, leveraged fund, option dealer หรือ risk desk
2. **Trigger:** ราคา, collateral ratio, volatility, VaR หรือเวลาปิดตลาดข้อไหนเป็นตัวสั่ง
3. **Deadline:** ต้องปรับทันที สิ้นวัน หรือภายในหลายวัน
4. **Direction:** ราคาลงแล้ว actor ต้องซื้อหรือขาย
5. **Size:** Flow โดยประมาณเทียบกับ average daily volume (ADV) และ order-book depth
6. **Counterflow:** มี short covering, buyback, pension fund หรือ value buyer ที่ต้องซื้อหรือไม่
7. **Clustering:** หลาย position ใช้ threshold และสินทรัพย์ต้นทางเดียวกันหรือเปล่า

คำว่า “forced” ต้องมีหลักฐานจากกติกาหรือข้อจำกัด ไม่ควรใช้แทนคำว่า panic selling ทุกครั้งที่ตลาดลง

## Fundamental thesis อาจถูก แต่ position ยังพังได้

กำไรบริษัทที่ดีไม่ได้หยุด forced flow ทันที เพราะคนที่ถูกบังคับขายไม่ได้กำลังโหวตเรื่องมูลค่าระยะยาว เขากำลังทำตามสัญญา

ดังนั้นการวิเคราะห์หนึ่ง position ต้องแยกสองเรื่อง:

- **Idea half-life:** เหตุผลพื้นฐานจะใช้เวลานานแค่ไหนกว่าจะพิสูจน์ตัวเอง
- **Structure half-life:** เงินทุน หลักประกัน และผลิตภัณฑ์ที่ใช้ถือจะทนความผันผวนได้นานแค่ไหน

ถ้าโครงสร้างอยู่ได้สั้นกว่า idea การวิเคราะห์ถูกก็ยังขาดทุนหรือถูกปิด position ก่อน

ผลคือ “ซื้ออะไร” กับ “ถือผ่านโครงสร้างแบบไหน” เป็นการตัดสินใจคนละชั้น และต้องถูกทั้งคู่

## ข้อจำกัด

แนวคิดนี้เป็นกรอบหา mechanism ไม่ใช่คำอธิบายสำเร็จรูป การเห็นราคาลงแรงกับ leverage สูงยังไม่พิสูจน์ว่า forced flow เป็นสาเหตุหลัก ต้องตรวจข้อมูล liquidation, fund flow, hedge exposure, short covering และสภาพคล่องจริงก่อน

## See also

- [[jrt-desk-kospi-liquidation-discovery]]
- [[implicit-government-put]]

