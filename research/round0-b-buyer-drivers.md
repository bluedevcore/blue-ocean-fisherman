# Round 0 (b) — What makes B2B buyers actually pay for monitoring / sensor products

Topic report (not an idea evidence file). Researcher: round-0 subagent (b). Date: 2026-11-05.

**Method / sourcing caveat (important for the critic).** 58 web searches were run (listed under
"Queries run"). Every WebFetch attempt in this session failed with a DNS error (`getaddrinfo
ENOTFOUND` for networkworld.com, fujitsu.com, telecomtv.com, hse.gov.uk, insurance-edge.net — the
session's network allowlist blocks fetching), so per roles/researcher.md every bullet below is
sourced from search-result snippets/summaries that showed the claim, and is marked
"(not fetched — blocked)". Where the search summary did not make clear which of several URLs carried
a figure, the bullet says "attribution uncertain". Vendor figures are labelled "(vendor claim)".
Geography is given as UK / US / EU / AU / global.

## Summary

- Buyers pay most readily when a **rule or insurer already forces a recurring check or record**
  (daily fridge logs, monthly legionella sentinel checks, quarterly fire-door checks, F-gas leak
  checks) so the sensor replaces a labour line that already exists, **and** a single failure has a
  money figure attached (fines up to £600k–£3m for legionella; ~US$95k spoiled stock; £105k from
  25 broken vaccine fridges in one region).
- **Payback expectations are short.** ~two-thirds of enterprises expect IoT ROI within 12 months
  (Omdia 2022); UK SMEs say they act on <2-year paybacks (DECC 2014). A vendor's own labour-only
  case for c-store fridge monitoring gives a 2.6-year payback — i.e. labour savings alone are
  marginal; avoided loss/compliance must carry the case.
- **Insurance-driven buying is real but mostly home/US.** Free devices: Hiscox and Covéa (LeakBot,
  UK home/HNW), State Farm (Ting, >1m US homes). Commercial: Chubb premium credits, HSB/Munich Re
  sensors leased (~US$200/yr) or free via partner insurers (Nationwide). UK commercial insurers
  mostly offer "preferential rates" via specialist partners (Aviva) or make monitoring a
  *condition* in niche covers (deterioration of stock, construction escape of water).
- **The payer is operations/compliance, not IT** (Bain: OT key decision-maker in 85% of IoT
  purchases). UK housing compliance managers hold budgets of ~£3.5m+.
- **Deal killers:** IT/security review (6–12 months in a US hospital), long deployments (49% name
  it the top ROI roadblock), PoC stall (30% Microsoft 2019; 60% Cisco 2017), false alarms/alarm
  fatigue, battery/installation labour, and no staff to act on data.
- **Channels that already work:** insurers (LeakBot: 23 carriers; HSB), buying/symbol groups
  (Nisa–Kelsius), service contractors (PTSG water treatment, Danfoss installers, Lowe Rental),
  electrical wholesalers + installers (Aico), IoT distributors (Monnit/Digi-Key).

## Purchase drivers

### 1. ROI and payback expectations

- Omdia IoT Enterprise Survey 2022 (~500 enterprises, nine countries): 67% expected ROI within one
  year of deployment; 49% said long deployment times were the biggest roadblock to ROI; ~48% cited
  supply-chain issues and 42% budgeting (global) — https://www.fiercesensors.com/iot-wireless/enterprise-iot-projects-move-toward-roi-roadblocks-remain (not fetched — blocked)
- Same survey framed as "70% of enterprises expect a 1-year ROI" (headline) — https://www.networkworld.com/article/3674768/iot-survey-70-of-enterprises-expect-a-1-year-roi.html (not fetched — blocked; WebFetch DNS failure)
- RCR Wireless framed the Omdia result as a tension: quick-return expectations vs poor planning and
  long delays (global) — https://www.rcrwireless.com/20220921/carriers/an-iot-conundrum-poor-planning-long-delays-hobble-quick-returns-high-expectations (not fetched — blocked)
- Omdia's own release: "over 90% of enterprises said their IoT projects have met or exceeded
  expectations" (global) — https://omdia.tech.informa.com/pr/2022-jul/new-omdia-research-finds-enterprises-are-turning-to-5g-for-their-iot-needs (not fetched — blocked)
- Fujitsu/IDG 2018: 31% of businesses expect a return from IoT within one to two years; 56% expect
  profitability within three years (EMEIA) — https://www.fujitsu.com/uk/news/pr/2018/fs-20181010.html (not fetched — blocked; WebFetch DNS failure)
- SumatoSoft 2026 study of 36 deployments: median payback 12 months; 72% fully paid back in year
  one (vendor claim; small sample) — https://macaubusiness.com/sumatosoft-reveals-insights-on-iot-roi-median-payback-period-just-12-months/ (not fetched — blocked)
- UK SMEs (DECC 2014, ENWORKS research): interviewees said they would generally act on measures
  paying back in under two years (some extended to five), yet the implementation rate for <2-year
  payback opportunities was only 13% — i.e. short payback is necessary but not sufficient (UK) —
  https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/392908/Barriers_to_Energy_Efficiency_FINAL_2014-12-10.pdf ;
  https://www.gov.uk/government/publications/research-to-assess-the-barriers-and-drivers-to-energy-efficiency-in-small-and-medium-sized-enterprises (not fetched — blocked)
- Same DECC study: when no capital investment was required, implementation still only ~20% —
  removing capex alone doesn't close deals (UK) — https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/392908/Barriers_to_Energy_Efficiency_FINAL_2014-12-10.pdf (not fetched — blocked)
- Kelsius (fridge/freezer monitoring) estimate for a UK convenience store: 3.8 hours/week of manual
  checks saved, worth "at least £2,260" a year at £11.44/h; **average payback 2.6 years** at £13/h
  (vendor claim, reported by trade press) (UK) — https://www.betterretailing.com/exclusive-fridge-monitor-could-save-stores-2000-a-year-according-to-kelsius/ (not fetched — blocked)
- Kelsius–Nisa trial: one store "optimised up to one hour of colleague labour a day, saving £9,000
  in annual costs"; forecast up to £10k/yr per Nisa retailer; fees "from £4 a day"; claimed ROI
  ~150% at 12 months (vendor claim; attribution between these two pages uncertain) (UK) —
  https://www.thegrocer.co.uk/news/nisa-stores-to-save-up-to-10k-a-year-with-food-safety-management-tech/704066.article ;
  https://kelsius.com/2025/05/13/ (not fetched — blocked)
- Microsoft IoT Signals 2019 (3,000+ decision makers): ~30% of projects fail at PoC "often because
  implementation is expensive or bottom-line benefits are unclear" (global) —
  https://news.microsoft.com/source/2019/07/30/microsoft-announces-iot-signals-research-report-on-state-of-iot-adoption/ ;
  https://venturebeat.com/security/microsoft-30-of-iot-projects-fail-in-the-proof-of-concept-stage (not fetched — blocked)

### 2. Compliance-driven purchases

**Legionella (L8 / HSG274, UK)**
- HSE prosecution of Amey Community Ltd (HMP Lincoln, prisoner death): fined £600,000 plus
  £15,186.85 costs on 3 Dec 2024 (UK) — https://press.hse.gov.uk/2024/12/03/company-failed-to-manage-legionella-risk-as-prisoner-dies (not fetched — blocked)
- HSE presentation on the case: "HSG274 guidance states that monthly temperature checks should be
  carried out to validate control"; the company "failed to carry out temperature checks on E Wing"
  in Oct–Nov 2017; sentencing starting point £1.2m, reduced to £900k then £600k (UK) —
  https://www.bohs.org/app/uploads/2025/11/Ceri-Rideout-HSE-Prosecutions_Legionella-2025.pdf (not fetched — blocked)
- BUPA Care Homes (BNH) Ltd fined £3m + £151,482 costs; staff taking water temperature measurements
  had not been trained to the required standard (UK) — https://www.hvpmag.co.uk/BUPA-fined-3m-after-legionella-death-in-nursing-home (not fetched — blocked)

**Food safety (HACCP / FSA, UK)**
- FSA: keeping cold food at 8°C or below is a legal requirement in England, Wales and NI; fridges
  recommended at 5°C or below; check with a fridge thermometer (UK) —
  https://www.food.gov.uk/business-guidance/chilling-food-correctly-in-your-business (not fetched — blocked)
- FSA's Safer Food Better Business packs are the food safety management system for small
  businesses (UK) — https://www.food.gov.uk/business-guidance/safer-food-better-business-sfbb (not fetched — blocked)
- Food Safety Act 1990 s.21 "due diligence" defence: accused must prove they "took all reasonable
  precautions and exercised all due diligence" (UK) — https://www.legislation.gov.uk/ukpga/1990/16/section/21/enacted (not fetched — blocked)

**Pharmacy / vaccine cold chain (UK)**
- GPhC inspection action plan wording: fridge temperature monitoring "must take place on a daily
  basis (preferably at the same time each day)", recording actual/max/min (UK; attribution among
  several GPhC action-plan pages uncertain) — https://inspections.pharmacyregulation.org/pharmacy/action-plan/1117249-2021-07-12-19790 (not fetched — blocked)
