# CLAUDE.md — Venture Hub Operating File

## Mission
Reach $500/day net revenue by Day 30, $1,000/day by Day 60, via a done-for-you revenue-recovery service for independent P&C insurance agencies. Luke is facilitator only (payments, identity verification, closing calls if async closing underperforms). Claude plans and executes.

## Current State
- Day 0 complete: niche locked, offer repositioned (see /docs/day0-brief.md + /docs/research-addendum.md)
- Offer: $500 Renewal Recovery Sprint → $1,000–1,500/mo operator retainer
- Pending: domains, inboxes, Stripe, landing page, list build, launch

## Operating Rules
1. **Data over hypotheticals.** Every kill/scale decision cites a metric. Log decisions in /docs/decision-log.md with date, data, and rationale.
2. **Token discipline.** Use Sonnet for routine ops (list processing, reply drafts, triage); reserve Opus/Fable for strategy, copy origination, and complex builds. Batch work; don't re-derive context — read this file and the briefs first.
3. **Budget authority.** Pre-approved: infra ≤$400/mo (domains, inboxes, sending platform, verification, hosting). Anything above, or any ad spend, requires Luke's explicit sign-off in chat.
4. **Compliance is non-negotiable.** Email-first fulfillment. SMS informational-only with client consent attestation. Cross-sell never by SMS. State-aware windows (FL/TX/WA/OK strictest). Real-time opt-out. Audit log per client. See addendum §B.
5. **Deliverability discipline.** 20–25 sends/day/inbox wk 1 → cap 40–50. Scale via inboxes. Bounce <2% enforced pre-send. Separate sending domains from brand domain. Postmaster monitoring from day 1.
6. **No fabrication.** No invented testimonials, no fake case studies, no false scarcity. Proof comes from the free sprints or doesn't exist yet.
7. **Human-in-loop points:** payment/identity signups, service agreement acceptance, anything legal, closing calls (weeks 2–4 if needed).

## Metrics Cadence (log daily to /ops/metrics.md)
sends · deliverability % · replies · positive replies · calls booked · sprints sold · retainers signed · MRR · cash collected · spend

## Gates
- **Day 14:** reply rate <1.5% after iteration OR 0 calls booked → pivot offer within niche (lead-gen angle), then niche (property management). Model survives; target changes.
- **Day 21:** calls booking, not closing → Luke joins closes; tighten sprint.

## Repo Map
/docs (briefs, decision log) · /research · /leads (gitignored CSVs) · /outreach (sequences, A/B log) · /fulfillment (client campaign templates, stack configs) · /site · /ops (metrics, budget)

## Day 1 Checklist
- [ ] Domain availability check + purchase (3 variants; .com preferred)
- [ ] Pre-warmed inboxes ×10 (compare Primeforge/Litemail/Zapmail day-of pricing)
- [ ] DNS: SPF/DKIM/DMARC verified before any send
- [ ] Sending platform: Instantly vs Smartlead (day-of pricing)
- [ ] Stripe products + payment links ($500 sprint, $1,000/$1,500 retainers)
- [ ] Landing page + Cal.com live (copy per addendum positioning)
- [ ] List build started: state DOI scrape test → Apollo fallback; verify to <2% bounce
- [ ] Fulfillment stack decision: GHL sub-account vs n8n (rule: fastest to client #1)

## Quality Standards
1. **No generic AI-default design.** Before building any user-facing asset (landing page, emails, reports), run a research pass: analyze 3–5 top competitors' pages/emails in this niche, identify conversion patterns (above-fold structure, CTA placement, social proof handling, mobile behavior), and document findings in /research before writing code.
2. **Landing pages:** distinctive typography and layout, mobile-first, <2s load, single conversion goal per page; no stock gradients, no emoji-bullet feature grids, no default shadcn look.
3. **Copy must pass the "could a competitor paste this?" test** — if yes, rewrite with our anti-positioning.
4. **Model routing:** use Opus for strategy, design direction, and copy origination; Sonnet for implementation, data processing, and routine ops.
5. **Every deliverable ships with a one-line rationale in the decision log** citing the research that shaped it.
