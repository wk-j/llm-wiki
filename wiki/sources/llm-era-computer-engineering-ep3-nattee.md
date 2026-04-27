---
title: วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง Ep. 3
type: source
tags: [ai, education, software-engineering, testing, ui-ux, infrastructure]
date_ingested: 2026-04-28
url: https://www.facebook.com/nattee.niparnan/posts/pfbid0D3r5G9z7N594186546367460984
---

# วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง Ep. 3

ตอนที่ 3 ของซีรีส์โดย [[nattee-niparnan|Nattee Niparnan]] เน้นเรื่องการใช้ AI ปิดจุดอ่อนส่วนตัว การที่ AI ทำลายความได้เปรียบของ "เป็ด" (Generalist) และความสำคัญของการรักษา [[eh-gland|ต่อมเอ๊ะ]]

## ประเด็นสำคัญ

### 1. AI ช่วยปิดจุดอ่อน (Closing the Gap)
- **Testing**: Nattee สารภาพว่าไม่ชอบเขียน test แต่ใช้ Claude Code สั่ง "We should have a test suite" ครั้งเดียวได้มา 225 test พร้อมสรุป coverage ที่ครอบคลุมส่วนสำคัญ
- **UI/UX**: ใช้ Gemini ช่วยตรวจหน้าจอเว็บ พบปัญหา [[horror-vacui|Horror Vacui]] (โรคกลัวที่ว่าง) ที่ทำให้ดีไซน์กลายเป็น "Wall of Text" และได้รับคำแนะนำให้เน้นจุดสำคัญแทน

### 2. จุดแข็งของ "เป็ด" เริ่มสั่นคลอน (The Shrinking Generalist Moat)
- ความรู้กว้างๆ แบบ "พอทำได้" ในด้าน Network, Ops, Infra (เช่น config Cisco/Huawei, Proxmox, Grafana) เคยเป็นจุดแข็ง แต่ตอนนี้ AI สามารถทำแทนได้ง่ายมาก
- ตัวอย่าง: Gemini ช่วยแก้ปัญหา SFP+ mismatch บน Cisco ด้วยคำสั่งที่ไม่มีใน doc (`service unsupported-transceiver`)
- สรุป: เส้นแบ่งที่ว่า "AI ทำไม่ได้" ขยับจาก code ไปสู่ architecture และ infrastructure อย่างรวดเร็ว

### 3. ยิ่งใช้ AI ยิ่งอ่อน (The Atrophy of Skills)
- การโยนงานให้ AI ทำหมดทำให้เราไม่ได้ฝึก "ต่อมเอ๊ะ" (Eh Gland) ซึ่งเป็นความสามารถในการตรวจจับความผิดปกติที่ AI มองข้าม (เช่น business logic ใน authorization)
- หากไม่มีต่อมเอ๊ะ เราจะไม่มีทางตรวจงาน AI ได้ และจะหยุดพัฒนาไปโดยปริยาย

### 4. ทางออก: รู้จักตัวเองและเลือกที่จะลึก
- ต้องกล้าออกจาก Comfort Zone ไปทำเรื่องที่ไม่ถนัดเพื่อให้รู้ "รูปร่าง" (ขอบเขต) ของตัวเอง
- นิสิตต้องเลือกว่าจะ "ลึก" เรื่องอะไร และ "กว้าง" เรื่องอะไร โดยต้องประเมินใหม่ทุก 6 เดือนเพราะ AI พัฒนาเร็วมาก
