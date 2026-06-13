# ADR-008: Kernel Integrity via Merkle Root + Verifier

**Status:** Proposed — `PROMOTION_AUTHORIZED: NO` (operator review required)
**Date:** 2026-05-31
**Deciders:** Mason Gines (Sovereign Operator)
**Supersedes:** —
**Related:** ADR-001 (Governance-First), ADR-003 (Local-First / stdlib-only), `GOVERNANCE_KERNEL_GUARDIAN.md`, `MANIFEST_GENERATOR_SPEC_v1.md`, `KERNEL_HASH.md`, `KERNEL_VERSION.md`, `DOCTRINE_IDENTITY_REGISTRY.md`, FL-002 (`04_logs/audit/fault_log.md`)
**Inspired-by (reference-class, NOT authority):** external project at `nexus-os.org` — NexFS storage/network ADR (a *different*, unrelated "Nexus OS"). The Merkle-integrity *concept* is adapted here; nothing external is ingested as authority, per the source-precedence hierarchy.

> **Numbering flag:** proposed as **ADR-008**, pending operator confirmation. ADR-005 was judged not-needed, ADR-006 is an unassigned gap, ADR-007 (Operator Fault Logging) is Proposed. The master-concept draft §8 referenced a *hypothetical* "ADR-008" for the Sovereign Council that was never created — if the operator reserves 008 for Council, this ADR becomes ADR-009.

---

## Context

Kernel integrity today is recorded in `00_governance_ref/support_records/KERNEL_HASH.md` as a **flat, hand-maintained list of per-file SHA-256 hashes** (one entry per canonical doctrine file plus a few kernel support records). It has three structural weaknesses:

1. **No single root.** There is no one value that represents "the kernel is intact." Verifying integrity means eyeballing ~15 individual hashes.
2. **No verifier tool.** Nothing recomputes the hashes and compares them. The generators that exist (`manifest_generator.py`, `snapshot_generator.py`, `context_export_generator.py`) cover inventory and state, but **no tool touches `KERNEL_HASH.md`** — there is no `hashlib`/integrity code anywhere in `01_core/`.
3. **Hand maintenance → silent drift.** Because it is edited by hand, the record drifts from disk and the drift is found by hand.

This last weakness is not hypothetical. **FL-002** (`04_logs/audit/fault_log.md`) recorded that the retired artifact `META_CONTROL_CENTER.md` — a file absent from disk — still carried a hash entry in `KERNEL_HASH.md`. It was discovered and surgically removed **manually** this session. A root-and-verifier model would have surfaced it automatically.

The `GOVERNANCE_KERNEL_GUARDIAN.md` defines activation conditions ("before milestone deep audits, doctrine promotion attempts, governance refactors, snapshot generation") and a check sequence — but it has **no integrity tool to run** at those points. There is a gap between the Guardian's intent and the available mechanism.

A review of an external project's NexFS ADR demonstrated a robust pattern for this exact problem: **content-addressed leaves rolled into a Merkle root, verified on read.** That pattern is adaptable to the governance kernel without adopting any of the external project's technology.

---

## Decision

**Adopt a Merkle-tree integrity model for the governance kernel: per-file hash leaves rolled into a single Merkle root, with a stdlib verifier the Guardian can run at its activation points.**

- **Canonical kernel set** — defined explicitly: the doctrine files enumerated in `DOCTRINE_IDENTITY_REGISTRY.md` plus the named kernel support records. The set is declared, not folder-scraped, so additions are deliberate.
- **Leaves = SHA-256 per file.** **Reuse the SHA-256 hashes already in `KERNEL_HASH.md`** — the leaf format does not change and no rehashing of the world is required. **SHA-256 via the Python standard library (`hashlib`)** — *not* BLAKE3 — so there is **zero new dependency** (honors ADR-003's stdlib-only, zero-external-attack-surface posture; the war test's "pure standard library" claim stays true).
- **Merkle root** — computed over the leaves in a deterministic (sorted-by-canonical-filename) order, recorded as the single **kernel integrity hash** (a new `KERNEL_MERKLE_ROOT` field/record alongside `KERNEL_HASH.md`). One value answers "is the kernel intact?"
- **Verifier** — a small stdlib tool (sibling to `manifest_generator.py`) that recomputes each leaf from disk, rebuilds the tree, and compares to the recorded root. It reports **PASS/FAIL and exactly which leaf drifted** (missing file, changed file, or unlisted file). It is **observational only** — it reports, it does not modify or enforce, consistent with the Guardian's own prohibitions and PRIME_AXIOM.
- **Guardian hook** — the Guardian runs the verifier at its defined activation points and includes the result in its report.

