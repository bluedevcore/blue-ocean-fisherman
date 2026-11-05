# Round 0 (b) — AI-enabled services, and which demand signals predict willingness to pay

Topic report (not a problem evidence file). Researcher: v2 round-0 subagent (b). Date: 2026-11-05.

**Method / sourcing caveat (for the critic).** 35 WebSearch queries were run (the cap; listed under
"Queries run"). WebFetch is blocked by the session's network policy and was not used, so **every
bullet below rests on search-result titles/extracts and is marked "(search extract)"**. Where a
search summary did not tie a figure to one specific URL, the bullet cites the candidate URLs and
says "attribution uncertain". Vendor and investor marketing figures are labelled "(vendor claim)"
or "(investor thesis)". Geography is given as UK / US / EU / global. Number tags such as [12] point to
the numbered Sources list. v1's "Implications" section (round0-b-buyer-drivers.md) was read and is
not repeated; this report adds the AI-service and signal-reliability angle.

## Summary

- **The thesis is everywhere, the audited evidence is not.** Foundation Capital ("service-as-software",
  a $4.6T pool = ~$2.3T salaries + ~$2.3T IT/business-process services), Sequoia ("Services: The New
  Software", Mar 2026: copilot sells the tool, autopilot sells the work), YC (RFS Spring 2026
  "AI-native agencies", Summer 2026 "AI-native service companies") and General Catalyst (AI
  roll-ups across 7 industries, aiming for up to 20) all argue AI lets services be sold at
  software-like margins [1][2][3][5][6][8]. All margin figures found are investor claims, not audited
  results [12][13][16].
- **Pricing has moved to units of work.** Per outcome: Intercom Fin $0.99 per outcome; Zendesk
  ~$1.50–$2.00 per automated resolution [21][22]. Per task: Garfield.Law (UK, SRA-authorised) £2
  per chaser letter, £7.50 per letter before action, £50 per court claim [27]; Crosby ~"several
  hundred dollars"/~$400 per contract reviewed [30][31]. Retainer: UK outsourced credit control
  £129–£500/month [34][35][36]. Agents in labour-short markets are reportedly priced at 75–100% of the
  equivalent salary [25].
- **Hybrid human+software services have a poor survival record**: Bench (shut without warning, Dec
  2024), Botkeeper (closed Feb 2026 after 11 years and ~$90m raised), Builder.ai (2025 collapse after
  reports that "AI" work was done by ~700 engineers) [38][39][40][42].
- **Buyers will delegate routine admin but keep a human on high-stakes calls.** Bookkeeping is the top
  task SMBs want to delegate (30%, US) but also draws the most hesitation about AI (privacy, accuracy,
  trust) [45][46][47]. Agents are not yet autonomous: the best model fully completed only ~30% of 175
  simulated office tasks [44].
- **Liability is unresolved.** The SRA authorised Garfield.Law but keeps named solicitors accountable
  [27][28]. US insurers have filed generative-AI exclusions widely, and UK PI wordings are mostly
  silent on AI [49][50][51].
- **Signals: only revealed spend predicts payment.** Stated willingness to pay overstates real
  payment by a median ~1.35× and a mean ~3.2× in meta-analyses [52][53][54][55]. "No market need" was
  the most-cited failure reason in CB Insights post-mortems (42% of 101) [60]. Practitioners rank
  existing spend (salaries, outsourced services, contracts) above complaints, waitlists or LOIs
  [56][62][69][71].
- **Triggers work, but late and locally.** One OSHA enforcement press release led to 73% fewer
  violations at peer facilities within ~5 km [81][82]. Deadlines produce sign-up surges, but most
  firms move late: ~4% had signed up for MTD-VAT weeks before it started, and three-quarters of
  landlords missed the MTD-ITSA launch [77][78][80].
- **Bad reviews don't make buyers switch.** 59% of businesses regret a recent software purchase, but
  SMBs cite upfront cost (29%) and "good enough" (26%) as reasons not to switch, and ~92–93% plan to
  renew [73][75][76].

## AI-enabled services (evidence)

### Theses and market sizing (all investor theses, global/US)
- Foundation Capital's "service-as-software" sizes the pool at ~$4.6T: ~$2.3T of salaries in sales,
  marketing, software engineering, security and HR, plus ~$2.3T of IT and business-process services
  (Gartner figure). Its point is that AI moves from tool to service provider (investor thesis;
  search extract) [1][2].
- Sequoia, "Services: The New Software" (Julien Bek, Mar 2026). "A copilot sells the tool. An
  autopilot sells the work." It argues the next $1T company will be "a software company masquerading
  as a services firm". Secondary summaries add ~$6 spent on services for every $1 on software. It
  names Harvey (legal), with Crosby and Lawhive as "autopilot-native" newcomers (investor thesis;
  search extract) [3][4].
- YC RFS Spring 2026, "AI-native agencies" (Aaron Epstein): agencies selling finished work with
  software-like margins. YC RFS Summer 2026, "AI-native service companies": commentary says the
  best-suited services are information-intensive and judged on accuracy and speed, not creativity
  (search extract via mirrors) [5][6]. A critique argues that services run on trust, which takes
  years to build (search extract) [7].
