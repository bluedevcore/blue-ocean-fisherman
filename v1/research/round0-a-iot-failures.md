# Round 0 (a): Why hardware and IoT startups fail, and what the survivors had in common

Researcher topic report, BLUE OCEAN FISHERMAN round 0. Prepared on 2026-11-05.

**How this was researched (read this first).** I ran 63 distinct WebSearch queries, listed at the end. Every WebFetch attempt failed with a DNS or egress denial from the session network policy: cbinsights.com, ciodive.com, venturebeat.com and mckinsey.com all failed. The proxy log also showed other researchers' fetches of en.wikipedia.org and tech.eu being refused. I therefore did not open any page directly. Every claim below comes from the search engine's extract of the cited page and is marked **(not fetched — blocked)**, as `roles/researcher.md` permits.

I used domain-restricted searches (`allowed_domains`) where possible, so that each figure is tied to the right page. Where a figure appeared in a mixed result set and I could not isolate the exact outlet, the bullet says so. Vendor figures are labelled **(vendor claim)**. Geography is given as US, UK, EU or global.

## Summary

- **Most IoT initiatives stall before scale.**
  - Cisco (2017, US/UK/India): 60% of IoT initiatives stalled at proof of concept, and only 26% of companies had an initiative they considered a complete success.
  - Beecham Research (2020, global): 58% of projects were judged unsuccessful.
  - Microsoft IoT Signals (2019, global): about 30% failed at proof of concept.
  - IoT Analytics (2023 data, global): connected-product OEMs averaged 41 months from kick-off to their first paying customer.
- **The main killers are commercial, not technical.** They are: no market need or unclear ROI, the cost of scaling beyond the pilot, integration and security concerns, installation and field-service cost, and long multi-stakeholder B2B sales cycles.
- **Hardware adds failure modes software companies do not have.** These include:
  - burn rate and tooling or manufacturing delays;
  - certification gates (PTCRB, carrier approval, and the EU RED cybersecurity rules from August 2025);
  - connectivity obsolescence or operator collapse (the US 3G sunset in 2022, UK 2G switch-off by 2033 at the latest, Sigfox's receivership in 2022 and its owner's French units back in court in 2025);
  - battery life that falls short of the datasheet;
  - dependence on the vendor's cloud (Insteon, Revolv);
  - "bulk hardware" revenue that does not convert into installed, paying use (Latch's restatement, SmartRent's hardware revenue falling 39%).
- **The survivors in the evidence share five traits.** Most success figures are company-reported, and survivorship bias applies.
  1. They sell monitoring as a multi-year subscription with the hardware bundled in. Samsara reports net retention above 115% and its GAAP gross margin rising from about 60% to about 70%. Augury, Controlant and the HACCP sensor rental vendors follow the same model.
  2. They sell through a party that already owns the risk or the site relationship: State Farm with Ting, UK insurers with LeakBot, Carrier with Augury, ready-mix suppliers with Giatec, and resellers and distributors with Monnit.
  3. They attach to a must-have loss or compliance duty: electrical fire, water damage, pharma cold chain, food-safety records, concrete strength, livestock water.
  4. They keep installation self-serve or bundled into an existing visit.
  5. They de-risk the technology with certified modules, more than one network, planned radio coverage and fallbacks that work without the cloud.

## Failure causes

### F1. No market need, "nice to have" and unclear ROI
- **CB Insights, consumer hardware.** Analysts reviewed nearly 400 failed consumer hardware startups. The top reasons were lack of consumer demand, then high burn rate, then lack of interest after the initial crowdfund, then product strategy mistakes (global, consumer-focused). https://www.cbinsights.com/research/report/hardware-startups-failure-success/ ; https://www.cbinsights.com/reports/CB-Insights_Hardware-Startups-Fail.pdf (not fetched — blocked)
- **CB Insights, all startups.** "No market need" ranks first and running out of cash second, the latter at about 29% (global, all sectors). https://www.cbinsights.com/reports/The-20-Reasons-Startups-Fail.pdf ; mirror: https://www.talentica.com/wp-content/uploads/2024/02/The-20-Reasons-Startups-Fail.pdf (not fetched — blocked)
- **Microsoft IoT Signals (2019, global).** "Nearly a third of projects fail at proof of concept", mainly because implementation is expensive or the bottom-line benefits are unclear. The same coverage says 38% of adopters cite complexity and technical challenges as a barrier. https://www.themanufacturer.com/articles/30-iot-projects-fail-proof-concept-stage/ (not fetched — blocked)
- **Microsoft IoT Signals, reasons for PoC failure.** Among projects that failed at proof of concept, 32% named the cost of scaling as the main reason and 28% named unclear business value or ROI. These figures appeared in a mixed search result set and I could not isolate the outlet; the two candidate pages are listed. https://venturebeat.com/security/microsoft-30-of-iot-projects-fail-in-the-proof-of-concept-stage ; https://rcrwireless.com/20190731/internet-of-things/microsoft-report-enterprise-iot-adoption (not fetched — blocked)
- **Bain (2018 survey of more than 600 commercial and industrial IoT buyers, 627 respondents; 533 in 2016).**
  - Buyers were wary of the same barriers as two years earlier: security, integration and uncertain ROI.
  - 42% of executives listed security as a top concern.
  - Bain estimated buyers would pay about 22% more for devices if security concerns were resolved.
  - Bain put the ROI uncertainty down to "the amount of customization currently required".
  - https://integrationcms.bain.com/contentassets/5aa3a678438846289af59f62e62a3456/bain_brief_unlocking_opportunities_in_the_internet_of_things.pdf ; https://www.bain.com/about/media-center/press-releases/2018/bain-predicts-the-iot-market-will-more-than-double-by-2021/ (not fetched — blocked)
- **Agricultural sensors (US).**
  - Fewer than 10% of US irrigated crops use moisture sensors. The paper blames sensor cost, the difficulty of deploying and maintaining sensors, and the difficulty of processing their data. It also finds that even for sparse deployments, benefits exceed costs only a third of the time. https://arxiv.org/pdf/1912.12382 (not fetched — blocked)
  - Lux Research: with growers near a $4-per-bushel break-even, "only farms over 2,500 acres will find it attractive to purchase new sensor hardware". https://www.electronicspecifier.com/news/analysis/price-challenges-block-agricultural-sensor-adoption (not fetched — blocked)
  - A University of Georgia extension project found a significant financial return from soil-moisture sensors. Even so, it found "the perceived complexity of the scheduling tools and reduced or loss of interest among agents (and farmers) were detrimental". https://striplingpark.caes.uga.edu/research/sfy2018-regional-water-plan-seed-grant/conclusions.html (not fetched — blocked)
- **Investor framing.** Angel investors sort ideas into "painkillers" and "vitamins". B2B startups also ask customers "to take a chance on the product and the company". https://www.holloway.com/g/angel-investing/sections/evaluating-the-idea (not fetched — blocked)

### F2. Pilot purgatory and long sales cycles
- **Cisco (May 2017).** 60% of IoT initiatives stalled at proof of concept, and only 26% of companies had an IoT initiative they considered a complete success. https://www.intelligentcio.com/me/2017/05/30/cisco-survey-reveals-close-to-three-quarters-of-internet-of-things-projects-are-failing/ (not fetched — blocked)
- **Cisco, further detail.** The same trade coverage reports:
  - 1,845 IT and business decision-makers in the US, UK and India were surveyed;
  - 35% of IT decision-makers called their initiatives a complete success, against 15% of business decision-makers;
  - a third of completed projects were not considered a success.
  - These figures appeared across a mixed result set; candidate pages: https://www.ciodive.com/news/cisco-more-than-half-of-enterprise-iot-projects-unsuccessful/444824/ ; https://www.telecomtv.com/content/iot/cisco-survey-reveals-close-to-three-fourths-of-iot-projects-are-failing-26983/amp/ (not fetched — blocked)
- **Beecham Research (2020, global).**
  - 42% of projects were judged successful (12% fully, 30% mostly) and 58% unsuccessful (18% not at all, 40% mostly).
  - 50% of the projects assessed were pilots or proofs of concept, and a further 35% were "Stage One" early deployments.
  - https://www.iot-now.com/2020/02/05/101076-iot-projects-fail/ ; https://www.iot-now.com/wp-content/uploads/IoT-Now-Magazines/2020-Q1/Why-IoT-projects-fail-v2.pdf (not fetched — blocked)
