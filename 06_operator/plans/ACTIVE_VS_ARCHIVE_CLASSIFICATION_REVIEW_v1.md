# ACTIVE_VS_ARCHIVE_CLASSIFICATION_REVIEW_v1

**Classification:** Process Review / Non-Doctrinal  
**Authority:** Advisory / Operator-Governed  
**Status:** Active Classification Review Artifact  
**Scope:** Define how NEXUS should distinguish active, stable-reference, and archive-worthy artifacts before later consolidation, compression, naming normalization, or rename/move actions occur

---

## I. PURPOSE

This review exists to determine which artifacts in NEXUS are:

- actively guiding current work
- still useful but no longer active
- historically important but no longer deserving active visibility
- deferred or experimental and therefore not part of the active operational surface

This review is necessary because Base V1 has now accumulated:

- checkpoints
- readiness packets
- starter packages
- policy packets
- process standards
- generated outputs
- reference materials
- legacy materials

Without classification, future consolidation or naming/path normalization may compress the wrong artifacts, hide active control surfaces, or preserve too much inactive weight in the active operating field.

This review is not:

- an archive action by itself
- a rename order
- a move order
- a deletion order
- a replacement for the consolidation strategy or naming/path review

It is the classification layer that should come before those actions.

---

## II. CORE PRINCIPLE

Not all preserved artifacts should remain equally visible.

NEXUS must preserve enough material for:

- rollback
- explanation
- comparison
- future reconstruction
- auditability

But it must also preserve enough clarity that the current active operating surfaces are easy to identify.

The main distinction this review exists to enforce is:

> useful history is not the same thing as current operational relevance

---

## III. REVIEW GOALS

This review should answer:

1. What is currently active and should stay visibly active?
2. What is stable reference and should remain visible but secondary?
3. What is archive-worthy and should later be moved out of the active field?
4. What is deferred/experimental and should remain clearly outside active operational truth?
5. What artifact families should later be classified together instead of one by one?
6. What must remain directly visible because it supports current operator stamina and system coherence?
7. What is currently creating active-field weight without enough current operational value?

---

## IV. PRIMARY CLASSIFICATION CATEGORIES

Every artifact under review should be placed into one of the following categories.

### A. ACTIVE OPERATIONAL
Artifacts that are actively guiding current NEXUS work and should remain easy to find in the active field.

Typical examples:
- current doctrine
- current active standards
- current support records with live interpretive value
- current readiness packets
- current starter packages
- current implementation-bearing code
- current process standards actively governing work
- current milestone/checkpoint records directly shaping next decisions

### B. ACTIVE SUPPORT
Artifacts that are not constitutional truth, but are currently useful enough that they still belong in the active visible field.

Typical examples:
- current policy packets
- current intake review notes if still feeding action
- current auxiliary planning artifacts
- current operator planning artifacts still actively referenced

### C. STABLE REFERENCE
Artifacts that remain useful and should stay preserved and visible, but are not part of the current active decision spine.

Typical examples:
- handoff packages still useful for context
- older but stable comparison artifacts
- ancestor-system translation notes
- historical support documents with ongoing reference value

### D. ARCHIVE-WORTHY
Artifacts that should remain preserved, but no longer deserve active visibility once reviewed.

Typical examples:
- older transition packages
- older milestone records superseded by stronger checkpoint chains
- older draft-side review artifacts replaced by stabilized versions
- completed phase bundles that are no longer needed for current navigation

### E. DEFERRED / EXPERIMENTAL
Artifacts that are not active now, but may matter later.

Typical examples:
- experiment concepts
- hardware/node future ideas
- tooling candidates
- memory/tooling packets not yet adopted
- future subsystem ideas derived from ancestor systems

---

## V. ACTIVE OPERATIONAL CRITERIA

An artifact should remain ACTIVE OPERATIONAL only if one or more of these are true:

- it directly affects current implementation decisions
- it defines current readiness or scope ceilings
- it is required to interpret the current state of the system
- it is a current checkpoint or milestone that still anchors active work
- it is part of the current working control spine
- later work would become riskier or less intelligible if it were demoted now

Strong rule:
Active operational artifacts should remain highly legible and easy to retrieve.

---

## VI. ACTIVE SUPPORT CRITERIA

An artifact should be ACTIVE SUPPORT if:

- it is not constitutional/system-truth-bearing
- but it is still currently used in planning, review, or controlled progression
- it helps current operator comprehension
- it meaningfully supports current decisions without being the main source of truth

These artifacts may remain in visible active planning lanes, but should not be mistaken for stronger authority classes.

---

## VII. STABLE REFERENCE CRITERIA

An artifact should be STABLE REFERENCE if:

- it is useful for context or lineage
- it may still inform future reasoning
- it is no longer actively controlling current work
- preserving it visibly is still helpful, but it should not compete with active control surfaces

