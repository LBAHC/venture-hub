#!/usr/bin/env python3
"""
Review-corpus collection for the renewal data piece, via Apify.

Phase A: discover independent insurance agencies in target metros
         (compass/crawler-google-places).
Phase B: pull reviews for the discovered places, capped per place
         (compass/google-maps-reviews-scraper).
Phase C: filter reviews for renewal-relevant keywords.

Budget guard: sized to stay inside Apify's ~$5/mo free credit —
10 metros x 35 places, top 300 places by review count, 30 reviews/place.
Do NOT raise the caps without checking account usage first.

Usage:  python3 collect_reviews.py            (reads APIFY_TOKEN from ../.env)
Output: ../data/places.json, ../data/reviews.json, ../data/renewal_hits.json
        + printed stats. data/ is gitignored — raw corpus never commits.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
API = "https://api.apify.com/v2"

METROS = [  # Tier 1 churn-pain + top Tier 2 (leads/metros.md)
    "Tampa FL", "Orlando FL", "Houston TX", "Dallas TX", "San Antonio TX",
    "New Orleans LA", "Oklahoma City OK", "Denver CO",
    "Columbus OH", "Pittsburgh PA",
]
MAX_PLACES_PER_SEARCH = 35
MAX_REVIEW_PLACES = 300
MAX_REVIEWS_PER_PLACE = 30

CAPTIVE = ["state farm", "allstate", "farmers", "american family", "geico",
           "progressive", "usaa", "liberty mutual", "farm bureau",
           "shelter insurance", "country financial", "goosehead"]

RENEWAL_PAT = re.compile(
    r"renew|rate increase|rates? (went|going) up|premium (went|going) up|"
    r"premium increase|shopped? around|shopping around|price[d]? increase|"
    r"went up (every|each) year|nobody (called|reached)|no one (called|reached)|"
    r"auto[- ]renew|non[- ]?renew", re.I)


def token():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("APIFY_TOKEN="):
            return line.split("=", 1)[1].strip()
    sys.exit("APIFY_TOKEN not found in .env")


TOKEN = token()


def api(method, path, body=None, timeout=60):
    url = f"{API}{path}{'&' if '?' in path else '?'}token={TOKEN}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def run_actor(actor, payload, label, max_wait_min=45):
    print(f"[{label}] starting {actor} ...", flush=True)
    run = api("POST", f"/acts/{actor}/runs", payload)["data"]
    run_id = run["id"]
    t0 = time.time()
    while True:
        time.sleep(30)
        st = api("GET", f"/actor-runs/{run_id}")["data"]
        status = st["status"]
        mins = (time.time() - t0) / 60
        print(f"[{label}] {status} ({mins:.1f} min)", flush=True)
        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            break
        if mins > max_wait_min:
            print(f"[{label}] exceeded {max_wait_min} min — aborting run")
            api("POST", f"/actor-runs/{run_id}/abort", {})
            break
    if status != "SUCCEEDED":
        sys.exit(f"[{label}] run ended {status} — stopping (check Apify "
                 f"console; free credit may be exhausted)")
    ds = st["defaultDatasetId"]
    items, offset = [], 0
    while True:
        page = api("GET", f"/datasets/{ds}/items?format=json&clean=true"
                          f"&offset={offset}&limit=1000", timeout=120)
        items.extend(page)
        if len(page) < 1000:
            return items
        offset += 1000


def main():
    DATA.mkdir(exist_ok=True)

    # ── Phase A: place discovery ──
    places = run_actor("compass~crawler-google-places", {
        "searchStringsArray": [f"independent insurance agency {m}"
                               for m in METROS],
        "maxCrawledPlacesPerSearch": MAX_PLACES_PER_SEARCH,
        "language": "en",
        "skipClosedPlaces": True,
        "scrapeContacts": False,
        "maxImages": 0,
        "maxReviews": 0,
        "maxQuestions": 0,
    }, "places")
    print(f"[places] raw: {len(places)}")

    keep = []
    seen = set()
    for p in places:
        title = (p.get("title") or "").lower()
        pid = p.get("placeId") or p.get("url")
        if not pid or pid in seen or any(c in title for c in CAPTIVE):
            continue
        if (p.get("reviewsCount") or 0) < 3:
            continue
        seen.add(pid)
        keep.append({
            "placeId": p.get("placeId"), "url": p.get("url"),
            "title": p.get("title"), "city": p.get("city"),
            "state": p.get("state"), "website": p.get("website"),
            "reviewsCount": p.get("reviewsCount"),
            "totalScore": p.get("totalScore"), "phone": p.get("phone"),
        })
    keep.sort(key=lambda p: p["reviewsCount"] or 0, reverse=True)
    (DATA / "places.json").write_text(json.dumps(keep, indent=1))
    targets = keep[:MAX_REVIEW_PLACES]
    print(f"[places] kept {len(keep)} independents (>=3 reviews); "
          f"pulling reviews for top {len(targets)}")

    # ── Phase B: reviews ──
    reviews = run_actor("compass~google-maps-reviews-scraper", {
        "startUrls": [{"url": p["url"]} for p in targets if p.get("url")],
        "maxReviews": MAX_REVIEWS_PER_PLACE,
        "reviewsSort": "newest",
        "language": "en",
        "personalData": False,
    }, "reviews")
    (DATA / "reviews.json").write_text(json.dumps(reviews, indent=1))
    print(f"[reviews] collected {len(reviews)}")

    # ── Phase C: renewal filter ──
    hits = []
    for r in reviews:
        text = r.get("text") or ""
        if text and RENEWAL_PAT.search(text):
            hits.append({
                "place": r.get("title"), "placeUrl": r.get("url"),
                "stars": r.get("stars"), "date": r.get("publishedAtDate"),
                "text": text,
            })
    (DATA / "renewal_hits.json").write_text(json.dumps(hits, indent=1))

    with_text = sum(1 for r in reviews if r.get("text"))
    print("\n=== SUMMARY ===")
    print(f"agencies discovered (independent, >=3 reviews): {len(keep)}")
    print(f"reviews collected: {len(reviews)} ({with_text} with text)")
    print(f"renewal-relevant: {len(hits)} "
          f"({100 * len(hits) / max(1, with_text):.1f}% of text reviews)")
    print("next: Claude analyzes data/renewal_hits.json -> data piece draft")


if __name__ == "__main__":
    main()
