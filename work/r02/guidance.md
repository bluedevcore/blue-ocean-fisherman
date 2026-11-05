# Guidance for Round 02 generators and breeder (from Round 01 results)

Round 1 results: 50 ideas scored, mean 60, max 74, none ≥ 90. Criterion averages (/10):
c1 Cost 5.2 | c2 Frequency 6.5 | c3 Workaround 6.4 | c4 Compliance 7.2 | c5 Buyer 5.3 |
c6 Channel 6.8 | c7 Market gap 4.5 | c8 Buildable 5.3 | c9 Recurring 5.7 | c10 Public pain 7.3

Biggest killers, in order:
1. **c7 Market gap (only 3/50 scored ≥ 7).** Critics knock ideas down hard when an incumbent
   already sells to that buyer. Already-served categories seen in Round 1 — AVOID unless you
   have a genuinely unserved sub-niche:
   - Legionella/water-temperature sentinel monitoring
   - HAV trigger-time tags (Reactec in the hire fleets)
   - LN2 dewar monitors
   - flood-drying remote monitoring
   - digital rodent/bait monitoring (Syngenta, Pelsis, Rentokil)
   - heating-oil tank gauges
   - transport temperature recorders
   - fridge/freezer loggers
   - void-property monitoring
   Look for niches where the only solutions are enterprise-priced or absent, ideally with
   evidence of complaints.
2. **c8 Buildable (3/50 ≥ 7).** Keep the sensor dead simple and cheap: temperature, reed/contact,
   float/level, tilt/vibration/accelerometer, current clamp, pressure switch, pulse/flow meter,
   load cell, PIR, all on LoRaWAN/LTE-M/NB-IoT with no customer IT. Avoid probes needing
   calibration (pH, chlorine, conductivity, particulates), cameras, ATEX zones and harsh
   immersion.
3. **c5 Buyer (5/50 ≥ 7).** The buyer must OWN the loss AND hold a budget. Good: owner-operators
   and ops managers of multi-site SMEs, compliance managers at agencies or contractors, service
   companies that bill per visit, franchise HQs, insurers. Bad: volunteers, charities, executors,
   NHS/council/prison procurement, "the landlord" of single homes.
4. **c1 Cost (13/50 ≥ 7).** Need a documented money loss of ≥ ~£5k per incident (fines,
   prosecutions, claims, stock or animal losses), not "inconvenience".

What scored best (70–74): a statutory or insurer check duty done MANUALLY at a fixed frequency,
which a sensor could evidence automatically:
- HSG282 hot-tub checks at holiday parks (74)
- TMV servicing (72)
- HAV records (71)
- sprinkler weekly pump tests (69)
- HMO weekly alarm tests (69)
- insurer unoccupancy inspections (70)
- culvert screen inspections (70)
Pair that duty-plus-frequency pattern with:
- an UNSERVED niche (c7);
- a buyer who owns the fine or loss (c5);
- a contractor who already visits to do the check (c6);
- a £5k+ documented loss (c1).
