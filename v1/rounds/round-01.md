# Round 01

Date: 2026-11-05 · Accepted this round: **0** · Accepted total: **0**

## Pipeline
| Step | Result |
|---|---|
| CAST | 4 generators produced 181 ideas (A 46, B 44, C 45, D 46). No breeder mutations in round 1. |
| SORT | 50 kept, 131 filtered. Decisions are in work/r01/sort.md and work/r01/reasons.tsv; 21 filtered ideas have explicit duplicate or no-hoper reasons. |
| HAUL | 50 evidence files written, with 29–54 distinct URLs each (median 44). Every claim is a "(search extract)" because WebFetch is blocked. |
| JUDGE | 5 critic batches scored all 50: 0 URLs fetch-verified (blocked), 134 URLs `search-confirmed`, 2 `mismatch`. |
| KILL PASS | Nothing qualified (score ≥ 90 with no criterion < 7), so no devil's advocates were dispatched. |
| BREED | Breeder dispatched on the top 15, writing to work/r02/mutations.jsonl for round 2. |

## Score distribution (50 scored)
40–49: 5 · 50–59: 16 · 60–69: 23 · 70–79: 6 · ≥80: 0. Mean 60.1, max 74.

Criterion averages: c1 Cost 5.2 · c2 Frequency 6.5 · c3 Workaround 6.4 · c4 Compliance 7.2 ·
c5 Buyer 5.3 · c6 Channel 6.8 · **c7 Market gap 4.5** · c8 Buildable 5.3 · c9 Recurring 5.7 ·
c10 Public pain 7.3.
Ideas scoring ≥ 7 on each criterion: c1 13, c2 28, c3 25, c4 34, **c5 5**, c6 30, **c7 3**, **c8 3**, c9 12, c10 38.

## Top 10
| id | score | idea | weakest |
|---|---|---|---|
| R01-D-10 | 74 | Holiday-park lodge hot tubs: HSG282 changeover tests done by hand | c8 5, c5 6, c7 6 |
| R01-C-12 | 72 | Type 3 TMVs serviced on fixed cycles | c7 5, c6 6, c8 6 |
| R01-D-02 | 71 | LN2 dewars boil down between weekly top-ups | c7 5, c4 6, c8 6 |
| R01-D-21 | 71 | Hired breakers/grinders: no real HAV trigger-time records | c7 4, c9 5, c2 6 |
| R01-B-30 | 70 | Empty probate homes: insurer inspection/drain-down proof | c5 4, c1 6, c8 6 |
| R01-C-03 | 70 | Culvert trash screens block; councils drive round to look | c8 5, c4 6, c5 6 |
| R01-A-27 | 69 | Church roof alarms on PSTN diallers (lead theft) | c2 3, c7 5, c8 5 |
| R01-B-11 | 69 | Sprinkler pump-house weekly test logs faked/skipped | c8 4, c7 5, c5 6 |
| R01-C-27 | 69 | HMO weekly fire alarm tests unrecorded | c5 5, c7 5, c8 5 |
| R01-D-18 | 69 | Little-used leisure showers: Legionella flushing by hand | c7 4, c1 6, c5 6 |

Bottom examples, with the critic's reason:
- **R01-D-29 glue boards (42):** only ~22 licences were granted in England in 2025.
- **R01-C-33 package treatment plants (43):** English operators have needed no maintenance records since 2014.
- **R01-A-19 LPG cages (41):** per-site losses are a few hundred pounds.
- **R01-A-23 pellet stores (41):** no sourced run-out cost.

## Killed
None (no qualifiers).

## Patterns
- **Scored well:** a statutory or insurer *check duty performed manually at a fixed frequency*
  that a sensor could evidence: HSG282 hot tubs, TMV servicing, HAV records, sprinkler pump
  tests, HMO alarm tests, unoccupancy inspections. These score well on c2/c3/c4/c10.
- **Consistently weak:**
  - **c7 market gap:** most compliance-monitoring categories already have incumbents —
    Legionella sentinel monitoring, Reactec HAV tags, LN2 monitors, drying monitors, digital
    rodent monitoring (Syngenta, Pelsis, Rentokil), transport temperature recorders.
  - **c8 buildable:** evidence files lacked priced components.
  - **c5 buyer:** volunteers, executors, councils and the NHS rarely own both the loss and a budget.
- Sectors performing best: swimming pools & spas (max 74), healthcare facilities (72),
  laboratories (71), plant hire (71). Weakest: heating oil/LPG (mean 47), data centres (46),
  pest control (mean 56).

## Decisions logged this round
1. **WebFetch is blocked** by the environment's network policy (see rounds/round-00.md).
   - Researchers cite search-result extracts.
   - Critics record `blocked` and then do `search-confirmed` checks.
   - The acceptance gate (≥ 3 fetched-OK URLs) is unchanged, so no idea can be accepted until
     fetching works. Ideas meeting every other gate would be held as PROVISIONAL.
2. **Shared WebSearch budget:** all agents share ~200 searches per orchestrator turn.
   - The first HAUL dispatched 10 researchers at once; they exhausted the budget after about
     1 idea each.
   - The remaining 40 ideas were re-researched in three waves, each capped at 8 queries per idea.
   - The pacing rule is recorded in CLAUDE.md: one search-heavy wave at a time, ≤ ~180 searches.
3. **roles/researcher.md tightened (not the rubric):**
   - section 8 must cite ≥ 2 priced components or comparable devices;
   - section 7 must state explicitly whether a cheap incumbent already serves the buyer.
4. **The loop continues to Round 2 despite the fetch block.** No idea is near 90 yet, and
   generating, researching, scoring and breeding don't depend on fetching. Only final
   acceptance does, and that can be done by re-verifying provisional qualifiers once network
   access is opened. The bar is not lowered.
5. **Round 2 generators were dispatched in parallel with the Round 1 breeder** to save time.
   Their files don't overlap; mutations and generator ideas are deduped together at Round 2 SORT.
6. **Round 2 guidance for generators and breeder** is in work/r02/guidance.md and
   state.notes_for_generators.
