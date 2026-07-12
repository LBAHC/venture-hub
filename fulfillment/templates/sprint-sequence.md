# Template — Sprint Campaign: 3-Touch Renewal Sequence (client-branded)

Sent AS the agency, FROM their systems/domain, in their voice (calibrated from intake voice samples). These are skeletons — every sprint gets a voice pass before the client approval gate. Compliance rails baked in: agency physical address in footer, working opt-out honored into per-client suppression list, state send-windows respected (FL 8am–8pm, etc.), email only.

Merge fields: {client_first}, {policy_type}, {renewal_date}, {producer_first}, {producer_calendar}, {agency_name}, {agency_phone}

---

## T1 — sent at entry (policy is 45–90 days from renewal)
Subject: Your {policy_type} renewal — {renewal_date}

Hi {client_first},

Your {policy_type} policy renews on {renewal_date}, and we like to get ahead of it rather than send you a surprise bill.

A few things have moved in the market this year — rates, coverage options, discounts you may now qualify for. Before your renewal is finalized, it's worth a quick look to make sure you're not paying for coverage you don't need (or missing coverage you do).

Nothing is required from you today. If you'd like us to review your policy before renewal, just reply to this email or call {agency_phone}.

— {producer_first} at {agency_name}

*[footer: agency address · reply "unsubscribe" or click here to stop renewal reminders]*

---

## T2 — entry +5 days (value touch, no pressure)
Subject: Quick question about your {policy_type} coverage

Hi {client_first},

While prepping your {renewal_date} renewal, one thing worth checking: has anything changed this year? New car, home projects, a teenager driving, a business on the side — small changes can mean discounts you're missing or gaps you don't want to find out about during a claim.

A 10-minute coverage checkup before renewal usually pays for itself. No obligation — it's your policy, we just want it right.

Reply here and {producer_first} will take a look.

— {agency_name}

*[footer]*

---

## T3 — entry +12 days (direct ask)
Subject: Let's lock in your renewal — 15 minutes with {producer_first}

Hi {client_first},

Your renewal on {renewal_date} is getting close. Grab 15 minutes with {producer_first} and we'll walk through your options before anything auto-renews:

**{producer_calendar}**

Prefer email or a call? Reply here or dial {agency_phone} — whatever's easiest.

We'd rather review it with you than have you wonder if you should be shopping. That's the whole point of working with an independent agency.

— {producer_first} at {agency_name}

*[footer]*

---

## Send rules (enforced in whatever tool runs this)
- Business hours in RECIPIENT's timezone; FL recipients 8am–8pm hard window; frequency caps per state table (docs/research-addendum.md §B)
- Opt-out: any reply expressing "stop/remove/unsubscribe" → suppression list same day, all channels, logged
- Reply handling: forwarded to {producer_email} instantly; unanswered replies flagged to us at 4 business hours → nudge producer
- No sends to policyholders with open claims if flagged in intake exclusions
