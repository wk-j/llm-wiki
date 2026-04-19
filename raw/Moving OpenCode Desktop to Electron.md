---
title: "Moving OpenCode Desktop to Electron"
source: "https://x.com/brendonovich/status/2045725889422610602"
author:
  - "[[@brendonovich]]"
published: 2026-03-25
created: 2026-04-19
description: "I recently announced that we’ve rebuilt OpenCode Desktop on top of Electron and will soon stop releasing the Tauri version. This wasn’t a de..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HGPaxQRbYAE-Bl3?format=jpg&name=large)

I recently announced that we’ve rebuilt OpenCode Desktop on top of Electron and will soon stop releasing the Tauri version. This wasn’t a decision we made lightly, and it has nothing to do with either Tauri or Electron being innately “better” or “faster” - Electron is simply a better fit for our use case. To understand why, let’s first discuss how OpenCode actually works.

## TypeScript all the way down

OpenCode operates on a client-server model, with everything written in TypeScript. Clients such as the TUI and web UI talk to a server, which handles running agent loops, communicating with LLMs, and interacting with its SQLite database. The web UI connects to servers over HTTP, and so requires a running server to communicate with. You can do this yourself by running \`opencode serve\` in a terminal, but we'd like to offer a simpler experience that just involves downloading and running an app - hence the existence of Desktop.

We initially picked Tauri for this as a lightweight wrapper around our web UI and CLI. On startup, the bundled CLI would run \`opencode serve\`, giving the web UI a local server to connect to. This let us ship a small, functional app that (mostly) worked across all OSes.

## Where things went wrong

Over time, though, we ran into a couple of problems. Adam puts the first one rather eloquently:

> Mar 25
> 
> Because WebKit is assssss. Moving to Electron very soon.

Tauri uses WebKit on macOS and Linux, which not only has worse performance than Chromium when rendering our app, but also has minor inconsistencies with it, especially around styles. This directly impacts our ability to ship a consistent experience across all platforms, and the reduced performance makes the app less pleasant to use day to day.

> Tauri has an ongoing effort to support Chromium via CEF instead of the system webview, but when that will be stable remains uncertain.

The second problem was running the CLI - it impacted startup time, and occasionally just failed (despite [@LukeParkerDev](https://x.com/@LukeParkerDev)'s best efforts on Windows). This was less important on its own, but once combined with our desire to move from Bun to Node (for other reasons), the idea of simply running our server code within Electron's built-in Node process was quite appealing.

## Actually doing it

After considering these problems, we decided to move to Electron. Getting our UI working was easy - we've designed it to be portable, and agents are pretty useful.

> Feb 19
> 
> i worked very hard on it

Early versions of the app continued to bundle the CLI because our server code still relied on Bun-specific APIs. Eventually we removed all of them and could run the server within Node.

> Feb 19
> 
> hate when people spam PRs on open source projects

> This does mean that any plugins that rely on Bun-specific APIs will not work in newer Desktop versions. We'll have more to say about this with OpenCode 2.0.

Now we have both Tauri and Electron versions of Desktop. We will soon make the Electron version the default for direct downloads and in-app updates on our beta channel, and will eventually do the same for our general releases.

## Wrapping up

I hope this has been informative to all of you who asked about our reasoning for this move. You can download our Electron beta today from the links in our beta repo: [https://github.com/anomalyco/opencode-beta](https://github.com/anomalyco/opencode-beta) For all my other Tauri and Rust enjoyers, I'll answer some common questions here. I'm happy to answer more questions in replies.

> Tauri uses Rust, doesn't that mean it's fast?

Getting the best performance out of Tauri requires implementing your app's logic in Rust - Tauri itself is little more than a Rust library for launching and communicating with webviews.

This was great when I worked on [@cap](https://x.com/@cap), for example, since we could do all our video encoding and rendering natively in Rust. OpenCode is all written in TypeScript though, so the server needs to run in a Node/Bun process regardless. Any Rust we did use in Desktop wasn't going to move the needle on performance unless we rewrote the entire core and server (which I would love to do tbf).

> Are you saying Rust and Tauri are bad?

Not at all! I have a fond history of building with Rust and Tauri, and will continue to do so on other projects. This is simply a pragmatic decision based on our use case. If you're building an app with a simpler UI that demands native performance or easy access to system APIs, I think Tauri is still a great fit.

> Doesn't Electron produce larger app bundles than Tauri?

Yeah, it's a trade-off we're willing to make.