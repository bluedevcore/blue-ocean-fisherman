Active run: v2. All run files are under v2/. v1/ is an archived earlier run: read-only reference, never resume it.

To resume: git pull, read v2/state.json and the latest v2/rounds/ file, continue from last_completed_step.
(Orchestrator implementation conventions are in the APPENDIX at the bottom of this file.
Helper script: python3 v2/tools/bof.py — run with no args for help.)

You are running BLUE OCEAN FISHERMAN v2.

ENVIRONMENT
You are in a Claude Code cloud session on the GitHub repo
bluedevcore/blue-ocean-fisherman (branch: main). Web search and web fetch work.
GitHub is the permanent record of this run: anything not committed and pushed can
be lost. Commit and push often (see RULES).

This repo contains a previous run (v1) at the top level. Before anything else:
  1. git pull.
  2. If v1/ does not exist yet: git mv every existing v1 file and folder
     (CLAUDE.md, state.json, ideas.jsonl, sectors.md, shortlist.md, rubric.md,
     roles/, evidence/, critiques/, devils/, research/, rounds/, tools/, work/,
     and anything else from v1, but NOT README.md or .git) into v1/.
     Commit and push: "archive v1 into v1/".
  3. ALL v2 files live under v2/. Every file path in this protocol is relative
     to v2/ (e.g. "state.json" means v2/state.json), EXCEPT CLAUDE.md: write the
     v2 protocol to the repo root as CLAUDE.md so it loads automatically, with
     this at the top: "Active run: v2. All run files are under v2/. v1/ is an
     archived earlier run: read-only reference, never resume it."
  4. v1/ is read-only reference material. Never modify it.

MISSION
Find real, painful, UNDERSERVED business problems worth building a business on.
The solution can be any form: software, an AI-run done-for-you service, a
sensor/hardware product, or a hybrid. The solution form is an OUTPUT of this
protocol, not an input.

WHY v2 IS DIFFERENT (lessons from v1)
- v1 brainstormed ideas and then researched them. That mostly found pains that
  are already well served, because well-documented pain attracts vendors.
  Brainstormed ideas are also the ideas everyone else using AI gets.
- v2 MINES raw real-world signals first (job ads, bad reviews of incumbents,
  new regulations, public tenders, freelance gigs, forums), then clusters
  them into problems. Ideas must be grounded in signals, not imagination.
- Software is cheap to build now, so the moat is elsewhere: distribution,
  trust, proprietary data, regulation know-how, hardware, or timing.
  Score for that.
- v1 required all 10 criteria ≥ 7, which rejected nearly everything. v2 uses
  KNOCKOUTS plus a WEIGHTED score.

You are the ORCHESTRATOR. You do not do the bulk mining or research yourself. You
dispatch subagents (Agent/Task tool), many in parallel, and you manage files, the
flow and the loop. Keep your context lean: read summaries and scores, not full
evidence files. When dispatching, tell each subagent: "Read v2/roles/<role>.md and
follow it exactly", then give it its inputs and output file path (under v2/).
Subagents write their results to files.

STOP CONDITION: stop when 10 problems are ACCEPTED, or when round 8 is complete,
whichever comes first. Then go to FINISH.

──────────────────────────────────────────
STEP 0 — SETUP / RESUME
──────────────────────────────────────────
After the ENVIRONMENT steps: if v2/state.json exists, this is a RESUMED run:
read CLAUDE.md, v2/state.json and the latest v2/rounds/ file and continue from
last_completed_step. Never redo completed steps or regenerate rubric.md.

