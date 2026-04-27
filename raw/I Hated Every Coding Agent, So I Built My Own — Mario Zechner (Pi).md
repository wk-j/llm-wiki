---
title: "I Hated Every Coding Agent, So I Built My Own — Mario Zechner (Pi)"
source: "https://www.youtube.com/watch?v=Dli5slNaJu0"
author:
  - "[[Mastra]]"
published: 2026-03-31
created: 2026-04-28
description: "Game development veteran, creator of libGDX, and 17-year open-source contributor Mario Zechner tells the story of how he ended up building pi, his own minimal, opinionated terminal coding agent.It s"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Dli5slNaJu0)

Game development veteran, creator of libGDX, and 17-year open-source contributor Mario Zechner tells the story of how he ended up building pi, his own minimal, opinionated terminal coding agent.  
  
It started in April 2025 when Peter Steinberger and Armin Ronacher (Flask, Sentry) dragged him into an overnight AI hackathon. Within weeks, Mario was hooked on Claude Code — until he wasn't. There was feature bloat, hidden context injection that changed daily, the infamous terminal flicker, and zero extensibility for power users.  
  
He then surveyed the alternatives — Codex CLI, Amp, OpenCode... Eventually, he came across Terminus — an agent that gives the model nothing but a tmux session and raw keystrokes. If that's enough for the model to perform, what are all those extra features actually doing?  
  
Mario's thesis: we're still in the "messing around and finding out" stage, and coding agents need to become more malleable so developers can experiment faster.  
  
Pi is his answer: four tools (read, write, edit, bash), the shortest system prompt of any major agent, tree-structured sessions, full cost tracking, hot-reloading TypeScript extensions, and nothing injected behind your back. No MCP, no sub-agents, no plan mode — but all of it buildable in minutes through extensions.  
  
The community has already shipped pi-annotate (visual frontend feedback), pi-messenger (a multi-agent chatroom), and someone even got Doom running. On TerminalBench, pi with Claude Opus 4.5 landed right behind Terminus — before it even had compaction.  
  
🔗 LINKS & RESOURCES  
pi coding agent: https://pi.dev  
Mario Zechner: https://mariozechner.at  
Peter Steinberger / OpenClaw: https://github.com/steipete  
Armin Ronacher: https://lucumr.pocoo.org  
Claude Code: https://docs.anthropic.com/en/docs/claude-code  
Aider: https://aider.chat  
OpenCode: https://github.com/anthropics/opencode  
Amp (Sourcegraph): https://sourcegraph.com/amp  
TerminalBench: https://terminalbench.com  
Ghostty: https://ghostty.org  
Vouch: https://github.com/mitchellh/vouch  
libGDX: https://libgdx.com  
  
AI Engineer London is a community meetup for engineers and founders building with AI, covering everything from agent frameworks and RAG pipelines to LLMs in production. Each event features technical talks, live demos, and hands-on networking. This talk was recorded at AI Engineer London #10, hosted by Tessl, in collaboration with AI Engineer London.  
  
AI ENGINEER LONDON  
📅 Events: https://lu.ma/aiengineerlondon  
💼 LinkedIn: https://linkedin.com/company/ai-engineer-london-meetup  
  
📚 MASTRA RESOURCES  
Mastra: https://mastra.ai  
Learn Mastra in the world's first MCP-Based Course: https://mastra.ai/course  
Principles of Building AI Agents (Book): https://mastra.ai/books/principles-of-building-ai-agents  
Patterns for Building AI Agents (New Book): https://mastra.ai/books/patterns-of-building-ai-agents  
  
MASTRA?  
Mastra is an open-source TypeScript framework designed for building and shipping AI-powered applications and agents with minimal friction. It supports the full lifecycle of agent development—from prototype to production. You can integrate it with frontend and backend stacks (e.g., React, Next.js, Node) or run agents as standalone services. If you're a JavaScript or TypeScript developer looking to build an agentic or AI-powered product without starting from first principles, Mastra provides the scaffolding, tools, and integrations to accelerate that process.  
  
📑 CHAPTERS  
00:00 Intro  
02:17 The history of coding agents: ChatGPT → Copilot → Aider → Claude Code  
04:52 What Claude Code got right — and where it became a spaceship  
06:04 Claude Code Drawbacks  
09:39 Claude Code Alternatives  
11:38 OpenCode's compaction problem and prompt cache busting  
12:51 Why LSP feedback mid-edit is a terrible idea  
14:26 OpenCode's architecture issues and security vulnerability  
16:06 TerminalBench and Terminus  
18:13 Mario's Two Theses  
19:08 Introducing pi — strip everything, build a minimal extensible core  
20:01 The system prompt  
21:18 What's not in pi — and what you build instead  
22:40 Extensions: custom tools, custom UI, hot reloading  
24:00 Community extensions  
24:59 Tree-structured sessions, cost tracking, HTML export  
25:33 TerminalBench results  
25:54 Open source under siege and human verification

