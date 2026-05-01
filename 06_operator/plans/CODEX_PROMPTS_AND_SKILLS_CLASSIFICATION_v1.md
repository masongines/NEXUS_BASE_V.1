# CODEX_PROMPTS_AND_SKILLS_CLASSIFICATION_v1

**Classification:** Auxiliary Workflow Policy / Non-Doctrinal  
**Authority:** Advisory / Operator-Governed  
**Status:** Active Auxiliary Planning Artifact  
**Scope:** Define which Codex prompts and skills are appropriate for NEXUS now, what they should do, and what should remain deferred

---

## I. PURPOSE

This artifact classifies Codex prompt and skill candidates for use inside the NEXUS workspace.

It exists to:

- identify high-value reusable workflows
- prevent Codex customization from silently becoming project truth
- separate immediate-use workflows from planning-only workflows
- preserve boundary discipline while increasing workflow efficiency

This artifact is not:

- doctrine
- implementation approval
- memory-policy approval
- agent autonomy approval
- MCP activation approval

---

## II. ROLE OF PROMPTS VS SKILLS

### Prompts
Prompts are lightweight reusable interaction patterns.

Best for:
- one-off structured reviews
- recurring analysis formats
- checkpoint discussions
- intake review passes

### Skills
Skills are more stable reusable workflow packages.

Best for:
- repeatable multi-step review flows
- structured project assistance sequences
- standardized packet or checkpoint preparation
- bounded coding/review workflows

### Strong distinction
Prompts help shape a conversation.  
Skills help shape a reusable workflow.

---

## III. IMMEDIATE CLASSIFICATION SUMMARY

### Discuss now
- D&R review prompt
- intake review prompt
- milestone review prompt
- checkpoint debrief prompt
- readiness packet review prompt
- structural intake review skill
- checkpoint audit skill
- implementation-lane review skill
- D&R refinement skill

### Planning-grade
- multi-artifact comparison skill
- code-lane starter-package skill
- generator/control lane verification skill
- limited MCP-assisted documentation skill

### Experiment-only
- hooks-backed workflow skills
- memory-dependent skills
- auto-follow-up skills
- agent-like self-expanding skills

### Deferred
- autonomous execution skills
- system-control skills
- cross-app memory skills
- plugin-bundled workflow packs

---

## IV. PROMPTS — DISCUSS NOW

## A. D&R Review Prompt
### Purpose
Run a Deconstruct → Review → Reconstruct pass on a system artifact, proposal, or lane.

### Good use cases
- architecture review
- packet review
- policy review
- lane review
- debrief after implementation step

### Why it is high-value
This is the clearest reusable reasoning pattern in the whole NEXUS system.

### Risk
Low, if it remains review-only.

### Classification
**Discuss now**

---

## B. Intake Review Prompt
### Purpose
Classify incoming files/folders/material into:
- place now
- reference only
- experiments
- defer

### Good use cases
- legacy intake
- PRE_DRAFT intake
- auxiliary material intake
- tool/reference bundle intake

### Why it is high-value
This has already been one of the most repeated and useful workflows in Base V1.

### Classification
**Discuss now**

---

## C. Milestone Review Prompt
### Purpose
Review whether a recent pass/result is milestone-worthy, what it proves, and what it does not prove.

### Good use cases
- preflight pass
- generator pass
- structural checkpoint
- lane-readiness lock

### Why it is high-value
It supports your checkpoint culture and reduces drift after successful work.

### Classification
**Discuss now**

---

## D. Checkpoint Debrief Prompt
### Purpose
Summarize current state, structural issue, proposed correction, dependency impact, approval requirement, and next step.

### Good use cases
- after any wave
- after any pass/fail result
- after any review checkpoint

### Why it is high-value
This is already a stable NEXUS response pattern.

### Classification
**Discuss now**

---

## E. Readiness Packet Review Prompt
### Purpose
Stress-test a lane readiness packet before code begins.

### Good use cases
- control lane
- generators lane
- later runtime lane
- future MCP/tooling lane

### Why it is high-value
This preserves readiness-before-implementation discipline.

### Classification
**Discuss now**

---

## V. SKILLS — DISCUSS NOW

## A. Structural Intake Review Skill
### Purpose
Guide repeatable intake classification for external materials.

