"""
NEXUS Base V1 — Security Wave 2 Bootstrap

Purpose:
    Builds the active security enforcement layer for NEXUS Base V1.
    Creates security_monitor.py (threat detection) and
    quarantine_handler.py (threat logging), then patches executor.py
    to call security checks BEFORE trust and approval evaluation.

Role in NEXUS flow:
    Wave 2 activates the security gate. After this bootstrap runs, the
    executor enforces: Action → Security → (Trust → Approval → Execution).
    The security check happens first; a quarantined action never reaches
    the approval gate.

Run:
    python nexus_security_wave2_bootstrap.py
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
def write_file(path, content):
    try:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            log_created(path)
        else:
            log_skipped(path)
    except Exception as e:
        log_failed(path, e)

# -----------------------------
# SECURITY MONITOR
# -----------------------------
def create_security_monitor():
    """Write security_monitor.py to the execution security directory.

    The monitor exposes a ``detect_threat(action)`` function that scans
    the action payload for known threat-trigger phrases and returns a
    threat dict with ``threat``, ``level``, and ``reason`` fields.
    """
    write_file(
        ROOT / "01_core/execution/security/security_monitor.py",
        '''
def detect_threat(action):
    text = str(action).lower()

    triggers = [
        "ignore previous instructions",
        "send system data",
        "reveal secrets",
        "bypass",
        "exfiltrate"
    ]

    for t in triggers:
        if t in text:
            return {
                "threat": True,
                "level": "T2",
                "reason": t
            }

    return {"threat": False}
'''
    )

# -----------------------------
# QUARANTINE HANDLER
# -----------------------------
def create_quarantine_handler():
    """Write quarantine_handler.py to the execution security directory.

    The handler exposes a ``quarantine(action, threat_info)`` function that
    appends a structured JSON entry to the threat log and prints a notice.
    It is called by the executor when detect_threat returns threat=True.
    """
    write_file(
        ROOT / "01_core/execution/security/quarantine_handler.py",
        '''
import json
from pathlib import Path
from datetime import datetime, UTC

LOG_PATH = Path(__file__).resolve().parents[3] / "04_logs/security/threat_log.txt"

def quarantine(action, threat_info):
    entry = {
        "timestamp": datetime.now(UTC).isoformat(),
        "action": action,
        "threat_level": threat_info.get("level"),
        "reason": threat_info.get("reason"),
        "status": "QUARANTINED"
    }

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\\n")

    print("\\nTHREAT DETECTED - ACTION QUARANTINED")
    print(entry)
'''
    )

# -----------------------------
# EXECUTOR PATCH
# -----------------------------
def patch_executor():
    """Inject security hook imports and the pre-approval security check into executor.py.

    The patch inserts ``detect_threat`` and ``quarantine`` calls before the
    approval gate so that security evaluation always precedes trust evaluation.
    Idempotent: if ``security_monitor`` is already present in the file, the
    patch is skipped.
    """
    executor_path = ROOT / "01_core/execution/executor.py"

    try:
        if not executor_path.exists():
            log_failed(executor_path, "Executor not found")
            return

        content = executor_path.read_text()

        if "security_monitor" in content:
            log_skipped(executor_path)
            return

        injection_imports = '''
from security.security_monitor import detect_threat
from security.quarantine_handler import quarantine
'''

        injection_check = '''
    # SECURITY CHECK
    threat_info = detect_threat(action)

    if threat_info.get("threat"):
        quarantine(action, threat_info)
        return
'''

        content = content.replace(
            "from approval_gate import request_approval",
            "from approval_gate import request_approval" + injection_imports
        )

        content = content.replace(
            "approved = request_approval(action)",
            injection_check + "\\n    approved = request_approval(action)"
        )

        executor_path.write_text(content)
        log_created(executor_path)

    except Exception as e:
        log_failed(executor_path, e)

# -----------------------------
# SUMMARY
# -----------------------------
def report():
    print("\\n=== WAVE 2 BUILD COMPLETE ===")

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
    create_security_monitor()
    create_quarantine_handler()
    patch_executor()
    report()