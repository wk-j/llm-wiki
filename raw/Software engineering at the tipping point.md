---
title: "Software engineering at the tipping point"
source: "https://www.youtube.com/watch?v=2n41YjR5QfU"
author:
  - "[[Google for Developers]]"
published: 2026-05-22
created: 2026-05-28
description: "Learn to use systems thinking to understand how developer ecosystems guide the evolution of your software systems. Improve your intuition for the systemic im..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=2n41YjR5QfU)

## Transcript

**0:00** · \[MUSIC PLAYING\] ADAM BENDER: Hey, everybody.

**0:07** · How you doing?

**0:07** · \[CHEERS\] Hey, that's pretty good!

**0:11** · That's pretty good.

**0:12** · 3:00 PM on a Wednesday, right?

**0:16** · It's a Wednesday-- not so bad.

**0:19** · Welcome to Software Engineering at the Tipping Point.

**0:22** · My name is Adam Bender.

**0:24** · And today I'm going to talk to you about something called software ecology, a term you might not have heard before.

**0:29** · I want to talk about it because it will tell us something about the impact of AI on our developer ecosystems, the developer ecosystems you work in every day.

**0:37** · Now I don't know if you guys have noticed this.

**0:39** · But things are getting pretty weird out there, right?

**0:42** · Your job in 2026 does not look like what you thought it would in 2020.

**0:47** · I assure you that.

**0:48** · If you tried to explain to 2020 me what this was going to be, I would not have believed you.

**0:53** · It can be a bit overwhelming to try and figure out where all of this change is taking us, right?

**0:59** · And while I can't predict the future, I think that if we study our software ecosystems as they are today, some of the answers we're looking for are a lot closer than we think.

**1:08** · I think that software ecology, this idea, it gives us the perfect lens for framing this particular moment in our industry.

**1:15** · Now I can hear you asking, what is software ecology?

**1:18** · And did he just make this up to get on stage?

**1:21** · I did not.

**1:22** · It is a real term.

**1:23** · But before I define it, I want to set some context for you.

**1:26** · So we're going to go a little deep-dive on systems thinking.

**1:28** · I hope you're OK with that.

**1:30** · Hang with me.

**1:30** · I promise you, it will all make sense when we get there.

**1:34** · So let's start with the concept of a system-- a system.

**1:38** · It's a group of interrelated elements that act according to a set of rules to form a unified whole.

**1:43** · That sounds pretty fancy.

**1:44** · But you know systems.

**1:45** · They look like this.

**1:46** · This is a system you're probably pretty grateful for today.

**1:49** · This is what air conditioning is, right?

**1:50** · So you have a thermostat that knows what temperature to be.

**1:52** · You have an HVAC that's going to jack the temperature up or down.

**1:55** · And you have a room.

**1:56** · And when the temperature is right, the signal stops.

**1:59** · That's a system.

**2:01** · If you're a software engineer, you're probably used to thinking about systems all the time.

**2:05** · You design them.

**2:05** · You build them.

**2:06** · You operate them.

**2:07** · But one thing you've probably learned when working with systems is that everything is connected, everything.

**2:13** · That's a theme you're going to hear from me a couple times today.

**2:17** · Now let's move on to an ecosystem, which is a particular kind of system.

**2:22** · This is a long one.

**2:22** · So bear with me.

**2:24** · An ecosystem is a dynamic network of interdependent actors that co-evolve with their environment, characterized by emergent behavior and decentralized agency.

**2:33** · Ecosystems are complex.

**2:36** · They're built from complex components.

**2:38** · The components themselves are deeply connected.

**2:40** · They have agency.

**2:41** · They can make decisions.

**2:42** · They can do things.

**2:43** · And critically for us, the environment is a part of that system.

**2:48** · The environment is a part of the system.

**2:50** · You can't separate the two.

**2:53** · So ecosystems are also a kind of complex adaptive system.

**2:56** · A Complex Adaptive System, or CAS, they're characterized by their ability to grow and change and evolve over time.

**3:03** · All the cool systems are complex adaptive systems.

**3:05** · Now, complex adaptive systems, they possess this emergence quality as well.

**3:10** · An emergent property is something that you can't see by looking at any individual piece of the system.

**3:15** · You can only see it when the system is all put together.

**3:18** · And then you see behavior emerge out of it.

**3:20** · And it's that constant change, that learning, plus the emergence that make it really hard to figure out what's going on in an ecosystem.

**3:29** · Now when you think of ecosystems, or at least when you thought of them before you walked in here, this is probably what you had in mind.

**3:34** · And frankly, I'd like to be here right now, right?

**3:36** · Looks kind of idyllic.

**3:38** · But your internal developer environment, it is also a kind of ecosystem.

**3:42** · You have all your tools and services.

**3:44** · You have complex actors.

**3:45** · You have people with opinions and things they want to get done.

**3:47** · You have business constraints.

**3:49** · This is a system, too.

**3:50** · And in fact, it's a particular kind of system.

**3:53** · It's a socio-technical system.

**3:55** · A socio-technical system is just a fancy way to say a system made of people and technology.

**4:01** · Now socio-technical systems are incredibly complicated.

**4:05** · They're complicated because you start with all that technology.

**4:08** · And then you mix in the people.

**4:10** · There's a pretty good chance though that you've encountered some wisdom about socio-technical systems without even realizing it.

**4:17** · Have any of you ever heard of Conway's law?

**4:19** · Yes, of course.

**4:20** · Everyone has heard of Conway's law.

**4:22** · But briefly, Conway's law goes like this.

**4:24** · Organizations build technologies that mirror their internal communication structures.

**4:29** · Or informally, if you have a four-team group working on a compiler, you're going to get a four-pass compiler.

**4:34** · That's just how it works.

**4:36** · Now at its core, Conway's law is an observation that the way we build technology is inseparable from the structure of the organizations that build it.

