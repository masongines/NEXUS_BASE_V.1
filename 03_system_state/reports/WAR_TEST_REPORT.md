# NEXUS Base V1 — War Test Report

Generated: 2026-05-01T00:38:19.391352+00:00
Verdict: PASS

## Summary

- PASS: 21
- WARN: 0
- FAIL: 0

## Results

- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\01_core\execution\executor.py: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\01_core\execution\security\security_monitor.py: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\01_core\execution\security\quarantine_handler.py: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\02_config\execution_trust_registry.json: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\04_logs\security\threat_log.txt: present
- PASS — file_exists::C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\04_logs\execution\log.txt: present
- PASS — safe_action_not_flagged: {'threat': False}
- PASS — attack_detected::prompt_injection_basic: {'threat': True, 'level': 'T2', 'reason': 'ignore previous instructions'}
- PASS — attack_detected::data_exfiltration_request: {'threat': True, 'level': 'T2', 'reason': 'send system data'}
- PASS — attack_detected::secret_reveal_request: {'threat': True, 'level': 'T2', 'reason': 'reveal secrets'}
- PASS — attack_detected::bypass_attempt: {'threat': True, 'level': 'T2', 'reason': 'bypass'}
- PASS — attack_detected::exfiltration_keyword: {'threat': True, 'level': 'T2', 'reason': 'exfiltrate'}
- PASS — quarantine_appends_threat_log: before=2, after=3
- PASS — trust_registry_valid_json: valid JSON
- PASS — trust_level_valid: T3
- PASS — auto_approved_boolean: True
- PASS — executor_has_security_hook: detect_threat/quarantine found
- PASS — executor_has_trust_hook: trust registry logic found
- PASS — security_before_trust: security_pos=240, trust_pos=543
- PASS — datetime_utcnow_deprecated: no datetime.utcnow() found
- PASS — windows_encoding_emoji_risk: no known risky emoji found in scanned files