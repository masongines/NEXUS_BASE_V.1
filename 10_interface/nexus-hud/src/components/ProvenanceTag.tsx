import type { FeedClass } from "@/types/hud";

const PROVENANCE = {
  LIVE: {
    label: "LIVE",
    dot: "bg-emerald-400",
    text: "text-emerald-300",
    ring: "ring-emerald-400/30",
    desc: "Real-time read from source",
  },
  OPERATOR_LOGGED: {
    label: "OPERATOR-LOGGED",
    dot: "bg-indigo-400",
    text: "text-indigo-300",
    ring: "ring-indigo-400/30",
    desc: "Manually logged by Sovereign Operator",
  },
  UNSOURCED: {
    label: "UNSOURCED",
    dot: "bg-amber-400",
    text: "text-amber-300",
    ring: "ring-amber-400/30",
    desc: "No API path — cannot verify",
  },
  STALE: {
    label: "STALE",
    dot: "bg-slate-500",
    text: "text-slate-400",
    ring: "ring-slate-500/30",
    desc: "Source exists but feed unfresh",
  },
} as const;

export function provenanceRing(feedClass: FeedClass): string {
  return PROVENANCE[feedClass].ring;
}

export function provenanceDot(feedClass: FeedClass): string {
  return PROVENANCE[feedClass].dot;
}

interface Props {
  feedClass: FeedClass;
  compact?: boolean;
}

export function ProvenanceTag({ feedClass, compact = false }: Props) {
  const p = PROVENANCE[feedClass];
  return (
    <span
      title={p.desc}
      className={`inline-flex items-center gap-1.5 rounded-sm border border-slate-800/80 bg-slate-900/60 px-1.5 py-0.5 font-mono text-[10px] uppercase tracking-[0.12em] ${p.text}`}
    >
      <span className={`h-1.5 w-1.5 rounded-full ${p.dot}`} />
      {compact ? p.label.slice(0, 4) : p.label}
    </span>
  );
}
