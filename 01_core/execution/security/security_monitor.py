
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