**4:43** · The organizations shape what gets built. Now of course, it's not just the organizational structure that impacts our developer ecosystems.

**4:52** · The values and culture of an organization can have just as profound an impact.

**4:57** · Your ecosystem builds what your organization incentivizes your engineering culture creates the environment around your developer ecosystem.

**5:06** · See, the thing is, once you learn about socio-technical systems, you see them everywhere in software development, from your architectures, to your postmortem culture, to code review, to security policy.

**5:16** · They're everywhere.

**5:17** · The things we build and the way we choose to build them are a reflection of what we value.

**5:22** · If we're thoughtful, we can use that knowledge to amplify our values and put them into the things we build, boosting the kinds of outcomes that we want.

**5:31** · So now I think I can properly define for you, software ecology.

**5:35** · Software ecology is the holistic study of the socio-technical ecosystems that produce software.

**5:42** · All right.

**5:43** · Now we're all caught up.

**5:45** · It's OK if all that felt a little abstract, by the way, because now we're going to look at a real example.

**5:50** · We're going to talk about Google's developer ecosystem.

**5:53** · Google has a very large, and I would argue somewhat complicated, developer ecosystem, because over the last 25 years, we have evolved truly remarkable capabilities and, yes, a little complexity.

**6:05** · Now as an upfront disclaimer, I'm talking about Google, partly because I work there.

**6:09** · But it is the developer ecosystem I understand the best.

**6:11** · My intent here is not to tell you, you got to go do what Google did.

**6:14** · That's not going to be good for you.

**6:16** · You're a different company.

**6:18** · You're in a different place.

**6:19** · You have a different set of trade-offs you're worried about.

**6:22** · Now like any engineering organization, Google has made a lot of choices.

**6:25** · They were very specific to the needs we had at the time we were building our ecosystem.

**6:30** · Your situation is different.

**6:32** · So a few years ago, we wrote a book.

**6:34** · Maybe some of you have seen this book before?

**6:36** · Internally, we call it the Flamingo Book.

**6:38** · We wrote this book to give people an understanding of how Google actually worked inside.

**6:42** · And we spent half this book talking about things like version control and testing.

**6:46** · But the entire first half of this book was spent on engineering culture.

**6:49** · And we used to get a lot of questions about that.

**6:51** · Why so much on engineering culture?

**6:52** · Well, the reality is, if you don't understand the culture that Google has, you can't appreciate why we have the technical choices that we've made.

**6:59** · These things are interlinked.

**7:01** · Now in case you didn't read the book, I'm going to give you a brief tour.

**7:04** · Don't worry.

**7:05** · You don't need to read all this.

**7:06** · Yes, take pictures.

**7:06** · That'll be fine.

**7:08** · There's a few things about Google that make it somewhat unique.

**7:10** · So for example, we're deeply engineering-led.

**7:12** · Engineers are always in the room when important decisions are being made.

**7:15** · We're big on transparency.

**7:17** · We try to make all the docs and code that we can available as often as possible.

**7:21** · We encourage people to be helpful.

**7:23** · In fact, if you talk to anyone who's ever left Google, the helpfulness of their colleagues will be one of the most important things they cite.

**7:29** · We treat code review as an opportunity for mentorship and not test grading.

**7:32** · We're big on standardization, real big on it.

**7:35** · We believe in continuous improvement.

**7:37** · We're big into blameless postmortems.

**7:40** · We're big on the idea that sustainability is better than heroics and that automation is better than toil.

**7:45** · Now we don't always achieve all of these ideals.

**7:47** · But this is kind of what we're aiming for culturally.

**7:50** · And on the technical side, we have our monolithic repository you've probably read about.

**7:54** · I'll tell you more about that in a second.

**7:56** · We have trunk-based development, where every change lands at head every time.

**8:01** · When you build a binary at Google, almost every line of code is built from source.

**8:04** · That's pretty wild, right?

**8:06** · We have a universal build tool chain.

**8:07** · Everybody uses it.

**8:08** · We have a global test automation platform.

**8:10** · One place runs all the tests, billions of tests a day.

**8:13** · We have a global signal for the last green.

**8:15** · I can tell you the state of any build, looking at one simple internal website.

**8:19** · We have a uniform compute environment.

**8:21** · So it works on my machine isn't possible, mostly.

**8:24** · We have opinionated developer frameworks and a small set of core languages.

**8:28** · And it's this mixture of culture and technology that give rise to what Google is.

**8:33** · You can't understand one half without the other.

**8:36** · Now if I had to pick one principle, one principle that seems to have guided us implicitly, if not explicitly at times, it's this thing called shared fate.

**8:45** · Now, shared fate is a term that describes the degree to which an ecosystem and its components are tightly linked to each other.

**8:51** · In a high shared fate ecosystem, one component can affect everything else, right?

**8:57** · Now in a developer ecosystem, shared fate is as much a technical choice as a social one.

**9:02** · You can't just get shared fate by making everyone use the same technology.

**9:06** · You also have to develop social contracts for how you're going to manage that technology.

**9:09** · Now at Google, our shared fate starts with our monolithic repository.

**9:15** · Every line of code at Google, with a couple notable exceptions like Android and Chrome, is in one shared repository, everything.

**9:22** · Everything is committed to trunk.

**9:23** · There are no branches.

**9:24** · There are no versions-- everything in one place.

**9:27** · This kind of shared fate allows us to apply a security patch in one file and know that, within a week, every application in the company will have been patched.

**9:35** · That's like a superpower, right?

**9:37** · 10 lines of code in the right place can patch 10 billion lines of application and system software.

**9:45** · That's pretty impressive, right?

**9:47** · Now, shared fate isn't always a good thing.

**9:51** · Shared fate is a choice.

**9:52** · There are places where shared fate might make less sense.

**9:55** · For example, in our production environment, we don't want one service to take down all the other services or one cluster to infect an entire region.

**10:03** · So we have worked really hard.

