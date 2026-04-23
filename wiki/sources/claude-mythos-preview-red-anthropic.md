---
title: Claude Mythos Preview Cybersecurity Capabilities
type: source
tags: [ai, security, anthropic, mythos, cybersecurity, zero-day, exploit]
created: 2026-04-22
updated: 2026-04-22
sources: [Claude Mythos Preview.md]
---

# Claude Mythos Preview Cybersecurity Capabilities

**Source:** <https://red.anthropic.com/2026/mythos-preview/> — Nicholas Carlini, Newton Cheng, Keane Lucas, Michael Moore, Milad Nasr, Vinay Prabhushankar, Winnie Xiao et al. Assessment of [[claude-mythos-preview|Claude Mythos Preview]]'s cybersecurity capabilities, published alongside the [[project-glasswing|Project Glasswing]] announcement.

## Key claims

1. **Mythos Preview finds and exploits zero-day vulnerabilities in every major OS and browser** — fully autonomously, using a simple agentic scaffold (container + [[claude-code|Claude Code]] + "find a vulnerability" prompt). No human intervention after initial prompt.
2. **Cyber capabilities were not explicitly trained** — they *emerged* as a downstream consequence of general improvements in code, reasoning, and autonomy. Same improvements that make the model better at patching also make it better at exploiting.
3. **Opus 4.6 → Mythos Preview is a qualitative jump**: Opus 4.6 turned Firefox 147 JS engine vulns into working exploits 2 out of several hundred attempts. Mythos Preview: 181 working exploits + 29 register controls. Opus 4.6 achieved zero tier-5 (control flow hijack) crashes on OSS-Fuzz corpus; Mythos Preview achieved 10.
4. **Will not be made generally available** — [[anthropic|Anthropic]] restricts release via [[project-glasswing|Project Glasswing]] to critical industry partners and open source developers while cyber safeguards mature.

## Scaffold methodology

1. Container (internet-isolated) runs project-under-test + source code.
2. [[claude-code|Claude Code]] with Mythos Preview, prompted "find a security vulnerability."
3. Each agent focuses on a different file; files pre-ranked by likelihood of containing bugs (1–5 scale).
4. Agent reads code, hypothesizes vulns, runs project to confirm/reject, iterates with debuggers.
5. Final validation agent filters "real and interesting" vs trivial.
6. Perfect crash oracle via Address Sanitizer — zero false positives encountered.

## Notable case studies

### OpenBSD SACK (27-year-old bug)
NULL-pointer dereference via signed integer overflow in TCP SACK implementation. Two chained bugs: (1) no validation of SACK block start position; (2) single SACK block deletes only hole and triggers append through NULL pointer. Cost: <$50 for the successful run, <$20K across 1000 runs.

### FFmpeg H.264 (16-year-old bug)
16-bit sentinel collision: `memset(..., -1, ...)` initializes slice-ownership table to 65535 (sentinel); frame with 65536 slices makes slice 65535 collide with sentinel → out-of-bounds write. Bug introduced 2003, made exploitable by 2010 refactor. Found despite entire research papers on fuzzing this exact library.

### FreeBSD NFS root RCE (CVE-2026-4747, 17-year-old bug)
Fully autonomous discovery + exploitation. Stack buffer overflow in RPCSEC_GSS → 304-byte overwrite → ROP chain split over 6 RPC packets → appends attacker's SSH public key to `/root/.ssh/authorized_keys`. No stack canary (`int32_t[32]` not `char[]`), no KASLR for kernel, hostid/bootime leakable via NFSv4 EXCHANGE_ID.

### Linux kernel privilege escalation
Mythos Preview chains 2–4 vulnerabilities: KASLR bypass → struct read → use-after-free → heap spray → root. Nearly a dozen successful chains. Could NOT exploit OOB write vulns due to Linux defense-in-depth (unlike simpler stacks).

### Browser JIT heap sprays
Multi-browser: discovered read/write primitives, chained into JIT heap spray. In one case: cross-origin bypass. In another: sandbox escape + kernel write = "visit webpage → kernel compromise."

### Memory-safe VMM guest-to-host corruption
Vulnerability in `unsafe` block of a Rust/Java/Python VMM → guest gets out-of-bounds write to host memory. Exploit not achieved but DoS confirmed.

### Cryptography libraries
Weaknesses in TLS, AES-GCM, SSH implementations across popular libraries. Includes a critical Botan cert-auth bypass (GHSA-v782-6fq4-q827).

### N-day exploits (fully disclosed in post)
Two detailed walkthroughs of Mythos Preview autonomously writing Linux kernel privilege escalation exploits from CVE identifiers: (1) one-bit adjacent-physical-page write via netfilter ipset → PTE R/W bit flip → writable `/usr/bin/passwd` mapping → root; (2) one-byte read via Unix socket OOB UAF → arbitrary kernel read → cross-cache reclaim → fake `struct cred` via `AF_PACKET` ring → root. Both <$2000, <1 day.

## Scale of findings

- **Thousands** of high/critical severity vulnerabilities identified, undergoing coordinated disclosure.
- **89% exact agreement** between Mythos Preview severity assessments and human validators (198 reviewed); 98% within one level.
- If trends hold: 1000+ critical, thousands more high severity.
- False positive rate: **zero** on memory corruption findings (ASan oracle).

## Defensive recommendations

1. **Use current frontier models now** (Opus 4.6 still finds high/critical bugs everywhere).
2. **Shorten patch cycles** — N-day exploits now generated autonomously in hours from CVE + git hash.
3. **Review vulnerability disclosure policies** for ML-scale bug discovery.
4. **Automate incident response pipelines** — models should triage, summarize, prioritize, draft postmortems.
5. **Expedite mitigation strategy** for legacy/critical software.
6. **Defense-in-depth friction-based mitigations weaken** — language models grind through tedium quickly; hard barriers (KASLR, W^X) remain important.

## Key quote

> "The trajectory is clear. Just a few months ago, language models were only able to exploit fairly unsophisticated vulnerabilities. Just a few months before that, they were unable to identify any nontrivial vulnerabilities at all."

## See also

- [[claude-mythos-preview]]
- [[project-glasswing]]
- [[model-cyber-capability-emergence]]
- [[agent-runtime-untrusted]]
- [[anthropic]]
