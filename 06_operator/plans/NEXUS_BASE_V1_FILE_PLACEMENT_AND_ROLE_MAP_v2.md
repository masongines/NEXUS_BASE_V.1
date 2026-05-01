NEXUS_BASE_V1_FILE_PLACEMENT_AND_ROLE_MAP_v2

Classification: Structural Placement Map / Non-Doctrinal
Authority: Advisory / Operator-Governed
Status: Active Build Map
Scope: Base V1 placement logic implemented under VS_CODE_NEXUS root

==================================================
I. ROOT MODEL
==================================================

ACTIVE IMPLEMENTATION ROOT:

C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS

ARCHITECTURAL FOUNDATION NAME:

NEXUS Base V1

LEGACY REFERENCE ROOT:

C:\Users\mason\Documents\PROJECTS\NEXUS_CORE_LEGACY

DRAFT / PRE-DRAFT ROOT:

C:\Users\mason\Documents\PROJECTS\PRE_DRAFT_BASE_V1

==================================================
II. TOP-LEVEL STRUCTURE
==================================================

VS_CODE_NEXUS
├── 00_governance_ref
├── 01_core
├── 02_config
├── 03_system_state
├── 04_logs
├── 05_experiments
├── 06_operator
├── 07_reference_material
└── README_STRUCTURE.txt

==================================================
III. ROOT FOLDER RULES
==================================================

00_governance_ref
Purpose:
- rewritten governance references only

Allowed:
- doctrine rewrites
- active standard rewrites
- support records
- staged review records

Disallowed:
- raw logs
- runtime code
- legacy dumps
- generated state outputs

--------------------------------------------------

01_core
Purpose:
- active system shell only

Allowed:
- bootstrap logic
- runtime modules
- generators
- control layer
- bounded api/service layer

Disallowed:
- doctrine text
- support records
- operator notes
- legacy reference material
- branch experiments by default

--------------------------------------------------

02_config
Purpose:
- configuration surfaces only

Allowed:
- environment templates
- local config templates
- machine-level configuration surfaces
- non-doctrinal config files

Disallowed:
- decision records
- runtime logs
- doctrine files
- audit evidence

--------------------------------------------------

03_system_state
Purpose:
- generated observational state only

Allowed:
- manifests
- snapshots
- context exports
- generated reviews
- generated reports

Disallowed:
- hand-edited doctrine
- implementation code
- operator approvals
- structural decisions disguised as reports

Authority ceiling:
- observational only
- not governance authority
- not approval source

--------------------------------------------------

04_logs
Purpose:
- append-oriented operational logging only

Allowed:
- audit logs
- event logs
- error logs
- sandbox logs
- later trace logs

Disallowed:
- baseline truth statements
- promoted records
- carry-forward summaries
- doctrine or standards

--------------------------------------------------

05_experiments
Purpose:
- non-foundational experimentation only

Allowed:
- sandbox protocol experiments
- pi_node work
- prototypes
- paused branches
- hardware trials
- branch-heavy runtime ideas

Disallowed:
- silent promotion into active foundation
- canonical governance truth
- default runtime import

--------------------------------------------------

06_operator
Purpose:
- operator-owned control layer

Allowed:
- decision records
- checkpoints
- plans
- milestone declarations
- adoption decisions
- operator workboard material

Disallowed:
- unbounded system logs
- raw branch dumps
- reference-only legacy material

--------------------------------------------------

07_reference_material
Purpose:
- reference-only intake and preserved evidence

Allowed:
- working reference
- legacy exports
- audit evidence
- handoff material

Disallowed:
- current governance truth by default
- hidden active runtime imports
- implementation authority by convenience

==================================================
IV. EXPECTED SUBFOLDER MAP
==================================================

00_governance_ref
- doctrine
- active_standards
- support_records
- staged_reviews

01_core
- bootstrap
- runtime
- generators
- control
- api

02_config
- env
- templates
- local

03_system_state
- manifests
- snapshots
- context_exports
- reviews
- reports

04_logs
- audit
- events
- errors
- sandbox

05_experiments
- sandbox_protocol
- pi_node
- prototypes
- paused

06_operator
- decision_register
- checkpoints
- plans

07_reference_material
- working_reference
- legacy_exports
- audit_evidence
- handoff_material

==================================================
V. PLACEMENT PRINCIPLES
==================================================

1. Governance != runtime
2. Generated state != authority
3. Logs != truth
4. Legacy != active Base V1 by default
5. Experiments != foundation by default
6. Operator layer != generated layer
7. Reference != approval

==================================================
VI. PI NODE PLACEHOLDER RULE
==================================================

Pi 5 remains experimental for now.

Default placeholder role:
- log/archive mirror
- watchdog/monitor node
- backup/sync relay

It is NOT foundationally assigned yet as:
- primary runtime node
- firewall authority
- VPN edge
- main LTM host
- critical control plane

==================================================
VII. END STATE
==================================================

This file defines the canonical placement logic for Base V1 build work under the VS_CODE_NEXUS root.

Anything placed outside these rules requires explicit operator direction.