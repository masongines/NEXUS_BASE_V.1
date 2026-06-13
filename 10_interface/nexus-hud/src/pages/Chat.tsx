import { useEffect, useState } from "react";
import { Send } from "lucide-react";
import { Panel } from "@/components/Panel";
import { ProvenanceTag } from "@/components/ProvenanceTag";
import { getChatThread } from "@/lib/api";
import type { ChatMessage } from "@/types/hud";

export function Chat() {
  const [thread, setThread] = useState<ChatMessage[]>([]);
  const [draft, setDraft] = useState("");

  useEffect(() => {
    void getChatThread().then(setThread);
  }, []);

  // Stage 1: draft is local-only; no submission to nexus-api yet.
  // Stage 5: route through approval queue before logging.
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setDraft("");
  };

  return (
    <Panel
      eyebrow="COUNCIL CHANNEL"
      title="Operator log + council responses"
      action={
        <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
          async — not live chat
        </span>
      }
    >
      <div className="mb-4 max-h-[60vh] space-y-4 overflow-y-auto pr-2">
        {thread.map((msg) => {
          const isOp = msg.senderRole === "operator";
          return (
            <div key={msg.id} className={`flex ${isOp ? "justify-end" : "justify-start"}`}>
              <div className="max-w-[80%]">
                <div
                  className={`mb-1 flex items-center gap-2 ${
                    isOp ? "justify-end" : "justify-start"
                  }`}
                >
                  <span
                    className={`font-mono text-[10px] uppercase tracking-wider ${
                      isOp ? "text-indigo-300" : "text-slate-300"
                    }`}
                  >
                    {msg.sender}
                  </span>
                  <span className="font-mono text-[10px] text-slate-500">{msg.timestamp}</span>
                  <ProvenanceTag feedClass={msg.feedClass} compact />
                </div>
                <div
                  className={`rounded-sm border p-3 text-sm leading-relaxed ${
                    isOp
                      ? "border-indigo-400/30 bg-indigo-500/10 text-slate-100"
                      : "border-slate-800/60 bg-slate-950/40 text-slate-200"
                  }`}
                >
                  {msg.body}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2 border-t border-slate-800/80 pt-4">
        <input
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          placeholder="Log as Sovereign Operator… (Stage 5 will gate this through approval)"
          className="flex-1 rounded-sm border border-slate-800 bg-slate-950 px-3 py-2 text-sm text-slate-100 placeholder:text-slate-600 focus:border-indigo-400/50 focus:outline-none"
        />
        <button
          type="submit"
          className="flex items-center gap-1 rounded-sm border border-indigo-400/30 bg-indigo-500/10 px-3 py-2 text-sm font-medium text-indigo-200 hover:bg-indigo-500/20"
        >
          <Send className="h-3.5 w-3.5" /> Log
        </button>
      </form>
    </Panel>
  );
}
