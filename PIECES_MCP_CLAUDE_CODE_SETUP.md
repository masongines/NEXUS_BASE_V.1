# Pieces OS → Claude Code MCP Setup Guide
## VS_CODE_NEXUS / NEXUS Base V1

**Status:** Ready to configure  
**Prerequisite confirmed:** `.vscode/settings.json` has `"pieces.cloudCapabilities": "Local"` ✅  
**Goal:** Let Claude Code (CLI) pull context directly from your running Pieces OS instance.

---

## What You Need Running First

Before Claude Code can connect to Pieces, make sure:

1. **Pieces OS desktop app is open and running** (check your system tray)
2. **Pieces for VS Code extension is active** (already confirmed ✅)
3. **Claude Code CLI is installed** — verify with `claude --version` in terminal

---

## Option A: CLI Command (Easiest — Do This First)

Open a terminal in VS Code and run:

```bash
claude mcp add --transport http pieces http://localhost:39300/model_context_protocol/2025-03-26/mcp
```

If Pieces uses SSE transport (try this if the above fails):

```bash
claude mcp add --transport sse pieces http://localhost:39300/model_context_protocol/2024-11-05/sse
```

Then verify it was added:

```bash
claude mcp list
```

You should see `pieces` in the list. Done — skip to the Test section.

---

## Option B: Manual Config File Edit

If the CLI command doesn't work, edit the global Claude Code config file directly.

**File location:** `C:\Users\mason\.claude.json`

If the file doesn't exist, create it. Add or merge this content:

```json
{
  "mcpServers": {
    "pieces": {
      "type": "http",
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

If the file already has content, add the `"pieces"` block inside the existing `"mcpServers"` object — don't replace anything else.

---

## Option C: Project-Level Config (VS_CODE_NEXUS Only)

To scope the Pieces connection only to this project, create `.mcp.json` at the project root:

**File:** `C:\Users\mason\Documents\PROJECTS\VS_CODE_NEXUS\.mcp.json`

```json
{
  "mcpServers": {
    "pieces": {
      "type": "http",
      "url": "http://localhost:39300/model_context_protocol/2025-03-26/mcp"
    }
  }
}
```

Or use the CLI with `--scope project`:

```bash
claude mcp add --transport http --scope project pieces http://localhost:39300/model_context_protocol/2025-03-26/mcp
```

This activates Pieces MCP only when Claude Code is running inside the VS_CODE_NEXUS directory. Recommended for keeping NEXUS context clean.

---

## Test the Connection

After setup, open a new terminal in VS_CODE_NEXUS and run:

```bash
claude
```

Then type a test prompt:

```
Summarize what I have open in Pieces right now
```

or

```
What are my most recent code snippets in Pieces?
```

If Pieces OS is running and MCP is connected, Claude Code will pull context directly from it.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `pieces not found` | Make sure Pieces OS desktop app is running |
| `Connection refused` | Check Pieces is on port 39300 — open Pieces → Settings → confirm MCP port |
| `Transport error` | Try `--transport sse` flag and the SSE URL above |
| `Permission denied` | Run terminal as administrator once to register the MCP server |
| Still failing | Export from Pieces manually → save to `PIECES_EXPORT/` folder as interim |

---

## What This Unlocks in Claude Code (VS Code Terminal)

Once connected, Claude Code can:

- **Pull recent snippets** — "what code did I save related to FAISS or embeddings?"
- **Get workflow context** — "what was I working on yesterday?"
- **Search Pieces** — "find my notes on RAG architecture"
- **Feed NEXUS** — paste relevant snippets directly into NEXUS governance docs

---

## NEXUS Governance Note

The Pieces MCP connection is **read-only context retrieval** from a local source.  
It falls under the NEXUS boundary rule: **Retrieval is not validation.**  
Content pulled from Pieces is `source_type: recall` until operator reviews and confirms it.

---

*Updated: 2026-05-06 — corrected MCP endpoint to official `/model_context_protocol/2025-03-26/mcp` path*  
*Active root: VS_CODE_NEXUS / NEXUS Base V1*