**10:04** · Google in particular has worked really hard to make sure we don't have the dangerous kinds of shared fate that cause things like cascading failures.

**10:11** · Again, the point is, shared fate is a trade-off.

**10:13** · You have to figure out the right place to put it, and then make sure that it works well for you.

**10:18** · Now one of the most interesting emergent properties of our shared fate environment is this notion of large scale changes.

**10:25** · Now long before AI, way before AI, Google's internal tools have made it possible for a single developer to change literally millions of lines of code-- millions of lines of code, code they will never look at.

**10:37** · They will never see again.

**10:39** · They might know nothing about it.

**10:41** · We've built tools that make that automatically possible, today.

**10:44** · And we've been doing it that way for at least the last 15 years.

**10:47** · This kind of capability has let us to evolve our monorepo over time.

**10:50** · We can update languages and frameworks.

**10:53** · It's really what keeps our internal environment from becoming stagnant.

**10:56** · It's no exaggeration to say that, without it, we wouldn't be the Google that we are today.

**11:00** · And the folks who work on those tools would tell you.

**11:03** · It's an unsung hero's kind of job to keep this company moving at the speed it needs to move.

**11:09** · The thing about large scale changes is, you can't appreciate them unless you understand the cultural components and the technical parts of our ecosystem that make it possible.

**11:17** · For example, you need a widespread testing culture.

**11:19** · Everybody needs to be writing tests for me to be able to do this.

**11:21** · We need to have a single platform so I know where to look to get the results of those tests, right?

**11:25** · It's good to have common build tools so we're all building the same software.

**11:28** · I build it.

**11:29** · You build it.

**11:29** · We get the same outcome.

**11:30** · We need a standard set of libraries.

**11:31** · So as we're swapping things out, we're not jumping around, trying to find which version of this library is working for you and not me.

**11:37** · We need standardized code review.

**11:38** · We need transparency in the monorepo itself, so I know which code needs to be changed.

**11:43** · LSCs are truly the ultimate manifestation of this automation over toil ethos at Google.

**11:48** · And it's only possible because of the entire ecosystem.

**11:51** · You can't point at one part of our developer environment and say, that's why LSCs happen.

**11:55** · It's everything linked together.

**11:57** · Now, every developer ecosystem, yours, anyone you've ever worked in, they have these emergent properties.

**12:03** · They're usually the things that feel somewhat unique to the place that you work.

**12:07** · And that's because they're usually the result of the constellation of choices you have made to shape how you want to work.

**12:13** · So every ecosystem has something like this.

**12:15** · Google has large scale changes.

**12:16** · You have something else.

**12:18** · Google's developer ecosystem, embedded in our specific engineering culture, has produced a unique set of trade-offs.

**12:25** · They serve our technical and business goals.

**12:27** · However, Google's ecosystem, like every ecosystem, cannot excel at all tasks.

**12:32** · We've chosen to optimize for extreme scale, security, performance, right?

**12:36** · And we'll do that typically even if it comes at the expense of developer productivity sometimes.

**12:41** · That's a trade-off we're willing to make in our ecosystem.

**12:44** · The developer ecosystem of other places, like, say, a five-person startup is going to look different.

**12:48** · And that's OK.

**12:49** · In a five-person startup, velocity and agility are the most important things you can possibly have.

**12:54** · Somewhere in between a five-person startup and Google is where you are, right?

**12:58** · Most of you are inhabiting an ecosystem that's somewhere between five people and 200,000.

**13:03** · The trade-offs you're going to make are really important to pay attention to, because when you look at the trade-offs being made, you can begin to understand the values of the organization.

**13:10** · What does it really care about?

**13:12** · Not what does it say it cares about, but what does your organization actually care about?

**13:16** · And when you understand those values, you can begin to shape the transformation as it begins to unfold.

**13:21** · We're all experiencing a lot of transformation right now.

**13:23** · So it would be good to understand where we're going.

**13:26** · I hope by now, the concept of a software ecosystem is a bit more clear.

**13:30** · And I think it's time we talk about the token-eating elephant in the room.

**13:34** · What does an AI-first developer ecosystem actually look like?

**13:38** · Now it would be nice to build one of these out from scratch, a greenfield ecosystem.

**13:43** · But I would bet none of you have that luxury, right?

**13:46** · You all have to continue shipping software, doing what it is you're doing today, while you're replacing literally every part of it.

**13:51** · No big deal, right?

**13:53** · Your company is depending on you to continue delivering value and make sure that nothing breaks.

**13:58** · So to make sure nothing breaks, let me ask you a question.

**14:01** · How well do you understand your developer ecosystem today?

**14:04** · Can you map it all out?

**14:07** · Do you know where all the pieces are, not just the technical ones, but the social ones?

**14:10** · Can you enumerate what your ecosystem is actually built from?

**14:13** · How well do others in your organization understand it?

**14:16** · What are its strengths or its weaknesses?

**14:18** · Where are your bottlenecks?

**14:19** · Where are you constrained or where are you free?

**14:22** · What optionality do you have?

**14:23** · What kind of emergent properties have you seen in your own ecosystems?

**14:26** · And perhaps most importantly, if your ecosystem suddenly had to grow by, I don't know, 10 to 15x in the next 18 months, do you know what would break first?

**14:36** · See, the thing about that last question is we're all going to have to answer it real quick, because every developer ecosystem on Earth is going through a radical transformation.

**14:46** · Maybe it hasn't gotten to everywhere you are yet.

**14:48** · But it's coming.

**14:51** · Every single developer ecosystem is going to have to wrestle with this idea of this 10x moment.

**14:56** · I wish I could tell you there was a way out of this.

**14:58** · But it's coming.

**14:59** · These are incredible times.

**15:01** · But they are also somewhat confusing.

**15:04** · All the trade-offs we have deliberately evolved over the last 25 years are going to get re-balanced.

**15:08** · You've heard that from probably every speaker here in some form or another.

