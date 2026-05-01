# Cleanup Inventory — 2026-05-01

One-time record taken at the start of the NEXUS Base V1 GitHub repo professionalization pass.

## Pre-cleanup snapshot

- Worktree: `.claude/worktrees/strange-cray-a09ec3`
- Branch: `claude/strange-cray-a09ec3` (tracking `origin/main`)
- Tag created for rollback: `pre-cleanup-2026-05-01`
- War test baseline: **21 PASS / 0 WARN / 0 FAIL**

## .bak / backup / __pycache__ files tracked in git

```
git ls-files | grep -iE '\.bak|backup|pycache'
→ (none)
```

The `.bak_*` files visible in the user's main local working tree at
`C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS` exist only on disk; they
were never staged into the repository (the existing `.gitignore` line
`*.bak_*` covered them). Nothing to remove from git history.

## Internal / draft documents removed from public repo

The following were removed from the GitHub repo because they expose
internal workflow material that does not belong in a public engineering
artifact. Originals preserved at:
`C:\Users\mason\Documents\PROJECTS\NEXUS_PRIVATE_DOCS\`

- `FACULTY_MESSAGE.md`
- `LINKEDIN_POST.md`
- `PUBLICATION_CHECKLIST.md`
- `GITHUB_PROJECT_ROADMAP.md`
- `README_STRUCTURE.txt`

## Documents merged into README and removed from root

- `SYSTEM_DEMONSTRATION.md` → README "Validation" + "Architecture"
- `DEMO_WALKTHROUGH.md` → README "Quickstart"

Content fully preserved; no information loss.

## Documents kept and linked from README

- `NEXUS_BASE_V1_DEEP_DIVE.md`
- `CAPSTONE_PAPER.md`

## Rollback

`git reset --hard pre-cleanup-2026-05-01` restores the entire pre-plan
state if any wave fails to meet its sandbox gate.
