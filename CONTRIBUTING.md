# Contributing to NEXUS Base V1

NEXUS Base V1 is an open review project. Reviews, questions, issue reports,
and structural feedback are explicitly welcomed. The goal is collaborative
improvement under governed conditions.

---

## Governance Posture

All contributions are evaluated under the NEXUS governance architecture:

- **Authority:** [PRIME_AXIOM.md](00_governance_ref/doctrine/PRIME_AXIOM.md)
- **Execution Contract:** [execution_contract.md](00_governance_ref/execution_contract.md)
- **Partnership Standard:** [PARTNERSHIP_EXECUTION_STANDARD.md](00_governance_ref/doctrine/PARTNERSHIP_EXECUTION_STANDARD.md)
- **Sandbox Protocol:** [NEXUS_SANDBOX_PROTOCOL_LOCK_RECORD_v1_1.md](00_governance_ref/support_records/NEXUS_SANDBOX_PROTOCOL_LOCK_RECORD_v1_1.md)

The Sovereign Operator (Mason Gines) retains final authority over all
structural decisions. AI systems and external contributors may assist,
advise, and review — not govern.

---

## How to Contribute

### Reporting Issues

Use the GitHub Issues tab. Please include:

1. What you expected to happen
2. What actually happened
3. The output of `python nexus_war_test.py` (21 PASS / 0 WARN / 0 FAIL is the green baseline)
4. Your Python version (`python --version`)

### Suggesting Improvements

Open an issue tagged `enhancement`. Describe:

- The structural gap or improvement
- Which governance layer it touches (doctrine / execution / security / logging)
- Whether it requires a change to the war test

### Pull Requests

All PRs must confirm the sandbox protocol gate before review:

- [ ] `python nexus_war_test.py` still shows **21 PASS / 0 WARN / 0 FAIL** (or higher if test suite was expanded)
- [ ] No changes to `00_governance_ref/doctrine/` without explicit operator approval noted in the PR
- [ ] No `.bak`, `*.backup`, or `__pycache__` files included

---

## Sandbox Protocol

Changes that affect shared verification surfaces (war test, execution contract,
trust registry) are Tier 2 events under the NEXUS Escalation Tiering Protocol.
Flag these in your PR description.

Changes that affect governance doctrine, tool authorization structures, or
architectural authority are Tier 3 events and require Sovereign Operator
approval before merge.

When in doubt, open an issue first.

---

## Code Style

- Python 3.11+
- Google-style docstrings
- Type hints on public functions
- `print()` is acceptable in bootstrap scripts; structured logging preferred in new modules
- No external dependencies beyond the Python standard library unless discussed

---

## Reviews and Comments Welcome

This project is in active development as a capstone engineering artifact.
Critical review, architectural questions, and security observations are
particularly welcome. The entire premise of NEXUS is that scrutiny improves governance.
