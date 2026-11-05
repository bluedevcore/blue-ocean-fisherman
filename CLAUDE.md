To resume: git pull, read state.json and the latest rounds/ file, continue the loop.

(Orchestrator implementation conventions are in the APPENDIX at the bottom of this file —
read them before resuming. The helper script is tools/bof.py.)

You are running a protocol called BLUE OCEAN FISHERMAN.

ENVIRONMENT
You are in a Claude Code cloud session on the GitHub repo
bluedevcore/blue-ocean-fisherman (branch: main). Web search and web fetch work
(verified). GitHub is the permanent record of this run: anything not committed
and pushed can be lost if the session ends. Commit and push often (see RULES).

MISSION
Find real, painful business problems that can be solved with a hardware
sensor/tracker product (sensor + firmware + connectivity + software/alerts).
Generate hundreds of problem ideas, research each against real evidence on the
web, score them strictly, breed the best into new variants, and repeat.
STOP when exactly 10 distinct ideas have been ACCEPTED (definition below).

You are the ORCHESTRATOR. You do not do the bulk research yourself. You
dispatch subagents (via the Agent/Task tool), many in parallel, and you manage
files, scoring flow and the loop. Keep your own context lean: read summaries
and scores, not full evidence files.

──────────────────────────────────────────
STEP 0 — SETUP / RESUME
──────────────────────────────────────────
First, git pull. If state.json exists, this is a RESUMED run: read CLAUDE.md,
state.json and the latest rounds/ file, then continue the loop from where it
stopped. Don't redo completed rounds, and don't regenerate rubric.md.

Otherwise create:
  CLAUDE.md          ← a copy of this whole protocol, so it survives restarts,
                       with this at the top: "To resume: git pull, read
                       state.json and the latest rounds/ file, continue the loop."
  state.json         ← {"round":0,"accepted":[],"total_ideas":0,
                        "last_completed_step":"setup"}
  ideas.jsonl        ← one JSON object per idea:
                       {id, round, title, problem, buyer, industry, sensor_concept,
                        parent_ids, status: new|filtered|researched|scored|accepted|killed,
                        score, criterion_scores, notes}
  sectors.md         ← a list of 40+ diverse industries/settings (agriculture,
                       cold chain, hospitality, property, construction, marine,
                       healthcare facilities, logistics, utilities, education,
                       retail, manufacturing, mining, waste, events, sport,
                       animal care, museums, telecoms, water, aviation ground ops,
                       etc.). Track how often each sector has been fished.
  roles/generator.md, roles/researcher.md, roles/critic.md,
  roles/devils_advocate.md, roles/breeder.md   ← role instructions (below)
  evidence/          ← one markdown file per researched idea
  rounds/            ← round-NN.md summary per round
  shortlist.md       ← final output
Commit and push: "setup".

When dispatching a subagent, tell it: "Read roles/<role>.md and follow it
exactly", then give it its specific inputs and output file path. Subagents
write their output to files. You don't paste their full results into your context.

──────────────────────────────────────────
ROUND 0 — RESEARCH THE SUCCESS CRITERIA (once only)
──────────────────────────────────────────
Dispatch 3 researcher subagents in parallel to investigate, with sources:
  (a) why hardware/IoT startups fail and what the survivors had in common
  (b) what makes B2B buyers pay for monitoring/sensor products
      (ROI, compliance, insurance, labour savings)
  (c) case studies of successful niche sensor businesses (e.g. cold-chain
      logging, leak detection, livestock water, concrete curing, asset tracking)
Save their findings to research/round0-*.md.
Then write rubric.md: exactly 10 criteria, each scored 0–10 (100 total), each
with a clear description of what 0, 5 and 10 look like and what evidence is
required. Start from this draft and refine it with what the research found:
  1. Cost of incident is quantifiable in money (sourced figures)
  2. Frequency: the pain recurs weekly/monthly, not rarely
  3. Existing paid or labour-heavy workaround (paper logs, manual checks, site visits)
  4. Compliance/insurance/audit pressure demands proof
  5. Identifiable buyer with budget (a job title, not "businesses")
  6. Distribution channel that already visits the site
  7. Market proven but underserved (competitors expensive/clunky/enterprise-only,
     or none for this niche)
  8. Buildable: off-the-shelf components, plausible BOM < ~£50, no exotic certification
  9. Recurring revenue potential (data/alerts stay valuable after install)
 10. Public evidence of pain (forum threads, Reddit, trade press, reviews, regulator notices)
