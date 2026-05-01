#!/usr/bin/env python3
from __future__ import annotations

"""
NEXUS Base V1 — Snapshot Generator v1

Ceiling:
- doctrine identity comes from DOCTRINE_IDENTITY_REGISTRY.md
- generated snapshot is observational only
- no mutation of doctrine, registry, standards, support records, or manifest
- no PRE_DRAFT or LEGACY scanning
- no context export generation
- no recommendation, approval, promotion, or runtime behavior
- no prior snapshot file used as an input source
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS")

SNAPSHOT_SPEC_PATH = ROOT / "00_governance_ref" / "active_standards" / "SNAPSHOT_GENERATOR_SPEC_v1.md"
SNAPSHOT_PROTOCOL_PATH = ROOT / "00_governance_ref" / "doctrine" / "SYSTEM_STATE_SNAPSHOT_PROTOCOL.md"
REGISTRY_PATH = ROOT / "00_governance_ref" / "support_records" / "DOCTRINE_IDENTITY_REGISTRY.md"
MANIFEST_PATH = ROOT / "03_system_state" / "manifests" / "KERNEL_MANIFEST.json"
CONTEXT_EXPORT_PATH = ROOT / "03_system_state" / "context_exports" / "NEXUS_CONTEXT_EXPORT.md"
OUTPUT_PATH = ROOT / "03_system_state" / "snapshots" / "SYSTEM_STATE_SNAPSHOT_CURRENT.md"

DOCTRINE_DIR = ROOT / "00_governance_ref" / "doctrine"
ACTIVE_STANDARDS_DIR = ROOT / "00_governance_ref" / "active_standards"
SUPPORT_RECORDS_DIR = ROOT / "00_governance_ref" / "support_records"


def fail(msg: str, code: int = 2) -> int:
    print("NEXUS Base V1 — Snapshot Generator v1")
    print("Mode: Read-Only Source Scan + Single Output Write")
    print("Result: FAIL")
    print("")
    print(f"Failure: {msg}")
    return code


def extract_registry_doctrine_filenames(registry_path: Path) -> list[str]:
    text = registry_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    in_table = False
    filenames: list[str] = []

    for line in lines:
        stripped = line.strip()

        if "Canonical Doctrine Identity Table" in stripped:
            in_table = True
            continue

        if not in_table:
            continue

        if not stripped:
            if filenames:
                break
            continue

        if not stripped.startswith("|"):
            if filenames:
                break
            continue

        if "Canonical File" in stripped or "---" in stripped:
            continue

        parts = [p.strip() for p in stripped.strip("|").split("|")]
        if parts and parts[0].endswith(".md"):
            filenames.append(parts[0])

    return filenames


def load_manifest(manifest_path: Path) -> dict:
    with manifest_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_snapshot_text(
    generated_at: str,
    doctrine_count: int,
    active_standard_count: int,
    support_record_count: int,
    context_export_present: bool,
) -> str:
    lines: list[str] = [
        "# NEXUS Base V1 — System State Snapshot v1",
        "",
        f"Generated At: {generated_at}",
        "Mode: Read-Only Source Scan + Single Output Write",
        "Status: OBSERVATIONAL",
        "",
        "## Doctrine Inventory",
        f"- canonical doctrine count: {doctrine_count}",
        "- source: DOCTRINE_IDENTITY_REGISTRY.md",
        "- note: registry remains stronger than generated surfaces",
        "",
        "## Support Counts",
        f"- active standard count: {active_standard_count}",
        f"- support record count: {support_record_count}",
        "- source: KERNEL_MANIFEST.json",
        "- note: manifest used as inventory support only",
        "",
        "## Observational Support Presence",
        "- manifest present: yes",
        f"- context export present: {'yes' if context_export_present else 'no'}",
        "",
        "## Uncertainty / Boundary Notes",
        "- output is observational only",
        "- no approval or promotion implied",
        "- lower surfaces did not replace stronger sources",
    ]

    if not context_export_present:
        lines.append("- context export support is absent; snapshot remains bounded to available stronger sources")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    print("NEXUS Base V1 — Snapshot Generator v1")
    print("Mode: Read-Only Source Scan + Single Output Write")
    print("")

    required_files = [
        SNAPSHOT_SPEC_PATH,
        SNAPSHOT_PROTOCOL_PATH,
        REGISTRY_PATH,
        MANIFEST_PATH,
    ]
    required_dirs = [
        DOCTRINE_DIR,
        ACTIVE_STANDARDS_DIR,
        SUPPORT_RECORDS_DIR,
        OUTPUT_PATH.parent,
    ]

    for d in required_dirs:
        if not d.exists() or not d.is_dir():
            return fail(f"required directory missing: {d}")

    for f in required_files:
        if not f.exists() or not f.is_file():
            return fail(f"required file missing: {f}")

    try:
        doctrine_files = extract_registry_doctrine_filenames(REGISTRY_PATH)
    except Exception as e:
        return fail(f"registry parse failed: {e}")

    if not doctrine_files:
        return fail("registry parse produced no doctrine filenames")

    missing_doctrine = [name for name in doctrine_files if not (DOCTRINE_DIR / name).exists()]
    if missing_doctrine:
        return fail("missing doctrine files listed in registry: " + ", ".join(missing_doctrine))

    try:
        manifest = load_manifest(MANIFEST_PATH)
    except Exception as e:
        return fail(f"manifest parse failed: {e}")

    counts = manifest.get("counts")
    if not isinstance(counts, dict):
        return fail("manifest counts block missing or malformed")

    active_standard_count = counts.get("active_standard_count")
    support_record_count = counts.get("support_record_count")

    if not isinstance(active_standard_count, int):
        return fail("manifest active_standard_count missing or malformed")

    if not isinstance(support_record_count, int):
        return fail("manifest support_record_count missing or malformed")

    context_export_present = CONTEXT_EXPORT_PATH.exists() and CONTEXT_EXPORT_PATH.is_file()

    generated_at = datetime.now().isoformat(timespec="seconds")

    snapshot_text = build_snapshot_text(
        generated_at=generated_at,
        doctrine_count=len(doctrine_files),
        active_standard_count=active_standard_count,
        support_record_count=support_record_count,
        context_export_present=context_export_present,
    )

    try:
        OUTPUT_PATH.write_text(snapshot_text, encoding="utf-8")
    except Exception as e:
        return fail(f"failed to write snapshot output: {e}")

    result = "PASS" if context_export_present else "WATCHLIST"

    print("Core Sources:")
    print(f"- PASS: snapshot spec found at {SNAPSHOT_SPEC_PATH}")
    print(f"- PASS: snapshot protocol found at {SNAPSHOT_PROTOCOL_PATH}")
    print(f"- PASS: registry found at {REGISTRY_PATH}")
    print(f"- PASS: manifest parsed at {MANIFEST_PATH}")
    print("")

    print("Classification:")
    print(f"- PASS: extracted {len(doctrine_files)} doctrine filenames from registry")
    print(f"- PASS: {len(doctrine_files)} doctrine files verified in doctrine lane")
    print(f"- PASS: active standard count sourced from manifest = {active_standard_count}")
    print(f"- PASS: support record count sourced from manifest = {support_record_count}")
    print("")

    print("Support:")
    if context_export_present:
        print(f"- PASS: context export present at {CONTEXT_EXPORT_PATH}")
    else:
        print(f"- WATCHLIST: context export missing at {CONTEXT_EXPORT_PATH}")
    print("")

    print("Output:")
    print(f"- PASS: snapshot written to {OUTPUT_PATH}")
    print(f"- PASS: generated_at set to {generated_at}")
    print("")

    print("Boundary:")
    print("- PASS: doctrine identity remained sourced from registry")
    print("- PASS: output marked observational only")
    print("- PASS: prior snapshot file was not used as an input source")
    print("")

    print(f"Result: {result}")
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())