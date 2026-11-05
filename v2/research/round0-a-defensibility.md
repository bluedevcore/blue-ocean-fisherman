# Round 0 (a): What makes a small business defensible when software is cheap to build (2024–2026)

Topic report (not a problem evidence file). Researcher: v2 round 0. Date: 2026-11-05.
Budget: 35/35 WebSearch queries used. **WebFetch was blocked by the network policy**, so no
page was opened in full. Every claim below comes from what the search results showed (titles and
extracts), so every bullet is marked "(search extract)". Figures from vendors or vendor-run surveys
are labelled "(vendor claim)" or "(vendor survey)". Where a figure appeared in the results but could
not be pinned to one URL, it is either flagged or left out. Geography: mostly US or global; UK items
are marked **[UK]**. The v1 IoT channel findings (insurers and equipment suppliers as channels) are
in `v1/research/round0-a-iot-failures.md` ("Implications") and are not redone here.

## Summary
- **Code has stopped being a moat.** About a quarter of YC's Winter 2025 founders said more than 95% of their code was AI-generated [38]. Cloudflare says one engineer re-implemented the Next.js API surface in about a week for about $1,100 in tokens (company claim; "not production-ready" per [65]) [64][65]. 35% of Retool's surveyed customers have already replaced at least one SaaS tool with something they built (vendor survey) [55].
- **Markets have repriced software on this basis.** The February 2026 "SaaSpocalypse" followed Anthropic's Claude Cowork plugins [5][6][7]. Constellation Software, the main buyer of niche vertical software, roughly halved over 12 months partly on AI fears [9]. Rightmove [UK] fell about 12–13% in a day when it announced heavy AI spending [48].
- **What still holds, according to the sources:**
  - distribution owned through a party that already serves the buyer (accountants for Xero; banks for FreeAgent) [19][80];
  - acting as the system of record for money flows or regulated records (embedded payments) [16];
  - mission-critical use, where the cost of failure dwarfs the cost of the software [14][3];
  - physical installation or hardware plus service [44][45];
  - real network effects [60][50];
  - outcome data plus services ([85], vendor claim).
- **Each of these has a failure mode in the evidence:**
  - switching costs are weak for SMBs, with 3–7% monthly churn [36][37];
  - a compliance listing is shared by 128 products [41];
  - hardware plus service can be sticky without growing (Checkit: ARR flat at about £14.3m) [71][73];
  - a community moat collapses when an LLM answers the question (Stack Overflow) [52][53];
  - wrappers die when the model owner competes (Jasper, Windsurf) [26][62].
- **AI-native products have worse unit economics.** Bessemer's fastest growers ("Supernovas") reportedly run at about 25% gross margin, against about 60% for "Shooting Stars" [24][25]. SaaS CEOs report customers asking for AI-related price cuts (82%), and 54% fear customers building their own tools more than they fear AI startups (vendor survey) [83][84].
- **[UK] Small-business buyers are wary of AI.** 92% of FSB members worry about AI risks [74]. Nearly half trust AI less than work led by people [76]. Trust and accountability therefore act as a moat in their own right.

## Moat types

