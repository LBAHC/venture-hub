# Lead Pipeline — how a list gets built

Target: 1,500 verified agency-principal contacts by end of Day 1 flow, 3,000 by Day 3, split across Angles A/B/C. All CSVs in this folder are gitignored — only scripts and docs get committed.

## Step 1 — Apollo export (Luke's account, ~10 min)
Filters (per docs/lead-data-strategy.md):
- Industry: **Insurance** · Location: **United States**
- Headcount: **2–15**
- Titles: **owner, principal, president, founder, agency principal**
- Company name EXCLUDES: State Farm, Allstate, Farmers, American Family
- Email status: verified preferred
Export CSV(s) into this folder.

## Step 2 — Clean + segment (automated)
```
python3 pipeline.py apollo_export.csv
```
Dedupes by agency domain, drops captives/wrong titles/wrong size, and splits into:
- `segment_A_retention.csv` — established agencies → "renewal leakage math" angle
- `segment_B_shelfware.csv` — detectable Levitate/Fuse/AgencyZoom/etc. → "shelfware" angle (priority: fastest conversion + case-study targets)
- `segment_C_quotefollow.csv` — ad-spend signals → "quotes that went quiet" angle
- `excluded.csv` + `pipeline_stats.txt` for the audit trail

Apollo's tool-detection columns are weak for niche insurance tools, so Segment B will be undersized at first — the enrichment pass (step 3) is what really populates it.

## Step 3 — Enrichment / personalization (Claude, scripted)
`first_lines.py` (to be built when list exists): visits each agency website, extracts carriers represented (independence check), tools in footer/careers pages (→ reassign to Segment B), and writes the personalized `first_line` used by all outreach touch-1s. Runs in batches; output reviewed before import.

## Step 4 — Verification (BLOCKING)
Run every segment file through NeverBounce or Prospeo. **<2% projected bounce or the file does not go into Smartlead.** Keep the verifier's export as the audit record.

## Step 5 — Import to Smartlead
One campaign per angle (A/B/C), ~1,000 contacts each at full list. Sending caps live in the platform: 20–25/day/inbox week 1, never past 50. Kill rule: <1% reply after 500 sends.

## Cross-reference (optional, later)
RI DBR publishes free quarterly producer bulk files (see research/fulfillment-stack-2026-07-12.md for URLs) — useful to spot-check active licensure in RI, not a primary source. NIPR PDB is **off-limits** (FCRA restriction — legal tripwire, see lead-data-strategy).
