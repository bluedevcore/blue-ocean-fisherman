# BLUE OCEAN FISHERMAN — Scoring Rubric (FROZEN)

**Status: FROZEN at Round 0 (2026-11-05). Never relax or rewrite this file.**

Derived from the protocol's draft criteria, refined with the Round 0 research:
`research/round0-a-iot-failures.md`, `research/round0-b-buyer-drivers.md`,
`research/round0-c-niche-case-studies.md`. The three key lessons from that research:
(1) "no market need / unclear ROI" is the top killer of IoT products, so money and proof of
pain are gates. (2) Survivors sold through a party that already holds the risk or already
visits the site, such as insurers, service contractors, distributors or suppliers. (3) The
best recurring revenue comes from record-keeping duties, not from "insight" alone.

Ten criteria, each scored as an integer from 0 to 10, total /100. Anchors are given for 0,
5, 7 and 10. Interpolate between them; for example, 8–9 means beyond 7 but missing part of
the 10 requirement. The 7 anchor matters because acceptance needs every criterion ≥ 7.

## General scoring rules (apply to every criterion)
1. **Only sourced evidence counts.** A claim in the evidence file without a URL is ignored.
2. **Vendor claims are weak.** Figures that come only from a vendor selling a related product
   can support at most **5** on c1, c2, c3 and c10, unless an independent source corroborates them.
3. **Broken, fabricated or misrepresented sources score 0.** If a source the critic checks is
   fabricated, dead or does not say what is claimed, the criterion relying on it scores 0
   unless independent verified evidence supports it.
4. **Geography.** Evidence from comparable markets (UK, EU, US, AU, NZ, CA) is acceptable,
   but the critic should note mismatches; for example, a US regulation does not create UK
   compliance pressure.
5. **9–10 needs breadth.** A 9 or 10 on any criterion requires at least two independent
   sources, or one primary authoritative source (regulator, statute, standards body, insurer
   policy wording) plus one corroborating source.
6. **Absence of evidence is evidence.** If the researcher searched for something and recorded
   "not found", score accordingly. Do not fill gaps with plausibility.

---

## c1. Cost of incident is quantifiable in money
Does an incident (or the ongoing problem) cost a quantifiable, sourced amount of money,
enough to pay for the product many times over?
- **0**: No money figure, or the pain is inconvenience only.
- **5**: Sourced figures exist but are national or industry aggregates only, vendor-only, or
  £500–£2k per incident. Or the loss per site per year is under ~3× the plausible annual
  cost of the product.
- **7**: At least one independent sourced figure per incident or per site of ≥ ~£2k
  (or equivalent). The loss is plausibly ≥ 5× the product's annual total cost of ownership
  (amortised hardware + subscription + install).
- **10**: Two or more independent sourced figures for this niche (fines, insurance claims,
  stock or animal losses, downtime, write-offs) of ≥ ~£5k per incident or ≥ ~£2k per site
  per year. Together they imply payback within 12 months.
- *Evidence required*: URLs with explicit £/$/€ amounts tied to this specific problem.

## c2. Frequency: the pain recurs weekly or monthly, not rarely
Pain that recurs can be shown inside a 1–3-month pilot. Rare catastrophic events can't, and
the research shows that's where pilots stall. The recurring pain can be the incident itself
OR the mandated manual task the sensor replaces.
- **0**: A rare event (once every several years per site) with no data.
- **5**: Incidents or tasks roughly yearly per site, or large aggregate counts with no rate per site.
- **7**: Sourced evidence of incidents several times a year per site, OR a required or
  routine manual check at least monthly.
- **10**: Sourced evidence that the pain event or the required manual task recurs daily or
  weekly per site, so value is demonstrable within a 1–3-month pilot.
- *Evidence required*: incident statistics, inspection/check schedules, regulator-required
  check frequencies, or credible first-hand accounts, all with URLs.

## c3. Existing paid or labour-heavy workaround
Do people already spend money or labour on this (paper logs, manual checks, site visits,
paid services), so that the sensor replaces a cost rather than creating a new one?
- **0**: Nobody does anything and there is no evidence anyone tries.
- **5**: A workaround exists (manual checks, paper logs, visits) but there's no evidence of
  its labour or cost.
- **7**: A documented manual routine or paid service, with some sourced indication of its
  time, frequency or cost.
- **10**: A documented workaround with quantified labour or £ cost (hours per week, cost per
  visit, contractor fees, staff rounds) from a credible source, which the sensor would remove
  or substantially reduce.
- *Evidence required*: URLs showing the workaround and, for 10, its cost.

## c4. Compliance, insurance or audit pressure demands proof
- **0**: No regulation, standard, insurer or contract pressure.
- **5**: Guidance or best practice recommends monitoring; insurers mention it informally or
  offer referral discounts.
- **7**: A named regulation, standard, contract or insurer condition requires checks or
  records (even if manual records would satisfy it), OR insurers subsidise or fund such devices.
- **10**: A named rule, standard or insurer condition requires monitoring or records, AND
  there is evidence of enforcement in this niche: fines, prosecutions, improvement or
  prohibition notices, failed audits, or claims refused or excluded.
- *Evidence required*: a URL to the regulation, guidance or insurer wording; for 10, URLs to
  enforcement cases or claim refusals.

## c5. Identifiable buyer with budget
- **0**: "Businesses", consumers or hobbyists; no identifiable payer.
- **5**: A plausible job title, but budget ownership is unevidenced or fragmented, or the
  sale is stuck in slow public procurement with no evidenced route.
- **7**: A specific job title evidenced (job adverts, trade bodies, org descriptions) as
  responsible for this risk or process, plausibly with discretionary operational budget.
