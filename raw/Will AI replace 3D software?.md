---
title: "Will AI replace 3D software?"
source: "https://x.com/andrewpprice/status/2044830011257913564"
author:
  - "[[@andrewpprice]]"
published: 2026-04-17
created: 2026-04-18
description: "Here are the top 3 questions I was asked in Austin at the North American Blender Conference.1. Will AI replace 3D software?No. 2D is still u..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HGCxsGva8AAvNe6?format=jpg&name=large)

Here are the top 3 questions I was asked in Austin at the North American Blender Conference.

# 1\. Will AI replace 3D software?

No. 2D is still used in 3D workflows, and 3D will still be used in AI workflows. Because while the advantage of AI is **ideation and rendering**; the advantage for 3D is **precision and control**. They complement each other.

For example, let’s say I want to make a moon base colony set in 2060 (I presented this workflow on stage).

I can get a result that’s close to what’s in my head, but there’s no language to explain the exact rotation and precise position of each object in relation to each other.

![Image](https://pbs.twimg.com/media/HGCw826WYAADOmQ?format=jpg&name=large)

Great for inspiration, but very limited control over shapes and positions of elements.

But with 3D, this is trivial. So, I do the block-in in Blender:

![Image](https://pbs.twimg.com/media/HGCx7BQbEAA4tr6?format=jpg&name=large)

Now, what do the dome shaped 3d printed concrete habits look like? It could take me days to lookdev a handful of ideas. But in AI, this is trivial. I render a depth map pass from Blender, and load it into the Flux1 Depth template in ComfyUI, then type in my ideas into a text prompt:

![Image](https://pbs.twimg.com/media/HGCxN6cXIAAPWql?format=jpg&name=large)

In minutes, I have dozens of ideas:

![Image](https://pbs.twimg.com/media/HGCxRawagAAI2xC?format=jpg&name=large)

But how do I keep certain objects, discard others and arrange them precisely? Again, in AI this is impossible but in 3D this is trivial. Just crop into key assets and generate meshes with Meshy.

![Image](https://pbs.twimg.com/media/HGCxXEtWsAAlJY1?format=jpg&name=large)

Then bring them back into Blender for staging:

![Image](https://pbs.twimg.com/media/HGCxfanX0AA0no1?format=jpg&name=large)

A scene like this, with customized bespoke assets, previously took months. But now it takes just one day. An AI artist couldn’t create this without 3D, and a 3D artist couldn’t do it this fast without AI. So I don’t see a future in which 3D is replaced. In fact, it’s much more likely that as AI artists hit a ceiling on what they can control, 3D adoption grows. Especially as MCP and guided DLSS-type rendering is made native in Blender.

## 2\. Is AI going to replace me?

No, but an artist who uses AI will.

An image generator could make a finished image in less time than I could alone. But I can take that generation and improve it with my own taste and control.

The idea that you'll be able to resist AI workflows forever - on someone else's dime - is quite frankly, foolish. Consider how likely you would be to hire a plumber at 10x the price because he refuses to use a pipe inspection camera.

That's why I won't shut up about AI. I want to encourage artists to dabble and try these workflows, so they'll be prepared for the day a boss or client requests something on an impossibly fast turnaround.

## 3\. What skills will be valuable in the future?

Any skills that rely on your judgement are unlikely to be automated. Whereas anything that is predictable is likely to be automated. For example, layout, lighting, color stylists, design, narrative and world building? There’s no correct answer to these. 100 concept artists will create 100 different moon bases. Their taste and judgement are what's valuable. However, ask 100 retopo artists to retopo a character, and (while there would be some variance) the results would be much more similar. And if you can predict it, you can train it. So focus on the skills that rely on judgement with unpredictable outcomes.

I go into more detail in my presentation "Controlling Blender with AI". I'll share it when it's published.

[Follow me](https://twitter.com/andrewpprice?lid=tp37l40w18fe) for other discoveries.