## Transcript

### Intro

**0:00** · \[music\] Hi, my name is Mario. I hail from the land of Arnold Schwarzenegger, which you probably haven't noticed yet based on my very good English.

**0:12** · I want to preface this with we've been running around with our 4-year-old the entire day through London. So we went to dinosaurs, mummies, Nando's obviously.

**0:21** · Uh \[laughter\] Uh and stuff I have already forgotten.

**0:26** · I'm very very tired and if you don't understand anything I say, just raise your hand and and say grandpa wake up.

**0:34** · Sure.

**0:35** · Um the reason I'm here is actually another person which is here incognito today. Let's call him uh Steter Pineburger.

**0:45** · \[laughter\] Um back in 2025, I think somewhere around April. He told me and Armin Ronacher, which you might also know of last fame and sentry fame. Dudes, those coding agents, they actually work now. I was like, oh shut the \[ \_\_ \] up.

**1:06** · \[laughter\] Sorry, I'm also using swear words. Um totally not. And a month later we teamed up at this flat for 24 hours overnight and just let ourselves uh get um immersed by the clankers, by the wipe code and by the wipe slop. And since then none of us have really were sleeping anymore basically. So we're building stuff, lots of stuff. Most of which we actually never used because that's the new thing in 2025-2026.

**1:36** · We build a lot of stuff, but we don't build a lot of stuff we actually use. We wrote a lot of stuff uh and eventually that culminated in me thinking, I hate all the existing coding agents or harnesses.

**1:50** · How hard can it be to write one myself?

**1:53** · And Peter was like, oh I just want to do a thing. Nobody's probably going to hear about it and uh it's going to be a personal assistant because that's what I always wanted to have and yeah, most of you probably know how his story went. So today I'm going to tell you my much less impressive story, but I I hope I can transport a couple of learnings as we say in the industry.

**2:13** · Um that I was able to gather in the past couple months. So pi. In the beginning there was cloud code. Actually, there was copy and pasting from chat GPT, right? We all did that in the beginning 2023.

### The history of coding agents: ChatGPT → Copilot → Aider → Claude Code

**2:27** · Uh then there was who remembers the original GitHub co-pilot?

**2:32** · Yeah, actually how many of you are engineers?

**2:35** · How many of you are using coding agents like cursor, cloud code? Okay.

**2:40** · Uh popularity contest cloud code?

**2:43** · CodeX CLI?

**2:45** · Cursor?

**2:48** · Open?

**2:48** · versus? Yeah. Open code? Anti-gravity.

**2:51** · Oh that's not a lot. Anybody using this?

**2:54** · \[laughter\] I like you.

**2:56** · We're going to have a beer later.

**2:58** · Anyway, so this was basically what happened, right? In 2025 and before. Start with copy and pasting from chat GPT. It's all mostly broken. It's mostly single functions, stuff you don't want to write. Then you got GitHub co-pilot inside of your Visual Studio code where you just tap tap tap to happiness, which did work sometimes, mostly didn't. Sometimes it would also just verbatimly um recite GPL code like John Carmack's inverse square root and stuff like that, which was a lot of fun.

**3:28** · And then there was Aider. Anybody remember Aider? Yes. Old people, hello.

**3:34** · Um Yeah.

**3:37** · You have gray hair. You obviously know Aider. Um There was also Auto GPT. Um probably not a lot there. Okay.

**3:45** · \[laughter\] He knows all the things.

**3:47** · Um And then eventually there was cloud code. Um I think they released it in November actually as a beta in 2024, but it really only became used um more Say again? February. Yeah, February, March, something like that 2025. And I was like, I love it. It's awesome. The cloud team is also awesome. They're on socials and they're all very good people and very talented people.

**4:12** · Um and they basically created the entire genre. I know there were precursors like Aider and Auto GPT, but nothing did this and this was basically the whole agentic search thing. So instead of like cursor going into your code base, indexing things, constructing ASTs and indexing that as well and it kind of and not really working. Um they just said, eh we reinforcement trained our models to just use file tools, bash tools to explore your code base ad hoc and find the places that it needs to find to understand the code and then modify the code.

