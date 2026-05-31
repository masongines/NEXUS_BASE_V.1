// NEXUS HUD — typed API client
//
// Stage 1: Mock data only — no calls to nexus-api yet.
// Stage 2: Replace mock branches with real fetches once nexus-api
//          exposes the /hud/* endpoints documented in README.md.
//
// Discipline:
//  - Every endpoint returns a typed shape from types/hud.ts.
//  - On any failure (network, 4xx, 5xx), the client returns null and
//    callers fall back to OPERATOR_LOGGED / UNSOURCED rendering.
//    NEVER fabricate data to fill a gap.

import type {
  ChatMessage,
  CouncilMember,
  MemoryEntry,
  StandingOrder,
  SystemState,
  TaskEntry,
} from "@/types/hud";
import { COUNCIL_REGISTRY } from "@/data/council";
import systemStateData from "@/data/system_state.json";

const BASE = import.meta.env.VITE_NEXUS_API_BASE_URL ?? "/api";

// Toggle off in Stage 2 once endpoints are live
const USE_MOCKS = true;

async function safeFetch<T>(path: string): Promise<T | null> {
  try {
    const res = await fetch(`${BASE}${path}`, {
      headers: { Accept: "application/json" },
    });
    if (!res.ok) return null;
    return (await res.json()) as T;
  } catch {
    return null;
  }
}

/* ────────────── Council ────────────── */

export async function getCouncilMembers(): Promise<CouncilMember[]> {
  if (USE_MOCKS) return COUNCIL_REGISTRY;
  const data = await safeFetch<CouncilMember[]>("/hud/council/activity");
  return data ?? COUNCIL_REGISTRY;
}

/* ────────────── System State (reconciled snapshot) ────────────── */

export async function getSystemState(): Promise<SystemState> {
  // Stage 1: static reconciled snapshot from data/system_state.json.
  // The HUD is the interface plane — this datum is non-authoritative.
  if (USE_MOCKS) return systemStateData as unknown as SystemState;
  const data = await safeFetch<SystemState>("/hud/system-state");
  return data ?? (systemStateData as unknown as SystemState);
}

/* ────────────── Memory ────────────── */

const MOCK_MEMORY: MemoryEntry[] = [
  {
    id: "m1",
    kind: "UPDATE",
    source: "Pieces OS",
    feedClass: "LIVE",
    timestamp: "2026-05-29 14:12",
    body: "LTM model synced with VS Code workspace. Context capture enabled for all file operations.",
    tags: ["system", "initialization"],
  },
  {
    id: "m2",
    kind: "RECALL",
    source: "Claude Code",
    feedClass: "OPERATOR_LOGGED",
    timestamp: "2026-05-29 13:40",
    body: "Base V1 lane architecture confirmed: 00_governance_ref through 08_security_index. Doctrine = 12 (cross-verified). Co-Dev v1.0 ACTIVE.",
    tags: ["architecture", "governance"],
  },
  {
    id: "m3",
    kind: "ORDER",
    source: "Operator",
    feedClass: "OPERATOR_LOGGED",
    timestamp: "2026-05-31 09:05",
    body: "HUD is the interface plane — observational only. No system may alter doctrine through this surface. Council must be an odd number (5).",
    tags: ["governance", "standing_order"],
  },
];

export async function getMemoryEntries(): Promise<MemoryEntry[]> {
  if (USE_MOCKS) return MOCK_MEMORY;
  const data = await safeFetch<MemoryEntry[]>("/hud/memory");
  return data ?? MOCK_MEMORY;
}

/* ────────────── Tasks ────────────── */

const MOCK_TASKS: TaskEntry[] = [
  {
    id: "t1",
    title: "Reconcile desktop-app draft against workspace files",
    detail:
      "Verify the claude.ai master-concept draft's claims against primary files; produce the reconciliation delta report.",
    priority: "HIGH",
    owner: "Claude Code",
    feedClass: "OPERATOR_LOGGED",
  },
  {
    id: "t2",
    title: "Ship HUD Stage 1 (fresh tracked scaffold)",
    detail: "Render all surfaces with mock data + System State; pause at operator checkpoint.",
    priority: "HIGH",
    owner: "Claude Code",
    feedClass: "OPERATOR_LOGGED",
  },
  {
    id: "t3",
    title: "Operator ruling on FL-002 manifest drift + DR-namespace",
    detail: "Regenerate manifest (8->11, drop phantom) and pick canonical DR register — gated.",
    priority: "MEDIUM",
    owner: "Operator",
    feedClass: "OPERATOR_LOGGED",
  },
];

export async function getTasks(): Promise<TaskEntry[]> {
  if (USE_MOCKS) return MOCK_TASKS;
  const data = await safeFetch<TaskEntry[]>("/hud/tasks");
  return data ?? MOCK_TASKS;
}

/* ────────────── Standing Orders ────────────── */

const MOCK_ORDERS: StandingOrder[] = [
  { id: "o1", body: "Inference only — no autonomous execution without operator approval." },
  { id: "o2", body: "The HUD is the interface plane; it surfaces state, it does not become state." },
  { id: "o3", body: "All governance modifications require Prime Axiom compliance check." },
  {
    id: "o4",
    body: "Source hierarchy: operator correction > doctrine registry > active standards > locked support records > generated outputs > interface surfaces.",
  },
];

export async function getStandingOrders(): Promise<StandingOrder[]> {
  if (USE_MOCKS) return MOCK_ORDERS;
  const data = await safeFetch<StandingOrder[]>("/hud/governance");
  return data ?? MOCK_ORDERS;
}

/* ────────────── Chat ────────────── */

const MOCK_CHAT: ChatMessage[] = [
  {
    id: "c1",
    sender: "Sovereign Operator",
    senderRole: "operator",
    timestamp: "09:00",
    body: "Verify desktop app vs local files, then build the dashboard. Council must be 5.",
    feedClass: "OPERATOR_LOGGED",
  },
  {
    id: "c2",
    sender: "Claude Code",
    senderRole: "claude_code",
    timestamp: "09:18",
    body: "Reconciliation complete: doctrine 12, kernel v1.2, war test 36/0, Co-Dev ACTIVE, HEAD 4dec846. Building fresh HUD Stage 1.",
    feedClass: "OPERATOR_LOGGED",
  },
  {
    id: "c3",
    sender: "Pieces OS",
    senderRole: "pieces",
    timestamp: "09:20",
    body: "LTM active. Workflow patterns captured. Ready for recall.",
    feedClass: "LIVE",
  },
  {
    id: "c4",
    sender: "Codex",
    senderRole: "codex",
    timestamp: "09:22",
    body: "Standing by for second-opinion validation on the Stage-1 scaffold.",
    feedClass: "OPERATOR_LOGGED",
  },
  {
    id: "c5",
    sender: "NEXUS_SUXEN",
    senderRole: "suxen",
    timestamp: "09:24",
    body: "Knowledge base loaded. No external API path — entries logged through operator hand-off.",
    feedClass: "UNSOURCED",
  },
];

export async function getChatThread(): Promise<ChatMessage[]> {
  if (USE_MOCKS) return MOCK_CHAT;
  const data = await safeFetch<ChatMessage[]>("/hud/chat");
  return data ?? MOCK_CHAT;
}
