# NEXUS HUD

**Desktop Operator HUD for the NEXUS Cognitive OS.**

Status: `PRE_DRAFT — Stage 1` · tracked build under `10_interface/nexus-hud/` (lane = interface plane). Requires Sovereign Operator approval before promotion to a NEXUS Base V1 deployment.

> **Authority posture (binding).** The HUD is the **interface plane** — the bottom of the
> NEXUS source-precedence hierarchy. It **visualizes** reconciled state; it never becomes
> state. **If anything here conflicts with doctrine, ADRs, registers, or workspace files,
> the workspace files win.** The System State surface carries this banner in-app, and
> `src/data/system_state.json` carries it in `meta.authority`.

This is a **fresh, tracked** build authored from the reference prototype at
`07_reference_material/working_reference/NEXUS_PROTOTYPE/nexus-hud/` (which is git-ignored).
It preserves that prototype's honest data model and design language.

---

## Surfaces (6)

| Surface | Purpose |
|---|---|
| Dashboard | Council status grid, standing orders, active tasks, recent memory |
| **System State** | Reconciled snapshot — kernel, doctrine count, Co-Dev status, war test, ADRs, decision register, labs, entropy (from `system_state.json`; non-authoritative) |
| Council | Detailed cards for each AI member with governance roles (5-member council) |
| Memory | Long-term context log (operator-logged + Pieces OS) |
| Tasks | Operator task queue |
| Chat | Async operator log + council response channel (not live chat) |

**Council = 5** (operator ruling 2026-05-31, odd for tie-breaking): Claude, Claude Code,
Codex, Pieces OS, NEXUS_SUXEN. IBM "Bob" is a non-voting trial auditor (read-only).

## Honest data model

Status badges reflect **provenance**, not vibes:

| Class | Meaning |
|---|---|
| `LIVE` | Real-time read from a verifiable source (Pieces OS local API, nexus-api) |
| `OPERATOR_LOGGED` | Manually logged / read-this-session by the operator or a seat |
| `UNSOURCED` | No API path exists — cannot be verified externally (NEXUS_SUXEN today) |
| `STALE` | Source exists but the feed is unfresh (e.g. the FL-002 manifest drift) |

Never invent feed sources. If `LIVE` data is unavailable, the badge stays `OPERATOR_LOGGED`
or `UNSOURCED`. Do not change the `FeedClass` type.

---

## Build stages (operator checkpoints — do not skip ahead)

```
STAGE 0 — DECISIONS                                 [COMPLETE]
STAGE 1 — SCAFFOLD                                  [THIS BUILD]
  → npm install ; npm run dev  (http://localhost:5173)
  → All six surfaces render with mock / static-snapshot data
  → No backend wiring
  Checkpoint: Operator confirms aesthetic + IA before Stage 2
STAGE 2 — BACKEND ENDPOINTS                         [NEXT — design only until approved]
  → Extend nexus-api with read-only GET /hud/* (governance, council/activity,
    memory, tasks, system-state, pieces/recent). No POST/PUT/DELETE.
STAGE 3 — DATA WIRING                               [sequential, operator-verified]
STAGE 4 — DOCKER + NGINX                            [deploy on Pi 5]
STAGE 5 — APPROVAL QUEUE                            [deferred]
STAGE 6 — PIECES OS DEEP INTEGRATION                [future]
```

## Quick start (Stage 1)

Prerequisites: Node.js ≥ 20, npm ≥ 10.

```bash
npm install
npm run dev        # open http://localhost:5173
npm run lint       # tsc --noEmit (run before every commit)
npm run build      # tsc -b && vite build (run before declaring a stage complete)
```

---

## Governance posture (preserved from NEXUS doctrine)

```
Governance is not memory.   Memory is not runtime.   Runtime is not interface.
Retrieval is not validation. Aggregation is not truth. Recall is not approval.
```

```
STATUS: DRAFT — Operator validation required before implementation
ACTIVE_ROOT: VS_CODE_NEXUS / NEXUS Base V1
SANDBOX_SCOPE: Stage 1 scaffold
PROMOTION_AUTHORIZED: NO — pending operator review
```

Source hierarchy: operator correction > doctrine registry > active standards > locked support
records > generated observational outputs > **interface surfaces (← this HUD lives here)**.
