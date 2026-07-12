# Research Addendum — Day 0 (Session 2)
**Supersedes:** Offer section (§2) of day0-brief.md · **Date:** July 10, 2026

---

## A. Competitive Landscape (changes positioning)

The insurance retention SaaS market is NOT empty. Incumbents:

| Player | Price | Notes |
|---|---|---|
| Agency Revolution (Fuse) | $249/mo + $500 setup; **$649/mo DIFM tier** | 3,000+ agencies; deep AMS integration (AMS360, Epic, HawkSoft, QQCatalyst); 2–4 wk onboarding |
| Levitate | $350–600/mo | Relationship marketing; personal-feel outreach; 45–65% open rates claimed |
| Better Agency | $79/mo | CRM + automation bundle; shallow AMS sync (no line-of-business/premium data) |
| AgencyZoom | ~$100+/mo | Sales pipeline + renewal workflows |
| InsuredMine | varies | Insurance-native CRM/automation |

**Implications:**
1. "We'll automate your renewals" as a pitch is dead on arrival — they've heard it, many own a tool already.
2. The $649/mo done-for-me tier from the incumbent is our price anchor. $2,500/mo retainers need extraordinary justification; $1,000–1,500/mo is the honest band.
3. **The wedge (named explicitly in industry sources):** no platform closes (a) AMS data reconciliation, (b) human follow-up routing/operation, (c) *proving* retention lift. Agencies buy Fuse/Levitate and underuse them — shelfware is common. The gap is operation, not software.

**Repositioned offer:** *Done-for-you revenue recovery, with proved lift.*
- We operate whatever stack they have (or install a lean one), reconcile the book data, run quote follow-up + renewal + cross-sell campaigns, and deliver a monthly report in dollars recovered — not opens/clicks.
- We are not selling a platform. We're the team that makes the platform (theirs or ours) actually produce.
- Anti-positioning line for copy: "You don't need another tool. You need someone to run the one you have."

**Pricing v2:**
- Renewal Recovery Sprint: $500 flat, 14 days, one book segment → the trust compressor
- Operator retainer: $1,000/mo (one line of business) / $1,500/mo (full book + cross-sell + reporting)
- Month-1 math: $15k/mo ≈ 10–12 retainers or 8 retainers + sprint flow. Month-2 doubling: case studies + reinvested ad spend + price ladder to $2k as proof accumulates.

## B. Compliance Findings (dictates fulfillment architecture)

**Federal TCPA:**
- Informational messages (renewal reminders, billing/policy notices) to existing policyholders → prior express consent suffices (number voluntarily provided in the relationship). Low risk.
- Marketing/promotional (CROSS-SELL) via autodialed SMS → prior express *written* consent required. $500–1,500 per message, no aggregate cap. Litigation up ~95% YoY.
- Opt-out: honor via "any reasonable method," ≤10 business days (process immediately in practice). Revocation kills informational messages too.
- Reassigned numbers create liability even with old valid consent — scrub lists.

**State mini-TCPA layer (stricter than federal, applies by recipient state):**
- FL (FTSA): 8am–8pm window, 3 contacts/24h, written consent for all marketing, broad autodialer definition
- TX (SB 140): texts count as solicitation, $5,000/violation private right of action
- WA, OK, MD, OR: various caps (3 attempts/day, tighter windows)
- Rule: apply the strictest standard per recipient state.

**Fulfillment architecture decisions (locked):**
1. Email-first for all campaign types (CAN-SPAM trivially satisfiable with existing customers)
2. SMS only for informational renewal notices, only where client attests documented consent; consent attestation clause in service agreement
3. Cross-sell NEVER via SMS — email only
4. State-aware send windows + frequency caps built into campaign logic
5. Opt-out processed in real time, propagated across channels
6. Consent/opt-out audit log maintained per client
7. **Sales angle:** "compliance-safe by design" is a differentiator vs. GHL agencies blasting unsolicited texts. Use it in copy and on the landing page.

## C. Source Reliability Notes
- Retainer benchmarks ($3–7k insurance): from AI-agency niche rankings — treat as top-of-market, not median. Our $1–1.5k pricing is set against the real incumbent anchor ($649 DIFM), not these.
- Deliverability/inbox pricing: vendor blogs; pricing verified across 4+ competing vendors, consistent.
- Compliance: cross-checked across legal-adjacent sources; final service agreement language should get a real attorney pass before client #3 (budget note: ~$200–400 template review, or use a vetted template initially).

## D. Open Items for Day 1 (Claude Code)
- [ ] Verify state DOI license databases are scrapeable per target state; fall back to Apollo/Google Maps if not
- [ ] Confirm Instantly vs Smartlead pick at purchase-day pricing
- [ ] Domain shortlist: check availability for RenewalEngine / PolicyFollow / AgencyRetain variants (.com preferred, .io fallback)
- [ ] Landing page copy draft (positioning above)
- [ ] Decide fulfillment stack: GHL sub-account ($97) vs n8n self-hosted ($0) — decision rule: whichever gets client #1 live faster wins; optimize later
