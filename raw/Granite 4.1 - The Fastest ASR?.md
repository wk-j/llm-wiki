---
title: "Granite 4.1 - The Fastest ASR?"
source: "https://www.youtube.com/watch?v=Tymq54Mn8SU"
author:
  - "[[Sam Witteveen]]"
published: 2026-05-07
created: 2026-05-09
description: "In this video, I dive into IBM's newly released Granite Speech 4.1 models and explore what makes them interesting — particularly the three 2B variants they've dropped and how each one makes a differen"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Tymq54Mn8SU)

In this video, I dive into IBM's newly released Granite Speech 4.1 models and explore what makes them interesting — particularly the three 2B variants they've dropped and how each one makes a different trade-off between accuracy, richness, and throughput that you'll actually care about for real applications.  
  
🔗 Links:  
IBM Research Blog → https://research.ibm.com/blog/granite-4-1-ai-foundation-models  
  
Twitter: https://x.com/Sam\_Witteveen  
  
🕵️ Interested in building LLM Agents? Fill out the form below  
Building LLM Agents Form: https://drp.li/dIMes  
  
👨‍💻Github:  
https://github.com/samwit/llm-tutorials  
  
⏱️Time Stamps:  
00:00 Intro  
00:20 IBM Granite Collection  
00:27 Granite Docling  
00:46 Granite Speech 4.1  
01:16 Granite 4.1 Blog  
01:38 Granite Speech 4.1 2B  
04:02 Granite Speech 4.1 2B Plus  
06:15 Granite Speech 4.1 2B NAR  
07:30 NLE: Non-autoregressive LLM-based ASR by Transcript Editing Paper  
07:45 Architecture  
09:45 Code Time  
12:00 Granite Speech Model Github  
  
#DellProPrecision #DellProMax #Delltech #localai #NVIDIA

## Transcript

### Intro

**0:00** · Okay.

**0:00** · So IBM has been quietly building out one of the more interesting open model families on the market with their Granite series of models.

**0:10** · And honestly, they're probably not getting enough credit for this because... It does seem in some ways that they've replaced kind of some of the things that Microsoft was doing with the Phi models and stuff like that.

### IBM Granite Collection

**0:20** · But the interesting thing is that they've got a whole suite of language, vision, speech, and embedding models going on here.

### Granite Docling

**0:27** · Now, one of the areas that has stood out well has been their Granite Vision for document understanding.

**0:33** · And that leads nicely into the DocLing models.

**0:36** · So if you're doing anything with OCR, a lot of people are finding Docling to being one of the key models for pulling sort of structured data out of PDFs, et cetera.

### Granite Speech 4.1

**0:46** · so while all of these models are actually quite interesting, in this video, I want to focus on their speech models, specifically their ASR side of this release.

**0:57** · Because this is not just one model, this is actually a suite of three separate ASR models, each with their own strengths and differences.

**1:07** · And, they really allow people to do a lot of the things that they haven't been able to do with Whisper or even with some of the other models out there like Parakeet, et cetera.

### Granite 4.1 Blog

**1:16** · Okay.

**1:16** · So let's break down what's actually in this speech release.

**1:20** · There are three models.

**1:22** · All of them are roughly 2 billion parameters in size.

**1:25** · They're built for sort of edge deployment here.

**1:28** · and the interesting thing is that IBM is kind of framing this as pick the variant based on what your bottleneck actually is.

**1:37** · So the first one up is Granite Speech 4.1 to be the base model here.

### Granite Speech 4.1 2B

**1:43** · And this is the one that currently is the leader on the Open ASR leaderboard on Hugging Face.

**1:49** · Now this model is at the top of the leaderboard with a word error rate of 5.33, meaning that it's basically getting around about 95% of the words accurate across a variety of different tasks and datasets.

**2:03** · while often you'll see really low error rates on things like LibriSpeech, et cetera, they often don't translate into sort of real-world use.

**2:12** · so this average word error rate here is actually a better guide to how the model's probably gonna perform in the wild.

**2:19** · Now, the other thing that we can take away from the Open ASR leaderboard is the RTFX score.

**2:25** · So this is basically the real-time factor.

**2:27** · So for every one second of compute, how many seconds of audio can actually be processed here?

**2:33** · And you'll see for this particular model, they're actually getting almost four minutes of audio for every one second of processing.

**2:41** · Basically means you can transcribe an hour of audio in 16 seconds or so which is pretty amazing Now this model is multilingual, but it's only supporting seven languages.

**2:53** · So you've got English, French, German, Spanish, Portuguese, Japanese for transcription.

**2:58** · on top of that, it does bidirectional sort of speech translation, so you can actually go from any of those languages into English, and from English out to a number of languages as well.

**3:10** · The model itself can handle punctuation and true casing, and it also has the ability to do keyword biasing built in.

**3:19** · So what that actually means is that you can pass in a list of names or acronyms or technical terms in the prompt, and the model will weight towards recognizing those correctly.

**3:32** · So if you've got sort of like a special spelling or something like that, this keyword biasing allows you to actually do that and get a better result.

**3:39** · and honestly, that alone can be worth it if you're transcribing sort of a lot of domain-specific content.

