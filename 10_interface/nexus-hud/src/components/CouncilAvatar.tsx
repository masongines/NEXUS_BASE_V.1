import type { CouncilMember } from "@/types/hud";
import { provenanceDot, provenanceRing } from "./ProvenanceTag";
import { cn } from "@/lib/utils";

interface Props {
  member: CouncilMember;
  size?: "md" | "lg";
}

export function CouncilAvatar({ member, size = "md" }: Props) {
  const dim = size === "lg" ? "h-12 w-12 text-sm" : "h-9 w-9 text-xs";
  return (
    <div className="relative">
      <div
        className={cn(
          "flex items-center justify-center rounded-full border border-slate-700 bg-slate-900 font-mono font-medium text-slate-200 ring-2",
          dim,
          provenanceRing(member.feedClass)
        )}
      >
        {member.initials}
      </div>
      <span
        className={cn(
          "absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full ring-2 ring-slate-950",
          provenanceDot(member.feedClass)
        )}
      />
    </div>
  );
}
