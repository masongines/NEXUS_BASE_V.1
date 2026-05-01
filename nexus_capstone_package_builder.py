"""
NEXUS Base V1 — Capstone Package Builder

Purpose:
    Generates the capstone documentation package for NEXUS Base V1.
    Writes a set of structured markdown documents to the repo root and
    appends capstone links to README.md.

Historical note:
    Some documents in the DOCS dict (LINKEDIN_POST.md, FACULTY_MESSAGE.md,
    GITHUB_PROJECT_ROADMAP.md, PUBLICATION_CHECKLIST.md) are internal
    communication materials not published to the public GitHub repo.
    These are preserved separately at NEXUS_PRIVATE_DOCS/. Running this
    script will recreate them locally; they remain gitignored on the
    public surface.

Run:
    python nexus_capstone_package_builder.py
"""

from pathlib import Path
from datetime import datetime, UTC

ROOT = Path(".").resolve()
REPORT_DIR = ROOT / "03_system_state" / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

DOCS = {
    "SYSTEM_DEMONSTRATION.md": [
        "# NEXUS Base V1 — System Demonstration",
        "",
        "NEXUS Base V1 is a governed AI execution system.",
        "",
        "Its purpose is to make sure AI-related actions are only allowed when they are safe, authorized, traceable, and aligned with governance rules.",
        "",
        "## Core Flow",
        "",
        "Action -> Security -> Trust -> Approval -> Execution -> Logging",
        "",
        "## What It Proves",
        "",
        "- Controlled execution",
        "- Human approval gating",
        "- Trust-based auto-approval",
        "- Rule-based security detection",
        "- Quarantine logging",
        "- Defensive sandbox validation",
        "",
        "## Validation Result",
        "",
        "PASS: 21",
        "WARN: 0",
        "FAIL: 0",
        "",
        "## Key Principle",
        "",
        "NEXUS does not only ask what AI can do. It asks what AI is allowed to do.",
        "",
        "## Current Limits",
        "",
        "- No advanced anomaly detection yet",
        "- No adaptive threat intelligence yet",
        "- No multi-agent orchestration yet",
        "- Not a production deployment",
    ],

    "CAPSTONE_PAPER.md": [
        "# Capstone Paper — NEXUS Base V1",
        "",
        "## Title",
        "",
        "NEXUS Base V1: A Governance-First AI Execution System",
        "",
        "## Summary",
        "",
        "NEXUS Base V1 is a local-first, governance-driven AI execution framework designed to control how AI-related actions are proposed, checked, approved, executed, and logged.",
        "",
        "The system implements this flow:",
        "",
        "Action -> Security -> Trust -> Approval -> Execution -> Logging",
        "",
        "## Implemented Components",
        "",
        "- executor.py",
        "- approval_gate.py",
        "- tool_registry.json",
        "- security_monitor.py",
        "- quarantine_handler.py",
        "- execution_trust_registry.json",
        "- trust_review.py",
        "- nexus_war_test.py",
        "",
        "## Validation",
        "",
        "The defensive sandbox war test passed with:",
        "",
        "PASS: 21",
        "WARN: 0",
        "FAIL: 0",
        "",
        "## Conclusion",
        "",
        "The main achievement is not simply that the system can execute actions. The main achievement is that the system controls whether an action should execute.",
    ],

    "DEMO_WALKTHROUGH.md": [
        "# NEXUS Base V1 — Demo Walkthrough",
        "",
        "## Demo Goal",
        "",
        "Show that NEXUS routes actions through security, trust, approval, execution, and logging.",
        "",
        "## Command 1 — Run Executor",
        "",
        "python 01_core/execution/executor.py",
        "",
        "Expected result: safe action executes through the approved/trusted path.",
        "",
        "## Command 2 — Run War Test",
        "",
        "python nexus_war_test.py",
        "",
        "Expected result:",
        "",
        "PASS: 21",
        "WARN: 0",
        "FAIL: 0",
        "",
        "## Explanation",
        "",
        "The war test confirms that unsafe phrases are detected, quarantined, and logged before execution.",
    ],

    "LINKEDIN_POST.md": [
        "# LinkedIn Post — NEXUS Base V1",
        "",
        "I just published my capstone project: NEXUS Base V1.",
        "",
        "NEXUS Base V1 is a governed AI execution system.",
        "",
        "Most AI systems focus on what AI can do.",
        "",
        "This project focuses on what AI is allowed to do.",
        "",
        "Core flow:",
        "",
        "Action -> Security -> Trust -> Approval -> Execution -> Logging",
        "",
        "The system includes approval gating, trust-based automation, rule-based security detection, quarantine logging, reproducible bootstrap scripts, and defensive sandbox validation.",
        "",
        "Validation result:",
        "",
        "PASS: 21",
        "WARN: 0",
        "FAIL: 0",
        "",
        "This is not a fully autonomous AI operating system. It is a governance-first execution framework built to preserve human control, traceability, and safety.",
        "",
        "#AI #Python #CyberSecurity #AIGovernance #SystemsArchitecture #MachineLearning",
    ],

    "FACULTY_MESSAGE.md": [
        "# Faculty / Reviewer Message",
        "",
        "Subject: NEXUS Base V1 Capstone Project Submission",
        "",
        "Hello,",
        "",
        "I am submitting my capstone project, NEXUS Base V1.",
        "",
        "NEXUS Base V1 is a governance-first AI execution system designed to ensure that AI-related actions are controlled, traceable, and validated before execution.",
        "",
        "The system flow is:",
        "",
        "Action -> Security -> Trust -> Approval -> Execution -> Logging",
        "",
        "The project passed its current validation run:",
        "",
        "PASS: 21",
        "WARN: 0",
        "FAIL: 0",
        "",
        "The system is not presented as a production deployment or fully autonomous AI platform. It is a governed execution framework demonstrating control boundaries, human approval, and defensive validation.",
        "",
        "Thank you for reviewing my project.",
        "",
        "Mason Gines",
    ],

    "GITHUB_PROJECT_ROADMAP.md": [
        "# GitHub Project Roadmap — NEXUS Base V1",
        "",
        "## Done",
        "",
        "- Publish repository",
        "- Add README",
        "- Pass defensive sandbox war test",
        "- Add final war test evidence",
        "",
        "## In Progress",
        "",
        "- Add capstone documentation package",
        "- Prepare demo walkthrough",
        "- Prepare faculty/reviewer message",
        "",
        "## Future Work",
        "",
        "- Expand attack pattern database",
        "- Add anomaly scoring",
        "- Add dashboard view",
        "- Add multi-agent governance plan",
    ],

    "PUBLICATION_CHECKLIST.md": [
        "# NEXUS Base V1 — Publication Checklist",
        "",
        "## Repository",
        "",
        "- [ ] README.md present",
        "- [ ] SYSTEM_DEMONSTRATION.md present",
        "- [ ] CAPSTONE_PAPER.md present",
        "- [ ] DEMO_WALKTHROUGH.md present",
        "- [ ] WAR_TEST_REPORT.md present",
        "",
        "## Validation",
        "",
        "- [ ] War test returns PASS",
        "- [ ] PASS = 21",
        "- [ ] WARN = 0",
        "- [ ] FAIL = 0",
        "",
        "## Claims Check",
        "",
        "- [ ] Does not claim production deployment",
        "- [ ] Does not claim full autonomy",
        "- [ ] Does not claim anomaly detection",
        "- [ ] Does not claim multi-agent orchestration",
    ],
}

