---
title: ComfyUI
type: entity
tags: [ai, image-generation, workflow, open-source]
created: 2026-04-18
updated: 2026-04-23
sources: ["Will AI replace 3D software?.md"]
---

# ComfyUI

UI แบบ node-based และ open-source สำหรับสร้าง pipeline การสร้างภาพด้วย diffusion-model แต่ละ node คือหนึ่งขั้นตอน (เช่น โหลดโมเดล, encode prompt, ใส่ conditioning, sample, decode, บันทึก); ผู้ใช้จะเชื่อมต่อ node เหล่านี้เข้าด้วยกันเป็นกราฟ ซึ่งจะถูกบันทึกและแชร์เป็น **workflow** ที่ใช้ซ้ำได้ มักใช้เป็นชั้น orchestration สำหรับ Stable Diffusion, [[flux|Flux]], และ ControlNet / LoRA เวอร์ชันต่างๆ

## ใน AI + 3D workflow

ComfyUI เป็นที่สำหรับรัน **Flux.1 Depth template** ซึ่งรับ depth-map pass ที่ export มาจาก [[blender|Blender]] พร้อมกับ text prompt และสร้างภาพเวอร์ชันต่างๆ ที่สอดคล้องกับรูปทรงเรขาคณิตของ input ดู pipeline ทั้งหมดได้ที่ [[ai-3d-workflow]]

การออกแบบที่เป็น node-based นี้คือสิ่งที่ทำให้การส่งต่อข้อมูลแบบ depth-conditioned เป็นไปได้จริงในทางปฏิบัติ: depth map จะถูกป้อนเข้าไปใน input socket เพียงช่องเดียว และการเปลี่ยนไปใช้ signal ควบคุมแบบอื่น (เช่น normal map, canny edge, pose) ก็เป็นเพียงแค่การต่อสายใหม่เท่านั้น

## ดูเพิ่ม

- [[flux]]
- [[will-ai-replace-3d-software]]
- [[ai-3d-workflow]]
