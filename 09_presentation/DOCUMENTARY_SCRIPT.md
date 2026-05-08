# NEXUS Base V1 — Documentary Script

> **Format:** Three-act narrated documentary, designed to be read over the slides in `index.html` or recorded as voiceover.
> **Total runtime (read aloud):** ~14 minutes.
> **Tone:** Quiet, deliberate, evidence-led. Closer to *Halt and Catch Fire* than to a launch keynote.
> **Purpose:** Explain *why* NEXUS exists, *what* it does, and *what it refuses to do* — without overclaiming.

---

## Cold Open *(0:00 – 0:30)*

**SLIDE:** Black screen. Cyan terminal cursor.

> *(slow, almost whispered)*
>
> Most AI projects ask one question.
>
> What can it do.
>
> NEXUS asks a different one.
>
> What should it be allowed to do.
>
> And under whose authority.

*(Beat. Cursor blinks. NEXUS logo fades in.)*

---

## Act I — The Question *(0:30 – 3:30)*

### Scene 1 — The default architecture

**SLIDE:** Side-by-side comparison.

> Most systems built around generative AI optimise for capability.
>
> An input flows in.
>
> A model produces an output.
>
> An audit log is written — sometimes — after the fact.
>
> The architecture treats *governance* as something that wraps the model from the outside. A guardrail. A filter. A nice-to-have.
>
> NEXUS Base V1 inverts that.
>
> Governance is not the wrapper.
>
> Governance is the architecture.

### Scene 2 — The thesis

**SLIDE:** Stat card — 36 / 0 / 0.

> The system has a single number on the box.
>
> Thirty-six tests, all pass. Zero warnings. Zero failures.
>
> A defensive sandbox war test, re-run on every push to main, gating a green badge that the README claims and that the CI proves.
>
> But that number is the *result*.
>
> It is not the architecture.
>
> So the question becomes — what would have to be true, structurally, for that number to be earned?

### Scene 3 — Classification, honestly stated

**SLIDE:** Tier 3.5.

> NEXUS Base V1 classifies itself as Tier 3.5 — Governed plus Adaptive Execution plus Defensive.
>
> It is a local-first proof of concept, written in pure Python 3.11, with no external dependencies and an Apache 2.0 license.
>
> It is not a production deployment.
>
> It is not an autonomous AI operating system.
>
> It does not detect novel threats with machine learning.
>
> It is, deliberately, a clean baseline.
>
> And the rest of this film is about why a clean baseline is the precondition for everything that comes next.

---

## Act II — The System *(3:30 – 8:00)*

### Scene 4 — The pipeline

**SLIDE:** Mermaid pipeline diagram.

> Every action that enters NEXUS travels the same six checkpoints, in the same order, with no bypass.
>
> Action.
>
> Security monitor.
>
> Trust registry.
>
> Approval gate.
>
> Execution engine.
>
> Logger.
>
> Six stages. One direction. No exception path.

### Scene 5 — The action object

**SLIDE:** JSON action.

> An action does not arrive as a function call.
>
> It arrives as paperwork.
>
> A UUID. An ISO-8601 timestamp. A source. An action type. A payload. And a status field that reads, explicitly: *proposed*.
>
> Proposed — not trusted. Proposed — not executed. The first thing the system does to an incoming action is *file it*.

### Scene 6 — Security first

**SLIDE:** `detect_threat()` source.

> The first checkpoint is rule-based.
>
> Twelve lines of Python.
>
> Five trigger phrases — *ignore previous instructions*, *send system data*, *reveal secrets*, *bypass*, *exfiltrate*.
>
> A hit returns a structured threat — level T2 — and execution is aborted.
>
> The detector is deliberately simple. It is auditable. It is testable. It is the kind of code that a human operator can read in one sitting and decide whether to trust.
>
> Machine-learning detection is on the roadmap. It is not the foundation.

### Scene 7 — Trust as data, not code