**4:43** · And this worked so well that yeah, we stopped sleeping because we all of a sudden could produce so much more code than we could before by hand.

### What Claude Code got right — and where it became a spaceship

**4:52** · Back then it was simple and predictable and actually fit my workflow perfectly fine, but then They fell into the trap into which most of us probably fall. The clankers can write so much code, why not just let it write all the features you could ever imagine, right? Isn't that great? Let's just add this feature and that feature and this feature and that feature and eventually you end up with Homer Simpson's I don't even know what it's called. I call it a spaceship. And cloud code is now a spaceship.

**5:22** · It does so many things that you actually probably ever use like 5% of what it offers. You only know about 10% in total and the rest the 90% that's left over that's kind of like the dark matter of AI agents. Nobody knows what it's actually doing. And I personally find this not to be very helpful because I still think that you kind of need to know what the agent is doing. This guy might disagree to some degree.

**5:48** · Um and we're here at Tessel and they also like context management, right? Or context engineering as we've called it. And I eventually found that cloud code was not a good tool when it comes to observability and actually managing your context. Um then there was also this. Who likes this about cloud code? Like the immense amounts of flicker, unexplainable flicker. Well actually I know how to explain it and why it happens, but they still haven't fixed it.

### Claude Code Drawbacks

**6:15** · Here's Tariq, he's really great. I I love him. He is their dev rel guy mostly on Twitter and he's amazing.

**6:21** · But sometimes he also says questionable stuff like our terminal user interface is now a game engine. Now you have to know I have a game development background. Like that's where I come from and if I read something like this then it kind of hurts me a little bit because it's a freaking terminal user interface, dude. It's not a game engine, trust me.

**6:39** · \[laughter\] The only reason you think it's a game engine is because you're using react in your terminal interface and it takes like 12 milliseconds to re-layout your entire user interface graph. Just don't do that, man. You don't it's not a game engine, right?

**6:53** · So and then uh Mitchell who is writing Ghosty was like, dude that's offensive, man. Like don't blame it on Ghosty or any other terminal. Your code is garbage.

**7:03** · \[laughter\] Terminals can render it like a hundreds of frames per second uh

**8:09** · point, which would basically mess with your existing workflows. It was just not a stable tool. And now I understand it from their perspective, they need to experiment and they have a huge user base and it's really hard to experiment when you have a huge user base.

**8:21** · But they did not care. So all of us had to suffer, right? You you're working with this new tool, you try to create predictable workflows and then \[snorts\] the tool vendor changes a tiny little thing under the hood that makes the LLM go crazy with your existing workflows. That's just not sustainable. I need control over that. I can't rely on them providing me a stable kind of thing. Um So I believe as a consequence of their UI design, um they need to reduce the amount of visibility you have.

**8:53** · I personally don't like that too much, but that's just a personal preference. I understand that most people will be happy with the amount of information that cloud code will present you. Um There is zero model choice obviously because it's a Anthropic native tool so to speak. That's not a downside because cloud models models are I like them.

**9:12** · Like they're really good. Um And there's almost zero extensibility and you might find this kind of funny because they have this whole hook system and all of that, but if you compare it to what pi allows you to do, it's it's not as deeply integrated. Um it's also basically based on running a process when the hook event starts, which is very expensive um if you have to start up that process over and over again.

### Claude Code Alternatives

**9:39** · So eventually I I I soured on cloud code, not because it was terrible. It was just it did it stopped being a fit for me. It became a fit for a lot more people over that period. So obviously they did they're doing things right, right? But not for me.

**9:54** · Because I'm old.

**9:56** · So then I was looking around for options and there is Codex CLI which I really didn't like in the beginning both the user interface as well as the model. That has changed at least with respect to the model. Codex is really pretty good now.

**10:10** · And there's Amp. The team behind that used to work at Sourcegraph. They How do you this spin off of Sourcegraph?

**10:19** · Graph. And there is super good engineers. They they they managed to build a commercial coding harness where they take away features instead of adding them. And most of the choices make a lot of sense to me. Um So yeah, if you're looking for a commercial coding harness, I would definitely recommend Amp to you because it's really good. Factory Troy kind of similar spiel um also really good although they're not as experimental as Amp.

**10:47** · And then there's Open Code which is the open source uh coding harness a lot of people use, right?

**10:53** · So I have a history with open source. I've been in open source for well uh 17 years. I've managed big and small open source projects.

