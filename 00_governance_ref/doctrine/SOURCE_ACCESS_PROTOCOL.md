# SOURCE_ACCESS_PROTOCOL (v1)

## Purpose

Ensure the ChatGPT system operating inside the NEXUS_SUXEN project environment can retrieve required governance information when runtime memory does not contain the needed data.

This protocol prevents workflow disruption caused by runtime context limitations.

---

## Architecture Constraint

ChatGPT operates with two storage layers.

### Layer A — Project Sources

Files stored under:

Project → Sources

These files act as the authoritative governance repository for the system.

However they are not automatically loaded into runtime context for every message.

This is a deliberate performance and safety constraint.

---

### Layer B — Runtime Context

Runtime context contains only information currently loaded into the reasoning environment.

Examples:

• session uploaded files  
• previously referenced content  
• summarized governance state  

Runtime context is temporary and limited.

---

## Operational Rule

When required information is not present in runtime context but is required for correct operation:

The system must:

1. Check Project Sources  
2. Retrieve the required section of the file  
3. Load the minimum required content  
4. Continue the task  

Manual re-upload is not required unless the file is missing.

---

## Efficiency Rule

When retrieving from Sources:

• Only retrieve the minimum necessary portion  
• Avoid loading entire files unless necessary  
• Prefer summarized retrieval  

---

## Governance Boundary

Sources retrieval is read-only.

The system may:

• read  
• reference  
• quote  
• summarize  

The system may not modify governance files.

Only the operator may modify governance documents.

---

## Failure Condition

If a required governance file cannot be retrieved the system must notify the operator.

Example:

Required governance file unavailable.
Please re-upload the file or confirm it exists in Project Sources.

---

End of protocol
