# Accelerating Gemma 4: Multi-Token Prediction Drafters

Source: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
Publication date: 2026-05-05
Authors: Olivier Lacombe (Director, Product Management), Maarten Grootendorst (Developer Relations Engineer)

## Overview

Google announced Multi-Token Prediction (MTP) drafters for the Gemma 4 model family, achieving "up to a 3x speedup without any degradation in output quality or reasoning logic."

## Key Technical Claims

The Problem: Standard LLM inference is memory-bandwidth constrained. The processor spends most time transferring billions of parameters from VRAM to compute units for generating single tokens, resulting in underutilized compute and high latency.

The Solution: Speculative decoding pairs a heavy target model (e.g., Gemma 4 31B) with a lightweight drafter. The drafter predicts multiple future tokens while the target model processes one token, then the target model verifies all suggestions in parallel.

## Technical Architecture Details

- Draft models utilize the target model's activations and share its KV cache
- Efficient clustering implemented in embedders for E2B and E4B edge models
- Apple Silicon achieves ~2.2x speedup at batch sizes of 4-8
- Similar gains observed with Nvidia A100 when increasing batch size

## Supported Frameworks & Platforms

- Hugging Face Transformers
- MLX
- vLLM
- SGLang
- Ollama
- LiteRT-LM
- Google AI Edge Gallery (Android/iOS)

## Developer Benefits

"Drastically reduce latency for near real-time chat, immersive voice applications and agentic workflows" while maintaining "identical frontier-class reasoning and accuracy."

## Availability

Released under Apache 2.0 license with documentation and model weights available on Hugging Face and Kaggle.