**15:11** · We don't know yet what the future is going to be.

**15:13** · We're trying to figure it out.

**15:14** · Some folks are predicting productivity that looks like 10x, 100x.

**15:18** · We're measuring things in orders of magnitude.

**15:21** · That's a lot.

**15:23** · Suddenly, the question of 10x growth is not just a thought exercise.

**15:27** · It's like a code red moment for you and your company.

**15:29** · You're going to have to figure this out, if not today, certainly in the next 12 months.

**15:34** · Now before I go much farther, I really want to stress that I understand, there's a big difference between generating code 10 times faster and engineering 10 times faster.

**15:43** · These are different things.

**15:44** · And in fact, at Google, we often say that engineering is programming integrated over time.

**15:49** · But the thing is, we're speeding up programming a lot.

**15:52** · We're making the code machine go fast.

**15:54** · So we're going to have to figure out how we engineer around that code machine in order to deliver real results to our customers.

**16:01** · No one knows yet how far we can push this productivity growth.

**16:04** · I really don't know.

**16:05** · We could stop next week.

**16:06** · I don't think so.

**16:07** · But one thing's for sure.

**16:08** · We're going up from here.

**16:11** · The problem is, I think we have a lot of work to do, because I would bet very good money that what we're doing today doesn't work at 10x.

**16:17** · I would bet, the way you're building software, the way I'm shipping software, doesn't work at 10 or 100x velocity.

**16:22** · Something's going to have to change.

**16:25** · Well, let's start by looking at a standard developer ecosystem.

**16:28** · It's simplified.

**16:29** · I know.

**16:29** · Hopefully you'll recognize some of these terms up here.

**16:31** · But let me put them in a form you're more used to seeing them, a complex graph, right?

**16:35** · In a world with 10x more productivity, or 10x more activity, rather, what has to change?

**16:40** · Well, let's start with the nodes related to getting code into the code base.

**16:43** · Now, notably, I've excluded testing and version control.

**16:46** · We'll get to those in a second.

**16:48** · What happens if the green nodes suddenly have to do 10 times more stuff?

**16:52** · Well, let's start with writing source code.

**16:55** · If everyone gets a lot faster at writing code, there's probably going to be a lot more of it, right?

**16:59** · That's not good.

**17:00** · Now seems a very good time to remind you of an old Jeff Atwood quote.

**17:04** · Software is a liability.

**17:07** · So right off the bat, 10x more code, 10x more liability.

**17:11** · We're not into a good place.

**17:13** · By the way, you've probably noticed that you can't just hand everyone a bunch of tokens and say, good luck.

**17:17** · So I hope you're investing in retraining.

**17:19** · You are investing in retraining, right?

**17:22** · Do you know where all your engineering practices are documented?

**17:24** · Would you know how to evolve them if you had to?

**17:27** · OK.

**17:27** · Well, something to think about when you get home.

**17:29** · Let's move on to the build system really fast.

**17:31** · At a minimum, more code is going to mean more compile time.

**17:35** · Bigger system, more compile time, just what we needed.

**17:38** · I'm sure no one at your company has ever complained about slow compiles.

**17:41** · Well, guess what?

**17:42** · They're going to get slower.

**17:43** · And if agents are driving a lot of work, that means more compiles-- so not just bigger, but more.

**17:47** · Compilation isn't free, in time or compute.

**17:50** · And it's possible you have never noticed how much time you spend on compilation.

**17:54** · But I can assure you, 10 times larger, you're going to notice something.

**17:58** · What about the design of all that code?

**18:00** · Do you have the right agentic skills to encourage decoupling?

**18:03** · What about the right server frameworks to ensure that you can compose capabilities quickly and safely?

**18:08** · Come to think of it, do you know how many ways web applications are served in your company today?

**18:12** · Do you know how many different server frameworks are actually running?

**18:16** · I don't, actually.

**18:18** · How are you going to manage component reuse if agents are writing all of that code?

**18:22** · Maybe you're betting it won't matter.

**18:24** · Don't be surprised though if agents write code that is easy to write and hard for you to maintain.

**18:29** · That seems to be the benchmark right now.

**18:31** · Agents are good at writing code.

**18:32** · But they're not always thinking long term the same way you and I need to.

**18:36** · That code, I'm sure, won't be well-factored.

**18:38** · That's OK.

**18:38** · We'll figure that part out.

**18:39** · But the truth of it is, agents are doing a lot of work for us now.

**18:45** · And we're going to have to figure out how we apply that most effectively, every single day.

**18:51** · At some point, all that agentic work could make your binary so big, you can't compile them anymore.

**18:57** · Or maybe they get so big, you can't ship them on phones anymore.

**19:01** · Have you ever asked the question, what is the largest binary you can compile?

**19:06** · I actually don't know what the answer is.

**19:07** · But I know we're bumping into limits at Google.

**19:09** · We're getting our binary so big in some places, we can't compile them anymore.

**19:13** · We'll figure it out.

**19:14** · I'm sure of that.

**19:15** · But the truth is, big has lots of consequences.

**19:18** · Scale has impacts everywhere.

**19:21** · Now perhaps you're more of a microservices shop.

**19:23** · And you're looking at me, going, why would I ever build a service that big?

**19:26** · All my services are tiny.

**19:28** · That's cool for you, except now I have a question.

**19:30** · What's going to happen with 10x more network traffic, 10x more services, 10x more chatter, 10x more network traffic?

**19:36** · Are you ready for that?

**19:37** · No one gets out of this unscathed.

**19:40** · Scale has effects everywhere.

**19:43** · Now let's say you can't reliably compile all this code.

**19:45** · I'm sure you can't, right?

**19:46** · What happens to your code review process?

**19:48** · Everyone is worried about code review right now.

**19:50** · And I think that's for good reason.

**19:51** · We're putting a lot of pressure on this very human process.

**19:56** · And in many cases, it is becoming a bottleneck.

