# NEXUS Base V1 — Demo Walkthrough

## Demo Goal

Show that NEXUS routes actions through security, trust, approval, execution, and logging.

## Command 1 — Run Executor

python 01_core/execution/executor.py

Expected result: safe action executes through the approved/trusted path.

## Command 2 — Run War Test

python nexus_war_test.py

Expected result:

PASS: 21
WARN: 0
FAIL: 0

## Explanation

The war test confirms that unsafe phrases are detected, quarantined, and logged before execution.
