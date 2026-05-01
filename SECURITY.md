# Security Policy

## Supported Versions

NEXUS Base V1 is a capstone proof-of-concept. Only the latest commit on `main` is
actively maintained.

## Reporting a Vulnerability

If you discover a security vulnerability in NEXUS Base V1, please **do not open a
public issue** until a fix has been discussed.

**Preferred path:**
1. Open a GitHub Issue titled `[SECURITY] <brief description>`
2. Mark it as confidential if the platform supports it, or email the maintainer directly

The maintainer (Mason Gines) will acknowledge within 5 business days and work toward
a resolution or a documented decision on scope.

## Scope Notes

NEXUS Base V1 is a local-first, offline system with no network-facing endpoints.
The primary security concerns relevant to this codebase are:

- Bypass of the threat detection layer (Security Monitor)
- Evasion of the approval gate
- Tampering with append-only execution or threat logs
- Injection via action payload fields

Findings in these areas are the most actionable and are strongly encouraged.