- NHS/UKHSA Vaccine Update issue 369 (Feb 2026): reported vaccine wastage in 2025 £6.4m at list
  price, ~84% avoidable; cold-chain failure caused 64% of incidents; power cuts 13% (UK) —
  https://www.gov.uk/government/publications/vaccine-update-issue-369-february-2026/vaccine-update-issue-369-february-2026 (not fetched — blocked)
- Vaccine Update issue 338 (May 2023): 2022 wastage £5.7m; fridge malfunction / fridge left open /
  vaccines left out ≈16% of avoidable wastage (£896k); power cuts ≈ £2.9m (UK) —
  https://www.gov.uk/government/publications/vaccine-update-issue-338-may-2023/vaccine-update-issue-338-may-2023 (not fetched — blocked)
- Vaccine Update issue 378 (Oct 2026): fridge failures "cost the NHS thousands of pounds each year";
  advises ordering only 2–4 weeks' stock (UK) — https://www.gov.uk/government/publications/vaccine-update-issue-378-october-2026/vaccine-update-issue-378-october-2026 (not fetched — blocked)
- NHS England East of England toolkit (2023): "in 2022 vaccine wastage accounted for 5.7 million
  pounds of NHS funds, and 50% of that wastage was due to a cold chain breach" (UK) —
  https://www.england.nhs.uk/wp-content/uploads/sites/47/2023/07/East-of-England-Cold-Chain-Toolkit-2023-V1.pdf (not fetched — blocked)
- Yorkshire Post citing Public Health England: 77 "cold chain" failures reported by GPs in West
  Yorkshire in one year, vaccines wasted at a cost of £191,000; 25 cases where the fridge was not
  working cost £105,000 (≈£4.2k each); £25,000 from fridges switched off in error; £17,500 from
  doors left open (UK; article date not shown in results) —
  https://www.yorkshirepost.co.uk/news/500-children-recalled-jabs-fridge-fails-village-gp-practice-1822563 (not fetched — blocked)
- MHRA GDP inspection deficiency data (2016, 10% sample, major findings): transportation
  deficiencies "mainly deal with temperature control and monitoring" (UK) —
  https://gmp-compliance.org/gmp-news/gdp-deficiency-data-available (not fetched — blocked)

**F-gas (UK/EU)**
- GOV.UK: equipment holding ≥500 tonnes CO2e of F-gas must have a fixed leak detection system;
  500 tCO2e ≈ 127 kg of R404A (UK) — https://www.gov.uk/guidance/checking-f-gas-equipment-for-leaks (not fetched — blocked)
- Leak-check frequency ≥500 tCO2e is every 3 months, relaxed to 6 months with a fixed detector
  (EU/UK) — https://climalife.com/?p=159477 ; Irish EPA table shows the same pattern for the 50–500 t
  band (6 → 12 months) — https://www.epa.ie/publications/compliance--enforcement/air/ods--f-gas/1-IRL-Summary-Guidance-to-Compliance-with-the-ODS-and-F-gas-Regulations-V1.0.pdf (not fetched — blocked)
  → a sensor that *reduces a mandated inspection frequency* is a direct, countable saving.

**Fire safety (UK)**
- Fire Safety (England) Regulations 2022 (from 23 Jan 2023): in multi-occupied residential
  buildings over 11 m, quarterly checks of communal fire doors (incl. self-closers) and
  best-endeavours annual checks of flat entrance doors (UK) —
  https://www.gov.uk/government/publications/fire-safety-england-regulations-2022/fact-sheet-fire-doors-regulation-10 (not fetched — blocked)

**Environmental permits (UK)**
- Environment Agency: permits may require MCERTS-certified equipment; CEMS must be MCERTS
  certified for the permit's continuously monitored measurands (UK) —
  https://www.gov.uk/government/publications/mcerts-for-stack-emissions-monitoring-equipment-at-industrial-installations/mcerts-for-stack-emissions-monitoring-equipment-at-industrial-installations ;
  https://www.gov.uk/government/publications/m20-quality-assurance-of-continuous-emission-monitoring-systems/monitoring-stack-emissions-quality-assurance-of-continuous-monitoring (not fetched — blocked)
  → compliance pull exists but certification is a barrier to a cheap new entrant.

