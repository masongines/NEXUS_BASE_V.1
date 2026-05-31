# NEXUS Fault Log (append-only)

**Governing doctrine:** ADR-007 (Operator Fault Logging) — Proposed, `docs/adr/ADR-007-operator-fault-logging.md`
**Discipline:** log faults; do not silently resolve. Memory/workspace conflicts are discrepancy signals resolved in the workspace's favor (ADR-004 / S-2). Tier-1 remediations follow the Co-Dev §S-9 ceremony.

**Categories:** `operator` (incl. gate overrides) · `system` (workspace/tooling/manifest drift) · `agent` (drift / integrity breach).

**Entry schema:**
```
### FL-NNN — <short title>
- Date:        YYYY-MM-DD
- Category:    operator | system | agent
- Source:      <who/what surfaced or caused it>
- Provenance:  EVIDENCE | RECALL | INFERENCE | OBSERVATION | DISCREPANCY  (+ confidence)
- Description: <what happened>
- Status:      OPEN | RESOLVED | MONITORING
- Resolution:  <action / ruling / pending>
- ADR-007 ref: <ceremony / category note>
```
Entries are append-only. Record resolution as a new `Status`/`Resolution` state; never delete the trail.

---

### FL-001 — Co-Dev Protocol v1.0 status: operator override of the ADR-007 gate (OD-1)
- Date:        2026-05-29
- Category:    operator (gate override)
- Source:      Operator ruling (OD-1); finding raised by C2; gate-absence confirmed by C6
- Provenance:  EVIDENCE | high
- Description: Co-Dev Protocol v1.0 file body read PROPOSED with promotion gated on ADR-007, which was absent on disk; header/recall said ACTIVE. Operator ruled **ACTIVE** (operator correction, top of S-2), superseding the ADR-007 promotion gate.
- Status:      RESOLVED
- Resolution:  File `NEXUS_CO_DEV_PROTOCOL_v1.md` synced to ACTIVE across all status markers (commit 734f9b0). ADR-007 demoted from gate to follow-up, now authored 2026-05-29.
- ADR-007 ref: operator-override ceremony — superseded gate named (ADR-007), rationale recorded.

### FL-002 — Kernel manifests stale + phantom artifact (system drift)
- Date:        2026-05-29
- Category:    system
- Source:      C4 (Codex) flagged; cross-verified by C6/C2 against disk
- Provenance:  DISCREPANCY | high
- Description: Both `KERNEL_MANIFEST.json` files report `active_standard_count: 8` while `00_governance_ref/active_standards/` holds 11; the support manifest (2026-03-19, legacy `governance_kernel/` scan root) lists `META_CONTROL_CENTER.md`, which does not exist on disk.
- Status:      OPEN
- Resolution:  Pending operator decision — regenerate both manifests via MANIFEST_GENERATOR_SPEC against `00_governance_ref/` (do not hand-edit; manifests say "Counts must not be manually edited").
- ADR-007 ref: system-fault category; resolve in workspace's favor (S-2).

### FL-TEST — TEST ENTRY (simulated — verifies the logging mechanism; not a real fault)
- Date:        2026-05-29
- Category:    operator (simulated override)
- Source:      ADR-007 deliverable script — mechanism self-test
- Provenance:  OBSERVATION | n/a (simulated)
- Description: Simulated operator override of a protocol gate, recording a memory↔workspace discrepancy, to confirm the fault-log schema and append flow work end-to-end.
- Status:      RESOLVED (test only)
- Resolution:  Mechanism verified; this entry is illustrative and carries no governance weight. Safe to leave or prune.
- ADR-007 ref: demonstrates the operator-override ceremony format.

### FL-002 — UPDATE 2026-05-31 (partial resolution: output-lane manifest regenerated)
- Date:        2026-05-31
- Category:    system
- Source:      C2 (Claude Code) under operator authorization ("do #1, manifest regen")
- Provenance:  EVIDENCE | high
- Description: Investigation refined FL-002 — the two manifests are DIFFERENT artifacts, not one drift. `03_system_state/manifests/KERNEL_MANIFEST.json` (current generator output, simple schema) was stale at `active_standard_count: 8` and has NO phantom. The phantom `META_CONTROL_CENTER.md` exists ONLY in `00_governance_ref/support_records/KERNEL_MANIFEST.json` (legacy 2026-03-19 rich schema, `governance_kernel/` scan root), which `manifest_generator.py` v1.1 does NOT write.
- Action:      Ran `manifest_generator.py` (read-only scan + single output write). `03_system_state/manifests/KERNEL_MANIFEST.json` regenerated: `active_standard_count` 8 -> 11 (added CLI_LOGS_SUB_LANE_CONVENTION_v1.md, CO-DEV_3.33_NEXUS_META_CENTER_UI_DASHBOARD_ENGINEER_BOOTSTRAP_v1.md, NEXUS_CO_DEV_PROTOCOL_v1.md); doctrine 12 / support records 8 unchanged. Generated, not hand-edited. Commit `0879c1b` on `local-work` (not pushed).
- Status:      PARTIALLY RESOLVED — output-lane manifest RESOLVED; support_records/ legacy copy + phantom OPEN.
- Resolution:  Output-lane drift fixed. The original FL-002 plan ("regenerate both") is not achievable with generator v1.1 (it manages only the output copy). Deciding the canonical manifest and retiring/superseding the legacy support_records copy (which still carries the phantom) is a STRUCTURAL change — escalated to operator per the standing rule "any structural change to the NEXUS system as a whole comes to the operator first." NOT actioned.
- ADR-007 ref: system-fault category; partial remediation recorded append-only; structural remainder gated to operator.