Otherwise create (all under v2/, except CLAUDE.md at the repo root):
  CLAUDE.md        ← this whole protocol, with the "Active run: v2" header
                     above, plus: "To resume: git pull, read v2/state.json and
                     the latest v2/rounds/ file, continue from last_completed_step."
  state.json       ← {"round":0,"accepted":[],"last_completed_step":"setup",
                      "source_type_yield":{}, "notes_for_miners":""}
  signals.jsonl    ← one raw pain signal per line:
                     {id, round, source_type, url, date_found, sector,
                      quote_or_datapoint (≤ 40 words, paraphrase if longer),
                      who_suffers, implied_payer, pain_summary}
  problems.jsonl   ← one problem per line:
                     {id, round, statement, buyer_job_title, sector, signal_ids,
                      source_types (distinct), trigger, solution_form, wedge,
                      status: candidate|researched|scored|accepted|killed|parked,
                      score, criterion_scores, knockouts, notes}
  sectors.md       ← 60+ diverse sectors across physical AND office/knowledge work
                     (trades, property, care, healthcare admin, legal admin,
                     accounting/bookkeeping, logistics, agriculture, hospitality,
                     education, local government, charities, manufacturing,
                     construction, compliance/HSE, recruitment, insurance
                     brokers, funeral services, vets, dental, events, marine,
                     energy, waste, etc.). Track how many times each has been mined.
  sources.md       ← the signal source types (below), with how many signals and
                     how many high-scoring problems each has produced
  roles/miner.md, roles/trigger_scout.md, roles/clusterer.md,
  roles/researcher.md, roles/critic.md, roles/devils_advocate.md,
  roles/validator.md, roles/targeted_miner.md  ← role instructions (below)
  evidence/        ← one markdown file per researched problem
  validation/      ← one validation pack per accepted problem
  rounds/          ← round-NN.md per round
  shortlist.md     ← final output
You may write a helper script (e.g. v2/tools/bof.py) to manage the JSONL files,
dedupe, batching and stats. Commit and push: "v2 setup".

SIGNAL SOURCE TYPES (one miner per type each round)
  S1 JOB ADS — roles hired to do repetitive manual work, chasing, logging,
     reconciling, checking or compliance admin. (Shows budget plus pain.)
  S2 BAD REVIEWS — 1–3 star reviews of leading vendors in a niche (G2, Capterra,
     Trustpilot, app stores, Google reviews). (Shows an incumbent exists, but
     there's a gap.)
  S3 TRIGGERS — new or upcoming regulations, deadlines, switch-offs, standards,
     insurer rule changes, price shocks or tech shifts from 2025–2028 in the UK, US,
     AU, EU, NZ or CA. (Shows "why now".) Handled by trigger_scout.
  S4 PUBLIC TENDERS & GRANTS — Contracts Finder, Find a Tender, SAM.gov,
     AusTender, council procurement. (Shows disclosed budget and buyer.)
  S5 FREELANCE GIGS — recurring Upwork, Fiverr or PeoplePerHour jobs where
     businesses pay people for the same workaround. (Shows paid workaround,
     ripe for automation.)
  S6 FORUMS & COMMUNITIES — trade forums, subreddits, Facebook-group posts quoted
     in articles, industry Q&A. (Shows first-hand pain.)
  S7 ENFORCEMENT & LOSSES — regulator fines, prosecutions, ombudsman cases,
     insurer loss data, failed audits. (Shows cost of the pain.)

──────────────────────────────────────────
ROUND 0 — RUBRIC (once only)
──────────────────────────────────────────
Read v1/rubric.md and the three v1/research/round0-*.md files (don't redo that
research). Dispatch 2 researcher subagents in parallel for the gaps v1 didn't
cover:
  (a) what makes a business defensible when software is cheap to build
      (distribution, data, trust, regulation, hardware, services)
  (b) evidence on AI-enabled services ("service-as-software", done-for-you
      businesses), plus which signal types best predict real willingness to pay
      (job ads, tenders, freelance spend, reviews)
Save to v2/research/round0-*.md. Then write v2/rubric.md using the structure
below, adding 0/5/10 anchors and evidence requirements for each criterion, and
carrying over v1's general evidence rules (only sourced claims count;
vendor-only claims are capped; fabricated or broken sources score 0; 9–10 needs
at least two independent sources; absence of evidence counts against the idea).

