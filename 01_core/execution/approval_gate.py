
import json
def request_approval(action):
    print("\n=== APPROVAL REQUIRED ===")
    print(json.dumps(action, indent=2))
    return input("Approve action? (y/n): ").lower() == "y"
