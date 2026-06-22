# NEXUS HUD - Stage 3 System-State Implementation Packet v0.1
Date: 2026-06-15
Repo: C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS
Branch: local-work
Verified HEAD: baa5b9d
War Test: 36 PASS / 0 WARN / 0 FAIL
Scope: GET /hud/system-state only
Status: documentation packet only
Implementation: not authorized until Operator approval
---
## 0. Indicator Key
| Marker | Meaning | Action |
|---|---|---|
| [GREEN] | Verified safe condition | Proceed |
| [HOLD] | Not ready for implementation | Inspect or revise |
| [STOP] | Safety/governance violation | Halt |
| [ACTION] | Operator action required | Run intentionally |
| [CHECKPOINT] | Pause and review output | Send result |
| [WHY] | Reason for requirement | Understand boundary |
| [BLOCKED] | Not authorized | Do not do |
| [DOC ONLY] | Documentation only | No runtime effect |
| [TEST] | Verification step | Confirm behavior |
---
## 1. Purpose
This packet defines the implementation boundary for the first HUD Stage 3 backend endpoint:
GET /hud/system-state
This packet does not authorize backend code by itself. It defines what may be implemented only if Operator approval is given.
---
## 2. Current Gate Standing
### Gate 1 - Architecture
Status: PROVISIONAL PASS WITH CONSTRAINTS G1-A + G1-B
Meaning:
\- HUD backend may exist only as a local read-only interface adapter.
\- HUD backend must not become a general NEXUS API.
### Gate 2 - Endpoint List
Status: PROVISIONAL PASS WITH CONSTRAINTS G2-A + G2-B + G2-C + G2-D
Meaning:
\- Endpoint review remains limited to the approved HUD GET surfaces.
\- No live integration is implied.
### Gate 3 - Data Sources for GET /hud/system-state
Status: PROVISIONAL PASS WITH CONSTRAINTS
Meaning:
\- First implementation may read approved local files only.
\- No shell execution.
\- No git calls.
\- No report generation.
\- No manifest regeneration.
---
## 3. Endpoint Scope
Allowed endpoint:
GET /hud/system-state
Allowed method:
GET
Blocked methods:
POST
PUT
PATCH
DELETE
Blocked endpoints for this implementation:
GET /hud/governance
GET /hud/council
GET /hud/memory
GET /hud/tasks
GET /hud/pieces
Endpoint role:
Return a read-only JSON summary of local NEXUS system state.
Endpoint non-role:
This endpoint is not:
\- a general API
\- a runtime controller
\- an executor wrapper
\- a manifest generator
\- a war-test runner
\- a task mutator
\- a memory sync surface
\- a Pieces integration
\- a daemon
\- an external network service
---
## 4. Authorized Files
If implementation is later approved, only these files may be created:
10_interface/nexus-hud/backend/hud_server.py
10_interface/nexus-hud/backend/README.md
Optional only if needed:
10_interface/nexus-hud/backend/test_hud_server.py
No other backend files are authorized by this packet.
---
## 5. Approved Read Sources
The endpoint may read only these local repo sources:
03_system_state/manifests/KERNEL_MANIFEST.json
03_system_state/reports/WAR_TEST_REPORT.md
03_system_state/reports/war_test_report.json
04_logs/audit/fault_log.md
docs/adr/
10_interface/nexus-hud/docs/HUD_STAGE_2_ENDPOINT_CONTRACTS.md
10_interface/nexus-hud/docs/HUD_STAGE_3_SYSTEM_STATE_MOCKUP_QC_v0.1.md
Blocked sources:
Pieces live memory
Chat summaries
Screenshots
Unverified memory recall
External APIs
GitHub network calls
Runtime executor output
Generated new reports
Regenerated manifests
Live polling
---
## 6. Hard Safety Constraints
The backend must:
\- bind to 127.0.0.1 only
\- use Python standard library only
\- support GET only
\- serve /hud/system-state only
\- return 404 for unknown paths
\- return 405 for non-GET methods
\- never import executor
\- never call subprocess
\- never run shell commands
\- never call git
\- never write files
\- never modify tasks
\- never access Pieces live memory
\- never poll
\- never run as daemon unless separately approved
---
## 7. Response Shape
The endpoint should return JSON with these top-level keys:
meta
system
sources
warnings
Required meta fields:
endpoint
schemaVersion
feedClass
generatedAt
sourceMode
authority
mutationAuthorized
Required system sections:
project
repo
warTest
hud
governance
Required safety value:
mutationAuthorized: false
---
## 8. FeedClass Rules
Allowed response-level FeedClass values:
LIVE
OPERATOR_LOGGED
UNSOURCED
STALE
Invalid response-level FeedClass:
MIXED
Rules:
\- If endpoint reads local files successfully at request time, meta.feedClass may be LIVE.
\- If important files are missing or stale, meta.feedClass must be STALE.
\- If a claim has no source, that item must be UNSOURCED.
\- Mixed provenance must be handled at item level, not response level.
---
## 9. Missing Source Behavior
If war_test_report.json is missing:
warTest.verdict = UNKNOWN
warning = WAR_TEST_REPORT_MISSING
meta.feedClass = STALE
If KERNEL_MANIFEST.json is missing:
warning = KERNEL_MANIFEST_MISSING
meta.feedClass = STALE
If docs/adr/ cannot be read:
warning = ADR_SOURCE_UNREADABLE
Missing sources must not trigger:
\- file creation
\- manifest regeneration
\- war-test execution
\- git commands
\- shell commands
\- external calls
---
## 10. Test Plan
After implementation, run from repo root:
python nexus_war_test.py
python 10_interface\nexus-hud\backend\hud_server.py
curl.exe http://127.0.0.1:8765/hud/system-state
curl.exe -I http://127.0.0.1:8765/hud/system-state
curl.exe http://127.0.0.1:8765/not-real
git status -sb
Expected:
\- war test remains 36 PASS / 0 WARN / 0 FAIL
\- GET /hud/system-state returns 200
\- unknown path returns 404
\- non-GET method returns 405
\- no unauthorized file changes occur
---
## 11. Commit Boundary
Authorized commit scope if implementation is approved:
10_interface/nexus-hud/docs/HUD_STAGE_3_SYSTEM_STATE_IMPLEMENTATION_PACKET_v0.1.md
10_interface/nexus-hud/backend/hud_server.py
10_interface/nexus-hud/backend/README.md
Optional only if created:
10_interface/nexus-hud/backend/test_hud_server.py
Not authorized in same commit:
\- frontend wiring
\- additional endpoints
\- Pieces integration
\- task mutation
\- memory sync
\- executor changes
\- manifest regeneration
\- doctrine changes
\- ADR acceptance
---
## 12. Operator Approval Gate
Before backend code is created, Operator must choose one:
[ ] APPROVE PACKET ONLY - documentation accepted, no backend code yet
[ ] APPROVE EXACT IMPLEMENTATION - create only listed backend files
[ ] HOLD - revise packet
[ ] REJECT - do not proceed
Operator: JOYBOY
Decision: TBD
Date: 2026-06-15
---
## 13. Final Boundary
This packet does not authorize:
/hud/governance implementation
/hud/council implementation
/hud/memory implementation
/hud/tasks implementation
/hud/pieces implementation
Pieces integration
memory sync
task mutation
executor coupling
external network exposure
daemonization
doctrine promotion
ADR acceptance
First implementation target remains:
GET /hud/system-state only
