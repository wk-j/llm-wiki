---
title: Flux
type: entity
tags: [ai, image-generation, model]
created: 2026-04-18
updated: 2026-04-23
sources: ["Will AI replace 3D software?.md"]
---

# Flux

ตระกูลโมเดล image diffusion จาก Black Forest Labs. มีการเผยแพร่ในหลายเวอร์ชัน — Flux.1 Dev, Flux.1 Schnell (เร็ว, open-weight), Flux.1 Pro (hosted), และโมเดลสำหรับ conditioning แบบ ControlNet (Depth, Canny, ฯลฯ)

## Flux.1 Depth

เป็นเวอร์ชันที่รับรู้เงื่อนไข (conditioning-aware) โดยรับ **depth map** เป็น input ควบคู่ไปกับ text prompt เพื่อสร้างภาพที่เคารพรูปทรงเรขาคณิตของ input เป็นส่วนประกอบหลักใน [[ai-3d-workflow]] ของ [[andrew-price|Andrew Price]]: โดย depth pass จะถูกเรนเดอร์จากการทำ block-in ใน [[blender|Blender]] แล้วส่งผ่าน template ของ Flux.1 Depth ใน [[comfyui|ComfyUI]] ซึ่งจะสร้าง scene ที่มี texture แตกต่างกันหลายสิบแบบในเวลาไม่กี่นาที

## ดูเพิ่ม

- [[comfyui]]
- [[will-ai-replace-3d-software]]
- [[ai-3d-workflow]]
