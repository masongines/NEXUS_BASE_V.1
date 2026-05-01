NEXUS Base V1 — Snapshot Generator Scope

Purpose:
Define the exact scope of the current snapshot generator lane.

Current Status:
- implemented at bounded scope
- snapshot_generator.py exists
- snapshot_generator.py v1 passed

Generator Target:
Snapshot generator only.

Current Implementation Objective:
Generate a read-only current-state observational snapshot from approved Base V1 sources and write one output to the approved snapshot path.

Included in Current Scope:
- read approved governance sources
- read approved observational support sources
- assemble a bounded current-state snapshot
- preserve source precedence
- preserve uncertainty visibility
- write one snapshot output to the approved snapshot lane

Explicitly Excluded:
- doctrine modification
- registry modification
- manifest modification
- active standard modification
- support record modification
- automatic promotion
- automatic trigger execution
- historical trend engine behavior
- context export generation
- runtime invocation
- auto-repair or auto-fix behavior

Output Rule:
The generated snapshot is observational only.
It does not become governance authority, approval authority, or canonical truth.

Current Ceiling:
- snapshot generator only
- no broader reporting engine implied
- no approval authority implied
- no prior snapshot file used as an input source
