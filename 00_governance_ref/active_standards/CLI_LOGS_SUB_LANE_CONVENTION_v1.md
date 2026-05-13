# CLI_LOGS_SUB_LANE_CONVENTION_v1

**Class:** Active Standard
**Status:** Active
**Tier:** T2 (governance-adjacent)
**Date:** 2026-05-13
**Governing ADR:** ADR-004 (Tri-System Knowledge Sync)
**Originating Cycle:** Commit `d65a65b` (2026-05-10) — war test run 67746111327 archive

---

## Purpose

Codify the `03_system_state/reports/cli_logs/` sub-lane schema and naming
convention. Establishes `cli_logs/` as the workspace's informational-logs
aggregate parent, with `ci/` as the dedicated sub-lane for continuous
integration runner archives. Defines container naming, internal file naming
references, and the boundary for future sibling lanes.

---

## Schema

```
03_system_state/reports/cli_logs/
├── ci/                          ← continuous integration runner archives
│   └── <date>_<workflow>_run_<run_id>/
│       ├── README.md            ← provenance and context
│       ├── RENAME_LOG.md        ← mechanical rename reference
│       └── (extracted log content per workflow structure)
└── (future siblings — see §Future Sibling Lanes below)
```

### Parent: `cli_logs/`

Informational-logs aggregate. Operator-created scaffolding. Holds all log-
archive types regardless of source. Never renamed once established.

### Sub-lane: `ci/`

Continuous integration runner archives only. Distinct from local-run reports
(which live as siblings under `03_system_state/reports/`, not inside
`cli_logs/`).

### Container: `<date>_<workflow>_run_<run_id>/`

Run-ID-keyed container. Naming components:

- **`<date>`** — ISO 8601 date of CI run origin (when the workflow executed on
  the CI platform). NOT the archive creation date in the workspace. The
  distinction is intentional and documented in each container's `README.md`.
- **`<workflow>`** — short workflow identifier (e.g., `war_test`).
- **`<run_id>`** — the CI platform's unique run identifier (e.g., GitHub
  Actions run ID).

Example: `2026-05-08_war_test_run_67746111327/`

---

## Naming Rules for Container Contents

Internal file and folder naming follows the **Strategy B convention**:

- Lowercase, underscored words
- Zero-padded numeric sort prefix (`01_`, `02_`, ..., `09_`, `10_`, `11_`)
- Version suffix dropped from filenames where the parent folder carries
  version identity (e.g., files inside `python_3_11/` do not repeat `3.11`)
- `system.txt` prefixed with `00_` to force sort-first within each folder

Strategy B is referenced here, not redefined. See its dedicated convention
record (or originating cycle `d65a65b` `RENAME_LOG.md`) for full rules.

---

## Required Container Artifacts

Every run-ID-keyed container must include:

1. **`README.md`** — provenance, source, verdict, naming-convention note,
   authority class, lifecycle status, cross-references
2. **`RENAME_LOG.md`** — mechanical original → renamed mapping for any
   files modified from the source archive

Both files use UTF-8 encoding. On PowerShell 5.1, `-Encoding utf8` produces
UTF-8 with BOM, which is acceptable for these markdown files.

---

## Idempotency Posture (per DEF-19)

Operations producing or modifying `cli_logs/ci/` containers declare
idempotency mode explicitly:

- **Directory creation:** force-flagged (`-Force` on `New-Item`)
- **Archive extraction:** force-flagged (`-Force` on `Expand-Archive`,
  zip-as-canonical-source)
- **Rename operations:** strict (no `-Force` on `Move-Item`; collision = halt)
- **README/RENAME_LOG authoring:** strict (`-NoClobber` on `Out-File`)

Rationale recorded per DEF-19 pattern at proposal time.

---

## Future Sibling Lanes

`cli_logs/` may host additional sub-lanes alongside `ci/`. The following are
**examples only**, not pre-approved commitments:

- `terminal_sessions/` — Claude Code or shell session captures
- `debug/` — debug-trace logs
- `claude_code/` — AI-tool session logs (if separated from terminal_sessions/)

Any new sibling lane requires operator decision before creation. This standard
does not pre-authorize them; it only acknowledges the schema can accommodate
them.

---

## Boundary

This convention applies to `03_system_state/reports/cli_logs/` only.

It does **not** extend to:
- Other directories under `03_system_state/reports/` (e.g.,
  `war_test_report.json`, `WAR_TEST_REPORT.md` — these are siblings of
  `cli_logs/`, not inside it)
- Doctrine, active-standards, or support-record locations
- Runtime or memory layers

---

## Cross-References

- **Originating cycle:** Commit `d65a65b` (2026-05-10)
- **Pattern protocol:** DEF-19 (per-action idempotency-mode declaration)
- **Naming convention reference:** Strategy B (lowercase, underscored,
  zero-padded sort prefix)
- **Governing ADR:** ADR-004 (Tri-System Knowledge Sync — workspace
  organization for cross-system artifacts)
- **Live example:**
  `03_system_state/reports/cli_logs/ci/2026-05-08_war_test_run_67746111327/`

---

## Authority Class

- **Source class:** evidence (derived from a completed, committed cycle)
- **Authority class:** active standard (operationally validated, not doctrine)
- **Lifecycle status:** active
- **Promotion path:** may be cited by future standards; promotion to doctrine
  requires operator decision and Doctrine Promotion Protocol
