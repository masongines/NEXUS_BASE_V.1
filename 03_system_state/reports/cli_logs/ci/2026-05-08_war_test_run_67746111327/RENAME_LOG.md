# RENAME_LOG — War Test Run 67746111327

## Scope

Mechanical rename reference only. Records Strategy B rename operations
applied to extracted zip contents. Provenance and context belong in
README.md.

`cli_logs/` and `ci/` were not renamed — both were created with their
final names (operator-created scaffolding, 2026-05-10).

## Strategy B Convention

- Lowercase, underscored words
- Zero-padded numeric sort prefix (01_, 02_, etc.)
- Version suffix dropped from filenames where parent folder carries
  version identity (python_3_11/, python_3_12/)
- system.txt prefixed with 00_ to force sort-first within each folder

## Rename Map

### Phase 1 — files inside python_3_11/
### (formerly: Defensive War Test (3.11)/)

| Original | Renamed |
|---|---|
| system.txt | 00_system.txt |
| 1_Set up job.txt | 01_set_up_job.txt |
| 2_Checkout repository.txt | 02_checkout_repository.txt |
| 3_Set up Python 3.11.txt | 03_set_up_python.txt |
| 4_Run NEXUS war test.txt | 04_run_nexus_war_test.txt |
| 5_Verify war test result.txt | 05_verify_war_test_result.txt |
| 9_Post Set up Python 3.11.txt | 09_post_set_up_python.txt |
| 10_Post Checkout repository.txt | 10_post_checkout_repository.txt |
| 11_Complete job.txt | 11_complete_job.txt |

### Phase 2 — files inside python_3_12/
### (formerly: Defensive War Test (3.12)/)

| Original | Renamed |
|---|---|
| system.txt | 00_system.txt |
| 1_Set up job.txt | 01_set_up_job.txt |
| 2_Checkout repository.txt | 02_checkout_repository.txt |
| 3_Set up Python 3.12.txt | 03_set_up_python.txt |
| 4_Run NEXUS war test.txt | 04_run_nexus_war_test.txt |
| 5_Verify war test result.txt | 05_verify_war_test_result.txt |
| 9_Post Set up Python 3.12.txt | 09_post_set_up_python.txt |
| 10_Post Checkout repository.txt | 10_post_checkout_repository.txt |
| 11_Complete job.txt | 11_complete_job.txt |

### Phase 3 — subdirectory renames

| Original | Renamed |
|---|---|
| Defensive War Test (3.11) | python_3_11 |
| Defensive War Test (3.12) | python_3_12 |

### Phase 4 — root summary files

| Original | Renamed |
|---|---|
| 0_Defensive War Test (3.12).txt | combined_log_python_3_12.txt |
| 1_Defensive War Test (3.11).txt | combined_log_python_3_11.txt |
