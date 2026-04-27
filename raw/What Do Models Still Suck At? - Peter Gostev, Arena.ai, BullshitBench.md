---
title: "What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench"
source: "https://www.youtube.com/watch?v=R7A8rX-09Zw"
author:
  - "[[AI Engineer]]"
published: 2026-04-24
created: 2026-04-28
description: "What type of real world model responses do users still hate? We get to see millions of user's prompts - and we let users 'dislike both' on the Arena. We'll show you trends and examples of the tasks th"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=R7A8rX-09Zw)

What type of real world model responses do users still hate? We get to see millions of user's prompts - and we let users 'dislike both' on the Arena. We'll show you trends and examples of the tasks that LLMs still suck at despite the relentless hillclimbing.  
  
Speaker info:  
\- https://x.com/petergostev  
\- https://www.linkedin.com/in/peter-gostev/

## Transcript

**0:07** · \[music\] I wanted to talk to you something maybe a little bit controversial today. Uh you can argue with me later. Uh but the topic is what do models still suck at?

**0:24** · And uh the reason why I wanted to talk about it is that I think we uh all look at these kinds of charts where any benchmark you seem to look at line goes up and uh we look at meter charts and they surprise us every time no matter how prepared we are and this could create this kind of psychosis that we all see where everyone is freaking out about the next model. you know, we we heard some new ones coming up.

**0:52** · And the feeling I think that we all get is that this is kind of um AGI like creatures that are just almost there. Just one one more turn and they're almost there. And um I think we we could be deceiving deceiving ourselves a little bit. Um uh because I think there's still quite a few things missing. I I want to explore that in a couple of different ways and we certainly by the way see that as well in our data uh at Arena as well. So we track uh models and if you notice the date there this is uh Q2 2023.

**1:23** · So we've got data going back to GPT4 and what we do is uh we can we've tracked I think is it 700 models so far uh in text and uh what this chart is showing is what the top model is uh for at any given time for for each organization. Uh so you can see line goes up, new model uh builds on top of each other and it's all it's all very impressive. Um but I think it's it's not the whole story.

**1:53** · So I've got couple of ways how I want to explore that. It's not the the end of the conversation. There are definitely many other ways of looking at it. Um one is my own benchmark that I I've built recently which I rather like. This is the the Busher benchmark. uh and then also I'll share some of the arena's data as well that uh we haven't shared so far which I think would be interesting for you guys to see.

**2:17** · Um so uh the idea behind the \[ \_\_ \] benchmark is quite simple um is that uh what happens if you ask nonsense questions uh from the models? What they going to do? Are they going to just uh tell you that oh this doesn't make sense and maybe reframe it or they just going to go with it? Um, and I honestly wasn't sure how that was going to go, but when I just posted it one random evening, I think a lot of people liked it. It resonated with a lot of people.

**2:47** · Um, and I think it the reason is that it probably spoke to a lot of maybe a kind of slight unease people had with different models. Um, and I'll give you one example uh here. And this is just one question. And the way it works, we've got I think I've got 155 questions, something like that.

**3:05** · Um and uh we then uh give this uh to the models um uh we get a response back and all we do is then grade it uh with llam as a judge and I've been through it myself as well. I read a lot of nonsense to to kind of see that I think llm as a judge works here. Uh so this one is a kind of silly question controlling for repository age and average file size.

**3:31** · How do you attribute variance in deployment frequency to the indentation style of the code base versus the average variable name length? So hopefully you understand that's it's nonsense. So it's just it's very a breached responses. Uh they're much longer just for the purpose of this. Uh so sonet gives a good response. I think it just says you can't meaningfully measure this. It kind of pushes back. Uh gem is like a little bit more complicated because this starts off well.

**3:57** · It says that oh uh strictly speaking it doesn't really make sense but then the second part is however both act as strong proxy variables for engineering culture uh language ecosystems and code quality which I hope uh you don't agree with. So um there and I'm not going to go through a bunch of examples. It's all open source by the way. You you can uh dig it out yourself.

