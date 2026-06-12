Compacted conversation# HUD Stage 3 Architecture Verification — Handoff Summary

**Completed:** 2026-06-11  
**Status:** Analysis complete; ready for operator approval  
**Authority:** Handoff to operator for Stage 3 gate decisions

---

## What Was Investigated

**Research Scope:** Determine whether HUD can consume existing NEXUS services vs. requires new dedicated backend.

**Questions Addressed:**
1. ✅ Is there an existing HTTP/API service?
2. ✅ Is there an existing JSON-producing runtime surface?
3. ✅ Can HUD consume existing runtime output directly?
4. ✅ Would adding /hud/* to runtime violate governance/security?
5. ✅ Is a new dedicated HUD backend necessary?
6. ✅ Recommended architecture?
7. ✅ Evidence and file citations?
8. ✅ Risks and unknowns?

**Research Method:** Read-only codebase analysis, governance document review, architecture decision record examination.

---

## Key Findings

| Finding | Status | Evidence |
|---------|--------|----------|
| No existing HTTP service | ✅ Confirmed | README_API.txt and README_RUNTIME.txt are placeholders only |
| Executor is CLI-based (not a server) | ✅ Confirmed | executor.py has no HTTP wrapper; designed for testing |
| ADR-003 prohibits persistent services | ✅ Confirmed | ADR-003 Local-First Architecture: "no persistent background services" |
| ADR-004 defers FastAPI to future work | ✅ Confirmed | ADR-004 Tri-Sync Architecture: "FastAPI... deferred per ADR-003" |
| Execution Contract requires read/write separation | ✅ Confirmed | execution_contract.md: "Outputs are observational (non-authoritative)" |
| Adding /hud/* to executor violates governance | ✅ Confirmed | Would couple HUD observation to executor decision-making; violates ADR-003 and Execution Contract §4 |

---

## Recommendation

**Architecture: NEW DEDICATED READ-ONLY BACKEND**

### Why This Works:

- ✅ **Preserves ADR-003:** Backend reads local files directly; no persistent executor service
- ✅ **Preserves Execution Contract:** Executor remains write-only; backend is read-only interface
- ✅ **Clean separation:** HUD interface ≠ execution engine
- ✅ **No new dependencies:** Pure Python `http.server` stdlib only
- ✅ **Test isolation:** War test unchanged; HUD backend tested separately
- ✅ **Scalability:** HUD can evolve independently without affecting executor

### Proposed Structure:

```
10_interface/nexus-hud/
├── backend/
│   ├── hud_service.py         (http.server listener, GET-only)
│   ├── endpoints/
│   │   ├── system_state.py
│   │   ├── governance.py
│   │   ├── council.py
│   │   ├── tasks.py
│   │   ├── memory.py
│   │   └── pieces.py
│   ├── data_sources/           (workspace file readers + fallback logic)
│   └── requirements.txt        (empty — pure stdlib)
└── src/                        (existing frontend)
```

---

## Next Steps: 8 Operator Approval Gates

**All gates must be approved before Stage 3 implementation begins.**

| Gate | Component | Approval Required | Status |
|------|-----------|-------------------|--------|
| **Gate 1** | Architecture (Python stdlib, location, read-only) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 2** | Endpoint list (6 GET endpoints) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 3** | Data sources (read permissions per endpoint) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 4** | FeedClass rules (LIVE/OPERATOR_LOGGED/UNSOURCED/STALE) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 5** | Test plan (unit + integration + war test) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 6** | Security constraints (GET-only, no leaks, Pieces fallback) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 7** | Governance alignment (interface plane, workspace override) | ✅ Documented | ⏳ Operator sign-off |
| **Gate 8** | Deployment (dev localhost vs. prod Nginx proxy) | ✅ Documented | ⏳ Operator sign-off |

**Gate Documentation:** See HUD_STAGE_2_ENDPOINT_CONTRACTS.md and HUD_STAGE_3_IMPLEMENTATION_PLAN.md (if created).

---

## Operator Clarifications Pending

**These must be answered before implementation:**

| Item | Impact | Status |
|------|--------|--------|
| Operator task storage format | `/hud/tasks` endpoint | ⏳ Needs clarification |
| Pieces OS fallback behavior | `/hud/pieces` endpoint | ⏳ Needs clarification |
| Frontend-backend URL discovery | Dev vs. prod config | ⏳ Needs clarification |
| War test expansion scope | Backend endpoint testing? | ⏳ Needs decision |

---

## Risks Identified

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Backend becomes complex (scope creep) | MEDIUM | Enforce strict read-only discipline; code review gate |
| ADR-003 interpretation unclear | LOW | Clarify if "local-only HTTP service" is allowed |
| Data staleness issues | MEDIUM | Mark all responses with `feedClass`; include timestamp; require operator refresh |
| Pieces OS unavailability | LOW | Graceful fallback to `UNSOURCED` feedClass |

---

## Evidence Artifacts

**Files Reviewed:**
- README.md — no HTTP service exposed
- bootstrap_runtime.py — executor bootstrapped as CLI
- executor.py — CLI-based, no server
- README_API.txt — placeholder
- README_RUNTIME.txt — placeholder
- ADR-003-local-first-architecture.md — local-first decision
- ADR-004-tri-sync-architecture.md — FastAPI deferred
- execution_contract.md — observational outputs
- api.ts — frontend expects `/api/hud/*`
- HUD_STAGE_2_ENDPOINT_CONTRACTS.md — endpoint specs

---

## Status Summary

✅ **Architecture Verification:** COMPLETE  
⏳ **Operator Approval (8 gates):** PENDING  
⏳ **Operator Clarifications (4 items):** PENDING  
⏸️ **Stage 3 Implementation:** BLOCKED until gates approved

---

## Handoff to Next Agent

**When operator approves all 8 gates:**
1. Create 10_interface/nexus-hud/backend/ directory structure
2. Implement 6 read-only GET endpoints per HUD_STAGE_2_ENDPOINT_CONTRACTS.md
3. Write unit tests (file I/O, feedClass, error handling)
4. Verify war test remains 36/0 (no regressions)
5. Begin Phase 2 after Phase 1 success (live endpoints + Pieces integration)

**Critical Constraints:**
- READ-ONLY only (no POST/PUT/PATCH/DELETE)
- Pure stdlib only (no new pip packages)
- All responses marked with `feedClass` (LIVE/OPERATOR_LOGGED/UNSOURCED/STALE)
- Must not write to workspace files (interface plane rule)
- War test baseline must remain 36/0

---

**Ready for operator review and gate approvals.**