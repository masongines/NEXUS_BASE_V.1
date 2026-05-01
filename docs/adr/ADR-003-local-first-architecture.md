# ADR-003: Local-First Architecture over Cloud-Native or API-Based Deployment

**Status:** Accepted  
**Date:** 2026-05-01  
**Deciders:** Mason Gines (Sovereign Operator)

---

## Context

NEXUS Base V1 is a governed AI execution system. When deciding where it runs
and how its components communicate, there are three broad deployment models
to consider:

**Local-first** — all components run on the operator's machine. No external
services, no network calls, no cloud infrastructure. The entire system is
self-contained and offline-capable.

**Cloud-native** — components run as services (containers, serverless functions,
managed queues). State is stored in cloud databases. Scaling is handled by the
platform.

**API-based** — the core runtime is local, but it calls external APIs for threat
detection, approval routing, or logging (e.g., a SaaS security intelligence
feed, a remote approval dashboard, a cloud logging service).

---

## Decision

**Local-first: all components run in-process on the operator's machine with no
external service dependencies.**

Every subsystem — security monitor, trust registry, approval gate, execution
engine, and logger — is a Python module that runs in the same process. All state
(logs, trust registry, action schema) is stored as local JSON or append-only text
files. No network calls are made at any point in the execution pipeline.

---

## Options Considered

| Dimension | Local-First (chosen) | Cloud-Native | API-Based |
|---|---|---|---|
| Complexity | Low — single process, stdlib only | High — infra, IAM, networking | Medium — external deps, auth |
| External attack surface | None — no network exposure | Large — all components network-accessible | Medium — API endpoints are attack surface |
| External dependencies | None | Many (cloud provider, platform) | API providers, network availability |
| Auditability | Complete — all state is local files | Partial — depends on cloud provider's logging | Partial — external service logs may not be accessible |
| Governance model validation | Direct — operator controls everything | Indirect — cloud provider is a third party in the trust chain | Indirect — API provider is in the trust chain |
| Operator sovereignty | Absolute | Delegated to cloud provider | Partially delegated to API providers |
| Scalability | Single machine | Horizontal | Moderate |
| Setup friction | None — `python nexus_war_test.py` | High — infra provisioning | Medium — API keys, auth setup |

---

## Trade-off Analysis

The primary weakness of local-first is **scalability**: the system cannot
distribute load across multiple machines or serve multiple operators
simultaneously. Cloud-native deployment addresses this directly.

However, scalability is explicitly **not a goal of NEXUS Base V1**. The goal is
to prove that the governance model works — that approval gating, trust-based
automation, and rule-based threat detection can be implemented as a coherent,
testable architecture.

Adding cloud infrastructure to a system whose governance model is unproven would
be premature: it would introduce operational complexity, external trust
dependencies, and debugging surface before the foundational question is
answered. If the governance model has a flaw, it is much easier to find and fix
it in a local-first system than in a distributed one.

This is the same principle as *building a prototype before a production system*:
prove the concept in the simplest possible environment, then extend.

There is a second reason: **operator sovereignty**. Under PRIME_AXIOM, the
Sovereign Operator is the root authority. A cloud-native deployment delegates
part of that authority to a cloud provider — their availability, their security
controls, their access to the operator's data. Local-first keeps the operator's
authority intact. Every log, every trust registry entry, every execution record
is on the operator's machine.

---

## Consequences

**What becomes easier:**
- Cold-clone quickstart: `git clone` + `python nexus_war_test.py` — no credentials,
  no infrastructure, no setup
- Full auditability: all state is local files the operator can inspect directly
- War test determinism: test results are not affected by network conditions,
  API rate limits, or external service outages
- Operator sovereignty: no third party is in the execution trust chain

**What becomes harder:**
- Multi-operator or multi-machine deployment
- Integration with external threat intelligence feeds
- Real-time remote monitoring or dashboards
- Horizontal scaling for high-throughput action pipelines

**What we will revisit in future versions:**
- A thin API layer (FastAPI) to expose the approval gate as an HTTP endpoint,
  enabling remote operator approval without requiring cloud infrastructure
- Optional cloud logging sink (append-only, write-only credentials) to provide
  off-machine audit durability

---

## Governance Alignment

- **PRIME_AXIOM Rule X (Governance Root Principle):** Operator sovereignty is the
  root of the authority hierarchy. Local-first ensures no external party is
  interpolated into the operator's authority chain.
- **Execution Contract Rule 3:** All executions must be logged (append-only) —
  local append-only log files fulfill this without introducing external service
  dependencies.
- **NEXUS_BASE_V1_DEEP_DIVE.md (Stage/Evolution section):** The staged evolution
  model explicitly identifies local-first as the correct posture for Base V1,
  with distribution as a future-stage concern.
