NEXUS Base V1 — Manifest Generator Scope

Purpose:
Define the exact scope of the current manifest generator lane.

Current Status:
- implemented at bounded scope
- manifest_generator.py exists
- manifest_generator.py v1 passed
- manifest_generator.py v1.1 passed

Generator Target:
Manifest generator only.

Current Implementation Objective:
Generate a read-only observational inventory of the governance kernel without modifying doctrine, registry, standards, or support records.

Included in Current Scope:
- read approved governance source files
- read doctrine identity registry
- classify doctrine vs non-doctrinal governance artifacts using approved source basis
- emit one generated manifest output to the proper observational lane
- preserve observational-only ceiling

Explicitly Excluded:
- doctrine modification
- registry modification
- active standard modification
- support record modification
- automatic promotion
- snapshot generation
- context export generation
- runtime invocation
- auto-repair or auto-fix behavior

Output Rule:
The generated manifest is observational only.
It does not become the source of canonical doctrine identity.

Current Ceiling:
- manifest generator only
- no broader generator bundle implied
- no approval authority implied

Delta Note:
- v1.1 adds generated_at timestamp metadata
- v1.1 does not widen authority, scope, or classification behavior
