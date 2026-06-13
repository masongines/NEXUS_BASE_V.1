# NEXUS HUD — Stage 2 Endpoint Contracts

**Status:** DESIGN ONLY
**Stage:** Stage 2 contract draft
**Implementation authorized:** NO
**Authority:** Interface-plane documentation only

---

## 0. Binding Rule

The HUD is an interface plane.

It visualizes state.
It does not become state.
It does not approve, promote, validate, modify, or enforce governance.

Workspace files, doctrine, ADRs, support records, audit logs, and operator rulings override all HUD output.

All Stage 2 endpoints are:

```text
READ ONLY
GET ONLY
NO POST
NO PUT
NO PATCH
NO DELETE
NO AUTO-WRITE
```

Allowed `feedClass` values:

```text
LIVE
OPERATOR_LOGGED
UNSOURCED
STALE
```

Do not introduce `MIXED` or any other feed class. If a response contains mixed provenance, set `meta.feedClass` to `OPERATOR_LOGGED` and require each item to carry its own `feedClass`.

---

## 1. GET /hud/system-state

### Purpose

Return the reconciled system-state snapshot used by the HUD System State surface.

### Sources

Primary source class:

```text
03_system_state/manifests/KERNEL_MANIFEST.json
03_system_state/reports/war_test_report.json
00_governance_ref/support_records/KERNEL_VERSION.md
docs/adr/
04_logs/audit/fault_log.md
10_interface/nexus-hud/src/data/system_state.json
```

### Response Shape

```json
{
  "meta": {
    "title": "NEXUS — Reconciled System State",
    "authority": "INTERFACE SURFACE — NON-AUTHORITATIVE",
    "gitHead": "short SHA",
    "feedClass": "OPERATOR_LOGGED",
    "source": "workspace snapshot"
  },
  "kernel": {
    "version": "1.2",
    "status": "STABLE",
    "feedClass": "OPERATOR_LOGGED"
  },
  "doctrine": {
    "count": 12,
    "feedClass": "OPERATOR_LOGGED"
  },
  "warTest": {
    "pass": 36,
    "warn": 0,
    "fail": 0,
    "feedClass": "OPERATOR_LOGGED"
  },
  "adrs": [],
  "decisionRegister": [],
  "labs": [],
  "entropy": {
    "riskBand": "GREEN",
    "feedClass": "OPERATOR_LOGGED"
  }
}
```

### Failure Behavior

| Case                   | Response                                    |
| ---------------------- | ------------------------------------------- |
| Snapshot missing       | `404`, `feedClass: "UNSOURCED"`             |
| Partial source missing | `200`, unavailable field marked `UNSOURCED` |
| Stale source           | `200`, affected field marked `STALE`        |

### Prohibited

```text
Do not auto-refresh.
Do not trigger reconciliation.
Do not edit manifests.
Do not edit fault logs.
Do not promote system state to authority.
```

---

## 2. GET /hud/governance

### Purpose

Return active governance display data: source hierarchy, boundary rules, standing orders, and AI ceiling.

### Sources

```text
00_governance_ref/
00_governance_ref/active_standards/NEXUS_CO_DEV_PROTOCOL_v1.md
00_governance_ref/doctrine/
00_governance_ref/support_records/
```

### Response Shape

```json
{
  "sourceHierarchy": [
    {"rank": 1, "name": "operator correction"},
    {"rank": 2, "name": "doctrine registry"},
    {"rank": 3, "name": "active standards"},
    {"rank": 4, "name": "locked support records"},
    {"rank": 5, "name": "generated observational outputs"},
    {"rank": 6, "name": "interface surfaces"}
  ],
  "boundaryRules": [
    "Governance is not memory.",
    "Memory is not runtime.",
    "Runtime is not interface.",
    "Retrieval is not validation.",
    "Aggregation is not truth.",
    "Recall is not approval."
  ],
  "standingOrders": [],
  "aiCeiling": {
    "summary": "AI is advisory unless operator explicitly approves a narrow implementation task.",
    "feedClass": "OPERATOR_LOGGED"
  },
  "meta": {
    "feedClass": "OPERATOR_LOGGED",
    "source": "00_governance_ref/"
  }
}
```

### Failure Behavior

| Case                      | Response                                   |
| ------------------------- | ------------------------------------------ |
| Governance source missing | `404`, `feedClass: "UNSOURCED"`            |
| Partial rule unavailable  | `200`, unavailable rule marked `UNSOURCED` |

### Prohibited

```text
Do not validate operator decisions.
Do not gate HUD features from this endpoint.
Do not modify doctrine or standards.
Do not infer missing governance rules.
```

---

## 3. GET /hud/council

### Purpose

Return council roster and activity metadata.

### Current Composition

Voting members: 5

```text
Claude
Claude Code
Codex
Pieces OS
NEXUS_SUXEN
```

Trial auditor: 1

```text
IBM Bob — non-voting, read-only
```

### Sources

```text
10_interface/nexus-hud/src/data/council.ts
operator ruling 2026-05-31
handoff records
```

### Response Shape

```json
{
  "councilComposition": {
    "total": 6,
    "votingMembers": 5,
    "trialAuditors": 1
  },
  "members": [
    {
      "id": "claude",
      "name": "Claude",
      "role": "Architect & Orchestrator",
      "feedClass": "OPERATOR_LOGGED",
      "lastActivity": "Session active"
    }
  ],
  "trialAuditors": [
    {
      "id": "bob_ibm",
      "name": "IBM Bob",
      "role": "Standards/Security Auditor",
      "feedClass": "OPERATOR_LOGGED"
    }
  ],
  "meta": {
    "feedClass": "OPERATOR_LOGGED",
    "source": "operator ruling + council.ts"
  }
}
```

