# GPT_INTERACTIVE_PRESENTATION_PATCH_IMPLEMENTATION_NOTES_v1

**Classification:** Patch Implementation Notes / Non-Doctrinal  
**Authority:** Advisory / Operator-Governed  
**Status:** Active Patch Guidance  
**Scope:** Define the exact implementation notes required to patch the GPT interactive presentation artifact into a stronger internal reference surface without promoting it into canonical truth

---

## I. PURPOSE

This artifact translates the patch review and patch plan into direct implementation guidance.

It exists to answer:

- what should be changed
- what should remain unchanged
- what should be relabeled
- what should be split
- what must be verified before patching
- what should remain future-only

This artifact is not:
- a doctrine file
- a live source of truth
- permission to treat the dashboard as current authority
- a public portfolio instruction set

---

## II. CORE IMPLEMENTATION RULE

Patch the presentation artifact as an:

**internal reference surface**

Do not patch it into:
- a canonical source
- a live operator-control panel
- a runtime authority surface
- a merged public/internal hybrid

---

## III. WHAT STAYS UNCHANGED

The following should remain substantially intact:

- overall HTML/CSS shell
- dark operator-grade visual language
- top bar / sidebar / main structure
- section order
- truth hierarchy section
- discrepancy matrix pattern
- appendix / raw packet section
- function state board concept
- checkpoint block concept
- lane structure visualization
- audit-oriented readability

These are strengths and should be preserved.

---

## IV. REQUIRED STATE MODEL PATCHES

## PATCH_01 — CONTEXT EXPORT DUAL-STATE FIX

### Current problem
The artifact treats context export too simply.

### Correct interpretation
Two different things must be separated:

#### A. Context export surface
`03_system_state/context_exports`
- status = ACTIVE
- class = OBSERVATIONAL_ONLY

#### B. Context export generator lane
This must not be silently collapsed into the surface above.

Use this rule:

- if patching against the 2026-04-17 readiness packet only:
  - status = NEAR_READY
- if patching against a later verified local checkpoint proving pass:
  - status = IMPLEMENTED / PASS

### Required implementation note
Do not let the artifact use one label for both:
- output family state
- generator lane maturity

They must be distinct.

---

## PATCH_02 — GENERATOR FAMILY STATE UPDATE

Update generator-family representation to show:

- Manifest Generator = PASS
- Snapshot Generator = PASS
- Context Export = split into:
  - active observational surface
  - generator-lane status per current verified source basis

Do not leave the generator family frozen at an earlier sequence state.

---

## PATCH_03 — NEXT SEQUENCE UPDATE

### Remove stale sequence items
Remove:
- “Draft CONTEXT_EXPORT_READINESS_PACKET_v1”
- “Decide ready / near-ready / hold for context export lane”
- “Only then draft context_export_generator.py”

These were valid earlier but are now stale relative to later packet/workflow state. The current patch review explicitly identifies this next-sequence block as stale. :contentReference[oaicite:0]{index=0}

### Replace with
Use either:

#### Option A — if dashboard should reflect current static system stage
- Preserve Base V1 stabilized checkpoint
- Keep dashboard advisory-only
- Patch source labels and freshness state
- Patch inventory and dual-state context export logic
- Patch interaction logic
- Review after patch

#### Option B — if dashboard should reflect current workflow stage more generally
- Preserve Base V1 stabilized save state
- Keep internal dashboard and external portfolio separate
- Patch state accuracy and terminology integrity
- Add source/freshness tags
- Reassess classification after patch

Do not reintroduce obsolete generator-sequencing steps.

---

## PATCH_04 — OBSERVATIONAL SPINE UPDATE

`03_system_state` must be represented as:

- manifests = ACTIVE
- snapshots = ACTIVE
- context_exports = ACTIVE
- all remain OBSERVATIONAL_ONLY

Do not imply any of them are governance authority.

---

## V. REQUIRED TERMINOLOGY PATCHES

The current patch review correctly flags terminology drift.

### Replace these non-canonical labels
- Doctrine Duplication Rate
- Escalation Deviation Rate
- Context Integrity Score
- Cross-Layer Coupling Count

### With canonical EMS-aligned labels
- Doctrine Density Ratio
- Exploration Dominance Ratio
- Compression Integrity Score
- Cross-Lab Contamination Count

### Important rule
Do not casually rename core governance metrics.

This patch is not cosmetic.
It is terminology-integrity repair.

The uploaded patch review identifies this drift explicitly and recommends restoring canonical EMS terminology. :contentReference[oaicite:1]{index=1}

---

## VI. REQUIRED SOURCE / FRESHNESS PATCHES

Every major panel should gain explicit source posture.

### Add SOURCE_TYPE labels
Use one of:
- CANONICAL
- ACTIVE_STANDARD
- SUPPORT_RECORD
- CHECKPOINT
- OBSERVATIONAL_ONLY
- WEAKER_SURFACE
- FUTURE_ONLY
- REFERENCE_ONLY

### Add FRESHNESS labels
Use one of:
- CURRENT
- STALE
- BASELINE_ONLY
- UNKNOWN
- NEEDS_REFRESH

### Minimum required sections for patching
At minimum add source/freshness tags to:
- System Identity
- Inventory Summary
- Lab Architecture
- Doctrine Registry
- Active Standards
- Support Records
- Observational Outputs
- Metrics
- Build State
- Context Export block
- Discrepancy Matrix
- Function State Board
- Next Sequence

---

## VII. INVENTORY PATCHES

### PATCH_05 — COUNT SAFETY
The artifact currently hardcodes counts in the top bar and in the `nexusData` object.

Do not treat those as trusted current truth unless they are sourced from current approved files.

### Required implementation note
Either:

