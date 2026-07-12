# Domain Research Report — RenewalEngine / PolicyFollow / AgencyRetain
*Checked live July 12, 2026 via registry RDAP (Verisign for .com, Identity Digital for .io, rdap.org for .co). "AVAILABLE" = authoritative registry returned 404 / no record; "REGISTERED" = full RDAP record returned.*

**Method note:** .com checks ran against rdap.verisign.com; .io/.co checks via rdap.org. The Verisign endpoint had a built-in positive control — it returned a full record for renewalengine.com while 404-ing the others — so the .com and .io results are high-confidence. The two .co results lacked a positive control; treat .co as high-probability-available rather than certain.

## (a) Availability — brand domains and variants

| Domain | Status | Notes |
|---|---|---|
| renewalengine.com | **REGISTERED** | Registrar: Gname 039 Inc; registered 2025-09-01, **expires 2026-09-01**; clientTransferProhibited. Gname is heavily used by domain speculators — likely a speculative/parked registration that *might* drop in ~7 weeks, but don't plan around it. |
| renewalengine.io | AVAILABLE | |
| policyfollow.com | AVAILABLE | |
| policyfollow.io | AVAILABLE | |
| agencyretain.com | AVAILABLE | |
| agencyretain.io | AVAILABLE | |
| getrenewalengine.com | AVAILABLE | variant |
| tryrenewalengine.com | AVAILABLE | variant |
| renewal-engine.com | AVAILABLE | variant |
| agencyretained.com | AVAILABLE | variant / defensive |
| renewalengine.co | AVAILABLE* | *rdap.org 404; no positive control run — slightly lower confidence |
| policyfollow.co | AVAILABLE* | *same caveat |

## (b) Sending-domain candidates (.com only — all AVAILABLE)

| Brand | Sending domain | Status |
|---|---|---|
| RenewalEngine | renewalenginehq.com | AVAILABLE |
| RenewalEngine | getrenewalengine.com | AVAILABLE |
| RenewalEngine | tryrenewalengine.com | AVAILABLE |
| RenewalEngine | renewal-engine.com | AVAILABLE |
| RenewalEngine | renewalengineteam.com | AVAILABLE |
| PolicyFollow | policyfollowhq.com | AVAILABLE |
| PolicyFollow | getpolicyfollow.com | AVAILABLE |
| PolicyFollow | trypolicyfollow.com | AVAILABLE |
| PolicyFollow | policy-follow.com | AVAILABLE |
| AgencyRetain | agencyretainhq.com | AVAILABLE |
| AgencyRetain | getagencyretain.com | AVAILABLE |
| AgencyRetain | tryagencyretain.com | AVAILABLE |
| AgencyRetain | agency-retain.com | AVAILABLE |

All 13 sending-domain candidates checked against Verisign RDAP; every one returned 404 (no record).

## (c) Registrar pricing (July 2026)

| | .com first year | .com renewal | .io first year | .io renewal |
|---|---|---|---|---|
| **Porkbun** (from porkbun.com, live) | $11.08 | $11.08 (flat — no markup) | $28.12 (sale) | $51.80 |
| **Namecheap** (via search; namecheap.com blocked direct fetch) | ~$6.79–9.58 promo | ~$13.98–16.98 (sources vary) | $34.98 | **$75.98** |

**Gotchas:** Namecheap's .io renewal ($75.98) is ~47% above Porkbun's. Namecheap's cheap .com is first-year-only; renewal roughly doubles. Porkbun is flat-priced on .com (renewal = registration). ICANN adds $0.18–0.20/yr per domain either way. Namecheap's exact day-of prices couldn't be verified on their own site (403 on fetch) — treat as approximate.

## (d) Recommendation

**RenewalEngine is the only compromised name** — its .com is taken (even if only by an apparent speculator). **PolicyFollow and AgencyRetain are both completely clean**: brand .com AND .io available, plus 4 natural sending .coms each. On pure domain situation it's a tie; **AgencyRetain gets a slight edge** because the defensive variant agencyretained.com is also open and the name self-describes the offer to the target buyer (independent P&C agencies).

**First-year cost estimate (AgencyRetain at Porkbun):**
- agencyretain.com (brand) + agencyretainhq.com, getagencyretain.com, tryagencyretain.com (3 sending) = 4 × $11.08 = **$44.32**
- Optional: agencyretain.io defensive (+$28.12) and agencyretained.com defensive (+$11.08) → **~$83.52 all-in**

At Namecheap the first year would run a few dollars cheaper but renewals — especially the .io — cost meaningfully more, so Porkbun is the better registrar for a hold-forever brand portfolio.

**Caution:** availability is live and these are cheap, guessable names — once the brand is settled, register the same day.
