# PRE_POST_ACTION_REVIEW_STANDARD_v1

**Classification:** Process Standard / Non-Doctrinal  
**Authority:** Advisory / Operator-Governed  
**Status:** Active Process Hardening Standard  
**Scope:** Define the before/after action review structure used for significant NEXUS operations

---

## I. PURPOSE

This standard exists to reduce:

- fatigue-driven shortcut risk
- complexity drift
- weak traceability
- silent structural change
- confusion about what changed, why, and with what consequence

It creates a repeatable process for capturing:

- the state before an action
- the action itself
- the state after the action
- the delta between the two
- the lessons and reconstruction value produced by the action

This standard is not:

- doctrine
- implementation approval
- automatic logging policy
- mandatory for trivial edits

It is intended for actions that materially affect:

- structure
- placement
- readiness
- implementation-bearing lanes
- naming/path changes
- consolidation work
- tooling policy
- migration behavior

---

## II. CORE PRINCIPLE

NEXUS should not merely do actions.

NEXUS should preserve a legible record of:

- what was true before
- what was attempted
- what changed
- what was learned
- what should happen next

This supports both:

- system accountability
- operator accountability support

The operator remains free to approve, reject, or defer.
This standard exists to make that choice safer and more intelligible.

---

## III. WHEN TO USE THIS STANDARD

Use this standard when an action is:

- structurally meaningful
- implementation-bearing
- migration-related
- naming/path changing
- checkpoint-worthy
- likely to affect future interpretation
- likely to create rollback need
- likely to benefit from explicit D&R review

Examples:

- readiness packet to starter package transition
- first implementation-bearing code draft
- checkpoint/milestone record after a pass
- migration register cleanup
- folder/file rename or move pass
- auxiliary tooling policy adoption
- consolidation or archive decision

Do not require this standard for:
- trivial typo correction
- cosmetic wording changes with no structural effect
- routine note edits unless they are part of a larger action wave

---

## IV. FIVE-PART ACTION MODEL

Each qualifying action should be captured in five parts:

1. Pre-Check
2. Action Record
3. Post-Check
4. Delta Review
5. Reconstruction Note

This is the default NEXUS before/after discipline.

---

## V. PRE-CHECK

### Purpose
Freeze the baseline before the action.

### Required fields
- Action Name
- Date / Time
- Lane or Scope
- Objective
- Source Basis
- Authority Basis
- Dependencies
- Current State
- Known Risks
- Expected Outcome
- Approval Basis

### Rule
No action should be treated as “cleanly understood” unless its pre-state is made explicit enough to compare against later.

---

## VI. ACTION RECORD

### Purpose
Record what was actually done.

### Required fields
- Action Executed
- Exact File(s) or Folder(s) Touched
- Exact Script / Command Used
- Output Path(s) Affected
- Actor
  - operator
  - AI-prepared
  - hybrid
- Execution Result
- Raw Console Output Reference
- Notes on Unexpected Behavior

### Rule
This section should describe the action, not reinterpret it.

---

## VII. POST-CHECK

### Purpose
Capture the immediate state after the action.

### Required fields
- Expected Outcome
- Actual Outcome
- PASS / WATCHLIST / INTERVENTION_REQUIRED
- Result Summary
- Structural Effect
- New Risks Introduced
- Rollback Need: Yes/No
- Checkpoint Worthy: Yes/No

### Rule
The post-check is where the system determines whether the action achieved what it was supposed to achieve.

---

## VIII. DELTA REVIEW

### Purpose
Identify the meaningful difference between before and after.

### Required fields
- What Changed
- What Stayed the Same
- What Was Confirmed
- What Broke or Drifted
- What Was Clarified
- What Increased Complexity
- What Reduced Complexity

### Rule
The delta section is not a narrative summary.
It is the structured answer to: “What materially changed?”

---

## IX. RECONSTRUCTION NOTE

### Purpose
Apply D&R logic and extract the most useful system learning.

### Required fields
- Core Lesson
- What Should Be Preserved
- What Should Be Tightened
- What Should Be Deferred
- Whether the Action Improved:
  - clarity
  - control
  - traceability
  - future readiness
- Best Next Step

### Rule
This is the reconstruction layer.
It turns an action from “something that happened” into “something the system learned from.”

---

## X. STATUS LANGUAGE

Use the following result language consistently when appropriate:

- PASS
- WATCHLIST
- INTERVENTION_REQUIRED

For readiness or lane review, use explicit lane-state language such as:

- PLACEHOLDER
- NEAR_READY
- READY_WITH_CONDITIONS
- HOLD
- DEFER

Do not invent new status classes casually.

---

## XI. NAMING / PATH CHANGE RULE

For any rename/move/restructure action, this standard becomes especially important.

### Additional required fields for rename/move actions
- Previous Name/Path
- New Name/Path
- Reason for Change
- Expected Improvement
- Risk of Linkage or Reference Breakage
- Whether a Mapping Record is Needed

### Strong rule
No broad naming/path normalization pass should occur without pre/post action capture.

This is because naming/path changes affect:

- retrieval
- scripts
- human review speed
- milestone traceability
- future consolidation logic

---

## XII. CONSOLIDATION RULE

As Base V1 grows, checkpoints, packets, logs, review artifacts, and support surfaces will accumulate.

This standard should later support a consolidation discipline based on:

- preserve
- compress
- archive
- supersede
- retire

### Future note
A later consolidation policy may define category blocks, abbreviations, and compression rules.
That is valid, but it should be built on top of this review standard, not instead of it.

---

## XIII. MINIMUM TEMPLATE

Use this minimum template for most qualifying actions:

Action Name:
Date / Time:
Lane or Scope:
Objective:
Source Basis:
Authority Basis:
Dependencies:
Current State:
Known Risks:
Expected Outcome:
Approval Basis:

Action Executed:
Files/Folders Touched:
Script / Command Used:
Output Paths Affected:
Actor:
Execution Result:
Raw Output Reference:
Unexpected Behavior:

Expected Outcome:
Actual Outcome:
Result:
Structural Effect:
New Risks Introduced:
Rollback Need:
Checkpoint Worthy:

What Changed:
What Stayed the Same:
What Was Confirmed:
What Broke or Drifted:
What Was Clarified:
What Increased Complexity:
What Reduced Complexity:

Core Lesson:
What Should Be Preserved:
What Should Be Tightened:
What Should Be Deferred:
Improvement Assessment:
Best Next Step:

---

## XIV. END STATE

This standard exists to make future NEXUS actions more traceable, more reviewable, and more reconstructable.

Its intended end state is to reduce drift, reduce operator overload, and improve the system’s ability to evolve without losing clarity.