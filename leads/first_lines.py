#!/usr/bin/env python3
"""
Enrichment pass — fetch each agency's website via Firecrawl, extract signals,
and stage the data Claude uses to write personalized first lines.

Usage:
    FIRECRAWL_API_KEY=fc-... python3 first_lines.py segment_A_retention.csv
    (or put the key in ../.env as FIRECRAWL_API_KEY=...)

For each row with a website, writes an enriched copy of the CSV
(<input>_enriched.csv) adding:
    site_ok          fetch succeeded
    carriers         carrier names found on the site (independence check)
    tools_detected   Levitate/Fuse/AgencyZoom/etc found in site text
                     -> rows gain candidates for reassignment to Segment B
    years_signal     "since 1987" / "35 years" style established-agency signals
    site_excerpt     first ~1,200 chars of readable site text (Claude's raw
                     material for the first line — the LLM step happens in a
                     Claude session over this file, NOT in this script)

Rate: ~2 req/sec max, resumable (skips rows already enriched). Stdlib only.
"""
import csv
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

API = "https://api.firecrawl.dev/v1/scrape"

CARRIERS = ["progressive", "travelers", "safeco", "liberty mutual", "hartford",
            "nationwide", "chubb", "cincinnati", "auto-owners", "erie",
            "grange", "westfield", "hanover", "encompass", "foremost",
            "national general", "berkshire", "kemper", "mercury", "dairyland"]

TOOLS = ["levitate", "agency revolution", "fuse", "agencyzoom",
         "better agency", "insuredmine", "gohighlevel", "highlevel",
         "rocket referrals", "clientcircle"]

YEARS = re.compile(r"(since\s+(19|20)\d{2}|(\d{2,3})\s*\+?\s*years)", re.I)


def api_key():
    key = os.environ.get("FIRECRAWL_API_KEY", "")
    env = Path(__file__).parent.parent / ".env"
    if not key and env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("FIRECRAWL_API_KEY="):
                key = line.split("=", 1)[1].strip()
    if not key:
        sys.exit("No FIRECRAWL_API_KEY in environment or ../.env")
    return key


def scrape(url, key):
    body = json.dumps({"url": url, "formats": ["markdown"],
                       "onlyMainContent": True, "timeout": 20000}).encode()
    req = urllib.request.Request(
        API, data=body, method="POST",
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.load(r)
    if not data.get("success"):
        raise RuntimeError(data.get("code") or "scrape_failed")
    return (data.get("data") or {}).get("markdown", "") or ""


def extract(md):
    low = md.lower()
    carriers = [c for c in CARRIERS if c in low]
    tools = [t for t in TOOLS if t in low]
    m = YEARS.search(md)
    # drop cookie-banner / consent / nav junk lines before excerpting
    keep = [ln for ln in md.splitlines()
            if ln.strip() and not re.search(
                r"cookie|consent|privacy polic|!\[|\bmenu\b|skip to",
                ln, re.I)]
    excerpt = re.sub(r"\s+", " ", " ".join(keep))[:1200]
    return carriers, tools, (m.group(0) if m else ""), excerpt


def run(path):
    key = api_key()
    src = Path(path)
    out = src.with_name(src.stem + "_enriched.csv")

    done = set()
    if out.exists():  # resumable
        with open(out, newline="", encoding="utf-8") as f:
            done = {r["email"] for r in csv.DictReader(f)}

    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    new_fields = ["site_ok", "carriers", "tools_detected", "years_signal",
                  "site_excerpt"]
    fields = list(rows[0].keys()) + [c for c in new_fields
                                     if c not in rows[0]]
    mode = "a" if done else "w"
    with open(out, mode, newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if not done:
            w.writeheader()
        ok = fail = skip = 0
        for r in rows:
            if r["email"] in done:
                continue
            url = (r.get("website") or "").strip()
            if url and not url.startswith("http"):
                url = "https://" + url
            if not url:
                r.update(dict.fromkeys(new_fields, ""))
                r["site_ok"] = "no_site"
                skip += 1
            else:
                try:
                    md = scrape(url, key)
                    carriers, tools, years, excerpt = extract(md)
                    r.update(site_ok="yes",
                             carriers="; ".join(carriers),
                             tools_detected="; ".join(tools),
                             years_signal=years,
                             site_excerpt=excerpt)
                    ok += 1
                except Exception as e:  # noqa: BLE001 — log & continue batch
                    r.update(dict.fromkeys(new_fields, ""))
                    r["site_ok"] = f"error: {e}"[:80]
                    fail += 1
                time.sleep(0.6)
            w.writerow(r)
            if (ok + fail) % 25 == 0 and (ok + fail):
                print(f"  ...{ok} ok / {fail} failed / {skip} no-site")
    print(f"done: {ok} enriched, {fail} failed, {skip} without sites -> {out}")
    print("NEXT: Claude session writes first_line per row from site_excerpt; "
          "rows with tools_detected move to Segment B.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    run(sys.argv[1])