**19:58** · And one thing I know about people, they do not like to be bottlenecks.

**20:02** · They act funny when you put pressure on them.

**20:04** · With 10x more code, you're going to get one of two things, 10x larger changes or 10x more of them.

**20:09** · So what does that mean for your code reviewers?

**20:11** · Well, I'd be willing to bet most of your tech leads cannot sustain the review velocity necessary to see, I don't know, even five of these 10x developers through a day.

**20:19** · That's a lot of work.

**20:21** · So what they're going to do in order to not become a bottleneck is they're going to start rearranging their process.

**20:26** · They're going to start cutting corners to make sure they don't block anyone, because no one wants to be a blocker.

**20:31** · Now you may be able to solve part of this with AI.

**20:33** · I'll give you that.

**20:34** · You may be able to deploy AI to make your review process better.

**20:37** · OK.

**20:38** · But that only solves part of your problem, because if the people on your team aren't writing code, then the only time they're encountering it is during review.

**20:45** · But they're not paying as much attention during review.

**20:47** · That's what we just said.

**20:48** · So who's paying attention to the code base as it evolves?

**20:51** · Well, no one.

**20:52** · Pretty soon, your code base is going to be a mess that no one can understand.

**20:57** · Now in addition to all that source code, we have to think about token management because tokens are expensive, as some of you probably know.

**21:04** · At scale, tokens are a real cost we have to factor.

**21:07** · What happens if everyone in your company starts using 10 times more tokens or 100 times more tokens?

**21:11** · Or what if you accidentally spend your monthly budget in a day, a thing that has happened to a friend of mine.

**21:17** · If you had to prioritize where you're going to put that spend, do you know where you'd put it?

**21:21** · Do you even have the visibility to know where the tokens are going right now?

**21:25** · See, even in just the first few nodes of this system, this simple system, we're already finding problems.

**21:30** · And it is very clear that there's going to be some challenging second order impacts.

**21:34** · Now let's move on to testing and version control.

**21:36** · These are a little bit special.

**21:38** · Have you ever looked at how much compute your testing infrastructure takes?

**21:41** · I do not know about you.

**21:42** · But at Google, I never have fast enough tests.

**21:45** · I've never said, boy, my tests are going faster than I needed to today.

**21:48** · I don't have enough capacity as it is.

**21:51** · Every change that lands in version control has to be tested, though.

**21:54** · But also, agents love running tests because it tells them whether or not they're doing good work.

**21:58** · So again, the agents are doing additional work.

**22:00** · And I have more work to do.

**22:02** · So with 10 times more commits and agents doing all that work, now how much test compute are you using?

**22:08** · Actually, it turns out it could be worse than that, because what we've seen at Google is that as your code base grows, your dependency graph grows quadratically, not linearly, with the size of your code base.

**22:19** · So if your code base is 10 times larger and you're trying to test all the dependencies so that you're sure nothing will break, you may have upwards of 100 times as many tests running.

**22:28** · Maybe it's 1,000 times as many tests running.

**22:30** · That's going to be a really interesting challenge.

**22:32** · And it's going to be a line item in your budget at some point.

**22:36** · That's something you should be thinking about.

**22:39** · So now you're not just running tests more often.

**22:42** · They may be 100 times bigger.

**22:44** · And quite frankly, if they're not going to get that big, if you're not worried about how much test compute you're spending, I'm more worried, because that means you probably don't have enough tests to begin with.

**22:52** · And those agents are YOLO-ing all over your code base with no way to know what is working, all right?

**22:58** · Now let's assume you figure that out.

**23:00** · You've solved compile.

**23:00** · You've solved testing.

**23:01** · Let's talk about your version control system.

**23:03** · Most popular version control systems are not optimized for performance, not at all.

**23:08** · They're optimized for consistency, ordering.

**23:12** · That's their job.

**23:13** · Their job is to keep a complete record, not to go real fast.

**23:15** · What's the performance of your version control system?

**23:17** · How many commits can it take a minute?

**23:20** · I assure you, it is less than you think.

**23:22** · It's not going to scale to 10x the velocity that you need it to.

**23:27** · When was the last time you even thought about the performance of your version control system, ever?

**23:33** · Not unless you work on Git, right?

**23:34** · Honestly, if we're talking about version control performance, something has gone horribly wrong.

**23:39** · We are in the bowels of the developer experience here, the bowels.

**23:43** · But that's what happens when you see systemic change.

**23:46** · Systemic change finds every corner of your system and says, hey, you paying attention?

**23:50** · Because here's something that you weren't expecting.

**23:53** · And by the way, for those of you who think you're going to solve this version control problem with a lot of little repos, I got some news for you.

**23:58** · Talk to anyone who's run that strategy who has hundreds or thousands of little repos.

**24:02** · And I can assure you, it's just an entirely new set of challenges, none of which AI is going to necessarily make easier for you.

**24:09** · So far, we've hit problems in every node we've looked at.

**24:12** · And believe it or not, we've only looked at the relatively easy to find capacity nodes.

**24:15** · These are all things you could just find.

**24:17** · You just take a number, multiply it by 10 and ask, will that go good or bad?

**24:21** · There's a lot of other unexpected challenges.

**24:22** · So we're going to go through a really quick list of some things I think you want to be worried about.

**24:27** · So first, validation beyond just your compute.

**24:31** · The validation strategy you use today is probably something like a lot of unit tests and maybe some integration tests.

**24:36** · But with 10x more code and 10x more services, integration tests are going to become the most important part of your quality strategy.

**24:42** · How many of you are happy with your integration testing setup today?

**24:46** · I will note for the live stream, there is not a single hand up.

**24:49** · OK, good.

**24:49** · That's what I thought.

**24:50** · I am also not happy.

**24:52** · Integration testing is really hard.

**24:53** · And I do not have the tools to do it the way I would like to right now.

**24:57** · Then you have this problem that I refer to as the conjunction of Booleans.