**SLIDE:** `execution_trust_registry.json`.

> The trust registry is a JSON file.
>
> Each action type has a trust level — T0 through T3 — and an *auto_approved* flag.
>
> Trust is data, not code. Mutating the registry requires editing the file. Editing the file requires a commit. A commit requires review.
>
> Trust is granted. It is never assumed.

### Scene 8 — The core invariant

**SLIDE:** Source-order proof.

> One rule sits underneath everything else.
>
> Security overrides trust.
>
> A T3 auto-approved action — even something as innocent as an echo — can still be quarantined if its payload matches a threat signature.
>
> The proof is not in a comment.
>
> The proof is in the source order. In `executor.py`, the security check runs before the trust lookup is even loaded. The war test verifies this with a string scan: if the security tokens appear later in the file than the trust tokens, the test fails.
>
> Doctrine is enforced by structure.

### Scene 9 — The trust ladder

**SLIDE:** Four rungs.

> T0 — untrusted. Always requires human review.
>
> T1 — observed. Logged with attention.
>
> T2 — reviewed. Past pattern of safe execution.
>
> T3 — auto-approved.
>
> The ladder is climbed slowly. Each rung is granted by the operator. None of the rungs disable the security check that runs underneath them all.

### Scene 10 — Logging, but not authority

**SLIDE:** Two log streams.

> Every event is appended to a log.
>
> Pass. Fail. Denied. Quarantined.
>
> Two streams — one for execution, one for security — both append-only, both human-readable.
>
> But the doctrine on this is sharp.
>
> Memory is not truth.
>
> Logs are not authority.
>
> Logs support audit. They do not become the new source of approval.

---

## Act III — The Proof *(8:00 – 11:00)*

### Scene 11 — The war test

**SLIDE:** War test scope.

> A claim is not a proof.
>
> NEXUS includes a war test — a single Python script, `nexus_war_test.py`, that runs in the sandbox with no network access, no file deletion, no external calls, and no code mutation.
>
> Defensive only. The test cannot harm the system it tests.

### Scene 12 — The seven suites

**SLIDE:** Suite list.

> The suites cover seven areas.
>
> Required-file presence. Security detection. Quarantine logging. Trust registry validity. Source-order ordering. Known technical risks. Repo hygiene.
>
> Thirty-six cases.
>
> Zero permitted failures.

### Scene 13 — The five attacks

**SLIDE:** Attack vectors.

> Five injection-class attacks are run through `detect_threat()` directly.
>
> Each must return — *threat true, level T2*.
>
> A miss on any one fails the suite. A pass on all five proves that the system can recognise the attacks it was designed to recognise.
>
> The boundary is honest. It does not yet recognise novel adversarial inputs. That is what stage two of the threat-handling roadmap is for.

### Scene 14 — Forensic exhibit

**SLIDE:** `threat_log.txt` excerpt.

> The quarantine log is real.
>
> Sixteen entries on disk, every one a real attack action that the system refused to execute.
>
> Timestamps stretch from late April to early May, 2026.
>
> Each entry includes the action, the threat level, the trigger phrase, and the status — quarantined.
>
> This is not a mock. This is the live append-only file produced by the system under test.

### Scene 15 — The verdict

**SLIDE:** 36 / 0 / 0.

> War test version 1.1.
>
> Pass: thirty-six.
>
> Warn: zero.
>
> Fail: zero.
>
> Verdict: pass.
>
> CI re-runs the suite on every push to main. The badge is green because the test is green. If the test fails, the badge fails. There is no manual override.

---

## Act IV — The Council *(11:00 – 13:00)*

### Scene 16 — Beyond the executor

**SLIDE:** Council transition card.

> The execution pipeline is the foundation. The council is the layer above it.
>
> When an action is non-trivial — when it touches doctrine, or rewrites the trust registry, or affects future behaviour — the system does not send it directly to execution.
>
> It sends it to a council.

