import { useEffect, useState } from "react";
import { Plus } from "lucide-react";
import { Panel } from "@/components/Panel";
import { ProvenanceTag } from "@/components/ProvenanceTag";
import { getMemoryEntries } from "@/lib/api";
import type { MemoryEntry } from "@/types/hud";

export function Memory() {
  const [entries, setEntries] = useState<MemoryEntry[]>([]);

  useEffect(() => {
    void getMemoryEntries().then(setEntries);
  }, []);

  return (
    <Panel
      eyebrow="LONG-TERM CONTEXT"
      title="Memory log"
      action={
        <button
          type="button"
          disabled
          title="Write paths deferred to Stage 5"
          className="flex items-center gap-1 rounded-sm border border-indigo-400/30 bg-indigo-500/10 px-2 py-1 font-mono text-[10px] uppercase tracking-wider text-indigo-200 opacity-50"
        >
          <Plus className="h-3 w-3" /> Log entry
        </button>
      }
    >
      <div className="space-y-3">
        {entries.map((entry) => (
          <article
            key={entry.id}
            className="rounded-sm border border-slate-800/60 bg-slate-950/40 p-4"
          >
            <header className="mb-3 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span
                  className={`rounded-sm px-2 py-0.5 font-mono text-[10px] uppercase tracking-wider ${
                    entry.kind === "ORDER"
                      ? "bg-amber-500/10 text-amber-300"
                      : entry.kind === "RECALL"
                      ? "bg-indigo-500/10 text-indigo-300"
                      : "bg-emerald-500/10 text-emerald-300"
                  }`}
                >
                  {entry.kind}
                </span>
                <span className="text-sm font-medium text-slate-200">{entry.source}</span>
                <ProvenanceTag feedClass={entry.feedClass} />
              </div>
              <span className="font-mono text-[10px] uppercase tracking-wider text-slate-500">
                {entry.timestamp}
              </span>
            </header>
            <p className="mb-3 text-sm leading-relaxed text-slate-200">{entry.body}</p>
            <div className="flex gap-2">
              {entry.tags.map((t) => (
                <span
                  key={t}
                  className="font-mono text-[10px] uppercase tracking-wider text-slate-500"
                >
                  #{t}
                </span>
              ))}
            </div>
          </article>
        ))}
      </div>
    </Panel>
  );
}