**4:20** · Um but uh it's really really surprised me how easy it was for the models to just go along with the complete nonsense questions. Um so the results that I got is that uh the way to read this chart is uh the green is the clear push back. So when the models like in the first example where it said oh maybe this doesn't really make sense uh then the uh

**4:44** · the amber and red there is kind of accepting the the nonsense and the basic results are that the latest set models or or rather cloud models are doing really well. There's like couple of other models like quen models not too bad. Uh there's even gro is like okay as well what the very latest one. Uh but if you go beyond that, there's a lot of models that we'll use all the time. So GPT models, uh Gemini models, they're basically kind of about 50/50 whether they're going going to go along with it or not.

**5:13** · And even looking at some of the traces and responses in more detail, even the ones that are green is still like a little bit shaky, they still kind of try to accommodate. So it's like for me, this is really not nowhere near good enough uh for the uh level of responses.

**5:31** · And just for completeness, if you go all the way, so this is the very bottom of the table. Um there are a bunch of smaller models there. Uh kind of all the models. Um yeah, some some results are completely terrible. Uh feels like you can ask anything. They they just uh respond.

**5:46** · Um, another way of looking at this data is I just took the anthropic openai and and Google there and I um measured uh the model performance over time and uh you don't see all the labels there but they're basically like all of the all of the models that you you remember them releasing.

**6:05** · Um so what the way I interpret this is that the anthropic models were like okay at the beginning but the since uh claude 4.5 uh sonet 4.5 they really went up and even haiku is is quite high uh but uh with open eye Google models they're kind of up and down but they they nowhere close uh the the top there which I think is kind of interesting um and I'll go into some of the other interesting dynamics there.

**6:35** · So for example, does thinking help? Right? So this is I always hear this when there is like a silly puzzle that the model can't do. What do you do?

**6:43** · It just all crank up. The reasoning it it solves it. If you see a look at the chart on the right, it basically is completely not true here. So reasoning often actually goes in reverse and doesn't help. It actually makes it worse. Um do model do more recent models perform better? It's kind of hard to tell for sure, but there's at least not the clear line going up. uh and I think if you exclude maybe the latest anthropic models, it's not even sure clear that the line goes up at all. Um then uh some specific comparisons for reasoning.

**7:13** · So for example uh what you see this kind of uh the uh is the same model with the low reasoning and high reasoning. Um and uh these are some examples where no reasoning performed better than high reasoning. And I spent a lot of time reading the traces of GPU 5.4. before um it's probably the most um confusing experience of of reading these uh traces.

**7:40** · And what I found was that quite often it would maybe have one line where it would question the the premise of the of of this question and then spend 20 paragraphs trying to solve it. And even if then comes back and says, "Okay, maybe this doesn't make sense," it still tries to solve it in some way. And this is uh feels uh completely crazy to me.

**8:05** · But the way I imagine and I don't know for sure, but I imagine the way the the reason why that happens is that um they were trained so much to solve the task at any cost. And I think there was probably not a lot of training to say actually maybe don't uh solve the problem sometimes.

**8:24** · I not noticed this first sometimes when you have a lot of agents running in parallel and I would sometimes forget which one is doing what and I would like ask one agent to do something that's completely the wrong project and I still go and do something and and I then I lose my mind. So yeah that's a kind of an interesting dynamic I thought about about thinking. Um then also so this is a subset for open source models only you try to see if bigger models do better. There's also no no real clear pattern.

**8:54** · So we've got the total parameters on the left then active parameters on the right and I don't know maybe you can see some patterns. I don't really see it's like kind of up and down. Um but yeah not not huge sample.

**9:06** · So don't know inconclusive at least not obviously uh is true. Um so that that was kind of one lens um looking at kind of this specific idea. uh but I want to uh take advantage of the data that that we have at Arena and and show you maybe more broader trends uh that we could uh look at.