KNOCKOUTS (any one kills the problem):
  K1 No identifiable payer with budget (consumers or hobbyists only).
  K2 A dominant, cheap, well-reviewed incumbent already solves it for this
     exact buyer.
  K3 Needs a licence or certification a solo founder can't realistically get
     (medical device, ATEX, FCA authorisation, legal practice, etc.).
  K4 Pain evidenced only by vendor marketing.
  K5 First 10 customers impossible without a 6+ month enterprise sales cycle
     or customer IT integration.

WEIGHTED CRITERIA (100 total):
  W1 Cost of pain in money, sourced ............................ 15
  W2 Budget proof: they already pay (salary, freelancer,
     service, tender, workaround cost) ........................ 15
  W3 Gap evidence: incumbent complaints, or no solution for
     this niche .............................................. 15
  W4 Why now: a trigger in 2025–2028 ............................ 10
  W5 Frequency: weekly or monthly pain ........................... 10
  W6 Reachability: a named channel or community where a solo
     founder can reach buyers within 30 days ................... 10
  W7 Buildable/deliverable by a solo founder with AI tools in
     ≤ 90 days ............................................... 10
  W8 Recurring revenue ........................................... 10
  W9 Defensibility beyond code (data, distribution, trust,
     hardware, regulatory know-how) ............................ 5

ACCEPTANCE: no knockouts, total ≥ 80, at least 8 distinct working source URLs
from at least 3 different signal source types, at least 3 URLs verified by the
critic by fetching, survived the Devil's Advocate, and materially different from
every other accepted problem.
Freeze v2/rubric.md. Commit and push: "v2 round 0 – rubric".

──────────────────────────────────────────
THE LOOP (round = 1 … 8)
──────────────────────────────────────────
1. MINE — Dispatch 7 subagents in parallel: one miner per source type S1, S2,
   S4, S5, S6, S7, plus one trigger_scout for S3. Give each 4–6 sectors,
   favouring the least-mined in sectors.md, and from round 2 also the source
   types with the best yield in sources.md. Each returns 40–60 signals, each
   with a URL. Append to signals.jsonl (dedupe by URL and by near-identical
   pain).
   ROUND 1 ONLY: also import the top 15 scored ideas from v1/ideas.jsonl as
   candidate problems (tagged "from_v1"), so v2's researchers re-research them
   under the new rubric.

2. CLUSTER — Dispatch 2 clusterer subagents (split by sector) to group ALL
   signals so far (old and new) into problems. A problem is one specific pain
   for one specific buyer. Rank them by the number of distinct source types
   pointing at them, then by signal count. Problems backed by 3+ source types
   are gold. Select up to 40 problems with ≥ 2 source types that haven't been
   researched yet. Status → "candidate".

3. RESEARCH & SHAPE — Dispatch researcher subagents in parallel (up to 8 at
   once, 5 problems each). Each deepens the evidence (cost, who already pays and
   how much, incumbents with prices plus their bad reviews, trigger, channel,
   frequency), then proposes the best SOLUTION FORM (software / AI-run service /
   sensor-hardware / hybrid), the wedge (smallest first product a buyer would pay
   for), and the price. Each writes evidence/<id>.md. Every claim carries a URL.
   Status → "researched".

4. JUDGE — Dispatch critic subagents in parallel (up to 5 at once, 8 problems
   each). Critics see ONLY rubric.md and the evidence files. They check the
   knockouts first, then score W1–W9 with one-line justifications, and fetch at
   least 3 URLs per problem to verify them. Status → "scored", or "killed" with
   the knockout named.

5. KILL PASS — For each problem with total ≥ 80 and no knockouts, dispatch a
   devils_advocate subagent. Its focus is "who already does this, and why won't
   buyers switch?", plus any fatal flaw. FATAL with evidence → "killed".
   SURVIVES → "accepted", added to state.json.

6. VALIDATION PACK — For each newly accepted problem, dispatch a validator
   subagent to write validation/<id>.md (see role).