- General Catalyst's "creation strategy" starts AI-native companies that buy mature service firms,
  automate them, and use the improved cash flow for more acquisitions. It has bets in 7 industries
  and plans up to 20 (search extract) [8][9]. Titan (IT managed services) raised $74m, and pilots
  reportedly automated 38% of typical MSP tasks (search extract) [10]. Long Lake rolls up
  HOA-management firms (search extract) [11]. An aggregator says GC targets doubling EBITDA margins
  by automating 30–70% of operations, but no primary GC source was found (unverified).

### Pricing models
- **Per outcome / per resolution** (US/global, vendor claims): Intercom Fin charges $0.99 per
  outcome, and an "outcome" can include handoffs and disqualifications as well as resolutions [21][23].
  Zendesk charges ~$1.50 per automated resolution on committed volume and $2.00 pay-as-you-go, as
  reported by a competitor's comparison [22]. HubSpot is moving AI pricing from per-use to
  per-resolution (title) [24]. All search extract.
- **Per task, fixed fee** (UK): Garfield.Law charges £2 for a "polite chaser", £7.50 for a letter
  before action and £50 to prepare and file a court claim, pay-as-you-go with no subscription, for
  debts up to £10k (search extract) [27][28]. Lawyers themselves use it to recover debts (title)
  [29].
- **Per document** (US): Crosby charges a fixed fee per contract (NDAs, MSAs, DPAs), "typically around
  $400" in one profile, with a median turnaround under an hour. Attribution between [30] and [31] is
  uncertain and no official price page was found (search extract) [30][31].
- **Retainer** (UK, outsourced credit control, vendor prices): Zmartly £129 / £250 / £499 per month
  [34]; Chaser's service from £310+VAT per month [35]; STA International from £500 per month [36]. A
  UK forum user puts the point where outsourcing beats a credit controller at about £10k/month of
  work. This is an anecdote and the figure's basis is unclear (search extract) [37].
- **Labour-anchored**: Tunguz says agents "command 75%, 85%, even 100% of a human equivalent salary"
  in some labour-short markets (search extract) [25]. Monetizely argues that software that does the
  task itself competes for the labour budget, not the software budget (search extract) [26].

### Gross margins vs SaaS
- Mayfield's Navin Chaddha (as reported by TechCrunch): if AI does 80% of the work, that work runs at
  80–90% gross margin, the blended business at 60–70%, and net income at 20–30% (investor thesis;
  search extract; attribution between [12] and [13] uncertain) [12][13].
- "Managed-service-as-software" essay: these businesses start at low (20–30%) gross margins while
  labour-heavy and move to 70–80% as AI takes over (investor thesis; search extract) [16].
- Counter-evidence: AI-native SaaS gross margins are said to run 20–40 points below classic SaaS,
  around 52% in 2026 against 70–90% (title plus extract; secondary) [17]. Commentary says services
  firms typically run 10–15% EBITDA and use AI to augment staff rather than replace them (search
  extract) [14].
- Valuation: tech-enabled services trade at ~1.5–2.5× revenue (12–16× EBITDA) against 3–8× revenue
  for SaaS [18]. A SaaS company pivoting to services moves from ~10× ARR to ~5–10× EBITDA [19].
  Services become dilutive above ~15–20% of revenue [20]. All search extract, secondary/opinion.

### Which tasks buyers will hand to an AI-run service
- US SMBs: bookkeeping is the top task to delegate (30% say handing it to someone else would help),
  with payroll second (OnPay 2025; search extract) [45].
- QuickBooks 2026 AI Impact Report (34,000+ owners, via a secondary write-up): bookkeeping ranks
  third for AI use (35%), and has the most hesitation of any category, over privacy, accuracy and
  trust (search extract) [46].
- Simply Business (1,047 US owners): "when the stakes get higher, the trust drops". Owners keep a
  human on insurance, finances and customer trust (search extract) [47].
- UK SMEs ask AI for financial advice before their accountant (title; search extract) [48].
- Information-intensive work judged on accuracy and speed suits AI services best: YC Summer 2026
  commentary (search extract) [6]. Live UK examples cover debt chasing and letters before action
  [27][29] and conveyancing/property law [32][33].

### Trust and liability
- The SRA authorised Garfield.Law, reported as the first purely AI-based firm allowed to provide
  regulated legal services in England & Wales. Named regulated solicitors stay accountable, and the
  AI may not suggest case law (search extract; attribution across [27][28] uncertain) [27][28].
- US insurance: one review counts 4,000+ adoptions of generative-AI exclusion forms across 49 states
  and DC, including W.R. Berkley's "absolute" AI exclusion on D&O/E&O. No court had yet ruled on how
  far these exclusions reach (search extract) [49].
- UK: PI policies mostly don't mention AI errors explicitly. Claims are likely to be treated as
  ordinary negligence, but "silent AI" is a recognised exposure (search extract) [50][51].