**9:28** · Um so just in case you don't know uh much about arena what we do is we publish um uh benchmarks and the way we derive them is that users go into our platform uh they can go in the battle mode they put in a query uh and then uh they get two responses back which are from two anonymous models and then they can say which one they like better and then you get um uh then the model names only revealed then and then in uh text arena we've got nearly um uh over 5 and a half million votes there.

**10:00** · Um and we've been going since 2023 as well with this data. So it gives us really nice uh broad view. Um the reason why I think this is really useful is first of all we we do have this long trend then there is not any other benchmark that lasts so long because this one you cannot u exhaust it. It will there will always be one model better than the other. Um so that gives us a long perspective.

**10:27** · Another one is that inevitably any benchmark that you pick it's inevitably has to be condensed to like very specific question that that you're asking because otherwise it's very hard to measure. So I'm sure it's all in your experience as well when you are I don't know doing coding or whatever is your task.

**10:46** · Um the benchmarks would measure like very tiny slice of what you actually care about and and in here we don't have that problem because user can put any prompt and then they could just use the judgment to see like is that is that a good thing or not. Um, so I'm what I want to specifically focus on is is a slightly like a a odd mechanic that we have that I'm really glad that we had since the beginning. Um, is that um you can uh vote a which model is better here a or b.

**11:19** · Uh but you can also say uh when both models give a bad response and you know if you ask the right model a joke uh response is always bad. So that's a easy easy example. Didn't take me long.

**11:34** · Um so that's that's the thing to remember. So u if you just to remember one thing that will really help you for the next seven eight minutes is that um this is the mechanic. Think of it as like dissatisfaction rate. And uh what we can do is uh if you want to take battles between top 25 models. So we're kind of sampling from the top.

**11:55** · So to avoid kind of I don't know llama 8b fighting grand 3b uh we just take uh the the top set of models and then we map this kind of dissatisfaction rate uh over time and I I think this is quite interesting that we do see progress with this metric. So this kind of pre-reasoning models you can see there is like uh 20 17% dissatisfaction rate then we when we after 01 we see that drop quite a bit to sort of about 12%.

**12:29** · And then after that it carries on uh improving to to sort of about I think it's about 9% now. Um but it's so improvement is definitely there but it's not 0% which I I find interesting. I must say when I when I first got to that result I I thought like that's quite high. So 9% of the time people would get two responses from two good models and they don't like them which I think it doesn't tell the same story as all of these like crazy lines going up.

**12:54** · Um so then what we can do is we can also take um so what the previous one you saw is like average across all like six million prompts and this is the categorization of those. These are just some uh I picked out in there and you can see some interesting trends as well. So maths was like at 25 27% and then it got so much better. So that that's quite a nice uh result. Uh that matches my experience of models as well.

**13:24** · But then when you look at like creative writing okay it did get better but it like the the improvement wasn't that dramatic which I I think is is true as well. Um the category I want to focus on to really really try to zero in on the most signal is the expert category. And the way it works is that we take those uh nearly six million prompts. Then we have a a way to classify what are the most interesting the kind of the harder the more kind of real tasks that expert people do. They could be experts in different fields.

**13:54** · U but they're kind of the most um I would say high signal prompts in terms of what what uh we could uh zero in on. And then we also narrow down to the battles just between the these top 25 models. So that gets us to about 40,000 prompts. Um and then uh we can look at these uh expert categories and then um uh expert category and then we can subdivide it even further. So in here uh I've got five criterias here.

**14:22** · So again quantitative for example so it's like math physics things like that you can see this kind of really really high uh uh dissatisfaction rate in the kind of uh when is it about yeah early uh 2025 late 2024 um so but and that drops dramatically and I think that feels true to me that a lot of the models got so much better at this kind of quantitative stuff and I would also say the reason why I think the line goes up.

