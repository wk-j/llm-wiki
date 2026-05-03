---
title: "Building pi in a World of Slop — Mario Zechner"
source: "https://www.youtube.com/watch?v=RjfbvDXpFls"
author:
  - "[[AI Engineer]]"
published: 2026-04-17
created: 2026-05-03
description: "All I wanted was a shitty coding agent that is truly mine. And I’d have loved to just tell you why and how I built pi. But then Peter decided to make it the agentic core of OpenClaw. And now pi is col"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=RjfbvDXpFls)

All I wanted was a shitty coding agent that is truly mine. And I’d have loved to just tell you why and how I built pi. But then Peter decided to make it the agentic core of OpenClaw. And now pi is collateral. So yes, this is a talk about pi. But it is also a talk about how agents are destroying OSS, how I deal with that, and a plea to slow the fuck down.  
  
https://x.com/badlogicgames  
https://github.com/badlogic  
https://www.linkedin.com/in/mariozechner/  
  
Timestamps  
0:00 – Intro and motivation for building pi  
0:29 – Act 1: Building pi and the frustration with existing agent harnesses  
1:56 – Why current context management in tools like Cloud Code and Open Code fails  
4:44 – The importance of minimal harnesses and the "Terminal" benchmark  
5:35 – Introducing pi: A self-modifying, extensible agent core  
7:27 – The "YOLO" security philosophy and extensibility through TypeScript  
9:03 – Examples of pi extensions (chat rooms, NES, Doom)  
10:46 – Act 2: OSS in the age of "clankers" and how to fight them  
12:03 – Act 3: A plea to slow down and stop the "slop" in software development  
13:58 – How agents create "enterprise-grade complexity" and why humans are still the bottleneck  
16:12 – Practical advice: How to effectively integrate agents into your workflow

## Transcript

### Intro and motivation for building pi

**0:14** · Hey there, I'm Mario. I built pie in a world of slop and this is a strategy, a tragedy in three acts. Just to talk about this real quick, bunch of people on the internet gave me money for ad space on my torso and all of that goes to a charity. So yeah, thanks guys.

### Act 1: Building pi and the frustration with existing agent harnesses

**0:29** · So act one building pi in the beginning there was cloud code and was good right we all got basically catnipped by that thing and stopped sleeping um bunch of stuff before that but code cloud code was the one thing that kind of clicked with me the most and to preface all of this I love the cloud cloud team they're are brilliant people talented super high velocity so uh they also created the entire game major props to them so this is not a roast this is just me an old man telling you why I stopped using cloud code and built my own thing.

**0:59** · Um in 2025 I started using cloud code in about April I think thanks to Peter uh because he told us the agents are working now and back then it was simple and predictable and fit my workflow but eventually the token madness got hold of them I think and the team got bigger and they started uh dog fooding that stuff and

**1:23** · build a lot of features a lot of features I don't need which is fine I can just ignore them but with velocity and more features come more bucks and that's mad because I used to work at construction sites and if my hammer breaks every day I'm getting really mad and if my development tools break every day I'm also getting mad. So there was this it's just a running gag and here's tar telling us that cloud code is now a game engine and here's Mitchell from Ghosty telling us no it's not and eventually they fixed the flicker but then other stuff broke and I think they're now in the third iteration of a 2y renderer.

**1:54** · Yeah but that's just a symptom. The real problem is that my context wasn't my context. Cloud code is the thing that controls my context. And behind my back, cloud code does things uh to the context. So you have the system prompt which changes on every release, including the tool definitions.

### Why current context management in tools like Cloud Code and Open Code fails

**2:11** · They would remove tools, modify tools.

**2:14** · It's not good. They would insert system reminders in the most oppoune place in your context, telling the model, here's some information. It may or may not be relevant to what you're doing. That it actually says it may or may not be relevant what you're doing. And that kind of confused the model and that kind of broke my workflows.

**2:34** · On top of all that, there's zero observability because that's how the tool is constructed and I like knowing what my agents are doing. There's zero model choice which is obvious. It's the native entropic uh harness. So it makes sense for them to want you to use cloud, right? And there's almost zero extensibility and some of you might have written some hooks for cloud code, but I'm telling you the number of hooks and the depth of those hooks is very shallow. Um, and every time a hook triggers, what actually happens is a new process gets spawned. Basically, the command you specified for the hook to be executed. And I don't find that specifically efficient.

