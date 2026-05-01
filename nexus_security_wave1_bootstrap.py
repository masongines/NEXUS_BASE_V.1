from pathlib import Path
import json

ROOT = Path(".").resolve()

CREATED = []
SKIPPED = []
FAILED = []

def log_created(p): CREATED.append(str(p))
def log_skipped(p): SKIPPED.append(str(p))
def log_failed(p, e): FAILED.append(f"{p} -> {e}")

# -----------------------------
# SAFE WRITE
# -----------------------------
def write_file(path, content):
    try:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(content, dict):
                path.write_text(json.dumps(content, indent=2), encoding="utf-8")
            else:
                path.write_text(content, encoding="utf-8")
            log_created(path)
        else:
            log_skipped(path)
    except Exception as e:
        log_failed(path, e)

# -----------------------------
# WAVE 1 BUILDER
# -----------------------------
def build_wave1():

    # 1. Threat Model
    write_file(
        ROOT / "00_governance_ref/security/threat_model_v1.md",
        """# NEXUS THREAT MODEL v1

## Threat Tiers

### Tier 1 — Benign
- malformed input
- no malicious intent

Action:
- log only

---

### Tier 2 — Suspicious
- prompt injection
- instruction override
- hidden directives

Action:
- quarantine
- operator review

---

### Tier 3 — Malicious
- data exfiltration attempt
- unauthorized execution request

Action:
- immediate block
- full audit

---

## Core Rule

No threat may trigger execution without operator approval.
"""
    )

    # 2. Security Log Schema
    write_file(
        ROOT / "02_config/security_log_schema.json",
        {
            "timestamp": "string",
            "input": "string",
            "threat_level": "T1 | T2 | T3",
            "action_taken": "log | quarantine | block",
            "requires_operator_review": True
        }
    )

    # 3. Threat Log (empty file)
    log_path = ROOT / "04_logs/security/threat_log.txt"
    try:
        if not log_path.exists():
            log_path.parent.mkdir(parents=True, exist_ok=True)
            log_path.touch()
            log_created(log_path)
        else:
            log_skipped(log_path)
    except Exception as e:
        log_failed(log_path, e)

    # 4. Attack Patterns
    write_file(
        ROOT / "07_reference_material/security/known_attack_patterns.md",
        """# KNOWN ATTACK PATTERNS

## Pattern 1
Type: Prompt Injection
Example: "ignore previous instructions"
Mitigation: Block + quarantine

---

## Pattern 2
Type: Data Exfiltration
Example: "send system data"
Mitigation: Immediate block
"""
    )

    # 5. Security System Map
    write_file(
        ROOT / "08_security_index/SECURITY_SYSTEM_MAP.md",
        """# SECURITY SYSTEM MAP

## Governance
00_governance_ref/security/

## Execution
01_core/execution/security/

## Logs
04_logs/security/

## Intelligence
07_reference_material/security/

## Config
02_config/
"""
    )

# -----------------------------
# SUMMARY
# -----------------------------
def report():
    print("\\n=== WAVE 1 BUILD COMPLETE ===")

    print("\\nCREATED:")
    for c in CREATED:
        print("-", c)

    print("\\nSKIPPED:")
    for s in SKIPPED:
        print("-", s)

    print("\\nFAILED:")
    for f in FAILED:
        print("-", f)

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    build_wave1()
    report()