**14:53** · It's not that the models got worse, but I think people's expectations shift as well. The the data that we see in terms of what prompts people use at the beginning like three years ago versus now, it shifts a lot.

**15:04** · So, this is also not like a static benchmark. So, we we can really see that kind of um kind of the the battle of the expectation versus the model performance. Um, interesting as well on the bottom we've got magical, finance, and law and the lines like it is the the scale is equal across the five charts.

**15:23** · So, it's it's a little harder to see, but it's not steep, right? It's not really improved all that much. Um, I don't want to go into the magical and and law and finance fields uh because I don't know enough about it, but it does feel like it's probably true that that's not really been the focus of um of of the models necessarily. So I think maybe the performance improvements not been that high. Um so then what I did was to take all of these prompts and and classify them further into these more deeper subcategories.

**15:54** · I'm going to focus on software now and give you the kind of view of of these subcategories uh which I think also gives us like even even more detailed view just to give you a feel of sense what kind of prompts we are talking about here. Obviously a tiny sample of three. Uh but to give you a sense for so for gaming someone's asking to get them my uh detailed game design

**16:17** · uh document uh then for security someone's got autonomous system as a hobby and they want to configure uh uh the two which I don't really know what this is but then uh for agent systems uh which I I thought was interesting like actually the you'll see the the rate is quite good but the person there is asking for refine this agent so it can run daily with with no supervision. So, uh these are the kind of just to give you a feel. These are kind of real things that that people want to do. And uh we've got two charts here. On the left is from Q2 2024.

**16:48** · These are kind of dissatisfaction rate. And then on the right we've got um the uh Q1 2026. So this the most recent data and you can definitely see improvements. So if you look at the top line, this is the the uh the overall average rate and we've gone from 23 and a half% to uh 13%. So really nice improvement, but I think the improvement is not really seen everywhere. So um we can we can see this as well.

**17:19** · Uh same data but with a with a closer timeline, which I think I think is quite interesting. Um and you'll have you probably have better theories on all of the different uh categories why why that's the case. And I think by mind the case that I think people do ask a lot harder questions. So I think GPU compute for example I imagine probably it's up and down because probably people ask harder things as well. But I think gaming is an interesting category because I've tried to use um LLMs to build games.

**17:51** · Uh not that I I I mean I I use games but I don't build them. But whenever you try to build games with LLMs, it just feels like they have no idea like how to build actual games. The mechanics like all over the place.

**18:07** · They're not interesting. They're not challenging. Uh so I I do get this feeling that the performance not really um improved in some dimensions like I don't think LLMs really get games. uh even though I'm sure maybe go back two years people asking to build much simpler games this versus now uh but I wouldn't say that I'm aware of any like really good gaming benchmarks that would kind of capture this.

**18:32** · So again if you compare this to kind of line going up I think this is not kind of matching that story which which I think is quite interesting. Um and there are a bunch of uh other examples uh that that you see in there. So like what's what's really

**18:50** · the gap uh between those between these kind of crazy charts which by the way I also agree with I think they are true and and what we see on the right and I think there's something that this kind of fuzziness that we all have in our heads in our experience about the judgment that we have that we use that doesn't necessarily match all of these super narrow very welldefined very well specified tasks and I think there's much more to what work is and what white color work is and all work is that is not really captured by these benchmarks.

**19:22** · So I think we should be just careful and maybe put a bit more effort to maybe bring up also the bottom of the distribution so it's not just the very frontier gets better but also kind of the the broader distribution um gets better as well. Um so I'll I'll uh close here. Uh one thing to mention if you I think you like this kind of data go to our hugging face. Uh there's a lot that that we publish and share. We're going to do more of that.

**19:49** · Um and uh we share some expert prompts for example and some of the leaderboard stuff. Um join us if you want to build arena or if you train models. Uh we also do a lot of private tables. Um so thanks very much.

**20:06** · \[applause\] Heat. Heat. \[music\]