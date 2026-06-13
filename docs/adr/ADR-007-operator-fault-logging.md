# ADR-007: Operator Fault Logging Doctrine

**Status:** Proposed  
**Date:** 2026-05-29  
**Deciders:** Mason Gines (Sovereign Operator)  
**Supersedes:** —  
**Related:** ADR-001 (Governance-First), ADR-004 (Tri-Sync / recall-as-non-authority), Co-Dev Protocol v1.0 §9 (Fault Handling) and §10 (Discrepancy Handling)

---

## Context

Faults occur across the NEXUS council: the operator overrides a gate, a generated manifest drifts from disk, an agent inflates flags or edits a slot it does not own. Until now the only discipline was the **interim** one in Co-Dev Protocol v1.0 §9 (acknowledge → categorize → note in-session → surface pattern-level), with §9 forward-referencing a then-unwritten ADR-007.

Recent concrete faults make the gap visible:
- **Operator override:** the OD-1 ruling promoted Co-Dev Protocol v1.0 to ACTIVE, *superseding* this very ADR's promotion gate (operator correction, top of S-2). Legitimate — but it must be recorded, not silent.
- **System drift:** both `KERNEL_MANIFEST.json` files report `active_standard_count: 8` while disk holds 11; the older manifest lists a **phantom `META_CONTROL_CENTER.md`** that does not exist on disk (cross-verified by C4 and C6/C2).
- **Agent/slot breach:** an agent (Manus) edited the C1 slot it did not own — an S-4 cross-verification-integrity violation.

There is no durable, auditable place to log these, no taxonomy, and no written operator-override ceremony. ADR-004 already establishes that memory/workspace conflicts are **discrepancy signals, not resolved in memory's favor** — but the logging mechanism for that was never codified.

---

## Decision

**Adopt an Operator Fault Logging Doctrine: a fault taxonomy, an append-only fault log, an escalation path, and an explicit operator-override ceremony.**

- Faults are **logged, never silently resolved.** Logging is observational; it does not adjudicate.
- The operator may override any gate (S-2). An override is itself a logged entry, with rationale and the superseded gate named.
- Memory/workspace conflicts (ADR-004) are logged as discrepancies via this doctrine and resolved in the **workspace's** favor (S-2), never memory's.

### Fault taxonomy
| Category | Definition | Examples |
|---|---|---|
| **Operator fault** | Operator-introduced error or a deliberate gate override | OD-1 override of the ADR-007 gate; a correction reversing a prior instruction |
| **System fault** | Workspace / tooling / generated-artifact drift | Stale `active_standard_count` (8 vs disk 11); phantom `META_CONTROL_CENTER.md`; duplicate DEF-13 commit |
| **Agent fault** | Agent drift or integrity breach | Slot-integrity breach (Manus→C1); flag-inflation; file over-production; dropped-thread; search omission; confidence decay |

### Logging protocol
- Single append-only log: `04_logs/audit/fault_log.md`.
- Each entry carries: **date · category · source · description · provenance label (S-5) · status/resolution · ADR-007 ref**.
- Entries are never edited away; resolution is recorded as a new state on the entry, preserving the trail.

### Escalation
1. **In-session note** — surface the fault plainly when observed.
2. **Pattern-level** — if likely to recur, log it and tag it as a pattern.
3. **Operator decision** — escalate to the operator; Tier-1 remediations follow the Co-Dev §S-9 ceremony (proposal → sandbox → gate → execute → halt → revert). Discrepancies route per §10.

### Operator-override ceremony
The operator's correction is top of S-2 and may supersede any gate. The ceremony is: **(a)** operator states the ruling; **(b)** the ruling is logged as an operator entry naming the superseded gate and rationale; **(c)** affected artifacts are synced to the ruling, with any residual ("apparent drift until artifact updated") noted. OD-1 is the worked example and is recorded as the first real entry in the fault log.

---

## Options Considered

### Option A: Dedicated append-only fault log + taxonomy (chosen)
**Pros:** durable audit trail; matches ADR-004's `04_logs/audit/*` precedent; keeps logging separate from adjudication; gives §9 a real target.  
**Cons:** one more artifact to maintain; relies on discipline to actually log.

### Option B: Inline-only (status quo §9 interim discipline)
**Pros:** zero new files.  
**Cons:** no persistence, no cross-session trail, no taxonomy; faults evaporate when a session ends.

### Option C: Structured `fault_log.json` consumed by tooling
**Pros:** machine-queryable.  
**Cons:** premature — no consumer exists yet; harder for the operator to read/append by hand. (Revisit if/when a HUD surface needs it.)

---

## Trade-off Analysis

The core choice is a human-readable Markdown log (Option A) over machine-structured JSON (Option C). For a solo, governance-first, operator-sovereign project, an append-only Markdown log the operator can read and append directly wins on trust and low overhead. A JSON log buys queryability no current surface consumes. Markdown also mirrors the existing ADR/standard documents, so the discipline reads like the rest of the kernel.

---

## Implementation

### New files
- `docs/adr/ADR-007-operator-fault-logging.md` — this document.
- `04_logs/audit/fault_log.md` — append-only fault log (schema header + entries).

### Modified files
- `00_governance_ref/active_standards/NEXUS_CO_DEV_PROTOCOL_v1.md` — §9 repointed from "ADR-007 … DRAFT" to "ADR-007 (Proposed, authored 2026-05-29)"; line-12 cross-reference refreshed. Interim discipline retained until ADR-007 is **Accepted**.

### Out of scope
- Manifest *regeneration* (the system-fault remediation) — a separate operator-gated action.
- Any automated/tooling consumer of the fault log.

---

## Consequences

**What becomes easier:**
- Operator overrides, system drift, and agent breaches have one durable home and a shared vocabulary.
- §9 of the Co-Dev Protocol points at a real doctrine; the OD-1 residual ("artifact not yet synced") has a logging home.
- Cross-verification findings (C4/C6 manifest drift) become loggable system-fault entries rather than loose notes.

**What becomes harder:**
- Requires the discipline to log faults at the time they occur.

**Acceptance:** this ADR is **Proposed**. On operator acceptance it becomes **Accepted**, and Co-Dev §9's interim discipline is replaced by a direct pointer to this doctrine.

---

## Governance Alignment

| Rule | How this ADR satisfies it |
|------|--------------------------|
| PRIME_AXIOM — no output accepted without operator consent | Overrides are operator-initiated and logged; ADR remains Proposed until operator accepts |
| ADR-001 — governance-first | Faults are logged and escalated through governance, not silently resolved |
| ADR-004 — recall is not authority | Memory/workspace conflicts logged as discrepancies, resolved in the workspace's favor |
| Co-Dev v1.0 §S-2 | Operator correction tops the hierarchy; override ceremony records the superseded gate |
| Co-Dev v1.0 §S-9 / §10 | Tier-1 remediations follow the ceremony; discrepancies route per §10 |
