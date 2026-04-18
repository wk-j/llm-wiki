---
title: "Will AI Replace 3D Software? — Andrew Price"
type: source
tags: [ai, 3d, blender, workflow, creative-tools, automation]
created: 2026-04-18
updated: 2026-04-18
url: https://x.com/andrewpprice/status/2044830011257913564
date_published: 2026-04-17
sources: ["Will AI replace 3D software?.md"]
---

# Will AI Replace 3D Software?

X thread by [[andrew-price|Andrew Price]] (@andrewpprice), published 2026-04-17, answering the top three questions he was asked at the North American Blender Conference in Austin. Makes a concrete case for AI + 3D complementarity using a moon-base scene walkthrough demonstrated live on stage.

## The three questions

### 1. Will AI replace 3D software?

**No.** AI's strength is **ideation and rendering**; 3D's strength is **precision and control**. They complement each other.

Pure AI is great for inspiration but offers little control over precise object rotation and position. In 3D this is trivial. Price predicts 3D adoption will *grow* as AI artists hit a ceiling on what they can control, especially as MCP and guided DLSS-style rendering go native in [[blender|Blender]].

### 2. Is AI going to replace me?

**"No, but an artist who uses AI will."** Taste and control still matter, but refusing AI workflows is "on someone else's dime" — analogous to hiring a plumber at 10× the price for refusing to use a pipe inspection camera. Artists should dabble now to be prepared when clients demand fast turnarounds.

### 3. What skills will be valuable in the future?

**Skills requiring judgement with unpredictable outcomes.** Examples: layout, lighting, color, design, narrative, worldbuilding — 100 concept artists make 100 different moon bases. In contrast, predictable tasks (e.g., retopology — 100 artists produce similar results) will be automated: *"If you can predict it, you can train it."* See [[judgement-vs-automation]].

## The moon-base workflow (demonstrated on stage)

A scene that would have taken *months* now ships in *one day*:

1. **Initial ideation with AI.** Text-to-image generation yields a rough "this is the vibe" concept. Good for inspiration, weak on shape/position control.
2. **Block-in in [[blender|Blender]].** Place objects with precise rotation and position.
3. **Depth-map pass → [[flux|Flux.1 Depth]] in [[comfyui|ComfyUI]].** Render a depth map from the Blender scene; feed it into the Flux.1 Depth template with text prompts ("dome-shaped 3D-printed concrete habitats"). Produces dozens of textured variations in minutes.
4. **Select key assets → mesh generation with Meshy.** Crop favored objects from AI outputs; Meshy (an AI image-to-3D service) converts them into meshes.
5. **Final staging in Blender.** Import generated meshes; compose the finished shot.

> "An AI artist couldn't create this without 3D, and a 3D artist couldn't do it this fast without AI."

## Key takeaways

- AI and 3D are **complementary, not competitive** — AI for ideation/rendering, 3D for precision/control. See [[ai-3d-workflow]].
- The **hybrid artist wins**. Refusing AI is economically untenable.
- Survive-vs-automate hinges on **judgement and unpredictability**; the same framework that appears in software via [[engineering-role-shift]].
- Expect **tighter AI/3D integration** — [[model-context-protocol|MCP]]-driven Blender, guided DLSS-style rendering.

## See also

- [[andrew-price]]
- [[blender]]
- [[comfyui]]
- [[flux]]
- [[ai-3d-workflow]]
- [[judgement-vs-automation]]
- [[engineering-role-shift]]
- [[model-context-protocol]]
