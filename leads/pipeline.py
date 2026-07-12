#!/usr/bin/env python3
"""
AgencyRetain lead pipeline — Apollo export -> clean, dedupe, exclude captives,
segment into outreach angles, emit per-angle CSVs + a stats summary.

Usage:
    python3 pipeline.py apollo_export.csv [more_exports.csv ...]

Outputs (into leads/, all gitignored):
    segment_A_retention.csv   established agencies, 5-15 staff  -> Angle A
    segment_B_shelfware.csv   detectable marketing tool in use  -> Angle B
    segment_C_quotefollow.csv ad/lead-buying signals            -> Angle C
    excluded.csv              captives, out-of-range, junk (with reason column)
    pipeline_stats.txt        counts at every stage

Stdlib only — no installs needed. Verification (NeverBounce/Prospeo) happens
AFTER this script, on the segment files; nothing sends above 2% bounce.
"""
import csv
import re
import sys
from pathlib import Path

# ── config ──────────────────────────────────────────────────────────────────
# Captive/exclusion brands: corporate handles retention, or they're not our buyer.
CAPTIVE_BRANDS = [
    "state farm", "allstate", "farmers insurance", "farmers agent",
    "american family", "amfam", "geico", "progressive", "usaa",
    "liberty mutual", "shelter insurance", "country financial",
    "farm bureau", "nationwide",  # nationwide kept some captives; safer out
]

# Tool signals for Angle B (matched against tech/keywords/website columns
# Apollo provides, when present).
SHELFWARE_TOOLS = ["levitate", "agency revolution", "fuse", "agencyzoom",
                   "better agency", "insuredmine", "gohighlevel", "highlevel"]

# Ad-spend / lead-gen signals for Angle C.
AD_SIGNALS = ["google ads", "adwords", "facebook ads", "meta ads",
              "call tracking", "callrail", "smartfinancial", "everquote",
              "quotewizard"]

TITLE_OK = re.compile(
    r"owner|principal|president|founder|ceo|managing (partner|member|director)",
    re.I)

HEADCOUNT_MIN, HEADCOUNT_MAX = 2, 15

# Column aliases — Apollo exports drift; extend here rather than editing logic.
COLS = {
    "email":     ["email", "work email"],
    "first":     ["first name", "first_name"],
    "last":      ["last name", "last_name"],
    "title":     ["title", "job title"],
    "company":   ["company", "company name", "organization"],
    "website":   ["website", "company website", "domain", "company domain"],
    "employees": ["# employees", "employees", "employee count", "headcount",
                  "num employees"],
    "state":     ["state", "company state", "contact state"],
    "city":      ["city", "company city"],
    "phone":     ["company phone", "phone", "work direct phone"],
    "keywords":  ["keywords", "technologies", "seo description",
                  "short description"],
}

FREE_MAIL = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
             "aol.com", "icloud.com", "msn.com", "comcast.net"}


# ── helpers ─────────────────────────────────────────────────────────────────
def pick(row, key):
    """Get a field by alias list, case-insensitive."""
    lower = {k.strip().lower(): v for k, v in row.items() if k}
    for alias in COLS[key]:
        if alias in lower and lower[alias]:
            return lower[alias].strip()
    return ""


def parse_headcount(raw):
    """'11-20' -> 11, '5' -> 5, '' -> None."""
    m = re.search(r"\d+", raw or "")
    return int(m.group()) if m else None


def email_domain(email):
    return email.rsplit("@", 1)[-1].lower() if "@" in email else ""


def contains_any(haystack, needles):
    hay = haystack.lower()
    return next((n for n in needles if n in hay), None)


# ── pipeline ────────────────────────────────────────────────────────────────
def run(paths):
    out_dir = Path(__file__).parent
    rows, seen_emails, seen_domains = [], set(), set()
    stats = {"read": 0, "no_email": 0, "dupe": 0, "captive": 0,
             "bad_title": 0, "headcount": 0, "kept": 0,
             "A": 0, "B": 0, "C": 0}
    excluded = []

    for path in paths:
        with open(path, newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                stats["read"] += 1
                email = pick(row, "email").lower()
                company = pick(row, "company")
                title = pick(row, "title")
                blob = " ".join([company, pick(row, "website"),
                                 pick(row, "keywords")])

                def drop(reason):
                    excluded.append({"email": email, "company": company,
                                     "title": title, "reason": reason})

                if not email or "@" not in email:
                    stats["no_email"] += 1
                    drop("no email")
                    continue

                dom = email_domain(email)
                # Dedupe: one contact per agency domain (principal preferred —
                # Apollo sorts by seniority when title filters applied).
                dedupe_key = email if dom in FREE_MAIL else dom
                if email in seen_emails or dedupe_key in seen_domains:
                    stats["dupe"] += 1
                    drop("duplicate")
                    continue

                brand = contains_any(blob, CAPTIVE_BRANDS)
                if brand:
                    stats["captive"] += 1
                    drop(f"captive: {brand}")
                    continue

                if title and not TITLE_OK.search(title):
                    stats["bad_title"] += 1
                    drop("not owner/principal")
                    continue

                hc = parse_headcount(pick(row, "employees"))
                if hc is not None and not (HEADCOUNT_MIN <= hc <= HEADCOUNT_MAX):
                    stats["headcount"] += 1
                    drop(f"headcount {hc}")
                    continue

                seen_emails.add(email)
                seen_domains.add(dedupe_key)

                # Segment: B (shelfware) wins if tool detected, then C (ads),
                # else A. B converts fastest per plan — priority is deliberate.
                tool = contains_any(blob, SHELFWARE_TOOLS)
                ad = contains_any(blob, AD_SIGNALS)
                segment = "B" if tool else ("C" if ad else "A")
                stats[segment] += 1
                stats["kept"] += 1

                rows.append({
                    "email": email,
                    "first_name": pick(row, "first"),
                    "last_name": pick(row, "last"),
                    "title": title,
                    "agency_name": company,
                    "website": pick(row, "website"),
                    "city": pick(row, "city"),
                    "state": pick(row, "state"),
                    "phone": pick(row, "phone"),
                    "headcount": hc if hc is not None else "",
                    "tool_detected": tool or "",
                    "ad_signal": ad or "",
                    "segment": segment,
                    # filled by the enrichment pass (first_lines.py, later):
                    "first_line": "",
                })

    # ── write outputs ──
    fields = list(rows[0].keys()) if rows else ["email"]
    names = {"A": "segment_A_retention.csv",
             "B": "segment_B_shelfware.csv",
             "C": "segment_C_quotefollow.csv"}
    for seg, fname in names.items():
        seg_rows = [r for r in rows if r["segment"] == seg]
        with open(out_dir / fname, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(seg_rows)

    if excluded:
        with open(out_dir / "excluded.csv", "w", newline="",
                  encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["email", "company", "title",
                                              "reason"])
            w.writeheader()
            w.writerows(excluded)

    summary = (
        f"read {stats['read']} | kept {stats['kept']} "
        f"(A:{stats['A']} B:{stats['B']} C:{stats['C']})\n"
        f"dropped: no_email {stats['no_email']}, dupes {stats['dupe']}, "
        f"captive {stats['captive']}, title {stats['bad_title']}, "
        f"headcount {stats['headcount']}\n"
        f"NEXT: verify each segment file (NeverBounce/Prospeo) — "
        f"<2% bounce required before any send.\n")
    (out_dir / "pipeline_stats.txt").write_text(summary)
    print(summary)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run(sys.argv[1:])
