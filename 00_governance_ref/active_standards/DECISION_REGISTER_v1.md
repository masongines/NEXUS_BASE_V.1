# DECISION_REGISTER_v1

Classification: Active Standard  
Authority: Non-Doctrinal  
Layer: Governance  

Purpose:
Track structural decisions persistently.

Required Fields:
- decision id
- context
- options
- risks
- reversibility
- approval status
- authority source

Rules:
- No decision = no structure change
- No approval without provenance
- No silent replacement

Status Flow:
Open → Review → Approved/Rejected → Closed

End State:
Full traceability of system evolution.