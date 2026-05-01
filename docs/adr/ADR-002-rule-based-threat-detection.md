# ADR-002: Rule-Based Threat Detection over ML/Embedding-Based Anomaly Detection

**Status:** Accepted  
**Date:** 2026-05-01  
**Deciders:** Mason Gines (Sovereign Operator)

---

## Context

The Security Monitor in NEXUS Base V1 must classify incoming actions as benign,
suspicious, or malicious before they reach the Trust Registry. There are two
primary design families for this classification task:

**Rule-based detection** — explicit keyword patterns and structural rules that
match known threat signatures. If a trigger phrase is present in the action
payload, the action is flagged. The decision is deterministic and fully
explainable.

**ML/embedding-based anomaly detection** — a model (e.g., a nearest-neighbour
embedder or fine-tuned classifier) learns a representation of "normal" action
space and flags actions that deviate from it. Recall on novel threats is higher
because the model generalizes beyond seen trigger phrases.

---

## Decision

**Rule-based detection using an explicit `frozenset` of threat triggers.**

The Security Monitor serializes the full action payload to a lowercase string and
checks for any phrase in the trigger set. This broad-match approach provides
complete coverage of the action — including nested fields — without requiring
field-by-field inspection.

Current trigger set:
```python
_THREAT_TRIGGERS = frozenset({
    "ignore previous instructions",
    "send system data",
    "reveal secrets",
    "bypass",
    "exfiltrate",
})
```

---

## Options Considered

| Dimension | Rule-Based (chosen) | ML / Embedding-Based |
|---|---|---|
| Complexity | Low — frozenset + string match | High — model training, embedding infrastructure |
| Explainability | 100% — exact trigger phrase is logged | Partial — similarity score, not a human-readable reason |
| Determinism | Fully deterministic | Non-deterministic (model updates change behavior) |
| False negative on novel threats | Higher — unknown phrases not caught | Lower — model may generalize |
| Training data requirement | None | Substantial — labeled threat/benign pairs |
| Operator auditability | Every block has an exact reason | Reason is a vector distance, not a rule |
| Runtime overhead | Negligible — O(n) string scan | Higher — embedding inference per action |

---

## Trade-off Analysis

The primary weakness of rule-based detection is **coverage of novel threats**: an
adversary who avoids every phrase in the trigger set can bypass the monitor. ML
detection addresses this by learning a representation of the threat space rather
than enumerating it.

However, this weakness is acceptable for NEXUS Base V1 for two reasons:

1. **Explainability is non-negotiable in a governance system.** When an action is
   blocked, the operator must be able to read *exactly why* in plain language. A
   similarity score of 0.83 to a threat cluster is not an auditable reason. An
   exact matched trigger phrase is.

2. **A black box cannot be verified.** The war test suite (`nexus_war_test.py`)
   validates the Security Monitor by asserting that specific known-threat phrases
   produce quarantine outcomes and specific safe phrases do not. This is only
   possible because the monitor is fully deterministic. An ML model's behavior
   changes when its weights are updated, which would invalidate the war test's
   guarantees.

The threat model (`00_governance_ref/security/threat_model_v1.md`) defines three
tiers: Tier 1 (benign/malformed), Tier 2 (suspicious/injection), Tier 3
(malicious/exfiltration). Rule-based detection is sufficient to enforce the T2/T3
boundary for the threat categories defined in Base V1.

---

## Consequences

**What becomes easier:**
- Every block decision is fully auditable and logged with an exact reason
- The war test can assert deterministic quarantine behavior
- The trigger set can be extended without retraining — add a phrase, commit, done
- No external dependencies or model hosting required

**What becomes harder:**
- Novel threat phrases not in the trigger set will not be caught
- Adversaries with knowledge of the trigger set can craft evasive payloads
- Coverage requires ongoing curation of the trigger set as new threat patterns emerge

**What we will revisit in future versions:**
- Hybrid approach: rule-based as a fast first pass, ML as a secondary pass for
  ambiguous actions that pass the rule filter but exhibit suspicious structural
  patterns

---

## Governance Alignment

- **Execution Contract Rule 1:** No action executes without operator approval —
  the monitor's quarantine decision is logged before any further evaluation, and
  quarantined actions never reach the approval gate.
- **Threat Model Core Rule:** No threat may trigger execution without operator
  approval — rule-based detection ensures the monitor's decision is fully
  traceable and the operator can verify every block decision independently.
- **PRIME_AXIOM Rule III:** No behavior becomes accepted without explicit consent —
  deterministic rule-based detection means the operator can verify the monitor's
  behavior without trusting a model whose internals are opaque.