**3:05** · So, I uh took a step back and looked around for alternatives. And I'd like to especially call out AMP and factory droid, the Porsche and Lamborghini of coding agent harnesses. So, if you can afford them, please use them. They're at the frontier. They're really good, and the teams are fantastic. And there's a bunch of other options. And I have history in OSS. So naturally I kind of gravitated towards open code and again brilliant team super high execution velocity and they don't sell you hype they sell you tools that work for the most part.

**3:33** · I started looking under the hood of open code uh with respect to context handling as well because that's the most important part for me and I found a bunch of things like given some conditions open code would just uh prune tool output after a specific minimum amount of tokens and that basically lobomizes the model.

**3:54** · Uh there's also LSP server support which means every time your model is calling the edit tool open code goes to the LSP server that's connected asks are there any errors and if so injects that as part of the edit tool uh result which is bad because

**4:11** · think about how you add editing code you're not writing a line of code checking the errors writing the next line checking the errors you don't do that you finish your work and then you check the errors this confuses the model there's a bunch of other things like storing individual messages of a session in a JSON file. Each me message is a JSON file on disk. Uh there was this and this happens to all of us. No, no claim there. But it's not great if by default a server spins up, course headers are set in such a way that any website you open in your browser can now access your open code server.

**4:41** · That's yeah, and entirely unrelated to all of this, I started looking into benchmarks for coding agent harnesses and found terminal bench um which is a pretty good benchmark all things considered. And the funny part about it is that it's the most minimal kind of thing you can think of. All it gives the model is a tool to send keystrokes to to a T-Max session and read the output of that T-Max session. There's no file tools, no sub agents, none of that stuff. And it's one of the best performing harnesses in the leaderboard.

### The importance of minimal harnesses and the "Terminal" benchmark

**5:12** · Here's the leaderboard from December 2025. irrespective of model family terminal scores higher mostly high even higher than the native harness of that model. So what does that tell us? A form two thesis is we are in the around and find out phase of coding agents and their current form is not their final form right.

**5:31** · So second thesis is we need better ways to around and for me that means self modifying malleable agents things that the agent itself can modify and I can modify depending on my workflow. So I stripped away all the things built a minimal core but made it super extensible and made it so that the agent can modify itself with some creature comforts. It's not entirely bare bones. Uh so that's PI.

### Introducing pi: A self-modifying, extensible agent core

**5:59** · It's an agent that adapts to your workflow instead of the other way around. It comes with four packages. Uh an AI package that's basically just an abstraction across providers and context handoff between providers. An agent core uh which is just a while loop and the tool calling. A bespoke toy framework. I come out of game development. So I built a thing that actually doesn't flicker too much. And the coding agent itself.

**6:21** · Here's Pi's system prompt.

**6:23** · That's it. Eventually the industry created a new standard called skills which is basically just markdown files.

**6:30** · So we added that as well. and that needs to go in a system prompt. So, be crouchingly, we had to add a couple more lines. And finally, here's the magic that makes Pi able to modify itself. We ship the documentation which was handcrafted by me and an agent. Um, and code examples of extensions, and all we need to do for the agent to modify itself is tell it, here's the documentation. Here's some code that shows you how to modify yourself by writing extensions.

**6:57** · It comes with four tools. That's all it has. Retrate, edit, mesh. Here's the tool definitions. Don't read the the text. Just look at the size.

**7:05** · That's it. Here's what happens when you start a new session in one of these tools.

**7:11** · So the thing is the models are actually reinforcement trained up to a wazoo. So they know what a coding agent is because a coding agent harness is basically what they're being trained when they are post-trained. You don't need 10,000 tokens to tell them you're a coding agent. They know because they are coding agents. No, PI is also YOL by default because my security needs are different than yours. And I don't think a little dialogue that pops up every now every time you call bash asking you to approve is a smart security uh uh mechanism.

### The "YOLO" security philosophy and extensibility through TypeScript

**7:38** · So instead I give you so much rope that you can build anything that's fit for your specific security needs. There's also stuff that's not built in. I'm a he because this is how I do it. But if you don't like that then you just ask Pi to build you sub agent support or plan mode or MCP support whatever you need.

**8:02** · Extensibility comes with a bunch of table stakes and then with the extensions itself and extensions imply are just TypeScript modules. In the simplest case a TypeScript file on disk.