- AI-washing risk: Builder.ai's "AI" app-building reportedly relied on ~700 engineers. Reports
  describe hidden human labour, inflated revenue projections and an SEC investigation (unresolved)
  (search extract) [42][43].

### Failure modes
1. **Hybrid economics don't converge.** Bench combined software with human bookkeepers and shut
   without warning on 27 Dec 2024. One source blames shrinking capital and failure to reach
   profitability (search extract) [40]. Botkeeper, a human accountant + AI managed bookkeeping
   service, closed in Feb 2026 after 11 years and ~$90m of funding (search extract) [38][39]. Bench's
   founder has since raised $10M from Khosla for an AI bookkeeping start-up, Synthetic (title)
   [41].
2. **Agents are not autonomous.** On TheAgentCompany benchmark the top agent fully solved ~30% of 175
   office tasks. Social communication and complex web interfaces were the weakest areas (search
   extract) [44].
3. **Cutting oversight to chase margin.** Commentary on the TechCrunch piece warns that firms which cut
   staff may lose the oversight needed to catch flawed AI output (search extract) [15]. TechCrunch
   says early signs suggest the transformation "may be more complicated than VCs anticipate" (search
   extract) [12].
4. **Trust and track record.** Buyers choose service partners on years of results (critique) [7], and
   trust falls as stakes rise [47].
5. **Liability gaps**: AI exclusions in cover [49], and regulator conditions [28].

## Signal types and willingness to pay (evidence)

### Cross-cutting: stated vs revealed
- **Hypothetical bias.** Murphy et al. (2005), a meta-analysis of 28 studies (83 observations in the
  working paper), found a median hypothetical/actual ratio of ~1.35, heavily right-skewed (search
  extract) [52][53]. Kanya et al. (2019), 159 comparisons from 50 papers, mostly health, found
  hypothetical WTP on average 3.2× actual (range 0.7–11.8), with pooled effects of 1.8–2.4 (search
  extract; attribution between [54] and [55] uncertain) [54][55].
- **Commitment over compliments** (The Mom Test): compliments and "I would…" talk are bad data. Real
  signals cost the customer something: time, reputation risk or money (search extract) [56][57].
- **Disciplined testing pays.** In an RCT of 116 Italian start-ups, those taught hypothesis-testing
  performed better and pivoted more [58]. A replication across 759 firms in four RCTs found more
  idea termination and better search efficiency (search extract) [59].
- **Failure base rate**: 42% of 101 CB Insights post-mortems cited "no market need" [60]. A separate
  sample of 111 post-mortems gives 35% (search extract) [61].
- **"Existing spend" heuristic** (practitioner/vendor blogs, low weight): validation needs proof that
  a budget already exists. Spend can be headcount, consultants, agencies, freelancers or penalties.
  Absence of spend is "a red flag, not an untapped market" (vendor claim; search extract;
  attribution between [62] and [63] uncertain) [62][63].

### S1 Job ads (salary spent on the task)
- They prove a labour budget, which is the budget AI services price against [1][25][26]. Caveats:
  "signals should … not be treated directly as demand", only as a testable hypothesis [64]. Postings
  live 30–60 days, so velocity matters (e.g. five postings in 30 days) (vendor claim) [66]. A role
  that exists only to do the task ("manual data reconciliation analyst") is the strongest form; a
  general admin role is weak (vendor claim) [65][66]. All search extract.

### S4 Tenders and contract awards
- UK PPN 02/15 requires authorities to publish both opportunities and awards on Contracts Finder, so
  sub-threshold awards are a public record of the buyer, supplier and value (search extract) [86].
  Award notices show which primes hold frameworks, which means the route in is often subcontracting
  (search extract) [87]. No methodology paper testing tenders as a WTP predictor was found. They are
  strong on budget but imply a procurement process (K5 risk).

### S5 Freelance spend
- Fiverr FY2025: annual spend per buyer $342 (up from $302), active buyers ~3.1M (down from ~3.6M),
  and GMV from transactions over $1,000 up 22.8% (search extract) [68]. This is real spend but
  small-ticket and anchored to freelancer rates. The claim that an Upwork posting "commits budget" is
  a vendor's; a posting shows intent, not realised spend (search extract) [67]. Recurring postings
  for the same task by the same client type are the useful variant. No independent data was found.

### S2 Negative reviews of incumbents
- They show someone pays and is unhappy. Capterra (2025, ~3,500 businesses): 59% regret at least one
  purchase in the last 18 months, 70% of financial firms, and SMBs blame poor implementation and
  higher-than-expected total cost (search extract) [73][74]. But inertia is strong: US SMBs cite
  upfront cost (29%), "good enough" (26%) and lock-ins (14%) as reasons not to switch, and 44% didn't
  change their stack in a year [75]. Info-Tech found ~92–93% planning to renew [76] (search extract).
  Bad reviews therefore show a W3 gap only when they come with price complaints or active
  alternative-seeking.

