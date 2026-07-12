# Sprint Intake Form — field spec v1
(Build target: Tally.so free tier or Cal.com routing form — decide when client #1 is in sight. This spec is the single source of truth; keep form + this doc in sync.)

**Purpose:** everything needed to run a Renewal Recovery Sprint with zero follow-up questions. One form, ~10 minutes of the client's time.

## Section 1 — Agency basics
| Field | Type | Required |
|---|---|---|
| Agency name | text | ✔ |
| Principal name + email | text | ✔ |
| Best phone (for sprint-blocking issues only) | text | ✔ |
| Agency physical address (goes in email footers — CAN-SPAM) | text | ✔ |
| Website | url | ✔ |
| States you write in | multi-select | ✔ (drives send-window rules: FL/TX/WA/OK/MD/OR strictest) |

## Section 2 — Stack
| Field | Type | Required |
|---|---|---|
| AMS (AMS360 / Epic / HawkSoft / QQCatalyst / EZLynx / other / none) | select | ✔ |
| Marketing/CRM tools in use (Levitate / Fuse / AgencyZoom / Better Agency / InsuredMine / GHL / none) | multi-select | ✔ |
| Can you give us operator access to the marketing tool? | yes/no | ✔ |
| If no tool: OK adding a subdomain of YOUR domain for sending? (their DNS, their brand — never our infra) | yes/no | conditional |

## Section 3 — The book
| Field | Type | Required |
|---|---|---|
| Book export or renewal report (CSV/XLSX) — policies with renewal dates next 60–120 days | file upload | ✔ |
| Lines of business to include (auto/home/commercial/umbrella/other) | multi-select | ✔ |
| Any segments to EXCLUDE (VIPs, in-progress claims, specific carriers) | textarea | – |
| Producer who takes renewal review calls + their calendar link | text | ✔ |

## Section 4 — Voice
| Field | Type | Required |
|---|---|---|
| Two example emails the agency has actually sent to clients (for voice matching) | file/paste | ✔ |
| Tone slider: formal ↔ neighborly | select | ✔ |
| Anything you'd never say to a client | textarea | – |

## Section 5 — Legal gates (blocking — sprint does not start without these)
| Field | Type | Required |
|---|---|---|
| **Consent attestation**: "I confirm the contact information in this book was collected by the agency in the course of its business relationship with these policyholders." | checkbox | ✔ |
| Service agreement + data-handling terms | e-sign | ✔ |
| Payment ($500 Stripe link) or free-case-study agreement | link | ✔ |

## Same-day deliverable back
Kickoff email: scope confirmation + which book segment we're targeting + what happens on each of the 14 days. Template: `templates/kickoff-email.md`.