**8:12** · You point PI at that. Here's an extension loaded as part of the harness.

**8:16** · And with that you get a basically an extension API that lets you hook into everything and define stuff for the harness to expose to the to the model.

**8:25** · And that includes tools uh slashcomand shortcuts. You can listen in on any kind of event and react and then save state in the session that's optionally provided to the agent as well or stored there for tools that analyze sessions as part of your organizational workflows.

**8:43** · You can do custom compaction, custom providers and you have full control over the tool. So you can modify everything in PI and you can then bundle all of that up and put it on mpm or on GitHub because I think we don't need to reinvent another bunch of silos called marketplaces. We already have package manage managers and all of that hot reloads.

### Examples of pi extensions (chat rooms, NES, Doom)

**9:03** · So if you develop an extension for pi, you do so in the session and you hot reload the changes and see the the effects of that immediately which is very great and it's also game development thing is in game development you want high very low iteration uh speeds and that's great. So a couple of examples cloud or anthropic ships the slash by the way which lets you talk to the agent why goes on its main quest. I posted this little prompt on Twitter jokingly and somebody build it in five minutes with more features and they didn't have to fork a clone pie.

**9:35** · They just let the agent write the extension based on the prompt. Here's Nico. He's one of the most prolific uh extension writers. I don't know what the is going on here. It's a chat room for all of his Pi agents and they talk with each other. I would never use this, but all of this is custom including the UI. or you can play NES games or you can play Doom.

**9:58** · And there's a bunch of other examples I'm not going to talk about. So, how do you build a PI extension? You don't. You tell Pi to build it for you based on your specifications. And then you just iterate with it on that and hot reload during the session. I'm going to skip that example as well. And if you don't like building things yourself, and I hope you do like building things yourself, but if you don't, you can look on MPM or our little search uh interface on top of MPM to find packages for sub agents, MCP, and so on. So, does it actually work? Well, here's the terminal bench leaderboard from October before Pi had compaction.

**10:29** · I added that for Peter's claw thingy. It scored sixth place.

**10:35** · Uh, but none of this is actually about Pi. If you want to retake, I I basically want you to retake control of your tools and workflows. So build your own. Um and if you want to know more about pi and openclaw, go to this talk please. Yeah.

### Act 2: OSS in the age of "clankers" and how to fight them

**10:46** · And then eventually Peter happened. He put pi inside of open claw as its aentic core which meant my open source project became the target of a lot of openclaw instances unbeknownst to their users. So this is act 2 oss in the age of clankers. Clankers are destroying oss.

**11:01** · Here's tal draw. They closed down the issue on pull request tracker. Here's open clause uh trackers. Here's mine.

**11:08** · Half of that is open source instances who post garbage. So I started to rage against the clankers.

**11:14** · Um if you send a pull request, it gets autoclosed with a comment that asks you to please write a nice issue in your human voice, no longer than a screen worth of text. And if I see that I write looks good to me and your account name gets put in a file in the repository and the next time you send a pull request, it's let through. Clankers don't read that comment. They don't go back once they posted a pull request. So that's a perfect filter. Uh Mitchell eventually turned it into vouch. Here's a clanker.

**11:40** · Uh I also labeled them. If you had interactions with openclaw, your issues get dep prioritized. I also built tools where I embed uh issues and pull request texts into 3D space. So I see clusters of issues. Uh I also invented OSS vacation. I just close the tracker whenever I want. So I have my life back.

**11:58** · So does this work? Yes, sort of.

**12:02** · Which leads me to act three. Slow the down. Everything's broken.

### Act 3: A plea to slow down and stop the "slop" in software development

**12:09** · And then there's people that say, "Our product's been 100% built by agents."

**12:12** · Yes, we know it sucks now.

**12:14** · Congratulations.

**12:22** · And I'm hearing this from my peers and this is entirely unhealthy.

**12:27** · Um, so here's how we should not work with agents and why, at least in my opinion. I wrote this on my blog a while ago, but the basic is this. We're having armory of agents and you're using beats on been and you don't know that it's basically uninstallable malware and entropic build a C compiler that kind of works but actually doesn't and we're hoping the next generation of models will fix it and here is Perso building a browser and that's also super broken but the next generation will fix it and SAS is dead software solved in six months and my grandma just built herself a Spotify with her open claw come on people so agents are actually

