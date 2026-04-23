---
title: "Kimi K2.6 Tech Blog: Advancing Open-Source Coding"
source: "https://www.kimi.com/blog/kimi-k2-6"
author:
published:
created: 2026-04-21
description: "Kimi K2.6 advances open-source coding, featuring long-horizon coding, coding-driven design, agent swarms, proactive agents, and the Claw Groups research preview."
tags:
  - "clippings"
---
Long-Horizon Coding

Coding-Driven Design

Agent Swarms, Elevated

Proactive Agents

Bring Your Own Agents

Benchmark Table

Footnotes

We are open sourcing our latest model, **Kimi K2.6**, featuring **state-of-the-art coding, long-horizon execution, and agent swarm capabilities**. Kimi K2.6 is now available via **[Kimi.com](https://www.kimi.com/), the Kimi App, the [API](https://platform.kimi.ai/), and [Kimi Code](https://www.kimi.com/code)**.

General Agents

###### Humanity's Last Exam (Full) w/ tools

###### BrowseComp

###### DeepSearchQA (f1-score)

###### Toolathlon

###### OSWorld-Verified

Coding

###### Terminal-Bench 2.0 (Terminus-2)

###### SWE-Bench Pro

###### SWE-Multilingual

Visual Agents

###### MathVision w/ python

###### V\* w/ python

## Long-Horizon Coding

Kimi K2.6 shows strong improvements in long-horizon coding tasks, with reliable generalization across programming languages (e.g., Rust, Go, and Python) and tasks (e.g., front-end, devops, and performance optimization). On **Kimi Code Bench**, our internal coding benchmark covering diverse complicated end-to-end tasks, Kimi K2.6 demonstrates significant improvements over Kimi K2.5.

![Kimi Code Bench](https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-04-20/1d7j305qav1fc641b5670?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1)

Kimi K2.6 demonstrates strong long-horizon coding in complex engineering tasks:

Kimi K2.6 successfully downloaded and deployed the **Qwen3.5-0.8B** model locally on a Mac. By implementing and optimizing model inference in **Zig** —a highly niche programming language—it demonstrated exceptional out-of-distribution generalization. Across **4,000+ tool calls, over 12 hours of continuous execution, and 14 iterations**, Kimi K2.6 dramatically improved throughput from ~15 to **~193 tokens/sec**, ultimately achieving speeds ~20% faster than LM Studio.

![K2.6 Qwen3.5-0.8B Mac inference optimization case](https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-04-20/1d7j1727f2ena623likig?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1)

Kimi K2.6 autonomously overhauled **exchange-core**, an 8-year-old open-source financial matching engine. Over a **13-hour execution**, the model iterated through 12 optimization strategies, initiating over 1,000 tool calls to precisely modify more than 4,000 lines of code. Acting as an expert systems architect, Kimi K2.6 analyzed CPU and allocation flame graphs to pinpoint hidden bottlenecks and boldly reconfigured the core thread topology (from 4ME+2RE to 2ME+1RE). Despite the engine already operating near its performance limits, Kimi K2.6 extracted a **185% medium throughput leap** (from 0.43 to 1.24 MT/s) and a **133% performance throughput gain** (soaring from 1.23 to 2.86 MT/s).

![K2.6 exchange-core coding showcase](https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-04-20/1d7j16siav1fc641arbr0?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1)

In beta tests, K2.6 performs well on long-horizon coding tasks in enterprise evaluations (by alphabetic order):

> **Kimi K2.6's evolution is impressive.** It excels on coding tasks at a level comparable to leading closed source models, and offers strong tool calling quality due to its deep understanding of third party frameworks. Kimi K2.6's excellent reliability makes it a great choice for complex and long-horizon engineering tasks.

> **Kimi K2.6 sets a new level for open-sourced models, especially in long-horizon, agent-style coding workflows.** It handles complex, multi-step tasks with stronger instruction following and consistently high code quality. We've seen it sustain extended coding sessions with remarkable stability, far beyond typical models. It also surfaces deep, non-obvious bugs that would normally take significant developer time to uncover. Overall, K2.6 sets a new bar for reliable coding.

> **Kimi K2.6 demonstrates significant improvements over K2.5 in internal evaluations conducted by CodeBuddy: code generation accuracy increased by 12%, long-context stability improved by 18%, and tool invocation success rate reached 96.60%.** Its stronger reasoning capabilities and more consistent output quality provide robust support for ensuring a reliable user experience in CodeBuddy WorkBuddy.

> **K2.6 is a clear improvement on K2.5 on both our benchmarks (+15%) and in side-by-side comparisons.** It seems to have better instruction following, more thorough exploration and reasoning, and less likely to make coding errors or use hacks.

> We are thrilled to see another leap in open source models with Kimi K2.6 release, which marks a significant advancement for high-stakes, agentic workflows. **The most impactful improvements lie in its long-horizon reliability and instruction following.** K2.6 excels at maintaining architectural integrity over extended coding sessions, making it a stable foundation for autonomous agent pipelines, like all the "claws". It demonstrates a measurable leap over K2.5 in long-context tasks, achieving state-of-the-art performance in complex reasoning.

> Got an early look at K2.6 and ran it through Hermes Agent. **Tool calling and agentic loops feel noticeably tighter, coding is a clear step up, and the creative range surprised us.** We're super excited about running a hackathon with Kimi on creativity. Kimi team continues to beat expectations!

> **K2.6 offers SOTA-level performance at a fraction of the cost.** It's tremendously good at long-context tasks across the codebase, as well as the day-to-day work needed to support an always-on agent like KiloClaw.

> **Kimi K2.6 raises the bar for open-source models.** It excels in coding and especially for agentic tools like OpenClaw and Hermes. In early testing, it sustains long multi-step sessions with impressive stability. It will work all of Ollama's integrations out of the box, and we're excited to see what developers build with it.

> **Within OpenCode, Kimi K2.6 proves to be exceptionally reliable.** Its approach to task decomposition and tool calling is both steady and consistent. With a sharper grasp of task requirements and more streamlined multi-step operations, it effectively minimizes repetitive overhead, resulting in a smoother, more trustworthy end-to-end experience.

> **Kimi K2.6 delivered a strong performance in Qoder's internal evaluations, showing significant progress over K2.5.** Specifically, there has been a notable increase in the frequency of tool calling and model invocations, reflecting a substantial boost in the model's proactivity and intelligence during task execution. This heightened initiative in tool calling enables the model to more actively grasp developer intent and automatically complete context, thereby minimizing user interruptions and wait times.

> K2.6 shows major gains over K2.5 on the capabilities our developers care about most: we're seeing more than 50% improvement on our Next.js benchmark, putting it among the top-performing models on the platform. Combined with its cost-performance ratio, it's a compelling option for agentic coding and front-end generation through AI Gateway. We're excited to offer it to our developer community.

01 / 06

## Coding-Driven Design

Based on the strong coding capabilities, Kimi K2.6 can turn simple prompts into complete front-end interfaces, generating structured layouts with deliberate design choices such as aesthetic hero sections, as well as interactive elements and rich animations, including scroll-triggered effects. With strong proficiency in leveraging image and video generation tools, Kimi K2.6 supports the generation of visually coherent assets and contributes to higher-quality, more salient hero sections.

Moreover, Kimi K2.6 expands beyond static frontend development to simple full-stack workflows—spanning authentication to user interaction to database operations for lightweight use cases like transaction logging or session management.

We established an internal **Kimi Design Bench**, organized into four categories: Visual Input Tasks, Landing Page Construction, Full-Stack Application Development, and General Creative Programming. In comparison with Google AI Studio, Kimi K2.6 shows promising results and performs well across these categories.

![Kimi Design Bench](https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-04-20/1d7j30aiav1fc641b5710?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1)

Below are examples generated by [K2.6 Agent](https://www.kimi.com/websites) from a single prompt, with preconfigured harnesses and tools:

Aesthetic: Beautiful front-end design with rich interaction

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnk053v89kkehrsu70?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video><video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnkiaav1fc641194p0?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video><video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnku2av1fc641197gg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

Functionality: With built-in database and authentication

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7isbkd3v89kkei4o4mg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video><video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnklpl51jas5f2nmng?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video><video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnl1edcmosb3uul6q0?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

Tool use: Use image/video gen tools to create a polished website

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7irsmpl51jas5fbh3qg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video><video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnkovf2ena623c10rg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video><video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-15/1d7fnl4nf2ena623c13jg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

## Agent Swarms, Elevated

**Scaling out, not just up.** An Agent Swarm dynamically decomposes tasks into heterogeneous subtasks executed concurrently by self-created domain-specialized agents.

Based on the K2.5 Agent Swarm research preview, [Kimi K2.6 Agent Swarm](https://www.kimi.com/agent-swarm) demonstrates **a qualitative leap** in the agent swarm experience. It seamlessly coordinates heterogeneous agents to combine complementary skills: broad search layered with deep research, large-scale document analysis fused with long-form writing, and multi-format content generation executed in parallel. This compositional intelligence enables the swarm to deliver end-to-end outputs—spanning documents, websites, slides, and spreadsheets—within a single autonomous run.

The architecture scales horizontally to **300 sub-agents executing across 4,000 coordinated steps simultaneously**, a substantial expansion from K2.5's 100 sub-agents and 1,500 steps. This massive parallelization fundamentally reduces end-to-end latency while significantly enhancing output quality and expanding the operational boundaries of Agents swarms.

It can also turn any high-quality files such as PDFs, spreadsheets, slides, and Word documents into **Skills**. Kimi K2.6 captures and maintains the documents' structural and stylistic DNA, enabling you to reproduce the same quality and format in future tasks.

Here are some examples:

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7itc9ff2ena623l0t3g?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

Designed and executed 5 quantitative strategies across 100 global semiconductor assets, deriving McKinsey-style PPT as reusable skills, and delivering detailed modeling spreadsheets and a full executive presentation.

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7itct7f2ena623l0vk0?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

Turned a high-quality astrophysics paper with rich visual data into a reusable academic skill, deriving its reasoning flow and visualization methods, and produced a 40-page, 7,000-word research paper, a structured dataset with 20,000+ entries, and 14 astronomy-grade charts.

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7itd0vf2ena623l0vvg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

Based on the uploaded CV, K2.6 spawned 100 sub-agents to match 100 relevant roles in California, delivering a structured dataset of opportunities and 100 fully customized resumes.

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7itdbn6rtp4tqb7mrkg?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

Identified 30 retail stores in Los Angeles without official websites from Google Maps, and generated high-converting landing pages for each, demonstrating opportunity discovery and end-to-end execution.

## Proactive Agents

K2.6 demonstrates strong performance in autonomous, proactive agents such as **[OpenClaw](https://openclaw.ai/)** and **[Hermes](https://hermes-agent.nousresearch.com/)**, which operate across multiple applications with continuous, 24/7 execution.

Unlike simple chat-based interactions, these workflows require AI to proactively manage schedules, execute code, and orchestrate cross-platform operations as a persistent background agent.

Our RL infra team used a K2.6-backed agent that operated autonomously for **5 days**, managing monitoring, incident response, and system operations, demonstrating persistent context, multi-threaded task handling, and full-cycle execution from alert to resolution. Here is K2.6's worklog (anonymized to remove sensitive information):

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7iu25d3v89kkei510d0?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

K2.6 Agent Trace — 5-day autonomous engineering worklog

Kimi K2.6 delivers measurable improvements in real-world reliability: more precise API interpretation, stabler long-running performance, and enhanced safety awareness during extended research tasks.

Performance gains are quantified by our internal **Claw Bench**, the evaluation suite spanning five domains: Coding Tasks, IM Ecosystem Integration, Information Research & Analysis, Scheduled Task Management, and Memory Utilization. Across all metrics, Kimi K2.6 significantly outperforms Kimi K2.5 in task completion rates and tool invocation accuracy—particularly in workflows requiring sustained autonomous operation without human oversight.

![Kimi Claw Bench](https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-04-20/1d7j2vv53v89kkei5on5g?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1)

## Bring Your Own Agents

Building upon Kimi K2.6's robust orchestration capabilities, Kimi K2.6 extends your proactive agents to **Claw Groups** as a research preview—a new instantiation of the Agent Swarm architecture.

Claw Groups embrace an open, heterogeneous ecosystem: Multiple agents and humans operate as true collaborators. Users can onboard agents from any device, running any model, each carrying their own specialized toolkits, skills and persistent memory contexts. Whether deployed on local laptops, mobile devices, or cloud instances, these diverse agents integrate seamlessly into a shared operational space.

At the center of this swarm, Kimi K2.6 serves as an adaptive coordinator. It dynamically matches tasks to agents based on their specific skill profiles and available tools, optimizing for capability fit. When an agent encounters failure or stalls, the coordinator detects the interruption, automatically reassigns the task or regenerates subtasks, and actively manages the full lifecycle of deliverables—from initiation through validation to completion.

We also want to thank the K2.6-powered agents in Claw Groups—we've been dogfooding our own agent marketing team by refining human–agent workflows in practice. Using Claw Groups, we run end-to-end content production and launch campaigns, with specialized agents like Demo Makers, Benchmark Makers, Social Media Agents, and Video Makers working together. K2.6 coordinates the process, enabling agents to share intermediate results and turn ideas into consistent, fully packaged deliverables.

<video src="https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/1/2026-04-20/1d7j46uudcmosb3v8m270?x-tos-process=image%2Fauto-orient%2C1%2Fstrip%2Fignore-error%2C1" controls=""></video>

We are moving beyond simply asking AI a question or assigning AI a task, and entering a phase where human and AI collaborate as genuine partners—combining strengths to solve problems collectively. Claw Groups marks our latest efforts toward a future where the boundaries between "my agent," "your agent," and "our team" dissolve seamlessly into a collaborative system.

## Benchmark Table

<table><thead><tr><th>Benchmark</th><th>Kimi K2.6</th><th>GPT-5.4 (xhigh)</th><th>Claude Opus 4.6 (max effort)</th><th>Gemini 3.1 Pro (thinking high)</th><th>Kimi K2.5</th></tr></thead><tbody><tr><td>Agentic</td><td colspan="5"></td></tr><tr><td rowspan="1"><p>HLE-Full w/ tools</p></td><td>54.0</td><td>52.1</td><td>53.0</td><td>51.4</td><td>50.2</td></tr><tr><td rowspan="1"><p>BrowseComp</p></td><td>83.2</td><td>82.7</td><td>83.7</td><td>85.9</td><td>74.9</td></tr><tr><td rowspan="1"><p>BrowseComp (agent swarm)</p></td><td>86.3</td><td>—</td><td>—</td><td>—</td><td>78.4</td></tr><tr><td rowspan="1"><p>DeepSearchQA (f1-score)</p></td><td>92.5</td><td>78.6</td><td>91.3</td><td>81.9</td><td>89.0</td></tr><tr><td rowspan="1"><p>DeepSearchQA (accuracy)</p></td><td>83.0</td><td>63.7</td><td>80.6</td><td>60.2</td><td>77.1</td></tr><tr><td rowspan="1"><p>WideSearch (item-f1)</p></td><td>80.8</td><td>—</td><td>—</td><td>—</td><td>72.7</td></tr><tr><td rowspan="1"><p>Toolathlon</p></td><td>50.0</td><td>54.6</td><td>47.2</td><td>48.8</td><td>27.8</td></tr><tr><td rowspan="1"><p>MCPMark</p></td><td>55.9</td><td>62.5*</td><td>56.7*</td><td>55.9*</td><td>29.5</td></tr><tr><td rowspan="1"><p>Claw Eval (pass^3)</p></td><td>62.3</td><td>60.3</td><td>70.4</td><td>57.8</td><td>52.3</td></tr><tr><td rowspan="1"><p>Claw Eval (pass@3)</p></td><td>80.9</td><td>78.4</td><td>82.4</td><td>82.9</td><td>75.4</td></tr><tr><td rowspan="1"><p>APEX-Agents</p></td><td>27.9</td><td>33.3</td><td>33.0</td><td>32.0</td><td>11.5</td></tr><tr><td rowspan="1"><p>OSWorld-Verified</p></td><td>73.1</td><td>75.0</td><td>72.7</td><td>—</td><td>63.3</td></tr><tr><td>Coding</td><td colspan="5"></td></tr><tr><td rowspan="1"><p>Terminal-Bench 2.0 (Terminus-2)</p></td><td>66.7</td><td>65.4*</td><td>65.4</td><td>68.5</td><td>50.8</td></tr><tr><td rowspan="1"><p>SWE-Bench Pro</p></td><td>58.6</td><td>57.7</td><td>53.4</td><td>54.2</td><td>50.7</td></tr><tr><td rowspan="1"><p>SWE-Bench Multilingual</p></td><td>76.7</td><td>—</td><td>77.8</td><td>76.9*</td><td>73.0</td></tr><tr><td rowspan="1"><p>SWE-Bench Verified</p></td><td>80.2</td><td>—</td><td>80.8</td><td>80.6</td><td>76.8</td></tr><tr><td rowspan="1"><p>SciCode</p></td><td>52.2</td><td>56.6</td><td>51.9</td><td>58.9</td><td>48.7</td></tr><tr><td rowspan="1"><p>OJBench (python)</p></td><td>60.6</td><td>—</td><td>60.3</td><td>70.7</td><td>54.7</td></tr><tr><td rowspan="1"><p>LiveCodeBench (v6)</p></td><td>89.6</td><td>—</td><td>88.8</td><td>91.7</td><td>85.0</td></tr><tr><td>Reasoning & Knowledge</td><td colspan="5"></td></tr><tr><td rowspan="1"><p>HLE-Full</p></td><td>34.7</td><td>39.8</td><td>40.0</td><td>44.4</td><td>30.1</td></tr><tr><td rowspan="1"><p>AIME 2026</p></td><td>96.4</td><td>99.2</td><td>96.7</td><td>98.3</td><td>95.8</td></tr><tr><td rowspan="1"><p>HMMT 2026 (Feb)</p></td><td>92.7</td><td>97.7</td><td>96.2</td><td>94.7</td><td>87.1</td></tr><tr><td rowspan="1"><p>IMO-AnswerBench</p></td><td>86.0</td><td>91.4</td><td>75.3</td><td>91.0*</td><td>81.8</td></tr><tr><td rowspan="1"><p>GPQA-Diamond</p></td><td>90.5</td><td>92.8</td><td>91.3</td><td>94.3</td><td>87.6</td></tr><tr><td>Vision</td><td colspan="5"></td></tr><tr><td rowspan="1"><p>MMMU-Pro</p></td><td>79.4</td><td>81.2</td><td>73.9</td><td>83.0*</td><td>78.5</td></tr><tr><td rowspan="1"><p>MMMU-Pro w/ python</p></td><td>80.1</td><td>82.1</td><td>77.3</td><td>85.3*</td><td>77.7</td></tr><tr><td rowspan="1"><p>CharXiv (RQ)</p></td><td>80.4</td><td>82.8*</td><td>69.1</td><td>80.2*</td><td>77.5</td></tr><tr><td rowspan="1"><p>CharXiv (RQ) w/ python</p></td><td>86.7</td><td>90.0*</td><td>84.7</td><td>89.9*</td><td>78.7</td></tr><tr><td rowspan="1"><p>MathVision</p></td><td>87.4</td><td>92.0*</td><td>71.2*</td><td>89.8*</td><td>84.2</td></tr><tr><td rowspan="1"><p>MathVision w/ python</p></td><td>93.2</td><td>96.1*</td><td>84.6*</td><td>95.7*</td><td>85.0</td></tr><tr><td rowspan="1"><p>BabyVision</p></td><td>39.8</td><td>49.7</td><td>14.8</td><td>51.6</td><td>36.5</td></tr><tr><td rowspan="1"><p>BabyVision w/ python</p></td><td>68.5</td><td>80.2*</td><td>38.4*</td><td>68.3*</td><td>40.5</td></tr><tr><td rowspan="1"><p>V* w/ python</p></td><td>96.9</td><td>98.4*</td><td>86.4*</td><td>96.9*</td><td>86.9</td></tr></tbody></table>

To reproduce official Kimi-K2.6 benchmark results, we recommend using the official API. For third-party providers, refer to Kimi Vendor Verifier (KVV) to choose high-accuracy services. Details: [https://kimi.com/blog/kimi-vendor-verifier](https://kimi.com/blog/kimi-vendor-verifier)

**1\. General Testing Details**

- We report results for Kimi K2.6 and Kimi K2.5 with thinking mode enabled, Claude Opus 4.6 with max effort, GPT-5.4 with xhigh reasoning effort, and Gemini 3.1 Pro with a high thinking level.
- Unless otherwise specified, all Kimi K2.6 experiments were conducted with temperature = 1.0, top-p = 1.0, and a context length of 262,144 tokens.
- Benchmarks without publicly available scores were re-evaluated under the same conditions used for Kimi K2.6 and are marked with an asterisk (\*). Except where noted with an asterisk, all other results are cited from official reports.

**2\. Reasoning Benchmarks**

- IMO-AnswerBench scores for GPT-5.4 and Claude 4.6 were obtained from [https://z.ai/blog/glm-5.1](https://z.ai/blog/glm-5.1).
- Humanity's Last Exam (HLE) and other reasoning tasks were evaluated with a maximum generation length of 98,304 tokens. By default, we report results on the HLE full set. For the text-only subset, Kimi K2.6 achieves 36.4% accuracy without tools and 55.5% with tools.

**3\. Tool-Augmented / Agentic Tasks**

- Kimi K2.6 was equipped with search, code-interpreter, and web-browsing tools for HLE with tools, BrowseComp, DeepSearchQA, and WideSearch.
- For HLE-Full with tools, the maximum generation length is 262,144 tokens with a per-step limit of 49,152 tokens. We employ a simple context management strategy: once the context window exceeds the threshold, only the most recent round of tool-related messages is retained.
- For BrowseComp, we report scores obtained with context management using the same discard-all strategy as Kimi K2.5 and DeepSeek-V3.2.
- For DeepSearchQA, no context management was applied to Kimi K2.6 tests, and tasks exceeding the supported context length were directly counted as failed. Scores for Claude Opus 4.6, GPT-5.4, and Gemini 3.1 Pro on DeepSearchQA are cited from the [Claude Opus 4.7 System Card](https://cdn.sanity.io/files/4zrzovbb/website/037f06850df7fbe871e206dad004c3db5fd50340.pdf).
- For WideSearch, we report results under the "hide tool result" context management setting. Once the context window exceeds the threshold, only the most recent round of tool-related messages is retained.
- The test system prompts are identical to those used in the [Kimi K2.5 technical report](https://arxiv.org/pdf/2602.02276).
- Claw Eval was conducted using version 1.1 with max-tokens-per-step = 16384.
- For APEX-Agents, we evaluate 452 tasks from the public 480-task release, as done by [Artificial Analysis](https://artificialanalysis.ai/evaluations/apex-agents-aa) (excluding Investment Banking Worlds 244 and 246, which have external runtime dependencies).

**4\. Coding Tasks**

- Terminal-Bench 2.0 scores were obtained with the default agent framework (Terminus-2) and the provided JSON parser, operating in preserve thinking mode.
- For the SWE-Bench series of evaluations (including Verified, Multilingual, and Pro), we used an in-house evaluation framework adapted from SWE-agent. This framework includes a minimal set of tools—bash tool, createfile tool, insert tool, view tool, strreplace tool, and submit tool.
- All reported scores for coding tasks are averaged over 10 independent runs.

**5\. Vision Benchmarks**

- Max-tokens = 98,304, averaged over three runs (avg@3).
- Settings with Python tool use max-tokens-per-step = 65,536 and max-steps = 50 for multi-step reasoning.
- MMMU-Pro follows the official protocol, preserving input order and prepending images.