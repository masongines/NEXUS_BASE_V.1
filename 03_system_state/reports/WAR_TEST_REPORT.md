# NEXUS Base V1 — War Test Report

Generated: 2026-05-01T09:49:27.093517+00:00
Verdict: PASS

## Summary

- PASS: 36
- WARN: 0
- FAIL: 0

## Results

- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.claude\worktrees\strange-cray-a09ec3\01_core\execution\executor.py: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.claude\worktrees\strange-cray-a09ec3\01_core\execution\security\security_monitor.py: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.claude\worktrees\strange-cray-a09ec3\01_core\execution\security\quarantine_handler.py: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.claude\worktrees\strange-cray-a09ec3\02_config\execution_trust_registry.json: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.claude\worktrees\strange-cray-a09ec3\04_logs\security\threat_log.txt: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.claude\worktrees\strange-cray-a09ec3\04_logs\execution\log.txt: present
- PASS — safe_action_not_flagged: {'threat': False}
- PASS — attack_detected::prompt_injection_basic: {'threat': True, 'level': 'T2', 'reason': 'ignore previous instructions'}
- PASS — attack_detected::data_exfiltration_request: {'threat': True, 'level': 'T2', 'reason': 'send system data'}
- PASS — attack_detected::secret_reveal_request: {'threat': True, 'level': 'T2', 'reason': 'reveal secrets'}
- PASS — attack_detected::bypass_attempt: {'threat': True, 'level': 'T2', 'reason': 'bypass'}
- PASS — attack_detected::exfiltration_keyword: {'threat': True, 'level': 'T2', 'reason': 'exfiltrate'}
- PASS — quarantine_appends_threat_log: before=14, after=15
- PASS — trust_registry_valid_json: valid JSON
- PASS — trust_level_valid: T3
- PASS — auto_approved_boolean: True
- PASS — executor_has_security_hook: detect_threat/quarantine found
- PASS — executor_has_trust_hook: trust registry logic found
- PASS — security_before_trust: security_pos=240, trust_pos=543
- PASS — datetime_utcnow_deprecated: no datetime.utcnow() found
- PASS — windows_encoding_emoji_risk: no known risky emoji found in scanned files
- PASS — A1_no_bak_files_committed: no *.bak/backup/old files tracked
- PASS — A2_no_pycache_committed: no __pycache__ tracked
- PASS — A3_gitignore_has_required_patterns: all required patterns present
- PASS — A4_internal_docs_absent: no internal draft docs committed
- PASS — B5_license_apache: LICENSE present with Apache marker
- PASS — B6_contributing_references_sandbox: CONTRIBUTING.md present with sandbox reference
- PASS — B7_requirements_exists: requirements.txt present
- PASS — B8_pyproject_python_pin: pyproject.toml present with requires-python
- PASS — B9_ci_workflow_exists: .github/workflows/ci.yml present
- PASS — C10_readme_has_quickstart: ## Quickstart found
- PASS — C11_readme_has_war_test_command: run command present
- PASS — C12_readme_links_docs: DEEP_DIVE and CAPSTONE_PAPER linked
- PASS — C13_readme_has_limitations: ## Limitations section found
- PASS — D14_governance_ref_populated: 40 items
- PASS — D15_decision_register_has_entries: 2 record(s)