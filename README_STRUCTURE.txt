NEXUS Base V1 — README_STRUCTURE

Root Path: C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS

Purpose:
- Marks approved Stage B scaffold creation.
- Defines the empty Base V1 folder structure.

Ceiling:
- Scaffold only.
- No file migration performed.
- No doctrine rewrite performed.
- No generator implementation performed.
- No Guardian implementation performed.

Structure:
VS_CODE_NEXUS/
├── 00_governance_ref/
│   ├── doctrine/
│   ├── active_standards/
│   ├── support_records/
│   ├── staged_reviews/
├── 01_core/
│   ├── bootstrap/
│   ├── runtime/
│   ├── generators/
│   ├── control/
│   ├── api/
├── 02_config/
│   ├── env/
│   ├── templates/
│   ├── local/
├── 03_system_state/
│   ├── manifests/
│   ├── snapshots/
│   ├── context_exports/
│   ├── reviews/
│   ├── reports/
├── 04_logs/
│   ├── audit/
│   ├── events/
│   ├── errors/
│   ├── sandbox/
├── 05_experiments/
│   ├── sandbox_protocol/
│   ├── pi_node/
│   ├── prototypes/
│   ├── paused/
├── 06_operator/
│   ├── decision_register/
│   ├── checkpoints/
│   ├── plans/
├── 07_reference_material/
│   ├── working_reference/
│   ├── legacy_exports/
│   ├── audit_evidence/
│   ├── handoff_material/
└── README_STRUCTURE.txt

Top-Level Purpose Map:
00_governance_ref  = rewritten governance references only
01_core            = active system shell only
02_config          = configuration surfaces only
03_system_state    = generated observational state only
04_logs            = append-oriented operational logging only
05_experiments     = non-foundational experimentation only
06_operator        = operator-owned control layer
07_reference_material = reference-only intake and preserved evidence

