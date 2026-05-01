"""
NEXUS Base V1 — Security Wave 3 Bootstrap

Purpose:
    Builds the trust layer for NEXUS Base V1.
    Creates execution_trust_registry.json (defines trust levels and
    auto-approval rules per action type) and trust_review.py (reads
    execution + threat logs to surface trust promotion candidates).
    Also patches executor.py to evaluate the trust registry before
    routing to the human approval gate.

Role in NEXUS flow:
    Wave 3 completes the full NEXUS governance pipeline:
    Action → Security → Trust → Approval → Execution → Logging.
    Trusted actions at level T3 with auto_approved=True bypass the
    human gate. All others still require human approval.

Run:
    python nexus_security_wave3_bootstrap.py
"""

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
def write_file(path, content, is_json=False):
    try:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            if is_json:
                path.write_text(json.dumps(content, indent=2), encoding="utf-8")
            else:
                path.write_text(content, encoding="utf-8")
            log_created(path)
        else:
            log_skipped(path)
    except Exception as e:
        log_failed(path, e)

# -----------------------------
# TRUST REGISTRY
# -----------------------------
def create_trust_registry():
    """Write execution_trust_registry.json defining trust levels per action type.

    The registry maps action_type strings to trust metadata (trust_level,
    auto_approved). Level T3 with auto_approved=True bypasses the human gate.
    """
    write_file(
        ROOT / "02_config/execution_trust_registry.json",
        {
            "echo": {
                "trust_level": "T1",
                "auto_approved": False
            }
        },
        is_json=True
    )

# -----------------------------
# TRUST REVIEW SCRIPT
# -----------------------------
def create_trust_review():
    """Write trust_review.py, a log-analysis script for trust promotion decisions.

    The script reads execution and threat logs to surface action types that
    have accumulated enough clean executions to be candidates for trust-level
    promotion. Output is advisory only — no automatic trust changes are made.
    """
    write_file(
        ROOT / "01_core/control/trust_review.py",
        '''
from pathlib import Path
import json

EXEC_LOG = Path("04_logs/execution/log.txt")
THREAT_LOG = Path("04_logs/security/threat_log.txt")

def load(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]

def run():
    exec_logs = load(EXEC_LOG)
    threat_logs = load(THREAT_LOG)

    tool_counts = {}
    for e in exec_logs:
        t = e.get("action_type")
        tool_counts[t] = tool_counts.get(t, 0) + 1

    threat_counts = {}
    for t in threat_logs:
        a = t.get("action", {}).get("action_type")
        threat_counts[a] = threat_counts.get(a, 0) + 1

    print("\\n=== TRUST REVIEW ===\\n")

    for tool, count in tool_counts.items():
        threats = threat_counts.get(tool, 0)

        if count >= 50 and threats == 0:
            print(f"[PROMOTE?] {tool} → candidate T3")
        elif threats > 0:
            print(f"[WATCH] {tool} → threats detected")
        else:
            print(f"[OK] {tool}")

if __name__ == "__main__":
    run()
'''
    )

# -----------------------------
# EXECUTOR PATCH
# -----------------------------
def patch_executor():
    """Inject the trust registry lookup into executor.py before the approval gate.

    Adds trust-level evaluation so that T3/auto_approved actions bypass the
    human gate. Idempotent: skipped if ``execution_trust_registry`` is already
    present in the file.
    """
    executor_path = ROOT / "01_core/execution/executor.py"

    try:
        if not executor_path.exists():
            log_failed(executor_path, "Executor not found")
            return

        content = executor_path.read_text()

        if "execution_trust_registry" in content:
            log_skipped(executor_path)
            return

        injection = '''
# -----------------------------
# TRUST SYSTEM
# -----------------------------
import json
TRUST_PATH = BASE / "02_config/execution_trust_registry.json"

def load_trust():
    if not TRUST_PATH.exists():
        return {}
    return json.load(open(TRUST_PATH))

trust_registry = load_trust()
tool_trust = trust_registry.get(action["action_type"], {})
trust_level = tool_trust.get("trust_level", "T0")
auto_approved = tool_trust.get("auto_approved", False)

if trust_level == "T3" and auto_approved:
    print("\\nTRUSTED AUTO-APPROVAL (T3)")
    approved = True
else:
    approved = request_approval(action)
'''

        content = content.replace(
            "approved = request_approval(action)",
            injection
        )

        executor_path.write_text(content)
        log_created(executor_path)

    except Exception as e:
        log_failed(executor_path, e)

# -----------------------------
# SUMMARY
# -----------------------------
def report():
    print("\\n=== WAVE 3 BUILD COMPLETE ===")

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
    create_trust_registry()
    create_trust_review()
    patch_executor()
    report()