**Damp & mould (Awaab's Law, England social housing)**
- In force 27 Oct 2025 for social landlords; councils describe emergency hazards to be addressed
  within 24 hours (UK) — https://www.lbhf.gov.uk/news/2025/10/tackling-damp-and-mould-keep-residents-safe-home (not fetched — blocked)
- CIH blog: Aico HomeLINK environmental sensors monitor temperature/humidity to "identify the
  conditions that cause condensation, damp and mould" — a shift from reactive repair to prediction
  (UK) — https://www.cih.org/blogs/awaab-s-law-marks-a-turning-point-for-safe-and-healthy-homes/ (not fetched — blocked)

### 3. Insurance-driven purchases

**Free or subsidised devices (insurer pays)**
- Hiscox (UK, 2020): free LeakBot "worth £149" plus free engineer visit for buildings insurance
  customers (UK home) — https://www.hiscox.co.uk/node/5001 (not fetched — blocked)
- Covéa (UK): free LeakBot for HNW customers plus nil escape-of-water excess (subject to previous
  EoW claims) (UK home/HNW) — https://www.coveainsurance.co.uk/brokers/broker-news/covea-insurance-extend-leakbot-as-part-of-core-proposition-for-hnw-portfolio/ (not fetched — blocked)
- LeakBot: "23 insurance carrier partnerships across Europe and USA" (Nationwide, Admiral, Direct
  Line Group, Hiscox, Länsförsäkringar, TopDanmark); "70% reduction in water damage claims cost
  validated" (vendor claim, attributed to Consumer Intelligence) (UK/EU/US) —
  https://leakbot.io/about/our-story/ (not fetched — blocked)
- State Farm + Whisker Labs Ting (US): free to eligible policyholders, no policy discount, $1,000
  remediation credit; expanded to 2 million homes (Apr 2024); >1 million sensors provided by June
  2025; "avoid potential losses over 15,000 times" (insurer claim) (US) —
  https://newsroom.statefarm.com/state-farm-expands-ting-fire-safety-program-to-2-million-homes/ ;
  https://newsroom.statefarm.com/state-farm-offers-customers-more-than-one-million-free-ting-sensors/ ;
  https://www.tingfire.com/statefarm-faqs/ (not fetched — blocked)
- HSB (Munich Re) launched a "low-cost IoT sensor solution for small businesses" (leak/freeze,
  2019, US) — https://munichre.com/hsb/en/press-and-publications/press-releases/2019/2019-09-17-low-cost-small-business-iot-sensor-solution.html (not fetched — blocked)
- Nationwide (US) commercial leak & freeze sensor programme "at no additional cost" to customers —
  https://www.nationwide.com/campaigns/commercial-leak-and-freeze-detection (not fetched — blocked)

**Premium credit / lease (customer pays, insurer rewards)**
- Chubb (US, 2022): an institution (Providence) pays ~$12,000/yr (~$600–700 per building) for
  sensors and receives a premium credit; Chubb had not disclosed the average commercial credit (US;
  attribution between these two articles uncertain) — https://www.insurancejournal.com/news/national/2022/01/31/651005.htm ;
  https://www.claimsjournal.com/news/national/2022/02/08/308536.htm (not fetched — blocked)
- Chubb + Hartford Steam Boiler partnership to deploy IoT sensors "in homes and businesses" (2018,
  US) — https://news.na.chubb.com/2018-10-31-Chubb-Partners-With-Hartford-Steam-Boiler-to-Deploy-Innovative-Internet-of-Things-Sensors-in-Homes-and-Businesses (not fetched — blocked)
- StreamLabs Scout (Chubb subsidiary) "qualifies for a premium credit on many carriers' insurance
  policies" (US) — https://insurancenewsnet.com/oarticle/streamlabs-expands-product-suite-with-scout-a-new-smart-water-sensor (not fetched — blocked)
- HSB (Munich Re) via EMC Insurance: small office locations can lease the sensor equipment "for
  about $200 per year" (US) — https://www.emcinsurance.com/losscontrol/vendors/sensor-solutions (not fetched — blocked)
- Zurich UK + Cocoon: discounted device and 10% off Zurich home insurance (UK home) —
  https://www.insurancetimes.co.uk/zurich-teams-up-with-smart-tech-company/1419257.article (not fetched — blocked)
- Plant theft (UK): Norwich Union (2004) premium discounts up to 45% on engineering insurance for
  protected plant — https://www.aviva.com/newsroom/news-releases/2004/05/uk-thiefbeating-security-system-offers-lifeline-1746 ;
  Tracker + Datatag (2011): "many leading insurers ... offering insurance premium discounts of up to
  25%" for CESAR + Tracker — https://www.fleetnews.co.uk/news/2011/6/9/tracker-and-datatag-announce-security-partnership/39779/ ;
  JCB Insurance Plantmaster 15% discount for CESAR-fitted machines (attribution uncertain) —
  https://khl.com/news/jcb-makes-anti-theft-move/1006173.article (not fetched — blocked)
- Fleet telematics/video (UK): a Geotab case cites a 2.7% premium reduction while the fleet grew
  40% (vendor claim) — https://www.geotab.com/uk/blog/can-dash-cams-lower-fleet-insurance-costs/ ;
  a comparison-site guide gives 5–15% typical — https://www.quotezone.co.uk/?p=65354 (not fetched — blocked)

**Insurer as referrer / preferential rates (UK commercial)**
- Aviva Risk Management Solutions lists escape-of-water specialist partners (Quensus, Leaksafe,
  Waterguard) whose services are offered to Aviva customers at "preferential rates" (UK commercial) —
  https://www.aviva.co.uk/risksolutions/specialist-partners/quensus/ ;
  https://www.aviva.co.uk/risksolutions/specialist-partners/leaksafe/ ;
  https://www.aviva.co.uk/risksolutions/protecting-your-property/escape-of-water/ (not fetched — blocked)
- Older Aviva/Waterguard campaign: Aviva commercial clients receive "discounted product pricing for
  all equipment supplied by Waterguard" (UK) — https://www.barbourproductsearch.info/aviva-and-waterguard-launch-escape-of-water-news043870.html (not fetched — blocked)
- Clyde & Co: some insurers offer leak devices free; expects more insurers to ask at presentation of
  risk whether a leak prevention device is fitted, "sometimes in exchange for lower premiums or
  excesses" (UK) — https://www.clydeco.com/en/insights-archive/2021/03/how-can-technology-help-you-mitigate-escape-of-wat (not fetched — blocked)

**Insurer conditions / exclusions (strongest form of pressure)**
- Munich Re (UK deterioration-of-stock cover) lists businesses with no temperature logging and no
  maintenance regime among risks it does not cover (UK) — https://www.munichre.com/specialty/global-markets-uk/en/solutions/construction-engineering-insurance/deterioration-of-stock-insurance.item-25aee387f438d61e0e9115a79623698d.html (not fetched — blocked)
- Deterioration-of-stock wordings: Prime Insurance (Rwanda) requires manual readings twice daily
  plus an alarm linked to an alarm receiving centre and ≥6-monthly specialist maintenance —
  https://prime.rw/public/themes/files/prime_insurance/productContract/Deterioration_Of_Stock.pdf ;
  Berjaya Sompo (Malaysia) requires constant supervision or automatic alarm to an attended location
  and readings ≥3×/day — https://www.berjayasompo.com.my/product/deterioration-stock-cold-storage (not fetched — blocked)
- Construction (UK): insurers "expect some or all" of the CIREG/Joint Code escape-of-water standards
  on high-risk sites; a compliant plan can bring benefits on premium and excess (attribution between
  these pages uncertain) — https://www.miller-insurance.com/news-and-insights/escape-of-water-how-damage-mitigation-plans-can-improve-your-construction-insurance/ ;
  https://global.lockton.com/gb/en/news-insights/tackling-rising-escape-of-water-claims-on-building-sites ;
  https://ciphe.org.uk/news-and-advice/press-releases/jcop-escape-of-water (not fetched — blocked)

**Scale of the insured loss pool (UK escape of water)**
- ABI 2023: escape-of-water claims cost £1.04bn, up 25% on 2022 (cited by Travelers) (UK) —
  https://www.insurancetimes.co.uk/expert-views/as-escape-of-water-claims-rise-brokers-can-mitigate-sme-risks-travelers/1453589.article (not fetched — blocked)
- ABI (2019): average daily cost ~£2.5m, up a third over three years (UK) —
  https://www.insurancetimes.co.uk/analysis/escape-of-water-claims-at-25m-a-day/1430915.article (not fetched — blocked)

### 4. Labour savings vs manual checks / logs

- Hastings Hotels: "saves 3 hours per day per property" with Kelsius (vendor case study, UK/NI) —
  https://www.casestudies.com/company/kelsius/case-study/hastings-hotels-saves-3-hours-per-day-per-property-with-kelsius (not fetched — blocked)
- The Bay Fish and Chips: 22+ hours of manual work saved per month (Navitas, vendor case study, UK)
  — https://www.casestudies.com/company/navitas-safety/case-study/the-bay-fish-and-chips-customer-case-study (not fetched — blocked)
- One Aldwych hotel: ~1 hour of staff time saved per day (Checkit, vendor case study, UK) —
  https://www.casestudies.com/company/checkit/case-study/one-aldwych-takes-food-safety-into-the-21st-century (not fetched — blocked)
- Nanna Mexico: ≥20 minutes/day saved by removing paper records (Checkit, vendor case study, UK) —
  https://www.casestudies.com/company/checkit/case-study/nanna-mexico-customer-case-study (not fetched — blocked)
- ComplianceMate white paper: paper logs take 20–30 s per item recorded vs ~5 s digitally (vendor
  claim, US) — https://compliancemate.com/wp-content/uploads/2025/04/Paper-Labor-Shortage-Foodservice-2024-update-v2.0-draft.pdf (not fetched — blocked)
- Selwood Housing (~7,000 homes) 12-week legionella remote-monitoring pilot: 75% drop in flushing
  requirement at one office site; *projected* 55 days of manpower saved across 21 facilities (vendor
  article, UK) — https://bdaily.co.uk/articles/2022/06/22/selwood-housing-to-reduce-flushing-requirement-by-75-using-remote-technology (not fetched — blocked)
- PTSG Water Treatment: remote monitoring across 160+ Change Grow Live sites, claimed no engineer
  attendance needed (vendor/contractor claim, UK) — https://www.ptsg.co.uk/ptsg-water-treatment-completes-remote-monitoring-roll-out-across-change-grow-live-estate/ (not fetched — blocked)
- Loreburn Housing Association rolling out remote monitoring/alerts in 26 supported-living units
  (UK) — https://www.scottishhousingnews.com/articles/loreburn-saves-time-and-money-thanks-to-innovative-monitoring-technology (not fetched — blocked)
- Co-op uses IoT monitoring/predictive maintenance across refrigeration in 2,500+ stores (UK) —
  https://chainstoreage.com/store-spaces/iot-monitoring-improves-u-k-retailers-operating-efficiency (not fetched — blocked)

### 5. Audit / proof requirements

- UK solicitor: an EHO "would expect to see your HACCP, your temperature management records ..."; a
  court looks at records as implemented at the inspection date, and you "cannot rely on putting
  systems or documents in place after the alleged breach" (UK) —
  https://www.nockolds.co.uk/enforcement-in-the-food-industry-dont-wait-for-the-inspector-strengthen-your-food-premises-defence-now/ (not fetched — blocked)
- FHRS "confidence in management" element assesses record-keeping practices (UK; attribution among
  local-authority FHRS pages uncertain) — https://eastcambs.gov.uk/food-safety/food-hygiene-rating-scheme (not fetched — blocked)
- CQC-related reporting: Keneydon House (Fenland) rated Requires Improvement; "only three
  occasions during October 2020 when recordings for room and fridge temperatures were documented"
  (UK) — https://www.wisbechstandard.co.uk/news/care-home-requires-improvement-again-6920962 (not fetched — blocked)
- Newbury Manor (Oldbury): medicines needing fridge storage "were not always stored at the correct
  temperature" (UK) — https://www.expressandstar.com/news/medicine-given-three-days-late-at-oldbury-care-home-6311379 (not fetched — blocked)
- Loggers reduce disposal: NHS toolkits say loggers show duration/extent of a breach, enabling
  advice rather than blanket disposal (UK) — https://www.england.nhs.uk/wp-content/uploads/sites/47/2023/07/East-of-England-Cold-Chain-Toolkit-2023-V1.pdf (not fetched — blocked)
- Insurer-side proof: deterioration-of-stock claims hinge on temperature logs and maintenance
  records (see Munich Re exclusion above) (UK) — https://www.munichre.com/specialty/global-markets-uk/en/solutions/construction-engineering-insurance/deterioration-of-stock-insurance.item-25aee387f438d61e0e9115a79623698d.html (not fetched — blocked)

## Buyer roles & budgets

- Bain: for 85% of IoT purchasing decisions, operational-technology people were the key decision
  makers or influencers (global) — https://www.bain.com/it/insights/selling-iot-solutions-to-experts/ (not fetched — blocked)
- IDC: lines of business are 40% of IoT budget decision makers, IT 36% (global) —
  https://blogs.idc.com/?p=219 (not fetched — blocked)
- Technalysis (2016, 620 respondents): 42% of IoT projects managed by facilities/operations or
  other business units (US) — https://www.pcworld.com/article/420527/on-many-iot-projects-it-shops-get-left-behind.html (not fetched — blocked)
- 451 Research (2018): only 34% of OT respondents "cooperate closely with IT" on IoT projects
  (global) — https://www.biztechreports.com/news-archive/2018/5/4/iot-survey-finds-operational-technology-and-information-technology-stakeholders-at-odds-451-research (not fetched — blocked)
- UK job adverts — **Compliance Manager** (housing): "direct line management responsibilities and a
  budget of approximately £3.5 million" — https://findajob.dwp.gov.uk/details/17168023 ; Maidenhead
  role £40k–£55k with £3.5m budget — https://www.jobleads.com/gb/job/compliance-manager--maidenhead--e7789a784728e87c7af61269d30e71d46 ;
  South Derbyshire DC Compliance Manager £50,788–£52,805 — https://www.southderbyshire.gov.uk/working-for-us/compliance-manager (not fetched — blocked)
  → legionella, fire, gas, electrical, asbestos and lifts typically sit with one compliance manager
  holding a revenue budget.
- Other named buyers seen in evidence: Responsible Person (fire doors) —
  https://www.gov.uk/government/publications/fire-safety-england-regulations-2022/fact-sheet-fire-doors-regulation-10 ;
  store owner/retailer in symbol groups (Nisa) — https://www.thegrocer.co.uk/news/nisa-stores-to-save-up-to-10k-a-year-with-food-safety-management-tech/704066.article ;
  registered manager in care homes / superintendent pharmacist (fridge records) —
  https://www.wisbechstandard.co.uk/news/care-home-requires-improvement-again-6920962 (not fetched — blocked)
- Opex vs capex: condition-monitoring vendors bundle hardware, software and support into a
  subscription to move it to opex (vendor claim) — https://tractian.com/en/blog/capex-or-opex-budgeting-for-condition-monitoring (not fetched — blocked)
- Subscription acceptance evidence (UK SMEs): Kelsius fees "from £4 a day" —
  https://www.thegrocer.co.uk/news/nisa-stores-to-save-up-to-10k-a-year-with-food-safety-management-tech/704066.article ;
  Logicall caterer monitoring "from just £40 per month" — https://catererlicensee.com/logicall-wireless-solutions-temperature-monitoring/ ;
  Hygiplas smart monitoring £51.58 ex VAT, up to 10 sensors, 1–3-year connectivity terms —
  https://chefstuff.co.uk/products/hygiplas-smart-monitoring-system-1 (not fetched — blocked)
- Recurring-revenue proof: Checkit FY23 ARR £11.5m (+28%), recurring revenue 93% of total (UK, LSE-
  listed monitoring/compliance company) — https://www.edisongroup.com/research/fy23-arr-ahead-of-expectations/31978/ (not fetched — blocked)

## Channels that work

- **Insurers (device as loss-prevention benefit):** LeakBot with 23 carriers —
  https://leakbot.io/about/our-story/ ; HSB Meshify Defender Slim "available through insurance
  companies that partner with HSB" — https://www.businesswire.com/news/home/20250508023834/en/HSBs-New-Slim-Sensors-Expand-IoT-Program-to-Habitational-Buildings-and-Homes-through-Amazon-Sidewalk ;
  HSB Canada sells through insurers and risk pools to commercial locations —
  https://www.munichre.com/hsbcanada/en/press-and-news/2020/hsb-canada-launches-sensor-systems-by-hsb.html (not fetched — blocked)
- **Brokers:** Covéa–LeakBot billed as "a first for brokers" — https://www.insurancebusinessmag.com/uk/news/property-insurance/covea-and-leakbot-partnership-offers-a-first-for-brokers-91063.aspx ;
  Ecclesiastical LeakBot trials with brokers — https://www.insurancetimes.co.uk/news/ecclesiastical-rolls-out-leakbot-trials-with-brokers/1429352.article ;
  Travelers urges brokers to help SMEs fit leak devices — https://www.insurancetimes.co.uk/expert-views/as-escape-of-water-claims-rise-brokers-can-mitigate-sme-risks-travelers/1453589.article (not fetched — blocked)
- **Insurer specialist-partner panels:** Aviva Quensus/Leaksafe/Waterguard at preferential rates —
  https://www.aviva.co.uk/risksolutions/specialist-partners/quensus/ (not fetched — blocked)
- **Symbol/buying groups:** Nisa partnership with Kelsius incl. 10% off installation (UK) —
  https://kelsius.com/2025/05/13/ ; Australian pharmacy body Gold Cross gives members exclusive
  pricing on Clever Logger fridge loggers (~A$450 single-fridge setup, 15% code) (AU) —
  https://cleverlogger.com/gold-cross/ (not fetched — blocked)
- **Service/maintenance contractors:** PTSG water treatment rolling remote monitoring into a 160+
  site charity contract — https://www.ptsg.co.uk/ptsg-water-treatment-completes-remote-monitoring-roll-out-across-change-grow-live-estate/ ;
  Danfoss ProsaLink "affordable monthly subscription paid by your customer", aimed at refrigeration
  installers — https://danfoss.com/en-gb/markets/refrigeration-and-air-conditioning/dcs/iot-cloud-solutions/installer-hub-for-prosa-iot-for-food-safety ;
  https://www.danfoss.com/en-gb/about-danfoss/news/dcs/one-app-for-affordable-temperature-monitoring-alarms-and-haccp/ ;
  Lowe Rental bundles IoT monitoring with planned/reactive maintenance in rental plans —
  https://www.lowerental.com/uk/long-term-rental/smart-enabled-commercial-refrigeration/ (not fetched — blocked)
- **Electrical wholesalers + installers:** Aico supplies through electrical wholesalers; social
  housing providers are its main customers and electrical contractors install (UK) —
  https://www.ifsecglobal.com/global/aico-qa-award-winning-training-rigorous-quality-control-innovations/ (not fetched — blocked)
- **IoT distributors/VARs:** Monnit IoTvantage programme for distributors, resellers, integrators,
  MSPs and OEMs (US/global) — https://monnit.com/blog/2017/10/27/monnit-partner-program-iotvantage/ (not fetched — blocked)

## Deal killers

- **IT/security review:** Henry Ford Hospital pathology informaticist: IT compliance and security
  assessments "can extend timelines by six to 12 months"; a 40–60-page vendor questionnaire; some
  devices disallowed (US) — https://www.captodayonline.com/pathologists-vendors-talk-lis-ims-integration/ (not fetched — blocked)
- **Security & cost as adoption barriers:** Vanson Bourne/Wi-SUN 2017 (350 IT decision makers
  UK/US/SE/DK): security held back 59%, cost of implementation delayed 46% —
  https://www.helpnetsecurity.com/2017/12/05/implement-iot-projects (not fetched — blocked)
- **PoC stall:** Cisco 2017 (1,845 IT/business decision makers, US/UK/India): 60% of IoT initiatives
  stall at PoC; only 26% had a complete success; IT–business collaboration top success factor (54%)
  — https://www.telecomtv.com/content/iot/cisco-survey-reveals-close-to-three-fourths-of-iot-projects-are-failing-26983/ ;
  https://technologymagazine.com/ai-and-machine-learning/cisco-survey-has-revealed-three-quarters-iot-projects-are-failing (not fetched — blocked)
- **Unclear benefit / cost:** Microsoft 2019, 30% PoC failure "because implementation is expensive
  or bottom-line benefits are unclear"; 47% lack skilled workers (global) —
  https://news.microsoft.com/source/2019/07/30/microsoft-announces-iot-signals-research-report-on-state-of-iot-adoption/ (not fetched — blocked)
- **Long deployments:** Omdia 2022, 49% say long deployment times are the biggest ROI roadblock —
  https://www.fiercesensors.com/iot-wireless/enterprise-iot-projects-move-toward-roi-roadblocks-remain (not fetched — blocked)
- **False alarms / alarm fatigue:** Lab Manager: "if you receive 99 alerts that are false alarms ...
  you will ignore the 100th"; cold storage can take 20–30 min to recover after a door opening, so
  short delays cause nuisance alerts (US) — https://www.labmanager.com/choose-the-right-alert-set-points-for-your-freezers-refrigerators-and-incubators-23385 ;
  https://www.labmanager.com/remote-temperature-monitoring-for-lab-cold-storage-setting-alert-thresholds-and-alarm-protocols-35296 (not fetched — blocked)
- Vaisala: alarm delays for GxP chambers should be set via risk assessment (global, vendor) —
  https://vaisala.com/en/blog/2024-09/managing-gxp-monitoring-system-alarms (not fetched — blocked)
- US patent text: lost wireless links and depleted batteries each trigger alarms; "too many false
  alerts can lead to alarm fatigue" (US) — https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11686642 (not fetched — blocked)
- **Alarm path failure = loss:** Vero loss bulletin — supermarket alarm battery flat, monitoring
  company never alerted, nearly $95,000 of stock spoiled (AU) —
  https://www.vero.com.au/content/dam/suncorp/insurance/broker/documents/vero-loss-bulletin-supermarket-alarm-failure-spoilage.pdf (not fetched — blocked)
- **Data overload / no one to act:** Schneider Electric FM survey (2016): 31% cite lack of internal
  resources to turn data into actionable results; funding 39% (US) —
  https://www.bdcnetwork.com/home/news/55160172/facility-managers-say-internet-of-things-analytics-will-impact-maintenance-soon (not fetched — blocked)
- **Battery/maintenance labour:** EnOcean model assumes ~US$2.50 change labour per node per battery
  swap (vendor claim, battery-free vendor) — https://www.enocean.com/wp-content/uploads/redaktion/pdf/white_paper/WhitePaper_EnOcean_Cost_of_Batteries_v4.0.pdf (not fetched — blocked)
- **Manual check not removed:** remote monitoring is described as a complement to, not a
  replacement for, periodic site checks in legionella (vendor framing) — see "Searched for but not
  found" re HSE wording.

## Named examples

| Example | What buyer pays / gets | Driver | URL |
|---|---|---|---|
| Hiscox × LeakBot (UK home) | Free £149 device + engineer visit | Insurance (EoW) | https://www.hiscox.co.uk/node/5001 |
| Covéa × LeakBot (UK HNW) | Free device + nil EoW excess | Insurance | https://www.coveainsurance.co.uk/brokers/broker-news/covea-insurance-extend-leakbot-as-part-of-core-proposition-for-hnw-portfolio/ |
| State Farm × Ting (US) | Free sensor, no discount, $1k credit; >1m homes | Insurance (fire) | https://newsroom.statefarm.com/state-farm-offers-customers-more-than-one-million-free-ting-sensors/ |
| Chubb (US commercial) | ~$600–700/building/yr, premium credit | Insurance (water) | https://www.insurancejournal.com/news/national/2022/01/31/651005.htm |
| HSB via EMC (US SMB) | ~$200/yr lease | Insurance (leak/freeze) | https://www.emcinsurance.com/losscontrol/vendors/sensor-solutions |
| Aviva specialist partners (UK commercial) | Preferential rates | Insurance referral | https://www.aviva.co.uk/risksolutions/specialist-partners/quensus/ |
| Kelsius × Nisa (UK c-stores) | From £4/day; 10% off install | Food safety + labour | https://www.thegrocer.co.uk/news/nisa-stores-to-save-up-to-10k-a-year-with-food-safety-management-tech/704066.article |
| Checkit (UK, listed) | Subscription; ARR £11.5m FY23 | Compliance workflows | https://www.edisongroup.com/research/fy23-arr-ahead-of-expectations/31978/ |
| PTSG × Change Grow Live (UK) | Remote legionella monitoring, 160+ sites | Legionella (HSG274) | https://www.ptsg.co.uk/ptsg-water-treatment-completes-remote-monitoring-roll-out-across-change-grow-live-estate/ |
| Danfoss ProsaLink (EU/UK) | Monthly sub paid by installer's customer | Refrigeration/HACCP | https://danfoss.com/en-gb/markets/refrigeration-and-air-conditioning/dcs/iot-cloud-solutions/installer-hub-for-prosa-iot-for-food-safety |
| Aico HomeLINK (UK social housing) | Via wholesalers/installers | Fire + Awaab's Law | https://www.cih.org/blogs/awaab-s-law-marks-a-turning-point-for-safe-and-healthy-homes/ |
| CESAR + Tracker (UK plant) | Up to 25% premium discount (2011) | Insurance (theft) | https://www.fleetnews.co.uk/news/2011/6/9/tracker-and-datatag-announce-security-partnership/39779/ |

(All table URLs: not fetched — blocked.)

## Searched for but not found

- WebFetch failed for every host tried (DNS ENOTFOUND); no page could be opened to confirm full
  context. All claims rely on search snippets.
- A current (2024/2025) ABI escape-of-water figure; latest found is £1.04bn for 2023 via Travelers.
- Any UK insurer giving **free** IoT leak sensors to **commercial/SME** customers (found only UK home
  programmes, US commercial programmes, and UK "preferential rates" referrals). Zurich UK commercial
  sensor discount: not found. Chubb's average commercial credit: not disclosed.
- Primary HSE text saying remote sensors can replace (not just supplement) HSG274 monthly manual
  sentinel checks.
- GPhC's binding standard wording on fridge monitoring and record retention (only inspection
  action plans and NHS SOPs found).
