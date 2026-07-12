# Lead Data Strategy v2 (verified July 10, 2026)

## Key corrections from research
1. **Do NOT use NIPR Producer Database (PDB)** — access is FCRA-restricted to "permissible purpose"; marketing is not one. Legal tripwire, avoid entirely.
2. State DOI data is uneven: RI posts free quarterly bulk CSVs; CA sells lists via mail-order form (+check, slow); most states offer lookup-only tools (scrape-hostile, slow).
3. **License lists = individual agents, not agencies.** Our buyer is the agency principal. Individual producer lists are noisy (captive agents, employees, inactive). Demoted to cross-reference.

## Primary pipeline (Day 1)
1. **Apollo**: filters — industry: insurance; headcount 2–15; titles: owner/principal/president/agency principal; US; exclude captive brands (State Farm, Allstate, Farmers, American Family in company name). Export w/ emails.
2. **Google Maps scrape** by metro: "independent insurance agency" — yields agency name, site, phone, review count/rating (budget-signal), owner name often on site.
3. **Enrichment merge**: AI extracts from agency websites — carriers represented (independence check), lines of business, staff size, tools in footer/careers pages (Levitate/Fuse badge = Angle B target).
4. **Verification**: NeverBounce/Prospeo, enforce <2% bounce pre-send.
5. Cross-reference free state bulk files (RI-style) where they exist to confirm active licensure.

## Segmentation for angles
- Angle B (shelfware): agencies with detectable Levitate/Fuse/AgencyZoom/Better Agency usage
- Angle A (retention math): 5–15 staff, established (10+ yrs, high review counts)
- Angle C (quote follow-up): agencies running Google Ads / active lead-buying signals

## Volume targets
- Day 3: 3,000 verified agency-principal contacts across 3 segments
- Cost estimate: Apollo credits + verification ≈ $100–150 (within budget line)
- Fallback if Apollo yield is poor: insuranceagentlists.com $249/state (annual refresh — verify sample first)