### 1. Distribution: owning a channel, partnering with those who already visit the buyer, community
- **Xero (accounting, ANZ/UK):** in 2013 Xero's Australian MD said "Seventy percent of our new customers come via the accountant or bookkeepers." (search extract) [19]. The CEO put channel-generated revenue at "60 to 70 percent … in ballpark" (search extract) [20]. Xero's partner programme is free, and it says 250,000+ accountants and bookkeepers use Xero in their practice (search extract) [21]. *Mechanism:* the adviser already sees the buyer every month or year and recommends the tool.
- **FreeAgent [UK]:** NatWest group business current-account holders get the standard version free "as long as you retain your bank account". Mettle (NatWest's digital bank) has offered it free since April 2020 (search extract) [80][82]. FreeAgent tells accountants "every month, over 1,000 of these customers look for an advisor who's familiar with FreeAgent" (search extract) [81]. *Implication:* if a bank, insurer or software incumbent gives a feature away free to the same buyer, a standalone paid product in that space has no moat. **No user count for the bank channel was found.**
- **Distribution as "the last moat" is mostly opinion.** TechCrunch (Jan 2026) describes GTMfund's thesis that distribution is the final moat in the AI era (search extract) [22]. No rigorous study showing that distribution predicts AI-era success was found (see "Searched for but not found").
- **Reputation and peers drive SMB shortlists.**
  - Capterra's buyer survey (about 3,500 buyers in 9 countries incl. UK, Aug 2024) found 59% regret at least one software purchase from the last 18 months (search extract) [56].
  - Canadian firms build vendor shortlists on reputation (55%), previous experience (47%) and peer recommendations (36%) (search extract) [57].
  - For SMBs, the main cost of a regretted purchase is increased costs (search extract) [89].
  - [UK] Only 27% of UK buyers were fully satisfied and 52% had regrets, often from implementation disruption (search extract; the extract did not show which of the two Capterra UK pages [58][59] holds the figure).
- **Community counter-example (Stack Overflow):** monthly questions fell to early-2009 levels by May 2025 [53]. Another report puts them at 2008 levels, while saying revenue doubled after ChatGPT (low-tier source) [54] (search extract). One analysis in the results dates the slow decline to around June 2020, before ChatGPT, which then sped it up (search extract; the extract did not pin this to [52] or [53]). *Lesson:* a community whose value is answers can be replaced by an LLM. A community whose value is trust and relationships (who to call, who to hire) is not substituted the same way. That second point is inference, not sourced.

### 2. Proprietary or accumulating data
- **a16z's "The Empty Promise of Data Moats" (Casado and Lauten, May 2019)** argues three points (search extract) [23]:
  - most "data network effects" are really scale effects;
  - a data moat's value falls as the dataset grows;
  - the cost of acquiring data tends to *rise* over time, unlike classic network effects.
- **Edge or outcome data is the stronger form.** Greenfield Partners (Sep 2025): "The ability to generate, process, and act on unique data at the edge creates a feedback loop that software alone can't replicate." (search extract) [45]
- **EvenUp (US personal-injury law):**
  - raised a $135m Series D at a valuation of about $1bn (search extract) [85];
  - describes a proprietary model plus human-in-the-loop experts producing demand letters (vendor claim; search extract) [86];
  - aggregator profiles call its moat "hundreds of thousands" of real case outcomes (vendor or aggregator claim; not independently verified).
- *Takeaway:* a customer's own records held in your system are a switching cost, not a data moat. Data counts as a moat only when it consists of outcomes across many customers that improve the product in a way rivals cannot buy. That is inference from [23][45].

### 3. Trust and brand in regulated niches
- **Mistakes are costly here.** One essay argues that moats still compound where mistakes are expensive, ground truth arrives late and several stakeholders define "correct". It adds that AI makes shipping cheaper but does not make institutions move faster (search extract) [3].
- **[UK] FSB (904 owners, fieldwork Nov 2025):**
  - AI use rose to 55% (from 20% in 2023);
  - 92% are worried about AI risks (from 73%);
  - concerns: inaccurate outputs, security, IP misuse, opaque training data and legal liability (search extract) [74][75].
- **[UK/IE] team.blue survey:** nearly half of small businesses trust AI less than work led by people (search extract) [76].
- **[UK] DSIT report:** one in six businesses use AI, most have no active plans to adopt it, and the concerns are data security and accuracy (search extract) [77].
- **EY (400 European software CTOs):** 46% see defensible moats *reinforced* by AI in workflow, integration, compliance and trust (search extract) [1].
- *Takeaway:* for SMB buyers in regulated work, an accountable named provider with human sign-off, and ideally professional indemnity cover, is something they value and a clone cannot offer on day one. The step from survey to moat is inference.

### 4. Regulatory know-how and compliance as a moat
- **[UK] Making Tax Digital for Income Tax:**
  - went live on 6 April 2026 (search extract) [42], for qualifying income over £50k, with £30–50k joining in April 2027 (search extract) [90];
  - HMRC's list for landlords' UK property income names **128 products**, and one in three cannot yet file a full return (search extract) [41];
  - HMRC does not recommend any product (search extract) [43].
  - *Lesson:* a regulation creates a trigger and a must-have category, but being on the official list is not a moat. Full-scope compliance know-how (being among the two-thirds that can file a full return) is the differentiator.
- **[UK] Gas-safety (CP12) certificates are a crowded category.**
  - A UK plumbing-software guide lists several products with digital CP12s: Gas Engineer Software, and Tradify, which also notifies the Gas Safe Register. It notes Jobber and YourTradebase lack certificates (search extract) [69].
  - A vendor blog gives £25–45/month as typical for job-management software (vendor claim; search extract) [70].
  - Verified prices for named CP12 apps were **not found**.
  - Simple compliance-form generation is a feature, not a moat.
- **"Compliance as moat" essays:** the search returned mostly low-quality, promotional blogs. **No rigorous essay or study was found**, and the counter-argument (that model vendors and incumbents clear the same rules) was absent from the results.

### 5. Hardware plus service bundles
- **Carlsquare (Oct 2025):** hybrid hardware-plus-software models offer the "best of both worlds". Barriers include supply chain, manufacturing know-how, certification and logistics (search extract) [44].
- **Oregon Venture Fund:** durable application-layer moats come from what AI cannot generate, namely regulated market access, embedded distribution and operational depth (search extract) [46].
- **VC Cafe:** AI's effect on software is pushing VCs "from bits to atoms", though the shift is not immediate (search extract) [47].
- **Checkit [UK, AIM-listed, automated monitoring platform]:**
  - FY25 (to 31 Jan 2025): ARR up 8% to £14.4m, revenue up 17% to £14.1m, non-recurring revenue only 6% (search extract) [71];
  - H1 FY26: still loss-making, with adjusted LBITDA improved 65% to £0.5m (search extract) [72];
  - FY26: revenue £13.7m (−2%), ARR £14.3m (−1%) (search extract) [73].
  - *Lesson:* sensors plus service gave very recurring revenue but did not, by itself, produce growth or profit. This matches the v1 finding that the channel matters more than the device.

### 6. Switching costs, workflow lock-in and systems of record
- **Vertical market software (Constellation Software, CSU):**
  - commentary attributes its durability to "long-lived customer relationships, high switching costs, and untapped pricing power" (search extract) [13];
  - software is a small cost next to operations, so switching saves little while the operational risk of switching is high (search extract) [14];
  - the risk concentrates at the top end and in less critical niches (search extract) [15];
  - management says folding AI into customers' existing systems *raises* switching costs (secondary; search extract) [12];
  - CSU held an AI-impact call in Sept 2025 [11] and announced a leadership change from Mark Leonard to Mark Miller [10] (search extract).
- **SMB lock-in is weak by default:**
  - SMB SaaS churn is 3–7% a month, or 30–58% a year (Vena; search extract) [36];
  - a 2026 cohort study puts SMB churn at 6.2% a month against 0.7% for enterprise (search extract) [37].
- **Embedded payments deepen lock-in.** A Matrix Partners interview frames embedded fintech as "the main way vertical SaaS companies defend their economics" (search extract) [16]. ServiceTitan is described as the system of record across dispatch, scheduling, estimates, invoices and payments (vendor case study; search extract) [18]. Toast's revenue is reported as about 80% financial services (search extract; single-blog figures, unverified) [17].
- **Agents and systems of record:** Jamin Ball argues agents "are not replacing systems of record. They are raising the standards for how they're read and written" (search extract) [78]. In a later piece he suggests "clearinghouses" for agents may be the next moat [79]. Low-tier results argued the opposite, that agents reach data over APIs or MCP and so erode workflow lock-in. Those claims were not pinned to a URL and are not counted.

### 7. Network effects
- **NFX:** "network effects are responsible for 70% of the value created by tech companies since … 1994" (search extract) [60]. The study covered 336 companies valued over $1bn, founded 1994–2017. The rest relied on embedding, scale and brand (search extract) [60][61]. *Caveat:* the sample is billion-dollar companies from before the AI wave, and **no AI-era revision was found**.
- **Rightmove [UK]:**
  - it reaffirmed a 70% underlying operating margin for 2025 (search extract) [51];
  - RBC argued that estate agents will keep paying and homebuyers will keep looking (search extract) [50];
  - shares still fell about 12–13% at the close (up to about 28% intraday) on 7 Nov 2025 when AI spending was announced (search extract) [48];
  - consensus 2028 margin moved from 70.5% to an implied 67.4% (search extract) [49].
  - *Lesson:* even a strong network effect must pay to defend itself against AI search. A solo founder cannot build this within 90 days.

### 8. Services-led businesses
- **General Catalyst** calls this the "AI-enabled roll-up": buying service businesses and automating them, which it believes could eclipse the SaaS wave (search extract) [31]. Coverage describes a $1.5bn fund with about half earmarked for this [32]. The margin logic, as reported, is to move from 5–10% EBITDA towards 30–40% (search extract; figure seen in the results for [32] but not pinned to one page).
- **Example deal:** Titan ($74m) acquired RFA, an IT managed service provider with 400+ financial-services clients (search extract) [35].
- **Critiques:** Fortune argues the services-to-software multiple gap "exists for a reason" [33]. TechCrunch: "the AI services transformation may be harder than VCs think" [34] (search extract).
- **Bessemer:** vertical AI competes for labour budgets (about 13% of US GDP) rather than IT budgets (about 1%). Its 2024 framing lists Copilots, Agents and AI-enabled Services as business models (search extract; secondary summaries of [66][67]).
- *Takeaway:* a service sold on outcomes, with AI doing the work and a person accountable, captures labour budgets and inherits the trust moat (§3). The cost is lower margins and multiples.

### 9. Vertical SaaS defensibility
- **Domain-insider founders.** BoomCloud is bootstrapped dental-membership software whose founder came from the family dental-lab business. It reports about $3M ARR, about 600 practices and 11 staff (founder-reported; search extract) [68]. A separate essay argues that encoding specialised domain knowledge remains hard, so vertical software keeps its edge (search extract) [87].
- **Vertical software with no moat beyond its features gets competed away.** A SaaS-founder publication notes a competitor can copy a feature in a week and customers may build it themselves (search extract) [4]. An Indie Hackers post argues "vibe coding is quietly killing simple SaaS products". In its view, the defensible part is "the boring layer" (search extract) [40].
- **Permanence over moats.** SignalFire argues AI startups should optimise for permanence: surviving successive waves of model progress (search extract) [88].

## How AI changes software defensibility
1. **Building is no longer the bottleneck.**
   - YC (Mar 2025): about a quarter of the W25 batch had 95% AI-written code, and the batch grew 10% a week in aggregate (search extract) [38].
   - Cloudflare's vinext: one engineer and about $1,100 in tokens (company claim), backed by 1,700+ Vitest and 380 Playwright tests, but experimental (search extract) [64][65].
   - The founder of Base44, sold to Wix for over $80m: "it's relatively easy to create a vibe coding tool" (search extract) [39].
2. **Buyers are building instead of buying.**
   - Retool's 2026 report (817 Retool customers, so a biased sample) found (vendor survey; search extract) [55]:
     - 35% replaced at least one SaaS tool;
     - 78% plan to build more;
     - 60% built tools outside IT oversight;
     - the top targets were workflow automations (35%), admin tools (33%) and BI (29%).
   - The Cruxy survey of 300 UK/US SaaS CEOs found (vendor survey; search extract) [83][84]:
     - 85% see AI as a threat to their business model;
     - 82% have had customers request AI-related price cuts;
     - 54% fear customers building their own tools, against 45% who fear AI-native startups.
3. **Public markets repriced "seat" software.**
   - Bloomberg covered the Feb 2026 "SaaSpocalypse" [5]. Headlines put it at about $285bn after the Claude Cowork release [7], and The Batch reports a slight rebound on partnerships [6] (search extract).
   - The fear was "seat compression": agents need fewer human seats. A dissent calls the sell-off a pricing error rather than extinction [8] (search extract).
   - Constellation's halving was attributed partly to AI uncertainty (search extract) [9].
4. **AI-native margins are thinner and depend on a platform.**
   - Bessemer (Aug 2025) reportedly found Supernovas at about 25% gross margin (often negative) against about 60% for Shooting Stars, with inference costs blamed (secondary; search extract) [24][25].
   - Windsurf: "With less than five days of notice, Anthropic decided to cut off nearly all of our first-party capacity to all Claude 3.x models." (search extract) [62][63]
5. **Commoditisation cases:**
   - Jasper cut its internal valuation by about 20% after a $1.5bn round, with ChatGPT "effectively a direct competitor" [26], and laid off staff 9 months after a $125m raise [27];
   - Chegg cut 22% of staff (248 people) in May 2025 [28]. Q1 2025 revenue fell about 30% and subscribers fell to 3.2m (−31%) [29]. Chegg blamed Google AI Overviews for keeping traffic within Google (search extract; across [28][29][30]).
6. **What sources say survives:**
   - integrations and everything around the product [2];
   - workflow, integration, compliance and trust [1];
   - contested-correctness domains [3];
   - switching costs in mission-critical niches [13][14];
   - distribution [22];
   - physical operations [44][46].
   All of this comes as opinion or vendor-run surveys, not causal studies.

## Named examples
| Company | Niche / size | Outcome | Why (moat or none) | Sources |
|---|---|---|---|---|
| Xero | SMB accounting (ANZ/UK) | Defended growth through channel | Accountants and bookkeepers bring about 70% of new customers (2013) | [19][20][21] |
| FreeAgent [UK] | Freelancer/SMB accounting | Bundled free by NatWest group | Bank already serves the buyer; free licence for account holders | [80][81][82] |
| Rightmove [UK] | Property portal | 70% margin, but shares hit on AI capex | Two-sided network effect; agents keep paying | [48]–[51] |
| Constellation Software | Hundreds of small VMS businesses | Shares roughly halved; business still growing per bulls | Switching costs, mission-critical; risk in less critical niches | [9][12]–[15] |
| ServiceTitan / Toast | Trades / restaurants vertical SaaS | Fintech is the main revenue line | System of record plus embedded payments | [16]–[18] |
| BoomCloud | Dental membership plans (bootstrapped) | About $3M ARR, about 600 practices (founder-reported) | Domain-insider founder, niche workflow | [68] |
| EvenUp | US personal-injury law | About $1bn valuation | Outcome data plus human-in-the-loop service (vendor claim) | [85][86] |
| Checkit [UK] | Sensor monitoring, AIM | Very recurring (94%) but flat ARR, loss-making | Hardware plus service sticky; growth not solved | [71]–[73] |
| Jasper | AI copywriting | Valuation cut, layoffs | Thin layer over a model whose owner competed | [26][27] |
| Chegg | Homework help | −31% subscribers, −22% staff | Content replaced by LLMs; traffic captured by AI Overviews | [28]–[30] |
| Stack Overflow | Developer Q&A community | Questions back to 2008–09 levels | Community value (answers) substituted by LLMs | [52]–[54] |
| Windsurf | AI coding IDE | Lost first-party Claude capacity at under 5 days' notice | Single upstream-model dependency | [62][63] |
| MTD software [UK] | Landlord/sole-trader tax filing | 128 listed products | Regulatory listing shared by many; not a moat | [41][43] |
| CP12 certificate apps [UK] | Gas engineers | Several products offer the same forms | Simple compliance forms are a feature | [69][70] |

Most of the defensible examples are not small. The small or niche examples with sources are BoomCloud, Checkit and the CP12/MTD categories. Examples with figures for **small** companies that stayed defensible were scarce in the results.

## Searched for but not found
- A primary Bessemer *State of AI 2025* page. Margin figures come only from secondary summaries [24][25].
- The primary a16z source for the claim that "fintech adds 2–5× revenue per customer" in vertical SaaS (seen only second-hand). A primary filing for the Toast or ServiceTitan revenue mix.
- Foundation Capital's "service-as-software" thesis (no result).
- Any rigorous study showing distribution predicts AI-era startup success.
- A verified Reddit or forum thread documenting an indie SaaS cloned within days. Cloning-speed claims are opinion pieces.
- An SMB-specific survey on AI-driven price cuts or competition from AI-native rivals.
- Multi-decade retention data for niche vertical software. Church or dental-lab software examples.
- An AI-era revision of NFX's 70% network-effect figure.
- A rigorous essay on "compliance as a moat" for SMB software, or the counter-argument.
- A transcript of Constellation's Sept 2025 AI call (only secondary write-ups).
- A FreeAgent user count from the bank channel. Verified prices for named CP12 apps.
- A Sequoia or Battery essay on systems of record versus agents. a16z's "Is Software Losing Its Head?" appeared only via a mirror and is not cited.
- Tome's pivot. Primary data for the "about 3,800 AI startup shutdowns in 2025" figure (attributed to SimpleClosure via secondary blogs; not used).
- Chegg's reported Oct 2025 cut of 388 roles (an aggregator citing Reuters; not verified; not used).
- Low-tier claims whose source URL could not be pinned and that were therefore dropped:
  - "labour savings competed away to near-zero margin";
  - "support is a feature, not a moat";
  - "you can copy features, not community";
  - "a clone of a $10M SaaS in two hours";
  - Andrew Wilkinson's funeral-home software analogy;
  - FrontRunner's $400–900/location price.

## Queries run
1. software moats when code is cheap AI coding defensibility essay 2025
2. SaaSpocalypse February 2026 software stocks sell-off AI agents Anthropic plugins
3. Constellation Software vertical market software AI disruption fears share price 2025 Mark Leonard
4. Constellation Software AI conference call September 2025 mission critical customers switching costs vertical market software what protects
5. vertical SaaS embedded payments moat Toast ServiceTitan Mindbody fintech revenue multiple of software revenue
6. Xero accountants and bookkeepers partner channel share of new subscribers small business distribution
7. "distribution is the moat" AI era startups 2025 software abundant attention scarce
8. a16z "empty promise of data moats" data network effects diminishing returns
9. Bessemer State of AI 2025 supernovas shooting stars gross margin 25% 60% inference costs
10. Jasper AI cut internal valuation layoffs ChatGPT commoditized AI copywriting wrapper
11. Chegg layoffs 2025 subscribers decline Google AI Overviews ChatGPT traffic
12. "service-as-software" OR "services as software" AI-enabled services roll-up General Catalyst Foundation Capital 2025 thesis
13. SMB SaaS churn benchmark monthly churn small business customers vs enterprise net revenue retention 2025 report
14. Y Combinator Winter 2025 batch 25% startups 95% of code AI-generated Garry Tan
15. indie hacker SaaS cloned by competitor in days vibe coding copycat 2025 reddit
16. compliance as a moat regulated industries vertical software AI startups trust liability 2025 essay healthcare legal insurance
17. HMRC Making Tax Digital income tax April 2026 recognised software list software suppliers number of products
18. hardware-enabled software defensibility AI can't copy atoms installation service moat 2025 venture essay
19. Rightmove shares fall AI investment November 2025 estate agents network effect operating margin
20. Stack Overflow questions decline 2025 ChatGPT monthly questions back to 2009 levels
21. Retool build vs buy report 2026 companies replacing SaaS with custom AI-built internal tools survey percent
22. Capterra 2025 tech trends small business software buying peer recommendations reviews trusted sources purchase regret survey
23. NFX network effects 70% of value created in tech since 1994 network effects manual AI era
24. Windsurf Anthropic cut Claude model access June 2025 platform risk AI coding startup
25. Cloudflare rebuilt Next.js one week AI $1,100 tokens vinext engineer Claude
26. Bessemer vertical AI roadmap labor spend services budgets defensibility vertical AI moats 2024 2025
27. bootstrapped niche vertical software company example funeral home OR church OR dental lab software sticky customers decades retention why defensible
28. gas safety certificate app CP12 software price per month UK engineers comparison cheap
29. Checkit plc results 2025 annual recurring revenue food safety monitoring sensors losses
30. UK small businesses AI adoption barriers survey 2025 trust accuracy data security FSB OR "British Chambers of Commerce"
31. systems of record survive AI agents moat essay 2025 Sequoia OR a16z OR Battery switching costs data gravity
32. AI startups shut down 2025 feature absorbed by ChatGPT OpenAI "wrapper" examples Tome pivot named companies
33. FreeAgent free for NatWest RBS Mettle business customers number of users distribution bank partnership
34. SaaS pricing pressure AI 2026 price cuts small business software cheaper AI-native competitors seat compression evidence survey
35. EvenUp personal injury demand letters proprietary data claims moat human-in-the-loop services AI valuation

## Sources
1. [OTHER] https://www.ey.com/content/dam/ey-unified-site/ey-com/en-nl/services/strategy/documents/ey-beyond-the-code-how-ai-is-redefining-the-software-industry-2026.pdf — EY, "Beyond the code: how AI is redefining the software industry", 2026
2. [OTHER] https://stroupaloop.com/blog/2026/04/12/when-code-gets-cheap-scarcity-moves/ — Stroupaloop, "When code gets cheap, scarcity moves", 12 Apr 2026
3. [OTHER] https://nibzard.com/meat-moat — nibzard essay on moats where correctness is contested
4. [OTHER] https://www.saasrise.com/blog/your-moat-when-engineering-gets-cheap — SaaSRise, "Your moat when engineering gets cheap"
5. [OTHER] https://www.bloomberg.com/news/articles/2026-02-04/what-s-behind-the-saaspocalypse-plunge-in-software-stocks — Bloomberg, 4 Feb 2026 (text not retrieved; title only)
6. [OTHER] https://www.deeplearning.ai/the-batch/claude-cowork-plugins-trigger-a-saas-stock-selloff-but-partnerships-lead-to-slight-rebound — DeepLearning.AI, The Batch, 2026
7. [OTHER] https://business.mammothtimes.com/mammothtimes/article/marketminute-2026-2-6-anthropics-claude-cowork-release-triggers-285-billion-saaspocalypse-a-brutal-wake-up-call-for-legacy-tech-and-finance — MarketMinute syndication, 6 Feb 2026 (low-tier)
8. [OTHER] https://philippdubach.com/posts/the-saaspocalypse-paradox/ — Philipp Dubach, "The SaaSpocalypse paradox", 2026
9. [OTHER] https://www.fool.ca/2026/09/16/the-market-has-punished-this-stock-enough-id-buy-before-sentiment-turns/ — Motley Fool Canada, 16 Sep 2026
10. [OTHER] https://www.globenewswire.com/news-release/2025/09/26/3157269/0/en/Constellation-Software-Inc-Announces-Conference-Call.html — Constellation Software via GlobeNewswire, 26 Sep 2025
11. [OTHER] https://www.csisoftware.com/category/webcasts/2025/09/23/conference-call-to-discuss-ai-s-impact-on-software-businesses — Constellation Software webcast page, 23 Sep 2025
12. [OTHER] https://www.5iresearch.ca/blog/constellation-software-update-on-artificial-intelligence-ai-and-what-investors-should-know — 5i Research, 2025
13. [OTHER] https://conference.investor.fm/constellation-software-inc/ — investor.fm conference summary (secondary)
14. [OTHER] https://theglobeandmail.com/investing/investment-ideas/article-constellation-ai-threat-software-stocks — The Globe and Mail, 2025/26
15. [OTHER] https://allmind.ai/news/3266d5f31207bb171d8205beca5a094b52f4b4f579b5b16c4224be1decb9523d — AllMind news summary (low-tier)
16. [OTHER] https://sacra.com/chat/h/b5d654b8-61bd-4134-b961-cfdd7bc6040b/ — Sacra, "Embedded fintech becomes vertical SaaS moat" (Matrix Partners interview)
17. [OTHER] https://www.paymentsjournal.com/vertical-saas-is-cashing-in-on-payments/ — PaymentsJournal, "Vertical SaaS is cashing in on payments"
18. [OTHER] https://payabli.com/how-servicetitan-drove-unprecedented-customer-adoption-and-growth-with-embedded-payments/ — Payabli (vendor case study)
19. [OTHER] https://www.techpartner.news/news/xero-accountants-are-the-new-channel-355262 — TechPartner News, "Xero: accountants are the new channel", 2013
20. [OTHER] https://www.techpartner.news/news/cloud-sales-surging-as-accountants-turn-resellers-381817 — TechPartner News, 2013
21. [OTHER] https://www.xero.com/nz/try-now/partner-programme — Xero partner programme page
22. [OTHER] https://techcrunch.com/2026/01/08/gtmfund-has-rewritten-the-distribution-playbook-for-the-ai-era/ — TechCrunch, 8 Jan 2026
23. [OTHER] https://a16z.com/2019/05/09/data-network-effects-moats/ — a16z, "The Empty Promise of Data Moats", 9 May 2019
24. [OTHER] https://confluencevcweekly.beehiiv.com/p/negative-gross-margins — Confluence VC Weekly, "negative gross margins, supernovas, and the end of pricing power", 2025 (secondary on Bessemer)
25. [OTHER] https://tldr.tech/ai/2025-08-18 — TLDR AI newsletter, 18 Aug 2025 (secondary on Bessemer)
26. [OTHER] https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/ — Maginative, 2023
27. [OTHER] https://voicebot.ai/2023/07/17/jasper-ai-laying-off-staff-9-months-after-125m-raise/ — Voicebot.ai, 17 Jul 2023
28. [OTHER] https://www.thestar.com.my/tech/tech-news/2025/05/12/chegg-to-lay-off-22-of-workforce-as-ai-tools-shake-up-edtech-industry — The Star (wire), 12 May 2025
29. [OTHER] https://www.edtechinnovationhub.com/news/chegg-q1-2025-revenue-down-30-as-company-restructures-and-explores-strategic-alternatives — EdTech Innovation Hub, May 2025
30. [OTHER] https://www.techradar.com/pro/chegg-announces-move-to-reduce-workforce-by-22-percent-as-students-turn-to-ai — TechRadar, May 2025
31. [OTHER] https://www.generalcatalyst.com/stories/the-future-of-services — General Catalyst, "The future of services"
32. [OTHER] https://capitalandclarity.substack.com/p/the-general-catalyst-behind-15-billion — Capital & Clarity, "The General Catalyst behind $1.5 billion of AI roll-ups"
33. [OTHER] https://dc.fortune.com/2025/06/27/ai-rollup-investment-strategy — Fortune, 27 Jun 2025
34. [OTHER] https://techcrunch.com/2025/09/28/the-ai-services-transformation-may-be-harder-than-vcs-think/ — TechCrunch, 28 Sep 2025
35. [OTHER] https://www.privateequitywire.co.uk/general-catalyst-backs-ai-driven-it-services-platform-titan-with-74m-investment/ — Private Equity Wire, 2025
36. [OTHER] https://www.venasolutions.com/blog/saas-churn-rate — Vena Solutions, SaaS churn benchmarks 2025
37. [OTHER] https://visionary-marketing.co.uk/blog/saas-churn-benchmarks-2026 — Visionary Marketing, SaaS cohort study 2026
38. [OTHER] https://www.nbcnewyork.com/news/business/money-report/y-combinator-startups-are-fastest-growing-most-profitable-in-fund-history-because-of-ai/6188199/ — CNBC via NBC New York, Mar 2025
39. [OTHER] https://www.aol.com/articles/vibe-coding-startups-face-big-060944200.html — Business Insider via AOL, 2025
40. [S6] https://www.indiehackers.com/post/vibe-coding-is-quietly-killing-simple-saas-products-the-thing-thats-actually-defensible-isn-t-a-feature-it-s-the-boring-layer-3a785dadf1 — Indie Hackers forum post
41. [S3] https://thenegotiator.co.uk/news/products-services-news/third-of-making-tax-digital-software-still-cant-provide-full-returns/ — The Negotiator (UK), 2026
42. [S3] https://www.gov.uk/government/publications/edition-1-making-tax-digital-for-income-tax-software-developer-newsletter/edition-1-making-tax-digital-for-income-tax-software-developer-newsletter — GOV.UK/HMRC developer newsletter
43. [S3] https://www.gov.uk/guidance/choose-the-right-software-for-making-tax-digital-for-income-tax — GOV.UK guidance
44. [OTHER] https://carlsquare.com/insights/softwares-crown-is-at-risk-hardware-is-king-again/ — Carlsquare, Oct 2025
45. [OTHER] https://greenfield-growth.com/knowledge/bits-and-atoms-why-full-stack-ai-is-one-of-the-next-great-venture-opportunities/ — Greenfield Partners, Sep 2025
46. [OTHER] https://www.oregonventurefund.com/perspectives/defensibility-in-the-age-of-ai — Oregon Venture Fund
47. [OTHER] https://www.vccafe.com/how-ais-impact-on-software-is-pushing-vcs-from-bits-to-atoms/ — VC Cafe, 2026
48. [OTHER] https://www.computing.co.uk/news/2025/rightmove-shares-tumble-ai-plans-rattle-investors — Computing (UK), Nov 2025
49. [OTHER] https://www.investing.com/news/earnings/rightmove-shares-crashes-over-25-after-2026-profit-forecast-cut-on-higher-ai-cost-4341271 — Investing.com, 7 Nov 2025
50. [OTHER] https://www.hl.co.uk/shares/stock-market-news/share-tips/stockbroker-tips/rbc-capital-upgrades-rightmove,-says-share-price-slump-was-an-over-reaction — Hargreaves Lansdown broker tips, Nov 2025
51. [OTHER] https://companyresearch.digitallook.com/news/35479817/Rightmove_to_ramp_up_AI_investment_reiterates_outlook.html?ac=209933 — Sharecast via Digital Look, Nov 2025
52. [OTHER] https://newsletter.pragmaticengineer.com/p/are-llms-making-stackoverflow-irrelevant — The Pragmatic Engineer
53. [OTHER] https://www.webpronews.com/stack-overflows-ai-driven-decline-from-peak-to-2009-levels — WebProNews, 2025
54. [OTHER] https://news.lavx.hu/article/stack-overflow-s-paradox-question-volume-plummets-to-2008-levels-while-revenue-doubles-post-chatgpt — LAVX News (low-tier)
55. [OTHER] https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software — Retool via Business Wire, 17 Feb 2026 (vendor survey)
56. [OTHER] https://businesswire.com/news/home/20241119695741/en/Businesses-Set-to-Increase-Software-Spending-in-2025-Despite-High-Levels-of-Purchase-Regret — Capterra via Business Wire, 19 Nov 2024
57. [OTHER] https://www.capterra.ca/blog/7228/tech-trends-canada-shortlisting-the-right-software-products-and-vendors — Capterra Canada
58. [OTHER] https://www.capterra.co.uk/blog/7673/software-buying-trends-uk-successful-adopters — Capterra UK
59. [OTHER] https://www.capterra.co.uk/blog/7557/uk-software-buying-trends-2025-research — Capterra UK
60. [OTHER] https://www.nfx.com/post/70-percent-value-network-effects — NFX, "70% of value in tech is driven by network effects"
61. [OTHER] https://www.nfx.com/post/network-effects-manual/ — NFX, "The Network Effects Manual"
62. [OTHER] https://the-decoder.com/anthropic-cuts-claude-access-for-windsurf-after-openais-3b-takeover-news/ — The Decoder, Jun 2025
63. [OTHER] https://www.techzine.eu/news/devops/131987/windsurf-acquired-by-openai-gets-the-cold-shoulder-from-anthropic — Techzine, Jun 2025
64. [OTHER] https://blog.cloudflare.com/vinext — Cloudflare blog, "How we rebuilt Next.js with AI in one week", 24 Feb 2026 (company claim)
65. [OTHER] https://blog.pragmaticengineer.com/the-pulse-cloudflare-rewrites-next-js-as-ai-rewrites-commercial-open-source/ — The Pragmatic Engineer, 2026
66. [OTHER] https://www.bvp.com/assets/uploads/2026/01/BUILDING-VERTICAL-AI_PDF_BESSEMER_VENTURE_PARTNERS_BOOK_JANUARY_2026.pdf — Bessemer Venture Partners, "Building Vertical AI", Jan 2026
67. [OTHER] https://rosetta.to/u/bessemerventurepartners/vertical-ai-shows-potential-to-dwarf-legacy-saas-state-of-the-cloud-2024 — Bessemer, State of the Cloud 2024 (vertical AI)
68. [OTHER] https://www.indiehackers.com/product/boomcloud — Indie Hackers product page, BoomCloud (founder-reported)
69. [OTHER] https://whito.co.uk/plumbers/tools/best-software-for-uk-plumbers/ — Whito, "Best software for UK plumbers"
70. [OTHER] https://www.trade2base.com/blog/gas-engineer-pricing-uk — Trade2Base blog, May 2026 (vendor)
71. [OTHER] https://www.investegate.co.uk/announcement/rns/checkit--ckt/final-results/8843078 — Checkit plc RNS, Final Results FY25
72. [OTHER] https://www.investegate.co.uk/announcement/rns/checkit--ckt/interim-results/9071340 — Checkit plc RNS, Interim Results H1 FY26
73. [OTHER] https://www.lse.co.uk/rns/fy26-trading-update-rqobyiwyo7u2p1i.html — Checkit plc RNS, FY26 trading update
74. [OTHER] https://www.resultsense.com/news/2026-06-23-fsb-ai-trust-gap-42bn/ — ResultSense on FSB research, 23 Jun 2026
75. [OTHER] https://businessmk.co.uk/articles/ai/trust-gap-threatens-42bn-ai-adoption-opportunity-fsb-says/ — Business MK on FSB research, 2026
76. [OTHER] https://itbrief.co.uk/story/small-businesses-in-uk-ireland-face-barriers-to-ai-adoption — IT Brief UK (team.blue survey)
77. [OTHER] https://assets.publishing.service.gov.uk/media/6960f3924343a0da370869ba/AI_Adoption_Research_Report.pdf — DSIT, "AI Adoption Research Report"
78. [OTHER] https://cloudedjudgement.substack.com/p/clouded-judgement-121225-long-live — Clouded Judgement (Jamin Ball), 12 Dec 2025
79. [OTHER] https://cloudedjudgement.substack.com/p/systems-of-record-won-the-saas-era — Clouded Judgement (Jamin Ball)
80. [OTHER] https://www.freeagent.com/pricing/free-accounting-software/ — FreeAgent, "Get FreeAgent for free"
81. [OTHER] https://www.freeagent.com/accountants/try/natwest-rbs-free-licences/ — FreeAgent accountant page
82. [OTHER] https://www.rbs.com/rbs/news/2020/04/mettle-by-natwest-offers-freeagent-free-of-charge.html — NatWest Group news, Apr 2020
83. [OTHER] https://cfotech.co.uk/story/saas-chiefs-expect-pricing-shift-as-ai-threatens-sales — CFOtech UK (Cruxy survey; vendor survey)
84. [OTHER] https://securitybrief.co.uk/story/saas-chiefs-expect-pricing-shift-as-ai-threatens-sales — SecurityBrief UK (Cruxy survey; vendor survey)
85. [OTHER] https://legaltechnology.com/evenup-raises-135m-series-d-valuing-the-personal-injury-startup-at-1bn/ — Legal IT Insider
86. [OTHER] https://pulse2.com/evenup-135-million-series-d-raised-at-over-1-billion-valuation-and-new-products-launched — Pulse 2.0 (company announcement coverage)
87. [OTHER] https://dev.to/keithjmackay/software-moats-in-the-age-of-ai-whats-actually-defensible-nnn — DEV Community essay
88. [OTHER] https://signalfire.com/blog/why-ai-startups-should-optimize-for-permanence-not-moats — SignalFire
89. [OTHER] https://capterra.com/resources/tech-trends-smb-enterprise-software-purchase-tips/ — Capterra, 2025 Tech Trends: SMBs vs enterprises
90. [S3] https://www.which.co.uk/money/tax/income-tax/making-tax-digital-mtd-for-income-tax-aboJ39E1tbWw — Which?, Making Tax Digital for income tax

## Implications for the v2 rubric
**W9 Defensibility anchors**
- **0:** the value is features, forms or a prompt over a third-party model. The buyer could build it (35% have replaced a SaaS tool [55]), or an incumbent they already pay for could bundle it free (FreeAgent via the bank [80]). Includes certificate generation [69] and "being on the official list" (128 MTD products [41]).
- **5:** one real non-code asset that is still early: a named channel partner, OR system-of-record status for records the buyer is legally required to keep, OR a physical install. Switching costs alone stay at 5, because SMB churn is 3–7% a month [36].
- **10:** two or more compounding assets, for example:
  - a channel owned by someone already serving the buyer (accountant, bank, insurer) [19][80];
  - money flows or regulated records in the product [16];
  - outcome data or a physical service clones cannot copy [45][85];
  - a mission-critical job where failure costs far more than the price [14][3].

**W6 Reachability**
- Score highest when a named intermediary already visits the buyer: Xero got about 70% of new customers via accountants [19]. SMBs shortlist on reputation and peers [57].
- Credit a founder from inside the sector [68].
- Score lower for search- or content-only plans; AI answers absorb that traffic [30].

**W7 Buildable**
- Give no credit for "easy to build", because everyone can now build [38][64].
- Score whether the *non-code* asset (first partner, first installs, human sign-off) can start within 90 days.
- Require gross margin after inference costs (Supernovas: about 25% [24]) and the ability to switch model providers.

**Knockouts / red flags**
- **K-wrapper:** core value sits on one model provider that could cut access or compete [62][26].
- **K-bundle:** a tool the buyer already pays for, or their bank, gives it away free or could do so [80].
- **Red flags:**
  - per-seat pricing where AI shrinks seats [5][83];
  - AI outputs carrying liability with no accountable human; 92% of UK small firms fear AI risks [74];
  - claiming a compliance listing or hardware alone as the moat (Checkit's ARR is flat) [73].
