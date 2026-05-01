NEXUS_BASE_V1_MIGRATION_REGISTER_v2

Classification: Migration Control Register / Non-Doctrinal
Authority: Advisory / Operator-Governed
Status: Active Working Register
Scope: Base V1 migration and rewrite mapping under VS_CODE_NEXUS root

==================================================
I. PURPOSE
==================================================

This register tracks how current materials move into Base V1 under the VS_CODE_NEXUS implementation root.

Use group/workstream level first.

Do not start at full file-level tracking unless a workstream enters active migration or high-risk rewrite.

==================================================
II. ACTION LEGEND
==================================================

Allowed action values:
- rewrite
- copy_as_reference
- quarantine
- archive
- generate
- defer
- reject
- extract_then_rewrite

Allowed status values:
- not_started
- mapped
- in_rewrite
- in_review
- migrated
- quarantined
- deferred
- closed

==================================================
III. REGISTER FIELDS
==================================================

Each row should track:
- workstream
- current source
- source_of_truth
- authority class
- target Base V1 path
- action
- status
- dependency
- approval required
- notes

==================================================
IV. GROUP / WORKSTREAM LEVEL REGISTER
==================================================

| Workstream | Current Source | Source of Truth | Authority Class | Target Base V1 Path | Action | Status | Dependency | Approval Required | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Canonical doctrine set | legacy governance kernel / current sources | doctrine registry + doctrine files | doctrine | 00_governance_ref/doctrine | rewrite | mapped | placement map | Yes | registry identity remains canonical source |
| Active standards set | legacy governance kernel / current sources | active standards + operator review | active standard | 00_governance_ref/active_standards | rewrite | mapped | placement map | Yes | keep doctrine/non-doctrine distinction hard |
| Support records / lock records | current project sources | lock records / support files | support record | 00_governance_ref/support_records | copy_as_reference + selective rewrite | mapped | placement map | Yes | includes sandbox lock and chunk lock records |
| Staged reviews / carry-forward review material | current project sources / review outputs | review artifacts | staged review | 00_governance_ref/staged_reviews | copy_as_reference | mapped | placement map | No | not active authority by default |
| Manifest generator shell | legacy/current generator material | generator spec + approved runtime rewrite | active standard / runtime support | 01_core/generators | extract_then_rewrite | in_review | governance layer population | Yes | observational-only output ceiling |
| Snapshot generator shell | legacy/current generator material | snapshot protocol + generator spec | active standard / runtime support | 01_core/generators | extract_then_rewrite | in_review | governance layer population | Yes | preserve observational-only posture |
| Guardian / preflight logic | current doctrine + automation spec | guardian doctrine + automation spec | active standard / control support | 01_core/control | extract_then_rewrite | in_review | governance layer population | Yes | analytical safeguard only |
| Runtime shell placeholder | legacy/runtime concepts | operator direction + placement map | defined / planned | 01_core/runtime | defer_then_rewrite | not_started | governance + placement map | Yes | minimal shell only |
| Bootstrap shell | current build planning | operator direction | planned | 01_core/bootstrap | rewrite | not_started | placement map | No | bounded startup logic only |
| Config templates | environment and local setup material | operator direction + actual runtime need | config | 02_config/templates + 02_config/env + 02_config/local | rewrite | not_started | placement map | No | no doctrine or decision logic here |
| Generated manifests | current outputs | manifest generator | generated observational | 03_system_state/manifests | generate | migrated | generators | No | observational only |
| Generated snapshots | current outputs | snapshot generator | generated observational | 03_system_state/snapshots | generate | migrated | generators + guardian | No | must not imply authority |
| Generated context exports | current outputs | context export generator | generated observational | 03_system_state/context_exports | generate | migrated | generators | No | bootstrap support only |
| Reviews / reports | current outputs | generator/review workflow | generated review surface | 03_system_state/reviews + 03_system_state/reports | generate | not_started | generators / sandbox | No | not governance authority |
| Audit / event / error / sandbox logs | runtime and governance events | logging workflow | logs | 04_logs/* | generate | not_started | logging plan | No | append/rotate only |
| Pi node experiments | future auxiliary node | operator direction | experiment | 05_experiments/pi_node | defer | mapped | foundation stabilization | Yes | default role not foundational yet |
| Prototypes / paused branches | legacy branch work | legacy reference only | experiment | 05_experiments/prototypes + 05_experiments/paused | quarantine | mapped | placement map | No | branch-only |
| Operator decision records | operator workflow | operator direct approval | operator-controlled | 06_operator/decision_register | rewrite_or_reference | not_started | operator workflow rule | Yes | do not confuse with generated state |
| Operator checkpoints | operator workflow | operator direct declarations | operator-controlled | 06_operator/checkpoints | rewrite | not_started | workboard | No | milestone declarations go here |
| Operator plans | operator workflow | operator direct planning | operator-controlled | 06_operator/plans | rewrite | not_started | workboard | No | current build plans go here |
| Legacy exports | old laptop system | reference only | reference only | 07_reference_material/legacy_exports | copy_as_reference | mapped | none | No | never active by default |
| Audit evidence | screenshots / comparisons / mismatch evidence | evidence only | reference / evidence | 07_reference_material/audit_evidence | copy_as_reference | mapped | none | No | supports review only |
| Handoff materials | bootstrap and continuity packages | handoff source | handoff reference | 07_reference_material/handoff_material | copy_as_reference | mapped | none | No | active handoff support |

==================================================
V. RULES
==================================================

1. Group/workstream level comes first.
2. File-level expansion happens only after a workstream enters active migration or high-risk rewrite.
3. Legacy usefulness does not imply active authority.
4. Generated outputs remain observational unless explicitly governed otherwise.
5. Any migration touching doctrine, routing, memory boundaries, security, or protocol logic requires operator review.

==================================================
VI. FILE-LEVEL EXPANSION TRIGGER
==================================================

Expand a workstream to full file-level tracking when any of the following are true:

- doctrine rewrite begins
- active standard rewrite begins
- generator implementation begins
- control/guardian implementation begins
- a conflict appears inside a workstream
- a file has unclear authority class
- operator requests exact file-level migration tracking

==================================================
VII. END STATE
==================================================

This register is the primary migration-planning surface for Base V1 reconstruction under the VS_CODE_NEXUS root.

It exists to stop blind copying, mixed-layer collapse, and legacy drift.