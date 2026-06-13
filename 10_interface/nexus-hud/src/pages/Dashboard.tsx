import { useEffect, useState } from "react";
import { Shield } from "lucide-react";
import { Panel } from "@/components/Panel";
import { ProvenanceTag } from "@/components/ProvenanceTag";
import { CouncilAvatar } from "@/components/CouncilAvatar";
import {
  getCouncilMembers,
  getMemoryEntries,
  getStandingOrders,
  getTasks,
} from "@/lib/api";
import type {
  CouncilMember,
  MemoryEntry,
  StandingOrder,
  TaskEntry,
} from "@/types/hud";

export function Dashboard() {
  const [council, setCouncil] = useState<CouncilMember[]>([]);
  const [orders, setOrders] = useState<StandingOrder[]>([]);
  const [tasks, setTasks] = useState<TaskEntry[]>([]);
  const [memory, setMemory] = useState<MemoryEntry[]>([]);

  useEffect(() => {
    void Promise.all([
      getCouncilMembers(),
      getStandingOrders(),
      getTasks(),
      getMemoryEntries(),
    ]).then(([c, o, t, m]) => {
      setCouncil(c);
      setOrders(o);
      setTasks(t);
      setMemory(m);
    });
  }, []);

  return (
    <div className="grid grid-cols-12 gap-4">
      <Panel
        eyebrow="COUNCIL STATUS"
        title="AI system roster"
        action={
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
            {council.length} members
          </span>
        }
        className="col-span-12"
      >
        <div className="grid grid-cols-5 gap-4">
          {council.map((m) => (
            <div
              key={m.id}
              className="flex flex-col items-center gap-2 rounded-sm border border-slate-800/60 bg-slate-950/40 p-4"
            >
              <CouncilAvatar member={m} size="lg" />
              <div className="text-sm font-medium text-slate-100">{m.name}</div>
              <ProvenanceTag feedClass={m.feedClass} />
              <div className="text-center font-mono text-[10px] uppercase tracking-wider text-slate-500">
                {m.lastActivity}
              </div>
            </div>
          ))}
        </div>
      </Panel>

      <Panel
        eyebrow="DOCTRINE"
        title="Standing Orders"
        action={<Shield className="h-4 w-4 text-amber-400/70" />}
        className="col-span-7"
      >
        <ul className="space-y-3">
          {orders.map((o) => (
            <li key={o.id} className="flex gap-3 text-sm leading-relaxed text-slate-300">
              <span className="mt-1.5 h-1 w-1 flex-shrink-0 rounded-full bg-amber-400/80" />
              {o.body}
            </li>
          ))}
        </ul>
      </Panel>

      <Panel
        eyebrow="QUEUE"
        title="Active Tasks"
        action={
          <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-indigo-300">
            {tasks.length} active
          </span>
        }
        className="col-span-5"
      >
        <ul className="space-y-3">
          {tasks.map((t) => (
            <li
              key={t.id}
              className="rounded-sm border border-slate-800/60 bg-slate-950/40 p-3"
            >
              <div className="flex items-start justify-between gap-2">
                <span className="text-sm leading-snug text-slate-200">{t.title}</span>
                <span
                  className={`font-mono text-[9px] uppercase tracking-wider ${
                    t.priority === "HIGH" ? "text-amber-300" : "text-slate-400"
                  }`}
                >
                  {t.priority}
                </span>
              </div>
              <div className="mt-2 flex items-center gap-2 font-mono text-[10px] uppercase tracking-wider text-slate-500">
                <span>→ {t.owner}</span>
              </div>
            </li>
          ))}
        </ul>
      </Panel>

      <Panel
        eyebrow="LTM"
        title="Recent Memory"
        className="col-span-12"
      >
        <div className="grid grid-cols-3 gap-3">
          {memory.map((entry) => (
            <article
              key={entry.id}
              className="rounded-sm border border-slate-800/60 bg-slate-950/40 p-3"
            >
              <div className="mb-2 flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span
                    className={`font-mono text-[9px] uppercase tracking-wider ${
                      entry.kind === "ORDER"
                        ? "text-amber-300"
                        : entry.kind === "RECALL"
                        ? "text-indigo-300"
                        : "text-emerald-300"
                    }`}
                  >
                    {entry.kind}
                  </span>
                  <span className="text-xs text-slate-400">{entry.source}</span>
                </div>
                <ProvenanceTag feedClass={entry.feedClass} compact />
              </div>
              <p className="mb-2 text-xs leading-relaxed text-slate-300">{entry.body}</p>
              <div className="flex items-center justify-between font-mono text-[10px] uppercase tracking-wider text-slate-500">
                <span>{entry.timestamp}</span>
                <span>#{entry.tags.join(" #")}</span>
              </div>
            </article>
          ))}
        </div>
      </Panel>
    </div>
  );
}
