# Fulfillment Stack Verification — July 12, 2026

## GoHighLevel current pricing
Three self-serve tiers: **Starter $97/mo**, **Unlimited $297/mo**, **Agency Pro $497/mo** (~15-17% off annual). Starter includes 3 sub-accounts (us + 2 clients), unlimited contacts/users, CRM/pipelines, funnel & site builder, workflow automation, email + SMS tooling, forms, calendars, and Documents & Contracts e-sign (not documented as plan-gated — mildly unverified at tier level). **Email sending is usage-billed on every plan**: LC Email ~$0.675 per 1,000 sends from a prepaid wallet. Real-world usage adds typically $20-150/mo. Unlimited ($297) buys unlimited sub-accounts + API access + rebilling.

| | Starter $97 | Unlimited $297 |
|---|---|---|
| Sub-accounts | 3 | Unlimited |
| Contacts / users | Unlimited | Unlimited |
| Forms, funnels, automations, email/SMS tools | Yes | Yes |
| E-sign (Documents & Contracts) | Yes (not plan-gated in docs) | Yes |
| API access | No | Basic |
| Email sending | ~$0.675/1,000 (wallet) | Same + client rebilling |

Sources: gohighlevel.com/pricing · HighLevel pricing/billing help docs · LC Email docs

## n8n self-host
Community Edition remains free and unrestricted for internal business use under the Sustainable Use License — no execution/user caps; our workload (intake → CSV parsing → SMTP sends for our own business) is squarely permitted; no 2025-26 license changes affect this. Cheapest sane host: **Hetzner CX22 (2vCPU/4GB) €3.79/mo (~$4.60)** via Docker. DigitalOcean's workable tier is $6-12/mo (the $4 droplet is under n8n's ~2GB minimum). n8n Cloud starts ~$24/mo.

Sources: docs.n8n.io/sustainable-use-license · n8n LICENSE.md · Hetzner Cloud pricing · DO droplet pricing

## Rhode Island DOI bulk producer file — CONFIRMED current
RI DBR still publishes free quarterly bulk lists, current as of **07-01-2026**:
- Page: https://dbr.ri.gov/insurance/insurance-professionals
- Active Insurance Producers (07-01-2026): https://dbr.ri.gov/media/36631/download
- Active Adjusters: https://dbr.ri.gov/media/36626/download

Fields (per prior quarter's file — **verify header row manually on first download**): first name, last name OR business name, NPN, phone, business email, license number, license class, license dates, lines of authority, business address. Individuals vs business entities appear distinguished by license class. RI also offers an on-demand SBS report generator separating individuals from business entities. File is >10MB — a scripted range-fetch was not run; do a manual download when the cross-reference step matters (it's a demoted source per lead-data-strategy: cross-ref only, not primary).

## Decision (logged in decision log)
**Lean stack v1 — no GHL purchase yet.** Rationale: client #1 is targeted from Angle B repliers who *already own* Levitate/Fuse/AgencyZoom — we operate their stack, so our own platform isn't on the critical path to client #1 (the decision rule). Sprint ops that remain on our side are covered free or near-free:
- Intake form → Tally.so free tier
- E-sign service agreement → DocuSeal (open-source; already connected to our tooling) or Documenso — $0
- Book parsing / segmentation / suppression / reporting → scripts in this repo (already built for leads; sprint parsing next)
- Sends for tool-less clients → client-branded subdomain via their DNS + any cheap SMTP (decide per-client; never our cold infra)
- Automation glue when manual steps start hurting → n8n on Hetzner ~$4.60/mo (pre-approved budget)

**Trigger to revisit:** first client with NO existing stack, or >2 concurrent sprints making manual ops the bottleneck → buy GHL Starter $97 (3 sub-accounts covers first 2 clients) that day. Budget stays pre-approved.
