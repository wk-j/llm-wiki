---
title: Flux
type: entity
tags: [ai, image-generation, model]
created: 2026-04-18
updated: 2026-04-18
sources: ["Will AI replace 3D software?.md"]
---

# Flux

Image diffusion model family from Black Forest Labs. Distributed in multiple variants — Flux.1 Dev, Flux.1 Schnell (fast, open-weight), Flux.1 Pro (hosted), and ControlNet-style conditioning models (Depth, Canny, etc.).

## Flux.1 Depth

A conditioning-aware variant that takes a **depth map** as input alongside a text prompt, producing images that respect the input geometry. Core piece of [[andrew-price|Andrew Price]]'s [[ai-3d-workflow]]: the depth pass is rendered from a [[blender|Blender]] block-in and routed through the Flux.1 Depth template in [[comfyui|ComfyUI]], yielding dozens of textured variants of the scene in minutes.

## See also

- [[comfyui]]
- [[will-ai-replace-3d-software]]
- [[ai-3d-workflow]]
