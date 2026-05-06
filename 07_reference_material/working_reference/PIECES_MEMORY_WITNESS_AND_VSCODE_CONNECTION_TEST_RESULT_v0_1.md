# Pieces Memory-Witness & VS Code Connection Test Result — v0.1

**Classification:** `MEMORY WITNESS — non-authoritative`
**Combined deliverable for:** Path A1 (single-client memory-witness test) + Path A2 (VS Code ↔ Pieces hookup)
**Per:** `NEXUS_MASTER_MILESTONE_HANDOFF_AND_DEVELOPMENT_PROGRESSION_PACKAGE_v0_1.md`
**Branch:** `feat/tri-sync-architecture` (post-ADR-004)

---

## Boundary statement (read first)

Pieces is treated as a **memory witness** only. Content retrieved through Pieces (MCP or VS Code extension) is `source_type: recall` and is **not** governance truth, **not** a NEXUS runtime authority, and **not** a substitute for operator review. No Base V1 component reads from Pieces at runtime. Personal Cloud is OFF (local-only). This document records observed state at the time of writing; no system behavior is changed by it.

---

## Environment captured

| Component | Version / state | Source of truth |
|---|---|---|
| Date | 2026-05-06 | system clock |
| Operator | Mason Gines (`masongines@gmail.com`) | git config |
| OS | Windows 11 Home 10.0.26200 | env |
| Pieces OS (`os_server.exe`) | **12.3.11.0**, PID 43264, started 2026-05-05 22:25 | `Get-Process` |
| Pieces Desktop (`pieces_for_x.exe`) | **5.1.1.0**, PID 49432, started 2026-05-06 07:20 | `Get-Process` |
| Pieces MCP listener | `127.0.0.1:39300`, Listen state, 56+ established connections | `Get-NetTCPConnection -LocalPort 39300` |
| VS Code path | `C:\Users\mason\Documents\applications\Microsoft VS Code\Code.exe` | `Get-Command code` |
| Pieces VS Code extension | `meshintelligenttechnologiesinc.pieces-vscode@3.0.1`, installed at `%USERPROFILE%\.vscode\extensions\meshintelligenttechnologiesinc.pieces-vscode-3.0.1`, `engines.vscode = ^1.61.1`, `activationEvents = ['onCommand:changePort', '*']`, `dist/extension.js` present | extension `package.json` |
| Project Pieces MCP config | `.claude/settings.json` → HTTP `http://localhost:39300/model_mcp` | repo file |
| Workspace Pieces config | `.vscode/settings.json` → `pieces.cloudCapabilities: Local` | repo file |

---

## A1 — Single-client memory-witness test (Claude Code MCP)

**Goal (per handoff):** Verify Pieces MCP is reachable from a single client (Claude Code), with Personal Cloud OFF, output labeled as memory witness.

**Result: PASS (configuration & infrastructure layer).**

- Pieces OS port 39300 reachable on IPv4 loopback (`Test-NetConnection localhost 39300` → True). IPv6 (`::1`) refuses, which is normal for a service bound to `127.0.0.1`.
- Project-scoped Claude Code MCP entry confirmed in `.claude/settings.json` (HTTP transport). No global Pieces MCP entry in `~/.claude.json`, which is the desired single-client posture.
- Personal Cloud confirmed OFF via `.vscode/settings.json` (`pieces.cloudCapabilities: "Local"`).

**Not yet captured in this artifact:** an actual `claude mcp list` output and a sample retrieval prompt response. This document was produced from process/log/manifest evidence; the in-`claude` recall round-trip is a follow-up step that should be paste-recorded in a v0.2 update once executed.

**Pieces data backup status:** ⚠ NOT VERIFIED in this run. Per A1 acceptance criteria, a backup of Pieces data should precede further integration work. See follow-ups.

---

## A2 — VS Code ↔ Pieces extension activation test

**Symptom as reported by operator:** "Pieces extension won't activate / load."

**Result: SYMPTOM NOT REPRODUCED in logs. Activation succeeds; UI symptom requires visual reproduction.**

### Evidence

VS Code Extension Host log for the most recent real GUI session (`%APPDATA%\Code\logs\20260506T111541\window2\exthost\exthost.log`) shows the Pieces extension activating cleanly at startup:

