from pathlib import Path
from datetime import datetime, UTC
import shutil

ROOT = Path(".").resolve()

TARGETS = [
    ROOT / "01_core" / "execution" / "executor.py",
    ROOT / "01_core" / "execution" / "security" / "quarantine_handler.py",
    ROOT / "bootstrap_runtime.py",
    ROOT / "nexus_phase_bcd_bootstrap.py",
    ROOT / "nexus_security_wave2_bootstrap.py",
    ROOT / "nexus_security_wave3_bootstrap.py",
]

REPLACEMENTS = [
    # Timezone-aware UTC replacement
    ("from datetime import datetime, UTC, UTC", "from datetime import datetime, UTC"),
    ("from datetime import datetime, UTC", "from datetime import datetime, UTC"),
    ("from datetime import datetime", "from datetime import datetime, UTC"),
    ("datetime.utcnow().isoformat()", "datetime.now(UTC).isoformat()"),

    # Windows-safe terminal output
    ("🚨 THREAT DETECTED — ACTION QUARANTINED", "THREAT DETECTED - ACTION QUARANTINED"),
    ("🚨 THREAT DETECTED - ACTION QUARANTINED", "THREAT DETECTED - ACTION QUARANTINED"),
    ("⚡ TRUSTED AUTO-APPROVAL (T3)", "TRUSTED AUTO-APPROVAL (T3)"),
]

def backup_file(path: Path) -> Path:
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    backup = path.with_suffix(path.suffix + f".bak_{timestamp}")
    shutil.copy2(path, backup)
    return backup

def patch_file(path: Path) -> dict:
    result = {
        "file": str(path),
        "status": "SKIPPED",
        "backup": None,
        "changes": 0,
        "reason": ""
    }

    if not path.exists():
        result["reason"] = "file missing"
        return result

    original = path.read_text(encoding="utf-8", errors="ignore")
    updated = original

    for old, new in REPLACEMENTS:
        if old in updated:
            count = updated.count(old)
            updated = updated.replace(old, new)
            result["changes"] += count

    # Clean accidental duplicate imports caused by repeated patching
    updated = updated.replace(
        "from datetime import datetime, UTC, UTC",
        "from datetime import datetime, UTC"
    )

    if updated == original:
        result["reason"] = "no matching warning patterns found"
        return result

    backup = backup_file(path)
    path.write_text(updated, encoding="utf-8")

    result["status"] = "PATCHED"
    result["backup"] = str(backup)
    return result

def main():
    print("\n=== NEXUS WAR TEST WARNING FIX START ===\n")
    print(f"Root: {ROOT}\n")

    results = [patch_file(path) for path in TARGETS]

    patched = 0
    skipped = 0

    for r in results:
        print(f"{r['status']} :: {r['file']}")
        if r["backup"]:
            print(f"  backup: {r['backup']}")
        if r["changes"]:
            print(f"  changes: {r['changes']}")
        if r["reason"]:
            print(f"  reason: {r['reason']}")
        print()

        if r["status"] == "PATCHED":
            patched += 1
        else:
            skipped += 1

    print("=== SUMMARY ===")
    print(f"PATCHED: {patched}")
    print(f"SKIPPED: {skipped}")

    print("\nNext command:")
    print("python nexus_war_test.py")

if __name__ == "__main__":
    main()