---
title: Blender
type: entity
tags: [3d, software, open-source, creative-tools]
created: 2026-04-18
updated: 2026-04-18
sources: ["Will AI replace 3D software?.md"]
---

# Blender

Open-source 3D creation suite maintained by the Blender Foundation. Covers the full pipeline — modeling, sculpting, rigging, animation, simulation, rendering (Cycles, Eevee), compositing, motion tracking — and is extensible via a Python API.

## Relevance to this wiki

The anchor 3D tool in [[andrew-price|Andrew Price]]'s **AI + 3D workflow**. Price uses Blender for the tasks AI handles poorly:

- **Block-in** — precise placement, rotation, and composition of scene objects.
- **Depth-map passes** — a rendered depth buffer exported as conditioning input to [[flux|Flux.1 Depth]] via [[comfyui|ComfyUI]].
- **Final staging** — composing AI-generated meshes into the finished scene.

Price predicts deeper AI integration in future Blender releases: [[model-context-protocol|MCP]]-aware Blender and guided DLSS-style rendering as native features.

## Community

Large community anchored by the Blender Foundation's conferences. The **North American Blender Conference** (Austin) featured Price's 2026 "Controlling Blender with AI" talk — the source for [[will-ai-replace-3d-software]].

## See also

- [[will-ai-replace-3d-software]]
- [[andrew-price]]
- [[ai-3d-workflow]]
- [[comfyui]]
- [[flux]]
