import { useEffect, useState } from "react";
import { Panel } from "@/components/Panel";
import { ProvenanceTag } from "@/components/ProvenanceTag";
import { CouncilAvatar } from "@/components/CouncilAvatar";
import { getCouncilMembers } from "@/lib/api";
import type { CouncilMember } from "@/types/hud";

export function Council() {
  const [members, setMembers] = useState<CouncilMember[]>([]);

  useEffect(() => {
    void getCouncilMembers().then(setMembers);
  }, []);

  return (
    <div className="grid grid-cols-2 gap-4">
      {members.map((m) => (
        <Panel
          key={m.id}
          eyebrow={m.role.toUpperCase()}
          title={m.name}
          action={<ProvenanceTag feedClass={m.feedClass} />}
        >
          <div className="flex gap-4">
            <CouncilAvatar member={m} size="lg" />
            <div className="flex-1">
              <p className="text-sm leading-relaxed text-slate-300">{m.summary}</p>
            </div>
          </div>

          <div className="mt-4 border-t border-slate-800/60 pt-4">
            <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
              Capabilities
            </div>
            <div className="flex flex-wrap gap-1.5">
              {m.capabilities.map((c) => (
                <span
                  key={c}
                  className="rounded-sm border border-indigo-400/20 bg-indigo-500/5 px-2 py-0.5 text-[11px] text-indigo-200"
                >
                  {c}
                </span>
              ))}
            </div>
          </div>

          <div className="mt-4 border-t border-slate-800/60 pt-4">
            <div className="mb-2 font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
              Governance Role
            </div>
            <p className="rounded-sm border-l-2 border-amber-400/50 bg-slate-950/40 p-3 text-xs leading-relaxed text-slate-300">
              {m.governance}
            </p>
          </div>
        </Panel>
      ))}
    </div>
  );
}