- **10**: A specific job title evidenced as owning both the loss AND a budget for it (job
  advert or role description stating budget or purchasing responsibility, trade press), able
  to buy at the target price without lengthy enterprise or IT procurement.
- *Deductions*: −2 if the buyer is IT, or if the product needs integration with the
  customer's corporate network or IT approval to work.
- *Evidence required*: URLs (job ads, role descriptions, trade bodies, case studies naming the buyer).

## c6. Distribution channel that already visits the site
Survivors in the research sold through someone already holding the risk or already on site.
Cold direct sales to fragmented SMEs is the classic failure mode.
- **0**: Only cold direct sales to fragmented sites; no intermediary identified.
- **5**: A regular site visitor or reseller exists (service engineer, installer, wholesaler,
  buying group, supplier rep, insurer surveyor), but there's no evidence they sell
  technology or monitoring.
- **7**: A named channel that regularly visits or serves this site type, with evidence that
  it sells, installs or bundles adjacent technology or services.
- **10**: Named channel(s) already reselling, installing or bundling comparable monitoring
  for this exact site type (insurer programme, service contractor's monitoring offer,
  distributor catalogue listing, supplier-provided telemetry), with evidence.
- *Evidence required*: URLs naming the channel and showing what it already sells.

## c7. Market proven but underserved
- **0**: No evidence anyone pays for anything similar, OR a cheap, good-enough incumbent
  dominates (free kit bundled by suppliers, ~£25/yr equivalents, a feature already built
  into equipment the buyer owns).
- **5**: Priced competitors exist, but their fit to this niche is unclear and the gap is
  asserted rather than evidenced. Or the market is crowded.
- **7**: Paying customers for comparable products are evidenced (prices, customer counts,
  funding), AND there is some evidence of a gap in this niche (enterprise-only pricing, no
  niche-specific product, or complaints).
- **10**: Willingness to pay is proven by priced incumbents in this or adjacent niches, AND
  there is clear evidence of a gap: incumbents are enterprise-only, expensive or clunky (with
  sourced complaints or prices), or none target this niche. Any dead predecessors in this
  exact niche are explained (wrong channel, old radio tech, etc.).
- *Evidence required*: competitor URLs with prices or positioning; complaint or review URLs.

## c8. Buildable
Off-the-shelf components, a plausible BOM under ~£50, and no exotic certification.
- **0**: Needs an exotic or unproven sensing method, or ATEX/IECEx, medical device (MDR/FDA),
  MCERTS or metrology type approval, or other safety-critical certification.
- **5**: Feasible, but has one or more of these problems:
  - the BOM is likely £50–£150;
  - it needs calibration or traceability certificates, a custom probe, or survival in a
    harsh environment;
  - battery life or connectivity is questionable for the site, for example RF trapped by
    steel, concrete, underground or water;
  - it depends on the customer's IT network;
  - the physics is prone to false alarms.
- **7**: Off-the-shelf sensors and pre-certified radio modules are evidenced, and the BOM is
  plausibly ≤ ~£50–60. Connectivity and power are plausible for the environment.
- **10**: All of the following are evidenced:
  - comparable off-the-shelf devices or modules with prices showing a BOM under ~£50;
  - a pre-certified LPWAN or cellular module, with no customer IT needed;
  - multi-year battery life at a realistic reporting interval, or easy mains power;
  - only standard CE/UKCA/FCC radio compliance;
  - self-install in under 30 minutes is plausible.
- *Evidence required*: component or comparable-device URLs with prices or specifications.

## c9. Recurring revenue potential
Does the data or alerting stay valuable long after install, so a subscription is justified?
- **0**: A one-off sale; the data has no value after install or diagnosis.
- **5**: Ongoing alerts are useful, but the case for a subscription is thin, or comparable
  products charge only ~£1–3 per month.
- **7**: There's a structural reason the data stays valuable (ongoing record-keeping, audits,
  consumables, recalibration, insurer reporting), and comparable products are evidenced
  charging subscriptions.
- **10**: Records must be retained or produced on a statutory, insurer or contract schedule,
  AND comparable products are evidenced charging ≥ ~£100 per site per year or ≥ ~£5 per
  sensor per month.
- *Evidence required*: URLs for the record-keeping duty and for comparable subscription pricing.

## c10. Public evidence of pain
- **0**: None found.
- **5**: One or two public mentions, or only vendor case studies or marketing, or only one
  source type.
- **7**: At least two independent, non-vendor public sources of different types, for example
  trade press plus a forum thread, or a regulator notice plus news.
- **10**: Three or more independent source types: regulator or enforcement data (or insurer
  loss data), trade press, AND first-hand complaints (forums, Reddit, reviews,
  ombudsman/tribunal cases).
- *Evidence required*: URLs of each.

---

## Red flags (critics should look for these; each should pull the relevant criterion down)
- Pain is evidenced only by vendor marketing or "visibility/insight" language (c1, c10).
- The loss is below ~5× the product's total annual cost of ownership (c1).
- Value is only provable through a rare catastrophic event (c2).
- Direct enterprise sales needing IT and OT sign-off, with no channel (c5, c6).
- Dead predecessors in the exact niche with no explanation of why this time differs (c7).
- Commoditised category: free or ~£25/yr equivalents exist (c7, c9).
- Custom sensing element, ATEX or medical certification, dependence on 2G/3G or a single
  proprietary network, or reliance on the customer's IT (c8).
- One-off diagnosis value; bulk hardware sales not tied to an ongoing service (c9).

## Acceptance (from CLAUDE.md — repeated for reference, not changed here)
Total ≥ 90/100, no criterion < 7, at least 8 distinct credible working URLs in the evidence
file, at least 3 URLs verified by the critic by fetching, survived the Devil's Advocate, and
materially different from every already-accepted idea.
