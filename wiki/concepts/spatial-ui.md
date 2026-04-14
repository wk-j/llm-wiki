---
title: Spatial UI
type: concept
tags: [ui, game-design, hud, immersion]
created: 2026-04-14
updated: 2026-04-14
sources: [The four horsemen of game UI design.md]
---

# Spatial UI

UI elements positioned within the game's 3D environment but invisible to in-game characters. They exist for the player's benefit, providing context-sensitive information anchored to objects or locations in the world.

## Characteristics

- Rendered in 3D space, attached to or hovering near game objects
- Characters are unaware of these elements — they're player-only aids
- Balances immersion and usability: information is "in the world" without claiming the character sees it
- Reduces friction by providing guidance without intrusive overlays

## Common Examples

- Pathfinding lines or navigation arrows
- Enemy outlines or nameplates hovering above characters
- Interaction prompts when approaching a door or item
- Trajectory arcs showing where a thrown object will land
- Health bars floating above NPCs

## Trade-offs

| Strength | Limitation |
|---|---|
| Context-sensitive — info appears where relevant | Still a UI element, not truly immersive |
| Helps novice players navigate and understand interactions | Overuse frustrates experienced players |
| Keeps screen uncluttered compared to [[non-diegetic-ui]] | May feel hand-holdy in exploration games |

Many games solve the experience-gap by letting players toggle spatial elements on or off.

## See also

- [[diegetic-ui]]
- [[non-diegetic-ui]]
- [[meta-ui]]
- [[four-horsemen-game-ui]]
