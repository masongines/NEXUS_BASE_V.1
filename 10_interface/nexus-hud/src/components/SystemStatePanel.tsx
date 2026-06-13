import type { FeedClass, SystemState } from "@/types/hud";
import { Panel } from "@/components/Panel";
import { ProvenanceTag } from "@/components/ProvenanceTag";
import { ShieldAlert } from "lucide-react";

// System State surface — visualizes the Phase-A reconciliation. NON-AUTHORITATIVE:
// it surfaces verified state but never becomes state. On conflict with workspace
// files, the files win (see the banner below + system_state.json `meta.authority`).

function StatCard({
  label,
  value,
  sub,
  feedClass,
}: {
  label: string;
  value: string;
  sub?: string;
  feedClass: FeedClass;
}) {
  return (
    <div className="rounded-sm border border-slate-800/60 bg-slate-950/40 p-4">
      <div className="mb-2 flex items-center justify-between">
        <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
          {label}
        </span>
        <ProvenanceTag feedClass={feedClass} compact />
      </div>
      <div className="text-2xl font-medium tracking-tight text-slate-100">{value}</div>
      {sub && <div className="mt-1 text-xs leading-relaxed text-slate-400">{sub}</div>}
    </div>
  );
}

export function SystemStatePanel({ state }: { state: SystemState }) {
  return (
    <div className="space-y-4">
      {/* Non-authoritative banner — the HUD is the interface plane */}
      <div className="flex items-start gap-3 rounded-sm border border-amber-400/30 bg-amber-500/5 p-4">
        <ShieldAlert className="mt-0.5 h-4 w-4 flex-shrink-0 text-amber-400/80" />
        <div>
          <div className="font-mono text-[10px] uppercase tracking-[0.18em] text-amber-300">
            Interface surface — non-authoritative
          </div>
          <p className="mt-1 text-xs leading-relaxed text-slate-300">{state.meta.authority}</p>
          <p className="mt-2 font-mono text-[10px] uppercase tracking-wider text-slate-500">
            Reconciled by {state.meta.reconciledBy} · {state.meta.reconciledOn} · HEAD{" "}
            {state.meta.gitHead} · {state.meta.snapshotClass}
          </p>
        </div>
      </div>

      {/* Stat grid */}
      <div className="grid grid-cols-4 gap-4">
        <StatCard
          label="Kernel"
          value={`v${state.kernel.version}`}
          sub={state.kernel.status}
          feedClass={state.kernel.feedClass}
        />
        <StatCard
          label="Doctrine files"
          value={String(state.doctrine.count)}
          sub={state.doctrine.note}
          feedClass={state.doctrine.feedClass}
        />
        <StatCard
          label="Co-Dev Protocol"
          value={`v${state.coDevProtocol.version}`}
          sub={state.coDevProtocol.status}
          feedClass={state.coDevProtocol.feedClass}
        />
        <StatCard
          label="War test (PASS/FAIL)"
          value={`${state.warTest.pass}/${state.warTest.fail}`}
          sub={`${state.warTest.verdict} · ${state.warTest.warn} WARN`}
          feedClass={state.warTest.feedClass}
        />
      </div>

      {/* Active standards — drift flagged STALE, surfaced not hidden */}
      <Panel
        eyebrow="ACTIVE STANDARDS"
        title={`${state.activeStandards.countOnDisk} on disk · manifest reports ${state.activeStandards.manifestCount}`}
        action={<ProvenanceTag feedClass={state.activeStandards.feedClass} />}
      >
        <p className="rounded-sm border-l-2 border-amber-400/50 bg-slate-950/40 p-3 text-xs leading-relaxed text-amber-200/90">
          {state.activeStandards.flag}
        </p>
        <p className="mt-2 font-mono text-[10px] uppercase tracking-wider text-slate-500">
          {state.activeStandards.source}
        </p>
      </Panel>

      <div className="grid grid-cols-2 gap-4">
        {/* ADRs */}
        <Panel eyebrow="DECISIONS" title="Architectural Decision Records">
          <ul className="space-y-2">
            {state.adrs.map((a) => (
              <li
                key={a.id}
                className="flex items-center justify-between rounded-sm border border-slate-800/60 bg-slate-950/40 px-3 py-2"
              >
                <div>
                  <span className="font-mono text-xs text-slate-300">{a.id}</span>
                  <span className="ml-2 text-sm text-slate-200">{a.title}</span>
                </div>
                <span
                  className={`font-mono text-[9px] uppercase tracking-wider ${
                    a.status === "ACCEPTED" ? "text-emerald-300" : "text-amber-300"
                  }`}
                >
                  {a.status}
                </span>
              </li>
            ))}
          </ul>
        </Panel>

        {/* Decision register */}
        <Panel eyebrow="OPEN DISCREPANCIES" title="Decision Register">
          <ul className="space-y-2">
            {state.decisionRegister.map((d) => (
              <li
                key={d.id}
                className="rounded-sm border border-slate-800/60 bg-slate-950/40 px-3 py-2"
              >
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs text-slate-300">{d.id}</span>
                  <span className="font-mono text-[9px] uppercase tracking-wider text-amber-300">
                    {d.status}
                  </span>
                </div>
                <div className="mt-1 text-sm text-slate-200">{d.title}</div>
              </li>
            ))}
          </ul>
        </Panel>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {/* Labs + excluded */}
        <Panel eyebrow="WORKING LABS" title="Active labs">
          <ul className="space-y-2">
            {state.labs.map((l) => (
              <li
                key={l.name}
                className="flex items-center justify-between rounded-sm border border-slate-800/60 bg-slate-950/40 px-3 py-2 text-sm"
              >
                <span className="text-slate-200">{l.name}</span>
                <span
                  className={`font-mono text-[9px] uppercase tracking-wider ${
                    l.state === "ACTIVE" ? "text-emerald-300" : "text-slate-400"
                  }`}
                >
                  {l.state}
                </span>
              </li>
            ))}
          </ul>
          <div className="mt-3 border-t border-slate-800/60 pt-3">
            <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
              Excluded
            </div>
            {state.excluded.map((e) => (
              <div key={e.name} className="text-xs leading-relaxed text-slate-400">
                <span className="text-slate-300">{e.name}</span> — {e.reason}
              </div>
            ))}
          </div>
        </Panel>

        {/* Entropy */}
        <Panel
          eyebrow="ENTROPY"
          title="Risk band"
          action={<ProvenanceTag feedClass={state.entropy.feedClass} />}
        >
          <div className="flex items-center gap-3">
            <span
              className={`h-3 w-3 rounded-full ${
                state.entropy.riskBand === "GREEN" ? "bg-emerald-400" : "bg-amber-400"
              }`}
            />
            <span className="text-2xl font-medium tracking-tight text-slate-100">
              {state.entropy.riskBand}
            </span>
          </div>
          <p className="mt-2 text-xs text-slate-400">{state.entropy.basis}</p>
          <p className="mt-2 font-mono text-[10px] uppercase tracking-wider text-slate-500">
            {state.entropy.source}
          </p>
        </Panel>
      </div>
    </div>
  );
}
