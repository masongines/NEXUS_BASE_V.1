import {
  LayoutDashboard,
  Users,
  Cpu,
  ListChecks,
  MessageSquareText,
  Gauge,
  ChevronRight,
  Hexagon,
  Lock,
} from "lucide-react";
import type { ViewId } from "@/types/hud";
import { cn } from "@/lib/utils";

const NAV: { id: ViewId; label: string; icon: typeof LayoutDashboard }[] = [
  { id: "dashboard", label: "Dashboard", icon: LayoutDashboard },
  { id: "system", label: "System State", icon: Gauge },
  { id: "council", label: "Council", icon: Users },
  { id: "memory", label: "Memory", icon: Cpu },
  { id: "tasks", label: "Tasks", icon: ListChecks },
  { id: "chat", label: "Chat", icon: MessageSquareText },
];

interface Props {
  current: ViewId;
  onChange: (v: ViewId) => void;
}

export function NavRail({ current, onChange }: Props) {
  return (
    <aside className="flex w-60 flex-col border-r border-slate-800/80 bg-slate-950/80 backdrop-blur-sm">
      <div className="border-b border-slate-800/80 p-5">
        <div className="flex items-center gap-2.5">
          <div className="relative">
            <Hexagon className="h-7 w-7 text-indigo-400" strokeWidth={1.5} />
            <Hexagon
              className="absolute inset-0 h-7 w-7 rotate-[30deg] text-indigo-400/40"
              strokeWidth={1.5}
            />
          </div>
          <div>
            <div className="font-mono text-[10px] uppercase tracking-widest2 text-slate-500">
              NEXUS
            </div>
            <div className="text-sm font-medium text-slate-100">Operator HUD</div>
          </div>
        </div>
      </div>

      <nav className="flex-1 p-3">
        {NAV.map((item) => {
          const Icon = item.icon;
          const active = current === item.id;
          return (
            <button
              key={item.id}
              onClick={() => onChange(item.id)}
              className={cn(
                "mb-1 flex w-full items-center gap-3 rounded-sm px-3 py-2 text-sm transition-colors",
                active
                  ? "border border-indigo-400/30 bg-indigo-500/10 text-indigo-100"
                  : "border border-transparent text-slate-400 hover:bg-slate-900 hover:text-slate-200"
              )}
            >
              <Icon className="h-4 w-4" strokeWidth={1.75} />
              <span className="flex-1 text-left">{item.label}</span>
              {active && <ChevronRight className="h-3 w-3" />}
            </button>
          );
        })}
      </nav>

      <div className="border-t border-slate-800/80 p-3">
        <div className="rounded-sm border border-slate-800/60 bg-slate-900/40 p-3">
          <div className="mb-2 flex items-center gap-2">
            <div className="flex h-7 w-7 items-center justify-center rounded-full bg-indigo-500/20 font-mono text-xs text-indigo-300">
              SO
            </div>
            <div>
              <div className="text-xs font-medium text-slate-100">Sovereign Operator</div>
              <div className="font-mono text-[9px] uppercase tracking-wider text-slate-500">
                Prime Axiom authority
              </div>
            </div>
          </div>
          <div className="flex items-center gap-1.5 font-mono text-[9px] uppercase tracking-wider text-emerald-300">
            <Lock className="h-2.5 w-2.5" /> Active session
          </div>
        </div>
      </div>
    </aside>
  );
}