**3:45** · Now, the architecture for this one is pretty standard.

**3:47** · It's basically just an autoregressive model.

**3:50** · And it really sort of rounds out this model as being a very good workhorse with a low word error rate.

**3:57** · And I think that alone would justify this, but there are still two models to come.

**4:01** · So the second model is the plus model, and the key thing here is that this model allows you to add a form of diarization where you've got speaker labels, so that I can actually tell you that this is speaker one speaking, this is speaker two speaking, et cetera.

### Granite Speech 4.1 2B Plus

**4:18** · So this is actually called speaker attributed ASR or diarization.

**4:23** · And this is a huge thing that people often want.

**4:25** · For example, if you're gonna transcribe a podcast, you kind of want to know who's saying what, so that you can attribute that.

**4:33** · Now, the model itself may not actually give you the names.

**4:37** · it will give you sort of speaker one, speaker two, But it shouldn't be that difficult for you to be able to swap those out for real names to put in the final transcript.

**4:46** · the second feature is word-level timestamps.

**4:49** · So this is where every word gets a tag with the end time notated in it.

**4:54** · so they're reporting timestamp accuracy that beats a lot of the models out there, including customized versions of Whisper that were actually built to do this specific task.

**5:04** · so if you've been using something like WhisperX to get word-level timing, this model is probably something you wanna have a serious look at using.

**5:12** · There's also some nice features in here for incremental decoding.

**5:15** · so you can actually pass in a previously transcribed text as a prefix, and the model just picks up from there.

**5:22** · So for example, if we've got a really, really long, audio recording and we cut it up into, chunks, what we can do is we can have overlap in the chunks and we can then pass in the transcribed text, have it sort of take over from that and continue generating the text out.

**5:40** · This is super useful for long-form audio where you wanna keep things like speaker numbering across consistent chunks.

**5:46** · now, not everything's ideal about the Plus model.

**5:49** · You've got some trade-offs here.

**5:50** · The number of languages goes down to five.

**5:53** · They drop Japanese entirely.

**5:55** · They also dropped the ability to do the translation stuff.

**5:58** · and also the word error rate on this one is actually a bit higher as well.

**6:02** · But certainly here, if you're building any kind of meeting recorder, podcast tool, anything where the structure of the transcript matters, the Plus model is the one that you want.

**6:14** · and that brings us to the third one.

### Granite Speech 4.1 2B NAR

**6:16** · This is the Granite Speech 4.1 2B NAR, and this model is all about throughput.

**6:24** · So this is a non-autoregressive model where the other models have been doing predictions of tokens as it's going along in an autoregressive fashion.

**6:35** · This one has the NAR because it stands for non-autoregressive.

**6:39** · and to understand why that matters, you have to understand how things like Whisper, Parakeet, Canary, basically most of the other transformer-based ASR models on the market today actually work.

**6:52** · They're autoregressive.

**6:53** · they generate one token at a time.

**6:55** · Each token is sort of conditioned on the previous one.

**6:59** · and the big takeaway there is that that means that decoding is sequential.

**7:03** · Your GPU has to do this tiny forward pass one token at a time and then wait before it does the next one.

**7:09** · Now obviously the goal of how to fix this has always been to just predict the whole sequence in parallel, and people have tried that for many years.

**7:18** · Usually, it hasn't worked very well because predicting an entire transcript from scratch in one shot is pretty hard.

**7:25** · You lose the ability to condition on what you've already written Now, what IBM has done instead though, is that they've got this technique called NLE.

### NLE: Non-autoregressive LLM-based ASR by Transcript Editing Paper

**7:34** · So this is non-autoregressive LLM-based editing.

**7:39** · And what this is doing is instead of generating a transcript, they're kind of like editing one.

**7:44** · So here's how it works.

### Architecture

**7:45** · Step one is this frozen encoder that runs over the audio and produces a draft transcript.

**7:53** · And this kind of CTC encoder are pretty cheap and fast to run.

**7:57** · And it gets you most of the way there.

**7:59** · In fact, if you look at the sort of drafts, you'll see that they're usually pretty correct.

**8:04** · But where this is able to perform better than previous models that try to do it all in one shot is that they're able to actually make use of having sort of bidirectional attention, And this allows it to actually kind of edit or copy, insert, delete, replace in that original transcript as it goes through.

**8:22** · So having this kind of re-editing step of that original draft transcript allows it to actually improve the accuracy and what you're getting out here.

**8:32** · Now, where the base model runs at, a real-time factor of about 231 for the OpenASR leaderboard, and remember, that's already pretty fast, right?

**8:42** · That's allowing you to do an hour of audio in 16 seconds.

**8:46** · The model card for the non-autoregressive model, claims that if you're running this with batches on an H100, so a reasonably powerful GPU here, you can actually get a real-time factor of 1,820.

**9:00** · And that itself is kind of insane.

**9:02** · That literally means that you can be, transcribing an hour of audio in two seconds on that hardware.

**9:10** · and the amazing thing here is that you're not even taking a huge hit on the word error rate.

**9:16** · Now, of course, there are some trade-offs here.

