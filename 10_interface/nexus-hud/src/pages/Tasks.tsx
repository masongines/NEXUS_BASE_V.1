import { useEffect, useState } from "react";
import { Plus } from "lucide-react";
import { Panel } from "@/components/Panel";
import { ProvenanceTag } from "@/components/ProvenanceTag";
import { getTasks } from "@/lib/api";
import type { TaskEntry } from "@/types/hud";

export function Tasks() {
  const [tasks, setTasks] = useState<TaskEntry[]>([]);

  useEffect(() => {
    void getTasks().then(setTasks);
  }, []);

  return (
    <Panel
      eyebrow="OPERATOR QUEUE"
      title={`Tasks — ${tasks.length} active`}
      action={
        <button
          type="button"
          disabled
          title="Write paths deferred to Stage 5"
          className="flex items-center gap-1 rounded-sm border border-indigo-400/30 bg-indigo-500/10 px-2 py-1 font-mono text-[10px] uppercase tracking-wider text-indigo-200 opacity-50"
        >
          <Plus className="h-3 w-3" /> New task
        </button>
      }
    >
      <ul className="space-y-3">
        {tasks.map((t) => (
          <li
            key={t.id}
            className="rounded-sm border border-slate-800/60 bg-slate-950/40 p-4"
          >
            <div className="flex items-start gap-3">
              <button
                type="button"
                disabled
                aria-label="Mark complete (Stage 5)"
                className="mt-0.5 h-4 w-4 flex-shrink-0 rounded-sm border border-slate-600 opacity-50"
              />
              <div className="flex-1">
                <h4 className="text-sm font-medium text-slate-100">{t.title}</h4>
                <p className="mt-1 text-xs leading-relaxed text-slate-400">{t.detail}</p>
                <div className="mt-3 flex items-center gap-2">
                  <span
                    className={`rounded-sm px-1.5 py-0.5 font-mono text-[9px] uppercase tracking-wider ${
                      t.priority === "HIGH"
                        ? "bg-amber-500/10 text-amber-300"
                        : "bg-indigo-500/10 text-indigo-300"
                    }`}
                  >
                    {t.priority}
                  </span>
                  <span className="font-mono text-[10px] uppercase tracking-wider text-slate-500">
                    → {t.owner}
                  </span>
                  <ProvenanceTag feedClass={t.feedClass} compact />
                </div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </Panel>
  );
}