- An independent (non-vendor) study of time saved by digital temperature monitoring — all hour
  figures are vendor case studies.
- Independent survey of UK SME buyers' acceptance of subscription vs one-off purchase for sensors.
- Field data on truck-roll / installation cost per sensor for SMEs.
- Current MHRA GDP deficiency data specifically on alarms/continuous monitoring (only 2016 summary).
- Aico market share or HomeLINK deployment numbers; a UK pharmacy wholesaler/buying-group offering
  member deals on fridge loggers (only an Australian example found).
- A source for the CESAR "twice as likely to be recovered" claim with a clear URL (dropped).
- Average legionella contractor price per monthly temperature visit (not searched in depth).

## Queries run

1. IoT survey payback period expectations businesses ROI months
2. insurer free water leak detection sensors commercial customers escape of water claims
3. IoT projects fail proof of concept stage survey percentage Cisco
4. ABI escape of water claims paid per day 2024 £ million home insurance
5. State Farm Ting electrical fire sensor free policyholders Whisker Labs results fires prevented
6. Zurich commercial property insurance IoT water leak sensors customers premium discount UK
7. Chubb commercial policyholders IoT water sensors free premium credit program
8. F-gas regulations automatic leak detection system mandatory 500 tonnes CO2 equivalent refrigeration
9. HSG274 legionella monthly sentinel outlet temperature checks remote monitoring
10. digital temperature monitoring kitchens saves hours per week manual temperature checks paper logs case study
11. Food Safety Act 1990 section 21 due diligence defence temperature records evidence EHO
12. vaccine fridge failure cost NHS cold chain incident wasted vaccines pharmacy £
13. vaccine wastage cost cold chain breach fridge policy [england.nhs.uk]
14. West Yorkshire GP cold chain failures vaccines wasted £191,000 fridge
15. Vaccine Update cold chain failures percentage wastage power cuts fridge malfunction [gov.uk]
16. survey barriers to IoT adoption security concerns integration cost skills percentage respondents
17. Microsoft IoT Signals report proof of concept failure reasons cost complexity percent
18. remote monitoring false alarms nuisance alerts users switch off alerts cold storage temperature monitoring alarm fatigue
19. LeakBot insurers partners number of homes claims reduction escape of water percentage HomeServe
20. water hygiene contractor remote temperature monitoring legionella reduce site visits cost saving housing association
21. plant theft tracker insurance discount CESAR scheme construction equipment theft cost UK
22. who makes IoT purchasing decisions operations vs IT department survey line of business budget
23. hardware as a service subscription opex instead of capex IoT sensors customers prefer monthly fee
24. hospital IT security approval IoT device network onboarding blocked medical device vendor security questionnaire delays sales
25. Fire Safety (England) Regulations 2022 quarterly fire door checks communal buildings over 11 metres responsible person
26. GPhC pharmacy fridge temperature monitoring daily record maximum minimum requirement inspection
27. Environment Agency MCERTS continuous monitoring permit requirement operators monitoring standard
28. Aviva Risk Management Solutions specialist partners discounted escape of water detection commercial customers
29. refrigeration maintenance contractor offers remote temperature monitoring service customers subscription UK supermarket convenience
30. Kelsius fridge monitor could save stores £2000 a year convenience retailers Nisa
31. company fined legionella failed to carry out monthly temperature checks HSE prosecution £
32. Selwood Housing remote monitoring reduce flushing requirement 75% legionella pilot manpower days
33. Henry Ford Hospital security assessments add six to 12 months vendor onboarding CAP Today
34. security assessment vendor onboarding months questionnaire network access instruments [captodayonline.com]
35. Omdia IoT survey enterprises expect ROI within 12 months deployment times roadblock 2022
36. fleet telematics insurance premium reduction commercial fleet insurer requires telematics UK percentage
37. "six to 12 months" vendor onboarding security pathology informaticist [captodayonline.com]
38. FSA Safer Food Better Business fridge temperature checks record daily opening closing checks small businesses [food.gov.uk]
39. IoT sensor installation cost battery replacement total cost of ownership barrier small business deployment truck roll
40. deterioration of stock insurance cover requires temperature alarm warranty refrigeration condition commercial policy
41. construction site escape of water insurers require leak detection system condition contractors all risks Quensus WaterSafe
42. Hiscox commercial insurance IoT water leak sensors offered business customers
43. HSB Sensor Systems small business leak freeze sensors price per month insurers Munich Re
44. Checkit annual report revenue recurring subscription customers facilities food safety monitoring ARR
45. Monnit OR Disruptive Technologies reseller partner channel integrators sell sensors through partners model
46. escape of water claims £ million a day insurers paid ABI figures latest [abi.org.uk, insurancetimes.co.uk]
47. CQC inspection report medicines fridge temperatures not monitored recorded care home requires improvement
48. job advert "Compliance Manager" housing association water hygiene legionella fire safety budget responsibility salary
49. "Compliance Manager" housing "budget of approximately £3.5 million" line management
50. Travelers SME escape of water claims brokers mitigate leak detection [insurancetimes.co.uk]
51. food hygiene rating confidence in management records inspection poor documentation proportion of businesses FSA
52. SMEs require payback period less than 2 years energy efficiency investment survey BEIS hurdle
53. Awaab's Law damp mould sensors social housing landlords environmental sensors Aico HomeLink deployment
54. Aico sells through electrical wholesalers installers channel smoke alarms social housing market share
55. MHRA GDP wholesale dealer temperature monitoring storage areas continuous monitoring alarm deficiencies inspection findings
56. facilities managers IoT data overload dashboards not used actionable insights survey building sensors too much data
57. wireless fridge temperature monitoring subscription £ per sensor per month pricing UK small business
58. pharmacy wholesaler or buying group offers members fridge temperature monitoring data logger partnership discount community pharmacy

