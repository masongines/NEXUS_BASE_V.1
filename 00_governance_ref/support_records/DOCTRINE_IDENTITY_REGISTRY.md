# DOCTRINE_IDENTITY_REGISTRY

Purpose:
The Doctrine Identity Registry guarantees that each governance doctrine
has exactly one canonical identity within Project Sources.

This registry prevents duplicate doctrine identities from entering the
system and provides a deterministic mapping between doctrine names and
their canonical filenames.

This file functions as a structural guardrail for governance audits.

---

## Identity Normalization Rule

Before comparison, doctrine filenames must be normalized using:

- lowercase
- trim whitespace
- preserve `.md`
- convert spaces, underscores, and hyphens to `_`
- collapse repeated separators

Example:

PRIME AXIOM.md  
PRIME_AXIOM.md  
prime-axiom.md  

All normalize to:

prime_axiom.md

Only **one canonical source file** may resolve to each normalized key.

---

## Canonical Doctrine Identity Table

| Canonical File | Normalized Identity Key | Status | Owning Lab |
|---|---|---|---|
| PRIME_AXIOM.md | prime_axiom.md | ACTIVE | NEXUS |
| MASTER_ARCHITECTURE.md | master_architecture.md | ACTIVE | NEXUS |
| SOURCE_ACCESS_PROTOCOL.md | source_access_protocol.md | ACTIVE | NEXUS |
| ESCALATION_TIERING_PROTOCOL.md | escalation_tiering_protocol.md | ACTIVE | NEXUS |
| DOCTRINE_PROMOTION_PROTOCOL.md | doctrine_promotion_protocol.md | ACTIVE | NEXUS |
| FACTUAL_VALIDATION_PROTOCOL.md | factual_validation_protocol.md | ACTIVE | NEXUS |
| ENTROPY_MONITORING_SYSTEM.md | entropy_monitoring_system.md | ACTIVE | NEXUS |
| SYSTEM_STATE_SNAPSHOT_PROTOCOL.md | system_state_snapshot_protocol.md | ACTIVE | NEXUS |
| PARTNERSHIP_EXECUTION_STANDARD.md | partnership_execution_standard.md | ACTIVE | NEXUS |
| RESPONSE_FORMAT_STANDARD.md | response_format_standard.md | ACTIVE | NEXUS |
| CONSOLIDATION_LOG.md | consolidation_log.md | ACTIVE | NEXUS |
| TERMINOLOGY_INDEX.md | terminology_index.md | ACTIVE | NEXUS |

---

## Non-Doctrinal Kernel Artifact Note

The governance kernel may contain additional governed artifacts
that are not classified as doctrine.

These may include:

- active standards
- safeguard frameworks
- kernel support records
- working governance artifacts

These artifacts:

- do not enter the Canonical Doctrine Identity Table
- do not count as doctrine
- are tracked separately in kernel inventory (e.g., KERNEL_MANIFEST.json)

They may be promoted into doctrine only through the Doctrine Promotion Protocol.

---

## Governance Rule

A new doctrine file **may not be introduced** if its normalized identity
matches an existing entry in this registry.

If a conflict is detected:

1. The audit must halt promotion.
2. A Tier-3 governance review is triggered.
3. The Sovereign Operator determines the canonical doctrine.

---

## Registry Update Rule

Whenever a doctrine is:

- promoted
- renamed
- deprecated

this registry **must be updated** to reflect the canonical identity.

The registry is considered part of the **governance kernel** and must
remain synchronized with Project Sources.