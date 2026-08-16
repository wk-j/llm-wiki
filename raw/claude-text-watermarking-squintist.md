# Claude Now Watermarks Its Text. How Do You Even Do That?

- URL: https://www.youtube.com/watch?v=3FhxdhVMJoU
- Author: Squintist (YouTube channel)
- Supplied by user, saved 2026-08-16

"""
![](https://www.youtube.com/watch?v=3FhxdhVMJoU)

Sources & further reading

\- Anthropic — How Claude marks AI-generated content (the support page this starts from) — https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
\- Peter Harrell on the copy-edit case — https://x.com/petereharrell/status/2087020627509100824
\- Sean Goedecke — why text watermarking is hard, and the cheap shortcuts — https://www.seangoedecke.com/text-ai-watermarks/
\- Nature — Scalable watermarking for identifying large language model outputs (the SynthID Text paper; tournament sampling, the ~20M-response Gemini experiment) — https://www.nature.com/articles/s41586-024-08025-4
\- Google DeepMind — Watermarking AI-generated text and video with SynthID — https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/
\- Google — SynthID developer documentation (detection states and thresholds) — https://ai.google.dev/responsible/docs/safeguards/synthid
\- google-deepmind/synthid-text — the open-source reference implementation — https://github.com/google-deepmind/synthid-text
\- Preprint (July 2026) — paraphrasing removed detection in 58 of 59 samples, on a public MarkLLM implementation over Gemma-2-9B, not Google's production detector — https://arxiv.org/html/2607.16010
\- EU AI Act, Article 50 — the marking obligation and the standard-editing exception — https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50
\- European Commission — guidelines on transparency obligations (what counts as standard editing) — https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
\- European Commission — Code of Practice on Transparency of AI-Generated Content — https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
\- European Commission — the signatory list — https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content
\- OpenAI — C2PA and SynthID in OpenAI-generated images (text provenance still planned) — https://help.openai.com/en/articles/8912793-c2pa-and-synthid-in-openai-generated-images
\- GPTZero — how AI detectors work — https://gptzero.me/news/how-ai-detectors-work/
\- GPTZero — perplexity and burstiness, and why they no longer describe the current system — https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
\- GPTZero — 2026 technical report (vendor-authored, including its own limitations section) — https://arxiv.org/abs/2602.13042
\- OpenAI — the 2023 classifier it withdrew: 26% caught, 9% false positives — https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/
\- Stanford-led study (2023) — seven detectors, 61% average false-positive rate on TOEFL essays by non-native writers — https://arxiv.org/html/2304.02819
\- r/academia — "AI detection software is junk science and we need to stop pretending otherwise" — https://www.reddit.com/r/academia/comments/1rjlea0/ai_detection_software_is_junk_science_and_we_need/
\- r/academia — the writing professor whose comedy story came back 100% AI — https://www.reddit.com/r/academia/comments/1rm11rs/pangram_claims_their_ai_writing_detectors_false/
\- NeurIPS 2026 — AI-generated papers in the Position Paper Track (969 screened, 178 desk-rejected) — https://blog.neurips.cc/2026/06/02/ai-generated-papers-in-the-neurips-2026-position-paper-track/
\- r/MachineLearning — the response from a rejected author — https://www.reddit.com/r/MachineLearning/comments/1tvwctd/neurips_used_uncalibrated_ai_detector_for_desk/
\- Pangram — what a "humanizer" is, and the tools it names — https://www.pangram.com/blog/what-is-a-humanizer
\- Pangram — how students try to avoid AI detection — https://www.pangram.com/blog/how-students-try-to-avoid-ai-detection
\- The Verge — ChatGPT's favourite words are showing up in human speech — https://www.theverge.com/openai/686748/chatgpt-linguistic-impact-common-word-usage
\- arXiv 2409.01754 — the Max Planck study behind that finding (~280,000 YouTube videos) — https://arxiv.org/abs/2409.01754

Chapters

00:00 Anthropic starts marking Claude's text
01:01 Why text is the hard case
01:49 A model never just takes the obvious word
02:17 Temperature: how much to let the dice matter
03:01 The tournament that rigs the roll
03:39 Why the words still come out ordinary
04:25 Detection: the same trick in reverse
05:12 Twenty million Gemini responses
05:37 Weakness one: no room in "Paris"
06:14 Weakness two: it washes off
07:00 Back to the report you wrote yourself
07:50 Why the labs are doing this: Brussels
08:25 The code of practice, and who signed it
08:57 AI detectors are a different animal
09:35 The detectors' track record
10:11 A professor, a comedy story, 100% AI
10:45 NeurIPS desk-rejects 178 papers
11:19 So how do you get the mark off?
11:48 The arms race, and a gap that's closing
12:53 What a watermark can actually answer
13:25 How this channel gets made

## Transcript

### Anthropic starts marking Claude's text

**0:00** · August 2026, Anthropic posts a new support page. It says that from now on, every new Claude model will invisibly watermark the text it writes. Not metadata in a file, not a hidden character.

**0:15** · The watermark lives in the choice of words themselves, and it travels with the text when you copy-paste it anywhere.

**0:22** · Which creates a strange situation. You write a thousand-word report, every word of it yourself, and ask Claude to copy-edit it. Fix the grammar, tighten the clumsy sentences, same content. What comes back can now carry a machine-readable mark saying an AI made this.

**0:41** · Anthropic is upfront about it. The mark means Claude touched the text. It says nothing about who wrote it. How do you even hide a signal inside plain English?

**0:51** · Why did the EU make it mandatory? And how did AI detectors end up rejecting nearly a fifth of the papers at the biggest AI research conference on Earth?

### Why text is the hard case

**1:02** · Watermarking an image is easy. A photo is millions of pixels. Nudge a few thousand, and no eye will ever know.

**1:10** · Audio has background noise to hide in.

**1:12** · Text has none of that. Text is like a barcode. Change one word, and everyone sees it. For years, the honest answer was that you can't watermark writing without wrecking it. There are two obvious shortcuts. The first is to hide invisible characters in the text. Swap normal spaces for look-alike spaces in a secret pattern.

**1:33** · It's cheap to add, and one find and replace strips it out. The second is to skip the watermark and guess from style.

**1:42** · Count the M dashes. Count how often it says delve. That one matters, because it's what most people think AI detection is.

### A model never just takes the obvious word

**1:50** · The real answer is much cleverer, and Google's version is called SynthID.

**1:55** · It works because of one fact about how a language model writes. The model never just takes the obvious next word. At every step, it computes a list of plausible options with odds. Bananas, 90%. Mangoes, eight. Airplanes, basically zero. And then it rolls the dice and picks one. One word at a time, but always from a list.

### Temperature: how much to let the dice matter

**2:18** · Why roll the dice at all? Why not just take the top word every time?

**2:23** · Because a model that always takes the favorite writes like a broken record.

**2:27** · Loops, safe phrases, the same sentence over and over.

**2:32** · Sampling from the list is what makes the text sound alive.

**2:36** · And how much to sample is a dial. And the dial's actual name is temperature.

**2:41** · Turn it down and the odds sharpen. The 90% word becomes 99 and the dice barely matter.

**2:48** · Turn it up and the long shots start winning.

**2:52** · So, a coding assistant runs cold, close to zero, because there's usually one right next token. While brainstorming runs warm.

### The tournament that rigs the roll

**3:01** · SynthID rigs the dice roll. Here's how, with a real example. Say the model is mid-sentence and the plausible next words are four near synonyms. Big, large, huge, vast. Normally, it would just pick one by the odds. SynthID instead runs a knockout tournament among the candidates. And in every match, the winner is decided by a hidden score.

**3:25** · That score comes from a secret key mixed with the last few words written. So, at this exact step, the key might mark big and vast as the winners and large and huge as the losers. And a winning synonym is what comes out as the next word. Now the part that took me a second to see. The key reshuffles at every step because it's mixed with the words just written. So, at the next synonym choice, the key flips. Now large and huge are the favorites, and big and vast are out.

### Why the words still come out ordinary

**3:55** · No word is permanently favored. Run it for a million steps, and big wins exactly as often as it would have with no tournament at all. The text reads ordinary. The word counts don't budge.

**4:08** · But for the one key the lab actually used, the words that came out tended to be ones the key favored at that step more often than chance would predict.

**4:17** · The pattern has no visible trace. The words are normal, and only the key knows. That's a signal hidden in the noise. Detection runs the same trick in reverse. Concretely, here's how.

### Detection: the same trick in reverse

**4:30** · You paste in the suspicious text. The checker holds the key.

**4:35** · It slides along the text, and at each word it redoes the sampler's math. Mix the key with the previous few words, pull up that step's hidden scores, and check whether the word actually sitting there got a high one.

**4:48** · Add it up.

**4:50** · In plain human writing, you'd expect coin flips. About half the words score high just by chance.

**4:56** · In text that came out of the keyed sampler, the score runs noticeably above half. Not on any single word, only across hundreds of them.

**5:06** · No database, no model, just the words plus the key. The words themselves are the evidence. Google ran this live inside Gemini, their chatbot, and published the whole thing in Nature, the science journal. About 20 million responses, half got the watermark, half didn't. The thumbs up rate differed by 1/100 of a percent, which is statistically nothing. And the slowdown was about half a percent. The people rating the answers couldn't tell the watermark was there.

### Twenty million Gemini responses

**5:36** · But it has a weakness, and the weakness tells you how it works. The tournament needs contestants. Ask for the capital of France, and there is exactly one word anyone will accept. That's a tournament with one contestant, a war built into the question itself. However, the model rolls the dice, only Paris lands.

### Weakness one: no room in "Paris"

**5:57** · There's nowhere to hide a signal. Code has the same problem. The wrong synonym breaks the built, and so does anything short. The watermark lives in linguistic freedom. The more ways there are to say a thing, the more room there is to rig the choice. You can hide a pattern in brushstrokes. You can't hide one in a barcode.

### Weakness two: it washes off

**6:15** · A second weakness is that the mark is easy to wash off. Translate the text into another language and back, or run it through a paraphrasing tool. The words change, and when the words change, the secret scores no longer line up. If the scores don't line up, there is no mark left. We know this works because Google released the SynthID code for free, so anyone can build a small copy and test the attack.

**6:39** · One research team did that this summer.

**6:42** · They made watermarked text with their copy, paraphrased it, and checked it again.

**6:47** · The mark was gone in 58 out of 59 cases.

**6:51** · Their copy is a home version, not the system Google runs inside Gemini. So, treat that number as a first result, but the attack itself clearly works.

### Back to the report you wrote yourself

**7:00** · Back to the report you wrote yourself.

**7:03** · Anthropic hasn't published how its mark works. That part's still under wraps, but a watermark of this kind can only be added while the model is choosing the words. You can't stamp it on afterward.

**7:14** · So, when Claude copy edits your text, the reply comes out through the same rigged tournament as everything else Claude writes.

**7:21** · That also tells you where the edge is.

**7:23** · If Claude changes nothing but two commas, there is only one acceptable word at almost every step. No tournament, no room for a signal.

**7:32** · The more the model rephrases, the stronger the mark can be, and a real copy edit involves a lot of rephrasing.

**7:39** · Anthropic's own wording, "A detected mark means the content may have been, quote, processed by Claude. Proofread, translated, summarized, or written from scratch, same mark.

### Why the labs are doing this: Brussels

**7:50** · Why are the labs doing this? The short answer is Brussels. The EU's argument, when a machine can generate a million words a day, people need a way to tell machine-made text from human text. Fake reviews, fraud, impersonation. So, the AI Act says that from August 2nd, generative AI output has to be machine readably marked. And the law makes an exception for standard editing.

**8:15** · Spelling, grammar, and translation need no mark. That covers the report from the beginning. The law exempts the spell check, but Anthropic watermarks it anyway. The EU's compliance code adds the details. Watermark free-form text longer than a solid paragraph, and give people a way to check marks for free.

### The code of practice, and who signed it

**8:34** · Though for plain text, the code lets labs restrict that checker to verified experts at first, because text marks are the least reliable kind.

**8:42** · Anthropic, Google, OpenAI, Meta, Microsoft, Mistral, all signed. The code is voluntary, but the law behind it isn't. So, if your plan was switching to a model that doesn't watermark, the sign-up sheet is on the fridge, and everyone's already signed.

### AI detectors are a different animal

**8:58** · Meanwhile, the tools most people actually meet are a different animal, AI detectors. GPT-3, Pangram, Turnitin's checker. There's no secret key and no tournament here. They read the text and judge the style.

**9:13** · Early GPT-3 scored how predictable your words were, and how even your sentence rhythm was. Too smooth, too steady, probably a machine.

**9:22** · These days, they're neural networks trained on millions of human and AI samples, looking for family resemblance.

**9:29** · If a watermark is a serial number stamped at the factory, these are handwriting experts. And the handwriting experts have a record. OpenAI built its own detector back in 2023. It caught about a quarter of AI-written text, falsely flagged 9% of human writing, and got shut down within months. A Stanford study that year ran essays by non-native English speakers through seven popular detectors, and 61% of them got flagged as AI.

### The detectors' track record

**9:58** · The current models are better. Pangram reports zero flags on that exact data set today, but the failure mode hasn't gone away. Careful, formal second language English is exactly what these systems are worst at judging.

### A professor, a comedy story, 100% AI

**10:12** · The collateral damage is its own genre on Reddit now. Students writing in typos on purpose so they don't get flagged.

**10:19** · A writing professor of 25 years spent six months polishing one comedy short story line by line.

**10:27** · Pangram flagged it 100% AI, and he said he was thinking of giving up.

**10:32** · Comedy runs on the rule of three, a classical human rhetorical device.

**10:37** · And the rule of three is exactly what these detectors now read as a machine tell.

**10:43** · Human craft mistaken for a machine.

### NeurIPS desk-rejects 178 papers

**10:46** · Then it hit academia. NeurIPS, one of the big AI conferences, ran an opinion essay track this year with a rule: AI for copy editing only.

**10:56** · They scanned all 969 submissions with Pangram and rejected 178 before peer review. 18% of the track, no appeal.

**11:07** · One rejected author ran the track chair's own published papers through the same detector. 24 to 69%.

**11:15** · Not high enough to trip their own thresholds, but not zero, either.

### So how do you get the mark off?

**11:19** · So, what if you just want the mark gone?

**11:22** · That's the easy part. We already saw both ways. Translate the text into another language and back, or hand it to a second model and say, "Rewrite this."

**11:31** · That second model doesn't have to live on anyone's server. The team from earlier used an open model with 9 billion parameters, which runs on a decent home machine. No provider in the loop, no watermark, and an open model can't be forced to mark anything because the person running it controls the dice.

### The arms race, and a gap that's closing

**11:48** · The detector companies say they're keeping up. They retrain against the humanizer tools and post new accuracy numbers. Humanizers are a whole product category that exists only because detectors do.

**12:00** · You paste in AI text and undetectable.ai or QuillBot or Stealth GPT gives it back with the marks scrubbed enough to score as human. So, the detector companies retrain against the washers, the washers retool against the detectors, and both markets grow on each other.

**12:18** · Maybe that keeps working, but the deeper problem is the premise. A style detector only works while AI writing looks different from human writing, and that gap is closing from both directions. The models are trained to sound human.

**12:32** · That's the training objective. And humans are absorbing model style. After ChatGPT came out, researchers found its favorite words, delve, meticulous, realm, appearing up to 50% more often in human talks, and the speakers didn't notice it happening. A style detector is a snapshot of a difference, and the difference is dissolving.

### What a watermark can actually answer

**12:54** · Fluent prose used to be a useful clue.

**12:57** · If something read well, someone had probably spent time making it read well.

**13:02** · Now, a model can produce clean sentences in seconds.

**13:06** · That shortcut is gone.

**13:08** · A watermark can answer one useful question. Did these words come through this model?

**13:14** · A style detector tries to guess the same thing without the mark.

**13:18** · Neither can tell you whether the claims are true or whether this video was worth your time. That's still your call. If you download the transcript of this video and run it through those detectors, it will probably come back mostly AI. And it wouldn't exactly be wrong. Almost every word in this script came from one AI model or another. The voice, yes, this voice was generated, too.

### How this channel gets made

**13:43** · I make this channel using several models and some code. The tools help with research and drafts, but there are still a lot of rewrites. It could be frustrating. Models write quickly, but not always well.

**13:56** · Some ideas never become stories and get abandoned.

**13:59** · But anyway, without these tools, this channel probably wouldn't exist. I made the first video a few months ago. More people liked it than I expected, so I kept going.

**14:09** · Part of the experiment was could I make YouTube videos without becoming, you know, a YouTuber?

**14:15** · I wanted to see if the videos could work without my face, natural voice, or resume doing the selling.

**14:22** · I wouldn't use Mr. Beast-style shocked face thumbnails, either.

**14:26** · The videos would have to stand on their own. That meant solid research and sources people could check. They also had to look and sound like something I would want to watch. Now, it's getting close-ish to 10,000 subscribers.

**14:40** · A lot of you have watched, subscribed, and told me the videos were useful.

**14:44** · Thank you.

**14:46** · When it gets there, I plan to do a Q&A about the channel.

**14:49** · The voice you normally hear will ask the questions, and I'll answer in my own voice.

**14:54** · If there is something you want to ask, leave it below.

**14:57** · Subscribe if you want to see it happen.
"""
