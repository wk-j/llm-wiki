---
title: "Mellum2 Goes Open Source: A Fast Model for AI Workflows | The JetBrains AI Blog"
source: "https://blog.jetbrains.com/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/"
author:
  - "[[Anton Semenkin]]"
  - "[[Nikita Pavlichenko]]"
published: 2026-06-01
created: 2026-06-05
description: "Trained from scratch and designed for practical deployment, Mellum2 is built for routing, Q&A, sub-agents, and private AI use in software engineering systems. Today, we’re open-sourcing Mellum2"
tags:
  - "clippings"
---
[News](https://blog.jetbrains.com/ai/category/news/)

## Mellum2 Goes Open Source: A Fast Model for AI Workflows

Read this post in other languages:

- [Deutsch](https://blog.jetbrains.com/de/ai/2026/06/mellum2-wird-open-source-ein-schnelles-modell-fuer-ki-workflows/)
,- [Español](https://blog.jetbrains.com/es/ai/2026/06/mellum2-se-pasa-al-codigo-abierto-un-modelo-rapido-para-flujos-de-trabajo-de-ia/)
,- [Français](https://blog.jetbrains.com/fr/ai/2026/06/mellum2-devient-open-source-un-modele-rapide-pour-les-workflows-d-ia/)
,- [日本語](https://blog.jetbrains.com/ja/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/)
,- [한국어](https://blog.jetbrains.com/ko/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/)
,- [简体中文](https://blog.jetbrains.com/zh-hans/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/)
,- [Português](https://blog.jetbrains.com/pt-br/ai/2026/06/o-mellum2-passa-a-ser-de-codigo-aberto-um-modelo-rapido-para-fluxos-de-trabalho-de-ia/)

**Trained from scratch and designed for practical deployment, Mellum2 is built for routing, Q&A, sub-agents, and private AI use in software engineering systems.**

Today, we’re open-sourcing Mellum2, a 12B model engineered to solve the hardest parts of production AI: latency, throughput, and cost. Built from scratch and released under the Apache 2.0 license, [Mellum2](https://www.jetbrains.com/mellum/) offers a high-performance, cost-efficient alternative for your infrastructure.

Mellum began with [code completion](https://blog.jetbrains.com/ai/2025/04/mellum-goes-open-source-a-purpose-built-llm-for-developers-now-on-hugging-face/); now we’ve evolved it to handle both natural language and code. It is now a versatile tool ready to power routing, summarization, and intermediate reasoning steps across your modern AI workflows.

Whether you want to experiment, fine-tune, or deploy at scale, Mellum2 is ready to run in your own systems.

## Architecture and performance

Mellum2 is engineered to solve the bottlenecks of production-scale systems through its architecture and focused, efficiency-driven design.

- **Mixture-of-Experts (MoE) design:** The model features 12B total parameters, but because it uses a MoE design, only 2.5B parameters are active per token. This reduces compute costs while enabling high-throughput, low-latency inference for real-time workloads.
- **Specialized focus:** Unlike many modern models, Mellum2 is not multimodal. It is trained specifically on natural language and code data. This specialization ensures the model excels in software engineering environments while remaining lean and fast.

In our [technical report](https://arxiv.org/abs/2605.31268), we detail our model’s performance across code generation, science, math, and reasoning benchmarks. Mellum2 is competitive with other similar-sized models while cutting inference time to less than half – a definitive advantage for production-grade deployments.

![](https://blog.jetbrains.com/wp-content/uploads/2026/05/Blog-1280x720-1-1.png)

## Key use cases for Mellum2

- **Route and orchestrate AI workloads:** Use Mellum2 to analyze incoming prompts and help select the right model or tool for each task.
- **Build low-latency RAG pipelines:** Retrieve relevant context, use Mellum2 to summarize it, and generate responses instantly.
- **Power fast sub-agents in complex workflows:** Break down agent pipelines into steps like context gathering, planning, and validation. Use Mellum2 for fast, specialized tasks instead of relying on a single large model.
- **Enable private, local AI deployment:** Run Mellum2 locally or self-host it to keep code and data fully under your control.

## The “focal model” philosophy: Why focused models scale better

As AI systems become more complex, performance bottlenecks shift from raw capability to latency, throughput, and cost at scale. Not every task requires the largest model. Many steps in modern AI systems are repetitive, latency-sensitive, and high-frequency. These steps benefit from a fast and reliable model that can be efficiently routed, hosted, and controlled.

At JetBrains, we believe the future belongs to coordinated systems, not single models. Frontier models will continue to push the limits, but practical AI products also require focal models: fast, specialized components that handle high-frequency tasks efficiently.

That’s the role we see for Mellum2 in the next generation of AI software tooling.

## Get started with Mellum2

If you’re building AI systems for software engineering – whether inside an IDE, in a RAG pipeline, as part of an agent workflow, or fully on your own infrastructure – we’d love for you to try Mellum2.

Open source is how better tools get made.