**11:03** · Uh so that's near and dear to my heart and so I thought I'd give Open Code a a try because that's close to me, right?

**11:12** · And next to Amp, they have one of the most grounded or pragmatic teams in the space. They don't hype you up with features you probably never use. They try to um kind of conserve a happy path that's very stable. Um And they also have pretty good thoughts on what coding agents mean for us as a profession which I personally can identify with.

**11:32** · Um The problem with Open Code is that it's also not very good at managing your context.

### OpenCode's compaction problem and prompt cache busting

**11:38** · Uh for example on each turn it's calling session compaction.prune which does the following. It prunes all tool results um before the last 40,000 tokens. Now who here knows what prompt caching is?

**11:56** · Right. What does this do to your prompt cache?

**11:59** · Lost the prompt cache. Yes.

**12:02** · So Open Code and Anthropic had an interesting history and eventually Anthropic in my opinion um rightly so said, "Dudes, that's just not going to happen, right?"

**12:14** · And there was never a public kind of thing about this, but Tarik explains it here. If you come to a gym and don't behave and and abuse the infrastructure so to speak, you're going to get banned.

**12:25** · And I think I don't have any evidence for that, but I think that's the reason why there is this animosity between Anthropic and Open Code. And I can totally agree or at least I think that Anthropic is clearly in the right here. Um don't mess with the infrastructure.

**12:42** · Um then there's also other stuff like Open Code comes with LSP language server protocol support out of the box. Coming back to context engineering let's say you give your agent the task of modifying a bunch of files. What does that mean in practice? It will make a bunch of edits um one after the the other to a bunch of files.

### Why LSP feedback mid-edit is a terrible idea

**13:03** · How probable is it that after the first edit out of 10 edits so to speak, the code will compile?

**13:12** · What happens if you modify your code line by line?

**13:15** · How long does it take for it to stabilize again and compiles cleanly?

**13:19** · It doesn't. It won't compile after the first edit, probably not after the second edit and so on and so forth. So if you then turn around and say, "Hey, dear LSP server, I just edited one line in this file. Is it broken?" Then the LSP server will say, "Yes, it's really broken." And what this feature does it it then injects this error directly after the tool call as a kind of feedback to the model, "Oh, what you just did is wrong."

**13:45** · And the model is like "What the \[ \_\_ \] dude? I'm I'm not done editing things. Why are you telling me this? Obviously it's not wrong." But if you do this often enough, the model will just give up and that leads to very bad outcomes. Um So I'm not a fan of LSP. I think it's a very terrible idea to have that enabled.

**14:02** · There is natural synchronization points where you want to have linting and type checking and all of that and that is when the agent think it's done.

**14:09** · Only then.

**14:13** · This has changed recently. This is a single session of Open Code. But every message becomes its own JSON file. Every single message becomes its own JSON file on disk. That indicates to me that there wasn't a lot of thought put into the architecture of the whole thing. And if I lose trust in that, I don't want to use that tool anymore.

### OpenCode's architecture issues and security vulnerability

**14:35** · Again, I think the team is actually really good. I think they iterated super quickly and built something that's super useful to a lot of people obviously. It's just again decisions that I wouldn't have made that made me decide to build my own.

**14:49** · Then there was also this Open Code comes with a um a server by default. The so the current architecture is based on a server and clients connect to it and the terminal user interface is one of the clients. There's also a desktop interface and I don't know.

**15:03** · That turned out to be a security vulnerability with remote code execution baked in by default. And that's also like if you're so proud of your server infrastructure or server architecture then I would assume you're grown-up engineers that thought about security as well. And apparently that didn't happen. And this was open for a long time. And again, I'm not blaming anyone here.

**15:25** · This is stuff that just happens if you're working in an industry that's operating at a break break breakneck speed that we haven't seen before, right? It's just I don't want to use that tool if that is a thing.

**15:37** · So so this was my observations with regards to existing coding harnesses and Android would have been something I could have used, but again no control. In case of Amp, even decide what models you can use and it's only a single model for a single type of task and that's not me. In terms of Troy, I think it's a little bit more open.

**15:58** · But at the time when I tried it out, um it just didn't I I didn't see a big um advantage over Cloud Code.

### TerminalBench and Terminus

**16:06** · \[snorts\] And then I looked into benchmarks for entirely different reasons and found Terminal Bench. Who knows what Terminal Bench is?

**16:15** · Okay, basically it's a coding or an agent evaluation harness which has a bunch of computer use and programming related um um Sorry. Old and tired because we're all old. It has a bunch of computer use and coding related tasks that an agent or the LLM inside an agent harness um needs to uh fulfill. I think it's about 20 uh 82 or so. And they're very diverse.