- **IoT Analytics (2024 report, survey of 100 OEMs in Q3 2023, global).**
  - Time from kick-off to first paying customer averaged 41 months in 2023, up 80% since 2020.
  - That splits into 18.5 months from kick-off to proof of concept and 22.8 months from proof of concept to the first paying customer.
  - Electrical-equipment OEMs were fastest (33 months) and automotive slowest (53 months).
  - https://iot-analytics.com/challenges-iot-product-launches-why-time-to-market-has-increased-80-percent-in-4-years/ (not fetched — blocked)
- **McKinsey via LNS Research.** LNS reports McKinsey found 56% of manufacturers stuck in pilot in 2019, rising to 74% in 2020. LNS's own survey disputes this, saying only a fraction of companies named "moving out of pilot phase" as a key challenge. https://blog.lnsresearch.com/pilot-purgatory-in-industrial-transformation-is-fake-news (not fetched — blocked)
- **Blues (vendor).** Blues cites a figure, which it attributes to McKinsey, that 74% of IoT pilots never reach production. It argues that pilots run in labs or offices miss poor signal, unreliable power and harsh environments, and that "technical success doesn't equal business viability". (vendor claim) https://blues.com/blog/iot-pilot-to-product/ (not fetched — blocked)
- **Asavie poll (2017, 79 IT professionals).** 57% expected it to take six months or more to move an IoT project from prototype to production. https://www.rfidjournal.com/?p=69878 (not fetched — blocked)
- **Founder evidence, industrial sensors.** The CEO of Arch Systems, a manufacturing sensor and analytics company, said enterprise sales cycles fell from roughly three years to about eight months as the process matured. He also noted that pilots stall and that IT and OT stakeholders must be coordinated. https://frontlines.io/podcasts/andrew-scheuermann-ceo-of-arch-systems (not fetched — blocked)
- **Founder post-mortem, retail engagement sensors (B2B).**
  - "B2B sales take time." Agencies were keen, but brand approvals and budget cycles stretched deployments out.
  - A rejected trial hurt badly. The founder wishes the team had found a trial use case built on an existing sensor instead of building a new one.
  - https://medium.com/noob-founder/my-hardware-startup-failed-in-3-years-6-lessons-i-learned-da5f8ccd7bb7 (not fetched — blocked)

### F3. Unit economics, BOM and COGS, and burn
- **Gross margin rule of thumb.** "You want to make at least a 50% gross margin on the sale of your device." The exception is when recurring service revenue carries the economics, as Kindle's book sales do. https://learn.adafruit.com/how-to-build-a-hardware-startup/pricing-your-product (not fetched — blocked)
- **Direct sales versus retail.** A 50–60% margin is "a good rule of thumb when selling direct"; retail needs much more. https://www.entrepreneur.com/starting-a-business/from-prototype-to-production-3-things-you-need-to-know/292145 (not fetched — blocked)
- **Burn and thin funding.** CB Insights:
  - high burn rate is the second-ranked reason;
  - Pearl Automation's CEO said the company "ran out of money";
  - the median crowdfunding raise among the failed companies was about $210,000.
  - https://www.cbinsights.com/research/report/hardware-startups-failure-success/ (not fetched — blocked)
- **Tooling cost before the first sale (retail sensor startup).**
  - The mould for a single sensor enclosure cost $8,000–12,000.
  - Trial enclosures were 3D-printed at about $40 each, while the PCB inside cost about $1.
  - https://medium.com/noob-founder/my-hardware-startup-failed-in-3-years-6-lessons-i-learned-da5f8ccd7bb7 (not fetched — blocked)
- **Scale of losses at a network operator.**
  - UnaBiz said Sigfox was losing around $54m in 2021, cut to around $20m in 2022 (company-reported). https://www.rcrwireless.com/20221207/carriers/we-did-what-we-said-unabiz-on-six-months-of-sigfox-plus-new-funds-big-plans (not fetched — blocked)
  - Sigfox's US network arm went bankrupt with $150m of unsecured debt. https://www.rcrwireless.com/20220404/internet-of-things/sigfoxs-american-dream-dies-in-bankruptcy-and-150m-of-debt-as-french-sale-closes (not fetched — blocked)
- **Agtech sensor and data platform (Canada).**
  - Fairfax offered 25 cents a share to take Farmers Edge private, about 99% below its $17 IPO price of March 2021. https://www.bnnbloomberg.ca/fairfax-offers-to-take-agritech-firm-farmers-edge-private-at-99-below-ipo-price-1.2000058 (not fetched — blocked)
  - CIBC analysts said they were "concerned about the long-term viability of the company", and Fairfax had extended a $75m credit facility. https://www.theglobeandmail.com/business/article-farmers-edge-in-go-private-talks-for-tiny-fraction-of-ipo-price (not fetched — blocked)
- **Smart-building hardware (US).** View Inc., a smart-glass maker, filed for Chapter 11 in April 2024 with about $359m of debt. https://law360.com/bankruptcy-authority/articles/1820661 ; https://therealdeal.com/national/2024/04/03/smart-glass-startup-view-to-declare-bankruptcy (not fetched — blocked)