README_LINK = """
---

## Capstone Documentation

- [System Demonstration](SYSTEM_DEMONSTRATION.md)
- [Capstone Paper](CAPSTONE_PAPER.md)
- [Demo Walkthrough](DEMO_WALKTHROUGH.md)
- [Publication Checklist](PUBLICATION_CHECKLIST.md)
"""

def write_doc(name, lines):
    path = ROOT / name
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE: {name}")

def update_readme():
    readme = ROOT / "README.md"
    if not readme.exists():
        readme.write_text("# NEXUS Base V1\n\nGoverned AI Execution System.\n", encoding="utf-8")

    text = readme.read_text(encoding="utf-8")
    if "## Capstone Documentation" not in text:
        readme.write_text(text.rstrip() + "\n" + README_LINK, encoding="utf-8")
        print("UPDATED: README.md")
    else:
        print("SKIPPED: README.md already has capstone links")

def write_report():
    report = REPORT_DIR / "CAPSTONE_PACKAGE_BUILD_REPORT.md"
    lines = [
        "# NEXUS Base V1 — Capstone Package Build Report",
        "",
        f"Generated: {datetime.now(UTC).isoformat()}",
        "Status: COMPLETE",
        "",
        "Files generated:",
    ]
    for name in DOCS:
        lines.append(f"- {name}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("WROTE: 03_system_state/reports/CAPSTONE_PACKAGE_BUILD_REPORT.md")

def main():
    print("=== NEXUS CAPSTONE PACKAGE BUILDER ===")
    print(f"Root: {ROOT}")
    for name, lines in DOCS.items():
        write_doc(name, lines)
    update_readme()
    write_report()
    print("DONE")

if __name__ == "__main__":
    main()