**25:00** · In order to ship software today, you request that every test pass.

**25:03** · All the Booleans turn green.

**25:05** · Everything is good before you ship.

**25:06** · That's a reasonable thing to do.

**25:08** · What happens when you have a million tests?

**25:09** · And the actual reliability of the underlying test infrastructure to run a million tests is in question.

**25:14** · It might not be possible to ship software where every Boolean has to be true.

**25:18** · So now you're going to need a new strategy, probably something statistical to figure out, what are the right tests to run?

**25:23** · Because I can't run everything.

**25:26** · OK.

**25:26** · What about super, extra large changes?

**25:28** · It's really exciting that we can refactor and change languages and frameworks, everywhere.

**25:31** · Everyone can do it.

**25:32** · Do you have the workflows or the social contracts to enable people to manage merge conflicts that are measured in the tens of thousands of lines, hundreds of thousands of lines, millions of lines?

**25:41** · Probably not.

**25:42** · So we're going to need to figure out, how do we build the workflows that support very large change sets moving past each other?

**25:48** · If everyone at the company can do it, we're going to need a new strategy.

**25:52** · And by the way, have you ever seen an agentic edit war where one edit, an agent makes a change.

**25:57** · And then another agent comes in and says, no, I don't like that change.

**25:59** · Let's do a different change.

**26:01** · Now, it's funny to watch until you realize you're paying for the tokens on both sides of that, right?

**26:07** · Let's move on to release.

**26:08** · How many times do you release to your customers today, daily?

**26:11** · If you're doing daily, you're doing pretty good.

**26:13** · If you're not, here's a problem for you.

**26:15** · You're going to get 10x more software.

**26:17** · And that software has to land somewhere.

**26:19** · And if you're not releasing daily, my guess is that each change is now going to get a lot bigger.

**26:24** · And if there's one thing my SRE friends will tell me, it is that very large changes are very scary.

**26:29** · Let's not do that.

**26:30** · But the code has to go somewhere.

**26:31** · It needs to get deployed to be valuable.

**26:33** · So one thing you're probably going to try to do is release more frequently.

**26:37** · And that's good.

**26:37** · Our friends at DORA would be proud.

**26:39** · They would say, yes, please release more.

**26:40** · But at some point, you're going to release diminishing returns.

**26:43** · Releasing every second is probably not going to provide a lot of value to you.

**26:47** · So somewhere between releasing every second and I'm not quite to releasing a day is the right balance.

**26:51** · But still, the code will grow.

**26:53** · And we're going to need to figure out, where do we put that code so that we don't create more risk?

**26:59** · How about your internal APIs?

**27:01** · We've been talking about building software.

**27:03** · But what about the internal developer environment with all the APIs and data?

**27:06** · What I've been telling my friends that I work with is, all of your APIs suddenly just became public.

**27:11** · They need the same kind of hardening that you would put on anything that you're going to send out to the public internet.

**27:16** · Why?

**27:16** · Because agents aren't going to negotiate with you.

**27:19** · They're going to find an API.

**27:20** · They're going to start calling it.

**27:21** · And if they can get access to your data, they're going to do it.

**27:23** · I guarantee it.

**27:24** · If an agent can access a data set, it's available to them.

**27:27** · So if you haven't put the same thought into your internal data sets and your internal APIs, you're going to run into some very interesting challenges, because agents are going to find things you probably didn't want them to.

**27:36** · Well, how about Jevon's paradox?

**27:37** · This is a word we all learned in the last probably 12 months.

**27:40** · No one knew what this was or even how to pronounce it.

**27:42** · But now we all know about Jevon.

**27:43** · Jevon says, the cheaper and more efficient a resource gets, the more we use it.

**27:47** · And, boy, do you see that with tokens.

**27:49** · We are putting them everywhere.

**27:50** · And it's changing how we work and how we think about how we work.

**27:53** · We're now optimizing-- or not optimizing.

**27:55** · We are putting a cost on previously-hidden productivity work that was invisible before.

**28:00** · So what is that going to do to the way we behave?

**28:03** · I don't know yet.

**28:04** · By the way, you need to be careful where you put those token engines.

**28:08** · If you put load-bearing token engines in place, weird things can happen.

**28:12** · For example, what if your rollback process depends on an agent to have enough capacity?

**28:16** · If someone ran that agent out down the end of its token budget and now you can't roll back, that's probably a bad thing.

**28:22** · And speaking of rollbacks, do you guys know why rollbacks work today, basically?

**28:26** · It's because you release software slightly slower than it takes you to detect a problem in production.

**28:32** · If you can release software really, really fast, faster than you can detect anything is wrong, what does that mean for your rollback posture?

**28:39** · Every rollback will now have to contend with multiple conflicting changes landing on top of it.

**28:43** · So it's not just enough to release faster.

**28:45** · We have to consider the whole system, the rollback as well.

**28:47** · That's a really important safety valve.

**28:49** · How about the idea that everyone's a builder?

**28:51** · This has been a big conference for celebrating the idea that everyone's a builder.

**28:54** · And I think it's cool.

**28:55** · Democratizing engineering is cool, until you realize you have democratized engineering.

**29:00** · You know that tool that you don't like, that you wish you could replace at your company?

**29:05** · I don't care what it is.

**29:06** · And I won't name names up here.

**29:07** · But I'm sure there's a tool you just wish I could vibe code up a replacement for.

**29:10** · OK.

**29:11** · Multiply that by everyone at your company for every tool they use.

**29:14** · What happens to the social fabric of your company when everyone is using completely different tools?

**29:18** · Now if you're lucky, you have a common data substrate.

**29:20** · That's a good thing.

**29:21** · Then all the data is going into the same place.

**29:23** · But what if you don't?

**29:24** · Everyone's a builder is cool, until you have to maintain all the stuff that everyone built.

**29:29** · And let's spare a thought for the technical leadership speed run we're going to put all our junior developers through.