### S6 Forum complaints
- A founder lists "I read complaint volume as demand" as a mistake. Threads sample who was annoyed
  enough to post, not who would pay (search extract) [69]. Reddit comments surface pain but "cannot
  confirm market demand" (search extract) [70]. Complaints count only when they come with spend or
  workaround evidence (e.g. a UK forum thread pricing outsourced credit control [37]).

### S3 Regulatory triggers
- Deadlines concentrate demand, but late. Weeks before MTD-VAT went live (Apr 2019), ~4% had signed
  up and ~1m businesses had not [77][78]. Under MTD-ITSA, >280,000 had signed up ahead of the first
  August 2026 filing deadline [79], yet three-quarters of landlords and sole traders missed the
  launch [80] (search extract). For scoring, a trigger is real but the sale often lands after the
  deadline. It favours firms already in the buyer's workflow (accountants, agents).

### S7 Enforcement, fines and losses
- Johnson (AER 2020): after one OSHA press release about a violation, peer facilities within ~5 km
  had 73% fewer violations. Matching that would take ~210 extra inspections. Releases followed
  penalties above ~$40–45k, and the effect was strongest where unions were strong (search extract)
  [81][82][83].
- GDPR fines cut market value by more than the fine itself (~−1% abnormal returns) (search extract)
  [84]. No study was found showing that fines raise firms' compliance budgets [85]. Publicised,
  local, sector-specific enforcement is the strong form; national fine totals are weak.

### Ranking of signal reliability (for predicting real willingness to pay)

| Rank | Signal | What it proves | Main failure mode | Evidence |
|---|---|---|---|---|
| 1 | Paid pre-sale / existing paying customers (not mined, but the anchor) | Revealed WTP | Small n | [52]–[57][71][72] |
| 2 | Incumbent or outsourced-service prices actually paid by this buyer (S2 + vendor price pages) | A budget line exists, at a known £ | Buyer may be happy (→K2) | [34]–[36][73] |
| 3 | Job ads with salary for a role dedicated to the task (S1) | A labour budget exists, recurring | The role covers many tasks; the hiring manager is not always the payer | [25][64]–[66] |
| 4 | Contract awards / tenders with values (S4) | Budget, buyer, renewal date | Procurement cycle (K5); prime-held frameworks | [86][87] |
| 5 | Publicised enforcement in the same sector/locality (S7) | Urgency that changes behaviour | National totals don't move individual buyers | [81]–[85] |
| 6 | Dated regulatory deadline (S3) | Timing, mandatory need | Late adoption; minimum-cost compliance | [77]–[80] |
| 7 | Recurring freelance postings with budgets (S5) | Willingness to outsource, small tickets | Price anchored to freelance rates; intent ≠ spend | [67][68] |
| 8 | Negative reviews alone (S2) | Dissatisfaction | Inertia: "good enough", switching cost | [73]–[76] |
| 9 | Forum complaints alone (S6) | Pain exists | Vocal minority; no spend | [69][70] |
| 10 | Surveys, waitlists, LOIs, "I would pay" | Interest | Hypothetical bias 1.35–3×; LOIs "cause more problems than they solve" | [52]–[57][71] |

Combinations beat any single signal. Spend (1–4) plus a trigger (5–6) is the profile to look for.

## Named examples