### Failure Behavior

| Case                 | Response                                             |
| -------------------- | ---------------------------------------------------- |
| Roster unavailable   | `404`, `feedClass: "UNSOURCED"`                      |
| Activity unavailable | `200`, roster preserved, activity marked `UNSOURCED` |

### Prohibited

```text
Do not create voting UI.
Do not modify council membership.
Do not auto-enable or disable members.
Do not treat member status as governance authority.
```

---

## 4. GET /hud/memory

### Purpose

Return recent advisory memory entries from Pieces OS and operator-logged records.

### Sources

```text
Pieces OS local API, if available
03_system_state/context_exports/
07_reference_material/
operator handoff records
```

### Query Parameters

```text
limit
offset
kind
source
tags
startDate
endDate
```

### Response Shape

```json
{
  "entries": [
    {
      "id": "m1",
      "kind": "RECALL",
      "source": "Pieces OS",
      "timestamp": "ISO date",
      "body": "memory text",
      "tags": ["system"],
      "feedClass": "LIVE"
    }
  ],
  "pagination": {
    "limit": 50,
    "offset": 0,
    "total": 1
  },
  "meta": {
    "feedClass": "OPERATOR_LOGGED",
    "source": "Pieces OS + operator logs"
  }
}
```

### FeedClass Rules

| Condition             | feedClass         |
| --------------------- | ----------------- |
| Pieces available      | `LIVE`            |
| Operator log fallback | `OPERATOR_LOGGED` |
| Old snapshot          | `STALE`           |
| No source             | `UNSOURCED`       |

### Failure Behavior

| Case                             | Response                        |
| -------------------------------- | ------------------------------- |
| Pieces unavailable with fallback | `200`, fallback entries         |
| No fallback                      | `503`, `feedClass: "UNSOURCED"` |
| Invalid filter                   | `400`                           |

### Prohibited

```text
Do not use memory as truth.
Do not write to Pieces.
Do not promote recall to authority.
Do not auto-sync memory to workspace files.
```

---

## 5. GET /hud/tasks

### Purpose

Return operator task queue and blocked work.

### Sources

Current source class:

```text
handoff records
operator-logged task entries
HUD mock task data
future task registry
```

Do not assume `06_operator/` exists unless verified.

### Query Parameters

```text
status
priority
owner
tags
```

### Response Shape

```json
{
  "tasks": [
    {
      "id": "t1",
      "title": "Draft HUD Stage 2 endpoint contracts",
      "detail": "Create design-only contracts.",
      "priority": "HIGH",
      "owner": "Operator",
      "status": "ACTIVE",
      "tags": ["HUD", "stage-2"],
      "feedClass": "OPERATOR_LOGGED"
    }
  ],
  "summary": {
    "active": 1,
    "blocked": 0,
    "done": 0,
    "pending": 0
  },
  "meta": {
    "feedClass": "OPERATOR_LOGGED",
    "source": "operator-logged task records"
  }
}
```

### Failure Behavior

| Case           | Response                                 |
| -------------- | ---------------------------------------- |
| No task source | `200`, empty task list                   |
| Parse error    | `500`, affected items marked `UNSOURCED` |

### Prohibited

```text
Do not complete tasks from HUD.
Do not edit tasks from HUD.
Do not auto-sync task status.
Do not create task write endpoints.
```

---

## 6. GET /hud/pieces

### Purpose

Return Pieces OS availability and recent capture metadata.

### Sources

```text
Pieces OS local API
operator-logged Pieces snapshots
context export files
```

### Query Parameters

```text
limit
type
```

### Response Shape

```json
{
  "status": "connected",
  "stats": {
    "totalSnapshotsAvailable": 0,
    "workflowsActive": 0,
    "ltmEntriesTotal": 0,
    "feedClass": "LIVE"
  },
  "recentCaptures": [],
  "ltmCapability": {
    "enabled": true,
    "personalCloudEnabled": false,
    "feedClass": "LIVE"
  },
  "meta": {
    "lastSync": "ISO date",
    "feedClass": "LIVE",
    "source": "Pieces OS local API"
  }
}
```

### FeedClass Rules

| Condition                | feedClass         |
| ------------------------ | ----------------- |
| Pieces API responsive    | `LIVE`            |
| Recent operator snapshot | `OPERATOR_LOGGED` |
| Old snapshot             | `STALE`           |
| No Pieces source         | `UNSOURCED`       |

### Failure Behavior

| Case                                | Response                                           |
| ----------------------------------- | -------------------------------------------------- |
| Pieces unavailable with snapshot    | `200`, snapshot fallback                           |
| Pieces unavailable with no snapshot | `503`, `feedClass: "UNSOURCED"`                    |
| Personal cloud enabled              | `200`, warning in `meta`, operator review required |

### Prohibited

```text
Do not write to Pieces.
Do not expose full Pieces API.
Do not auto-export HUD state to Pieces.
Do not treat Pieces memory as authority.
```

---

## 7. Implementation Gate

This document does not authorize implementation.

Implementation requires operator approval for:

```text
endpoint list
response shapes
source files
feedClass assignment
backend read permissions
failure behavior
prohibited behavior
Stage 2 to Stage 3 transition
```

Until then:

```text
Stage 2 = contract documentation only
Stage 3 = backend endpoint implementation, if approved
Stage 4 = live HUD wiring, if approved
```

**End of Stage 2 contract draft.**
