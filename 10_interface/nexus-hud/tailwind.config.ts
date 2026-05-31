import type { Config } from "tailwindcss";

export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Sans"', "ui-sans-serif", "system-ui", "sans-serif"],
        mono: ['"IBM Plex Mono"', "ui-monospace", "SFMono-Regular", "Menlo", "monospace"],
      },
      colors: {
        // Provenance accent tokens — referenced by ProvenanceTag and others
        provenance: {
          live: "#34d399", // emerald-400
          operator: "#818cf8", // indigo-400
          unsourced: "#fbbf24", // amber-400
          stale: "#64748b", // slate-500
        },
      },
      letterSpacing: {
        widest2: "0.2em",
      },
    },
  },
  plugins: [],
} satisfies Config;
