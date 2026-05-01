NEXUS Base V1 — Generators Shell

Purpose:
- home for bounded generator logic

Current Status:
- implemented at bounded lane scope
- manifest generator selected as first generator target and passing
- snapshot generator selected as second bounded generator target and passing at v1
- no broader generator bundle active

Current Implemented Artifacts:
- manifest_generator.py
- snapshot_generator.py

Current Known Passes:
- manifest_generator.py v1 passed
- manifest_generator.py v1.1 passed
- snapshot_generator.py v1 passed

Allowed Current Contents:
- bounded generator implementations
- generator source maps
- generator test checklists
- scope definitions
- observational-only output builders

Allowed Future Contents:
- later context export generator work after separate readiness treatment
- later bounded generator helper logic
- later generator-lane refinements under checkpoint discipline

Disallowed:
- doctrine modification
- registry modification
- support record mutation
- automatic promotion
- runtime orchestration
- broad uncontrolled automation
- bundled multi-generator expansion by default

Current Ceiling:
- generator lane is active only at bounded observational scope
- outputs remain observational only
- no generator output implies approval or canonical authority

Implementation Sequence Rule:
1. lock readiness packet
2. approve generator target
3. lock starter package
4. implement bounded code
5. checkpoint the result before wider expansion