Once written, rubric.md is FROZEN. Never relax it later.
Commit and push: "round 0 – rubric".

──────────────────────────────────────────
ACCEPTANCE DEFINITION
──────────────────────────────────────────
An idea is ACCEPTED only if ALL are true:
  - Total score ≥ 90/100 from the Critic
  - No single criterion below 7
  - At least 8 distinct, credible, working source URLs in its evidence file
  - The Critic verified at least 3 of those URLs by fetching them
  - It SURVIVED the Devil's Advocate pass (no fatal flaw backed by evidence)
  - It is materially different from every already-accepted idea (a different
    problem or buyer, not just a different sector wrapper on the same thing)

──────────────────────────────────────────
THE LOOP (round = 1, 2, 3 …)
──────────────────────────────────────────
1. CAST — Dispatch 4 generator subagents in parallel. Each gets ~5 sectors,
   prioritising the least-fished ones in sectors.md. Each returns 40–50 problem
   ideas. From round 2 onwards, also include the Breeder's mutations.
   Append everything to ideas.jsonl with status "new".

2. SORT — Dedupe against ALL previous ideas (similar problem + buyer = duplicate).
   Do a quick plausibility filter yourself (obvious no-hopers, consumer-only,
   needs an impossible sensor). Keep the best ~50. Mark the rest "filtered".

3. HAUL — Dispatch researcher subagents in parallel: up to 10 at once, each
   handling 5 ideas. Each writes evidence/<id>.md using real web search and
   fetching. Every claim must carry a URL. No URL = the claim doesn't count.
   Status → "researched".

4. JUDGE — Dispatch critic subagents in parallel (up to 5 at once, 10 ideas
   each). Critics see ONLY rubric.md and the evidence files, never the
   generator's pitch. They score each criterion, justify each score in one
   line, and fetch at least 3 URLs per idea to check they're real and say what's
   claimed. Fabricated or broken sources → that criterion scores 0.
   Write scores into ideas.jsonl. Status → "scored".

5. KILL PASS — For every idea scoring ≥ 90 with no criterion < 7, dispatch a
   devils_advocate subagent. Its job is to find a fatal flaw: a dominant cheap
   incumbent, buyers who demonstrably won't pay, a regulatory/certification wall,
   physics that won't work, or a market too small. If it finds a fatal flaw
   backed by evidence → status "killed" with the reason. Otherwise → "accepted",
   added to state.json.

6. BREED — Dispatch one breeder subagent with the top 15 non-accepted ideas
   (by score) plus their weakest criteria. It produces ~40 mutations aimed at
   fixing the weak criteria: same problem with a different buyer, a different
   sector, a different channel, a narrower niche, combinations of two ideas,
   or a compliance angle. Each records its parent_ids.

7. LOG — Write rounds/round-NN.md: ideas cast, researched, score distribution,
   newly accepted, killed and why, which sectors and patterns are scoring well.
   Update state.json (round, accepted, total_ideas, last_completed_step) and
   sectors.md. Commit and push: "round NN – X accepted total".

8. CHECK — If accepted count ≥ 10 → go to FINISH. Otherwise next round.
   Use what's working: if certain criteria are consistently weak, tell the
   generators and breeder what kinds of problems score well.

HARD CAP: 25 rounds. If you reach it without 10 accepted, do NOT lower the
bar. Go to FINISH anyway, list the accepted ideas plus the best near-misses,
and state clearly which criteria they fell short on.

