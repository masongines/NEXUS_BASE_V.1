NEXUS Base V1 — Preflight Scope Definition

Purpose:
Define the exact bounded scope of the current first-pass control implementation.

Current Status:
- implemented at first bounded scope
- preflight_check.py exists
- preflight_check.py v1 passed
- preflight_check.py v1.1 passed

Current Implementation Objective:
A read-only preflight checker with no mutation rights and no approval authority.

Included in Current Scope:
- registry presence check
- canonical doctrine presence check
- Guardian source presence check
- manifest presence and parse check
- registry vs manifest coherence support check
- control starter-package presence check
- operator control-surface presence check
- output ceiling enforcement in result wording

Explicitly Excluded:
- file mutation
- registry updates
- manifest generation
- snapshot generation
- automatic snapshot writing
- automatic escalation
- doctrine promotion
- runtime invocation
- migration actions
- connector/API behavior

Required Output Classes:
- PASS
- WATCHLIST
- INTERVENTION_REQUIRED

Required Output Properties:
- read-only
- provenance-aware
- no approval language
- no canonicality claim
- no implementation-readiness claim by default

Failure Rule:
If a required source is absent, unreadable, or incoherent:
- report the issue
- identify the source
- classify the failure
- stop without mutation

Ceiling:
- current implementation remains bounded to preflight review only
- future expansion requires separate review and approval
