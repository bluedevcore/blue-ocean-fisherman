# BLUE OCEAN FISHERMAN v2 — Rubric (FROZEN)

**Status: FROZEN at v2 Round 0 (2026-11-05). Never relax or rewrite this file.**

## Sources
Built from the v2 protocol's structure, with input from these research files:
- v1 research: `v1/rubric.md`, `v1/research/round0-a-iot-failures.md`,
  `v1/research/round0-b-buyer-drivers.md`, `v1/research/round0-c-niche-case-studies.md`
- v2 research: `v2/research/round0-a-defensibility.md`,
  `v2/research/round0-b-ai-services-and-signals.md`

## Key lessons from that research
1. **Score revealed spending, not stated interest.** Stated willingness to pay overstates real
   payment about 1.35–3×. Compliments, waitlists and letters of intent are worth nothing.
   Salaries, incumbent prices and contract awards are the strongest proof.
2. **Code is no longer a moat.** What holds:
   - distribution through someone who already serves the buyer;
   - owning money flows or legally required records;
   - mission-critical jobs;
   - installed hardware or service;
   - accumulating outcome data.
3. **Pain that recurs and is bought as a retainer or per unit beats one-off jobs.**
4. **A dated mandatory deadline with publicised enforcement is the strongest "why now".**
   "AI makes it possible" is supply-side, not a buyer trigger.

## Scoring mechanics
- **Knockouts first.** If any of K1–K5 is hit, the problem is killed whatever its score.
- **Quality scores.** Each criterion W1–W9 is scored as an integer from 0 to 10 using the
  anchors below; 7 and 9 sit between anchors.
- **Weighted total** = Σ quality × weight / 10, maximum 100. The weights are:

  | Criterion | Weight |
  |---|---|
  | W1 Cost | 15 |
  | W2 Budget proof | 15 |
  | W3 Gap | 15 |
  | W4 Why now | 10 |
  | W5 Frequency | 10 |
  | W6 Reachability | 10 |
  | W7 Buildable | 10 |
  | W8 Recurring | 10 |
  | W9 Defensibility | 5 |

- **Acceptance**, from CLAUDE.md, repeated here and not changed:
  - no knockouts;
  - total ≥ 80;
  - ≥ 8 distinct working source URLs from ≥ 3 different signal source types (S1–S7);
  - ≥ 3 URLs verified by the critic by fetching;
  - survived the Devil's Advocate;
  - materially different from every other accepted problem.

## General evidence rules (carried over from v1; apply everywhere)
1. **Only sourced claims count.** A claim without a URL is ignored.
2. **Vendor-only claims are capped.** Figures that come only from a vendor selling a related
   product can support at most **5/10** on any criterion unless independently corroborated.
   Investor theses and TAM estimates count as vendor-type claims.
3. **Fabricated, broken or mismatched sources score 0** for the criterion that relies on them,
   unless independent verified evidence supports that criterion.
4. **9–10 needs breadth.** A 9 or 10 needs at least two independent sources, or one primary
   authoritative source (statute, regulator, official tender record, insurer wording) plus one
   corroborating source.
5. **Absence of evidence counts against the idea.** If the researcher searched and recorded
   "not found", score accordingly. Don't fill gaps with plausibility.
6. **Geography.** UK/US/AU/EU/NZ/CA evidence is acceptable. Note mismatches, such as a US rule
   used to claim UK pressure.
7. **Revealed behaviour beats stated intent.** Surveys, "would pay" statements, waitlists and
   LOIs carry no weight on W2 or W3.

---

## KNOCKOUTS (any one kills the problem)

**K1 — No identifiable payer with budget.**
- *Hit if:*
  - the only payers are consumers or hobbyists; or
  - there is no evidence of £/$ spend on this pain beyond forum posts or one-off micro-gigs.
- *Not hit if:* a business or public-body buyer is evidenced with spend (salary, service,
  software, tender, fines paid).

