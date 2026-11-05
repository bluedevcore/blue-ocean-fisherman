# Round 00 — Success-criteria research & rubric

Date: 2026-11-05

## What was done
- Three researcher subagents ran in parallel:
  - research/round0-a-iot-failures.md: why hardware/IoT startups fail and what survivors share (115 URLs, 63 queries)
  - research/round0-b-buyer-drivers.md: what makes B2B buyers pay (111 URLs, 58 queries)
  - research/round0-c-niche-case-studies.md: niche sensor business case studies (~150 URLs)
- rubric.md written and FROZEN. It has 10 criteria, c1–c10, with 0/5/7/10 anchors, evidence
  requirements, general scoring rules and red flags.

## Key findings that shaped the rubric
- "No market need / unclear ROI" is the top failure cause, so c1 and c10 require sourced
  money figures. Vendor-only figures are capped at 5.
- Survivors sold through parties that already hold the risk or visit the site (insurers,
  service contractors, distributors, suppliers), so c6 rewards an evidenced existing channel.
  Cold direct-to-SME selling scores 0.
- Recurring pain that can be shown inside a 1–3-month pilot beats rare catastrophes (c2).
- Record-keeping duties (HACCP, ACoP L8, vaccine cold chain, Awaab's Law) drive both
  compliance (c4) and durable subscriptions (c9). The subscription benchmark is ≥ ~£100 per
  site per year or ≥ ~£5 per sensor per month.
- Red flags: ATEX/medical/MCERTS certification, 2G/3G or single-network dependence,
  customer-IT dependence, commoditised categories (e.g. oil-tank monitors at £25/yr), and
  dead predecessors.

## ENVIRONMENT ISSUE — page fetching is blocked
All three researchers reported that WebFetch fails on every host ("getaddrinfo ENOTFOUND …
outside the session's allowed network domains"). The orchestrator confirmed this:
WebFetch to www.hse.gov.uk fails, and curl gets a 403 from the egress proxy. WebSearch works.
- Consequence: Round 0 claims come from search-result extracts and are marked
  "(not fetched — blocked)".
- Consequence: the acceptance gate "Critic verified ≥3 URLs by fetching" cannot currently be met.
- Decision (logged; the bar is NOT lowered): critics still attempt fetches and also run
  search-based checks, recorded as `search-confirmed`. These do NOT count as fetch-verification.
  Ideas that meet every other gate are held as PROVISIONAL and re-verified by fetch once the
  network policy allows it. No idea is ACCEPTED without ≥3 fetched-`ok` URLs.
- Fix (user action): broaden the cloud environment's Network access (environment settings →
  Network access → Full, or allow the domains needed). See
  https://code.claude.com/docs/en/cloud-environments#network-access
