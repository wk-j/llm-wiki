---
title: AI + 3D Workflow
type: concept
tags: [ai, 3d, workflow, creative-tools, complementarity]
created: 2026-04-18
updated: 2026-04-18
sources: ["Will AI replace 3D software?.md"]
---

# AI + 3D Workflow / เวิร์กโฟลว์ AI + 3D

ไปป์ไลน์สร้างสรรค์แบบผสม ที่ใช้ **AI สำหรับ ideation และ rendering** ร่วมกับ **ซอฟต์แวร์ 3D สำหรับความแม่นยำและการควบคุม** — [[andrew-price|Andrew Price]] นำเสนอแนวคิดนี้ต่อสาธารณะในงาน North American Blender Conference 2026

## แก่นความคิด

จุดแข็งของสองแนวทางอยู่คนละด้าน (opposite strengths):

| แนวทาง | จุดแข็ง | จุดอ่อน |
|---|---|---|
| AI ล้วน | สร้าง concept ได้เป็นโหลในไม่กี่นาที เรนเดอร์ material / lighting ได้หลากหลาย | ควบคุม shape, rotation, placement แบบแม่นยำไม่ได้ |
| 3D ล้วน | จัด layout ได้แบบ surgical — ทุก pixel สืบย้อนกลับไปหา transform ต้นทางได้ | ทำ lookdev และ iterate material ช้า ไอเดียไม่กี่แบบใช้เวลาเป็นวัน ๆ |

รวมกันแล้วหักล้างจุดอ่อนของกันและกัน

## ไปป์ไลน์ต้นแบบ

ตัวอย่าง moon base:

1. **คิดไอเดียด้วย AI** (ideate). รัน text-to-image หนึ่งรอบเพื่อให้ได้ concept "ประมาณนี้"
2. **วางโครงใน [[blender|Blender]]** (block-in). วาง scene พร้อมตำแหน่งและการหมุนที่แม่นยำ — เรื่องง่ายใน 3D
3. **Depth-map pass → [[flux|Flux.1 Depth]] ผ่าน [[comfyui|ComfyUI]]**. Depth buffer ที่ได้จากการ render จะทำหน้าที่ condition การ generate ทำให้ output เคารพ geometry ของ block-in — ได้ textured variant หลายสิบแบบในไม่กี่นาที
4. **เลือก asset ที่ชอบ → สร้าง mesh ด้วย Meshy** (บริการ AI image-to-3D). Crop object ออกจาก AI output แล้ว Meshy แปลงเป็น 3D mesh
5. **Final staging ใน Blender**. Re-import mesh แล้วประกอบเป็นช็อตสุดท้าย

ฉากที่เคยใช้เวลาเป็นเดือน ตอนนี้เหลือวันเดียว

## ผลกระทบ

- **ทักษะเดียวไม่พอ — ต้องทั้งคู่.** *"An AI artist couldn't create this without 3D, and a 3D artist couldn't do it this fast without AI."* — Price
- **3D น่าจะถูกใช้มากขึ้น ไม่ใช่น้อยลง.** พอ AI artist ชน ceiling เรื่องการควบคุม 3D คือเครื่องมือที่พวกเขาจะหยิบมาใช้
- **Integration ในอนาคตอันใกล้.** Price คาดว่าจะมี Blender ที่ควบคุมผ่าน [[model-context-protocol|MCP]] และ guided rendering สไตล์ DLSS ฝังมาในตัว

## กรอบคิดที่เกี่ยวข้อง

- [[judgement-vs-automation]] — taxonomy ของทักษะที่อธิบาย *ทำไม* ความแม่นยำของงาน 3D ถึงรอดจากการ automate: มันขึ้นกับวิจารณญาณและคาดเดาไม่ได้ ไม่ใช่งาน rote
- [[engineering-role-shift]] — pattern bimodal เดียวกันในงาน software engineering: งานต้นน้ำ (framing) และปลายน้ำ (review) ขยาย ตรงกลาง (predictable execution) หดลง
- [[llm-knowledge-bases]] / [[idea-file]] — การแบ่งบทบาทแบบ "AI ideate / คน curate" เทียบเคียงได้กับงานเขียนและ knowledge work

## See also

- [[will-ai-replace-3d-software]]
- [[andrew-price]]
- [[blender]]
- [[comfyui]]
- [[flux]]
- [[judgement-vs-automation]]
- [[engineering-role-shift]]
