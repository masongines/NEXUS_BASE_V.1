
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
        f.write(json.dumps(entry) + "\n")

    print("\nTHREAT DETECTED - ACTION QUARANTINED")
    print(entry)
