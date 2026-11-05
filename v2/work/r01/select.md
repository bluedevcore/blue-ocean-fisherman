# v2 Round 01 — CLUSTER & SELECT (orchestrator)

**Clustering results**
- 414 signals were clustered into 166 new problems. Half 1 produced 62, half 2 produced 104.
- One signal (R01-S3-002) was attached to the imported problem R01-V-07.
- There are 0 gold problems (3 or more source types) and only 4 problems with 2 source types.

**Why multi-type problems are rare.** Each source type was mined in a DIFFERENT set of sectors
in round 1, so few problems could gather more than one source type.

**Selection**
- The protocol rule (select only problems with ≥ 2 source types) leaves 4 candidates.
- R01-P-044 duplicates R01-P-154 (guarding/cleaning contractors proving attendance to clients).
  It was merged into P-154 and marked killed as a duplicate.
- Round 1 therefore researches 3 signal-born problems (R01-P-038, R01-P-090, R01-P-154) plus
  the 15 v1 imports (R01-V-01..15).

**Fix for round 2.** All 7 miners will mine the SAME focus sectors. These are the sectors of the
strongest single-type pool problems:
- the PestPac-class software gap (P-006);
- small-trades job-management pricing (P-012);
- small-lab LIMS (P-080);
- staffing back office (P-016);
- MSHA records (P-057);
- MSP invoice reconciliation (P-077);
- museum inventories (P-156);
- vet PIMS (P-010);
- bid writing for guarding (P-046);
- receipt capture (P-095).
Re-clustering ALL signals can then add the 2nd and 3rd source types to these problems.
