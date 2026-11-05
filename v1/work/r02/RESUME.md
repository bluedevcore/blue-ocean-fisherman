# RESUME POINT — Round 02, mid-HAUL (stopped by user, 2026-11-05: "stop here, im upgrading the system")

State: round 1 complete and logged (rounds/round-01.md). Round 2 CAST and SORT are done: 202 cast, 50 kept
(work/r02/keep.txt, sort.md). In ideas.jsonl all 50 kept ideas still have status "new".

HAUL progress: 33/50 evidence files written (all have a Sources section). The wave-2 researchers were
stopped mid-run, so these files may be slightly incomplete. Spot-check them before judging:
R02-C-23 R02-C-24 R02-D-02 R02-D-12 R02-D-15 R02-D-16 R02-D-27 R02-D-30 R02-D-31 R02-D-32 R02-D-35 R02-D-37 R02-M-01

STILL TO RESEARCH (17):
R02-C-25 R02-C-26 R02-C-34 R02-D-20 R02-D-34 R02-M-03 R02-M-06 R02-M-08
R02-M-10 R02-M-15 R02-M-17 R02-M-19 R02-M-21 R02-M-27 R02-M-29 R02-M-33 R02-M-35

Next steps:
1. Research the missing ideas. Use waves of ≤ 4 researchers × 5 ideas, one wave at a time,
   because of the ~200 searches/turn budget (see CLAUDE.md appendix).
2. `python3 tools/bof.py researched 2`
3. JUDGE in critic batches of 10, at most ~4 concurrent searches budget-wise.
4. Run `tools/bof.py scored 2`.
5. KILL PASS, then BREED (→ work/r03/mutations.jsonl), then LOG rounds/round-02.md.

Environment: if the network policy now allows WebFetch, critics should fetch-verify. Any
PROVISIONAL ideas from earlier rounds would then need fetch re-verification (none so far: round-1 max was 74).
