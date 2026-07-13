# Feasibility: Harvesting ~500–1,000 public reviews of US independent P&C agencies
*Actual fetch attempts made July 12, 2026 — findings are tested, not assumed.*

## Route 1: Google Maps (direct + official API)
**Direct fetch: BLOCKED (confirmed).** Maps URLs return an empty JS shell — zero review content. Not viable without a headless browser + anti-bot fight.

**Official Places API: works, capped, effectively $0.**
- `reviews` field returns **max 5 reviews per place**, Google-selected "most relevant," no pagination (unchanged since 2015).
- Requesting `reviews` = Enterprise + Atmosphere SKU (~$25–40/1,000 calls) — BUT since Google's March 2025 pricing change, each Enterprise SKU gets **1,000 free calls/month** (Pro SKUs like Text Search get 5,000 free).
- Math: 1,000 agencies × 1 Place Details call = exactly the free Enterprise cap → **up to 5,000 full review texts for $0, fully ToS-compliant.** Caveats: Google curates which 5 reviews (selection bias); Maps ToS restricts long-term caching (fine for one-time analysis; quote reviews, don't republish the dataset).

## Route 2: Yelp — dead end
Direct fetch 403-blocked (confirmed, desktop + mobile); ToS prohibits scraping. Official Fusion API returns only 3 excerpts/business truncated to 160 chars. Volume thin anyway (a large metro ≈ 100–300 agency reviews total). Skip.

## Route 3: BBB (bbb.org) — works as a supplement
**Full review text fetches cleanly (confirmed).** Sample pulled: Branch Insurance (Columbus OH), 43 reviews with dates — e.g. *"I have had nothing but increases well over the $900 each and every year for the last consecutive three years"* (06/12/2026) — exactly the renewal-experience material wanted. Catch: small local independents carry 0–3 BBB reviews; the deep pages are insurtechs/national brands. BBB ToS prohibits automated scraping — modest targeted pulls for quoted excerpts is the defensible use. **Great free supplement for vivid renewal narratives, not the backbone.**

## Route 4: Paid scrapers (day-of pricing)
- **Apify Google Maps Reviews Scraper:** $0.30/1,000 reviews, full text + dates. **Free plan includes $5/mo credit** → ~15,000 reviews + place discovery = $0 out of pocket.
- **Outscraper:** first 500 Google reviews/mo free, PAYG after.
- ToS note: these scrape Google Maps in violation of Google's ToS (favorable US public-data case law à la hiQ notwithstanding — it remains a ToS breach posture).

## Route 5: Other sources
- Trustpilot: 403-blocked (confirmed); skews national insurtech. Skip.
- Clearsurance: zombie site (lead-gen redirect since ~2024). Skip.
- Agency-owned testimonial pages: fetch cleanly but curated/positive-only — unusable for an honest data piece.

## Recommendation
**Primary (ToS-clean, $0): official Google Places API** — Text Search (5K free Pro calls) to find ~1,000 independent agencies + Place Details with `reviews` (1K free Enterprise calls) → up to 5,000 review texts. At a 5–15% renewal-relevance hit rate → **~250–750 renewal-relevant texts**; widen across 2 monthly quota cycles if needed. Requires a Google Cloud account + API key (billing enabled but usage stays in free tier) — Luke signup.
**Alternative (higher volume, ToS-gray): Apify free plan** — 10–20K reviews → 500–1,500 renewal-relevant texts, ~$0. Breaches Google's ToS; conflicts with our "compliance-safe by design" brand posture if ever surfaced.
**Supplement (free): targeted BBB pulls** for narrative quotes.

Total cost: $0 either way. Yelp/Trustpilot confirmed dead ends.
