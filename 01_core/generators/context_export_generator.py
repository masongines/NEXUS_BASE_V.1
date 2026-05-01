#!/usr/bin/env python3
from __future__ import annotations

"""
NEXUS Base V1 — Context Export Generator v1

Ceiling:
- doctrine identity comes from DOCTRINE_IDENTITY_REGISTRY.md
- generated context export is observational and orientation-only
- no mutation of doctrine, registry, standards, support records, manifest, or snapshot
- no PRE_DRAFT or LEGACY scanning
- no recommendation, readiness, approval, promotion, or runtime behavior
- no prior context export file used as an input source
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS")

REGISTRY_PATH = ROOT / "00_governance_ref" / "support_records" / "DOCTRINE_IDENTITY_REGISTRY.md"
DOCTRINE_DIR = ROOT / "00_governance_ref" / "doctrine"
MANIFEST_PATH = ROOT / "03_system_state" / "manifests" / "KERNEL_MANIFEST.json"
SNAPSHOT_PATH = ROOT / "03_system_state" / "snapshots" / "SYSTEM_STATE_SNAPSHOT_CURRENT.md"

PLACEMENT_MAP_PATH = ROOT / "06_operator" / "plans" / "NEXUS_BASE_V1_FILE_PLACEMENT_AND_ROLE_MAP_v2.md"
MIGRATION_REGISTER_PATH = ROOT / "06_operator" / "plans" / "NEXUS_BASE_V1_MIGRATION_REGISTER_v2.md"
WORKBOARD_PATH = ROOT / "06_operator" / "checkpoints" / "NEXUS_BASE_V1_FOUNDATION_COMPLETION_WORKBOARD_v2.md"

CHECKPOINTS_DIR = ROOT / "06_operator" / "checkpoints"
OUTPUT_PATH = ROOT / "03_system_state" / "context_exports" / "NEXUS_CONTEXT_EXPORT.md"


def fail(msg: str, code: int = 2) -> int:
    print("NEXUS Base V1 — Context Export Generator v1")
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


def count_checkpoint_files(checkpoints_dir: Path) -> int:
    if not checkpoints_dir.exists() or not checkpoints_dir.is_dir():
        return 0
    return sum(1 for p in checkpoints_dir.iterdir() if p.is_file() and p.suffix.lower() == ".md")


def build_context_export_text(
    generated_at: str,
    doctrine_count: int,
    active_standard_count: int,
    support_record_count: int,
    checkpoint_count: int,
) -> str:
    lines: list[str] = [
        "# NEXUS Context Export v1",
        "",
        f"Generated At: {generated_at}",
        "Mode: Read-Only Source Scan + Single Output Write",
        "Status: OBSERVATIONAL",
        "",
        "## Governance Orientation",
        f"- canonical doctrine count: {doctrine_count}",
        "- source: DOCTRINE_IDENTITY_REGISTRY.md",
        "- note: doctrine identity remains sourced from the registry",
        "",
        "## Current Inventory Support",
        f"- active standard count: {active_standard_count}",
        f"- support record count: {support_record_count}",
        "- source: KERNEL_MANIFEST.json",
        "- note: manifest used as inventory support only",
        "",
        "## Current State Support",
        "- snapshot present: yes",
        "- source: SYSTEM_STATE_SNAPSHOT_CURRENT.md",
        "- note: snapshot used as observational support only",
        "",
        "## Current Planning Support",
        "- placement map present: yes",
        "- migration register present: yes",
        "- foundation workboard present: yes",
        "",
        "## Current Checkpoint Support",
        f"- checkpoint artifacts present: {'yes' if checkpoint_count > 0 else 'no'}",
        f"- checkpoint artifact count: {checkpoint_count}",
        "- note: checkpoints support current orientation only and do not replace governance truth",
        "",
        "## Uncertainty / Boundary Notes",
        "- output is observational and orientation-only",
        "- no approval, readiness, or promotion implied",
        "- no memory authority implied",
        "- lower surfaces did not replace stronger sources",
        "- prior context export file was not used as an input source",
    ]

    if checkpoint_count == 0:
        lines.append("- checkpoint support is absent; context export remains bounded to available stronger sources")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    print("NEXUS Base V1 — Context Export Generator v1")
    print("Mode: Read-Only Source Scan + Single Output Write")
    print("")

    required_files = [
        REGISTRY_PATH,
        MANIFEST_PATH,
        SNAPSHOT_PATH,
        PLACEMENT_MAP_PATH,
        MIGRATION_REGISTER_PATH,
        WORKBOARD_PATH,
    ]
    required_dirs = [
        DOCTRINE_DIR,
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

    checkpoint_count = count_checkpoint_files(CHECKPOINTS_DIR)

    generated_at = datetime.now().isoformat(timespec="seconds")

    context_export_text = build_context_export_text(
        generated_at=generated_at,
        doctrine_count=len(doctrine_files),
        active_standard_count=active_standard_count,
        support_record_count=support_record_count,
        checkpoint_count=checkpoint_count,
    )

    try:
        OUTPUT_PATH.write_text(context_export_text, encoding="utf-8")
    except Exception as e:
        return fail(f"failed to write context export output: {e}")

    result = "PASS" if checkpoint_count > 0 else "WATCHLIST"

    print("Core Sources:")
    print(f"- PASS: registry found at {REGISTRY_PATH}")
    print(f"- PASS: manifest parsed at {MANIFEST_PATH}")
    print(f"- PASS: snapshot support found at {SNAPSHOT_PATH}")
    print(f"- PASS: placement map found at {PLACEMENT_MAP_PATH}")
    print(f"- PASS: migration register found at {MIGRATION_REGISTER_PATH}")
    print(f"- PASS: foundation workboard found at {WORKBOARD_PATH}")
    print("")

    print("Classification:")
    print(f"- PASS: extracted {len(doctrine_files)} doctrine filenames from registry")
    print(f"- PASS: {len(doctrine_files)} doctrine files verified in doctrine lane")
    print(f"- PASS: active standard count sourced from manifest = {active_standard_count}")
    print(f"- PASS: support record count sourced from manifest = {support_record_count}")
    print("")

    print("Support:")
    if checkpoint_count > 0:
        print(f"- PASS: checkpoint artifacts present in {CHECKPOINTS_DIR} (count = {checkpoint_count})")
    else:
        print(f"- WATCHLIST: no checkpoint artifacts found in {CHECKPOINTS_DIR}")
    print("")

    print("Output:")
    print(f"- PASS: context export written to {OUTPUT_PATH}")
    print(f"- PASS: generated_at set to {generated_at}")
    print("")

    print("Boundary:")
    print("- PASS: doctrine identity remained sourced from registry")
    print("- PASS: output marked observational and orientation-only")
    print("- PASS: prior context export file was not used as an input source")
    print("")

    print(f"Result: {result}")
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())