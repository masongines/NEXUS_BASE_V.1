#!/usr/bin/env python3
from __future__ import annotations

"""
NEXUS Base V1 — Manifest Generator v1.1

Ceiling:
- doctrine identity comes from DOCTRINE_IDENTITY_REGISTRY.md
- generated manifest is observational only
- no mutation of doctrine, registry, standards, or support records
- no PRE_DRAFT or LEGACY scanning
- no snapshot or context export generation
- no approval or promotion behavior
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS")

REGISTRY_PATH = ROOT / "00_governance_ref" / "support_records" / "DOCTRINE_IDENTITY_REGISTRY.md"
DOCTRINE_DIR = ROOT / "00_governance_ref" / "doctrine"
ACTIVE_STANDARDS_DIR = ROOT / "00_governance_ref" / "active_standards"
SUPPORT_RECORDS_DIR = ROOT / "00_governance_ref" / "support_records"
OUTPUT_PATH = ROOT / "03_system_state" / "manifests" / "KERNEL_MANIFEST.json"


def extract_registry_doctrine_filenames(registry_path: Path) -> list[str]:
    """
    Parse the Canonical Doctrine Identity Table and return canonical filenames.
    """
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


def collect_file_names(folder: Path, allowed_suffixes: tuple[str, ...] | None = None) -> list[str]:
    names: list[str] = []
    for p in sorted(folder.iterdir(), key=lambda x: x.name.lower()):
        if not p.is_file():
            continue
        if allowed_suffixes is not None and p.suffix.lower() not in allowed_suffixes:
            continue
        names.append(p.name)
    return names


def fail(msg: str, code: int = 2) -> int:
    print("NEXUS Base V1 — Manifest Generator v1.1")
    print("Mode: Read-Only Source Scan + Single Output Write")
    print("Result: FAIL")
    print("")
    print(f"Failure: {msg}")
    return code


def main() -> int:
    print("NEXUS Base V1 — Manifest Generator v1.1")
    print("Mode: Read-Only Source Scan + Single Output Write")
    print("")

    required_dirs = [DOCTRINE_DIR, ACTIVE_STANDARDS_DIR, SUPPORT_RECORDS_DIR, OUTPUT_PATH.parent]
    for d in required_dirs:
        if not d.exists() or not d.is_dir():
            return fail(f"required directory missing: {d}")

    if not REGISTRY_PATH.exists() or not REGISTRY_PATH.is_file():
        return fail(f"registry missing: {REGISTRY_PATH}")

    try:
        doctrine_files = extract_registry_doctrine_filenames(REGISTRY_PATH)
    except Exception as e:
        return fail(f"registry parse failed: {e}")

    if not doctrine_files:
        return fail("registry parse produced no doctrine filenames")

    missing_doctrine = [name for name in doctrine_files if not (DOCTRINE_DIR / name).exists()]
    if missing_doctrine:
        return fail("missing doctrine files listed in registry: " + ", ".join(missing_doctrine))

    active_standard_files = collect_file_names(ACTIVE_STANDARDS_DIR, allowed_suffixes=(".md",))
    support_record_files = collect_file_names(SUPPORT_RECORDS_DIR, allowed_suffixes=(".md", ".json"))

    generated_at = datetime.now().isoformat(timespec="seconds")

    manifest = {
        "schema_version": "1.0",
        "artifact_kind": "generated_inventory",
        "kernel_name": "NEXUS Governance Kernel",
        "generated_at": generated_at,
        "inventory_basis": {
            "doctrine_identity_source": "DOCTRINE_IDENTITY_REGISTRY.md",
            "artifact_scan_root": "00_governance_ref/",
            "count_policy": "generated_only",
            "classification_policy": "registry_and_folder_derived",
        },
        "counts": {
            "canonical_doctrine_count": len(doctrine_files),
            "active_standard_count": len(active_standard_files),
            "support_record_count": len(support_record_files),
        },
        "doctrine_files": doctrine_files,
        "active_standard_files": active_standard_files,
        "support_record_files": support_record_files,
        "warnings": [
            "This manifest is generated inventory and is not the source of canonical doctrine identity.",
            "Canonical doctrine identity is governed exclusively by DOCTRINE_IDENTITY_REGISTRY.md.",
            "Counts must not be manually edited.",
        ],
    }

    try:
        OUTPUT_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    except Exception as e:
        return fail(f"failed to write manifest output: {e}")

    print("Registry:")
    print(f"- PASS: registry found at {REGISTRY_PATH}")
    print(f"- PASS: extracted {len(doctrine_files)} doctrine filenames")
    print("")

    print("Folders:")
    print("- PASS: doctrine folder present")
    print("- PASS: active standards folder present")
    print("- PASS: support records folder present")
    print("")

    print("Classification:")
    print(f"- PASS: {len(doctrine_files)} doctrine files counted")
    print(f"- PASS: {len(active_standard_files)} active standard files counted")
    print(f"- PASS: {len(support_record_files)} support record files counted")
    print("")

    print("Output:")
    print(f"- PASS: manifest written to {OUTPUT_PATH}")
    print(f"- PASS: generated_at set to {generated_at}")
    print("")

    print("Boundary:")
    print("- PASS: doctrine identity sourced from registry")
    print("- PASS: output marked observational only")
    print("")

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())