**29:34** · The reason that it takes so long to become a lead is because you have to build intuition and judgment and expertise to help you make calls, because when you're leading a team, there's a blast radius that is much larger than when you're just doing it yourself.

**29:46** · When a new grad steps into an environment where they have 50 agents at their disposal, but none of the intuition and none of the judgment, what's going to go wrong?

**29:54** · How do I teach 10 years of experience in six months?

**29:57** · I don't know yet.

**29:59** · And this last one you've heard a lot about, especially in the last talk if you were here.

**30:03** · Human attention is the most precious resource we have.

**30:06** · And right now, there's a lot of noise.

**30:07** · There's so many agents, so many things demanding our attention.

**30:09** · We're going to have to figure out how to manage this, because we don't know how to do it really well right now.

**30:13** · We've benefited from the fact that we couldn't make more trouble for ourselves than we could pay attention to.

**30:17** · And now that is not the case.

**30:20** · All right.

**30:20** · So that seems like a lot.

**30:21** · That's because, in a system, everything is connected.

**30:24** · All the challenges I just mentioned, by the way, you can't resolve any of these by just looking at a single node in the system.

**30:30** · You have to look at the whole system.

**30:32** · In order to adapt to agentic development, I think we're going to all have to start learning to think in systems all the time.

**30:39** · So I'm not going to go through all of these.

**30:41** · Take a screenshot of it if you want.

**30:43** · But when you're thinking about systems, these are the things you should be worried about, things getting bigger, the effects over time.

**30:49** · Which direction does causality move?

**30:51** · Which nodes are talking to all of their neighbors?

**30:53** · What does emergence look like?

**30:55** · What are the things that are coming out of nowhere?

**30:56** · What about the incentives, both the social and the technical?

**30:59** · And that's right.

**30:59** · Technical systems can have incentives, too.

**31:01** · But be careful of the incentives in your ecosystem.

**31:03** · Capacity, I've said it a couple of times.

**31:05** · I'll hear it at least one more time today.

**31:07** · Feedback loops and bottlenecks, these are the tools of systems analysis.

**31:11** · Now, it may seem complicated.

**31:13** · But you really only need two questions, why, and what if?

**31:17** · Why do we have so few integration tests?

**31:19** · What if we had more integration tests than unit tests?

**31:22** · Why do we use these specific programming languages?

**31:25** · What if AI writes all the code?

**31:27** · "Why" is the drill that you are going to use to bore into the heart of your system to figure out how it works.

**31:32** · "What if" will challenge what you find.

**31:35** · And it will require you to flex your imagination a little bit.

**31:38** · All of you are probably very good at asking why.

**31:40** · I can see it in your faces.

**31:41** · You guys know how to ask why.

**31:43** · Why are we doing this?

**31:44** · Why are we doing that?

**31:45** · But, "what if", "what if" is more challenging.

**31:48** · "What if" can be scary, if we're asking you to abandon the practices you thought were really well-designed for the problems that you had.

**31:54** · "What if" can be scary.

**31:55** · What if we didn't test this way?

**31:57** · What if we didn't write tests at all?

**31:59** · Let's not get carried away, right?

**32:01** · But if you allow it to be, "what if" can also be pretty exciting.

**32:05** · Now while you're thinking about where these opportunities are, I want to talk to you about a pattern that I've seen.

**32:11** · It's this pattern that AI acts as an amplifier.

**32:13** · As soon as I learned about this, I started seeing it everywhere.

**32:16** · Now I can't take credit for that idea.

**32:17** · That actually comes from my friends at DORA.

**32:19** · And their report last year on AI development, they found this sort of relationship among teams that have really figured stuff out.

**32:27** · They figured out how to make AI an amplifier.

**32:30** · AI can do more.

**32:33** · AI can get you more tests, more documentation, more code, but also more confusion.

**32:37** · That's because amplification is a magnitude and not a direction.

**32:40** · AI doesn't care where all of that stuff goes.

**32:43** · It's just going to give you more of it.

**32:45** · What DORA really found was that teams that had good fundamentals could apply that amplification in useful directions, which begs the question, how are you feeling about your fundamentals?

**32:54** · How is the decision making culture in your company?

**32:57** · What could you do to improve it?

**32:58** · What about your technical strategies?

**33:00** · Is anyone looking at developer productivity?

**33:03** · How well do people in your organization collaborate today?

**33:05** · What's your security posture look like?

**33:07** · How's your code health, your release hygiene, your reliability?

**33:11** · AI doesn't solve any of these problems for you, by default.

**33:14** · It can amplify the practices you have, if they're good.

**33:17** · But if they're not good, it's going to cause more trouble.

**33:20** · But even with solid fundamentals, we're in for a real ride.

**33:23** · My guess is-- this is a guess.

**33:25** · You can come check me on it later.

**33:26** · In 2030, our developer ecosystems today are going to feel like 2001 does to us now.

**33:32** · And I should point out that, in 2001, we were shipping software on CD-ROMs, right?

**33:36** · That's how far away we might be in 2030.

**33:39** · Now as you continue to build your fundamentals, let me give you some other things you can think about along the way.

**33:43** · First and most importantly, you need to know about infrastructure capacity.

**33:47** · You can't deploy the AI and you can't deploy the compute if you don't know how much resource you have to spend.

**33:51** · You need a good way to keep track of this.

**33:53** · Next, you need validation, because you can't, or at least you shouldn't ship software that you haven't validated.

**33:57** · But like I've said before, validation is going to change.

**33:59** · So you're going to need a validation strategy.

**34:02** · Now's the time to figure that out.

**34:03** · Beyond that, you need isolation, because you're going to get a lot of code for a lot of different purposes that, previously, we didn't use code for.

**34:09** · That's OK.

**34:10** · But you don't want that cool prototype code to actually find its way into production.

**34:13** · So you need to worry about isolation.

**34:15** · You need to make sure the fun stuff doesn't impact the money-making stuff.

