---
title: OWASP Autonomous Penetration Testing Standard (APTS)
type: source
tags: [security, ai, agents, governance, owasp, pentesting, standard]
created: 2026-04-20
updated: 2026-04-20
sources: [OWASP APTS.md]
url: https://github.com/OWASP/APTS
version: v0.1.0
published: 2026
---

# OWASP APTS v0.1.0

OWASP Incubator project — a **governance standard** for autonomous penetration-testing platforms (vendor-delivered, service-operated, or built in-house by enterprise security teams). Licensed CC BY-SA 4.0. Project leads: Jinson Varghese Behanan, Shikhil Sharma.

APTS is explicitly **not a testing methodology** — it complements PTES, OWASP WSTG, and OSSTMM. It addresses problems unique to autonomous operation: scope enforcement, safe autonomy, manipulation resistance, and accountability.

## 173 tier-required requirements across 8 domains

| # | Domain | Prefix | Reqs | Focus |
|---|---|---|---|---|
| 1 | Scope Enforcement | `SE` | 26 | Boundary definition, validation, continuous monitoring |
| 2 | Safety Controls & Impact Mgmt | `SC` | 20 | Impact classification, blast radius, kill switches, rollback, execution sandbox |
| 3 | Human Oversight & Intervention | `HO` | 19 | Approval gates, escalation, operator qualifications |
| 4 | Graduated Autonomy Levels | `AL` | 28 | L1 Assisted → L4 Autonomous, level assessment, containment verification |
| 5 | Auditability & Reproducibility | `AR` | 20 | Decision trails, evidence integrity, audit-trail isolation |
| 6 | Manipulation Resistance | `MR` | 23 | Prompt injection, scope widening, model poisoning, agent-runtime isolation |
| 7 | Third-Party & Supply Chain Trust | `TP` | 22 | AI providers, data handling, multi-tenancy, foundation-model disclosure |
| 8 | Reporting | `RP` | 15 | Finding validation, confidence scoring, coverage disclosure |

Plus 10 advisory practices under the `APTS-<DOMAIN>-A0x` pattern (not counted toward conformance).

## Three cumulative compliance tiers

- **Tier 1 — Foundation (72 reqs).** Scope-bounded, stoppable, basic audit trail. Baseline for supervised autonomous testing of non-critical systems.
- **Tier 2 — Verified (85 additional, 157 cumulative).** Tamper-proof audit trails, decision transparency, reproducible findings. Production / regulated industries.
- **Tier 3 — Comprehensive (16 additional, 173 cumulative).** Continuous integrity monitoring, evasion governance, L4 campaign management, red-team validation. Critical infrastructure and full L4 operation.

No certification body, no mandatory audit, no fee. Assessment path (self / internal review / third-party) is left to the adopter. Reference format: `APTS-SE-001` or versioned `APTS-v0.1.0-SE-001`.

## Graduated autonomy: L1 – L4 (the AL domain)

The central safety mechanism of the standard — a platform's autonomy must be matched by proportionate oversight, boundary enforcement, and audit coverage. See [[graduated-autonomy]].

| Level | Name | Human role | Platform authority |
|---|---|---|---|
| **L1** | Assisted | Commands every action | One technique per command, no chaining |
| **L2** | Supervised | Approves at each phase boundary | Chains techniques *within* a phase |
| **L3** | Semi-Autonomous | Sets boundaries; intervenes on exceptions | Executes complete attack chains inside pre-approved bounds |
| **L4** | Autonomous | Reviews periodically (weekly / monthly / quarterly / annual) | Manages multi-target campaigns; dynamic scope; adaptive strategy |

Canonical phase model used throughout the standard: **Reconnaissance → Enumeration → Identification → Exploitation → Post-Exploitation → Reporting.**

**Tier ≠ Level.** Tier = conformance posture (which reqs are met). Level = operational mode (how much the platform does alone). Tier 1 ≈ L1, Tier 2 → L2/L3, Tier 3 → L4. Some level-specific requirements appear at lower tiers because they apply to any platform that *offers* that level.

## Capability frontier and containment assumption (net-new framing)

The Introduction's "Capability Frontier and Containment Assumptions" section encodes the standard's architectural stance, summarized in [[agent-runtime-untrusted]]:

> APTS does not try to verify that a foundation model is aligned, cannot scheme, or will not attempt to exceed its mandate. These properties cannot be reliably verified by platform operators today, and a standard that claimed otherwise would give customers false assurance. APTS instead takes an architectural stance: treat the agent runtime as a component that may, for any reason, attempt actions outside its declared mandate, and build the platform so that such attempts fail by construction rather than by the agent's own restraint.

Concrete requirements that encode the stance:

- **APTS-SC-019** — kernel-enforced execution sandbox whose boundary the agent runtime has no credentials to move
- **APTS-SC-020** — tool / action allowlist enforced by a component **external to the model**, not by system prompt
- **APTS-MR-023** — agent runtime named as an untrusted component in the threat model
- **APTS-AR-020** — authoritative audit trail lives on infrastructure the agent runtime cannot reach
- **APTS-AL-028** — periodic operator-run containment verification at L3/L4
- **APTS-TP-021 / APTS-TP-022** — disclose the foundation model powering the agent; re-assess when it changes materially
- **APTS-SE-026** — monitor the agent's action distribution for deviations *inside* scope but outside expected behavior

## Relationship to other standards

- **Testing methodology:** PTES, WSTG, OSSTMM (autonomous systems should follow these while under APTS governance)
- **AppSec:** OWASP ASVS, OWASP Top 10 (what the autonomous system tests)
- **Governance:** NIST CSF, ISO 27001, NIST AI RMF, SOC 2, PCI DSS, GDPR
- **Agentic AI:** OWASP Top 10 for Agentic Applications (2026); Singapore IMDA Agentic AI Governance Framework
- **Regulation:** EU AI Act — APTS conformance does not constitute compliance, but HO / AR / RP domains overlap substantively

## Interpreting prescriptive values

Three categories:

1. **Safety-critical bounds** (kill-switch response times, process-termination timeouts): maximum acceptable values. No deviation.
2. **Regulatory minimums** (retention periods citing HIPAA / SOX): legal obligations regardless of APTS.
3. **Environment-dependent defaults** (payload size, bandwidth caps, scan rates): deviation permitted only if documented + validated + change-managed.

Default interpretation when not specified: treat as a bound unless the requirement explicitly uses *configurable*, *documented*, or *per the platform's policy*.

## Why this matters to this wiki

- Introduces a **governance vocabulary for autonomous agents** (L1–L4) that parallels harness-level permission controls like [[auto-mode]] at a much higher blast radius
- Formalizes the **agent-runtime-as-untrusted** pattern that the wiki has circled around — [[subagent-patterns|pipeline subagents]], [[advisor-strategy]] reviewers, [[harness-engineering]]'s audit-by-pipeline — but none of those sources stated the architectural stance as cleanly
- Provides the **OWASP/CC-BY-SA-4.0 authority** to cite when pushing back on vendor claims that system-prompt instructions alone constitute scope enforcement

## See also

- [[owasp]]
- [[graduated-autonomy]]
- [[agent-runtime-untrusted]]
- [[auto-mode]]
- [[harness-engineering]]
- [[subagent-patterns]]
- [[advisor-strategy]]
