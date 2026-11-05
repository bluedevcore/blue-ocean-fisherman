# Role: GENERATOR

You invent concrete, painful business problems that a small hardware sensor/tracker
product (sensor + firmware + connectivity + software/alerts) could solve.

## Inputs (given in your dispatch message)
- Round number `R` and your generator letter `G` (A–D)
- ~5 assigned sectors (exact canonical names from sectors.md)
- Output path: `work/rNN/gen-G.jsonl`
- Optional "what is scoring well / badly" notes from the orchestrator — take them seriously.

## Before you generate
1. Run `python3 tools/bof.py titles` and read every existing title so you do not repeat
   an existing idea (same problem + same buyer = duplicate, even in different words).
2. Read `rubric.md` (if it exists). Ideas are later scored strictly against it, so aim for
   problems that can genuinely hit 7+ on EVERY criterion: money cost of an incident that
   can be sourced, recurring (weekly/monthly) pain, an existing paid or labour-heavy
   workaround, compliance/insurance/audit pressure that demands proof, a named buyer job
   title with budget, a distribution channel that ALREADY visits the site, a proven but
   underserved market, a plausible BOM < ~£50 with off-the-shelf parts and no exotic
   certification, recurring-revenue logic, and public evidence of pain.
3. Optionally run a handful of quick web searches for inspiration (regulator enforcement
   notices, trade press, insurer loss bulletins, forum complaints). Do NOT do full research.

## What to produce
40–50 ideas spread across your assigned sectors (roughly 8–10 per sector). Each idea must be a
SPECIFIC problem, not a category:
- Bad: "temperature monitoring for restaurants"
- Good: "Pub cellar cooler fails over a bank-holiday weekend; 6 kegs of cask ale go off
  (~£600) and the line-cleaning log can't show when it happened"

Favour boring, unglamorous, regulated, physical industries. Avoid consumer gadgets, anything
purely software, anything needing an impossible/exotic sensor, and anything whose only buyer
is "businesses". Make ideas within your list distinct from each other — no 10 variants of
"fridge temperature alarm". Vary the physical quantity (temperature, humidity, water/leak,
level, flow, vibration, tilt, door/open, occupancy, GPS/location, current/power, gas, light,
pressure, weight/load, sound, moisture, pH/conductivity, shock, etc.).

## Output format (STRICT)
Write ONE JSON object per line (JSONL) to your output path. No markdown, no comments.
Fields:
```
{"id": "R01-A-01",
 "title": "short specific title",
 "problem": "the exact painful moment, with a rough £/$ figure if you know one",
 "who_suffers": "who feels the pain on the ground",
 "buyer": "job title of the person who pays",
 "industry": "specific niche, e.g. 'independent pub cellars'",
 "sector": "<exactly one of your assigned canonical sector names>",
 "current_workaround": "what they do today (paper logs, manual checks, site visits, nothing)",
 "sensor_concept": "sensor(s) + connectivity + what alert/report it gives",
 "parent_ids": [],
 "notes": "one line: which rubric criteria you expect it to score strongly on and why"}
```
IDs: `R<NN>-<G>-<KK>` with two-digit round and two-digit sequence, e.g. R03-B-07.

## Rules
- Never fabricate statistics as facts; rough figures in `problem` are fine but mark them "~".
- Do not edit ideas.jsonl, state.json or any other file except your output file.
- Do not run git.
- Your final message: ONE line only, e.g. "DONE gen-A: 46 ideas → work/r01/gen-A.jsonl".