**K2 — A dominant, cheap, well-reviewed incumbent already solves it for this exact buyer.**
- *Hit if:* there is evidence that a product is BOTH cheap relative to the pain AND well
  reviewed by THIS buyer type, and is widely used by them. Also hit if a tool the buyer already
  pays for (their practice-management system, accounting package, bank, insurer or regulator)
  provides it free or bundled.
- *Not hit if:*
  - the incumbent is expensive, enterprise-only, badly reviewed, or aimed at a different
    buyer. Those facts feed W3 instead;
  - competitors merely exist.

**K3 — Needs a licence or certification a solo founder can't realistically get.**
- *Hit if:* delivering the wedge requires, for example:
  - FCA authorisation;
  - legal-practice or reserved legal activities;
  - medical-device approval;
  - ATEX/IECEx;
  - MCERTS or metrology type approval;
  - regulated professional sign-off with no realistic partner route;
  - a security-industry licence the founder can't obtain.
- *Not hit if:* the work can be delivered under an existing professional's supervision through a
  realistic partnership, and the evidence shows that route.

**K4 — Pain evidenced only by vendor marketing.**
- *Hit if:* every pain source is a vendor, an idea-validation tool, an investor thesis or a TAM
  report.
- *Not hit if:* there is at least one independent signal: a job ad, tender, regulator or
  enforcement record, ombudsman case, buyer forum post, or incumbent review.

**K5 — First 10 customers impossible without a 6+ month enterprise sales cycle or customer IT integration.**
- *Hit if:*
  - the only buyers are large enterprises or public bodies buying via formal procurement; or
  - the wedge cannot work without integration into the customer's IT systems or IT/security
    approval.
- *Not hit if:* small or mid-sized buyers can say yes within weeks.
- Note: tenders prove budget but imply procurement. Hit K5 if a tender is the ONLY route to buyers.

---

## WEIGHTED CRITERIA (quality 0–10; weight in brackets)

### W1 Cost of pain in money, sourced (15)
- **0**: no money figure, or the pain is inconvenience only.
- **5**: sourced money figures exist, but they are aggregates, vendor-only, or small (under
  ~£2k a year per buyer, or under ~3× the plausible price of the solution).
- **10**: ≥ 2 independent sourced figures for THIS buyer: fines, prosecutions, losses, claims,
  staff hours × wage, lost revenue. Together they show the pain costs ≥ ~5× the proposed annual
  price, implying payback within a year.
- *Evidence:* URLs with explicit £/$/€ amounts tied to this problem.

### W2 Budget proof: they already pay (15)
- **0**: no evidence of existing spend; only complaints, surveys or micro-gigs.
- **5**: one spend type for this task (a job ad naming the task with a salary, OR an incumbent
  or outsourcer price, OR a tender), or spend evidenced only on a broader role.
- **10**: ≥ 2 independent spend types for THIS task and buyer, with £ figures. Examples:
  - a salaried job ad naming the task plus an outsourced-service price;
  - a contract award plus recurring freelance spend.
- *Evidence:* job-ad, pricing-page, tender or contract-award, or gig URLs with amounts.

### W3 Gap evidence (15)
- **0**: a cheap, well-reviewed incumbent serves this buyer. That is also K2.
- **5**: incumbents exist and there are some bad reviews or complaints, but the buyer could
  plausibly be served by what exists. Or "no solution found" without evidence the researcher
  looked properly.
- **10**: paid incumbents prove demand but are priced or packaged out of THIS buyer's reach,
  or fail them, with sourced complaints about price, fit or service (S2/S6). Or there is a
  documented search showing no product serves this niche, while adjacent niches pay for one.
  Inertia is real: about 92–93% of buyers renew and many find paper "good enough". A 10 needs
  evidence that buyers are actively looking or switching.
- *Evidence:* incumbent URLs with prices; review or forum URLs with complaints.

