NEXUS Base V1 — Control / Preflight Shell

Purpose:
- bounded control and preflight logic lane

Current Status:
- implemented at bounded first-pass scope
- control starter package present
- preflight_check.py exists
- preflight_check.py v1 passed
- preflight_check.py v1.1 passed

Allowed Current Contents:
- read-only preflight checks
- bounded validation helpers
- source-grounded control support logic
- checkpoint-safe control artifacts

Allowed Future Contents:
- later preflight expansions
- later Guardian-support logic with explicit scope ceilings
- later verification helpers under separate review

Disallowed:
- doctrine modification
- registry mutation
- manifest mutation
- automatic migration
- automatic approval
- runtime orchestration by default
- broad automation hub behavior

Current Ceiling:
- read-only analytical preflight lane
- no active control authority implied
- no mutation authority implied

Implementation Sequence Rule:
1. maintain bounded read-only posture
2. expand only under explicit readiness and review
3. preserve checkpoint discipline before any further widening

Output Ceiling:
- outputs remain analytical only
- PASS / WATCHLIST / INTERVENTION_REQUIRED does not equal approval
