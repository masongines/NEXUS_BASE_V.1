# CODEX_SKILL_CANDIDATES_v1

**Classification:** Auxiliary Workflow Planning / Non-Doctrinal  
**Authority:** Advisory / Operator-Governed  
**Status:** Active Auxiliary Planning Artifact  
**Scope:** First three Codex skill candidates for NEXUS workflow support

---

## I. PURPOSE

This artifact defines the first three Codex skill candidates that are most aligned with current NEXUS workflow reality.

These skills are intended to improve repeatable review and planning work without widening authority, execution, or memory boundaries.

These skills are not:

- doctrine
- implementation approval
- autonomous execution policy
- memory authority
- project truth

---

## II. SELECTION RULE

The first Codex skills should be chosen by these criteria:

- already repeated often in real NEXUS work
- low risk of authority inflation
- useful across multiple lanes
- supportive of checkpoints, planning, and review
- bounded enough to avoid hidden automation pressure

---

## III. SKILL CANDIDATE 1

# STRUCTURAL_INTAKE_REVIEW_SKILL_v1

## Purpose
Run a controlled intake review on files, folders, exports, legacy material, PRE_DRAFT material, or auxiliary tooling material.

## Core function
Classify incoming material into:
- place now
- reference only
- experiment only
- defer

## Best use cases
- legacy intake
- PRE_DRAFT intake
- auxiliary tooling intake
- external project ancestor/reference review
- loose material triage before placement

## Required output pattern
- source root
- material type
- classification result
- placement recommendation
- reasoning
- target path
- risk notes
- approval requirement
- next step

## Why it is high-value
This is already one of the most repeated and useful NEXUS workflows.

## Risk level
Low

## Current status
**Best candidate for first skill set**

---

## IV. SKILL CANDIDATE 2

# CHECKPOINT_AUDIT_SKILL_v1

## Purpose
Run a bounded checkpoint audit on the current state of a lane, milestone, or work phase.

## Core function
Evaluate:
- what is complete
- what is partially complete
- what remains deferred
- whether the current state is stable enough to checkpoint
- what should happen next

## Best use cases
- wave completion review
- implementation pass review
- generator/control lane checkpoint review
- foundation checkpoint review
- auxiliary task checkpoint review

## Required output pattern
- current state
- what is confirmed
- what is bounded
- what remains open
- milestone-worthiness
- structural issue
- proposed correction
- dependency impact
- approval required
- next step

## Why it is high-value
This directly supports the checkpoint/milestone culture of NEXUS.

## Risk level
Low

## Current status
**Best candidate for first skill set**

---

## V. SKILL CANDIDATE 3

# IMPLEMENTATION_LANE_REVIEW_SKILL_v1

## Purpose
Determine whether a lane is:
- placeholder
- near-ready
- ready with conditions
- hold
- defer

## Core function
Review:
- source basis
- scope ceiling
- readiness evidence
- verification path
- missing prerequisites
- correct first objective

## Best use cases
- control lane
- generators lane
- later runtime lane
- later API lane
- future connector/MCP lane

## Required output pattern
- lane
- current readiness
- source basis
- scope ceiling
- verification path
- what is in place
- what is missing
- readiness verdict
- recommended first objective
- approval required
- next step

## Why it is high-value
This is one of the strongest reusable workflows in the system because it prevents placeholder inflation and premature implementation.

## Risk level
Low to moderate, but still safe if kept review-only

## Current status
**Best candidate for first skill set**

---

## VI. COMMON GUARDRAILS FOR ALL THREE SKILLS

These skills may:

- support review
- support classification
- support bounded planning
- support checkpoint discipline

These skills may not:

- replace NEXUS artifacts as project truth
- approve implementation automatically
- mutate files
- promote doctrine
- become memory authority
- widen execution boundaries by convenience

Strong rule:
**Skills improve workflow support. They do not become governance authority.**

---

## VII. RECOMMENDED ORDER OF REAL USE

1. STRUCTURAL_INTAKE_REVIEW_SKILL_v1
2. CHECKPOINT_AUDIT_SKILL_v1
3. IMPLEMENTATION_LANE_REVIEW_SKILL_v1

This is the best order because it follows the real operating rhythm of NEXUS:
- intake
- checkpoint
- readiness

---

## VIII. END STATE

The intended end state of these first three skill candidates is to give Codex a reusable, bounded, low-risk workflow layer that improves NEXUS review speed and consistency without introducing hidden authority, hidden memory trust, or hidden execution behavior.