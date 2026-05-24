# Director's Notes — NEXUS Base V1 Demonstration

> Reference card for delivering the full demo pack live. Keep this open on a second screen during the talk.

---

## Pack Overview

| Asset | Purpose | Runtime |
|---|---|---|
| `index.html` | Cinematic 4-act Reveal.js deck. Main keynote surface. | ~12–14 min narrated |
| `war_test_replay.html` | Animated CRT-terminal playback of all 36 war-test cases. Press `Space` to play / pause. | ~45 sec on "Normal" |
| `council_review_demo.html` | Visual storyboard of one action travelling through the 4-lens council. Static — scroll to advance frames. | ~2 min walkthrough |
| `DOCUMENTARY_SCRIPT.md` | Full narration in 5 acts with scene-by-scene breakdown. Use as voiceover or speaker notes. | 14 min read |

---

## Pre-Flight (do this once, before showing anything)

1. Open all three HTMLs in separate browser tabs. Same window. Tab order: deck → replay → council.
2. In the deck, press `S` to open speaker notes in a second window if you have a second monitor.
3. In the replay, set the playback speed dropdown to **Cinematic**. Click `Run` once and immediately pause — this loads the buffer so the first card renders without a flicker.
4. In the council storyboard, scroll to top.
5. Hide your dock / taskbar. The dark theme assumes a clean black canvas.
6. Browser zoom — `Cmd/Ctrl =` once or twice if presenting on a large screen.
7. Do not present in low light without dimming your monitor brightness one notch — the cyan glows and the slide bottoms can clip on bright displays.

---

## Live Cue Sheet

```
ACT 0 — COLD OPEN                           (deck, slide 1)
  hold the silence ~3 seconds before saying anything

ACT I — THE QUESTION                        (deck, slides 2–6)
  - the "compare" slide is the first one to point at; let it land
  - the 36 / 0 / 0 stat is your flag-plant — say "we'll prove this"

ACT II — THE SYSTEM                         (deck, slides 7–17)
  - on the architecture slide, wait for the diagram to render before talking
  - on the "security overrides trust" slide, slow down — this is the doctrine

>>> CUE 1: switch tab to war_test_replay.html
       press "Run", playback speed = Cinematic
       narrate during playback (use Documentary Scene 11–14)
       when verdict overlay appears, press ESC and switch back

ACT III — THE PROOF                         (deck, slides 18–22)
  - the forensic exhibit slide is the strongest evidence — pause here

>>> CUE 2: switch tab to council_review_demo.html
       scroll down once per frame (6 frames total)
       point to the verdict pills on Frame 03, then the Hub row on Frame 04

ACT IV — THE COUNCIL                        (deck, slides 23–28)
ACT V — THE BOUNDARY                        (deck, slides 29–32)

END CARD                                    (deck, last slide)
  hold for at least 2 seconds before lights up
```

---

## Talking Points by Slide *(condensed)*

**Cold open.** Don't fill it. The cursor blinks for you.

**Compare slide.** "The industry default is the left column. Audit comes after. NEXUS is the right column. Authority comes first."

**Stat card 36 / 0 / 0.** "This is the flag we're going to plant. We'll come back to it with proof."

**Pipeline diagram.** "Six checkpoints. One direction. No bypass. There is no exception path implemented in the code, because the moment you implement the exception path, the doctrine is gone."

**Action JSON.** "An action enters as paperwork, not as a function call. That's the first design decision."

**Security source.** "Twelve lines. Auditable in one sitting. ML detection is on the roadmap — not the foundation."

**Trust registry.** "Trust is data, not code. Mutating it requires a commit. A commit requires review. The audit trail is the version control."

**Security-overrides-trust.** *(slow down here)* "This is enforced by source order. The war test reads the source of `executor.py` and verifies that the security tokens appear before the trust tokens. Doctrine is enforced by structure."

**Trust ladder.** "Climbed slowly. Each rung granted by the operator. None of them disable the security check that runs underneath."

