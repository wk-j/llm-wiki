---
title: Blender
type: entity
tags: [3d, software, open-source, creative-tools]
created: 2026-04-18
updated: 2026-04-23
sources: ["Will AI replace 3D software?.md"]
---

# Blender

ชุดเครื่องมือสร้างสรรค์ 3D แบบ open-source ที่ดูแลโดย Blender Foundation ครอบคลุม pipeline ทั้งหมด — modeling, sculpting, rigging, animation, simulation, rendering (Cycles, Eevee), compositing, motion tracking — และสามารถขยายความสามารถได้ผ่าน Python API

## ความเกี่ยวข้องกับ wiki นี้

Blender เป็นเครื่องมือ 3D หลักใน **[[ai-3d-workflow|AI + 3D workflow]]** ของ [[andrew-price|Andrew Price]] โดย Price ใช้ Blender สำหรับงานที่ AI ยังทำได้ไม่ดี:

- **Block-in** — การวางตำแหน่ง, การหมุน, และการจัดองค์ประกอบของ object ใน scene อย่างแม่นยำ
- **Depth-map passes** — การเรนเดอร์ depth buffer แล้ว export ออกมาเป็น input สำหรับ conditioning ให้กับ [[flux|Flux.1 Depth]] ผ่านทาง [[comfyui|ComfyUI]]
- **Final staging** — การนำ mesh ที่ AI สร้างขึ้นมาประกอบเป็น scene ที่เสร็จสมบูรณ์

Price คาดการณ์ว่าจะมีการ integrate AI ที่ลึกขึ้นใน Blender เวอร์ชันอนาคต: เช่น Blender ที่รองรับ [[model-context-protocol|MCP]] และการเรนเดอร์แบบ guided สไตล์ DLSS ที่เป็นฟีเจอร์ในตัว

## ชุมชน (Community)

มีชุมชนขนาดใหญ่ที่มีศูนย์กลางอยู่ที่งานประชุมของ Blender Foundation **North American Blender Conference** (จัดที่ Austin) เป็นเวทีที่ Price ได้พูดในหัวข้อ "Controlling Blender with AI" ในปี 2026 ซึ่งเป็นแหล่งที่มาของ [[will-ai-replace-3d-software]]

## ดูเพิ่ม

- [[will-ai-replace-3d-software]]
- [[andrew-price]]
- [[ai-3d-workflow]]
- [[comfyui]]
- [[flux]]
