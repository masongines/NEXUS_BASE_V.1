# ADR-001: Governance-First Architecture

**Status:** Accepted  
**Date:** 2026-05-01  
**Deciders:** Mason Gines (Sovereign Operator)

---

## Context

Every AI execution system must answer a foundational ordering question: does
authorization happen *before* an action executes, or does the system execute
first and validate after?

Execution-first systems are common in early-stage AI tooling because they are
simpler to build. The system runs, then checks logs, then flags anomalies. The
cost is that unauthorized or malicious actions may have already produced side
effects before any governance layer fires.

NEXUS Base V1 was designed for a context where that trade-off is unacceptable:
a governed AI execution environment where the Sovereign Operator must be the
authority for every action, and where auditability is a first-class requirement
(not a post-hoc addition).

---

## Decision

**Governance-first:** every action passes through the full security → trust →
approval pipeline *before* the execution engine is reached. Execution is the
terminal step, not the first step.

The pipeline is strictly ordered and non-bypassable:

```
Action → Security Monitor → Trust Registry → Approval Gate → Execution Engine → Logger
```

No action may skip a stage. Blocked or quarantined actions are logged before
they are discarded.

---

## Options Considered

| Dimension | Governance-First (chosen) | Execution-First |
|---|---|---|
| Complexity | Medium — pipeline adds stages | Low — execute, then audit |
| Latency | Higher — gate adds overhead | Lower — no pre-flight |
| Auditability | Complete — every decision is logged before execution | Partial — post-hoc only |
| Blast radius on failure | Low — unauthorized actions never reach execution | High — actions may execute before detection |
| Explainability | Full — each gate decision is traceable | Partial — post-execution analysis required |
| Operator control | Absolute — gate is the chokepoint | Delegated — action runs before operator sees it |

---

## Trade-off Analysis

The core trade-off is **latency and simplicity vs. safety and auditability**.

Execution-first is faster to build and introduces no latency overhead. For
systems where actions are cheap to reverse and threats are rare, this may be
acceptable.

NEXUS Base V1 operates under the opposite assumption: the cost of an
unauthorized action is higher than the cost of a delayed or rejected execution.
This is borrowed directly from construction operations — the *permit-before-dig*
principle. A crew does not excavate and then apply for a permit. The permit is
the authorization that makes execution legal.

Applied to AI: an AI agent does not act and then ask for review. Authorization
precedes action.

---

## Consequences

**What becomes easier:**
- Threat containment: T2 threats are quarantined before they can cause harm
- Auditability: every gate decision is logged with timestamp, actor, and outcome
- Operator trust: the operator knows no action executed without passing the full pipeline

**What becomes harder:**
- Throughput: every action pays the full pipeline cost, even trusted ones
- Bootstrapping: new action types must be explicitly added to the trust registry before they can auto-approve
- Complexity: adding a new gate requires updating the pipeline contract

**What we will revisit in future versions:**
- Async approval for low-risk, high-frequency trusted actions (performance optimization)
- Parallel threat scanning for multi-action batches

---

## Governance Alignment

- **PRIME_AXIOM Rule III:** No output or behavior becomes accepted without explicit
  consent from the Sovereign Operator — the approval gate operationalizes this rule.
- **Execution Contract Rule 1:** No action executes without operator approval — this
  ADR is the architectural expression of that rule.
- **Execution Contract Rule 3:** All executions must be logged (append-only) — the
  Logger stage at the end of the pipeline fulfills this.
