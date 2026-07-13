# DNS & Email Auth Runbook — run the day domains are purchased
Rule (CLAUDE.md #5): **nothing sends until SPF, DKIM, and DMARC verify on every sending domain.** Brand domain (agencyretain.com) is never used for cold outreach.

## Domain roles
| Domain | Role | Mail? |
|---|---|---|
| agencyretain.com | Brand: landing page, calculator, sprint/client email later | Not for cold outreach |
| agencyretainhq.com | Sending domain 1 (3-4 inboxes) | Cold outreach only |
| getagencyretain.com | Sending domain 2 (3-4 inboxes) | Cold outreach only |
| tryagencyretain.com | Sending domain 3 (3-4 inboxes) | Cold outreach only |

## Step order (per sending domain)
1. **Primeforge setup** — it automates Workspace/M365 tenant + DNS records; approve the records it pushes (or paste them into Porkbun DNS if manual): MX, SPF (`v=spf1 include:_spf.google.com ~all` for Google tenants), DKIM (2048-bit, selector per tenant), DMARC.
2. **DMARC start value** (week 1-2): `v=DMARC1; p=none; rua=mailto:dmarc@agencyretainhq.com; fo=1` — monitor only. Move to `p=quarantine` after 2 clean weeks.
3. **Redirects:** each sending domain 301-redirects to agencyretain.com (Porkbun URL forwarding) — a bare parked sending domain looks like spam infrastructure to filters and humans who check.
4. **Custom tracking domain** in Smartlead per sending domain (CNAME, e.g. `track.agencyretainhq.com`) — never the shared default tracking domain.
5. **Google Postmaster Tools:** register all three sending domains day 1; check weekly (spam rate must stay <0.1%; 0.3% is the Google enforcement line).

## Verification gate (run before first campaign; re-run after any DNS change)
For each domain, all must pass:
```
dig TXT <domain>                      # SPF present, exactly one v=spf1 record
dig TXT <selector>._domainkey.<domain>  # DKIM present
dig TXT _dmarc.<domain>               # DMARC present
dig MX <domain>                       # MX resolves
```
Then: send test mail from each inbox to a Gmail seed → "show original" must read **SPF: PASS, DKIM: PASS, DMARC: PASS**. Smartlead's built-in checker as a second opinion. Log results in ops/metrics.md notes.

## Warm-up policy
Inboxes arrive pre-warmed (Primeforge) but still: connect all 10 to Smartlead warm-up pool on day 1, keep warm-up running alongside campaigns permanently (10-20 warm-up mails/day/inbox), start campaigns at 20-25 sends/day/inbox, raise only after week 1 with clean Postmaster data. Cap 40-50 forever; scale by adding inboxes, not volume.

## Brand domain (separate track)
- agencyretain.com hosting: static — Cloudflare Pages / Netlify free tier (decide at deploy; either is fine and $0). Point apex + www.
- SPF/DMARC on the brand domain too even before it sends mail (`v=spf1 -all` + p=reject if truly no mail yet) — stops spoofing of the brand.