7. TARGETED MINING — For the top 10 non-accepted problems scoring 65–79,
   dispatch targeted_miner subagents. Each mines new signals aimed ONLY at that
   problem's weakest criterion (e.g. weak gap → hunt incumbent reviews; weak
   budget → hunt job ads and tenders), or finds a narrower buyer or niche where
   the problem is stronger. Their findings go into signals.jsonl. These problems
   are re-researched and re-judged next round (max 2 re-tries each, then "parked").

8. LOG — Write rounds/round-NN.md: signals mined per source type, problems formed,
   score distribution, criterion averages, accepted, killed (and why), and which
   source types and sectors produce the best problems. Update state.json
   (source_type_yield, notes_for_miners), sectors.md and sources.md.
   Commit and push: "v2 round NN – X accepted total".

9. CHECK — If accepted ≥ 10 or round 8 is complete → FINISH. Otherwise next round.

──────────────────────────────────────────
ROLE FILES (write these into v2/roles/)
──────────────────────────────────────────
miner.md: You mine ONE source type in the sectors you're given. Find real,
  specific signals of pain or paid workaround. For each: URL, a short quote or
  datapoint (≤ 40 words; paraphrase anything longer), who suffers, who pays, and
  the pain in one line. Prefer recent sources (2024 onwards). No invented
  signals. Don't record names or personal details of private individuals: refer to
  posters as "a UK letting agent on <forum>". 40–60 signals per run, varied.

trigger_scout.md: Find regulations, deadlines, switch-offs, standards, insurer
  rule changes, price shocks and technology shifts from 2025–2028 that create
  new obligations or new pain for a specific buyer. For each: what changes, when,
  who is affected, what they now must do or prove, and URLs (prefer primary
  sources such as legislation, regulators and official guidance).

clusterer.md: Group signals into specific problems (one pain + one buyer).
  Merge near-duplicates. Record each problem's signal_ids and its DISTINCT
  source types. Don't invent problems with no signals. Flag clusters backed by
  3+ source types.

researcher.md: For each problem, run at least 8 varied searches. Establish the
  cost of the pain, who already pays and how much, incumbents with prices AND
  their complaints, any trigger, frequency, the channel or community where
  buyers gather, and the buyer's job title. Then propose the solution form
  (software / AI-run service / sensor-hardware / hybrid), the wedge and the
  price, and say why that form beats the others. Record what you searched for
  and DIDN'T find. Every claim needs a URL. Never invent sources or figures.

critic.md: Strict and sceptical. Check the knockouts first. Score only on the
  evidence file against rubric.md. Fetch and verify at least 3 URLs per
  problem. Output: knockouts (with reasons), W1–W9 scores with one-line
  justifications, the total, and the single weakest point.

devils_advocate.md: Try to kill it. Search specifically for existing
  solutions (including tiny ones, spreadsheets, templates, agencies and
  features inside bigger products), reasons buyers won't switch, and fatal
  flaws. Report "FATAL: <reason + evidence>" or "SURVIVES: <strongest objection
  and why it isn't fatal>".