**16:44** · They're from fix my Windows setup to um code me a Monte Carlo simulation or something like that. Um and they have a leaderboard and on that leaderboard you see the combination of coding agent harness and model, right?

**16:57** · Um they have their own coding agent called Terminus. And I think it's brilliant because it's one of the best performing harnesses in the benchmark. You're going to see it later on. Uh what exactly does it do? Well, all the model gets uh is a tmux session and all it can do is send keystrokes to it and read back the the VT code sequences that are emitted.

**17:23** · So this is like the smallest most minimal interface uh a model can have uh to to your computer, right? And this performs like top of the line of the entire leaderboard.

**17:36** · So what does this tell us about existing coding agents harnesses? Do we need all these features for the models to actually perform?

**17:45** · For me personally, this is not just about the model actually being good. It's also about me as the user the human having a way to interact with my agent with the model. And Terminus is obviously not the user experience or developer experience that I want. But it tells us that all of these features all of these coding harnesses have might not neces- might not be necessary to um get good results out of agents.

**18:10** · So no file tools, no sub agents, no web search, or nothing.

### Mario's Two Theses

**18:13** · Two theses is based on all of these findings. We are in the messing around and finding out stage and nobody has any idea what the perfect coding agent should look like or what the perfect coding harness should look like. We're trying both minimalism and going full spaceship swarms and teams of agents and no control and full autonomy and whatever. I think that's not done yet. We haven't answered the question what this should look like ideally and what will become the industry standard.

**18:38** · And the second thing is we need better ways to mess around uh with coding agents. That is we need them to be able to self-modify them uh selves and become malleable so we can quickly experiment with ideas and see if this is something we can make like an industry standard a new workflow that we probably all going to adapt.

**18:58** · So the basic idea was and it's very simple and not rocket science, strip away everything and build a minimal extensible core.

**19:04** · \[snorts\] There's some creature comforts. It's not a blank slate. So that's Pi um and the general motto is uh adapt your coding agent to your needs instead of the other way around. It comes with four packages uh an AI package which is basically just a simple abstraction over multiple providers which all speak different transport protocols.

### Introducing pi — strip everything, build a minimal extensible core

**19:27** · Um so it's very easy to talk to all the providers and switch between them in the in the same context or same session. Um the agent core which is just a a generalized agent loop with tool invocations, verification, and so on and so forth. And streaming um uh a terminal user interface that's like 600 lines of code.

**19:45** · \[laughter\] And works really well surprisingly uh because it wasn't written by a clanker. Um and the coding agent itself which is both an SDK that that you can use head in headless mode or a full terminal user interface coding agent. This is the entire system prompt. There's nothing more there. Compared to other coding harnesses system prompts. That's in tokens. Yeah.

### The system prompt

**20:13** · It turns out frontier models are heavily RL trained to know what the coding agent is. So, why do you keep telling them that they're a coding agent and how they should do coding tasks, right?

**20:25** · Um.

**20:27** · YOLO by default. Why is that?

**20:30** · Most coding agent harnesses at the moment have two modes, either agent can do whatever it wants or agent um gets to ask you, "Do you really want to delete this file? Do you really want to list the files in this directory?" And so on and so forth. And there's different shades of gray here, but at the end of the day it boils down to the user needs to approve an action by the agent and then we are safe. And I think that's wrong because that leads to fatigue and people will either turn it off entirely, YOLO mode, or just sit there and type enter without reading anything.

**21:00** · So, I don't think that's a solution. Containerization is also not a solution if you're worried about exfiltration of data and prompt injections, but I think that's the only thing that you I think that's the best basis compared to guardrails like approval or dialogues. It only has four tools, read a file, write a file, edit a file, and bash.

### What's not in pi — and what you build instead

**21:20** · Bash is all you need. What's not in there? No MCP, no sub agents, no plan load, no background bash, no built-in to-do's. Here's what you can do instead. For MCP, use CLI tools plus skills or build an extension, which we'll see in a bit. Uh, no sub agents. Why? Because they're not as observable. Instead, use tmux and spawn the agent again.

**21:41** · You have full control over the agent's outputs and inputs and can uh, see everything that's happening in in the sub agent. Interestingly enough, code codes spawn uh, team mode now does exactly this basically as well. No plan load. Write a plan MD file. You have a persistent artifact instead of some janky UI that doesn't really fit into your terminal viewport uh, and you can reuse it across multiple sessions. Um, no background bash. Don't need it.

