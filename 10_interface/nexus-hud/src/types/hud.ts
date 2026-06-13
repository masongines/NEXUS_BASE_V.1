// NEXUS HUD — shared types
//
// FeedClass governs the visible provenance badge on the HUD.
// Never invent values not present here.

export type FeedClass = "LIVE" | "OPERATOR_LOGGED" | "UNSOURCED" | "STALE";

export type ViewId = "dashboard" | "council" | "memory" | "tasks" | "chat" | "system";

export interface CouncilMember {
  id: string;
  initials: string;
  name: string;
  role: string;
  summary: string;
  capabilities: string[];
  governance: string;
  feedClass: FeedClass;
  lastActivity: string;
}

export interface MemoryEntry {
  id: string;
  kind: "UPDATE" | "RECALL" | "ORDER";
  source: string;
  feedClass: FeedClass;
  timestamp: string;
  body: string;
  tags: string[];
}

export interface TaskEntry {
  id: string;
  title: string;
  detail: string;
  priority: "HIGH" | "MEDIUM" | "LOW";
  owner: string;
  feedClass: FeedClass;
  done?: boolean;
}

export interface ChatMessage {
  id: string;
  sender: string;
  senderRole: "operator" | "claude" | "claude_code" | "codex" | "pieces" | "suxen";
  timestamp: string;
  body: string;
  feedClass: FeedClass;
}

export interface StandingOrder {
  id: string;
  body: string;
}

/* ───────────── System State (reconciled snapshot — interface plane only) ─────────────
 *
 * This is the Phase-A reconciliation rendered as a read-only surface. It is
 * NON-AUTHORITATIVE: it visualizes verified state but never becomes state. On any
 * conflict with doctrine, ADRs, registers, or workspace files, the files win.
 * Source of truth: 00_governance_ref/staged_reviews/NEXUS_MASTER_CONCEPT_RECONCILIATION_v0.1.md
 */

export interface AdrEntry {
  id: string;
  title: string;
  status: string;
}

export interface DrEntry {
  id: string;
  title: string;
  status: string;
}

export interface LabEntry {
  name: string;
  state: string;
}

export interface ExcludedEntry {
  name: string;
  reason: string;
}

export interface SystemState {
  meta: {
    title: string;
    authority: string;
    reconciledBy: string;
    reconciledOn: string;
    gitHead: string;
    snapshotClass: string;
  };
  kernel: { version: string; status: string; feedClass: FeedClass; source: string };
  doctrine: { count: number; feedClass: FeedClass; source: string; note: string };
  coDevProtocol: { version: string; status: string; feedClass: FeedClass; source: string };
  warTest: {
    pass: number;
    warn: number;
    fail: number;
    verdict: string;
    feedClass: FeedClass;
    source: string;
  };
  activeStandards: {
    countOnDisk: number;
    manifestCount: number;
    feedClass: FeedClass;
    flag: string;
    source: string;
  };
  adrs: AdrEntry[];
  decisionRegister: DrEntry[];
  labs: LabEntry[];
  excluded: ExcludedEntry[];
  entropy: { riskBand: string; basis: string; feedClass: FeedClass; source: string };
}