## Sources

All: not fetched — blocked (WebFetch DNS failure in this session); content seen in search results.

1. https://www.fiercesensors.com/iot-wireless/enterprise-iot-projects-move-toward-roi-roadblocks-remain — Fierce Sensors, Omdia enterprise IoT survey, 2022
2. https://www.networkworld.com/article/3674768/iot-survey-70-of-enterprises-expect-a-1-year-roi.html — Network World, 2022
3. https://www.rcrwireless.com/20220921/carriers/an-iot-conundrum-poor-planning-long-delays-hobble-quick-returns-high-expectations — RCR Wireless, 21 Sep 2022
4. https://omdia.tech.informa.com/pr/2022-jul/new-omdia-research-finds-enterprises-are-turning-to-5g-for-their-iot-needs — Omdia press release, Jul 2022
5. https://www.fujitsu.com/uk/news/pr/2018/fs-20181010.html — Fujitsu UK press release, 10 Oct 2018
6. https://macaubusiness.com/sumatosoft-reveals-insights-on-iot-roi-median-payback-period-just-12-months/ — SumatoSoft study (vendor), 2026
7. https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/392908/Barriers_to_Energy_Efficiency_FINAL_2014-12-10.pdf — DECC, SME energy efficiency barriers, Dec 2014
8. https://www.gov.uk/government/publications/research-to-assess-the-barriers-and-drivers-to-energy-efficiency-in-small-and-medium-sized-enterprises — GOV.UK publication page
9. https://www.betterretailing.com/exclusive-fridge-monitor-could-save-stores-2000-a-year-according-to-kelsius/ — Better Retailing
10. https://www.thegrocer.co.uk/news/nisa-stores-to-save-up-to-10k-a-year-with-food-safety-management-tech/704066.article — The Grocer, 2025
11. https://kelsius.com/2025/05/13/ — Kelsius news (vendor), May 2025
12. https://news.microsoft.com/source/2019/07/30/microsoft-announces-iot-signals-research-report-on-state-of-iot-adoption/ — Microsoft, 30 Jul 2019
13. https://venturebeat.com/security/microsoft-30-of-iot-projects-fail-in-the-proof-of-concept-stage — VentureBeat, 2019
14. https://www.telecomtv.com/content/iot/cisco-survey-reveals-close-to-three-fourths-of-iot-projects-are-failing-26983/ — TelecomTV, May 2017
15. https://technologymagazine.com/ai-and-machine-learning/cisco-survey-has-revealed-three-quarters-iot-projects-are-failing — Technology Magazine
16. https://www.helpnetsecurity.com/2017/12/05/implement-iot-projects — Help Net Security, 5 Dec 2017
17. https://www.hiscox.co.uk/node/5001 — Hiscox UK, LeakBot offer, 2020
18. https://www.coveainsurance.co.uk/brokers/broker-news/covea-insurance-extend-leakbot-as-part-of-core-proposition-for-hnw-portfolio/ — Covéa Insurance broker news
19. https://leakbot.io/about/our-story/ — LeakBot / Ondo (vendor)
20. https://www.clydeco.com/en/insights-archive/2021/03/how-can-technology-help-you-mitigate-escape-of-wat — Clyde & Co, Mar 2021
21. https://newsroom.statefarm.com/state-farm-expands-ting-fire-safety-program-to-2-million-homes/ — State Farm newsroom, Apr 2024
22. https://newsroom.statefarm.com/state-farm-offers-customers-more-than-one-million-free-ting-sensors/ — State Farm newsroom, 2025
23. https://www.tingfire.com/statefarm-faqs/ — Ting / Whisker Labs FAQ
24. https://www.nationwide.com/campaigns/commercial-leak-and-freeze-detection — Nationwide (US)
25. https://www.insurancejournal.com/news/national/2022/01/31/651005.htm — Insurance Journal, 31 Jan 2022
26. https://www.claimsjournal.com/news/national/2022/02/08/308536.htm — Claims Journal, 8 Feb 2022
27. https://news.na.chubb.com/2018-10-31-Chubb-Partners-With-Hartford-Steam-Boiler-to-Deploy-Innovative-Internet-of-Things-Sensors-in-Homes-and-Businesses — Chubb, 31 Oct 2018
28. https://insurancenewsnet.com/oarticle/streamlabs-expands-product-suite-with-scout-a-new-smart-water-sensor — InsuranceNewsNet
29. https://www.emcinsurance.com/losscontrol/vendors/sensor-solutions — EMC Insurance loss control
30. https://www.insurancetimes.co.uk/zurich-teams-up-with-smart-tech-company/1419257.article — Insurance Times
31. https://www.aviva.com/newsroom/news-releases/2004/05/uk-thiefbeating-security-system-offers-lifeline-1746 — Aviva (Norwich Union), May 2004
32. https://www.fleetnews.co.uk/news/2011/6/9/tracker-and-datatag-announce-security-partnership/39779/ — Fleet News, Jun 2011
33. https://khl.com/news/jcb-makes-anti-theft-move/1006173.article — KHL
34. https://www.geotab.com/uk/blog/can-dash-cams-lower-fleet-insurance-costs/ — Geotab UK (vendor)
35. https://www.quotezone.co.uk/?p=65354 — Quotezone guide
36. https://www.aviva.co.uk/risksolutions/specialist-partners/quensus/ — Aviva Risk Management Solutions
37. https://www.aviva.co.uk/risksolutions/specialist-partners/leaksafe/ — Aviva Risk Management Solutions
38. https://www.aviva.co.uk/risksolutions/protecting-your-property/escape-of-water/ — Aviva Risk Management Solutions
39. https://www.barbourproductsearch.info/aviva-and-waterguard-launch-escape-of-water-news043870.html — Barbour Product Search (undated)
40. https://www.munichre.com/specialty/global-markets-uk/en/solutions/construction-engineering-insurance/deterioration-of-stock-insurance.item-25aee387f438d61e0e9115a79623698d.html — Munich Re Specialty UK
41. https://prime.rw/public/themes/files/prime_insurance/productContract/Deterioration_Of_Stock.pdf — Prime Insurance (Rwanda) policy wording
42. https://www.berjayasompo.com.my/product/deterioration-stock-cold-storage — Berjaya Sompo (Malaysia)
43. https://www.miller-insurance.com/news-and-insights/escape-of-water-how-damage-mitigation-plans-can-improve-your-construction-insurance/ — Miller Insurance
44. https://global.lockton.com/gb/en/news-insights/tackling-rising-escape-of-water-claims-on-building-sites — Lockton
45. https://ciphe.org.uk/news-and-advice/press-releases/jcop-escape-of-water — CIPHE
46. https://www.insurancetimes.co.uk/expert-views/as-escape-of-water-claims-rise-brokers-can-mitigate-sme-risks-travelers/1453589.article — Insurance Times / Travelers
47. https://www.insurancetimes.co.uk/analysis/escape-of-water-claims-at-25m-a-day/1430915.article — Insurance Times, 2019
48. https://press.hse.gov.uk/2024/12/03/company-failed-to-manage-legionella-risk-as-prisoner-dies — HSE press, 3 Dec 2024
49. https://www.bohs.org/app/uploads/2025/11/Ceri-Rideout-HSE-Prosecutions_Legionella-2025.pdf — BOHS / HSE presentation, 2025
50. https://www.hvpmag.co.uk/BUPA-fined-3m-after-legionella-death-in-nursing-home — HVP Magazine
51. https://www.food.gov.uk/business-guidance/chilling-food-correctly-in-your-business — Food Standards Agency
52. https://www.food.gov.uk/business-guidance/safer-food-better-business-sfbb — Food Standards Agency
53. https://www.legislation.gov.uk/ukpga/1990/16/section/21/enacted — Food Safety Act 1990 s.21
54. https://www.nockolds.co.uk/enforcement-in-the-food-industry-dont-wait-for-the-inspector-strengthen-your-food-premises-defence-now/ — Nockolds Solicitors
55. https://eastcambs.gov.uk/food-safety/food-hygiene-rating-scheme — East Cambridgeshire DC
56. https://inspections.pharmacyregulation.org/pharmacy/action-plan/1117249-2021-07-12-19790 — GPhC inspection action plan, 2021
57. https://www.gov.uk/government/publications/vaccine-update-issue-369-february-2026/vaccine-update-issue-369-february-2026 — UKHSA Vaccine Update 369, Feb 2026
58. https://www.gov.uk/government/publications/vaccine-update-issue-338-may-2023/vaccine-update-issue-338-may-2023 — UKHSA Vaccine Update 338, May 2023
59. https://www.gov.uk/government/publications/vaccine-update-issue-378-october-2026/vaccine-update-issue-378-october-2026 — UKHSA Vaccine Update 378, Oct 2026
60. https://www.england.nhs.uk/wp-content/uploads/sites/47/2023/07/East-of-England-Cold-Chain-Toolkit-2023-V1.pdf — NHS England East of England, 2023
61. https://www.yorkshirepost.co.uk/news/500-children-recalled-jabs-fridge-fails-village-gp-practice-1822563 — Yorkshire Post (date not shown)
62. https://gmp-compliance.org/gmp-news/gdp-deficiency-data-available — ECA / GMP-Compliance on MHRA GDP deficiency data
63. https://www.gov.uk/guidance/checking-f-gas-equipment-for-leaks — GOV.UK
64. https://climalife.com/?p=159477 — Climalife (refrigerant supplier)
65. https://www.epa.ie/publications/compliance--enforcement/air/ods--f-gas/1-IRL-Summary-Guidance-to-Compliance-with-the-ODS-and-F-gas-Regulations-V1.0.pdf — Irish EPA
66. https://www.gov.uk/government/publications/fire-safety-england-regulations-2022/fact-sheet-fire-doors-regulation-10 — GOV.UK / Home Office
67. https://www.gov.uk/government/publications/mcerts-for-stack-emissions-monitoring-equipment-at-industrial-installations/mcerts-for-stack-emissions-monitoring-equipment-at-industrial-installations — Environment Agency
68. https://www.gov.uk/government/publications/m20-quality-assurance-of-continuous-emission-monitoring-systems/monitoring-stack-emissions-quality-assurance-of-continuous-monitoring — Environment Agency M20
69. https://www.lbhf.gov.uk/news/2025/10/tackling-damp-and-mould-keep-residents-safe-home — LB Hammersmith & Fulham, Oct 2025
70. https://www.cih.org/blogs/awaab-s-law-marks-a-turning-point-for-safe-and-healthy-homes/ — Chartered Institute of Housing
71. https://www.casestudies.com/company/kelsius/case-study/hastings-hotels-saves-3-hours-per-day-per-property-with-kelsius — vendor case study
72. https://www.casestudies.com/company/navitas-safety/case-study/the-bay-fish-and-chips-customer-case-study — vendor case study
73. https://www.casestudies.com/company/checkit/case-study/one-aldwych-takes-food-safety-into-the-21st-century — vendor case study
74. https://www.casestudies.com/company/checkit/case-study/nanna-mexico-customer-case-study — vendor case study
75. https://compliancemate.com/wp-content/uploads/2025/04/Paper-Labor-Shortage-Foodservice-2024-update-v2.0-draft.pdf — ComplianceMate white paper (vendor)
76. https://bdaily.co.uk/articles/2022/06/22/selwood-housing-to-reduce-flushing-requirement-by-75-using-remote-technology — Bdaily partner article, Jun 2022
77. https://www.ptsg.co.uk/ptsg-water-treatment-completes-remote-monitoring-roll-out-across-change-grow-live-estate/ — PTSG
78. https://www.scottishhousingnews.com/articles/loreburn-saves-time-and-money-thanks-to-innovative-monitoring-technology — Scottish Housing News
79. https://chainstoreage.com/store-spaces/iot-monitoring-improves-u-k-retailers-operating-efficiency — Chain Store Age
80. https://www.wisbechstandard.co.uk/news/care-home-requires-improvement-again-6920962 — Wisbech Standard
81. https://www.expressandstar.com/news/medicine-given-three-days-late-at-oldbury-care-home-6311379 — Express & Star
82. https://www.bain.com/it/insights/selling-iot-solutions-to-experts/ — Bain & Company
83. https://blogs.idc.com/?p=219 — IDC blog
84. https://www.pcworld.com/article/420527/on-many-iot-projects-it-shops-get-left-behind.html — PCWorld / Technalysis, 2016
85. https://www.biztechreports.com/news-archive/2018/5/4/iot-survey-finds-operational-technology-and-information-technology-stakeholders-at-odds-451-research — 451 Research, May 2018
86. https://findajob.dwp.gov.uk/details/17168023 — DWP Find a Job advert
87. https://www.jobleads.com/gb/job/compliance-manager--maidenhead--e7789a784728e87c7af61269d30e71d46 — JobLeads advert
88. https://www.southderbyshire.gov.uk/working-for-us/compliance-manager — South Derbyshire DC advert
89. https://tractian.com/en/blog/capex-or-opex-budgeting-for-condition-monitoring — Tractian (vendor)
90. https://catererlicensee.com/logicall-wireless-solutions-temperature-monitoring/ — Caterer & Licensee / Logicall
91. https://chefstuff.co.uk/products/hygiplas-smart-monitoring-system-1 — Chefstuff (reseller)
92. https://www.edisongroup.com/research/fy23-arr-ahead-of-expectations/31978/ — Edison Group on Checkit, 2023
93. https://www.businesswire.com/news/home/20250508023834/en/HSBs-New-Slim-Sensors-Expand-IoT-Program-to-Habitational-Buildings-and-Homes-through-Amazon-Sidewalk — HSB via Business Wire, 8 May 2025
94. https://www.munichre.com/hsbcanada/en/press-and-news/2020/hsb-canada-launches-sensor-systems-by-hsb.html — HSB Canada, 2020
95. https://www.insurancebusinessmag.com/uk/news/property-insurance/covea-and-leakbot-partnership-offers-a-first-for-brokers-91063.aspx — Insurance Business UK
96. https://www.insurancetimes.co.uk/news/ecclesiastical-rolls-out-leakbot-trials-with-brokers/1429352.article — Insurance Times
97. https://munichre.com/hsb/en/press-and-publications/press-releases/2019/2019-09-17-low-cost-small-business-iot-sensor-solution.html — HSB (Munich Re) press release, Sep 2019
98. https://cleverlogger.com/gold-cross/ — Clever Logger × Gold Cross (AU)
99. https://danfoss.com/en-gb/markets/refrigeration-and-air-conditioning/dcs/iot-cloud-solutions/installer-hub-for-prosa-iot-for-food-safety — Danfoss
100. https://www.danfoss.com/en-gb/about-danfoss/news/dcs/one-app-for-affordable-temperature-monitoring-alarms-and-haccp/ — Danfoss news
101. https://www.lowerental.com/uk/long-term-rental/smart-enabled-commercial-refrigeration/ — Lowe Rental UK
102. https://www.ifsecglobal.com/global/aico-qa-award-winning-training-rigorous-quality-control-innovations/ — IFSEC Global, Aico interview, 2018
103. https://monnit.com/blog/2017/10/27/monnit-partner-program-iotvantage/ — Monnit, Oct 2017
104. https://www.captodayonline.com/pathologists-vendors-talk-lis-ims-integration/ — CAP TODAY, 2026
105. https://www.labmanager.com/choose-the-right-alert-set-points-for-your-freezers-refrigerators-and-incubators-23385 — Lab Manager
106. https://www.labmanager.com/remote-temperature-monitoring-for-lab-cold-storage-setting-alert-thresholds-and-alarm-protocols-35296 — Lab Manager
107. https://vaisala.com/en/blog/2024-09/managing-gxp-monitoring-system-alarms — Vaisala (vendor), Sep 2024
108. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11686642 — USPTO patent 11686642
109. https://www.vero.com.au/content/dam/suncorp/insurance/broker/documents/vero-loss-bulletin-supermarket-alarm-failure-spoilage.pdf — Vero (Suncorp) loss bulletin
110. https://www.bdcnetwork.com/home/news/55160172/facility-managers-say-internet-of-things-analytics-will-impact-maintenance-soon — Building Design+Construction, 2016
111. https://www.enocean.com/wp-content/uploads/redaktion/pdf/white_paper/WhitePaper_EnOcean_Cost_of_Batteries_v4.0.pdf — EnOcean white paper (vendor)