**34:18** · And then, finally, you need to worry about abstraction.

**34:21** · We build abstractions to keep developers from making bad choices.

**34:24** · That's why we build libraries and frameworks and whatever.

**34:26** · We wouldn't build a web server from scratch today.

**34:28** · There's frameworks-- because there's a lot of ways to get things wrong.

**34:31** · Well, asking agents to make a lot of decisions leads to the same consequences.

**34:34** · So we need good abstractions for the agents to hold on to.

**34:37** · Don't give them bad choices.

**34:38** · Now you're going to have to accept that engineering practices are not sacrosanct.

**34:42** · Practices change.

**34:43** · It's the principles that matter.

**34:44** · And it's easier said than done.

**34:46** · I get that, especially when some of our principles feel like practices.

**34:49** · They feel like they're all the same thing, like testing.

**34:52** · If you've never really thought about why your team tests software the way it does or why your release process works the way that it does, you're not going to be able to evolve it.

**34:59** · Understanding the principles is what's going to give you the power and the confidence to change things as we move through this 10x moment.

**35:05** · It is a fascinating time to be a software engineer.

**35:07** · I'm not going to lie.

**35:08** · Every dimension of our work is being redefined.

**35:10** · We need to flex our creativity more than ever, right?

**35:13** · We need skills to tackle problems like context management, token economics, model drift.

**35:19** · We need creativity.

**35:20** · And we can't get so hung up on the temptation to optimize everything.

**35:24** · We need to encourage exploration.

**35:27** · There is a problem that's been keeping me up at night that I know can't be solved by just optimizing it.

**35:31** · And that is, how are we going to maintain intellectual control over our code bases as we grow?

**35:35** · Intellectual control, by the way, is just a fancy way of saying, can humans reason about this thing in front of them?

**35:40** · We've been losing this war for at least the last 15 years.

**35:43** · Our largest systems are way bigger than any of us can think about today.

**35:46** · That's OK.

**35:47** · I think AI offers us an opportunity.

**35:50** · I think AI might give us the tools to actually begin to understand these very large systems as whole systems.

**35:57** · And if, for example-- or not example.

**36:00** · If by chance you don't believe me when I tell you that we've been losing this war, let me suggest an exercise to you.

**36:05** · When you go back to your team, ask everyone to draw an architecture diagram for your system.

**36:09** · See how many different pictures you get, right?

**36:11** · We have been losing this war for a long time.

**36:13** · So we're going to need help.

**36:15** · The thing is, a lot of our software systems are really brittle.

**36:18** · You can break a million line system with one bad line of code or one bad config flag.

**36:23** · That's the kind of fragile that really makes you think twice before you go about making changes.

**36:27** · One potential use of AI that I've been really excited about is this idea that I can get a continuously updated, almost interactive architectural space that I can begin to ask questions of.

**36:36** · Like, what would happen if we took capacity from here and moved it to the East Coast?

**36:40** · Or what would happen if our user growth suddenly jumped 40%?

**36:43** · Doing that for even a modestly-sized system today is functionally impossible.

**36:46** · There's just too many variables and too many things you need to know.

**36:49** · But AI can make sense of very large sets of data.

**36:51** · So I think there's something there.

**36:52** · But the thing I like about this problem is that, instead of focusing purely on making the code machine go, we're asking, how can we deepen our understanding of the things that we have built?

**37:00** · That's where I think some of the most exciting problems are.

**37:03** · Now there's no denying that change is happening really fast in our industry.

**37:06** · And it's happening at a pace probably faster than most of you have ever experienced.

**37:10** · One of the most important things all of you can do right now is offer to help someone who is struggling, right?

**37:17** · Be a helping hand for someone who has not figured this out yet.

**37:21** · We're all moving at different speeds.

**37:22** · We're all dealing with this change in different ways.

**37:25** · It is very easy to feel like you're falling behind.

**37:27** · Senior engineers, be a mentor.

**37:30** · Find the people who are stuck and help them.

**37:32** · If you have figured out your AI developer workflow, go share it with people.

**37:35** · It's not a precious secret.

**37:37** · Help the other people around you.

**37:39** · If you are a technical lead, you need to get involved.

**37:42** · You need to help steer how software engineering is happening at your company.

**37:45** · And critically, if you care about software quality or software design, you have to use your voice to advocate for it.

**37:53** · You in this room are the people who are going to do that.

**37:56** · Your bosses probably aren't, right?

**37:59** · Now at the risk of ending on a somewhat clumsy metaphor, if you imagine our developer ecosystems as living ecosystems, we have all grown accustomed to staring intently at each individual leaf on each individual branch, caring for each tree as though it were some sort of special life form.

**38:16** · However, it will not be long before we are all not just managing a tree, but an entire forest.

**38:21** · And you can't manage a forest by looking at individual trees.

**38:25** · You have to manage a forest by seeing it as an ecosystem.

**38:28** · Now here's the trouble with systemic change.

**38:31** · It has this quality of happening to everything, everywhere, all at once, of being too big for any of us to influence.

**38:39** · It can feel, right now, impossible to grab anything to steady yourself with the waves of change washing up on us, what seems like weekly.

**38:47** · But as we've just discovered, in a system, everything is connected.

**38:52** · Small actions can have big consequences.

**38:55** · Despite how it might seem, AI transformation is not the sole domain of your company's leaders.

**39:00** · They have a role to play.

**39:01** · But so do you.

**39:02** · As front-line software engineers, in this tipping point moment, you are at the heart of deciding what software engineering is going to be.

**39:10** · From your tools, to your workflows, from your engineering practices, to your engineering culture, if you can see the systems at work, you can look for leverage.

**39:18** · You have more agency than you think.

**39:20** · You really do.

**39:21** · Use that agency to create the future for your organization, for your team, and for you.

**39:27** · Thank you.

**39:28** · \[MUSIC PLAYING\]