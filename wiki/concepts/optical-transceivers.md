---
title: Optical Transceivers
type: concept
tags: [photonics, networking, data-center, semiconductors]
created: 2026-07-03
updated: 2026-07-03
sources: [review-lite-cohr-nok-aaoi.md]
---

# Optical Transceivers / โมดูลรับส่งข้อมูลด้วยแสง

Optical transceiver คือ module ที่แปลงสัญญาณไฟฟ้าเป็นแสงและแสงกลับเป็นไฟฟ้า เพื่อส่งข้อมูลผ่าน fiber ใน network. ในวิดีโอ [[review-lite-cohr-nok-aaoi|Review LITE COHR NOK AAOI]] transceiver คือสินค้าแกนกลางที่ผูก [[photonic-interconnects|photonics]] เข้ากับ AI data center

## หน้าที่ใน data center

Data center ต้องย้ายข้อมูลจำนวนมหาศาลระหว่าง server และ switch. ถ้า link ช้า GPU ก็รอข้อมูล Optical transceiver จึงเป็นจุดที่ network bandwidth, latency, power consumption, และ cost ต่อ bit มาเจอกัน

คลิปพูดถึง module ความเร็ว 800G ถึง 1.6T. ยิ่ง bandwidth สูงขึ้น demand ต่อ laser, DSP, packaging, yield, และ thermal management ก็สูงขึ้นตาม

## อยู่ตรงไหนใน supply chain

ในกรอบของคลิป transceiver อยู่ปลายน้ำกว่าการทำ [[indium-phosphide-wafer|Indium Phosphide wafer]] แต่ยังไม่ใช่ data center ปลายสุด มันเป็นชิ้นส่วนที่ต้องถูกใส่ใน switch / optical circuit / network equipment อีกที

ผู้เล่นที่คลิปพูดถึง:

- [[coherent|Coherent]] — ถูกวางเป็นผู้นำเพราะคุมต้นน้ำถึง module และส่งของ 6-inch แล้วตามคำกล่าวในคลิป
- [[lumentum|Lumentum]] — photonics pure play ที่รายได้/margin โตเร็ว แต่ capacity 6-inch ยังต้อง ramp
- [[aaoi|AAOI]] — ตัวเล็กที่ต้องพิสูจน์การ scale MBE และส่งมอบตามเป้า
- [[nokia|Nokia]] — ผูก photonics กับ network/DSP stack มากกว่าเป็น pure module supplier

**ผลคือ:** transceiver เป็นจุดที่ theme AI กลายเป็นรายได้จริงได้ แต่ margin จะขึ้นกับ supply chain upstream และความสามารถผลิต volume

## See also

- [[review-lite-cohr-nok-aaoi]]
- [[photonic-interconnects]]
- [[indium-phosphide-wafer]]
- [[ai-data-center-bottlenecks]]
