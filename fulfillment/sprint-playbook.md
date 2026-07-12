# Sprint Fulfillment Playbook v1 — "Renewal Recovery Sprint" ($500, 14 days)

Purpose: the productized unit we sell first. Must be deliverable almost entirely by Claude with ~zero Luke hours. This doc is the fulfillment spec Claude Code executes per client.

## Day 0 — Intake (client's hour, our automation)
- Intake form (built once): agency name, AMS/tools in use, lines of business, book export or renewal report (CSV), sending domain access OR we send via their existing tool, consent attestation checkbox (they confirm policyholder contact info was collected in the business relationship), voice/tone preferences, e-sign service agreement + data handling terms.
- Deliverable back same day: kickoff email confirming scope + the segment we'll target.

## Day 1–2 — Book analysis
- Parse export: renewal dates next 60–120 days, premium by policy, lines held per household (cross-sell gaps flagged for the REPORT only — sprint executes renewals, upsell comes in retainer).
- Pick the sprint segment: policies renewing in 45–90 days, mid-to-high premium, single-line households deprioritized (save for retainer pitch).
- Deliverable: 1-page "Leakage Snapshot" — renewals at risk, estimated premium exposed, benchmark retention delta. (This document alone justifies the $500 and sells the retainer.)

## Day 3–4 — Campaign build
- 3-touch email sequence per segment (client-branded, their voice, approval required):
  T1 (90–60 days out equiv.): "renewal ahead — here's what's changing / let's review coverage"
  T2 (+5 days): value touch — coverage checkup offer, no pressure
  T3 (+7 days): direct — book a renewal review call w/ their producer (their calendar link)
- Compliance pass: email-only; footer w/ agency address; opt-out honored into suppression list we maintain per client; FL/TX/state windows respected on any send timing.
- Client approval gate (async — Loom walkthrough + approve button).

## Day 5–12 — Run
- Send via client's tool if they have one (Levitate/Fuse/GHL — we operate it) or via a client-subdomain we configure (their DNS, their brand — NOT our cold-outreach infra; never mix).
- Reply routing: responses go to the agency's producers; we monitor, nudge producers on unanswered replies within 4 business hours (this "human follow-up routing" is the named gap no platform closes — it's the product).
- Mid-sprint pulse (Day 8): one-paragraph status to client.

## Day 13–14 — Report + convert
- Sprint report: sends, engaged policyholders, review calls booked, renewals confirmed during window, premium touched. Dollars first, email stats second.
- Conversion ask built into report delivery: "Here's what 14 days on one segment produced. The retainer runs this across your whole book, plus quote follow-up and cross-sell. $1,000/mo, cancel anytime." + payment link.
- If results are weak: say so plainly, diagnose why (list quality, timing, offer), and either extend free for 7 days or part cleanly. Reputation compounds; fake wins don't.

## Ops notes
- Target cost per sprint: <$20 marginal (sending + verification) → ~96% margin
- Concurrency: playbook must handle 5+ simultaneous sprints by week 3 — every step above gets a script/template in /fulfillment
- Free case-study sprints (first 2): identical playbook, testimonial + numbers in exchange, prioritize Angle B repliers (existing tools = fastest deploy)
- Data handling: client book data stays in per-client encrypted folder, deleted on request, never used across clients; note in agreement.