### F4. Certification and manufacturing pain
- **Late delivery is the norm in crowdfunded hardware (global).**
  - "75% of Tech Projects Funded on Kickstarter Don't Finish on Time" (Mollick's research): only about a quarter delivered on time, with an average delay of 2.4 months. https://brainstation.io/magazine/75-of-tech-projects-funded-on-kickstarter-dont-finish-on-time (not fetched — blocked)
  - Of 144 successfully funded technology campaigns, "no more than 32% … managed to deliver the crowdfunded products on time". https://www.cambridge.org/core/journals/design-science/article/identifying-challenges-in-crowdfunded-product-development-a-review-of-kickstarter-projects/F2659234936B8349EAF5AFCFBA2199E8 (not fetched — blocked)
  - Outright failure to deliver was about 9% (range 5–14%). https://repository.upenn.edu/mgmt_papers/210 (not fetched — blocked)
- **Cellular certification is a gate to market (US).**
  - Several North American mobile operators and MVNOs make PTCRB certification a prerequisite for using their networks. https://www.ptcrb.com/wp-content/uploads/2021/12/10_Steps_to_PTCRB_Cert_for_Cell_Enabled_IoT_Devices-V2.pdf (not fetched — blocked)
  - AT&T requires devices to be FCC and PTCRB certified. https://www.business.att.com/content/dam/attbusiness/briefs/att-global-device-certification-brief.pdf (not fetched — blocked)
- **Certification cost and time (US, indicative).**
  - A Hologram community estimate: FCC testing "$2–10k", PTCRB end-device certification "~$10–20k", with carrier costs extra. https://community.hologram.io/t/cheapest-module/2018 (not fetched — blocked)
  - A vendor guide: about $20,000–30,000 for PTCRB plus one carrier certification, over 6–8 weeks, using a pre-certified module (vendor claim). https://hubble.com/community/comparisons/the-true-cost-of-cellular-iot/ (not fetched — blocked)
  - Quectel: certification "can take up to six months" if a device maker goes directly to certification or carrier organisations (vendor claim). https://www.quectel.com/?p=64723 (not fetched — blocked)
- **New EU cybersecurity gate (EU).**
  - Delegated Regulation (EU) 2022/30 under the Radio Equipment Directive applies from 1 August 2025. It covers internet-connected radio equipment, equipment that processes personal data, and equipment that enables monetary transactions.
  - The EN 18031-1, -2 and -3 harmonised standards are the usual route to showing conformity.
  - https://www.tuvsud.com/en-us/services/product-certification/red-cybersecurity-requirements ; https://blog.qima.com/certification/how-red-shapes-cybersecurity-requirements-for-wireless-products (not fetched — blocked)
- **Regulation lengthens launches.** IoT Analytics partly attributes longer time-to-market to OEMs working through security and regulatory hurdles. https://iot-analytics.com/challenges-iot-product-launches-why-time-to-market-has-increased-80-percent-in-4-years/ (not fetched — blocked)

### F5. Connectivity choices and their failure modes
- **Cellular sunset, US 3G (2022).**
  - CE Pro coverage gave estimates of more than 10 million alarm systems at risk, and later of around 2 million radio upgrades still to complete (per the AICC).
  - A truck roll could cost a dealer up to $200, plus $50–100 for new hardware.
  - AT&T agreed a roaming bridge with T-Mobile that extended 3G for alarm companies only to July 1. The AICC called this "a partial solution at best".
  - The figures came from several CE Pro articles in one domain-restricted result set; candidate pages: https://www.cepro.com/networking/cellular/how-the-security-industry-is-pressuring-att-to-postpone-3g-sunset/ ; https://www.cepro.com/news/cellbounce_3g_cdma_sunset_security_alarm_industry_diy_no_truck_roll/8838/ (not fetched — blocked)
- **Fleets (US).** About 7.5 million 3G-based IoT devices were still in fleet use, according to SmartDrive's CEO. Most embedded systems "are not easily retrofitted to new radios", so they had to be replaced outright. https://www.ccjdigital.com/business/article/14937916/will-the-end-of-3g-cellular-be-more-disruptive-to-fleets-than-eld-mandate (not fetched — blocked)
- **Cellular sunset, UK 2G and 3G.**
  - Ofcom lists telecare, fire and security alarms, smart meters, telemetry and tracker devices, parking meters and bus ticketing machines as at risk. It says "all 2G and 3G devices will need to be upgraded to at least 4G", and that EE will begin switching off 2G from May 2029. https://www.ofcom.org.uk/phones-telecoms-and-internet/information-for-industry/policy/2g-and-3g-switch-off/advice-for-iot-and-third-party-device-suppliers (not fetched — blocked)
  - VodafoneThree will switch off the Vodafone 2G network in spring 2030. https://www.vodafone.co.uk/newscentre/smart-living/everything-you-need-to-know-about/vodafonethree-2g-switch-off/ (not fetched — blocked)
  - The government's 2G Switch-off Charter (24 March 2026) records that all mobile operators have committed to switching off 2G by 2033 at the latest. https://www.gov.uk/government/publications/2g-switch-off-charter/2g-switch-off-charter (not fetched — blocked)
- **Proprietary low-power network operator risk (France, US, global).**
  - Sigfox went into receivership. UnaBiz was appointed new owner of Sigfox SA and Sigfox France SAS by the Commercial Court of Toulouse in April 2022. https://www.telecomtv.com/content/telco-and-csp/unabiz-appointed-as-new-owner-of-sigfox-sa-and-sigfox-france-sas-under-receivership-proceeding-by-the-commercial-court-of-toulouse-44247/ (not fetched — blocked)
  - In September 2025, UnaBiz's French units filed twice with the same court for judicial reorganisation, over about €5m of debt mostly inherited from unpaid tower rents. https://rcrwireless.com/20250909/internet-of-things/sigfox-unabiz-court (not fetched — blocked)
- **NB-IoT and LTE-M gaps.**
  - Of networks supporting LTE-M, "a little over half" support the PSM power-saving mode and "fewer than half" support eDRX. Most operators deploy LTE-M or NB-IoT, "but usually not both". https://ibasis.com/when-engaging-in-a-cellular-iot-lpwa-deployment-part-2/ (not fetched — blocked)
  - NB-IoT roaming "is currently limited" (vendor). https://emnify.com/nb-iot-coverage (not fetched — blocked)
  - A device in PSM or eDRX mode cannot be contacted from the network side. https://www.rcrwireless.com/20211028/fundamentals/roaming-billing-provisioning-10-key-nb-iot-challenges-1-5 (not fetched — blocked)
- **LoRaWAN field failure modes.**
  - Known causes of loss in an uplink-only network are duty-cycle limits, collisions, insufficient coverage, and saturation of the gateway's demodulation paths. Adding gateways helps only when they are spaced apart. https://eprints.gla.ac.uk/251066 (not fetched — blocked)
  - Kerlink (vendor): installation practices such as gateway height, cabling losses and radio interference cause many field coverage gaps. A planning study cut a UK smart-metering design from 36 to 27 gateways. https://www.kerlink.com/blog/2026/08/04/optimising-lorawan-coverage-best-practices-and-radio-planning/ (not fetched — blocked)
  - A Things Network forum user traced packet loss to one gateway going offline after its cellular SIM ran out of credit (anecdotal). https://www.thethingsnetwork.org/forum/t/packet-loss-when-multiple-gateways-used/27620 (not fetched — blocked)
- **Coverage sinks whole projects (Beecham).** All respondents named connectivity (coverage, reliability, bandwidth, latency) as a significant technical challenge. One logistics firm's nationwide monitoring project failed simply because of the lack of rural wireless coverage. https://www.iot-now.com/2020/02/05/101076-iot-projects-fail/ (not fetched — blocked)
- **Cloud and vendor dependence.**
  - Insteon's cloud went dark in April 2022. Hubs that were not built to run locally were left inoperable. https://www.theregister.com/2022/04/19/insteon_cloud_shutdown/ ; https://www.forrester.com/blogs/insteon-and-the-internet-of-bricks/ (not fetched — blocked)
  - After the Revolv shutdown, Particle's CEO argued that an acquirer should carry the acquired company's customers "as a liability on your books". https://betanews.com/2016/05/04/revolv-shutdown/ (not fetched — blocked)

### F6. Battery life
- **Datasheets mislead.** A UTS study found "a disparity between power consumption values in datasheets and experimental measurements, which could have significant consequences in terms of battery life in the field". https://opus.cloud1.lib.uts.edu.au/handle/10453/172967 (not fetched — blocked)
- **Cells vary.** LiSOCl2 cells with similar datasheet specifications showed "substantial discrepancies in actual performance". Lower-grade cells may self-discharge by up to 3% a year. https://epubl.ktu.edu/object/elaba:248266545 (not fetched — blocked)
- **Predictions miss deployments.** The Bristol SPHERE study compared real-world battery lifetimes against predictions made during development. https://research-information.bris.ac.uk/en/publications/on-predicting-the-battery-lifetime-of-iot-devices-experiences-fro/ (not fetched — blocked)
- **Field example (secondary source).** A sensor with a published 10-year battery specification that states no update-rate conditions lasted about 11 months at its default update rate. https://industrialmonitordirect.com/blogs/knowledgebase/banner-q45-wireless-sensor-battery-life-and-deployment-guide (not fetched — blocked)
- **Vendor claims are conditional.** Disruptive Technologies quotes up to 15 years of battery life but says it depends on usage (vendor claim). https://www.disruptive-technologies.com/sensors/temperature-sensor (not fetched — blocked)

### F7. Installation friction and field-support burden
- **Installation cost undermines ROI.** Digi says many IoT providers "are failing to factor installation costs into their business proposals, and both suppliers and customers are coming unstuck as a result". https://www.rcrwireless.com/20180518/internet-of-things/iot-installation-costs-scuppering-roi-tag40 (not fetched — blocked)
- **Truck rolls.** Truck rolls "easily cost $150 each", and they become prohibitive across dispersed sites (vendor claim). https://www.digi.com/blog/post/the-roi-of-remote-iot-device-management (not fetched — blocked)
- **Field repair.** Manually repairing a device in the field "often can exceed the cost of the device itself" (vendor claim). https://ubuntu.com/core/features/recovery (not fetched — blocked)
- **Commissioning.** "Somebody needs to calibrate the device, put it into service, and assure that it is providing accurate measurement." https://www.arcweb.com/node/52996 (not fetched — blocked)
- **No DIY path for alarms.** In the 3G sunset there was no DIY upgrade path for legacy cell-only security panels as of 2019, which forced site visits. https://www.cepro.com/news/cellbounce_3g_cdma_sunset_security_alarm_industry_diy_no_truck_roll/8838/ (not fetched — blocked)

### F8. Hardware-sale revenue traps, churn and weak recurring logic
- **Latch (US, smart-building access).**
  - In August 2022 its audit committee opened an investigation into hardware revenue booked mainly through third-party channel partners. Revenue for 2019–2021 and Q1 2022 was restated. https://www.sec.gov/Archives/edgar/data/1826000/000182600024000069/lat-20220630.htm ; https://therealdeal.com/2022/08/26/tishman-speyer-backed-latch-says-its-financial-statements-cant-be-relied-upon (not fetched — blocked)
  - Latch then missed Nasdaq's compliance deadline. https://therealdeal.com/national/2023/08/02/latch-wont-meet-deadline-for-nasdaq-compliance (not fetched — blocked)
- **SmartRent (US, Q2 2025).**
  - Revenue fell 21% and hardware revenue fell 39%. The company said this reflected its "strategic move away from bulk hardware sales not aligned with customer implementation timelines".
  - Annual recurring revenue (ARR) rose 11% to $56.9m.
  - https://www.businesswire.com/news/home/20250806932749/en/SmartRent-Reports-Second-Quarter-2025-Financial-Results (not fetched — blocked)
- **Farmers Edge.** A shareholder claim alleges the company misrepresented its farmer subscription income. The company disputes this. https://foodindustrynetwork.com/?p=66083 (not fetched — blocked)
- **IoT churn (vendor).** Zipit cites average IoT churn of about 5.88%, mostly voluntary (vendor claim; the period was not stated in the extract). https://zipitwireless.com/blog/iot-subscriber-churn-what-it-is-how-to-measure-it-and-why-it-matters (not fetched — blocked)
- **Hardware-to-software pivot.** Adero, an item-tracking startup, laid off 45% of its staff weeks after pivoting "to put more focus on building software instead of hardware". https://techcrunch.com/2019/02/08/item-tracking-startup-adero-is-laying-off-45-of-staff-just-weeks-after-it-pivoted (not fetched — blocked)

## What survivors had in common

### S1. Hardware bundled into multi-year subscriptions, with high gross margin and expansion revenue
- **Samsara (US, connected operations).**
  - GAAP gross margin moved from 59.6% to 69.8% between S-1 periods, which Tunguz calls "impressive for a business providing hardware". https://tomtunguz.com/samsara-s-1/ (not fetched — blocked)
  - Dollar-based net retention was above 115% as of 30 October 2021, and above 125% for customers with more than $100,000 of ARR. https://www.sec.gov/Archives/edgar/data/1642896/000119312521334578/d261594ds1.htm (not fetched — blocked)
  - Contracts are "typically for a subscription term of three to five years". https://www.sec.gov/Archives/edgar/data/1642896/000164289622000016/samsaraform10-kxq42022.htm (not fetched — blocked)
  - Samsara gives a hardware warranty for the entire subscription term. https://www.sec.gov/Archives/edgar/data/1642896/000162828026039507/iot2026ars.pdf (not fetched — blocked)
- **Augury (industrial machine health).**
  - Sells "Machine Health as a Service": sensors, connectivity, software and expert services under one subscription (secondary source). https://businessmodelcanvastemplate.com/blogs/how-it-works/augury-how-it-works (not fetched — blocked)
  - Added an AI warranty ("Guaranteed Diagnostics") with Munich Re. https://www.techtarget.com/ai/news/252484554/Predictive-maintenance-vendor-launches-AI-warranty (not fetched — blocked)
- **Controlant (pharma cold chain, global).** Sells real-time IoT data loggers, a cloud platform, and round-the-clock monitoring and response. Its 2023 AGM release is titled around revenue doubling (title only seen). https://www.controlant.com/insights/two-years-safeguarding-the-pfizer-biontech-covid-19-vaccine ; https://www.controlant.com/insights/controlant-agm-2023-revenue-doubled-and-continued-growth-ahead (not fetched — blocked)
- **HACCP sensors on rental (EU).**
  - Octopus HACCP rents sensors at about €6 a month, plus a hub at €12 a month excluding tax (vendor price). https://octopus-haccp.com/?p=18130 (not fetched — blocked)
  - Digi's restaurant system is sold as a subscription with hardware and software included. https://fruitgrowersnews.com/?p=10874 (not fetched — blocked)
- **IoT Analytics OEM survey.**
  - "Upselling software/services based on actual product usage" succeeded for 90% of those who tried it (60 of 67).
  - Among successful companies (amortisation in 24 months or less), 61% said workflow optimisation was crucial or high-value, against 21% at less successful firms.
  - Performance guarantees had a 59% success rate but carry more risk.
  - I could not isolate which of these two IoT Analytics pages carries these figures: https://iot-analytics.com/product/iot-commercialization-business-model-adoption-report-2024/ ; https://iot-analytics.com/how-to-create-a-successful-iot-business-model-insights-from-early-innovators/ (not fetched — blocked)

### S2. Selling through a party that already holds the risk, the budget or the site visit
- **Insurer channel, electrical fire (US).**
  - State Farm gives eligible customers a free Ting sensor and pays the annual service fee for three years. Whisker Labs adds a $1,000 credit toward remediation. https://newsroom.statefarm.com/state-farm-ting-electrical-fire/ (not fetched — blocked)
  - At the time of the expansion announcement, nearly 700,000 State Farm homes had a sensor, with 50,000 more a month and a target of 2 million homes. Eligibility requires a smartphone and home Wi-Fi, so it is self-installed. https://newsroom.statefarm.com/state-farm-expands-ting-fire-safety-program-to-2-million-homes/ (not fetched — blocked)
  - State Farm Ventures led Whisker Labs' funding round, so the insurer is also an investor. https://newsroom.statefarm.com/whisker-labs/ (not fetched — blocked)
- **Insurer channel, water leaks (UK, Denmark, US).**
  - Aviva began offering HomeServe's LeakBot in October 2016. https://www.aviva.com/newsroom/news-releases/2016/10/uk-homeserve-partners-with-aviva-to-offer-smart-water-leak-detector-leakbot-to-customers-17683/ (not fetched — blocked)
  - Legal & General became the third major insurer in 2017. https://www.expressandstar.com/business/legal-general-strikes-leakbot-deal-with-homeserve-6264616 (not fetched — blocked)
  - Covéa offered it through brokers. https://insurancebusinessmag.com/uk/news/home-property/covea-and-leakbot-partnership-offers-a-first-for-brokers-91063.aspx (not fetched — blocked)
  - Topdanmark subsidises a plumber visit when a leak is detected. https://insurancebusinessmag.com/uk/news/property-insurance/topdanmark-partners-with-leakbot-174055.aspx (not fetched — blocked)
  - The US launch framed water leaks as "the largest predictable home insurance claim category". https://coverager.com/leakbot-connected-device-enters-us-market-prevent-major-damage-household-water-leaks-largest-predictable-home-insurance-claim-category/ (not fetched — blocked)
  - The device clips onto the main water pipe and flags abnormal flow from temperature-differential changes during low-usage periods. https://www.computerweekly.com/news/450422417/Legal-General-picks-HomeServes-IoT-LeakBot-to-protect-homeowners (not fetched — blocked)
- **Equipment maker channel.** Augury expanded its collaboration with Carrier to add machine health to Carrier's BluEdge service offering. https://www.augury.com/media-center/press/augury-expands-collaboration-with-carrier-to-add-machine-health-capabilities/ (not fetched — blocked)
- **Materials supplier channel (Canada, US).**
  - Through the SmartRock Plus programme, ready-mix producers offer Giatec's sensors to contractors as a value-added service. https://www.newswire.com/news/giatecs-smartrock-plus-program-signs-new-technology-forward-producer-21180158 ; https://www.casestudies.com/company/giatec/case-study/stoneway-concrete-customer-case-study (not fetched — blocked)
  - Giatec faced early pushback from "old-school" concrete veterans. https://www.on-sitemag.com/features/ottawa-tech-firm-takes-on-primitive-concrete-testing/ (not fetched — blocked)
- **Reseller and distributor channel (US).**
  - Monnit built a partner programme for value-added resellers, system integrators and OEMs, including private-label options. https://www.fierceelectronics.com/components/monnit-creates-partner-program-for-resellers-and-oems-to-capitalize-iot (not fetched — blocked)
  - It reports 72,000+ customers in 85+ countries over 15 years (company claim). https://www.monnit.com/blog/time-to-celebrate-monnits-15th-anniversary/ (not fetched — blocked)
- **Connecting products you already sell (McKinsey, 2018).** In a survey of 300 IoT practitioners at companies with more than $500m revenue, leaders were nearly three times more likely than laggards to add IoT connectivity to existing products they sell. They also implemented 80% more IoT applications. https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/McKinsey%20Digital/Our%20Insights/What%20separates%20leaders%20from%20laggards%20in%20the%20Internet%20of%20Things/What-separates-leaders-from-laggards-in-the-Internet-of-Things-vF.pdf (not fetched — blocked)
- **Service presence as a moat.** B2B hardware "usually requires local sales and service teams", which makes it harder for foreign competitors to copy. https://cdixon.org/2013/04/30/hardware-startups/ (not fetched — blocked)

### S3. A must-have loss or compliance duty, with an obvious payer
- **Electrical fire (US).** Ting reportedly mitigated more than 500 potential home fires in 2022 (State Farm and Whisker Labs data; not independently verified). https://www.propertycasualty360.com/2024/04/24/state-farms-ting-fire-monitor-detected-and-mitigated-over-500-fires-in-2022/ (not fetched — blocked)
- **Pharma cold chain (global).** Pfizer's vaccine needed about −70°C. Controlant says it helped deliver more than 5.7 billion doses to over 185 countries (company claim). https://www.controlant.com/insights/two-years-safeguarding-the-pfizer-biontech-covid-19-vaccine (not fetched — blocked)
- **Food-safety records (UK).** The UK hospitality trade body publishes guidance on digital HACCP and wireless temperature monitoring. https://www.ukhospitality.org.uk/digital-haccp-wireless-temperature-monitoring/ (not fetched — blocked)
- **Livestock water (Australia).** Farmbot's tank sensor measures water pressure and reports over 3G/4G or satellite. A South Australian government agtech listing describes it and offers a 3-year cost comparison. https://pir.sa.gov.au/research/agtech/find_solutions/products/farmbot-tank-monitor (not fetched — blocked)
- **Waste collection (US).** RoadRunner bought Compology for its camera-based dumpster metering, a capability RoadRunner said it lacked. https://www.waste360.com/mergers-acquisitions/roadrunner-recycling-acquires-compology (not fetched — blocked)

### S4. Low-friction installation and multiple or robust networks
- **Self-install examples.**
  - Ting plugs in at home over Wi-Fi. https://newsroom.statefarm.com/state-farm-expands-ting-fire-safety-program-to-2-million-homes/ (not fetched — blocked)
  - LeakBot clips onto a pipe. https://www.computerweekly.com/news/450422417/Legal-General-picks-HomeServes-IoT-LeakBot-to-protect-homeowners (not fetched — blocked)
  - ComplianceMate describes its system as "self-install / plug-and-play". https://www.compliancemate.com/frequently-asked-questions (not fetched — blocked)
- **Fallback networks.**
  - Farmbot offers cellular or satellite. https://pir.sa.gov.au/research/agtech/find_solutions/products/farmbot-tank-monitor (not fetched — blocked)
  - Vodafone says most IoT and M2M devices are already compatible with 4G, 5G, NB-IoT or LTE-M. https://www.vodafone.co.uk/newscentre/smart-living/everything-you-need-to-know-about/vodafonethree-2g-switch-off/ (not fetched — blocked)
- **Local operation limits the damage.** When Insteon's cloud went down, physical switches and the local radio mesh kept working; hubs built only for the cloud failed. https://www.theregister.com/2022/04/19/insteon_cloud_shutdown/ (not fetched — blocked)

### S5. "Survival" often meant being absorbed by the channel owner
- **Compology.** Acquired by RoadRunner in October 2022; terms not disclosed. https://www.wastedive.com/news/roadrunner-recycling-compology-acquisition-ai-technology/633392/ (not fetched — blocked)
- **Enevo.**
  - Its US waste-service accounts went to RTS in 2020, with Enevo continuing to supply the sensors. https://www.wastedive.com/news/recycle-track-systems-rts-acquires-enevo-us-accounts/579670/ (not fetched — blocked)
  - REEN, a fleet-telematics venture of ABAX, then acquired the Enevo group. https://www.abax.com/en-gb/newsroom/the-abax-venture-company-reen-acquires-enevo-group-c3363064 (not fetched — blocked)

## Named examples

| Company | Segment | Outcome | Lesson | Source |
|---|---|---|---|---|
| Sigfox | Proprietary low-power network (France, US) | Receivership in 2022; US arm bankrupt with $150m debt; owner's French units back in court in 2025 | Building on one proprietary network is a supplier-continuity risk | https://www.telecomtv.com/content/telco-and-csp/unabiz-appointed-as-new-owner-of-sigfox-sa-and-sigfox-france-sas-under-receivership-proceeding-by-the-commercial-court-of-toulouse-44247/ ; https://rcrwireless.com/20250909/internet-of-things/sigfox-unabiz-court |
| Latch | Smart-building access (US) | Hardware and channel revenue restated; delisted from Nasdaq | Hardware sold into a channel is not the same as installed use | https://www.sec.gov/Archives/edgar/data/1826000/000182600024000069/lat-20220630.htm |
| SmartRent | Rental-property IoT (US) | Hardware revenue −39% in Q2 2025 while pivoting to ARR | Bulk hardware sales get ahead of installation | https://www.businesswire.com/news/home/20250806932749/en/SmartRent-Reports-Second-Quarter-2025-Financial-Results |
| View Inc. | Smart glass (US) | Chapter 11 in April 2024 with about $359m debt | Capital-heavy building hardware | https://law360.com/bankruptcy-authority/articles/1820661 |
| Farmers Edge | Agtech sensors and data (Canada) | Taken private about 99% below its IPO price | Farm sensor economics are weak below large acreage | https://www.bnnbloomberg.ca/fairfax-offers-to-take-agritech-firm-farmers-edge-private-at-99-below-ipo-price-1.2000058 |
| Enevo | Waste bin fill sensors (Finland, US) | Exited waste services; sold to REEN | Moving into services did not save the economics; the channel owner absorbed it | https://www.wastedive.com/news/recycle-track-systems-rts-acquires-enevo-us-accounts/579670/ |
| Insteon | Home automation (US) | Cloud shut down without notice in 2022 | Customers fear a vendor's cloud dying | https://www.theregister.com/2022/04/19/insteon_cloud_shutdown/ |
| Retail engagement sensor startup (founder: Sahan De Silva) | Retail B2B sensors | Failed within 3 years | Tooling cost, slow B2B approvals, a failed trial | https://medium.com/noob-founder/my-hardware-startup-failed-in-3-years-6-lessons-i-learned-da5f8ccd7bb7 |
| Adero | Item trackers (US) | 45% layoffs after pivoting to software | Hardware-heavy model abandoned | https://techcrunch.com/2019/02/08/item-tracking-startup-adero-is-laying-off-45-of-staff-just-weeks-after-it-pivoted |
| Pearl Automation | Consumer car camera (US) | "Ran out of money" | Burn rate | https://www.cbinsights.com/research/report/hardware-startups-failure-success/ |
| Helium | Enterprise sensors (2015: smart refrigeration for hospitals and food), then a token-incentivised network | Pivoted; parent Nova Labs cut 36% of staff in 2024 | Enterprise sensor business abandoned | https://www.eweek.com/networking/startup-helium-systems-offers-iot-platform-for-enterprises/ ; https://blockworks.com/news/helium-parent-company-layoffs |
| Samsara | Fleet and operations IoT (US) | Public; net retention >115%; gross margin about 70% | Bundled subscription, expansion revenue | https://tomtunguz.com/samsara-s-1/ |
| Whisker Labs (Ting) | Electrical fire sensor (US) | Rolled out to State Farm policyholders, targeting 2 million homes | Insurer pays and distributes | https://newsroom.statefarm.com/state-farm-expands-ting-fire-safety-program-to-2-million-homes/ |
| HomeServe LeakBot | Water leak sensor (UK, Denmark, US) | Multiple insurer partners since 2016 | Insurer channel plus repair network | https://www.aviva.com/newsroom/news-releases/2016/10/uk-homeserve-partners-with-aviva-to-offer-smart-water-leak-detector-leakbot-to-customers-17683/ |
| Augury | Industrial machine health | Subscription with an insured guarantee; Carrier channel | Outcome-based subscription through an equipment maker | https://www.augury.com/media-center/press/augury-expands-collaboration-with-carrier-to-add-machine-health-capabilities/ |
| Controlant | Pharma cold chain (Iceland, global) | Pfizer vaccine logistics; revenue doubled per its 2023 AGM title | Compliance-critical, monitored service | https://www.controlant.com/insights/two-years-safeguarding-the-pfizer-biontech-covid-19-vaccine |
| Giatec | Concrete curing and strength sensors (Canada) | Growth via ready-mix producers | Niche plus supplier channel | https://www.newswire.com/news/giatecs-smartrock-plus-program-signs-new-technology-forward-producer-21180158 |
| Monnit | General wireless sensors (US) | 15 years trading; 72,000+ customers (company claim) | Reseller and distributor channel | https://www.monnit.com/blog/time-to-celebrate-monnits-15th-anniversary/ |
| Farmbot | Livestock water monitoring (Australia, US) | Raised $4.6m to expand in the US as Ranchbot | Replaces a costly manual task (water runs); satellite fallback | https://www.agriculturedive.com/news/australia-based-startup-farmbot-raises-funding-us-expansion/719109/ |
| Compology | Dumpster fill cameras (US) | Acquired by RoadRunner in 2022 | Exit to the channel owner | https://www.waste360.com/mergers-acquisitions/roadrunner-recycling-acquires-compology |

## Searched for but not found
- **Direct page fetches.** Every WebFetch was blocked by the session's egress policy: cbinsights.com, ciodive.com, venturebeat.com and mckinsey.com failed, and the proxy log shows other researchers' wikipedia.org and tech.eu fetches refused. I stopped trying further hosts. No page in this file was opened directly.
- **McKinsey's "84% stuck in pilot" figure (2018).** It is widely repeated, but I could not find it in McKinsey's own text.
- **CB Insights' "97% of consumer hardware startups fail or fizzle".** One extract attributed this to CB Insights; another found no primary source. Unconfirmed, so not used as a finding.
- **A B2B-specific (rather than consumer) hardware failure-rate statistic.** CB Insights' hardware study covers consumer hardware.
- **Independent truck-roll or installation-cost benchmarks.** One vendor glossary itself says no verified industry benchmark exists.
- **An independent multi-device study comparing field battery life with datasheet claims.**
- **Independent B2B IoT churn benchmarks.** Only vendor blogs (Zipit, LanPDT) were found.
- **Monnit's funding history or profitability.**
- **Everactive layoffs or shutdown.** No reports found.
- **Density layoffs or pivot.** No reports found.
- **The date of Helium's pivot from sensors to network.** Not found.
- **LeakBot's connectivity.** One search extract said it "runs off the SIGFOX" network, but Computer Weekly describes a SIM card. Unresolved, so Sigfox dependence is not asserted.
- **Prices for SmartSense (Digi) and ComplianceMate.** Not found.
- **Samsara's hardware versus subscription revenue split.** Not found.
- **Independent verification of State Farm and Whisker Labs fire-prevention figures.** Not found.
- **Independent estimates of EU RED or EN 18031 compliance cost.** Not found.
- **A primary source for Enevo Oy's bankruptcy.** Only a Wikipedia extract, which was blocked and is not cited.
- **The failure taxonomy in arXiv 2206.13560 ("Reflecting on Recurring Failures in IoT Development").** The categories were not visible in the extract.

## Queries run
1. CB Insights hardware startup failure post-mortems reasons
2. Cisco survey 60% IoT initiatives stall proof of concept 26% complete success
3. McKinsey IoT "pilot purgatory" percentage of companies
4. Microsoft IoT Signals report proof of concept failure rate cost of scaling
5. Why hardware startups fail lack of consumer demand high burn rate report [cbinsights.com]
6. Cisco IoT projects stall proof of concept survey 2017 [computing.co.uk] (no relevant hit)
7. Microsoft IoT Signals 30% projects fail proof of concept [themanufacturer.com]
8. Beecham Research why IoT projects fail survey percentage
9. Beecham Why IoT projects fail 58% unsuccessful connectivity coverage [iot-now.com]
10. hardware startup gross margin BOM cost retail price markup rule of thumb
11. cellular IoT device certification cost PTCRB carrier certification FCC CE cost time
12. 3G sunset IoT devices stranded alarm panels telematics AT&T shutdown 2022 replacement cost
13. Sigfox receivership 2022 UnaBiz acquisition why Sigfox failed IoT network
14. LoRaWAN deployment problems coverage gateways packet loss field experience lessons learned
15. IoT sensor battery life field vs datasheet shorter than expected study
16. average truck roll cost field service visit IoT device installation
17. Samsara S-1 gross margin net dollar retention IoT hardware subscription model
18. Helium pivot enterprise IoT sensors to network layoffs 2019 why
19. Enevo waste sensor company bankruptcy
20. LeakBot HomeServe insurers distribution leak detection water claims partnership
21. Whisker Labs Ting sensor insurers State Farm free to policyholders electrical fires prevented
22. Latch smart lock company delisted restatement hardware revenue problems
23. Mollick Kickstarter study hardware projects delivered late percentage
24. Bain IoT survey customers barriers security integration ROI enterprise buyers
25. Compology waste dumpster camera sensors acquired Roadrunner 2023
26. View Inc smart glass Chapter 11 bankruptcy 2024 losses
27. Everactive batteryless sensors layoffs shut down
28. Augury machine health subscription business model customers outcome guarantee
29. Blues Wireless pilot purgatory why IoT projects never reach production [blues.com]
30. industrial IoT sales cycle length months enterprise sensor startup long sales cycle
31. IoT startup post-mortem "shutting down" sensor company lessons learned founder blog B2B
32. hardware as a service IoT subscription churn nice to have vs must have sensor startup investor essay
33. "My hardware product failed within 3 years" retail sensor lessons trial mold cost [medium.com]
34. Controlant pharma cold chain real-time loggers COVID vaccine Pfizer revenue growth layoffs
35. Farmers Edge losses delisted Fairfax take private agtech sensors weather stations
36. Monnit wireless sensors company history bootstrapped profitable channel partners resellers
37. restaurant food safety wireless temperature monitoring HACCP compliance sensors SmartSense ComplianceMate subscription price
38. EU Radio Equipment Directive delegated act cybersecurity August 2025 IoT devices EN 18031 compliance burden
39. NB-IoT LTE-M roaming availability problems PSM eDRX carrier support IoT deployment failure
40. Insteon shutdown 2022 cloud servers devices stopped working company collapse
41. Cisco survey three quarters IoT projects failing human factors 1,845 [intelligentcio.com]
42. leaders and laggards Internet of Things pilots scale survey [mckinsey.com]
43. Samsara S-1 hardware revenue recognized subscription term net retention 115% [tomtunguz.com, sec.gov]
44. Sigfox losing money a year UnaBiz identity crisis 3G sunset Sigfox network [rcrwireless.com]
45. Giatec SmartRock concrete sensors growth customers niche success
46. Farmbot Monitoring Solutions livestock water tank monitoring growth farmers subscription Australia
47. agricultural sensor adoption barriers farmers study abandoned soil moisture sensors cost complexity
48. alarm industry 4 million alarm panels AT&T 3G sunset truck roll [cepro.com]
49. Density people counting sensor startup layoffs pivot hardware cost depth sensor
50. SmartRent hardware revenue decline shift to SaaS recurring revenue CEO ousted 2024 2025
51. IoT device fleet support burden field failures returns RMA cost connected products remote management
52. IoT installation cost exceeds hardware cost self-install sensors deployment labor commissioning
53. Digi IoT installation costs scuppering ROI hurting suppliers and customers [rcrwireless.com]
54. Enevo restructuring exits waste services focus technology bankruptcy Reen acquires [wastedive.com, recyclingtoday.com, waste360.com, reen.com, abax.com]
55. hardware startups "painkiller" "vitamin" B2B sensors investor advice must-have
56. UK 2G 3G switch off IoT devices smart meters telecare alarms risk 2033 Vodafone EE
57. Reflecting on Recurring Failures in IoT Development arxiv failure categories [arxiv.org]
58. Disruptive Technologies sensor lifetime battery years transmission frequency [disruptive-technologies.com]
59. IoT Analytics time to market connected product launch months escalates 80% [iotdesignpro.com, iot-analytics.com]
60. how to create a successful IoT business model insights from early innovators recurring revenue share [iot-analytics.com]
61. Kerlink LoRaWAN coverage map dead zones after sensors installed radio planning gateways [kerlink.com]
62. LeakBot Sigfox network HomeServe Legal & General leak detector [computerweekly.com, iot-now.com]
63. State Farm Ting sensors homes enrolled per month expansion two million [newsroom.statefarm.com, propertycasualty360.com]

## Sources
All sources were seen as search-result extracts only (not fetched — blocked).
1. https://www.cbinsights.com/research/report/hardware-startups-failure-success/ — CB Insights, "Why Do So Many Hardware Startups Fail?"
2. https://www.cbinsights.com/reports/CB-Insights_Hardware-Startups-Fail.pdf — CB Insights, "The Top 9 Reasons Hardware Startups Fail"
3. https://www.cbinsights.com/reports/The-20-Reasons-Startups-Fail.pdf — CB Insights, "The Top 20 Reasons Startups Fail" (2019)
4. https://www.talentica.com/wp-content/uploads/2024/02/The-20-Reasons-Startups-Fail.pdf — mirror of source 3
5. https://www.themanufacturer.com/articles/30-iot-projects-fail-proof-concept-stage/ — The Manufacturer, Microsoft IoT Signals coverage
6. https://venturebeat.com/security/microsoft-30-of-iot-projects-fail-in-the-proof-of-concept-stage — VentureBeat (2019)
7. https://rcrwireless.com/20190731/internet-of-things/microsoft-report-enterprise-iot-adoption — RCR Wireless (31 July 2019)
8. https://integrationcms.bain.com/contentassets/5aa3a678438846289af59f62e62a3456/bain_brief_unlocking_opportunities_in_the_internet_of_things.pdf — Bain brief, "Unlocking Opportunities in the Internet of Things" (2018)
9. https://www.bain.com/about/media-center/press-releases/2018/bain-predicts-the-iot-market-will-more-than-double-by-2021/ — Bain press release (2018)
10. https://arxiv.org/pdf/1912.12382 — arXiv, "RF Soil Moisture Sensing via Radar Backscatter Tags"
11. https://www.electronicspecifier.com/news/analysis/price-challenges-block-agricultural-sensor-adoption — Electronic Specifier, Lux Research analysis
12. https://striplingpark.caes.uga.edu/research/sfy2018-regional-water-plan-seed-grant/conclusions.html — University of Georgia, Stripling Park conclusions
13. https://www.holloway.com/g/angel-investing/sections/evaluating-the-idea — Holloway Guide to Angel Investing
14. https://www.intelligentcio.com/me/2017/05/30/cisco-survey-reveals-close-to-three-quarters-of-internet-of-things-projects-are-failing/ — Intelligent CIO (30 May 2017)
15. https://www.ciodive.com/news/cisco-more-than-half-of-enterprise-iot-projects-unsuccessful/444824/ — CIO Dive (2017)
16. https://www.telecomtv.com/content/iot/cisco-survey-reveals-close-to-three-fourths-of-iot-projects-are-failing-26983/amp/ — TelecomTV (2017)
17. https://www.iot-now.com/2020/02/05/101076-iot-projects-fail/ — IoT Now, "Why do IoT projects fail?" (5 February 2020)
18. https://www.iot-now.com/wp-content/uploads/IoT-Now-Magazines/2020-Q1/Why-IoT-projects-fail-v2.pdf — IoT Now / Beecham Research, Q1 2020
19. https://iot-analytics.com/challenges-iot-product-launches-why-time-to-market-has-increased-80-percent-in-4-years/ — IoT Analytics (2024)
20. https://blog.lnsresearch.com/pilot-purgatory-in-industrial-transformation-is-fake-news — LNS Research blog
21. https://blues.com/blog/iot-pilot-to-product/ — Blues, "IoT Pilot to Production" (vendor)
22. https://www.rfidjournal.com/?p=69878 — RFID Journal, Asavie poll (2017)
23. https://frontlines.io/podcasts/andrew-scheuermann-ceo-of-arch-systems — Frontlines podcast, Arch Systems CEO
24. https://medium.com/noob-founder/my-hardware-startup-failed-in-3-years-6-lessons-i-learned-da5f8ccd7bb7 — Sahan De Silva, "My hardware startup failed within 3 years. 6 lessons I learned"
25. https://learn.adafruit.com/how-to-build-a-hardware-startup/pricing-your-product — Adafruit, "How to build a hardware startup: pricing your product"
26. https://www.entrepreneur.com/starting-a-business/from-prototype-to-production-3-things-you-need-to-know/292145 — Entrepreneur
27. https://www.rcrwireless.com/20221207/carriers/we-did-what-we-said-unabiz-on-six-months-of-sigfox-plus-new-funds-big-plans — RCR Wireless (7 December 2022)
28. https://www.rcrwireless.com/20220404/internet-of-things/sigfoxs-american-dream-dies-in-bankruptcy-and-150m-of-debt-as-french-sale-closes — RCR Wireless (4 April 2022)
29. https://www.bnnbloomberg.ca/fairfax-offers-to-take-agritech-firm-farmers-edge-private-at-99-below-ipo-price-1.2000058 — BNN Bloomberg (17 November 2023)
30. https://www.theglobeandmail.com/business/article-farmers-edge-in-go-private-talks-for-tiny-fraction-of-ipo-price — The Globe and Mail
31. https://law360.com/bankruptcy-authority/articles/1820661 — Law360, "Window-Shading Co. View Inc. Hits Ch. 11 With $359M Debt" (2024)
32. https://therealdeal.com/national/2024/04/03/smart-glass-startup-view-to-declare-bankruptcy — The Real Deal (3 April 2024)
33. https://brainstation.io/magazine/75-of-tech-projects-funded-on-kickstarter-dont-finish-on-time — BrainStation, summary of Mollick's research
34. https://www.cambridge.org/core/journals/design-science/article/identifying-challenges-in-crowdfunded-product-development-a-review-of-kickstarter-projects/F2659234936B8349EAF5AFCFBA2199E8 — Design Science (Cambridge)
35. https://repository.upenn.edu/mgmt_papers/210 — Mollick, "Delivery Rates on Kickstarter" (University of Pennsylvania)
36. https://www.ptcrb.com/wp-content/uploads/2021/12/10_Steps_to_PTCRB_Cert_for_Cell_Enabled_IoT_Devices-V2.pdf — PTCRB, "10 Steps to PTCRB Certification"
37. https://www.business.att.com/content/dam/attbusiness/briefs/att-global-device-certification-brief.pdf — AT&T, device certification brief
38. https://community.hologram.io/t/cheapest-module/2018 — Hologram community forum
39. https://hubble.com/community/comparisons/the-true-cost-of-cellular-iot/ — Hubble, "The True Cost of Cellular IoT" (vendor)
40. https://www.quectel.com/?p=64723 — Quectel (vendor)
41. https://www.tuvsud.com/en-us/services/product-certification/red-cybersecurity-requirements — TÜV SÜD, RED cybersecurity requirements
42. https://blog.qima.com/certification/how-red-shapes-cybersecurity-requirements-for-wireless-products — QIMA blog
43. https://www.cepro.com/networking/cellular/how-the-security-industry-is-pressuring-att-to-postpone-3g-sunset/ — CE Pro
44. https://www.cepro.com/news/cellbounce_3g_cdma_sunset_security_alarm_industry_diy_no_truck_roll/8838/ — CE Pro (2019)
45. https://www.ccjdigital.com/business/article/14937916/will-the-end-of-3g-cellular-be-more-disruptive-to-fleets-than-eld-mandate — CCJ
46. https://www.ofcom.org.uk/phones-telecoms-and-internet/information-for-industry/policy/2g-and-3g-switch-off/advice-for-iot-and-third-party-device-suppliers — Ofcom
47. https://www.vodafone.co.uk/newscentre/smart-living/everything-you-need-to-know-about/vodafonethree-2g-switch-off/ — Vodafone UK
48. https://www.gov.uk/government/publications/2g-switch-off-charter/2g-switch-off-charter — UK Government, 2G Switch-off Charter (24 March 2026)
49. https://www.telecomtv.com/content/telco-and-csp/unabiz-appointed-as-new-owner-of-sigfox-sa-and-sigfox-france-sas-under-receivership-proceeding-by-the-commercial-court-of-toulouse-44247/ — TelecomTV (April 2022)
50. https://rcrwireless.com/20250909/internet-of-things/sigfox-unabiz-court — RCR Wireless, "Sigfox back in court" (9 September 2025)
51. https://ibasis.com/when-engaging-in-a-cellular-iot-lpwa-deployment-part-2/ — iBASIS (vendor)
52. https://emnify.com/nb-iot-coverage — emnify NB-IoT coverage table (vendor)
53. https://www.rcrwireless.com/20211028/fundamentals/roaming-billing-provisioning-10-key-nb-iot-challenges-1-5 — RCR Wireless (28 October 2021)
54. https://eprints.gla.ac.uk/251066 — University of Glasgow eprint (LoRaWAN packet loss)
55. https://www.kerlink.com/blog/2026/08/04/optimising-lorawan-coverage-best-practices-and-radio-planning/ — Kerlink blog (4 August 2026, vendor)
56. https://www.thethingsnetwork.org/forum/t/packet-loss-when-multiple-gateways-used/27620 — The Things Network forum
57. https://www.theregister.com/2022/04/19/insteon_cloud_shutdown/ — The Register (19 April 2022)
58. https://www.forrester.com/blogs/insteon-and-the-internet-of-bricks/ — Forrester blog
59. https://betanews.com/2016/05/04/revolv-shutdown/ — BetaNews, open letter on the Revolv shutdown (4 May 2016)
60. https://opus.cloud1.lib.uts.edu.au/handle/10453/172967 — University of Technology Sydney (UTS) repository
61. https://epubl.ktu.edu/object/elaba:248266545 — Kaunas University of Technology (KTU) repository (LiSOCl2 batteries)
62. https://research-information.bris.ac.uk/en/publications/on-predicting-the-battery-lifetime-of-iot-devices-experiences-fro/ — University of Bristol
63. https://industrialmonitordirect.com/blogs/knowledgebase/banner-q45-wireless-sensor-battery-life-and-deployment-guide — Industrial Monitor Direct (secondary)
64. https://www.disruptive-technologies.com/sensors/temperature-sensor — Disruptive Technologies (vendor)
65. https://www.rcrwireless.com/20180518/internet-of-things/iot-installation-costs-scuppering-roi-tag40 — RCR Wireless (18 May 2018)
66. https://www.digi.com/blog/post/the-roi-of-remote-iot-device-management — Digi (vendor)
67. https://ubuntu.com/core/features/recovery — Canonical, Ubuntu Core (vendor)
68. https://www.arcweb.com/node/52996 — ARC Advisory Group
69. https://www.sec.gov/Archives/edgar/data/1826000/000182600024000069/lat-20220630.htm — Latch, Form 10-Q (SEC)
70. https://therealdeal.com/2022/08/26/tishman-speyer-backed-latch-says-its-financial-statements-cant-be-relied-upon — The Real Deal (26 August 2022)
71. https://therealdeal.com/national/2023/08/02/latch-wont-meet-deadline-for-nasdaq-compliance — The Real Deal (2 August 2023)
72. https://www.businesswire.com/news/home/20250806932749/en/SmartRent-Reports-Second-Quarter-2025-Financial-Results — Business Wire, SmartRent Q2 2025 results (6 August 2025)
73. https://foodindustrynetwork.com/?p=66083 — Food Industry Network, "Farmers Edge disputes merits of claim made by former investors"
74. https://zipitwireless.com/blog/iot-subscriber-churn-what-it-is-how-to-measure-it-and-why-it-matters — Zipit Wireless (vendor)
75. https://techcrunch.com/2019/02/08/item-tracking-startup-adero-is-laying-off-45-of-staff-just-weeks-after-it-pivoted — TechCrunch (8 February 2019)
76. https://tomtunguz.com/samsara-s-1/ — Tomasz Tunguz, "Samsara S-1"
77. https://www.sec.gov/Archives/edgar/data/1642896/000119312521334578/d261594ds1.htm — Samsara, Form S-1 (2021)
78. https://www.sec.gov/Archives/edgar/data/1642896/000164289622000016/samsaraform10-kxq42022.htm — Samsara, Form 10-K (FY2022)
79. https://www.sec.gov/Archives/edgar/data/1642896/000162828026039507/iot2026ars.pdf — Samsara Annual Report (2026)
80. https://businessmodelcanvastemplate.com/blogs/how-it-works/augury-how-it-works — Business Model Canvas Template blog (secondary)
81. https://www.techtarget.com/ai/news/252484554/Predictive-maintenance-vendor-launches-AI-warranty — TechTarget
82. https://www.controlant.com/insights/two-years-safeguarding-the-pfizer-biontech-covid-19-vaccine — Controlant (company)
83. https://www.controlant.com/insights/controlant-agm-2023-revenue-doubled-and-continued-growth-ahead — Controlant (company; title only seen)
84. https://octopus-haccp.com/?p=18130 — Octopus HACCP (vendor)
85. https://fruitgrowersnews.com/?p=10874 — Fruit Growers News, Digi wireless temperature monitoring (May 2016)
86. https://iot-analytics.com/product/iot-commercialization-business-model-adoption-report-2024/ — IoT Analytics report page (2024)
87. https://iot-analytics.com/how-to-create-a-successful-iot-business-model-insights-from-early-innovators/ — IoT Analytics
88. https://newsroom.statefarm.com/state-farm-ting-electrical-fire/ — State Farm newsroom
89. https://newsroom.statefarm.com/state-farm-expands-ting-fire-safety-program-to-2-million-homes/ — State Farm newsroom
90. https://newsroom.statefarm.com/whisker-labs/ — State Farm newsroom, "Whisker Labs Funding Led by State Farm Ventures Oversubscribed"
91. https://www.aviva.com/newsroom/news-releases/2016/10/uk-homeserve-partners-with-aviva-to-offer-smart-water-leak-detector-leakbot-to-customers-17683/ — Aviva (October 2016)
92. https://www.expressandstar.com/business/legal-general-strikes-leakbot-deal-with-homeserve-6264616 — Express & Star (2017)
93. https://insurancebusinessmag.com/uk/news/home-property/covea-and-leakbot-partnership-offers-a-first-for-brokers-91063.aspx — Insurance Business UK
94. https://insurancebusinessmag.com/uk/news/property-insurance/topdanmark-partners-with-leakbot-174055.aspx — Insurance Business UK
95. https://coverager.com/leakbot-connected-device-enters-us-market-prevent-major-damage-household-water-leaks-largest-predictable-home-insurance-claim-category/ — Coverager
96. https://www.computerweekly.com/news/450422417/Legal-General-picks-HomeServes-IoT-LeakBot-to-protect-homeowners — Computer Weekly (2017)
97. https://www.augury.com/media-center/press/augury-expands-collaboration-with-carrier-to-add-machine-health-capabilities/ — Augury press release (April 2021)
98. https://www.newswire.com/news/giatecs-smartrock-plus-program-signs-new-technology-forward-producer-21180158 — Newswire, Giatec SmartRock Plus
99. https://www.casestudies.com/company/giatec/case-study/stoneway-concrete-customer-case-study — CaseStudies.com, Giatec and Stoneway Concrete
100. https://www.on-sitemag.com/features/ottawa-tech-firm-takes-on-primitive-concrete-testing/ — On-Site Magazine
101. https://www.fierceelectronics.com/components/monnit-creates-partner-program-for-resellers-and-oems-to-capitalize-iot — Fierce Electronics (2015)
102. https://www.monnit.com/blog/time-to-celebrate-monnits-15th-anniversary/ — Monnit blog (company)
103. https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/McKinsey%20Digital/Our%20Insights/What%20separates%20leaders%20from%20laggards%20in%20the%20Internet%20of%20Things/What-separates-leaders-from-laggards-in-the-Internet-of-Things-vF.pdf — McKinsey, "What separates leaders from laggards in the Internet of Things" (2018)
104. https://cdixon.org/2013/04/30/hardware-startups/ — Chris Dixon, "Hardware startups" (30 April 2013)
105. https://www.propertycasualty360.com/2024/04/24/state-farms-ting-fire-monitor-detected-and-mitigated-over-500-fires-in-2022/ — PropertyCasualty360 (24 April 2024)
106. https://www.ukhospitality.org.uk/digital-haccp-wireless-temperature-monitoring/ — UKHospitality
107. https://pir.sa.gov.au/research/agtech/find_solutions/products/farmbot-tank-monitor — Primary Industries and Regions South Australia (PIRSA), Farmbot listing
108. https://www.waste360.com/mergers-acquisitions/roadrunner-recycling-acquires-compology — Waste360 (October 2022)
109. https://www.compliancemate.com/frequently-asked-questions — ComplianceMate FAQ (vendor)
110. https://www.wastedive.com/news/roadrunner-recycling-compology-acquisition-ai-technology/633392/ — Waste Dive (2022)
111. https://www.wastedive.com/news/recycle-track-systems-rts-acquires-enevo-us-accounts/579670/ — Waste Dive (2020)
112. https://www.abax.com/en-gb/newsroom/the-abax-venture-company-reen-acquires-enevo-group-c3363064 — ABAX newsroom
113. https://www.eweek.com/networking/startup-helium-systems-offers-iot-platform-for-enterprises/ — eWeek (2015)
114. https://blockworks.com/news/helium-parent-company-layoffs — Blockworks (October 2024)
115. https://www.agriculturedive.com/news/australia-based-startup-farmbot-raises-funding-us-expansion/719109/ — Agriculture Dive

## Implications for the scoring rubric
1. **Public evidence of pain is a gate.** "No market need" or unclear ROI is the top failure cause (CB Insights; Microsoft 28%; Bain). Require a sourced loss and a named party already paying for it (insurer, fines, write-offs). *Red flag:* pain evidenced only by vendor marketing or "visibility/insight" language.
2. **Cost of incident.** Score annual loss per site against full annual cost of ownership: amortised hardware, subscription, installation, truck rolls. Pilots die on the cost of scaling (32%). *Red flag:* loss below about 5× total cost of ownership.
3. **Frequency means provability.** Reward pain that recurs within a 1–3-month pilot. Rare catastrophic events cannot be shown in a pilot; 60% of initiatives already stall at proof of concept, and OEMs take 41 months to a first paying customer.
4. **Workaround.** Score highest when the sensor removes a recurring paid labour task (water runs, manual temperature logs, site rounds), giving measurable ROI.
5. **Compliance.** Weight highly only when a named regulation, insurer or contract requires records (HACCP, pharma cold chain). A records duty keeps data valuable and reduces churn.
6. **Buyer and channel: weight these most.** Nearly every survivor sold through a party already holding the risk or site visit (insurers, Carrier, ready-mix suppliers, resellers). *Red flag:* direct enterprise sales needing IT and OT sign-off, with no channel.
7. **Market gap.** Look for dead predecessors (Enevo, Sigfox-based products); a gap where incumbents failed may be a bad market.
8. **Buildability and BOM.** Require:
   - a pre-certified off-the-shelf radio module;
   - at least 50% hardware gross margin, or hardware recovered within the subscription;
   - self-installation in under 30 minutes;
   - battery life evidenced at the real reporting interval.

   *Red flags:* custom sensing elements; ATEX or medical certification; a single proprietary network; 2G, 3G or single-operator NB-IoT dependence; cloud-only operation.
9. **Recurring revenue.** Score why data stays valuable after month 3 (ongoing records, insurer reporting, consumables). *Red flags:* a one-off diagnosis; bulk hardware sales not tied to installation (SmartRent, Latch).