──────────────────────────────────────────
ROLE FILES (write these into roles/)
──────────────────────────────────────────
generator.md: Produce specific, concrete problems, not categories. Each idea:
  title, the exact painful moment ("walk-in freezer fails overnight, £3k of
  stock binned"), who suffers, who pays, current workaround, sensor concept.
  Favour boring, unglamorous, regulated, physical industries. Avoid consumer
  gadgets and anything that's purely software. Before generating, read
  ideas.jsonl titles so you don't repeat existing ideas.

researcher.md: For each idea, search hard (at least 6 different queries) for:
  cost figures, frequency, current workarounds, regulations/insurance
  requirements, existing competitors and their prices, real complaints (forums,
  Reddit, trade press, reviews), buyer job titles, channels. Record findings as
  bullet points, each with a URL. Record what you looked for and couldn't find
  too, because absence of evidence matters. Never invent sources or figures.

critic.md: You are strict and sceptical. Score only on the evidence in the file
  against rubric.md. Missing evidence = low score. Fetch and verify at least 3
  URLs per idea. Output per-criterion scores, one-line justifications, the total,
  and the single weakest point.

devils_advocate.md: Try to kill the idea. Search specifically for reasons it
  fails. Report "FATAL: <reason + evidence>" or "SURVIVES: <strongest
  objection and why it isn't fatal>".

breeder.md: Take strong-but-not-accepted ideas and mutate them to fix their
  weakest criteria. Be inventive. Each mutation must be a genuinely new
  idea, not a rewording.

──────────────────────────────────────────
FINISH
──────────────────────────────────────────
Write shortlist.md. For each accepted idea:
  - One-line problem statement
  - Buyer (job title) and how to reach them (channel)
  - Cost of the pain (sourced figure), frequency, current workaround
  - Competitors and the gap
  - Product concept: sensors, connectivity, rough BOM, subscription model
  - Score breakdown and the Devil's Advocate's strongest objection
  - The 8+ evidence links
  - 5 questions to ask real buyers to validate it in interviews
Add a section at the end: patterns across the winners, what kinds of
problem scored well, and what consistently failed.
Commit and push: "FINISH – shortlist". Then stop.

RULES
- Never fabricate data, quotes or URLs. If you can't find it, say so.
- Commit and push to main after setup, after round 0, at the end of every
  round, and at FINISH. If a round is very long, also commit after HAUL and
  JUDGE. Uncommitted work can be lost.
- If a push fails, git pull --rebase and push again. Never force-push.
- Always write to files before moving on, so the run can resume after any
  interruption.
- Maximise parallel subagent use, but stagger batches if you hit rate limits.
  If you hit a usage limit, commit and push what you have before stopping.
- Don't stop to ask me questions. Make reasonable decisions, log them in the
  round file and keep fishing until the stop condition is met.

Begin with STEP 0.

══════════════════════════════════════════
APPENDIX — ORCHESTRATOR IMPLEMENTATION CONVENTIONS (decided at setup)
══════════════════════════════════════════
Branch: the user explicitly instructed "commit and push to main", and the resume
procedure relies on main, so all work is committed to and pushed from `main`.

Helper script: `python3 tools/bof.py <command>` — run with no args for help.
Only the orchestrator (via this script) writes ideas.jsonl and state.json.
Subagents never edit ideas.jsonl/state.json and never run git.

ID scheme: R<NN>-<G>-<KK>, e.g. R03-B-17 (round 3, generator B, idea 17).
  Breeder mutations bred at the end of round N belong to round N+1: R<N+1>-M-<KK>.

Working files (per round NN, zero-padded):
  work/rNN/gen-A.jsonl … gen-D.jsonl  generator outputs (one JSON idea per line)
  work/rNN/mutations.jsonl            breeder output for round NN (bred at end of NN-1)
  work/rNN/sort.md                    orchestrator's SORT decisions (kept ids + reasons)
  work/rNN/haul.json                  researcher batch assignments
  evidence/<id>.md                    researcher output (one per idea)
  critiques/<id>.json                 critic output (one per idea; machine-readable)
  devils/<id>.md                      devil's advocate output; first line
                                       "VERDICT: FATAL — …" or "VERDICT: SURVIVES — …"
  rounds/round-NN.md                  round log
  research/round0-*.md                round-0 success-criteria research

Criterion keys used in JSON: c1..c10 (same order as rubric.md).
Acceptance is computed by `tools/bof.py qualifiers` (score>=90, min>=7,
>=8 distinct URLs in evidence, >=3 critic-verified OK URLs), then the devil's
advocate verdict and an orchestrator distinctness check against accepted ideas.

state.json also carries: "sector_fished" (sector -> times assigned to a generator)
and "notes_for_generators" (what is scoring well / badly, updated each round).

Subagents return only a one-line summary in their final message; all substance
goes into files.

WEB SEARCH BUDGET (learned in Round 1): all subagents share a WebSearch cap of ~200 calls
per orchestrator turn; overlapping waves share it. Run only ONE search-heavy wave at a time
(≤ ~180 planned searches: e.g. 4 researchers × 5 ideas × 8 queries, or critics at ~4
searches per idea), and start the next wave only after the previous one has fully reported.
WebFetch is blocked by the environment network policy (as of 2026-11-05) — see rounds/round-00.md.
