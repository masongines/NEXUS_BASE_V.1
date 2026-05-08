# NEXUS Base V1 — Demonstration Pack

> **Status:** Draft. First creative pass. Designed to be edited, swapped, or replaced piece-by-piece without breaking the others.

This folder contains everything needed to present, narrate, or record a walkthrough of NEXUS Base V1: the **governance-first execution pipeline**, the **war test**, the **four-lens review council**, and the **operator companion app**.

---

## What's in here

| File | What it is | How to open |
|---|---|---|
| **`index.html`** | The main keynote — a 4-act cinematic Reveal.js deck with embedded Mermaid diagrams, real code snippets, and a live forensic exhibit from `threat_log.txt`. | Double-click → opens in browser. Use arrow keys / `Space` to advance. `S` opens speaker notes. |
| **`war_test_replay.html`** | Standalone CRT-terminal animation that plays back all 36 war-test cases line by line, with live PASS/WARN/FAIL counters and a verdict overlay. | Double-click → press `Run`. `Space` toggles play/pause. Speed selector top-right. |
| **`council_review_demo.html`** | A scrollable visual storyboard of one action travelling through the 4-lens review council (Vault / Researcher / Engineer / Nexus Core), the Hub classifier, and the operator gate. | Double-click → scroll. Static — no controls. |
| **`DOCUMENTARY_SCRIPT.md`** | A 5-act narrated script designed to be read aloud over the deck or recorded as voiceover. ~14-minute runtime. | Open in any markdown reader. |
| **`DIRECTOR_NOTES.md`** | Live cue sheet, talking points by slide, anticipated Q&A, failure recovery, and short / long variants of the talk. | Open in any markdown reader. |

All HTML files are **self-contained** — they pull Reveal.js and Mermaid from CDN but ship no local dependencies. You can drop the folder onto a USB stick or a static host (GitHub Pages, Netlify drop, `python -m http.server`) and present immediately.

---

## How to deliver the demo

### One-minute version
Show the deck. Show the verdict. Done.

### Five-minute version
Run `index.html` end-to-end at fade pace. Skip the per-stage pipeline slides and the limitations section.

### Fourteen-minute version
Run `index.html` with the documentary narration. Cut to `war_test_replay.html` between Act III and Act IV. Cut to `council_review_demo.html` between Acts IV and V. Return to the deck for the closer.

### Twenty-minute (technical) version
Add a live `python nexus_war_test.py` in a real terminal between Acts II and III. Walk through `executor.py` on the security-before-trust slide. Tail `threat_log.txt` from a shell.

See `DIRECTOR_NOTES.md` for cue timing.

---

## Theme and aesthetic

- **Palette:** deep navy (`#07090f`) ground, cyan (`#00d4ff`) signal, red (`#ff4757`) threat, green (`#00ff88`) trust, amber (`#ffa502`) caution, violet (`#b794f6`) governance.
- **Typography:** Inter for headers, JetBrains Mono for code and HUD chrome.
- **Visual motif:** schematic blueprint grid + soft CRT scanlines on the terminal replay. Reads as a control-panel HUD, not a marketing deck.
- **Tone:** *Halt and Catch Fire*, not *product launch*. Quiet, deliberate, evidence-led.

---

## Editing this pack

Each file is independent. To swap a section:

- **Re-time the war-test playback:** edit `TIMELINE` in the `<script>` block of `war_test_replay.html`. Each entry corresponds to one console line.
- **Change the council scenario:** edit the action card and lens quotes in `council_review_demo.html`. The four lenses and the verdict pills are CSS classes — restyle without touching layout.
- **Reorder the deck:** every slide in `index.html` is a `<section>`. Move them around freely; Reveal.js handles ordering by DOM order.
- **Rewrite the narration:** `DOCUMENTARY_SCRIPT.md` maps scene-by-scene to the deck. Keep the act headers if you want the cue sheet in `DIRECTOR_NOTES.md` to keep working.

No build step. No `npm install`. Reload the browser to see edits.

---

## Source material

This pack was assembled from the live state of the repository on the `claude/review-testing-presentation-dmaeO` branch:

- `README.md` — at-a-glance facts, validation result, classification.
- `NEXUS_BASE_V1_DEEP_DIVE.md` — the 16-section architecture explanation. Most of the documentary script's structure mirrors this document's structure.
- `CAPSTONE_PAPER.md` — abstract and scope.
- `nexus_war_test.py` — the actual 36-case war-test runner; suite names and counter shape come directly from this file.
- `01_core/execution/executor.py` — the execution pipeline; the security-before-trust ordering is verified against this file's source.
- `01_core/execution/security/security_monitor.py` — the 12-line `detect_threat()` function quoted on the security slide.
- `02_config/execution_trust_registry.json` — the trust registry shown on the trust-data slide.
- `04_logs/security/threat_log.txt` — the forensic exhibit shown verbatim (timestamps preserved).

If any of those source files change, the deck and replay should be updated to match. The forensic exhibit slide in particular should never be edited in a way that diverges from `threat_log.txt`.

---

## Companion deck (mobile)

A second, mobile-first companion deck lives in the **`nexus-council-mobile`** repository on the same branch (`claude/review-testing-presentation-dmaeO`). It tells the operator-side of the story — what approving an action looks like from a phone — and is designed to be presented as a follow-on after this deck's Act IV.

---

## Credits

NEXUS Base V1 — Mason Gines — Apache 2.0 — 2026.
Demonstration pack drafted on `claude/review-testing-presentation-dmaeO`. Edit, replace, or rewrite freely.
