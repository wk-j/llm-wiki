---
title: ComfyUI
type: entity
tags: [ai, image-generation, workflow, open-source]
created: 2026-04-18
updated: 2026-04-18
sources: ["Will AI replace 3D software?.md"]
---

# ComfyUI

Open-source, node-based UI for building diffusion-model image-generation pipelines. Each node is a step (load model, encode prompt, apply conditioning, sample, decode, save); users wire them into a graph that is saved and shared as a reusable **workflow**. Commonly used as the orchestration layer around Stable Diffusion, [[flux|Flux]], and various ControlNet / LoRA variants.

## In the AI + 3D workflow

Hosts the **Flux.1 Depth template**, which takes a depth-map pass exported from [[blender|Blender]] plus a text prompt and generates variants that conform to the input geometry. See [[ai-3d-workflow]] for the full pipeline.

The node-based design is what makes the depth-conditioned handoff practical: the depth map drops into a single input socket, and swapping in a different controlling signal (normal map, canny edge, pose) is a matter of rewiring.

## See also

- [[flux]]
- [[will-ai-replace-3d-software]]
- [[ai-3d-workflow]]
