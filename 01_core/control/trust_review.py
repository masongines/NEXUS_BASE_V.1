
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

    print("\n=== TRUST REVIEW ===\n")

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