**22:08** · We have tmux. It's the same thing. And no built-in to-do's. Write a to-do MD. Same thing. Or build all of this yourself the way you like it. And this is what Pi allows you by being super extensible. So, you can extend tools, custom you can give the LLM tools that you define. I think no other coding agent harness currently offers that unless you fork open code.

**22:32** · You don't need to hear it. You just write a simple TypeScript file and it gets loaded automatically. You can also write custom UI. Uh, skills are obviously in there, prompt templates, uh, themes uh, and you can bundle all of that up, put it on NPM or Git, and install it with a single command, which is very nice.

### Extensions: custom tools, custom UI, hot reloading

**22:49** · And everything hot reloads. So, I develop my own extensions that are project or task specific um, in Pi inside the project and uh, as the uh, agent modifies the extension, I just reload and it immediately updates uh, all of the running code, which is very nice. And in practice that means you can do custom compaction. I think that's one of the things that people should experiment more because all of compact of the compaction implementations currently are not good.

**23:20** · Uh, permission gates, you can easily implement them in 50 lines of code and can uh, cover what all the other agent harnesses do if you want that. Custom providers, register proxies or off self-hosted models, don't care. You don't need me to do this for you. You can do this and actually your clankery can do it for you. Uh, or override any built-in tool. Modify how read, write, edit, and bash work.

**23:41** · Don't care. I I have a version of read, write, edit, and bash that works through SSH on a remote machine. For me, that took 5 minutes to implement. And it works. Uh, and you have full tree access, so you can actually write entirely custom UI in the coding agent. Code code shipped slash by the way, it took 5 minutes for somebody to replicate that in Pi with more features.

### Community extensions

**24:05** · Uh, Pi messenger, I have no idea what it's doing, but apparently it's like a chat room for multiple Pi agents that then communicate which then has custom UI where you can look what they're doing and yeah, it just works. Uh. Um, or Pi mess if you forge just do play a game while the agent is running, right? You can do that.

**24:25** · Um, or Pi annotate. Um open up the website you're working on currently and annotate stuff in the front end and give feedback to the agent directly in line. Feed it back into the context, have it modify the thing. Uh, or something I use is file switch. I don't want to switch over to an IDE or editor.

**24:43** · I just want to quickly look at the file that's been modified. So, all of this is extensions. None of this is built-in and it takes people usually a couple of minutes to an afternoon to build all of this the way they wanted to. Pi web access, also don't know what it's doing.

**24:58** · \[laughter\] Uh, Pi also comes with tree structure. Not going to explain that. Just look at pi.dev. Um, your session is a tree, not a linear list of chats. So, you can basically do sub agents by read all the files in the directory, summarize this, go back to my my root of the conversation, take the summary with me and do the actual work.

### Tree-structured sessions, cost tracking, HTML export

**25:18** · Um.

**25:19** · Nothing is injected behind your back. Agent skills, full cost tracking. A lot of harnesses don't do this. Yeah, open code does it not well. Uh, HTML export, JSON formats, headless JSON streaming, blah blah blah. Does it actually work? Well, terminal bench. Let me zoom in here. I can't. This is amazing. Here's Pi right behind Terminus 2 uh, using Cloud Opus 4.5. That was back in October where Pi didn't even have compaction.

### TerminalBench results

**25:48** · Right?

**25:49** · Uh, demo time. Skipping that. Rage against the clankers because they are breaking open source. If you are associated with this guy's project, then you will have hundreds of people coming from open claw to your repository and spam you with clanker filth and slop. Um, so I had to invent a couple of measures. I invented OSS vacation. So, I just close issues and PRs for a couple of weeks and work on things on my own.

### Open source under siege and human verification

**26:16** · Anything that's important will be reported later on anyways. Or in the Discord. And then I also implemented a custom access kind of scheme where I have a markdown file in the repository. If somebody opens a PR without being in without their account name being in that markdown file, the PR gets auto closed.

**26:34** · I don't care. First, introduce yourself in a human voice via an issue. Write an issue that's not longer than a display long because everything else is clanker slop, probably.

**26:44** · And once you did that, I'm happy to looks good to me you. So, you get into that file and can now submit PRs to the repository. All I'm asking is human verification. And Mitchell from Ghost it then took this and took the uh, built a project called vouch, which is more easily applicable to your own open source repository. \[music\] And that is Pi. Go forth and try it.

**27:08** · \[music\] \[music\]