| Example | Type | Geography | Model / price | Status | Src |
|---|---|---|---|---|---|
| Garfield.Law | AI-run regulated law firm (small claims debt) | UK | £2 chaser / £7.50 LBA / £50 claim, PAYG | Authorised by the SRA (reported 2025; dates conflict across extracts) | [27][28][29] |
| Crosby | AI + lawyer contract review | US | ~$400 / contract (unofficial), <1 h | VC-backed | [30][31] |
| Lawhive / Woodstock Legal | AI platform bought a law firm (50+ consultant lawyers) | UK | Fixed fee (unconfirmed) | Acquired Sep 2025 | [32][33] |
| Intercom Fin; Zendesk AI | Per-resolution AI agents | Global | $0.99; ~$1.50–2.00 | Live | [21][22] |
| Titan; Long Lake; Crete | AI roll-ups (MSP; HOA; CPA) | US | Buy & automate | GC-backed (Crete's link unverified) | [8]–[11] |
| Chaser, Zmartly, STA | Outsourced credit control | UK | £129–£500 / month | Live (vendor) | [34]–[36] |
| Bench | Software + human bookkeepers | US/CA | Subscription | Shut Dec 2024 | [40] |
| Botkeeper | Human accountants + AI, for firms | US | Managed service | Closed Feb 2026 | [38][39] |
| Builder.ai | "AI" app building, humans behind it | UK/global | Project fees | Collapsed 2025 | [42][43] |
| Synthetic | AI bookkeeping (Bench founder) | US | n/a | $10M seed (Khosla) | [41] |

## Searched for but not found
- Audited gross margins for any AI-run service company (Crosby, Garfield, Lawhive, the GC roll-ups).
  Only investor theses were found.
- A primary GC source for "double EBITDA margins via 30–70% automation".
- An official Crosby price page.
- Any bootstrapped/small AI-run done-for-you business with verifiable revenue. Indie Hackers results
  were AI SaaS or API resellers with self-reported MRR.
- An SMB survey asking specifically about outsourcing tax/compliance to an AI-run *service*.
- The Ravical "90% of UK SMEs think compliance can be done by AI" survey's source page. It appeared
  in a summary but could not be tied to a URL, so it is not used.
- A causal study showing fines or enforcement raise firms' compliance *spending*. Only market-value
  and behaviour studies were found.
- Any study validating job ads, Upwork postings or tenders as predictors of purchase. Only vendor or
  practitioner blogs were found.
- Base rates for LOI → paid conversion.
- Primary essays by Rob Walling, Jason Cohen or Paul Graham on "find people already paying". None
  surfaced.
- A CB Insights update after 2014–2017.
- Fiverr's 2025 repeat-buyer share.
- An accounting-specific "considered switching but didn't" figure.
- Names and amounts of SEC "AI-washing" cases.
- Any report of Pilot (bookkeeping) closing. None was found; it is listed as still operating.

## Queries run
1. Foundation Capital "service-as-software" AI thesis $4.6 trillion
2. "services as software" AI-enabled services gross margin vs SaaS roll-up
3. Sequoia "services: the new software" autopilot AI 2025
4. outcome-based pricing AI agents Intercom Fin $0.99 per resolution Zendesk per automated resolution
5. AI bookkeeping service startup failure human accountants behind AI Pilot Bench closure
6. General Catalyst AI roll-up strategy acquire services firms margins Crete Long Lake 2025
7. Crosby AI law firm contract review flat fee per contract hours turnaround pricing
8. TechCrunch "AI services transformation may be harder than VCs think" margins human workers
9. survey small businesses trust AI to handle bookkeeping tax compliance tasks would outsource 2025
10. professional indemnity insurance AI errors exclusion insurers AI-generated advice liability 2025
11. Y Combinator request for startups "AI-native" agencies services full-stack company 2025
12. bootstrapped AI-powered done-for-you service small business revenue indie hacker productized service AI agents MRR
13. Garfield.Law SRA approved AI law firm debt recovery price per letter small claims
14. Builder.ai collapse "AI washing" human engineers 2025 lessons; SEC AI washing enforcement
15. AI credit control service small business chasing invoices pricing per month UK done-for-you outsourced credit controller
16. tech-enabled services gross margin 40% 60% investors "tech-enabled services" valuation multiple lesson Pilot Bench gross margin
17. hypothetical bias willingness to pay meta-analysis stated vs actual payment overstatement ratio
18. "The Mom Test" compliments fluff commitment advancement currency time money reputation validation signal
19. Camuffo Gambardella scientific approach entrepreneurs randomized control trial hypothesis testing revenue pivot results
20. startup idea validation "already paying" existing budget spend signal "spending money" problem Rob Walling OR Jason Cohen OR Paul Graham
21. job postings as signal for startup ideas automate the role companies hiring for repetitive task "job postings" demand validation B2B
22. Upwork recurring job postings validate business idea freelance marketplace demand productized service spend data
23. CB Insights top reasons startups fail "no market need" percent post-mortems 2021 update
24. Capterra software buying trends survey percent businesses switched software regret purchase reasons 2025
25. Making Tax Digital deadline drove software adoption small businesses spike sign-ups bridging software 2019 2026 income tax evidence
26. study enforcement fines increase compliance spending firms GDPR enforcement effect on compliance investment empirical
27. "Regulation by Shaming" OSHA press releases deterrence nearby facilities fewer violations Johnson American Economic Review
28. Reddit complaints not a reliable demand signal people complain but won't pay startup validation lesson founder post-mortem
29. letters of intent pre-orders startup validation reliability non-binding LOI conversion paying customers versus waitlist signups
30. using public procurement contract award data to identify market opportunities recurring contracts SMEs Contracts Finder Find a Tender spend analysis
31. AI agents target labor budgets not IT budgets salary spend pricing AI employee replace headcount a16z OR Bessemer 2025
32. TheAgentCompany benchmark AI agents complete percent of real workplace tasks autonomously Carnegie Mellon results
33. small businesses stay with software despite dissatisfaction switching costs status quo survey percent considered switching but didn't accounting practice management
34. Lawhive acquires law firm AI-native legal services UK 2025 fixed fee model
35. Fiverr 2025 annual spend per buyer active buyers repeat buyers share of marketplace revenue results

## Sources
All seen as search results only (WebFetch blocked). Tags follow roles/researcher.md.
1. [OTHER] https://foundationcapital.com/ai-service-as-software/ — Foundation Capital, "AI leads a service as software paradigm shift" (investor)
2. [OTHER] https://foundationcapital.com/the-ai-hype-600b-question-or-4-6t-opportunity/ — Foundation Capital (A. Garg), "$600B question or $4.6T+ opportunity?", 2024
3. [OTHER] https://sequoiacap.com/article/services-the-new-software — Sequoia, "Services: The New Software", Mar 2026
4. [OTHER] https://tosea.ai/blog/sequoia-insight-autopilot-services-software — secondary summary of the Sequoia essay
5. [OTHER] https://modelence.com/yc-rfs-spring-2026/ai-native-agencies — mirror of YC RFS Spring 2026, "AI-native agencies"
6. [OTHER] https://modelence.com/yc-rfs-summer-2026/ai-native-service-companies — mirror of YC RFS Summer 2026
7. [OTHER] https://cherry-picked-gigi.beehiiv.com/p/yc-is-wrong-about-ai-native-agencies — newsletter critique
8. [OTHER] https://www.cognitiverevolution.ai/the-revolution-in-services-general-catalysts-ai-rollup-strategy-with-marc-bhargava/ — podcast, GC AI roll-up strategy, Aug 2025
9. [OTHER] https://capitalandclarity.substack.com/p/the-general-catalyst-behind-15-billion — "The General Catalyst behind $1.5B of AI roll-ups"
10. [OTHER] https://www.privateequitywire.co.uk/general-catalyst-backs-ai-driven-it-services-platform-titan-with-74m-investment/ — PE Wire, Titan $74m
11. [OTHER] https://www.generalcatalyst.com/stories/manufacturing-outliers-long-lake — GC, Long Lake
12. [OTHER] https://techcrunch.com/2025/09/28/the-ai-services-transformation-may-be-harder-than-vcs-think/?rand=324 — TechCrunch, Sep 2025 (the search index showed a different headline for this URL; the slug matches)
13. [OTHER] https://techcrunch.com/2025/06/29/why-ai-will-eat-mckinseys-lunch-but-not-today — TechCrunch, Jun 2025, Navin Chaddha
14. [OTHER] https://www.inkl.com/news/ai-rollup-investors-think-services-firms-can-trade-more-like-software-companies-here-s-what-they-get-wrong — Fortune commentary (syndicated)
15. [OTHER] https://www.squaredtech.co/ai-services-transformation-harder-than-vcs-think — summary of the TechCrunch piece
16. [OTHER] https://dannguyenhuu.substack.com/p/introducing-the-managed-service-as — "Managed-Service-as-Software" essay (investor)
17. [OTHER] https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-31-ai-native-saas-gross-margins-are-still-running-20-40-points — Enterprise DNA, Jul 2026
18. [OTHER] https://ibinterviewquestions.com/guides/tmt-investment-banking/tech-enabled-services-vs-pure-software — banking guide on multiples
19. [OTHER] https://sahilpatwa.substack.com/p/ai-powered-roll-ups-part-iv-the-pivot — "AI-Powered Roll-ups Part IV"
20. [OTHER] https://livmo.com/blog/software-enabled-services-valuation-the-saas-margin-gap/ — software-enabled services valuation, 2026
21. [OTHER] https://www.intercom.com/learning-center/ai-customer-service-agent-pricing-comparison — Intercom (vendor)
22. [OTHER] https://fin.ai/learn/ai-customer-service-agent-pricing-comparison — Intercom/Fin (vendor), Zendesk rates
23. [OTHER] https://www.getmacha.com/blog/intercom-fin-vs-zendesk-ai-pricing — Macha comparison (vendor)
24. [OTHER] https://www.saastr.com/hubspot-switching-ai-pricing-from-per-use-to-per-resolution/ — SaaStr
25. [OTHER] https://www.tomtunguz.com/observations-about-agent-pricing/index.md — T. Tunguz, observations on agent pricing
26. [OTHER] https://www.getmonetizely.com/monetizing-agentic-ai-book-saas/the-revenue-line-labor-budgets-not-software-budgets — Monetizely book chapter
27. [OTHER] https://www.lawgazette.co.uk/news/sra-approves-2-letter-ai-law-firm/5123191.article — Law Gazette, SRA approves £2-letter AI firm
28. [OTHER] https://www.globallegalpost.com/news/legal-regulator-approves-first-ai-driven-law-firm-1313197284 — Global Legal Post
29. [OTHER] https://www.legalfutures.co.uk/latest-news/lawyers-using-ai-law-firm-to-recover-their-debts — Legal Futures
30. [OTHER] https://sacra.com/c/crosby — Sacra profile of Crosby
31. [OTHER] https://research.contrary.com/company/crosby — Contrary Research profile of Crosby
32. [OTHER] https://www.legalcheek.com/2025/09/google-backed-ai-platform-buys-law-firm-in-uk-legal-industry-first/ — Legal Cheek, Sep 2025
33. [OTHER] https://www.lawgazette.co.uk/news/ai-platform-buys-existing-firm-as-law-embraces-new-tech/5124460.article — Law Gazette, Lawhive/Woodstock
34. [OTHER] https://zmartly.co.uk/services/credit-control-services-uk — Zmartly (vendor price page)
35. [OTHER] https://www.chaserhq.com/blog/why-you-should-consider-outsourcing-your-credit-control-and-accounts-receivables — Chaser (vendor)
36. [OTHER] https://stainternational.com/?p=13568 — STA International, outsourced credit control (vendor)
37. [S6] https://www.ukbusinessforums.co.uk/threads/costs-of-outsourcing-credit-control-and-also-debt-collection.174950/ — UK Business Forums thread
38. [OTHER] https://www.cpapracticeadvisor.com/2026/02/09/botkeeper-is-closing-its-doors/177677/ — CPA Practice Advisor, Feb 2026
39. [OTHER] https://cfotech.co.uk/story/ai-bookkeeping-startup-botkeeper-shuts-after-11-years — CFOtech UK
40. [OTHER] https://www.outsourceaccelerator.com/?p=139896 — "Lessons from the $100m Bench Accounting fiasco"
41. [OTHER] https://aiproductivity.ai/news/ian-crosby-synthetic-ai-bookkeeping-khosla-10-million/ — Synthetic $10M
42. [OTHER] https://www.eweek.com/news/builderai-bankruptcy-ai-developers-coding/ — eWeek, Builder.ai
43. [OTHER] https://techspot.com/news/108173-builderai-collapses-after-revelation-ai-hundreds-engineers.html — TechSpot, Builder.ai
44. [OTHER] https://arxiv.org/html/2412.14161v3 — TheAgentCompany benchmark (CMU et al.), arXiv
45. [OTHER] https://onpay.com/insights/2025-small-business-outlook/ — OnPay 2025 small business outlook (US)
46. [OTHER] https://beancount.io/blog/2026/07/13/quickbooks-ai-impact-report-small-business-trust-guide — secondary write-up of the QuickBooks AI Impact Report
47. [OTHER] https://www.simplybusiness.com/small-businesses-are-using-ai-but-theyre-not-letting-it-run-the-show-2026-outlook/ — Simply Business 2026 outlook (US)
48. [OTHER] https://cfotech.co.uk/story/uk-smes-turn-to-ai-before-accountants-survey-finds — CFOtech UK
49. [OTHER] https://www.jdsupra.com/legalnews/the-ai-coverage-gap-what-new-insurance-6589089/ — JD Supra (Lathrop GPM), AI insurance exclusions (US)
50. [OTHER] https://www.dacbeachcroft.com/en/what-we-think/professional-indemnity-insurance-risk-of-ai-hallucinations — DAC Beachcroft (UK)
51. [OTHER] https://kennedyslaw.com/en/thought-leadership/article/2025/silent-ai-cover-the-unforeseen-risks-for-insurers — Kennedys, 2025
52. [OTHER] https://econpapers.repec.org/RePEc:kap:enreec:v:30:y:2005:i:3:p:313-325 — Murphy et al. 2005, Env. & Resource Economics
53. [OTHER] https://ageconsearch.umn.edu/record/14518 — Murphy et al. working paper
54. [OTHER] https://researchonline.lshtm.ac.uk/id/eprint/4653245 — LSHTM repository (WTP meta-analysis; attribution uncertain)
55. [OTHER] https://econpapers.repec.org/RePEc:ehl:lserod:100741 — LSE repository record (WTP meta-analysis; attribution uncertain)
56. [OTHER] https://mtlynch.io/book-reports/the-mom-test/ — book report, The Mom Test
57. [OTHER] https://www.ybrikman.com/blog/2023/03/29/the-mom-test/ — book review, The Mom Test
58. [OTHER] https://econpapers.repec.org/RePEc:cpr:ceprdp:12421 — Camuffo et al., CEPR DP12421 (RCT)
59. [OTHER] https://www.ie.edu/research/research-publications/a-scientific-approach-to-entrepreneurial-decision-making-large-scale-replication-and-extension/ — replication (SMJ 2024)
60. [OTHER] https://entrepreneur.com/article/238088 — Entrepreneur on CB Insights' 101 post-mortems
61. [OTHER] https://www.smartcompany.com.au/startupsmart/analysis/startups-fail-founders-capital/ — SmartCompany, 111 post-mortems
62. [OTHER] https://bigideasdb.com/multi-signal-startup-idea-validation — idea-validation vendor blog
63. [OTHER] https://painonsocial.com/blog/validation-signals-startup-idea — idea-validation vendor blog
64. [OTHER] https://blog.bloola.com/digital-change/signals-do-not-yet-indicate-a-need — "Signals do not yet indicate a need"
65. [OTHER] https://www.trend-seeker.app/blog/job-ads-business-ideas — vendor blog, job ads → ideas
66. [OTHER] https://www.cotera.co/articles/hiring-signals-b2b-intent-data.md — vendor, hiring signals
67. [OTHER] https://bigideasdb.com/validate-saas-demand-with-upwork-jobs — vendor, Upwork demand validation
68. [OTHER] https://www.fiverr.com/news/fiverr-q4-earnings-2025 — Fiverr Q4/FY2025 results
69. [S6] https://www.indiehackers.com/post/four-ways-mining-reddit-for-startup-ideas-went-wrong-for-me-and-one-disclosure-307e18f861 — Indie Hackers founder post
70. [OTHER] https://dev.to/ideacrystal/why-reddit-scraping-isnt-enough-for-saas-validation-1cem — DEV Community post
71. [OTHER] https://www.skmurphy.com/blog/2015/05/21/assessing-prospect-intent/ — SKMurphy, on LOIs
72. [OTHER] https://kromatic.com/real-startup-book/2-evaluative-market-experiments/value-proposition-test/pre-sales-smoke-test/ — Real Startup Book, pre-sales test
73. [OTHER] https://www.accountingtoday.com/news/70-regret-at-least-one-software-purchase-over-last-year — Accounting Today on Capterra
74. [OTHER] https://capterra.com/resources/tech-trends-smb-enterprise-software-purchase-tips/ — Capterra 2025 Tech Trends
75. [OTHER] https://www.expertmarket.com/small-business/switching-tech-fuels-smb-regret — Expert Market SMB switching survey (US)
76. [OTHER] https://www.ivanti.com/blog/press-pause-on-auto-renewals-how-to-brave-a-software-switch — Ivanti citing Info-Tech (vendor)
77. [OTHER] https://www.itpro.com/digital-transformation/33313/only-4-of-businesses-have-signed-up-for-making-tax-digital — ITPro, 2019
78. [OTHER] https://www.which.co.uk/news/2019/03/hmrcs-new-digital-vat-system-starts-tomorrow-and-1m-businesses-still-havent-signed-up — Which?, Mar 2019
79. [OTHER] https://www.taxi-point.co.uk/post/more-than-280-000-sign-up-to-hmrc-s-making-tax-digital-ahead-of-first-august-filing-deadline — TaxiPoint, 2026
80. [OTHER] https://thenegotiator.co.uk/news/regulation-law-news/three-quarters-of-landlords-miss-digital-tax-sign-up-deadline/ — The Negotiator, 2026
81. [OTHER] https://www.aeaweb.org/doi/10.1257/aer.20180501 — Johnson, "Regulation by Shaming", AER 2020
82. [OTHER] https://sanford.duke.edu/story/one-press-release-osha-violations-yields-compliance-equal-210-inspections/ — Duke Sanford
83. [OTHER] https://www.safetyandhealthmagazine.com/articles/19792 — Safety+Health magazine
84. [OTHER] https://repository.uel.ac.uk/item/89zxy — "Impact of GDPR infringement fines on the market value of firms"
85. [OTHER] https://www.americanbar.org/groups/antitrust_law/resources/source/2021-june/persisting-effects-eu-data — ABA, Jia/Jin/Wagman on GDPR effects
86. [OTHER] https://tendertracker.co.uk/guides/contracts-finder — TenderTracker guide (PPN 02/15)
87. [OTHER] https://openopps.com/blog/how-smes-can-find-and-win-public-sector-contracts-uk-procurement-act-2023/ — Open Opps (vendor)

## Implications for the v2 rubric
Score revealed behaviour only: stated WTP overstates payment ~1.35–3× [52][54]; compliments,
waitlists and LOIs score 0 [56][71].

**W2 Budget proof.** 10 = two or more independent spend types for this exact task and buyer, with £
figures: a salaried job ad naming the task, an incumbent or outsourcer price (e.g. credit control
£129–£500/month [34][36]), or a valued contract award [86]. 5 = one spend type, or spend on a broader
role. 0 = complaints, surveys or micro-gigs only.

**W3 Gap.** 10 = paid incumbents exist but are priced or packaged out of this buyer's reach, plus
buyer complaints about price or service. 5 = bad reviews alone; inertia is strong (29% upfront cost,
26% "good enough", ~92–93% renew [75][76]). 0 = cheap, well-reviewed incumbent (→K2).

**W4 Why now.** 10 = dated 2025–28 mandatory deadline plus publicised enforcement in the
buyer's sector (one OSHA press release ≈ 73% fewer violations at nearby peers
[81]). 5 = a deadline with known slow uptake (~4% signed up weeks before MTD-VAT [77]), or guidance
only. 0 = "AI now makes it possible" (supply, not a buyer trigger).

**W8 Recurring.** 10 = the task recurs at least monthly and buyers already pay retainers or per-unit
fees for it [21][34]. 5 = the task recurs but is bought per job (Garfield's per-letter fees [27]).
0 = one-off or annual.

**K1**: hit if there is no £ spend evidence beyond freelance gigs or forum posts. **K2**: needs
evidence the incumbent is both cheap and well reviewed by this buyer; bad reviews of an expensive
incumbent count for W3. **K4**: hit if the pain is evidenced only by vendors, idea-validation tools
or investor TAMs [2]; require at least one job ad, tender, regulator record or buyer forum post.
**K5**: tenders prove budget but imply procurement; hit if a tender is the only route.

**AI-run service form.** Credit it only with an accountable professional where regulated [28], PI
cover without an AI exclusion [49], and costed human review. Agents finished ~30% of
office tasks [44]. 70–90% margins are investor theses [12][16]; Bench and Botkeeper failed [38][40].
