#!/usr/bin/env python3
from __future__ import annotations

"""
NEXUS Base V1 — Preflight Check v1.1

Ceiling:
- read-only only
- no mutation
- no approval authority
- no runtime invocation
- no migration actions
- no PRE_DRAFT or LEGACY scanning

Interpretation rules:
- doctrine identity comes from DOCTRINE_IDENTITY_REGISTRY.md
- KERNEL_MANIFEST.json is support only, not canonical doctrine identity
- observational surfaces remain support only
"""

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(r"C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS")


@dataclass
class CheckResult:
    section: str
    level: str  # PASS / WATCHLIST / INTERVENTION_REQUIRED
    item: str
    detail: str


REQUIRED_FOLDERS = [
    Path("00_governance_ref/doctrine"),
    Path("00_governance_ref/active_standards"),
    Path("00_governance_ref/support_records"),
    Path("01_core/control"),
    Path("03_system_state/manifests"),
    Path("03_system_state/snapshots"),
    Path("03_system_state/context_exports"),
]

REQUIRED_FILES = [
    Path("00_governance_ref/support_records/DOCTRINE_IDENTITY_REGISTRY.md"),
    Path("00_governance_ref/support_records/GOVERNANCE_KERNEL_GUARDIAN.md"),
    Path("00_governance_ref/support_records/KERNEL_MANIFEST.json"),
    Path("00_governance_ref/doctrine/PRIME_AXIOM.md"),
    Path("00_governance_ref/doctrine/ESCALATION_TIERING_PROTOCOL.md"),
    Path("00_governance_ref/doctrine/FACTUAL_VALIDATION_PROTOCOL.md"),
    Path("00_governance_ref/doctrine/ENTROPY_MONITORING_SYSTEM.md"),
    Path("00_governance_ref/doctrine/SYSTEM_STATE_SNAPSHOT_PROTOCOL.md"),
    Path("00_governance_ref/active_standards/GUARDIAN_AUTOMATION_SPEC_v1.md"),
    Path("00_governance_ref/active_standards/NEXUS_AUTHORITY_AND_BOUNDARY_SAFEGUARDS_v1.md"),
]

OPTIONAL_SUPPORT_FILES = [
    Path("03_system_state/manifests/KERNEL_MANIFEST.json"),
    Path("03_system_state/snapshots/SYSTEM_STATE_SNAPSHOT_CURRENT.md"),
    Path("03_system_state/context_exports/NEXUS_CONTEXT_EXPORT.md"),
]

CONTROL_PACKAGE_FILES = [
    Path("01_core/control/README_CONTROL.txt"),
    Path("01_core/control/README_PREFLIGHT_SCOPE.txt"),
    Path("01_core/control/PREFLIGHT_SOURCE_MAP.txt"),
    Path("01_core/control/PREFLIGHT_TEST_CHECKLIST.txt"),
]

OPERATOR_CONTROL_FILES = [
    Path("06_operator/plans/NEXUS_BASE_V1_FILE_PLACEMENT_AND_ROLE_MAP_v2.md"),
    Path("06_operator/plans/NEXUS_BASE_V1_MIGRATION_REGISTER_v2.md"),
    Path("06_operator/checkpoints/NEXUS_BASE_V1_FOUNDATION_COMPLETION_WORKBOARD_v2.md"),
    Path("07_reference_material/handoff_material/NEXUS_MEMBER_MASTER_SYNC_BOOTSTRAP_v1.md"),
]

ALLOWED_FINAL_STATUSES = ("PASS", "WATCHLIST", "INTERVENTION_REQUIRED")


def rel(p: Path) -> str:
    return p.as_posix()


def add(results: list[CheckResult], section: str, level: str, item: str, detail: str) -> None:
    results.append(CheckResult(section=section, level=level, item=item, detail=detail))