### Workflow shape
1. identify source root
2. classify by lane/value/risk
3. recommend placement or defer status
4. produce a controlled intake recommendation

### Why it is strong
This is highly reusable and low-risk.

### Classification
**Discuss now**

---

## B. Checkpoint Audit Skill
### Purpose
Run a bounded checkpoint review on a current lane or build phase.

### Workflow shape
1. inspect current state
2. identify what is complete
3. identify what remains bounded or deferred
4. recommend next move

### Why it is strong
This directly supports Base V1’s milestone architecture.

### Classification
**Discuss now**

---

## C. Implementation-Lane Review Skill
### Purpose
Review whether a lane is at:
- placeholder
- ready with conditions
- near-ready
- hold
- defer

### Workflow shape
1. inspect structure
2. inspect source basis
3. inspect scope ceiling
4. inspect verification path
5. issue readiness verdict

### Why it is strong
This is one of the best reusable NEXUS workflows.

### Classification
**Discuss now**

---

## D. D&R Refinement Skill
### Purpose
Apply D&R to a draft, output, or packet and propose the tighter reconstructed form.

### Workflow shape
1. deconstruct to first principles
2. identify strengths and failure points
3. reconstruct better bounded version
4. recommend retain / revise / defer result

### Why it is strong
It matches your stated operating style directly.

### Classification
**Discuss now**

---

## VI. PLANNING-GRADE SKILLS

## A. Multi-Artifact Comparison Skill
### Purpose
Compare multiple packets, artifacts, or candidate structures at once.

### Reason for caution
Useful, but can blur source hierarchy if overused.

### Classification
**Planning-grade**

---

## B. Starter-Package Builder Skill
### Purpose
Generate starter-package components for a lane after readiness lock.

### Reason for caution
Very useful, but should follow lane approval, not precede it.

### Classification
**Planning-grade**

---

## C. Generator / Control Verification Skill
### Purpose
Review bounded implementation results against packet and checklist expectations.

### Reason for caution
Good later, but should not become a hidden code-authority layer.

### Classification
**Planning-grade**

---

## D. MCP-Assisted Documentation Skill
### Purpose
Use a future read-only docs MCP source to improve documentation-grounded coding help.

### Reason for caution
Potentially valuable, but connector policy must exist first.

### Classification
**Planning-grade**

---

## VII. EXPERIMENT-ONLY WORKFLOWS

## A. Hook-Based Workflows
Hooks introduce hidden lifecycle behavior and should not be active by default.

### Classification
**Experiment-only**

## B. Memory-Dependent Workflows
Any workflow that assumes persistent recall or cross-session memory authority belongs in sandbox first.

### Classification
**Experiment-only**

## C. Auto-Follow-Up Workflows
Anything that self-continues without explicit checkpoint approval is too risky for current NEXUS discipline.

### Classification
**Experiment-only**

---

## VIII. DEFERRED WORKFLOWS

These should remain deferred:

- autonomous execution skills
- system-control skills
- cross-app memory skills
- plugin-bundled workflow packs
- agent-managed file mutation workflows
- silent connector-trigger workflows

Reason:
They widen authority, execution, or memory boundaries too early.

---

## IX. RECOMMENDED FIRST PROMPT SET

If you want a minimal first working prompt set, I recommend these four:

1. D&R Review Prompt
2. Intake Review Prompt
3. Milestone Review Prompt
4. Readiness Packet Review Prompt

These are the highest-value, lowest-risk Codex prompt candidates.

---

## X. RECOMMENDED FIRST SKILL SET

If you want a minimal first working skill set, I recommend these three:

1. Structural Intake Review Skill
2. Checkpoint Audit Skill
3. Implementation-Lane Review Skill

These are the strongest reusable workflows for NEXUS right now.

---

## XI. STRONG RULE

Prompts and skills may improve Codex workflow support.

They may not:

- replace NEXUS artifacts as project truth
- override readiness packets
- widen execution behavior by convenience
- become memory authority
- silently define policy

---

## XII. END STATE

The intended end state of this artifact is to let Codex become more useful inside NEXUS through reusable prompts and skills, while preserving the rule that workflows remain subordinate to the project’s explicit artifacts, checkpoints, and governance structure.