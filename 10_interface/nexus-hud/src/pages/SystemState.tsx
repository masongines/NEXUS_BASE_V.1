import { useEffect, useState } from "react";
import { SystemStatePanel } from "@/components/SystemStatePanel";
import { getSystemState } from "@/lib/api";
import type { SystemState } from "@/types/hud";

export function SystemStateView() {
  const [state, setState] = useState<SystemState | null>(null);

  useEffect(() => {
    void getSystemState().then(setState);
  }, []);

  if (!state) {
    return <div className="text-sm text-slate-500">Loading reconciled state…</div>;
  }

  return <SystemStatePanel state={state} />;
}