**War test scope.** "Defensive only. The test cannot harm the system it tests. No network. No mutation. No deletion."

**Forensic exhibit.** *(point to a specific timestamp)* "These are not mocks. This is the live append-only file. Sixteen entries on disk."

**Verdict reveal.** "Pass thirty-six. Warn zero. Fail zero. CI re-runs on every push. The badge is green because the test is green."

**Council four lenses.** "Independent reasoning, then structured agreement. Not consensus by default."

**Why odd numbers.** "Reduces deadlock. Makes the agreement threshold clean."

**Hub.** "The Hub routes. The operator decides. The agent executes only what was decided."

**Limitations.** "These aren't bugs. They're the boundary of the proof. A system that overclaims its scope is not a governed system."

**Doctrine card.** *(read the six rules out loud, slowly, one per line)*

**End card.** "Governance is not the obstacle to AI. It is the architecture for trustworthy AI." — *hold the silence*.

---

## Q&A Anticipations

**"Why rule-based detection in 2026? Isn't this primitive?"**
> Yes — and that is the point. The detector is twelve lines of Python because it has to be auditable in one sitting. ML detection is stage two of the threat-handling roadmap. We do not build the more sophisticated layer until the simpler layer is provably correct. The simpler layer is now provably correct.

**"How does this scale beyond a local sandbox?"**
> It does not — yet. Scaling is a future direction. Base V1 is intentionally bounded so that the governance baseline is provable before complexity arrives. The execution contract, the trust ladder, and the doctrine all carry forward. The sandbox is the proving ground, not the destination.

**"What stops me from disabling the security check?"**
> Three things in order: source-order enforcement (war test fails), CI gating (badge fails), and operator review (commits require review). Defeating all three requires deliberate, traceable, multi-step action — which is exactly what the system is supposed to make adversarial behaviour cost.

**"Where does the council actually live? It looks like a future feature."**
> Correct — the four-lens council is described in the deep dive and demonstrated in the storyboard. Implementation is part of the NEXUS OS direction, not Base V1. Base V1 establishes the executor; the council is the next layer above it.

**"What does the mobile companion add?"**
> Approval-gate visibility from a phone. Pending action queue. Council deliberation feed. Quarantine log mirror. It does not give the phone *more* authority than the desktop — it gives the operator the same authority from a different surface.

---

## Failure Recovery

| Symptom | Fix |
|---|---|
| Mermaid diagram doesn't render | Press right-arrow then left-arrow on the deck — this re-fires the `slidechanged` event |
| War test replay keeps "awaiting initiation..." | Click `Reset` then `Run` |
| Verdict overlay won't dismiss | Press `Esc` |
| Slides look washed out on a projector | Press `B` to black out, restart projector colour profile, press `B` again |
| Speaker notes window won't open | Press `S` while focused on the deck |

---

## Fast variant *(if you have 6 minutes, not 14)*

Skip:
- Slides 4 (classification table)
- Slides 9, 12, 13 (individual pipeline stages — collapse to "six checkpoints, one direction")
- Slides 19–22 (war-test detail — go straight from scope to verdict)
- All of Act V (boundary section)

Keep:
- Cold open
- Compare slide
- Pipeline diagram
- Forensic exhibit
- Verdict
- Council four-lens grid
- End card

That's an 8-slide cut that still tells the story. Use Cinematic playback speed and cut to verdict immediately.

---

## Long variant *(20 minutes, technical audience)*

Insert:
- A live `python nexus_war_test.py` run in a real terminal between Acts II and III
- Open `executor.py` in an editor and walk through it line-by-line for the security-before-trust slide
- Show `threat_log.txt` in a terminal — `cat 04_logs/security/threat_log.txt | tail -16`
- Open `02_config/execution_trust_registry.json` and demonstrate that adding a new entry is one commit

Cut:
- Nothing. The deck holds the structure; the live terminal is supplementary.
