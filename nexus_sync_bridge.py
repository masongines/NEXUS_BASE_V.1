import argparse
import json
import sys
import uuid
from datetime import datetime, UTC
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "01_core" / "execution"))

from security.security_monitor import detect_threat
from security.quarantine_handler import quarantine

TRUST_PATH = BASE / "02_config/execution_trust_registry.json"
ACTION_SCHEMA_PATH = BASE / "02_config/action_schema.json"

LOG_ROUTES = {
    "learning_capture": BASE / "04_logs/audit/skillup_learning_log.txt",
    "governance_event":  BASE / "04_logs/audit/governance_events_log.txt",
}


def load_trust():
    if not TRUST_PATH.exists():
        return {}
    return json.load(open(TRUST_PATH))


def validate_payload(raw: dict) -> dict:
    required = {"action_type", "payload", "source"}
    missing = required - raw.keys()
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    if raw["action_type"] not in LOG_ROUTES:
        raise ValueError(
            f"Unknown action_type '{raw['action_type']}'. "
            f"Allowed: {list(LOG_ROUTES.keys())}"
        )
    return raw


def build_action(raw: dict) -> dict:
    return {
        "action_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "source": raw.get("source", "operator"),
        "action_type": raw["action_type"],
        "payload": raw["payload"],
        "requires_approval": True,
        "status": "proposed",
    }


def request_approval(action: dict) -> bool:
    print("\n--- PROPOSED SYNC ENTRY ---")
    print(json.dumps(action, indent=2))
    print("---------------------------")
    answer = input("Approve this entry? [y/N]: ").strip().lower()
    return answer == "y"


def append_log(action: dict):
    log_path = LOG_ROUTES[action["action_type"]]
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(action) + "\n")


def run(raw: dict):
    try:
        validate_payload(raw)
    except ValueError as e:
        print(f"VALIDATION ERROR: {e}")
        sys.exit(1)

    action = build_action(raw)

    threat_info = detect_threat(action)
    if threat_info.get("threat"):
        quarantine(action, threat_info)
        print(f"THREAT DETECTED — quarantined. Reason: {threat_info['reason']}")
        sys.exit(1)

    trust_registry = load_trust()
    tool_trust = trust_registry.get(action["action_type"], {})
    auto_approved = tool_trust.get("auto_approved", False)

    if auto_approved:
        approved = True
        print("AUTO-APPROVED (T3)")
    else:
        approved = request_approval(action)

    if not approved:
        action["status"] = "denied"
        append_log(action)
        print("Entry denied — not written.")
        sys.exit(0)

    action["status"] = "executed"
    append_log(action)
    print(f"Entry written to: {LOG_ROUTES[action['action_type']]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="NEXUS Sync Bridge — operator-approved cross-system log writer"
    )
    parser.add_argument(
        "--payload",
        type=str,
        required=True,
        help='JSON string with action_type, source, and payload fields',
    )
    args = parser.parse_args()

    try:
        raw_input = json.loads(args.payload)
    except json.JSONDecodeError as e:
        print(f"INVALID JSON: {e}")
        sys.exit(1)

    run(raw_input)
