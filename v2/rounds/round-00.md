# v2 Round 00 — Rubric

Date: 2026-11-05

- **v1 inputs:** v1's rubric and its three round-0 research files were read, not redone.
- **New research:** two researchers covered the gaps v1 didn't. Both used search extracts only,
  because WebFetch is blocked:
  - `v2/research/round0-a-defensibility.md` — 90 sources;
  - `v2/research/round0-b-ai-services-and-signals.md` — 87 sources.
- **Rubric:** `v2/rubric.md` is written and FROZEN. It has knockouts K1–K5, the weighted
  criteria W1–W9 scored 0–10 with 0/5/10 anchors, v1's general evidence rules, and red flags.

## Key decisions
- **Scoring:** critics score quality 0–10 per criterion. bof.py computes the weighted total
  (max 100).
- **K2 widened:** it now also covers a tool the buyer already pays for (or their bank, insurer
  or regulator) providing the feature free. This comes from the defensibility research.
- **Single-model wrapper:** treated under W7 = 0 and W9 = 0 rather than as a new knockout. The
  protocol fixes K1–K5.
- **"Revealed behaviour beats stated intent":** added as general rule 7, from the
  willingness-to-pay research (stated WTP overstates payment ~1.35–3×).

## Environment (carried from v1)
- **WebFetch is still blocked by this session's network policy.** Two hosts tested after the
  "upgrade", www.hse.gov.uk and www.gov.uk, both returned ENOTFOUND. The fetch-verification
  acceptance gate therefore cannot be met yet. Critics record `blocked` plus
  `search-confirmed`; ideas meeting every other gate are held PROVISIONAL. The bar is not
  lowered.
- **WebSearch budget:** ~200 searches per orchestrator turn, shared by all agents. Agents are
  dispatched in waves with explicit per-agent caps.
