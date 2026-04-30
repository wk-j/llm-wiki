---
title: ทำไม AI ช่วยให้เขียนโค้ดเร็วขึ้น 10 เท่า แต่โปรเจกต์ยังเสร็จช้าเท่าเดิม?
type: source
tags: [ai-productivity, project-management, software-delivery, lean, bottleneck, lead-time]
created: 2026-04-28
updated: 2026-04-28
author: "[[jeeraphan-lairat|Jeeraphan Lairat]]"
url: "https://sharing.senestia.com/https-medium-com-jeeraphan-lairat-b54bf07c99ff"
---

# ทำไม AI ช่วยให้เขียนโค้ดเร็วขึ้น 10 เท่า แต่โปรเจกต์ยังเสร็จช้าเท่าเดิม?

Source article by [[jeeraphan-lairat|Jeeraphan Lairat]] from [[senestia|Senestia]] discussing why the 10x productivity boost in coding provided by LLMs often fails to translate into faster project delivery (Lead Time).

## Key Takeaways

### 1. The Bottleneck Trap (Theory of Constraints)
- Process speed is determined by the slowest part ([[theory-of-constraints|Bottleneck]]).
- Coding is often only ~10% of the total delivery time.
- Speeding up coding without fixing wait times is a [[local-optimization-trap|Local Optimization Trap]].

### 2. Wait Time is the Real Enemy
- Code might be done in 30 minutes, but it sits in "Ready to Test" or "Code Review" for 3 days.
- AI acceleration just creates a larger pile of work-in-progress ([[limit-wip|WIP]]) at the next bottleneck.

### 3. Making Bottlenecks Visible
- Track the duration work spends in each stage.
- Identifying that work "sleeps" in certain stages (e.g., \`Ready to Test\` average of 2.8 days) is the first step to fixing it.

### 4. Proposed Solutions
- **Break Down Tasks:** Smaller tasks (1-2 days) to enable faster reviews and testing.
- **[[shift-left-testing|Shift-Left Testing]]:** Prepare test cases during planning, before coding starts.
- **Self-Testing:** Developers run prepared test cases themselves immediately after implementation to get instant feedback.
- **[[limit-wip|Limit WIP]]:** "Stop Starting, Start Finishing" — prioritize closing existing tasks over starting new ones with AI.

## Related
- [[lead-time]]
- [[alignment-bottleneck]]
- [[harness-engineering]] (Ryan Lopopolo's view on code abundance)
