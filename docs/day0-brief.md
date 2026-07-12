# PROJECT BRIEF — Day 0
**Goal:** $500/day net by Day 30. $1,000/day by Day 60.
**Prepared:** July 10, 2026 · Status: Niche locked, awaiting repo + Stripe setup

---

## 1. The Decision

**Venture:** Productized, AI-fulfilled retention & follow-up automation service for **independent insurance agencies** (P&C focus: auto/home/commercial lines).

**Working name candidates (pick at domain purchase):** RenewalEngine, PolicyFollow, AgencyRetain — final name chosen with domain availability in hand.

**Why this niche won (data, not vibes):**
- Highest retainer benchmarks of any AI-services niche: $3,000–$7,000/mo, with low competition — sources explicitly attribute the low competition to the niche being unglamorous
- Revenue-side pitch (renewals + cross-sell = measurable dollars), which closes faster than cost-savings pitches
- Reported outcomes to anchor copy: 25–40% increases in policy renewals and cross-sell revenue from automation
- Buyers are salespeople: high email responsiveness, short evaluation cycles, comfortable buying over email/call
- List-building advantage: state insurance licensing databases + agency directories = cheap, accurate, verifiable lead data
- AI-fulfillable end-to-end: sequences, copy, CRM automation — no on-site work, no compliance blocker at the automation layer (no PHI; TCPA/CAN-SPAM basics apply and are handled in design)

**Why the obvious alternatives lost:**
- ❌ Home services (missed-call text-back / AI receptionist): most saturated offer in the ecosystem — thousands of GoHighLevel white-label agencies pitching identical automations; $25–97/mo SaaS undercuts service pricing; inboxes burned
- ❌ Law firm intake: real pain, underserved, but skeptical slow buyers — wrong for a 30-day revenue window
- ❌ Med spas / healthcare: strong retainers but HIPAA-adjacent complexity and higher-touch sales
- 🔁 **Backup niche (pivot target if Day-14 gate fails): property management** — very low competition, 50–500 units per small team, heavy manual ops

## 2. The Offer

**Core offer (retainer):** "Done-for-you renewal & follow-up engine" — $1,500/mo starter, $2,500/mo standard.
Includes: quote follow-up sequences (speed-to-lead), renewal reminder campaigns starting 60 days pre-expiration, cross-sell campaigns keyed to existing policy types, review/referral request automation, monthly performance report.

**Foot-in-door offer:** $500 flat "Renewal Recovery Sprint" — one campaign, one book segment, results in 14 days. Converts to retainer. Exists to compress the trust gap of a brand-new vendor.

**Guarantee (risk reversal):** if the sprint doesn't produce measurable renewals/appointments, they don't convert to retainer — no long-term contract on entry.

**Revenue math to goal:**
- $500/day = $15k/mo ≈ 6 standard retainers, or 10 starters, or a mix + sprints
- $1,000/day (month 2) = ~12 standard retainers — fed by month-1 case studies + reinvested revenue into paid channel
- Conservative funnel at benchmark rates: 3,000 sends/mo → 3–6% reply → ~30–90 replies → 10–20 booked calls → 3–6 closes/mo. Two inbox-scale steps + sprint conversions close the gap. **This is the tightest assumption in the plan — flagged honestly.**

## 3. ICP Definition (v1)

- Independent P&C insurance agencies, US, 2–15 staff
- Owner/principal identifiable (they are the buyer)
- Signals of budget: multiple carriers listed, active Google reviews, paid ads or SEO presence
- Exclude: captive agents (State Farm/Allstate — corporate handles retention), single-person shops (<$500k revenue), enterprise brokerages
- Data sources: state DOI licensing databases, Trusted Choice / Big "I" directories, Google Maps scraping, Apollo/enrichment for emails, verification via NeverBounce/Prospeo (<2% bounce required)

## 4. Tech Stack & Budget (Month 1)