def check_required_folders(root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    for folder in REQUIRED_FOLDERS:
        full = root / folder
        if full.exists() and full.is_dir():
            add(results, "Folder Checks", "PASS", rel(folder), "folder present")
        else:
            add(results, "Folder Checks", "INTERVENTION_REQUIRED", rel(folder), "required folder missing")
    return results


def check_required_files(root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    for file in REQUIRED_FILES:
        full = root / file
        if full.exists() and full.is_file():
            add(results, "Required Source Checks", "PASS", rel(file), "required file present")
        else:
            add(results, "Required Source Checks", "INTERVENTION_REQUIRED", rel(file), "required file missing")

    for file in OPTIONAL_SUPPORT_FILES:
        full = root / file
        if full.exists() and full.is_file():
            add(results, "Required Source Checks", "PASS", rel(file), "optional observational support present")
        else:
            add(results, "Required Source Checks", "WATCHLIST", rel(file), "optional observational support missing")
    return results


def check_control_package_files(root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    for file in CONTROL_PACKAGE_FILES:
        full = root / file
        if full.exists() and full.is_file():
            add(results, "Control Package Checks", "PASS", rel(file), "control package file present")
        else:
            add(results, "Control Package Checks", "INTERVENTION_REQUIRED", rel(file), "required control package file missing")
    return results


def check_operator_control_files(root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    for file in OPERATOR_CONTROL_FILES:
        full = root / file
        if full.exists() and full.is_file():
            add(results, "Operator Control Surface Checks", "PASS", rel(file), "operator control surface present")
        else:
            add(results, "Operator Control Surface Checks", "INTERVENTION_REQUIRED", rel(file), "required operator control surface missing")
    return results


def extract_registry_doctrine_filenames(registry_path: Path) -> list[str]:
    """
    Parse the 'Canonical Doctrine Identity Table' rows.
    Pull the first markdown-table column as the canonical filename.
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


def check_doctrine_presence(root: Path, expected_files: Iterable[str]) -> list[CheckResult]:
    results: list[CheckResult] = []
    doctrine_dir = root / "00_governance_ref" / "doctrine"

    for filename in expected_files:
        full = doctrine_dir / filename
        if full.exists() and full.is_file():
            add(results, "Doctrine Presence Checks", "PASS", filename, "registry-listed doctrine file present")
        else:
            add(results, "Doctrine Presence Checks", "INTERVENTION_REQUIRED", filename, "registry-listed doctrine file missing")
    return results


def load_manifest(manifest_path: Path) -> dict:
    with manifest_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def check_manifest(root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    manifest_path = root / "00_governance_ref" / "support_records" / "KERNEL_MANIFEST.json"

    if not manifest_path.exists():
        add(results, "Manifest Checks", "INTERVENTION_REQUIRED", rel(manifest_path.relative_to(root)), "manifest missing")
        return results

    try:
        manifest = load_manifest(manifest_path)
        add(results, "Manifest Checks", "PASS", rel(manifest_path.relative_to(root)), "manifest JSON parsed successfully")
    except Exception as e:
        add(results, "Manifest Checks", "INTERVENTION_REQUIRED", rel(manifest_path.relative_to(root)), f"manifest JSON parse failed: {e}")
        return results

    if "doctrine_files" in manifest and isinstance(manifest["doctrine_files"], list):
        add(results, "Manifest Checks", "PASS", "doctrine_files", "manifest doctrine_files list present")
    else:
        add(results, "Manifest Checks", "WATCHLIST", "doctrine_files", "manifest doctrine_files list missing or malformed")

    return results


def check_manifest_coherence(expected_registry_files: list[str], root: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    manifest_path = root / "00_governance_ref" / "support_records" / "KERNEL_MANIFEST.json"

    if not manifest_path.exists():
        add(results, "Coherence Notes", "INTERVENTION_REQUIRED", "registry_vs_manifest", "manifest unavailable for coherence support check")
        return results

    try:
        manifest = load_manifest(manifest_path)
    except Exception as e:
        add(results, "Coherence Notes", "INTERVENTION_REQUIRED", "registry_vs_manifest", f"manifest unreadable for coherence support check: {e}")
        return results

    manifest_files = manifest.get("doctrine_files")
    if not isinstance(manifest_files, list):
        add(results, "Coherence Notes", "WATCHLIST", "registry_vs_manifest", "manifest doctrine_files unavailable; registry remains stronger source")
        return results

    reg_set = set(expected_registry_files)
    man_set = set(str(x) for x in manifest_files)

    if reg_set == man_set:
        add(results, "Coherence Notes", "PASS", "registry_vs_manifest", "registry and manifest doctrine file lists align")
    else:
        missing_in_manifest = sorted(reg_set - man_set)
        extra_in_manifest = sorted(man_set - reg_set)
        detail_parts = []
        if missing_in_manifest:
            detail_parts.append(f"missing in manifest: {', '.join(missing_in_manifest)}")
        if extra_in_manifest:
            detail_parts.append(f"extra in manifest: {', '.join(extra_in_manifest)}")
        detail = "; ".join(detail_parts) if detail_parts else "lists differ"
        add(results, "Coherence Notes", "WATCHLIST", "registry_vs_manifest", f"{detail}. Registry remains stronger source")
    return results


def boundary_notes() -> list[CheckResult]:
    return [
        CheckResult(
            section="Boundary Notes",
            level="PASS",
            item="output_ceiling",
            detail="output is analytical only; no approval, mutation, or authorization performed",
        ),
        CheckResult(
            section="Boundary Notes",
            level="PASS",
            item="source_precedence",
            detail="registry remains stronger than manifest for doctrine identity",
        ),
    ]


def summarize_status(results: Iterable[CheckResult]) -> str:
    levels = [r.level for r in results]
    if "INTERVENTION_REQUIRED" in levels:
        return "INTERVENTION_REQUIRED"
    if "WATCHLIST" in levels:
        return "WATCHLIST"
    return "PASS"


def print_section(title: str, results: list[CheckResult]) -> None:
    print(f"{title}:")
    for r in results:
        print(f"- {r.level}: {r.item} — {r.detail}")
    print("")


def print_report(results: list[CheckResult], final_status: str) -> None:
    print("NEXUS Base V1 — Preflight Check v1.1")
    print("Mode: Read-Only")
    print(f"Result: {final_status}")
    print("")

    sections = [
        "Folder Checks",
        "Required Source Checks",
        "Doctrine Presence Checks",
        "Manifest Checks",
        "Coherence Notes",
        "Control Package Checks",
        "Operator Control Surface Checks",
        "Boundary Notes",
    ]

    for section in sections:
        section_results = [r for r in results if r.section == section]
        if section_results:
            print_section(section, section_results)


def main() -> int:
    results: list[CheckResult] = []

    results.extend(check_required_folders(ROOT))
    results.extend(check_required_files(ROOT))

    registry_path = ROOT / "00_governance_ref" / "support_records" / "DOCTRINE_IDENTITY_REGISTRY.md"
    expected_registry_files: list[str] = []

    if registry_path.exists():
        try:
            expected_registry_files = extract_registry_doctrine_filenames(registry_path)
            if expected_registry_files:
                add(results, "Doctrine Presence Checks", "PASS", "registry_parse", f"extracted {len(expected_registry_files)} doctrine filenames from registry")
                results.extend(check_doctrine_presence(ROOT, expected_registry_files))
            else:
                add(results, "Doctrine Presence Checks", "INTERVENTION_REQUIRED", "registry_parse", "could not extract doctrine filenames from registry")
        except Exception as e:
            add(results, "Doctrine Presence Checks", "INTERVENTION_REQUIRED", "registry_parse", f"registry parse failed: {e}")
    else:
        add(results, "Doctrine Presence Checks", "INTERVENTION_REQUIRED", "registry_parse", "registry missing")

    results.extend(check_manifest(ROOT))

    if expected_registry_files:
        results.extend(check_manifest_coherence(expected_registry_files, ROOT))
    else:
        add(results, "Coherence Notes", "WATCHLIST", "registry_vs_manifest", "coherence support check skipped because registry extraction failed")

    results.extend(check_control_package_files(ROOT))
    results.extend(check_operator_control_files(ROOT))

    results.extend(boundary_notes())

    final_status = summarize_status(results)
    if final_status not in ALLOWED_FINAL_STATUSES:
        print("[FAIL] Invalid final status computed.")
        return 2

    print_report(results, final_status)

    if final_status == "PASS":
        return 0
    if final_status == "WATCHLIST":
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())