## Implications for the scoring rubric

- **Cost of incident:** 10 = sourced £/$ loss per *site/incident* (fine, claim, spoiled stock) — e.g. £600k legionella fine [48], ~$95k spoilage [109], £105k across 25 failed vaccine fridges [61]; 5 = national aggregate only (EoW £1.04bn [46]); 0 = no figure. Payback test: evidence implying ≤12-month payback scores high; >2 years caps at 5 [1][7][9].
- **Frequency:** 10 = a mandated check or incident recurring at least monthly per site (daily fridge logs [56], monthly sentinel checks [49], quarterly fire doors [66]); 5 = roughly annual; 0 = rare/unquantified.
- **Workaround:** 10 = manual routine with quantified hours/£ (e.g. 3.8 h/week ≈ £2.2k/yr [9]); 5 = exists, unquantified; 0 = none.
- **Compliance/insurance pressure:** 10 = named rule or policy condition requiring monitoring/records *plus* enforcement or claim-exclusion evidence [48][40][80]; 7–8 = insurer pays/subsidises devices [17][21]; 5 = guidance, "recommends" or preferential-rate referral [36]; 0 = none.
- **Buyer with budget:** 10 = operations/compliance title with evidenced budget (advert stating £ budget [86]); 5 = title only; 0 = "businesses". Deduct when the buyer is IT, since OT drives most IoT purchases [82].
- **Distribution channel:** 10 = named intermediary already reselling/bundling monitoring to that site type (insurer [19], buying group [10], service contractor [77][99], wholesaler [102]); 5 = a regular site visitor exists but no evidence it sells tech; 0 = direct sales only.
- **Market gap:** 10 = paying incumbents prove willingness to pay but are enterprise-priced or absent in the niche; 5 = crowded or vendor-only evidence; 0 = dominant cheap incumbent.
- **Buildability/BOM:** 10 = commodity sensor, LPWAN/cellular (no customer IT network), multi-year battery, CE/UKCA only; 5 = needs calibration/traceability or harsh environment; 0 = MCERTS/ATEX/medical certification [67] or unproven sensing. Penalise corporate-network dependency (6–12-month reviews [104]) and false-alarm-prone physics [105].
- **Recurring revenue:** 10 = records must be retained on a statutory/insurer schedule *and* comparable subscriptions exist (£4/day [10], ~$200/yr [29], Checkit 93% recurring [92]); 5 = alerts only; 0 = one-off sale.
- **Public evidence of pain:** 10 = regulator enforcement + trade press + forums; 5 = vendor case studies only; 0 = none.