**13:00** · combounding boooos which is my word for errors with serial learning and No bottlenecks and uh delayed pain. The delayed pain is for you. Here's your code base on a human on one agent and 10 agents. How much of the agent code can you review? Here's the same codebase but expressed in number of boooos per day.

**13:19** · How much of those boooos do you think you'll find? Then you say, "Oh, I have a review agent. Let me introduce you to the wonderful world of the Oro." Doesn't work. It catches some issues. Um the problem is that agents and merchants have learned complexity. Where did they learn that complexity from? From the internet. What's on the internet? All our old garbage code. There are some pearls on the internet, really well-designed systems, but 90% of code on the internet is our old garbage. And that's what the models learn from. And every decision of an agent is local, especially if the codebase is so big that it doesn't fit into its context.

**13:52** · And if you let it go wild and add abstractions everywhere that are intertwined. Um, so that leads to lots of abstractions and duplication and backwards compatibility. Who has seen that in the output of their agent? It's annoying or defense in depth. So yeah, you get enterprise grade complexity within two weeks with just two humans and 10 agents.

### How agents create "enterprise-grade complexity" and why humans are still the bottleneck

**14:15** · Congratulations.

**14:16** · And then you say, but my detailed spec.

**14:19** · Yes, sure. You know what we call a sufficiently detailed spec? It's a program.

**14:25** · So if you leave blanks in your spec, what do you think happens? How does the model fill in the blanks? And with what does it fill that in? It fills it in with the garbage that it learned on the internet from our old code, which is garbage to mediocre. And then you say, but humans also, yes, humans are horrible, fail failable beings, but they can learn and they are bottlenecks.

**14:46** · There's only so many boooos they can add to your code base on a daily basis. And humans feel pain, which is a very interesting property because humans hate pain. And once there's too much pain, the human has a bunch of options. It can quit their job. It can uh blame somebody else and make them fix it or everybody bands together and starts refactoring the out of the garbage codebase, right? Agents will happily keep into your codebase.

**15:16** · And now your agents MD and super complex memory systems will not save you. agents don't learn the way we learn.

**15:24** · Those are my most most beloved people. I don't even read the code anymore.

**15:28** · Congratulations. Something is broken and your users are screaming. So, who you going to call? Not yourself because you haven't read the code. So, you're relying on your agents, but they are now also overwhelmed because the codebase is so humongous that there's absolutely zero chance they can get all the context they need to fix the issues. And long context windows are a heck, as most of you will find out this year. as everybody's switching to 1 million tokens context windows and agentic search is also failing.

**15:57** · So the agent patches locally and up globally. If you see this in your codebase, you're So you cannot trust your codebase anymore and also not your test because your agent wrote your test. So good game. So here's how I think we should work. Um there's a bunch of properties for good agent tasks. That means scope.

### Practical advice: How to effectively integrate agents into your workflow

**16:18** · If you can scope it in such a way that the agent is guaranteed to find all the things it needs to find to do a good job, you're done. That means modularize your codebase. If you can give it a function to evaluate how well it did the job, even better. Hill climbing, auto research. Uh, anything non-m mission critical, let it wipe. Boring stuff, let it wipe. Reproduction cases for user issues, which are usually only partial in information, perfect. I don't spend any mornings anymore doing that. Or if you don't have a human near you, rubber duck. So, lots of tasks you can use them for and save time.

**16:48** · At the end of that, you evaluate. You take what's reasonable. Most of it isn't. And then finalize. My final slide, more or less, slow the down. Think about what you're building and why. And don't just build because your agent can do it. Now, that's stupid. Uh, learn to say no. This is your most valuable uh capability at the moment. Fewer features, but the ones that matter. And then use your agents to polish the out of that. Enlighten your users, not your uh token maxing desires.

**17:20** · Get the amount of generated code uh that you need to review.

**17:26** · And non-critical code, sure, wipe slop ahead. Critical code, read every line. See the keynote after me for more info on that. So, how do you know what's critical? Any guesses?

**17:38** · Well, you read the code. Uh, if you do anything important, write it by hand. You can use a clanker to help you with that, but don't let it make the decisions for you because we've learned all the decisions it makes are learned from the internet. And that friction is the thing that builds the understanding of the system in your head, which is important. And it's also where you learn new things. And all of this requires discipline and agency. And all of this still requires humans. Thank you.