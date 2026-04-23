---
title: AI + 3D Workflow
type: concept
tags: [ai, 3d, workflow, creative-tools, complementarity]
created: 2026-04-18
updated: 2026-04-23
sources: [will-ai-replace-3d-software]
---

# AI + 3D Workflow / เวิร์กโฟลว์ AI + 3D

ไปป์ไลน์การสร้างสรรค์แบบผสมผสาน ที่ใช้ **AI สำหรับการสร้างไอเดีย (ideation) และการเรนเดอร์ (rendering)** ควบคู่ไปกับ **ซอฟต์แวร์ 3D สำหรับความแม่นยำและการควบคุม** แนวคิดนี้นำเสนอโดย [[andrew-price|Andrew Price]] ในงาน North American Blender Conference 2026

## แก่นความคิด

จุดแข็งของสองเครื่องมือนี้อยู่ตรงข้ามกันโดยสิ้นเชิง:

| แนวทาง | จุดแข็ง | จุดอ่อน |
|---|---|---|
| **AI ล้วน** | สร้าง concept art ได้หลายสิบแบบในไม่กี่นาที, สามารถทำ lookdev และลอง material/lighting ที่หลากหลายได้อย่างรวดเร็ว | ไม่สามารถควบคุมรูปทรง (shape), การหมุน (rotation), หรือการจัดวาง (placement) วัตถุได้อย่างแม่นยำ |
| **3D ล้วน** | จัดวาง layout ได้อย่างแม่นยำในระดับ surgical precision — ทุก pixel สามารถสืบย้อนกลับไปยัง transform ต้นทางได้ | ขั้นตอนการทำ lookdev และการ перевірка material ใช้เวลานาน, การลองไอเดียเพียงไม่กี่แบบอาจใช้เวลาเป็นวันๆ |

เมื่อนำมารวมกัน, จุดแข็งของเครื่องมือหนึ่งจะเข้ามา補จุดอ่อนของอีกเครื่องมือหนึ่งพอดี

## ไปป์ไลน์ต้นแบบ

ตัวอย่างการสร้างฉากฐานบนดวงจันทร์ (moon base):

1.  **คิดไอเดียด้วย AI (Ideation):** เริ่มต้นด้วยการรัน text-to-image เพื่อให้ได้ concept gro gro ว่าต้องการภาพประมาณไหน
2.  **วางโครงใน [[blender|Blender]] (Block-in):** จัดวางองค์ประกอบหลักของฉาก (scene) พร้อมกำหนดตำแหน่งและการหมุนที่แม่นยำ ซึ่งเป็นเรื่องง่ายในโปรแกรม 3D
3.  **สร้าง Depth Map → [[flux|Flux.1 Depth]] ผ่าน [[comfyui|ComfyUI]]:** เรนเดอร์ depth buffer จาก Blender แล้วนำไปใช้เป็นเงื่อนไข (condition) ในการ generate ภาพด้วย AI ผ่าน Node ที่ชื่อว่า `Flux.1 Depth` ใน ComfyUI ทำให้ AI สร้างภาพที่ยังคงเคารพโครงสร้างและมิติของ block-in เดิม แต่ได้รายละเอียดพื้นผิว (texture) และแสงเงาที่แตกต่างกันหลายสิบรูปแบบในเวลาไม่กี่นาที
4.  **เลือก Asset ที่ชอบ → สร้าง Mesh ด้วย Meshy:** Crop วัตถุที่น่าสนใจจากภาพที่ AI สร้างขึ้น แล้วใช้บริการ AI image-to-3D เช่น Meshy เพื่อแปลงภาพนั้นให้กลายเป็น 3D mesh
5.  **จัดฉากสุดท้ายใน Blender (Final Staging):** นำ mesh ที่ได้กลับเข้ามาใน Blender เพื่อประกอบเป็นฉากสุดท้ายที่สมบูรณ์

ด้วยไปป์ไลน์นี้, งานที่เคยใช้เวลาเป็นเดือนอาจเสร็จได้ในวันเดียว

## ผลกระทบ

- **ทักษะเดียวไม่พอ — ต้องใช้ทั้งสองอย่าง:** *"An AI artist couldn't create this without 3D, and a 3D artist couldn't do it this fast without AI."* — Andrew Price
- **โปรแกรม 3D จะถูกใช้มากขึ้น, ไม่ใช่น้อยลง:** เมื่อ AI artist ชนกำแพงเรื่องการควบคุม, โปรแกรม 3D คือเครื่องมือถัดไปที่พวกเขาจะหยิบมาใช้เพื่อก้าวข้ามข้อจำกัดนั้น
- **Integration ในอนาคต:** Price คาดการณ์ว่าในอนาคตอันใกล้, เราจะได้เห็น Blender ที่สามารถควบคุมผ่าน [[model-context-protocol|MCP]] และมีฟีเจอร์ guided rendering แบบ DLSS ฝังมาในตัว

## กรอบความคิดที่เกี่ยวข้อง

- [[judgement-vs-automation]]: กรอบแนวคิดที่ใช้อธิบายว่า *ทำไม* ทักษะที่ต้องใช้วิจารณญาณสูงอย่างการทำงาน 3D จึงรอดพ้นจากการถูก automate — เพราะมันไม่ใช่แค่งาน rote ที่มีขั้นตอนตายตัว
- [[engineering-role-shift]]: รูปแบบการเปลี่ยนแปลงบทบาทในงานวิศวกรรมซอฟต์แวร์ที่คล้ายกัน: งานต้นน้ำ (framing) และปลายน้ำ (review) มีความสำคัญมากขึ้น, ในขณะที่งานตรงกลาง (predictable execution) ถูกลดทอนลง
- [[llm-knowledge-bases]] / [[idea-file]]: แนวคิดการแบ่งบทบาท "AI สร้างไอเดีย / มนุษย์คัดเลือกและจัดการ" ซึ่งเทียบเคียงได้กับ workflow ในงานเขียนและ knowledge work อื่นๆ

## See also

- [[will-ai-replace-3d-software]]
- [[andrew-price]]
- [[blender]]
- [[comfyui]]
- [[flux]]
- [[judgement-vs-automation]]
- [[engineering-role-shift]]