**9:18** · Not only do you have no translation and stuff like that here, you also have no keyword biasing, so you can't sort of influence the transcript in the same way.

**9:28** · You don't have speaker attribution.

**9:30** · You don't have timestamps.

**9:31** · but if you just needed the raw transcripts of hundreds of hours of audio, this is gonna allow you to process all of that in a really insane amount of time.

**9:41** · so I think the best thing is Let's jump in and actually have a look at how we could run this on a local machine Okay, so you can see here that I am running this on a Dell Pro Max Tower T2 here.

### Code Time

**9:54** · And the cool thing about this is I have an RTX Pro, 6000 Blackwell, GPU in here.

**10:00** · So a big shout out to the people at Dell for providing the compute today.

**10:04** · and as you can see here, I'm easily able to run this plus multiple other models actually that I've got going in here and serving at the same time.

**10:13** · Now, that said, because these models are actually so small, you can run them on lots of different GPUs.

**10:19** · It doesn't need to be a super big one.

**10:21** · one thing that you will need to be aware of is to be able to do some of the fancier things for the non-autoregressive model, you're probably gonna need Flash Attention, installed.

**10:30** · And for me on my system, because I've been using CUDA 13, I've actually compiled my own version of Flash Attention to make sure that everything would fit with my system.

**10:39** · So if you're trying this out in something like Colab or something like that, you may run into some issues where, for example, if you've got one of the older GPUs like a T4, you may run into issues of trying to install Flash Attention and get that working.

**10:52** · so as long as you've got your PyTorch lined up with your CUDA, with your Flash Attention, et cetera, the code for getting this to work is actually pretty simple.

**11:01** · So you can see in here it's actually using, the Transformers library.

**11:04** · It's loading the model up.

**11:05** · it's using AutoProcessor, et cetera.

**11:08** · And then If you want to do things like the diarization or speaker attributed ASR, you can see that, okay, you need to change the prompt for going through this.

**11:16** · but then you can still do the transcribe function that they've got up here.

**11:19** · Just make sure that you've got, the right model loaded, et cetera.

**11:23** · The cool thing here is they've also got examples of code for the incremental decoding.

**11:28** · so this is basically where you pass in, the previous chunk.

**11:32** · If you're going to be doing long audio, you're gonna need some way to chunk it up, and honestly, I'm not seeing the higher speed that they're claiming most likely because I'm not using, an H100, but also I think it's got to do with the chunking and the batching of this.

**11:46** · That said, on the GPU that I've been using, I've been able to get very nice outputs from this.

**11:51** · Just coming into the GitHub here they've got a bunch of nice things of where you could do speculative decoding, with this.

**11:58** · but also their notebook from the previous version for doing fine-tuning, which you Should be able to use to actually fine-tune a model perhaps for your specific voice if you've got an accent, or if you've got a specific kind of use case.

### Granite Speech Model Github

**12:11** · A good example like this could be something like court transcripts or a specific podcast, where you can actually get some transcripts already for certain episodes, use them as training data to actually get a fine-tuned version of this model that will work for the particular host that you're trying to transcribe.

**12:30** · So for me personally, I've started to put together my own repo of all the things that I wanted to have in there, and set up some simple scripts.

**12:39** · I'll probably end up writing some agent skills to actually go along with this, so that I could actually have this running on my machine, And then have agents reach out to it to do the transcriptions fully locally without needing to get anything in the cloud.

**12:52** · And just showing you something from some of my own tests.

**12:54** · One of the things that is really cool here is the whole idea of timestamps.

**12:58** · Now, I need to probably do a lot more analysis of checking this, but so far, It's looking pretty good at how it's able to basically give us timestamps for each word that we're actually transcribing.

**13:10** · Some of the issues I've had with this that I'm still experimenting with is what is the best way to do really long-form audio?

**13:16** · So if you've got something like a four-hour podcast or something like that, You want to be able to pass in the keyword biasing stuff.

**13:22** · And you can see actually here how, that is actually done, right?

**13:25** · So that you've got a specific prompt that you pass in where you've got keywords, and then you just pass in each of those keywords.

**13:32** · And definitely one of the things I'm still experimenting with is what is the best chunking size to be able to do the long-form audio.

**13:38** · And what are the best pretext filling strategies for you to be able to stitch together really long transcripts and to have, multiple speakers for the diarization, et cetera?

**13:48** · Overall though, just to finish up, I would say that while perhaps the language models, there's better things out there than the Granite stuff, the speech stuff is really super interesting.

**13:59** · also the embedding stuff and the Guardian models probably deserve some more investigation on their own, et cetera.

**14:04** · but altogether, this is a really interesting release from IBM, and I hope they keep it up, right?

**14:11** · I hope this doesn't become like the Microsoft Phi models where they've kind of scaled it back and are not really doing it.

**14:17** · it's great to see that IBM realizes that a lot of people want these smaller kind of models, whether they're smaller language models, vision models, speech models, et cetera.

**14:27** · So anyway, let me know what you think in the comments.

**14:29** · As always, if you found the video useful, please click like and subscribe, and I will talk to you in the next video.

**14:34** · Bye for now.