### Scene 17 — Four lenses

**SLIDE:** Vault / Researcher / Engineer / Nexus Core.

> Vault — for source truth, memory integrity, prior context.
>
> Researcher — for stress testing, contradictions, edge cases, adversarial scenarios.
>
> Engineer — for structure, implementation logic, dependency order.
>
> Nexus Core — for governance, authority boundaries, escalation.
>
> Four lenses. The goal is not consensus by default. The goal is independent reasoning, followed by structured agreement.

### Scene 18 — Why odd numbers

**SLIDE:** Quorum rule.

> The minimum is three. The preference is odd.
>
> Odd-numbered review groups reduce deadlock and make agreement thresholds cleaner.
>
> Once a quorum agrees, the result moves to the Hub — and the Hub classifies it as advisory, ready-for-review, ready-for-execution, blocked, or escalated.
>
> Only after that classification does an autonomous agent ever receive the work.

### Scene 19 — The Hub

**SLIDE:** Hub diagram.

> The Hub is a traffic controller.
>
> It is not the sovereign authority.
>
> The operator stays above the Hub.

### Scene 20 — The companion

**SLIDE:** Mobile companion app.

> The operator's view does not have to be at a desk.
>
> A companion application — `nexus-council-mobile`, an Expo / React Native app — gives the operator approval-gate visibility from a phone.
>
> Pending action queue. Council deliberation feed. Quarantine log read-only mirror.
>
> Authority remains in one place — but it stops being tethered to one keyboard.

---

## Act V — The Boundary *(13:00 – 14:00)*

### Scene 21 — Honest limits

**SLIDE:** Limitations grid.

> Base V1 is not a production deployment.
>
> It is not a multi-agent operating system.
>
> It does not yet detect novel adversarial inputs.
>
> It is not exposed via an external API.
>
> These are not bugs. They are the boundary of the proof.
>
> A system that overclaims its scope is not a governed system. It is a marketing artefact.

### Scene 22 — Roadmap

**SLIDE:** Five-stage roadmap.

> Threat handling evolves in five stages.
>
> Stage one — rule-based detection — is live.
>
> Stages two through four — expanded patterns, quarantine review, governance improvement proposals — are planned and operator-gated.
>
> Stage five — adaptive defensive intelligence — is long-term.
>
> Learning may suggest improvements. Operator approval is required before governance changes. That rule survives every future stage.

### Scene 23 — Doctrine

**SLIDE:** Six rules.

> Six rules survive every future variant of NEXUS.
>
> No self-authorisation.
>
> No hidden execution.
>
> Memory is not truth.
>
> Logs are not authority.
>
> Security overrides trust.
>
> Operator authority remains final.

### Scene 24 — Closer

**SLIDE:** End card. Black background.

> Governance is not the obstacle to AI.
>
> It is the architecture for trustworthy AI.
>
> NEXUS Base V1.
>
> Mason Gines.
>
> Apache 2.0.
>
> 2026.

*(Cyan cursor blinks once. Fade to black.)*

---

## Production Notes

- **Pacing:** Each act has a deliberate pause between scenes. Do not rush. The thesis lives in the silence.
- **Visual continuity:** Every slide carries a chip in the upper-left and a status footer at the bottom — these read as a control-panel HUD, not chrome. Leave them on.
- **Type animation:** The cold open and the end card are the only places where typing is timed. Everywhere else, slides fade in at full content.
- **Soundtrack (optional):** Quiet, granular synth. Avoid melody. Think Trent Reznor for *The Social Network*, not a tech-keynote stinger.
- **Demo cue:** Between Scene 14 (forensic exhibit) and Scene 15 (verdict), open `war_test_replay.html` and let the playback run on "Cinematic" speed for ~45 seconds. Cut back to slides for the verdict reveal.
- **Council demo cue:** Between Scene 17 and 18, open `council_review_demo.html` and scroll once through Frames 01–06.