### W4 Why now: a trigger in 2025–2028 (10)
- **0**: no trigger, or only "AI now makes it possible".
- **5**: a relevant change exists but is guidance only, delayed, voluntary, or has a known slow
  uptake with no enforcement.
- **10**: a dated, mandatory 2025–2028 deadline or change (regulation, switch-off, insurer
  rule, standard, price shock) that hits THIS buyer, with a primary source. Plus evidence of
  enforcement or consequences in the buyer's sector.
- *Evidence:* a primary-source URL (legislation, regulator, official guidance), plus an
  enforcement or news URL.

### W5 Frequency (10)
- **0**: one-off, or rarer than yearly per buyer.
- **5**: roughly quarterly or yearly per buyer, or frequent only in aggregate.
- **10**: the pain or the required task recurs weekly or monthly per buyer (sourced: schedules,
  mandated check intervals, job-ad duties, first-hand accounts). Value is provable within a
  month.

### W6 Reachability (10)
- **0**: no named channel; would need cold outreach to anonymous, fragmented buyers, or search
  or content only.
- **5**: named communities exist (association, subreddit, Facebook group, directory), but with
  no evidence of size or access, or the founder would need paid ads.
- **10**: ≥ 2 named channels with evidence of size or activity, where a solo founder can reach
  buyers within 30 days. Examples:
  - an association with a member directory;
  - an active forum or group;
  - trade events;
  - an intermediary who already serves the buyer, such as accountants, insurers, suppliers or
    service contractors (strongest).

### W7 Buildable/deliverable by a solo founder with AI tools in ≤ 90 days (10)
"Easy to code" earns nothing by itself, because everyone can code now.
- **0**:
  - needs a licence, unproven technology, proprietary data the founder can't get, or deep IT
    integration; or
  - the value is a thin wrapper on one model provider that could cut access or compete.
- **5**: the software is buildable, but delivery depends on something uncertain: data access,
  accuracy for liability-bearing outputs, hardware certification, or human review that hasn't
  been costed.
- **10**: the evidence shows all of the following:
  - the needed data or APIs, or off-the-shelf hardware with prices, are available;
  - there is a realistic human-in-the-loop for liability-bearing outputs;
  - margin after AI or inference costs is plausible;
  - the first NON-code asset (a partner, first installs, sign-off) can start within 90 days.

### W8 Recurring revenue (10)
- **0**: a one-off or annual job; no reason to keep paying.
- **5**: the task recurs, but buyers buy per job today, or comparable products charge little.
  Or there are per-seat economics that AI shrinks.
- **10**: the task recurs at least monthly, AND buyers already pay retainers, subscriptions or
  per-unit fees for it. Ideally record-keeping duties keep the data valuable.
- *Evidence:* comparable subscription or retainer prices; recurring-duty sources.

### W9 Defensibility beyond code (5)
- **0**: the value is features, forms or a prompt over a third-party model. Or the buyer, or a
  tool they already pay for, could replicate or bundle it. Or the only moat is a compliance
  listing.
- **5**: one real non-code asset, still early. One of:
  - a named channel partner;
  - system-of-record status for legally required records;
  - a physical install;
  - specialist regulatory know-how.
  Switching costs alone score at most 5, because SMB churn runs about 3–7% a month.
- **10**: ≥ 2 compounding assets, such as:
  - a channel owned by someone already serving the buyer;
  - money flows or regulated records in the product;
  - outcome data that compounds;
  - an installed physical service;
  - a mission-critical job where failure costs far more than the price.

---

## Red flags (pull the relevant criterion down)
- Evidence is stated intent only: surveys, "would pay", waitlists (W2, W3).
- Per-seat pricing where AI shrinks seats (W8).
- AI outputs carrying liability with no accountable human (W7, possibly K3).
- An AI-run service form claimed with 70–90% margins on investor-thesis evidence only (W7, W8).
- Dead predecessors in the exact niche, unexplained (W3).
- The trigger has been delayed or withdrawn (W4).
- Buyers are reachable only via public procurement (K5).
