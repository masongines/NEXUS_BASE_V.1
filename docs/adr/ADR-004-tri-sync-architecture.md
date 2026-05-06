# ADR-004: Tri-System Knowledge Sync via Operator-Mediated Hub

**Status:** Accepted  
**Date:** 2026-05-06  
**Deciders:** Mason Gines (Sovereign Operator)  
**Supersedes:** —  
**Related:** ADR-001 (Governance-First), ADR-002 (Rule-Based Threat Detection), ADR-003 (Local-First)

---

## Context

NEXUS Base V1 operates in isolation from two other active systems:

- **SkillUp Capstone** (`CAPSTONE_SKILLUP/`) — Python Jupyter notebooks implementing RAG, BERT, autoencoders; no API surface; deadline August 30, 2026.
- **Pieces OS + PIECES_EXPORT** — Local long-term memory vault running at `localhost:39300`; MCP endpoint available via `ask_pieces_ltm`.

These systems generate related knowledge that currently does not cross system boundaries. SkillUp learning events could become NEXUS audit entries. Pieces recall could orient new SkillUp sessions. NEXUS governance events could trace back to specific capstone work.

The question is how to connect them without violating the local-first, governance-first, and operator-sovereignty principles established in ADR-001 and ADR-003.

Three topologies were considered:

| Topology | Description |
|----------|-------------|
| Mesh (peer-to-peer) | Each system communicates directly with every other |
| Event-driven | File watchers or message broker trigger cross-system writes |
| Hub-and-spoke | Claude Code mediates all cross-system operations |

---

## Decision

**Hub-and-spoke with Claude Code as the operator-controlled hub.**

All cross-system writes are operator-initiated and require explicit approval before execution. The sync bridge (`nexus_sync_bridge.py`) is a command-line Python script invoked by the operator through Claude Code — not a background server, not an automated scheduler.

Sync entries pass through the existing Security Monitor (`detect_threat()`) before being written. No new pip packages. No cloud dependencies. Pure Python stdlib.

**Sync model: pull-on-demand, not push-on-event.**

---

## Options Considered

### Option A: Hub-and-Spoke (chosen)

| Dimension | Assessment |
|-----------|------------|
| Operator control | Full — every write is operator-approved |
| ADR-001 compliance | Full — sync bridge routes through Security Monitor and approval gate |
| ADR-003 compliance | Full — no new services, no network, zero new pip packages |
| Complexity | Low — one script, existing patterns |
| Solo developer overhead | Minimal |
| Capstone deadline impact | Helps — accelerates context recall, low build overhead |

**Pros:** Respects PRIME_AXIOM sovereignty; fits existing NEXUS execution contract; Claude Code is already the primary interface for all three systems.  
**Cons:** Sync is not real-time; requires Mason to initiate every capture manually.

### Option B: Mesh

**Pros:** Theoretically lower latency for future multi-agent use.  
**Cons:** SkillUp has no API surface; Pieces direct writes to NEXUS would bypass the Security Monitor and Approval Gate (ADR-001 violation); requires building three API surfaces.

### Option C: Event-Driven (File Watchers)

**Pros:** More automatic.  
**Cons:** File watchers are persistent background processes — violates ADR-003's local-first, no-persistent-service mandate; auto-triggered writes bypass operator approval (PRIME_AXIOM Rule III violation).

---

## Trade-off Analysis

The deliberate choice of manual operator initiation over automation is the core trade-off. The benefit is complete sovereignty alignment. The cost is that context is only surfaced when Mason asks for it, not proactively.

For a solo developer targeting a certification deadline, this trade-off favors reliability and trust over automation. An incorrectly auto-triggered write to the NEXUS audit log would be harder to trace and clean up than a missing manual capture.

---

## Implementation

### New files
- `nexus_sync_bridge.py` — operator-invoked sync entry writer (root of VS_CODE_NEXUS)
- `04_logs/audit/skillup_learning_log.txt` — learning capture entries (append-only)
- `04_logs/audit/governance_events_log.txt` — governance event entries (append-only)
- `.claude/settings.json` — project-scoped Pieces MCP config (VS_CODE_NEXUS and CAPSTONE_SKILLUP)
- `docs/adr/ADR-004-tri-sync-architecture.md` — this document
- `CAPSTONE_SKILLUP/NEXUS_ALIGNMENT_NOTES.md` — cross-system capstone traceability
- `PIECES_EXPORT/nexus_artifacts/war_test_results/` — NEXUS artifact landing zone
- `PIECES_EXPORT/course_materials/skillup_session_log.md` — human-readable session timeline

### Modified files
- `02_config/execution_trust_registry.json` — added `learning_capture` (T2) and `governance_event` (T2)
- `01_core/execution/tool_registry.json` — added `nexus_sync_bridge`

### Three data flows
- **Flow A:** SkillUp session → `ask_pieces_ltm` → operator-approved `learning_capture` → `skillup_learning_log.txt`
- **Flow B:** Session start → `ask_pieces_ltm` → `skillup_learning_log.txt` read → session briefing (read-only)
- **Flow C:** NEXUS governance event → operator-approved `governance_event` → `governance_events_log.txt` + `PIECES_EXPORT/nexus_artifacts/`

---

## Consequences

**What becomes easier:**
- SkillUp session context is available at the start of every NEXUS session and vice versa
- Pieces long-term memory feeds both systems via a single Claude Code interface
- The capstone paper can cite NEXUS audit entries as cross-system governance evidence

**What becomes harder:**
- Sync is not real-time — requires Mason to initiate capture after each session
- Pieces content not explicitly saved by the operator is not surfaced automatically

**Explicitly out of scope:**
- Automated file watchers or cron-triggered sync
- Google Sheets API integration (cloud dependency, ADR-003 violation)
- FastAPI exposure of the NEXUS approval gate (deferred per ADR-003 stated future work)
- Any write to `00_governance_ref/` from the sync bridge (doctrine plane is off-limits)

---

## Governance Alignment

| Rule | How this ADR satisfies it |
|------|--------------------------|
| PRIME_AXIOM Rule III — no output accepted without operator consent | Every sync entry requires explicit `y` approval before `append_log()` is called |
| ADR-001 — governance-first | `nexus_sync_bridge.py` calls `detect_threat()` before any write |
| ADR-003 — local-first | No external services, no cloud dependencies, zero new pip packages |
| `NEXUS_AUTHORITY_AND_BOUNDARY_SAFEGUARDS_v1.md` Section 10 | Pieces remains Plane 3 Operational Memory; recall outputs labeled `source_type: recall`; ceiling not elevated |
| Execution Contract Rule 3 — all executions logged | Both `approved` and `denied` entries are written to the audit log |