Stable reference should remain accessible, but secondary.

---

## VIII. ARCHIVE-WORTHY CRITERIA

An artifact should be ARCHIVE-WORTHY if:

- it is preserved mainly for history, rollback, or audit lineage
- it no longer informs current next-step decisions
- a stronger newer artifact has replaced it
- keeping it in the active visual field adds more weight than value

Archive-worthy does not mean disposable.
It means the artifact may later be moved out of the active field while remaining preserved.

---

## IX. DEFERRED / EXPERIMENTAL CRITERIA

An artifact should be DEFERRED / EXPERIMENTAL if:

- it represents a possible future rather than a current lane
- it has not yet passed readiness discipline
- it would create confusion if treated as active now
- it belongs to experiments, future auxiliary systems, or planning-only domains

These artifacts should remain clearly bounded away from active truth and active implementation.

---

## X. CURRENT STRATEGIC READING OF BASE V1

At the current stage of Base V1, the following broad classes are likely active:

### Strongly Active Operational
- doctrine
- active standards
- live support records
- current readiness packets
- current starter packages
- active process standards
- current operator plans/checkpoints
- current implementation-bearing code for control and generator lanes

### Strongly Active Support
- current auxiliary policy packets
- current Codex prompts/skills planning artifacts
- current naming/path/consolidation strategy artifacts
- current intake review artifacts still feeding decisions

### Stable Reference
- handoff packages
- some legacy-supportive context materials
- ancestor-system translation materials when created
- reference-only preserved materials in `07_reference_material`

### Archive-Worthy (future likely)
- older superseded milestone records
- older transition-phase bundles once no longer active
- completed wave artifacts replaced by stronger summaries or later checkpoints

### Deferred / Experimental
- tooling experiments
- Pieces/LTM posture materials
- future MCP connectors
- node/port concepts not yet adopted
- ancestor-system subsystem ideas not yet translated into NEXUS-native artifacts

---

## XI. REVIEW QUESTIONS BEFORE ANY FUTURE ARCHIVE OR DEMOTION

Before demoting an artifact from active visibility, answer all of these:

1. Is it still shaping current work?
2. Would removing it from the active field reduce clarity?
3. Has a stronger or newer artifact clearly replaced it?
4. Is it still needed for rollback or interpretation?
5. Is it being kept active only out of caution, not because it is still useful?
6. Would archiving it now improve or harm operator stamina?
7. Would future reviews still be able to reconstruct the decision chain if it moved?

---

## XII. FAMILY-BASED REVIEW RULE

This review should prefer family-based classification over one-off decisions wherever possible.

Examples of likely future review families:
- milestone/checkpoint records
- readiness packets
- starter packages
- auxiliary policy packets
- legacy transition records
- generated output history
- planning review packets

This is important because later consolidation and normalization will be stronger if whole families are classified consistently.

---

## XIII. REQUIRED GUARDRAILS

This review must be used together with:

- `CONSOLIDATION_AND_RETENTION_STRATEGY_v1`
- `PRE_POST_ACTION_REVIEW_STANDARD_v1`
- `NAMING_AND_PATH_NORMALIZATION_REVIEW_v1`

Meaning:

- consolidation strategy defines what types of cleanup are legitimate
- pre/post review standard defines how meaningful cleanup actions are recorded
- naming/path review defines how future rename/move actions should be judged
- this review defines which artifacts should stay active, become reference, or later move toward archive

---

## XIV. CURRENT RECOMMENDED POSTURE

At the present stage:

### Do now
- identify candidate active families
- identify candidate stable-reference families
- identify candidate archive-worthy families
- preserve the currently active decision spine

### Do next
- use this review to build later archive/compression mapping
- use it to inform future naming/path normalization priorities

### Do not do yet
- broad archive pass
- broad demotion pass
- broad visual cleanup of checkpoint families
- move active support artifacts out of view before a family-level review exists

---

## XV. FUTURE FOLLOW-ON ACTIONS

This review should later feed:

### 1. ACTIVE_TO_REFERENCE_MAPPING_v1
Maps what active artifacts can safely become stable reference.

### 2. REFERENCE_TO_ARCHIVE_MAPPING_v1
Maps what preserved reference artifacts can later move into archive treatment.

### 3. CHECKPOINT_AND_PACKET_COMPRESSION_PLAN_v1
Identifies repeated families that may later be compressed or superseded.

### 4. Controlled archive/move utilities
Only after mapping and pre/post review requirements are satisfied.

---

## XVI. END STATE

The intended end state of this review is a NEXUS system where:

- active work surfaces remain easy to identify
- stable references remain preserved but secondary
- archive-worthy materials are preserved without cluttering the active field
- deferred/experimental ideas remain bounded
- future consolidation, compression, and normalization actions become safer and more accurate