| Item | Choice | Cost |
|---|---|---|
| Domains ×3 (variants of brand) | Namecheap/Porkbun | ~$45/yr |
| Pre-warmed inboxes ×10 | Primeforge / Litemail / Zapmail (compare at purchase) | ~$50–80/mo |
| Sending platform | Instantly ($37) or Smartlead ($39) | ~$40/mo |
| Lead data + verification | Apollo credits + verifier | ~$100–150 |
| Landing page + booking | Carrd/Framer + Cal.com | ~$20 |
| Fulfillment CRM (client-side) | GoHighLevel sub-account or n8n + open-source stack — decide Day 2 | $0–97/mo |
| **Total infra** | | **~$250–400** |

Remaining budget ($600–1,600) reserved: additional inbox scaling in weeks 3–4, sprint fulfillment costs, and month-2 paid channel seeded by revenue reinvestment.

**Sending discipline (from deliverability data):** 20–25/day/inbox week 1 → 40–50/day/inbox cap. Scale via inboxes, not volume. Separate sending domains from brand domain. SPF/DKIM/DMARC verified before first send. Monitor Google Postmaster from day 1.

## 5. Five Working Days

- **Day 1:** Buy domains + inboxes; DNS + auth setup; Stripe products/payment links; landing page + Cal.com live; ICP list build begins (target 1,500 verified contacts)
- **Day 2:** Fulfillment system build (sequence templates, campaign architecture, reporting). Recruit 1–2 agencies for free/discounted sprints via targeted outreach → manufactured case studies
- **Day 3:** Finish list (3,000 verified); write 3 campaign angles × 4-touch sequences; personalization pipeline (AI-generated first lines from agency websites/reviews)
- **Day 4:** Launch sequences across all inboxes; reply-handling automation (AI triage + draft responses); booking flow tested end-to-end
- **Day 5:** First reply data review; kill losing angles, scale winners; layer channel 2 (LinkedIn manual-assist or cold-call-via-hired-VA decision point)

## 6. Go/No-Go Gates

**Day 14 gate:** reply rate <1.5% after copy iteration OR 0 booked calls → pivot offer within niche first (e.g., lead-gen instead of retention), then pivot niche to property management. Model (cold outbound B2B services) survives; only the target changes.
**Day 21 gate:** calls booking but not closing → move Luke into closing calls (2–4 short calls/wk) + tighten sprint offer.

## 7. Division of Labor

**Claude (via Claude Code):** research, list building, copy, campaign ops, reply triage, fulfillment builds, reporting, landing page, all iteration.
**Luke (facilitator only):** Stripe identity verification, domain/inbox purchases (card in hand), any account signups requiring human verification, 2–4 closing calls/week in weeks 2–4 if async closing underperforms.

## 8. Repo Structure (set up when home)

```
/venture-hub
  /docs          ← this brief, decision log, ICP, offer docs
  /research      ← niche data, competitor scans, source dumps
  /leads         ← list building scripts + verified CSVs (gitignored)
  /outreach      ← sequences, angles, A/B log, reply templates
  /fulfillment   ← client campaign templates, n8n/GHL configs
  /site          ← landing page source
  /ops           ← dashboards, daily metrics log, budget tracker
  CLAUDE.md      ← project context + operating rules for Claude Code
```

## 9. Honest Risk Register

1. **30-day timeline is the tail outcome.** Benchmarks make month 1 revenue of $5–15k plausible; $15k requires above-median close rates or sprint volume. Mitigation: sprints compress deal size to compress sales cycle.
2. **Cold outbound reply rates are declining ecosystem-wide.** Mitigation: tight ICP + real personalization + boring niche = less inbox competition.
3. **Zero case studies at launch.** Mitigation: Day 2 free-sprint manufacturing.
4. **Vendor-blog data bias.** Most benchmark sources sell inboxes/software. Treated pricing as accurate, ROI claims as optimistic; funnel math above uses the conservative end.
5. **Hands-off constraint vs. B2B closing.** Async close (Loom demo + AI follow-up) is Plan A; Luke on calls is Plan B and likely needed for the doubling month.

## 10. Immediate Next Actions

- [ ] Luke: hub repo created, Claude Code running (Day −1)
- [ ] Luke: Stripe account + identity verification complete
- [ ] Claude: domain shortlist w/ availability check → purchase list ready for Day 1
- [ ] Claude: inbox provider final comparison at time of purchase (pricing drifts)
- [ ] Joint: Day 1 execution session
