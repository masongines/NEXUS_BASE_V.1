// NEXUS Council registry — governance metadata only.
//
// Source: NEXUS doctrine (council member governance roles).
// This file is the canonical client-side reference for what each
// member IS and what authority class they hold. Do not modify
// without operator approval per NEXUS source hierarchy.
//
// Roster = 5 (operator ruling 2026-05-31: council must be an odd number).
// IBM "Bob" is a non-voting trial auditor (read-only) and is intentionally
// NOT a standing council member.

import type { CouncilMember } from "@/types/hud";

export const COUNCIL_REGISTRY: CouncilMember[] = [
  {
    id: "claude",
    initials: "CL",
    name: "Claude",
    role: "Architect & Orchestrator",
    summary:
      "Primary LLM for system design, governance analysis, and structured reasoning. Operates as lead advisor under operator authority (claude.ai seat).",
    capabilities: [
      "System Architecture",
      "Governance Analysis",
      "Review",
      "Documentation",
      "Structured Reasoning",
    ],
    governance:
      "Lead Advisor — proposes, does not decide. All outputs require operator verification per Prime Axiom.",
    feedClass: "OPERATOR_LOGGED",
    lastActivity: "Session active",
  },
  {
    id: "claude_code",
    initials: "CC",
    name: "Claude Code",
    role: "Primary Implementation",
    summary:
      "The hands at the workspace — writes and edits code/files under operator direction. Workspace-reachable seat; authored the reconciliation report.",
    capabilities: [
      "Implementation",
      "File Operations",
      "Workspace Verification",
      "Build & Test",
      "Tier-1 Ceremony",
    ],
    governance:
      "Primary Implementation — executes only operator-approved tasks. Cannot modify governance or promote outputs to authority.",
    feedClass: "OPERATOR_LOGGED",
    lastActivity: "Local-work session — HUD Stage 1",
  },
  {
    id: "codex",
    initials: "CO",
    name: "Codex",
    role: "Second Opinion",
    summary:
      "Independent cross-check within VS Code. Provides second-opinion validation, bug analysis, and implementation support.",
    capabilities: ["Cross-Check", "Bug Analysis", "Refactoring", "Testing", "Second Opinion"],
    governance:
      "Implementation Support — executes under operator direction. Cannot modify governance or promote outputs.",
    feedClass: "OPERATOR_LOGGED",
    lastActivity: "VS Code session — last edit logged",
  },
  {
    id: "pieces",
    initials: "PI",
    name: "Pieces OS",
    role: "Long-Term Memory & Context",
    summary:
      "LTM layer. Captures, manages, and provides context through code snippets, screenshots, and workflow data via the Pieces local API.",
    capabilities: [
      "Long-Term Memory",
      "Context Capture",
      "Workflow Tracking",
      "Code Snippets",
      "Recall",
    ],
    governance:
      "Memory Layer — observational (Plane 3, ADR-004). Provides recall and context but holds no governance authority.",
    feedClass: "LIVE",
    lastActivity: "Pieces local API reachable",
  },
  {
    id: "suxen",
    initials: "NX",
    name: "NEXUS_SUXEN",
    role: "Verifier & Knowledge Base",
    summary:
      "Local knowledge project. Serves as a verification layer and knowledge set for cross-referencing council outputs. No external API path.",
    capabilities: [
      "Verification",
      "Knowledge Base",
      "Cross-Reference",
      "Historical Context",
      "Pattern Analysis",
    ],
    governance:
      "Verifier — validates outputs against established knowledge. Cannot override operator decisions.",
    feedClass: "UNSOURCED",
    lastActivity: "No external API — operator-logged only",
  },
];
