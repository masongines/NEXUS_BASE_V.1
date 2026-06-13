# NEXUS HUD — Stage 3 System-State Mockup QC v0.1

**Date:** 2026-06-12 / 2026-06-13 UTC
**Repo state at draft:** `main`, `origin/main`, `local-work`, and `origin/local-work` synced at `93b8183`
**Authority class:** Stage 3 mockup / QC draft
**Promotion status:** Not doctrine
**Implementation status:** No backend implementation authorized by this document
**Scope:** `GET /hud/system-state` mockup and quality-control confirmation only

---

## 0. Purpose

This document defines the quality-control mockup for the first proposed HUD Stage 3 backend endpoint:

```text
GET /hud/system-state
```

The goal is to verify expected behavior, response shape, provenance behavior, operator usability, and safety boundaries before any backend implementation begins.

This document does not authorize backend code, file creation outside this draft, frontend wiring, service startup, live integration, endpoint implementation, doctrine promotion, or ADR acceptance.

---

## 1. Stage Position

Current stage posture:

```text
Stage 1 — HUD scaffold: complete
Stage 2 — endpoint contracts: complete
Stage 3 — architecture verification: complete
Stage 3 implementation: blocked pending gate review
```

Current approved review posture:

```text
Gate 1 — Architecture:
PROVISIONAL PASS WITH CONSTRAINTS G1-A + G1-B

Gate 2 — Endpoint List:
PROVISIONAL PASS WITH CONSTRAINTS G2-A + G2-B + G2-C + G2-D
```

Current active review lane:

```text
Gate 3 — Data Sources for GET /hud/system-state
Gate 4 — FeedClass behavior for GET /hud/system-state
Gate 5 — Test Plan preparation
Gate 6 — Security Constraints preparation
```

---

## 2. Endpoint Under Mock Review

```text
GET /hud/system-state
```

### Intended role

Provide a read-only HUD-facing summary of current system state using approved local source files.

### Non-role

This endpoint is not:

* a general NEXUS API
* a runtime controller
* an executor wrapper
* a doctrine authority
* an ADR promotion mechanism
* a manifest generator
* a war-test runner
* a task mutator
* a memory sync surface
* a Pieces integration
* a background service
* a daemon

---

## 3. Mock Data Source Map

Candidate approved local sources for first implementation review:

```text
03_system_state/manifests/KERNEL_MANIFEST.json
03_system_state/reports/WAR_TEST_REPORT.md
04_logs/audit/fault_log.md
docs/adr/
00_governance_ref/support_records/KERNEL_MANIFEST.SUPERSEDED.md
```

Optional / later sources:

```text
03_system_state/snapshots/SYSTEM_STATE_SNAPSHOT_CURRENT.md
00_governance_ref/support_records/DOCTRINE_IDENTITY_REGISTRY.md
```

Rejected for first implementation pass:

```text
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
```

---

## 4. Mock Response Shape

The first mock response should use this shape:

```json
{
  "meta": {
    "endpoint": "/hud/system-state",
    "schemaVersion": "0.1",
    "feedClass": "OPERATOR_LOGGED",
    "generatedAt": "STATIC_MOCK_TIMESTAMP",
    "sourceMode": "mock",
    "authority": "interface-adapter-only",
    "implementationAuthorized": false
  },
  "system": {
    "project": "NEXUS Base V1",
    "branchState": {
      "main": "93b8183",
      "originMain": "93b8183",
      "localWork": "93b8183",
      "originLocalWork": "93b8183",
      "parity": true
    },
    "warTest": {
      "version": "1.1.0",
      "pass": 36,
      "warn": 0,
      "fail": 0,
      "verdict": "PASS",
      "feedClass": "OPERATOR_LOGGED"
    },
    "hud": {
      "stage1": "complete",
      "stage2Contracts": "complete",
      "stage3ArchitectureVerification": "complete",
      "stage3Implementation": "blocked",
      "feedClass": "OPERATOR_LOGGED"
    },
    "governance": {
      "doctrinePromotion": "not_authorized",
      "adrAcceptance": "not_authorized",
      "backendImplementation": "not_authorized",
      "feedClass": "OPERATOR_LOGGED"
    }
  },
  "sources": [
    {
      "path": "03_system_state/reports/WAR_TEST_REPORT.md",
      "feedClass": "OPERATOR_LOGGED",
      "required": true,
      "status": "mocked"
    },
    {
      "path": "03_system_state/manifests/KERNEL_MANIFEST.json",
      "feedClass": "OPERATOR_LOGGED",
      "required": true,
      "status": "mocked"
    },
    {
      "path": "04_logs/audit/fault_log.md",
      "feedClass": "OPERATOR_LOGGED",
      "required": false,
      "status": "mocked"
    },
    {
      "path": "docs/adr/",
      "feedClass": "OPERATOR_LOGGED",
      "required": false,
      "status": "mocked"
    }
  ],
  "warnings": [
    {
      "code": "MOCK_ONLY",
      "message": "This response is a Stage 3 mockup and is not live backend output."
    },
    {
      "code": "NO_IMPLEMENTATION_AUTHORIZED",
      "message": "Backend implementation remains blocked pending gate review."
    }
  ]
}
```

