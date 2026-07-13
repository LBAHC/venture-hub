#!/usr/bin/env python3
"""
Sprint Day 1-2: book analysis. Parses a client's book export / renewal report
CSV and computes every number the Leakage Snapshot template needs, plus the
sprint segment selection.

Usage:
    python3 book_analysis.py client_book.csv [--asof 2026-07-12]

Expected columns (aliases handled; extend COLS as real AMS exports appear —
every AMS names these differently):
    policy id, insured/household name, line (auto/home/etc), premium,
    renewal/expiration date, email (optional)

Output: <input>_snapshot.json + a printed summary. The JSON feeds
templates/leakage-snapshot.md; Claude writes the prose, this script owns
the arithmetic (numbers must never be improvised).

Stdlib only. Client CSVs never leave the per-client folder; never commit them.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

COLS = {
    "policy":  ["policy id", "policy number", "policy #", "policy", "pol_num"],
    "insured": ["insured", "insured name", "household", "customer",
                "named insured", "client name", "account name"],
    "line":    ["line", "line of business", "lob", "policy type", "type",
                "product"],
    "premium": ["premium", "annual premium", "written premium", "full term premium",
                "total premium"],
    "renewal": ["renewal date", "expiration date", "expiration", "exp date",
                "renewal", "x-date", "xdate", "effective to"],
    "email":   ["email", "insured email", "contact email"],
}

DATE_FMTS = ["%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%m-%d-%Y", "%d-%b-%Y",
             "%b %d, %Y", "%Y/%m/%d"]

# sprint segment window + priority premium threshold (per playbook)
WIN_LO, WIN_HI = 45, 90
NEXT_LO, NEXT_HI = 91, 120


def pick(row, key):
    lower = {k.strip().lower(): v for k, v in row.items() if k}
    for alias in COLS[key]:
        if alias in lower and lower[alias] not in (None, ""):
            return str(lower[alias]).strip()
    return ""


def parse_money(raw):
    m = re.sub(r"[^0-9.]", "", raw or "")
    try:
        return float(m) if m else 0.0
    except ValueError:
        return 0.0


def parse_date(raw):
    raw = (raw or "").strip()
    for fmt in DATE_FMTS:
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    return None


def run(path, asof):
    rows, skipped = [], 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            renewal = parse_date(pick(row, "renewal"))
            if not renewal:
                skipped += 1
                continue
            rows.append({
                "policy": pick(row, "policy"),
                "insured": pick(row, "insured"),
                "line": pick(row, "line").lower() or "unknown",
                "premium": parse_money(pick(row, "premium")),
                "renewal": renewal,
                "days_out": (renewal - asof).days,
            })

    if not rows:
        sys.exit(f"No parseable rows (skipped {skipped}). Check column names "
                 f"against COLS aliases and date formats.")

    # households: group by insured name (normalized) to find single-line ones
    lines_per_household = defaultdict(set)
    for r in rows:
        key = re.sub(r"\W+", "", r["insured"].lower())
        if key:
            lines_per_household[key].add(r["line"])

    def household_single(r):
        key = re.sub(r"\W+", "", r["insured"].lower())
        return len(lines_per_household.get(key, {1})) == 1

    sprint = [r for r in rows if WIN_LO <= r["days_out"] <= WIN_HI]
    nxt = [r for r in rows if NEXT_LO <= r["days_out"] <= NEXT_HI]
    premiums = sorted((r["premium"] for r in sprint if r["premium"]),
                      reverse=True)
    # priority threshold: top-quartile premium within the sprint window
    threshold = premiums[len(premiums) // 4] if premiums else 0

    snapshot = {
        "asof": asof.isoformat(),
        "total_policies": len(rows),
        "rows_skipped_unparseable": skipped,
        "sprint_window": {
            "policies": len(sprint),
            "premium": round(sum(r["premium"] for r in sprint), 2),
            "single_line_households": sum(1 for r in sprint
                                          if household_single(r)),
            "priority_premium_threshold": round(threshold, 2),
            "priority_policies": sum(1 for r in sprint
                                     if r["premium"] >= threshold > 0),
            "by_line": dict(Counter(r["line"] for r in sprint)),
            "by_month": dict(Counter(r["renewal"].strftime("%Y-%m")
                                     for r in sprint)),
        },
        "next_wave_91_120": {
            "policies": len(nxt),
            "premium": round(sum(r["premium"] for r in nxt), 2),
        },
        "cross_sell_flag_count": sum(1 for r in rows if household_single(r)),
        "segment_recommendation": (
            "Policies renewing in 45-90 days; producer-call priority on the "
            f"{sum(1 for r in sprint if r['premium'] >= threshold > 0)} "
            f"policies at/above ${threshold:,.0f} premium; single-line "
            "households noted for the retainer report only."),
    }

    out = Path(path).with_suffix("").name + "_snapshot.json"
    out_path = Path(path).parent / out
    out_path.write_text(json.dumps(snapshot, indent=2))
    print(json.dumps(snapshot, indent=2))
    print(f"\n-> {out_path}\nNumbers feed templates/leakage-snapshot.md — "
          "Claude writes prose, never new numbers.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    asof = date.today()
    if len(sys.argv) == 4 and sys.argv[2] == "--asof":
        asof = parse_date(sys.argv[3]) or asof
    run(sys.argv[1], asof)
