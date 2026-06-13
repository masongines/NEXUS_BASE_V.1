---
name: nexus-deep-dive-reporter
description: Source-labeled NEXUS deep-dive reporting for KAIROS/KAIROZ, KAIROS 1.0, AKARA, AEGIS, NEXUS_SUXEN, Sovereign Council material, glossary/index material, local multi-LLM material, project folders, Pieces conversations, and Codex chat history. Use when Codex needs to locate, digest, classify, and report on NEXUS-adjacent project knowledge without promoting memory, chats, generated outputs, or reference material into doctrine or project truth.
---

# NEXUS Deep Dive Reporter

## Operating Boundary

Treat this skill as `project-draft / auxiliary / not installed` unless a stronger current artifact says otherwise.

Preserve this source order:

1. Current operator instruction
2. Live NEXUS governing artifacts and current files
3. Active standards, checkpoints, registries, and approved plans
4. Reference material, older projects, and pre-draft material
5. Pieces, Codex, ChatGPT, and other chat or memory records
6. Generated summaries, reports, context exports, and observational outputs

Never let this skill:

- promote doctrine, standards, reports, memory, or chat findings
- treat Pieces/Codex/chat recall as validation or approval
- silently resolve source conflicts
- install itself into Codex skills
- mutate source project files while gathering a report
- imply that generated report findings are governance truth

Generated reports are `observational / advisory / operator-review required`.

## Workflow

1. Read `references/source_map.md` before collecting sources.
2. Read `references/query_terms.md` before searching.
3. Use `scripts/source_inventory.py` for local file and Codex-session inventory when useful.
4. Use available Pieces conversation/message search tools when the user requests recent chats, long-term memory, or Pieces history. If the tools are unavailable, record a source-access gap.
5. Read only the files/messages needed for the report. Prefer targeted keyword searches before opening large files.
6. Label every finding with source class, path or conversation ID, confidence, and whether it is current, reference-only, observational, or unresolved.
7. Use `references/report_template.md` for the final report structure.

## Local Inventory Helper

Run the helper from the workspace root. It writes nothing; it prints JSON to stdout.

```powershell
python "C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\06_operator\plans\codex_skills\nexus-deep-dive-reporter\scripts\source_inventory.py" --nexus-defaults --query "KAIROS" --query "KAIROZ" --query "SOVEREIGN COUNCIL" --query "AKARA" --query "AEGIS"
```

Use `--root` for narrower source passes:

```powershell
python "C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\06_operator\plans\codex_skills\nexus-deep-dive-reporter\scripts\source_inventory.py" --root "C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\07_reference_material" --terms-file "C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\06_operator\plans\codex_skills\nexus-deep-dive-reporter\references\query_terms.md"
```

The helper extracts/searches:

- `.md`
- `.txt`
- `.json`
- `.csv`
- `.log`
- `.docx`

It indexes these as extraction gaps for a second pass:

- PDFs
- images and screenshots
- archives
- spreadsheets
- slide decks
- unsupported binaries
- unreadable files

## Pieces And Chat Procedure

For Pieces searches, use keyword-based message searches first, then retrieve exact message snapshots as needed. Start with:

- `KAIROS`
- `KAIROZ`
- `KAIROZ 111`
- `OPTIMUS PRIME`
- `AKARA`
- `AEGIS`
- `NEXUS`
- `SOVEREIGN COUNCIL`
- `JOYBOY`
- `MYTHOS PRIME AXIOM`
- `HEKATE`

Record spelling and hit discrepancies. Planning evidence showed Pieces hits for `KAIROS`, `AKARA`, and `SOVEREIGN COUNCIL`, while exact sample searches for `KAIROZ` and `OPTIMUS PRIME` returned no matches. Re-check during each run instead of treating that as permanent truth.

For Codex local sessions, search:

- `C:\Users\mason\.codex\session_index.jsonl`
- `C:\Users\mason\.codex\sessions`

Classify Codex/Pieces/chat material as `memory-chat / advisory recall only`.

## Reporting Rules

Use concise NEXUS status labels:

- `implemented`
- `planned`
- `deferred`
- `reference-only`
- `draft`
- `observational`
- `stable`
- `active`
- `legacy`
- `review`

Use confidence labels:

- `high`
- `medium`
- `low`

For conflicts, write the conflict plainly:

- stronger source
- weaker source
- why they conflict
- what remains unresolved
- whether operator approval is required

Do not smooth conflicts into a single narrative unless the source hierarchy clearly resolves them.