#### A. static-but-labeled mode
Keep hardcoded values, but visibly label them as:
- PRESENTATION_COUNTS
- BASED_ON_LAST_APPROVED_REVIEW

or

#### B. derived-display mode
Derive what can safely be derived from the embedded data arrays.

### Strong rule
No count should visually look canonical unless its source basis is visible.

The manifest standard explicitly says counts are generated and not to be manually maintained as truth. :contentReference[oaicite:2]{index=2}

---

## VIII. LANE MODEL PATCHES

### PATCH_06 — ADD / STRENGTHEN LANE REPRESENTATION

The lane model should explicitly cover:

- `00_governance_ref`
- `01_core`
- `02_config`
- `03_system_state`
- `04_logs`
- `05_experiments`
- `06_operator`
- `07_reference_material`

### Required lane clarifications

#### `03_system_state`
Represent as:
- observational spine
- current outputs
- not authority

#### `04_logs`
Represent as:
- intentionally empty
- no fake/backfilled logs
- active log meaning not yet established

#### `05_experiments`
Represent as:
- quarantine lane
- experimental / future bridge candidates
- experimental-only, not active foundation

#### `06_operator`
Represent as:
- checkpoints
- plans
- decision support
- process metabolism layer

#### `07_reference_material`
Represent as:
- handoff materials
- audit evidence
- working reference
- legacy/reference reservoir

### Optional future lane
If `08_release_staging` is shown at all, label it:
- FUTURE_ONLY
- NOT_ACTIVE
- NOT_IMPLEMENTED

---

## IX. TECHNICAL PATCHES

## PATCH_07 — OBSERVATIONAL TOGGLE FIX

### Current issue
The current logic is effectively a no-op because both branches assign the same display value. The extracted HTML shows the current next-sequence and state model are hardcoded in the same script block that stores the UI state. :contentReference[oaicite:3]{index=3}

### Replace conceptually with
Target actual observational sections and toggle them explicitly.

Example target groups:
- observational output cards
- observational-only info boxes
- observational function-board entries
- observational appendix items if desired

### Rule
The toggle must actually change visibility.

---

## PATCH_08 — STRONGEST_ONLY MODE FIX

### Current issue
“Show strongest only” mostly hides metadata strips.

### Required behavior
It should reduce the surface to strongest-source material.

### Minimum strongest-only set
Show:
- System Identity
- Authority Hierarchy
- Doctrine Registry
- Active Standards
- locked checkpoint block
- discrepancy matrix

Hide or dim:
- observational-only blocks
- weaker surfaces
- convenience display surfaces
- future-only blocks
- appendix unless explicitly kept

---

## PATCH_09 — FILTER MODEL FIX

### Current issue
Filtering is text-fragile and should not rely on `textContent.includes(...)`. The current HTML uses that kind of text-based filtering approach and static `nexusData`, which the uploaded review correctly identifies as weak. 

### Required behavior
Add metadata tags to cards/sections, such as:
- `data-source-type`
- `data-freshness`
- `data-status`
- `data-surface-role`

Then filter using those attributes.

---

## PATCH_10 — VIEW MODE BEHAVIOR

### Executive mode
Emphasize:
- identity
- truth hierarchy
- architecture
- checkpoint state
- key next sequence

### Full mode
Show everything.

### Audit mode
Emphasize:
- discrepancies
- freshness warnings
- weaker-surface notices
- raw appendix
- dual-state labeling

---

## X. INTERNAL VS EXTERNAL SPLIT

### Internal dashboard should emphasize
- truth hierarchy
- discrepancy handling
- checkpoint logic
- source/freshness posture
- internal structural explanation

### External portfolio site should emphasize
- public-safe system explanation
- employer-facing positioning
- role-fit clarity
- simplified narrative

### Strong rule
Do not use the internal dashboard as the public portfolio shell.

The external portfolio and the internal dashboard are now separate presentation classes.

---

## XI. WHAT MUST REMAIN FUTURE-ONLY

Do not patch the artifact in a way that makes these look active:

- runtime activation
- API activation
- bridge-online truth
- live execution pathways
- scheduler layer
- graph-memory layer
- multi-node orchestration
- completed public-release staging
- enterprise deployment claims

These may only appear if clearly tagged:
- FUTURE_ONLY
- REFERENCE_ONLY
- EXPERIMENT_ONLY

---

## XII. PATCH IMPLEMENTATION ORDER

### STEP_01
Preserve current artifact as pre-patch reference version.

### STEP_02
Patch context export dual-state logic.

### STEP_03
Patch generator-family and build-state status.

### STEP_04
Patch next-sequence content.

### STEP_05
Patch EMS terminology drift.

### STEP_06
Patch lane structure and lane descriptions.

### STEP_07
Add source/freshness labels.

### STEP_08
Patch observational toggle.

### STEP_09
Patch strongest-only mode.

### STEP_10
Patch filter logic.

### STEP_11
Reassess classification after patch.

---

## XIII. SUCCESS CONDITIONS

This patch is successful only if:

1. context export surface and generator lane are no longer collapsed into one label
2. stale next-sequence logic is removed
3. canonical EMS terminology is restored
4. observational-only surfaces remain visibly weaker than stronger sources
5. counts are visibly sourced or visibly presentation-only
6. toggles actually work
7. strongest-only mode actually narrows the surface
8. internal dashboard and external portfolio remain separate
9. no new feature implies broader system authority
10. the artifact remains readable and visually strong

---

## XIV. FINAL IMPLEMENTATION JUDGMENT

The correct move is not:
- rebuild the dashboard from scratch
- discard the shell
- treat the current version as live truth

The correct move is:

> preserve the shell, patch the state model, restore terminology integrity, strengthen source/freshness tagging, and keep the dashboard as an internal reference surface unless and until it is fully realigned.