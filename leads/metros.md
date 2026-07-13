# Target Metros — Google Maps discovery list
Used for: (a) lead-gen Maps scrape fallback/supplement, (b) the review-analysis data piece (Apify place discovery). Selection logic: metros with dense independent-agency populations, weather/catastrophe-driven premium churn (renewal shopping pain = our pitch), and a spread across regions. Captive-heavy markets are fine — the filter removes captives.

## Tier 1 — churn-pain markets (rate turmoil = renewal shopping = agency pain)
1. Tampa, FL · 2. Orlando, FL · 3. Jacksonville, FL · 4. Houston, TX · 5. Dallas–Fort Worth, TX · 6. San Antonio, TX · 7. New Orleans / Baton Rouge, LA · 8. Oklahoma City, OK · 9. Tulsa, OK · 10. Denver / Colorado Springs, CO (hail)

## Tier 2 — dense independent-agency country (IA market share high)
11. Pittsburgh, PA · 12. Columbus, OH · 13. Cleveland, OH · 14. Cincinnati, OH · 15. Indianapolis, IN · 16. Grand Rapids, MI · 17. Milwaukee, WI · 18. Minneapolis–St. Paul, MN · 19. Kansas City, MO · 20. St. Louis, MO · 21. Buffalo / Rochester, NY (upstate — avoid NYC) · 22. Hartford, CT · 23. Charlotte, NC · 24. Nashville, TN · 25. Birmingham, AL

## Tier 3 — fill if volume short
26. Boise, ID · 27. Salt Lake City, UT · 28. Omaha, NE · 29. Des Moines, IA · 30. Richmond, VA

## Search strings per metro
- "independent insurance agency {metro}"
- "insurance agency {metro}" (filtered post-hoc: exclude captive brand names)

## Notes
- FL/TX heavy in Tier 1 is deliberate: worst rate environment → strongest "your clients are shopping" pitch. (State compliance windows affect client SMS fulfillment, not our B2B email.)
- For the review data piece: pull ALL reviews from discovered agencies, then keyword-filter (renewal, rate increase, premium went up, shopped around, nobody called) — expect 5-15% relevance yield.
