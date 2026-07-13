# Smartlead Campaign Spec — paste-ready for account day
Three campaigns (Angle A/B/C from sequences-v1.md), identical settings except audience + copy. Kill rule: <1% reply after 500 sends per angle.

## Global settings (all campaigns)
- **Sending accounts:** all 10 inboxes attached to every campaign (Smartlead rotates); per-inbox daily cap **22** week 1 → raise to 40 only after clean week-1 Postmaster data
- **Schedule:** Mon–Fri, 8:40am–4:20pm **recipient's timezone**, randomized intervals (never round numbers/instant bursts)
- **Warm-up:** ON for all inboxes, permanent, alongside campaigns
- **Tracking:** open tracking OFF touch 1–2 (deliverability > vanity metrics), click tracking OFF until links appear in touch 3; custom tracking domain per sending domain
- **Plain text only** touches 1–2; no images anywhere in the sequence
- **Stop-on-reply:** stop entire sequence on any reply; auto-pause contact on OOO for 7 days
- **Unsubscribe:** touch 1–2 use reply-to-opt-out language (in copy); touches 3–4 include list-unsubscribe footer with agency-required physical address
- **Bounce guard:** campaign auto-pauses if bounce >2% (manual check daily until automated)

## Campaign 1 — "A / Retention math"
- Audience: `segment_A_retention.csv` (verified, enriched, first_line filled)
- Sequence: sequences-v1.md Angle A, touches at day 0 / 3 / 7 / 12
- Spintax: 2 subject variants for T1 (`{agency_name} renewals` / `renewals at {agency_name}`) — Smartlead A/B at 50/50

## Campaign 2 — "B / Shelfware" (priority — case-study source)
- Audience: `segment_B_shelfware.csv` — includes enrichment-detected tool users
- Sequence: Angle B; T1 subject personalizes detected tool where known: `your {tool} setup`
- Replies from this campaign get first crack at the 2 FREE case-study sprints

## Campaign 3 — "C / Quote follow-up"
- Audience: `segment_C_quotefollow.csv`
- Sequence: Angle C, same cadence

## Launch-day checklist
1. DNS gate passed (ops/dns-auth-runbook.md) — hard blocker
2. Lists verified <2% projected bounce — hard blocker
3. `first_line` present on ≥95% of rows; rows without it held back
4. Send a 5-contact internal seed test through each campaign; check rendering + footer + opt-out
5. Start all three at 1/3 volume day 1, full cap day 3 if bounces clean
6. Log daily to ops/metrics.md: sends, deliverability%, replies, positive, per angle

## A/B log
Maintain outreach/ab-log.md from day 1: date, angle, variant, sends, replies, decision. Kills and scale-ups cite this file in the decision log.
