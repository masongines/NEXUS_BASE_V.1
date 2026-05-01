# NEXUS THREAT MODEL v1

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