---

## 5. FeedClass Rule

Allowed response-level `meta.feedClass` values:

```text
LIVE
OPERATOR_LOGGED
UNSOURCED
STALE
```

Invalid:

```text
MIXED
```

For this mockup:

```text
meta.feedClass = OPERATOR_LOGGED
```

Reason:

The mock is based on operator-verified local repo state and documented verification results, but it is not live backend output.

If any item uses a weaker source, that item must carry its own feedClass.

---

## 6. Quality-Control Checks

Before implementation, the mockup must pass these checks:

### QC-1 — Endpoint scope

Pass if the mock response represents only:

```text
GET /hud/system-state
```

Fail if it introduces new endpoint behavior.

### QC-2 — Read-only posture

Pass if the mock response implies no writes, no mutation, no execution, and no generation.

Fail if it implies manifest regeneration, war-test execution, ADR mutation, doctrine promotion, or file writing.

### QC-3 — Authority boundary

Pass if the response clearly states HUD output is interface-adapter-only.

Fail if the response presents HUD output as canonical authority.

### QC-4 — FeedClass validity

Pass if response-level feedClass is one of:

```text
LIVE
OPERATOR_LOGGED
UNSOURCED
STALE
```

Fail if `MIXED` appears as response-level FeedClass.

### QC-5 — Source traceability

Pass if each major field maps to a local source or mock status.

Fail if state appears without source or status.

### QC-6 — Implementation block

Pass if the mock explicitly states:

```text
implementationAuthorized: false
```

Fail if the mock implies backend implementation is already approved.

### QC-7 — Security boundary

Pass if the mock implies no shell, no executor import, no subprocess, no external API, no daemon, and no external bind.

Fail if it implies any runtime control path.

---

## 7. Operator Usage Confirmation Questions

Before implementation, operator should confirm:

1. Does this response shape display the right information for the HUD System State panel?
2. Is the `meta` block clear enough to prevent pseudo-authority?
3. Are source references explicit enough?
4. Should branch parity be shown in the endpoint or left out as Git-only context?
5. Should war-test results be shown as current verified result or stale file-derived result?
6. Should ADR status be summarized in `/hud/system-state`, or reserved for `/hud/governance`?
7. Should `implementationAuthorized: false` remain visible in the response after implementation, or move to a warning/status field?

---

## 8. Mock Acceptance Criteria

This mockup may pass if:

```text
Operator confirms response shape is useful.
Operator confirms authority boundary is clear.
Operator confirms FeedClass behavior is acceptable.
Operator confirms first implementation should remain limited to GET /hud/system-state.
Operator confirms no live Pieces/task/memory integration is implied.
```

This mockup must hold if:

```text
Response shape is confusing.
HUD authority boundary is unclear.
Source mapping is too broad.
FeedClass behavior is ambiguous.
Operator wants `/hud/governance` separated before implementation.
Security boundary is insufficient.
```

---

## 9. Recommended Next Step After Mock QC

If mock QC passes, draft the implementation packet for:

```text
GET /hud/system-state only
```

That packet must include:

* exact backend file list
* exact source files to read
* no-write guarantee
* no-executor-import guarantee
* allowed HTTP methods
* loopback binding
* missing-source fallback behavior
* test commands
* rollback plan
* operator approval checkpoint

No backend code should be written until that implementation packet is approved.

---

## 10. Current Boundary

This document is a mockup/QC draft only.

It does not authorize:

* backend implementation
* endpoint creation
* server startup
* frontend wiring
* live data integration
* Pieces integration
* memory sync
* task mutation
* polling
* daemonization
* GitHub network access
* doctrine promotion
* ADR acceptance
* repo mutation beyond saving this draft if operator approves
