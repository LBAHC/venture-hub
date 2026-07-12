# Cold-Email Infrastructure Pricing — verified July 12, 2026

Scope: 10 pre-warmed inboxes on 2–3 dedicated domains + 1 sending platform. Week 1: 20–25 sends/day/inbox (~5,000–5,500/mo); capped later at 40–50/day/inbox (~9,000–11,000/mo). That later cap matters — it exceeds the cheapest plan on **both** platforms (see Task 2).

## Task 1 — Pre-warmed inbox providers

All three vendors (Primeforge, Litemail, Zapmail) exist and are active — no rebrands, no substitutions needed.

| | Primeforge | Litemail | Zapmail |
|---|---|---|---|
| Infrastructure | Official Google Workspace **and** MS365, US IPs | Official Google Workspace **and** MS365 ("no SMTP relays") | Google Workspace + MS365 (same price) |
| Per-inbox / mo | $4.50 monthly billing; ~$3.75 billed yearly | Fresh: $3.70 (Starter, 10 inboxes = $37/mo). Pre-warmed: "from $4/inbox" | Starter: $39/mo for 10 mailboxes ($3.90 eff.); extra mailboxes $3.50; yearly = 2 months free |
| Minimum | **10 mailbox slots** | 10-inbox Starter plan is the floor for bulk plans | Starter plan (10 mailboxes) |
| Setup fee | None; automated DNS included | None; "ready in 5 mins" | None; OAuth setup, ~10 min |
| Domains | **Not included** — $14/yr per .com | Fresh plans: not included, $15/yr. **Pre-warmed plans: domains included** | Not included — from $13/.com via their domain service |
| Warm-up claim | All mailboxes pre-warmed at no extra charge (per ColdEmailKit review — the vendor pricing page itself doesn't show a pre-warmed line item) | Pre-warmed = 12 weeks warm-up history, send immediately | Pre-warmed = "12+ weeks warm-up," but **pricing not public** — third-party sources report a $6–8/mailbox premium over base tiers; must book a call to confirm |
| 10-inbox cost | $45/mo (monthly) or ~$37.50/mo (yearly) + ~$3.50/mo domains | $37/mo fresh + domains; ~$40–50/mo pre-warmed w/ domains included | $39/mo + ~$3.25/mo domains; pre-warmed premium unverified |

**Verification notes:**
- Primeforge's pricing page uses a slot slider — "Mailbox cost of $4.5/month" confirmed verbatim on primeforge.ai/pricing (the $113/$94 figures displayed are for a 25-slot example). The "no extra charge for pre-warmed" claim is from ColdEmailKit's review, not verified on the vendor page.
- Litemail's exact pre-warmed per-inbox price is fuzzy: homepage says "from $4/inbox," search snippets show $4.99/inbox; litemail.ai/pricing 404'd. Treat $40–50/mo for 10 as the planning range.
- Zapmail flag (third-party, PuzzleInbox/InboxKit): its Google Workspace tenants are reportedly sourced via **India-based resellers**, which some reviewers claim measurably hurts inbox placement on US lists vs. US/EU-region tenants. Unverified, but a deliverability risk worth weighing since Google-tenant region matching is the whole point of paying for Workspace inboxes.

## Task 2 — Sending platforms (verified on vendor pricing pages)

| | Instantly Growth | Instantly Hypergrowth | Smartlead Base | Smartlead Pro |
|---|---|---|---|---|
| Price/mo | **$47** ($42.30 annual, 10% off) | $97 | **$39** ($32.50 annual) | $94 ($78.30 annual) |
| Email accounts | Unlimited | Unlimited | Unlimited | Unlimited |
| Contacts | 1,000 | 25,000 | 2,000 | 30,000 |
| Emails/mo | 5,000 | 100,000 | 6,000 | 90,000 |
| Warm-up | Unlimited, included | Included | Included (warmup pool) | Included |

**Critical fit check:** 10 inboxes connect fine on either cheapest plan (both allow unlimited accounts). But:
- **Week 1** (~5,000–5,500 campaign emails/mo at full month-rate): right at Instantly Growth's 5,000 cap; inside Smartlead Base's 6,000.
- **Capped volume** (40–50/day/inbox ≈ 9,000–11,000/mo): **exceeds both cheapest plans.** You'd need Instantly Hypergrowth ($97) or Smartlead Pro ($94) — the $40 platform budget line only holds at week-1 volume.
- Instantly Growth's 1,000-contact cap also binds immediately at "1,000+ contacts." Smartlead Base's 2,000 gives breathing room.

## Task 3 — Recommendations (10 inboxes + platform, monthly billing)

**Best overall: Primeforge + Smartlead Base — ~$87.50/mo** ($45 inboxes + ~$3.50 domains amortized + $39 platform). Primeforge's 10-slot minimum matches the need exactly, pre-warming is bundled rather than a paywalled add-on, you choose Google or Microsoft per mailbox (useful for ESP-matching), and slots let you rotate burned mailboxes free. Smartlead Base beats Instantly Growth on price ($39 vs $47), contacts (2,000 vs 1,000), and send cap (6,000 vs 5,000). Drops to ~$80/mo on annual inbox billing.

**Cheapest verified: Zapmail Starter + Smartlead Base — ~$81/mo** ($39 + ~$3.25 domains + $39) — but only if you take *standard* mailboxes and warm them via Smartlead's included warm-up pool (2–3 weeks before real sends), because Zapmail's pre-warmed premium isn't public ($6–8/mailbox per third parties, which erases the savings). The India-reseller tenant question is the other reason it ranks below Primeforge for a US-targeting operation.

**Litemail: credible middle option — ~$79–89/mo pre-warmed** (10 pre-warmed inboxes ~$40–50 with domains *included*, + Smartlead $39). Domains-included pre-warmed plans are the cleanest "send day one" package of the three, but the exact pre-warmed per-inbox rate could not be verified on their site (pricing page 404; homepage says "from $4"). Confirm the number at checkout before committing.

**Changed vs. 2025 assumptions:**
1. **Instantly Growth is now $47/mo, not $37/mo**, and carries a hard 1,000-contact / 5,000-email cap — it no longer works as the default "cheap unlimited-ish starter plan." Smartlead Base is now the better entry plan for this shape of operation.
2. **Budget line for the platform breaks at scale-up:** at 40–50/day/inbox you'll need a ~$94–97 plan on either platform. Plan the upgrade, or hold at ~25/day/inbox on Smartlead Base.
3. Inbox pricing has continued to fall — $3.50–4.50/inbox is now the market rate (vs ~$5–7 assumptions from 2025), so the $50–80 inbox budget is comfortably oversized; 10 pre-warmed inboxes + 3 domains lands at $40–55/mo everywhere.

## Sources
- Vendor pages (fetched directly): primeforge.ai/pricing, litemail.ai, litemail.ai/bulk-email-inboxes, zapmail.ai, zapmail.ai/Pre-Warmed-Mailboxes, instantly.ai/pricing, smartlead.ai/pricing
- Third-party (used where vendor pages were silent/404): ColdEmailKit Primeforge review (pre-warmed included at no premium), InboxKit Zapmail pricing ($6–8 pre-warmed premium, $13 domains), PuzzleInbox Zapmail review (India-reseller tenant concern)
