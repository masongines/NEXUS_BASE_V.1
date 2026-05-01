"""
NEXUS Base V1 — Polished Reference Module

PURPOSE: Illustrative only. NOT imported by the live system.

This file demonstrates what a production-grade version of the core
NEXUS execution patterns would look like using modern Python conventions:
  - Structured ``logging`` instead of ``print()``
  - Full type hints on all public functions
  - Explicit ``pathlib.Path`` everywhere
  - Named exceptions rather than bare ``except Exception``
  - ``dataclasses`` for structured result types

Reviewers can use this file to understand the operator's intent for
future refactoring without any risk to the running system — this module
has zero runtime imports from the live codebase.

To see the production code this illustrates, see:
  - bootstrap_runtime.py
  - nexus_security_wave2_bootstrap.py
  - nexus_war_test.py
"""

from __future__ import annotations

import json
import logging
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

log = logging.getLogger("nexus.reference")


# ---------------------------------------------------------------------------
# Result type — replaces bare dict returns
# ---------------------------------------------------------------------------

@dataclass
class TestResult:
    """A single war-test case outcome.

    Attributes:
        test: Unique test identifier string.
        status: One of ``PASS``, ``FAIL``, or ``WARN``.
        details: Human-readable detail string for the outcome.
    """

    test: str
    status: str  # Literal["PASS", "FAIL", "WARN"] once Python 3.11+ is required
    details: str = ""


# ---------------------------------------------------------------------------
# Idempotent file writer — illustrates write_file pattern with type hints
# ---------------------------------------------------------------------------

def write_if_missing(path: Path, content: str | dict) -> bool:
    """Write content to path only if the file does not already exist.

    Args:
        path: Destination file path (created with parents as needed).
        content: String written verbatim, or dict serialised to indented JSON.

    Returns:
        True if the file was created, False if it was skipped.

    Raises:
        OSError: If the parent directory cannot be created or the file
            cannot be written.
    """
    if path.exists():
        log.debug("skip (exists): %s", path)
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(content, indent=2) if isinstance(content, dict) else content
    path.write_text(text, encoding="utf-8")
    log.info("created: %s", path)
    return True


# ---------------------------------------------------------------------------
# Threat detection — illustrates security_monitor pattern with type hints
# ---------------------------------------------------------------------------

_THREAT_TRIGGERS: frozenset[str] = frozenset(
    {
        "ignore previous instructions",
        "send system data",
        "reveal secrets",
        "bypass",
        "exfiltrate",
    }
)


def detect_threat(action: dict) -> dict:
    """Scan an action dict for known threat-trigger phrases.

    Serialises the entire action to a lowercase string and checks for any
    phrase in ``_THREAT_TRIGGERS``. This broad-match strategy avoids fragile
    field-by-field inspection at the cost of false positives on benign
    payloads that happen to contain trigger words.

    Args:
        action: Arbitrary action dict following the NEXUS action schema.

    Returns:
        ``{"threat": False}`` if no trigger matched.
        ``{"threat": True, "level": "T2", "reason": "<trigger>"}`` otherwise.
    """
    text = str(action).lower()
    for trigger in _THREAT_TRIGGERS:
        if trigger in text:
            log.warning("T2 threat detected — reason: %s", trigger)
            return {"threat": True, "level": "T2", "reason": trigger}
    return {"threat": False}


# ---------------------------------------------------------------------------
# Quarantine handler — illustrates quarantine pattern with type hints
# ---------------------------------------------------------------------------

def quarantine(
    action: dict,
    threat_info: dict,
    *,
    log_path: Path,
) -> None:
    """Append a quarantine record to the threat log and emit a warning.

    Args:
        action: The action that triggered the threat.
        threat_info: Dict returned by ``detect_threat()``.
        log_path: Absolute path to the threat log file. Created if absent.

    Raises:
        OSError: If the log directory cannot be created or the entry cannot
            be appended.
    """
    entry = {
        "timestamp": datetime.now(UTC).isoformat(),
        "action": action,
        "threat_level": threat_info.get("level"),
        "reason": threat_info.get("reason"),
        "status": "QUARANTINED",
    }

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")

    log.warning("THREAT DETECTED - ACTION QUARANTINED: %s", entry)


# ---------------------------------------------------------------------------
# Illustrative main — shows structured logging setup pattern
# ---------------------------------------------------------------------------

def _configure_logging() -> None:
    """Configure root logger for structured console output."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        stream=sys.stdout,
    )


if __name__ == "__main__":
    _configure_logging()
    log.info("Reference module loaded — this file is illustrative only.")
    log.info("No live NEXUS components are imported or modified.")