```
2026-05-06 11:15:54.868 [info] ExtensionService#_doActivateExtension MeshIntelligentTechnologiesInc.pieces-vscode, startup: true, activationEvent: '*'
2026-05-06 11:15:56.523 [warning] Provider for scheme 'explainedPiecesSnippetPreview' is firing event for schema 'piecesSnippetPreview' which will be IGNORED
```

The `*` activation event fires at startup; `engines.vscode = ^1.61.1` is well below current VS Code, so no engine-incompatibility block. No error thrown by the Pieces extension itself.

### What looked like a Pieces error but isn't

The same exthost log contains:

```
2026-05-06 11:15:57.450 [error] Error: e is not iterable
TypeError: e is not iterable
    at JOe.setItems (.../app/extensions/copilot/dist/extension.js:1165:19961)
```

The stack trace path `app\extensions\copilot\dist\extension.js` identifies this as the **VS Code-bundled GitHub Copilot extension**, not Pieces. It is unrelated to the Pieces hookup question and is recorded here only to prevent future misattribution.

### Benign Pieces warning

The `Provider for scheme 'explainedPiecesSnippetPreview' is firing event for schema 'piecesSnippetPreview' which will be IGNORED` warning indicates two URI scheme registrations whose names disagree. This is from inside the Pieces extension itself (a likely typo in `explainedPiecesSnippetPreview` vs `piecesSnippetPreview`) and is logged as a warning, not an error. It does not block activation. It would be reportable upstream to Pieces but is not a NEXUS-side fix.

### Open question for the operator

The reported "won't activate / load" feeling needs a more specific symptom before a fix can be proposed. Candidates to reproduce visually in VS Code and record in a v0.2 update:

1. Is the **Pieces sidebar icon** present in the activity bar? If yes, click it — what is shown?
2. Are Pieces commands available via `Ctrl+Shift+P` → typing "Pieces"? If yes, run "Pieces: Save to Pieces" on a selection — does it succeed?
3. Is there a **Pieces status bar item**? What does it say?
4. Open `Output` panel → channel dropdown → select "Pieces" (if listed). What does it print on workspace open?
5. Open `Help` → `Toggle Developer Tools` → `Console` while VS Code is running — capture any `pieces`-prefixed errors there (these don't always reach exthost.log).

Until one of these surfaces a concrete failure, the conclusion stands: **the extension activates and the Pieces OS service is reachable**. The "broken" perception may be UI/UX (empty snippet list because nothing has been saved, expected sidebar feature absent in v3.0.1, etc.) rather than a connection failure.

---

## Conclusion

| Plane | State |
|---|---|
| Pieces OS service | ✅ healthy, listening on `:39300` |
| Pieces Desktop | ✅ running |
| Claude Code MCP single-client config | ✅ present, project-scoped, local-only |
| Personal Cloud disabled | ✅ confirmed in `.vscode/settings.json` |
| VS Code extension installed | ✅ v3.0.1 |
| VS Code extension activation | ✅ logs show clean activation |
| VS Code extension *user-visible behavior* | ⚠ unverified — needs operator screen-level reproduction |
| Memory-witness classification preserved | ✅ no NEXUS runtime depends on this |
| Pieces data backup | ⚠ not verified in this run |

**A1 acceptance:** infrastructure pass; a paste-recorded recall round-trip is the remaining follow-up to fully close.
**A2 acceptance:** logs do not show an activation failure; operator visual reproduction required to confirm or refute the original symptom report.

---

## Follow-ups (do not roll into this v0.1)

1. Record an actual `claude mcp list` and one Pieces recall prompt-response pair in a v0.2 update of this file.
2. Verify Pieces data backup exists (Pieces Desktop → Settings → Backup, or operator's existing backup process). Note backup location and timestamp.
3. Operator to reproduce one specific VS Code symptom from the open-questions list above and append it.
4. If the warning on `explainedPiecesSnippetPreview` / `piecesSnippetPreview` proves load-bearing, consider filing it upstream to Pieces. **Not** a NEXUS scope item.
5. A3 (context export starter package) remains unblocked — it does not require A2 to fully close, only that retrieval continues to be classified as `recall`.

---

*Generated 2026-05-06. Memory witness only. No governance authority. No runtime dependency.*
