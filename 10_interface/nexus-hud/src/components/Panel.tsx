import type { ReactNode } from "react";
import { cn } from "@/lib/utils";

interface Props {
  title?: string;
  eyebrow?: string;
  action?: ReactNode;
  children: ReactNode;
  className?: string;
}

export function Panel({ title, eyebrow, action, children, className }: Props) {
  return (
    <section
      className={cn(
        "rounded-sm border border-slate-800/80 bg-slate-900/40 backdrop-blur-sm",
        className
      )}
    >
      {(title || eyebrow) && (
        <header className="flex items-center justify-between border-b border-slate-800/80 px-4 py-3">
          <div className="flex flex-col gap-0.5">
            {eyebrow && (
              <span className="font-mono text-[10px] uppercase tracking-[0.18em] text-slate-500">
                {eyebrow}
              </span>
            )}
            {title && <h3 className="text-sm font-medium text-slate-100">{title}</h3>}
          </div>
          {action}
        </header>
      )}
      <div className="p-4">{children}</div>
    </section>
  );
}
