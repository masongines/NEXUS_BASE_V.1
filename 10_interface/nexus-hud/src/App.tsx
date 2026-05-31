import { useState } from "react";
import { Activity, Database } from "lucide-react";
import type { ViewId } from "@/types/hud";
import { NavRail } from "@/components/NavRail";
import { SandboxFooter } from "@/components/SandboxFooter";
import { Dashboard } from "@/pages/Dashboard";
import { SystemStateView } from "@/pages/SystemState";
import { Council } from "@/pages/Council";
import { Memory } from "@/pages/Memory";
import { Tasks } from "@/pages/Tasks";
import { Chat } from "@/pages/Chat";

const TITLES: Record<ViewId, { eyebrow: string; title: string }> = {
  dashboard: { eyebrow: "MISSION CONTROL", title: "NEXUS Council" },
  system: { eyebrow: "RECONCILED STATE", title: "System State" },
  council: { eyebrow: "ROSTER", title: "Council Members" },
  memory: { eyebrow: "LTM", title: "Memory" },
  tasks: { eyebrow: "QUEUE", title: "Tasks" },
  chat: { eyebrow: "CHANNEL", title: "Council Chat" },
};

export default function App() {
  const [view, setView] = useState<ViewId>("dashboard");
  const meta = TITLES[view];

  return (
    <div className="min-h-screen bg-slate-950 font-sans text-slate-100">
      <div className="pointer-events-none fixed inset-0 grid-bg opacity-[0.04]" />

      <div className="relative flex min-h-screen">
        <NavRail current={view} onChange={setView} />

        <main className="flex flex-1 flex-col overflow-hidden">
          <header className="sticky top-0 z-10 border-b border-slate-800/80 bg-slate-950/80 px-8 py-5 backdrop-blur-md">
            <div className="flex items-end justify-between">
              <div>
                <div className="font-mono text-[10px] uppercase tracking-widest2 text-slate-500">
                  {meta.eyebrow}
                </div>
                <h1 className="text-2xl font-medium tracking-tight text-slate-100">
                  {meta.title}
                </h1>
              </div>
              <div className="flex items-center gap-4 font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
                <div className="flex items-center gap-1.5">
                  <Database className="h-3 w-3" />
                  <span>nexus-api :8000</span>
                  <span className="h-1.5 w-1.5 rounded-full bg-slate-500" title="Not yet wired" />
                </div>
                <div className="flex items-center gap-1.5">
                  <Activity className="h-3 w-3" />
                  <span>nexus-node-01</span>
                  <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
                </div>
              </div>
            </div>
          </header>

          <div className="flex-1 overflow-y-auto px-8 py-6">
            {view === "dashboard" && <Dashboard />}
            {view === "system" && <SystemStateView />}
            {view === "council" && <Council />}
            {view === "memory" && <Memory />}
            {view === "tasks" && <Tasks />}
            {view === "chat" && <Chat />}
          </div>

          <SandboxFooter />
        </main>
      </div>
    </div>
  );
}
