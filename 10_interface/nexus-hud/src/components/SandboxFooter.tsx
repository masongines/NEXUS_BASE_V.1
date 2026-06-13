import { AlertTriangle } from "lucide-react";

// CRITICAL: do not remove this footer without explicit operator approval.
// It is the visible NEXUS sandbox / draft indicator. The HUD must
// communicate its non-authoritative status at all times.

export function SandboxFooter() {
  return (
    <footer className="border-t border-slate-800/80 px-8 py-3">
      <div className="flex items-center justify-between font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
        <div className="flex items-center gap-2">
          <AlertTriangle className="h-3 w-3 text-amber-400/70" />
          <span>STATUS: DRAFT — Operator validation required before promotion</span>
        </div>
        <div className="flex items-center gap-4">
          <span>ACTIVE_ROOT: VS_CODE_NEXUS</span>
          <span>PROMOTION_AUTHORIZED: NO</span>
        </div>
      </div>
    </footer>
  );
}