This ADR **proposes the model only.** It does not build the verifier, compute a root, or edit `KERNEL_HASH.md` — those are separate, operator-gated steps.

---

## Options Considered

### Option A — Keep the flat manual SHA list (status quo)
**Pros:** zero work; human-readable.
**Cons:** no root, no verifier, no automation; drift (e.g., META/FL-002) is found by hand, late, or not at all.

### Option B — Flat list + a regenerate/verify script (no root)
**Pros:** automates detection; small.
**Cons:** still no single integrity value; the Guardian still has nothing to summarize as one PASS/FAIL.

### Option C — Merkle root + verifier (chosen)
**Pros:** one value = kernel intact; deterministic; pinpoints the drifted leaf; integrates with the Guardian; reuses existing SHA-256 leaves; stdlib-only.
**Cons:** a new tool to build and maintain; the canonical kernel set must be defined precisely once.

**Hash algorithm:** **SHA-256 (stdlib, chosen)** vs **BLAKE3** (faster, used by the external reference). BLAKE3 would add an external dependency, violating ADR-003 and the zero-dependency posture — **rejected.** SHA-256 also lets us reuse the existing leaf hashes verbatim.

---

## Trade-off Analysis

The real choice is **B vs C** — both automate drift detection; only C gives a single root. For a governance kernel whose whole point is auditability, a one-line "the kernel is intact (root: …)" that the Guardian can assert is worth the modest extra logic of a Merkle roll-up. The roll-up is a few lines of stdlib over hashes that already exist, so C's marginal cost over B is small while its auditability gain is large.

The model is deliberately kept **observational** rather than enforcing. An auto-enforcing integrity gate would conflict with PRIME_AXIOM (operator sovereignty) and the Guardian's stated prohibition on modifying/enforcing. Reporting drift loudly, and leaving the decision to the operator, is the correct altitude.

---

## Implementation

### New files (this ADR)
- `docs/adr/ADR-008-kernel-integrity-merkle.md` — this document (proposal).

### Future, separately operator-gated (NOT part of this ADR)
- A stdlib verifier tool (e.g., `01_core/control/kernel_integrity_verify.py`) + its SOURCE_MAP / TEST_CHECKLIST, matching the existing generator/control conventions.
- A recorded `KERNEL_MERKLE_ROOT` (new field in `KERNEL_HASH.md` or a sibling record).
- A Guardian hook invoking the verifier at its activation points.

### Out of scope
- Building any tooling, computing a root, or editing `KERNEL_HASH.md`.
- Changing the leaf hash format or rehashing files.
- Accepting/promoting this ADR.

---

## Consequences

**What becomes easier:**
- Drift like the FL-002 META phantom is detected automatically, with the exact drifted leaf named.
- The Guardian gains a concrete integrity check to run; its report can assert one root value.
- Hand-edits to the integrity record become verifiable instead of trusted.

**What becomes harder:**
- One more tool to build and maintain.
- The canonical kernel set must be defined precisely (what counts as "the kernel") and kept in step with `DOCTRINE_IDENTITY_REGISTRY.md`.

**Acceptance:** this ADR is **Proposed**. On operator acceptance it becomes **Accepted**, after which the verifier tool, the recorded root, and the Guardian hook can be built as separate gated steps.

---

## Governance Alignment

| Rule | How this ADR satisfies it |
|------|--------------------------|
| PRIME_AXIOM — operator sovereignty | Proposed until the operator accepts; the verifier is observational and never enforces or modifies |
| ADR-001 — governance-first | Integrity is verified and surfaced through governance, not silently trusted |
| ADR-003 — local-first / stdlib-only | SHA-256 via `hashlib`, no external dependency, no network, no attack surface; BLAKE3 explicitly rejected |
| GOVERNANCE_KERNEL_GUARDIAN — analytical safeguard, may not enforce | The verifier reports PASS/FAIL only; the Guardian summarizes, the operator decides |
| FL-002 (Operator Fault Logging / ADR-007) | This is the proposed *systemic* fix for the manual-integrity drift class that FL-002 recorded |
| Source-precedence hierarchy | External NexFS reference is cited as reference-class inspiration, never ingested as authority |