validator.md: Write a validation pack for an accepted problem:
  - one-paragraph problem and offer
  - the buyer: job title, typical organisation types, and 15–20 example
    ORGANISATIONS (businesses or public bodies, from public sources, never
    private individuals' contact details), plus where these buyers gather
    (associations, forums, events, directories)
  - a short cold outreach message, and a LinkedIn/forum post version
  - 5 interview questions focused on past behaviour and spending, not opinions
  - a smoke test: landing page headline, subheadline, offer and price
  - the 30-day plan to get 10 conversations and the first paying customer
  - the riskiest assumption and how to test it first

targeted_miner.md: You get ONE problem and its weakest criterion. Hunt only
  for signals that would raise or settle that criterion, or for a narrower
  buyer or niche where the problem is stronger. Report honestly if the
  evidence doesn't exist.

──────────────────────────────────────────
FINISH
──────────────────────────────────────────
Write v2/shortlist.md: the TOP 10 problems ranked by score (accepted ones
first, then the best near-misses, each clearly labelled ACCEPTED or NEAR-MISS).
For each:
  - a one-line problem statement and the buyer (job title)
  - the solution form, wedge and price, and why that form
  - cost of the pain, budget proof, gap evidence, trigger
  - knockout check, score breakdown and the Devil's Advocate's strongest objection
  - 8+ evidence links grouped by source type
  - a link to its validation pack (write packs for near-misses too at FINISH)
End with: which signal source types produced the winners, patterns across
winners, and what consistently failed.
Commit and push: "v2 FINISH – shortlist". Then stop.

RULES
- Never fabricate data, quotes or URLs. If you can't find it, say so.
- Don't reproduce long passages from sources: quotes ≤ 40 words, otherwise
  paraphrase.
- Never modify anything in v1/.
- Commit and push after setup, after round 0, after each loop step that
  produces files, and at FINISH. If a push fails, git pull --rebase and push
  again. Never force-push.
- Web search is rate-limited: pace searches, stagger subagent batches and
  re-dispatch any batch that comes back partial. If you hit a usage limit,
  commit and push before stopping.
- Don't ask me questions. Make reasonable decisions, log them in the round file
  and keep going until the stop condition is met.

Begin with the ENVIRONMENT steps, then STEP 0.

══════════════════════════════════════════
APPENDIX — ORCHESTRATOR IMPLEMENTATION CONVENTIONS (v2, decided at setup)
══════════════════════════════════════════
Helper: `python3 v2/tools/bof.py <command>` (no args = help). Only the orchestrator (via
this script) writes v2/signals.jsonl, v2/problems.jsonl, v2/state.json, v2/sectors.md,
v2/sources.md. Subagents write only their own output files and never run git.

IDs
  signals:  R<NN>-S<k>-<NNN>   e.g. R01-S6-014   (targeted mining: R<NN>-T<k>-<NNN>)
  problems: R<NN>-P-<NNN>       e.g. R02-P-007    (v1 imports: R01-V-<NN>)
Problem status: pool (formed by a clusterer but not selected) → candidate → researched →
  scored | killed (knockout or devil's advocate) → accepted | parked.
  "pool" is an orchestrator extension to the protocol's status list.

Working files per round NN (zero-padded) under v2/work/rNN/:
  sectors.json                      sector groups given to each miner
  signals-S1.jsonl … signals-S7.jsonl   miner / trigger-scout output
  targeted-<problem_id>.jsonl (+ .md)   targeted-miner output (merged next round)
  clusters-1.jsonl, clusters-2.jsonl    clusterer output
  research.json, judge.json             batch assignments
Per problem: v2/evidence/<id>.md (researcher), v2/critiques/<id>.json (critic),
  v2/devils/<id>.md (devil's advocate; first line "VERDICT: FATAL — …" or
  "VERDICT: SURVIVES — …"), v2/validation/<id>.md (validator).

Scoring: critics score each criterion W1–W9 on a 0–10 QUALITY scale using the rubric's
0/5/10 anchors; the weighted total = Σ quality × weight / 10 (max 100), computed by bof.py.
Evidence-file Sources lines are tagged with a signal source type: [S1]…[S7] or [OTHER];
bof.py counts distinct working URLs and distinct S-types for the acceptance gate.

ENVIRONMENT LESSONS (carried from v1, 2026-11-05)
- WebFetch has been blocked by the session's network policy (ENOTFOUND for external hosts),
  even though the brief says it works. Critics attempt fetches, then do search-based checks
  recorded as `search-confirmed`. Those do NOT count as fetch-verification. Acceptance needs
  ≥ 3 fetched-OK URLs, so ideas meeting every other gate are held PROVISIONAL until
  fetching works. The bar is never lowered.
- All subagents share a WebSearch budget of ~200 calls per orchestrator turn, and
  overlapping waves share it. Run one search-heavy wave at a time, ≤ ~180 planned searches
  in total, with an explicit per-agent search cap in every dispatch. Re-dispatch partial
  batches.
- reddit.com is rejected by the WebSearch tool in this environment (round 1, S6 miner). S6 miners should use
  trade forums, Q&A sites, trade-body boards and articles quoting community posts instead.
