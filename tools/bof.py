#!/usr/bin/env python3
"""BLUE OCEAN FISHERMAN — orchestrator helper.

Only the orchestrator runs this (subagents may run the read-only `titles` command).
All mutations of ideas.jsonl / state.json / sectors.md go through here.

Commands
  init                         create state.json, ideas.jsonl, sectors.md (fresh run only)
  titles                       compact list of every idea so far (id | status | score | title | buyer)
  pick-sectors R [G] [K]       choose G groups (default 4) of K (default 5) least-fished sectors for round R
  merge-cast R                 append work/rNN/gen-*.jsonl + work/rNN/mutations.jsonl to ideas.jsonl (status new)
  list R                       compact listing of round R ideas with status new (for SORT)
  sort R KEEP [REASONS]        KEEP = file of ids to keep; others of round R (status new) -> filtered.
                               REASONS (optional) = TSV "id<TAB>reason" for filtered ideas
  haul R [PER]                 make researcher batches (default 5 ideas each) -> work/rNN/haul.json
  researched R                 mark kept ideas with evidence files as researched; report URL counts
  judge R [PER]                make critic batches (default 10) -> work/rNN/judge.json
  scored R                     merge critiques/<id>.json into ideas.jsonl -> scored; print distribution
  qualifiers [R]               ideas meeting numeric acceptance gates, not yet accepted/killed
  verdicts R                   show devil's advocate verdicts for round R qualifiers
  accept ID                    mark accepted (after DA SURVIVES + distinctness check)
  kill ID REASON               mark killed with reason
  top N                        top-N non-accepted scored/killed ideas with weakest criteria
  stats [R]                    score distribution, criterion averages, sector performance
  set-state R STEP             update state.json (round, step, accepted, totals) + render sectors.md
  note TEXT                    replace state.notes_for_generators with TEXT
  render-sectors               regenerate sectors.md
"""
import json, os, re, sys, glob, random, statistics
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDEAS = os.path.join(ROOT, "ideas.jsonl")
STATE = os.path.join(ROOT, "state.json")
SECTORS_MD = os.path.join(ROOT, "sectors.md")
CKEYS = [f"c{i}" for i in range(1, 11)]
CNAMES = {"c1": "Cost", "c2": "Frequency", "c3": "Workaround", "c4": "Compliance",
          "c5": "Buyer", "c6": "Channel", "c7": "Market gap", "c8": "Buildable",
          "c9": "Recurring", "c10": "Public pain"}

SECTORS = [
    "Agriculture – arable, horticulture & greenhouses",
    "Livestock farming (cattle, sheep, pigs, poultry)",
    "Aquaculture & fisheries",
    "Cold chain & refrigerated transport",
    "Food & drink manufacturing",
    "Restaurants, pubs & commercial kitchens",
    "Hospitality – hotels, B&Bs, holiday lets",
    "Residential lettings & social housing",
    "Commercial property & facilities management",
    "Construction sites",
    "Marine – marinas, boatyards, small commercial vessels",
    "Healthcare facilities – hospitals & clinics",
    "Care homes & assisted living",
    "Pharmacies, dispensing & vaccine storage",
    "Laboratories & research facilities",
    "Logistics & warehousing",
    "Fleet & road haulage",
    "Electricity networks & substations",
    "Water & wastewater utilities",
    "Heating oil, LPG & fuel distribution",
    "Education – schools, colleges, universities",
    "Retail – shops & supermarkets",
    "Manufacturing & industrial plants",
    "Mining & quarrying",
    "Waste management & recycling",
    "Events, festivals & temporary venues",
    "Sport & leisure – gyms, pitches, stadiums",
    "Swimming pools & spas",
    "Animal care – kennels, catteries, vets, rescue",
    "Equine – stables, yards, horse transport",
    "Zoos, aquariums & wildlife parks",
    "Museums, archives, galleries & heritage buildings",
    "Telecoms infrastructure – masts, cabinets, exchanges",
    "Aviation ground operations & airports",
    "Rail & transit infrastructure",
    "Ports, shipping containers & freight terminals",
    "Renewable energy – solar, wind, battery storage",
    "Forestry, timber & sawmills",
    "Vineyards, wineries, breweries & distilleries",
    "Beekeeping & pollination services",
    "Self-storage, lock-ups & archives storage",
    "Funeral services & mortuaries",
    "Data centres, server rooms & comms rooms",
    "Places of worship, community halls & charities",
    "Motor trade – garages, dealerships, vehicle storage",
    "Plant, tool & equipment hire",
    "Local councils – parks, highways, street assets",
    "Security, alarm monitoring & key holding",
    "Commercial laundry, cleaning & washroom services",
    "Pest control",
    "Fire safety & building safety compliance",
    "Grain stores, feed mills & bulk storage silos",
    "Fuel forecourts & EV charging sites",
    "Lifts, escalators & building plant rooms",
    "Dental, GP & veterinary practices",
    "Prisons, police custody & secure facilities",
]


def nn(r):
    return f"{int(r):02d}"


def wdir(r):
    d = os.path.join(ROOT, "work", f"r{nn(r)}")
    os.makedirs(d, exist_ok=True)
    return d


def load_ideas():
    out = []
    if os.path.exists(IDEAS):
        with open(IDEAS) as f:
            for line in f:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
    return out


def save_ideas(ideas):
    tmp = IDEAS + ".tmp"
    with open(tmp, "w") as f:
        for i in ideas:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")
    os.replace(tmp, IDEAS)


def load_state():
    with open(STATE) as f:
        return json.load(f)


def save_state(s):
    with open(STATE, "w") as f:
        json.dump(s, f, indent=2, ensure_ascii=False)
        f.write("\n")


URL_RE = re.compile(r"https?://[^\s<>\"'`\]\)|]+")


def norm_url(u):
    u = u.strip().rstrip(".,;:!?*_")
    u = re.sub(r"#.*$", "", u)
    u = u.rstrip("/")
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://www\.", "https://", u)
    return u.lower()


def evidence_urls(iid):
    p = os.path.join(ROOT, "evidence", f"{iid}.md")
    if not os.path.exists(p):
        return None
    txt = open(p, encoding="utf-8", errors="ignore").read()
    return sorted({norm_url(u) for u in URL_RE.findall(txt)})


def critique(iid):
    p = os.path.join(ROOT, "critiques", f"{iid}.json")
    if not os.path.exists(p):
        return None
    try:
        return json.load(open(p))
    except Exception as e:
        print(f"!! bad critique JSON {iid}: {e}")
        return None


def verified_ok(iid, crit, ev_urls):
    ev = set(ev_urls or [])
    ok = 0
    for v in (crit or {}).get("verified_urls", []):
        res = str(v.get("result", "")).lower()
        if res.startswith("ok") and norm_url(v.get("url", "")) in ev:
            ok += 1
    return ok


def search_ok(iid, crit, ev_urls):
    ev = set(ev_urls or [])
    return len({norm_url(v.get("url", "")) for v in (crit or {}).get("verified_urls", [])
                if str(v.get("result", "")).lower().startswith("search-confirmed")
                and norm_url(v.get("url", "")) in ev})


def fmt_scores(cs):
    return " ".join(f"{k}={cs.get(k, '?')}" for k in CKEYS)


def weakest(cs, n=3):
    items = sorted(((cs.get(k, 0), k) for k in CKEYS))
    return ", ".join(f"{k}({CNAMES[k]})={v}" for v, k in items[:n])


# ---------------------------------------------------------------- commands
def cmd_init():
    if os.path.exists(STATE):
        sys.exit("state.json exists — this is a resumed run; refusing to init")
    s = {"round": 0, "accepted": [], "total_ideas": 0, "last_completed_step": "setup",
         "sector_fished": {k: 0 for k in SECTORS}, "notes_for_generators": ""}
    save_state(s)
    open(IDEAS, "a").close()
    cmd_render_sectors()
    print("initialised")


def cmd_titles():
    for i in load_ideas():
        sc = i.get("score")
        print(f"{i['id']} | {i.get('status')} | {sc if sc is not None else '-'} | {i.get('title')} | {i.get('buyer')}")


def cmd_pick_sectors(r, g=4, k=5):
    s = load_state()
    fished = s["sector_fished"]
    names = list(fished.keys())
    random.seed(1000 + int(r))
    random.shuffle(names)
    names.sort(key=lambda x: fished[x])
    chosen = names[: g * k]
    random.shuffle(chosen)
    groups = {chr(65 + gi): chosen[gi * k:(gi + 1) * k] for gi in range(g)}
    for grp in groups.values():
        for sec in grp:
            fished[sec] += 1
    save_state(s)
    json.dump(groups, open(os.path.join(wdir(r), "sectors.json"), "w"), indent=2, ensure_ascii=False)
    for gname, grp in groups.items():
        print(f"{gname}: " + " ; ".join(grp))


REQUIRED = ["title", "problem", "buyer", "industry", "sensor_concept"]


def cmd_merge_cast(r):
    ideas = load_ideas()
    have = {i["id"] for i in ideas}
    files = sorted(glob.glob(os.path.join(wdir(r), "gen-*.jsonl"))) + \
        sorted(glob.glob(os.path.join(wdir(r), "mutations.jsonl")))
    added = 0
    for fp in files:
        tag = os.path.basename(fp).replace("gen-", "").replace(".jsonl", "")
        letter = "M" if tag == "mutations" else tag.upper()
        n = 0
        with open(fp) as f:
            for ln, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except Exception as e:
                    print(f"!! {fp}:{ln} bad JSON: {e}")
                    continue
                n += 1
                iid = o.get("id") or f"R{nn(r)}-{letter}-{n:02d}"
                if not re.match(r"^R\d\d-[A-Z]-\d\d+$", iid):
                    iid = f"R{nn(r)}-{letter}-{n:02d}"
                while iid in have:
                    n += 1
                    iid = f"R{nn(r)}-{letter}-{n:02d}"
                missing = [k for k in REQUIRED if not o.get(k)]
                if missing:
                    print(f"!! {iid} missing {missing}")
                rec = {
                    "id": iid, "round": int(r), "title": o.get("title"), "problem": o.get("problem"),
                    "who_suffers": o.get("who_suffers"), "buyer": o.get("buyer"),
                    "industry": o.get("industry"), "sector": o.get("sector", o.get("industry")),
                    "current_workaround": o.get("current_workaround"),
                    "sensor_concept": o.get("sensor_concept"),
                    "parent_ids": o.get("parent_ids", []) or [],
                    "status": "new", "score": None, "criterion_scores": None,
                    "notes": o.get("notes", ""),
                }
                for extra in ("mutation_type", "fixes"):
                    if o.get(extra):
                        rec[extra] = o[extra]
                ideas.append(rec)
                have.add(iid)
                added += 1
        print(f"{os.path.basename(fp)}: {n} ideas")
    save_ideas(ideas)
    print(f"added {added}; total ideas {len(ideas)}")


def cmd_list(r):
    for i in load_ideas():
        if i["round"] == int(r) and i["status"] == "new":
            par = f" <{','.join(i['parent_ids'])}>" if i.get("parent_ids") else ""
            print(f"{i['id']} | {i.get('title')} | {i.get('buyer')}{par}")


def read_ids(path):
    txt = open(path).read()
    return [x for x in re.findall(r"R\d\d-[A-Z]-\d\d+", txt)]


def cmd_sort(r, keep, reasons=None):
    keep_ids = set(read_ids(keep))
    rs = {}
    if reasons and os.path.exists(reasons):
        for line in open(reasons):
            if "\t" in line:
                a, b = line.rstrip("\n").split("\t", 1)
                rs[a.strip()] = b.strip()
    ideas = load_ideas()
    kept = filt = 0
    for i in ideas:
        if i["round"] == int(r) and i["status"] == "new":
            if i["id"] in keep_ids:
                kept += 1
            else:
                i["status"] = "filtered"
                i["notes"] = ("filtered: " + rs.get(i["id"], "not in top ~50 at SORT")).strip()
                filt += 1
    missing = keep_ids - {i["id"] for i in ideas}
    if missing:
        print("!! keep ids not found:", sorted(missing))
    save_ideas(ideas)
    print(f"kept {kept}, filtered {filt}")


def kept_ids(r, status="new"):
    return [i["id"] for i in load_ideas() if i["round"] == int(r) and i["status"] == status]


def cmd_haul(r, per=5):
    ids = kept_ids(r, "new")
    batches = [ids[x:x + per] for x in range(0, len(ids), per)]
    json.dump(batches, open(os.path.join(wdir(r), "haul.json"), "w"), indent=1)
    for b in batches:
        print(" ".join(b))


def cmd_researched(r):
    ideas = load_ideas()
    for i in ideas:
        if i["round"] == int(r) and i["status"] == "new":
            u = evidence_urls(i["id"])
            if u is None:
                print(f"MISSING evidence: {i['id']}")
            else:
                i["status"] = "researched"
                i["evidence_urls"] = len(u)
                print(f"{i['id']}: {len(u)} urls")
    save_ideas(ideas)


def cmd_judge(r, per=10):
    ids = kept_ids(r, "researched")
    batches = [ids[x:x + per] for x in range(0, len(ids), per)]
    json.dump(batches, open(os.path.join(wdir(r), "judge.json"), "w"), indent=1)
    for b in batches:
        print(" ".join(b))


def cmd_scored(r):
    ideas = load_ideas()
    totals = []
    for i in ideas:
        if i["round"] == int(r) and i["status"] in ("researched", "scored"):
            c = critique(i["id"])
            if c is None:
                print(f"MISSING critique: {i['id']}")
                continue
            cs = {k: int(c.get("criterion_scores", {}).get(k, 0)) for k in CKEYS}
            tot = sum(cs.values())
            if c.get("total") is not None and int(c["total"]) != tot:
                print(f"note {i['id']}: critic total {c['total']} != sum {tot}; using sum")
            ev = evidence_urls(i["id"]) or []
            i.update({"status": "scored", "score": tot, "criterion_scores": cs,
                      "evidence_urls": len(ev), "verified_ok": verified_ok(i["id"], c, ev),
                      "search_ok": search_ok(i["id"], c, ev),
                      "notes": ("weakest: " + str(c.get("weakest", ""))[:300])})
            totals.append((tot, i["id"]))
    save_ideas(ideas)
    totals.sort(reverse=True)
    for t, iid in totals:
        print(f"{iid}: {t}")


def is_qualifier(i):
    cs = i.get("criterion_scores") or {}
    return (i.get("score") or 0) >= 90 and cs and min(cs.values()) >= 7 \
        and (i.get("evidence_urls") or 0) >= 8 and (i.get("verified_ok") or 0) >= 3


def cmd_qualifiers(r=None):
    for i in load_ideas():
        if r is not None and i["round"] != int(r):
            continue
        if i["status"] == "scored" and is_qualifier(i):
            print(f"{i['id']} | {i['score']} | urls={i['evidence_urls']} verified={i['verified_ok']} | {i['title']}")
    # provisional: all gates met except fetch-verification (network blocked)
    for i in load_ideas():
        if r is not None and i["round"] != int(r):
            continue
        cs = i.get("criterion_scores") or {}
        if i["status"] == "scored" and (i.get("score") or 0) >= 90 and cs and min(cs.values()) >= 7 \
                and (i.get("evidence_urls") or 0) >= 8 and (i.get("verified_ok") or 0) < 3 \
                and (i.get("verified_ok") or 0) + (i.get("search_ok") or 0) >= 3:
            print(f"PROVISIONAL (needs fetch-verification): {i['id']} | {i['score']} | "
                  f"fetched_ok={i.get('verified_ok')} search_ok={i.get('search_ok')} | {i['title']}")
    # near-misses for info
    for i in load_ideas():
        if r is not None and i["round"] != int(r):
            continue
        cs = i.get("criterion_scores") or {}
        if i["status"] == "scored" and (i.get("score") or 0) >= 90 and not is_qualifier(i):
            print(f"(near: {i['id']} {i['score']} min={min(cs.values()) if cs else '?'} "
                  f"urls={i.get('evidence_urls')} verified={i.get('verified_ok')})")


def cmd_verdicts(r):
    for i in load_ideas():
        if i["round"] == int(r) or i["status"] == "scored":
            p = os.path.join(ROOT, "devils", f"{i['id']}.md")
            if os.path.exists(p):
                first = open(p).readline().strip()
                print(f"{i['id']} [{i['status']}]: {first[:400]}")


def set_status(iid, status, note=None):
    ideas = load_ideas()
    for i in ideas:
        if i["id"] == iid:
            i["status"] = status
            if note:
                i["notes"] = (note + " | " + (i.get("notes") or ""))[:600]
            save_ideas(ideas)
            return i
    sys.exit(f"no idea {iid}")


def cmd_accept(iid):
    i = set_status(iid, "accepted", "ACCEPTED (survived devil's advocate)")
    s = load_state()
    if iid not in s["accepted"]:
        s["accepted"].append(iid)
    save_state(s)
    print(f"accepted {iid} — total accepted {len(s['accepted'])}")


def cmd_kill(iid, reason):
    set_status(iid, "killed", "KILLED: " + reason)
    print(f"killed {iid}")


def cmd_top(n):
    pool = [i for i in load_ideas() if i["status"] in ("scored", "killed") and i.get("score") is not None]
    pool.sort(key=lambda i: -i["score"])
    for i in pool[: int(n)]:
        print(f"{i['id']} | {i['score']} | {i['status']} | {i['title']} | weakest: {weakest(i['criterion_scores'])}")


def cmd_stats(r=None):
    ideas = load_ideas()
    sel = [i for i in ideas if (r is None or i["round"] == int(r))]
    st = Counter(i["status"] for i in sel)
    print("status:", dict(st))
    sc = [i for i in sel if i.get("score") is not None]
    if sc:
        bins = Counter((i["score"] // 10) * 10 for i in sc)
        print("score bins:", {f"{b}-{b+9}": bins[b] for b in sorted(bins)})
        print(f"mean {statistics.mean(i['score'] for i in sc):.1f}  max {max(i['score'] for i in sc)}")
        avg = {k: statistics.mean(i["criterion_scores"][k] for i in sc) for k in CKEYS}
        print("criterion avg:", " ".join(f"{k}:{CNAMES[k]}={v:.1f}" for k, v in avg.items()))
        ge7 = {k: sum(1 for i in sc if i["criterion_scores"][k] >= 7) for k in CKEYS}
        print("count >=7:   ", " ".join(f"{k}={v}" for k, v in ge7.items()))
        bysec = defaultdict(list)
        for i in sc:
            bysec[i.get("sector") or i.get("industry")].append(i["score"])
        print("by sector (n, mean, max):")
        for sec, v in sorted(bysec.items(), key=lambda x: -max(x[1])):
            print(f"  {sec}: n={len(v)} mean={statistics.mean(v):.0f} max={max(v)}")


def cmd_set_state(r, step):
    s = load_state()
    ideas = load_ideas()
    s["round"] = int(r)
    s["last_completed_step"] = step
    s["total_ideas"] = len(ideas)
    s["accepted"] = [i["id"] for i in ideas if i["status"] == "accepted"]
    save_state(s)
    cmd_render_sectors()
    print(json.dumps({k: s[k] for k in ("round", "last_completed_step", "total_ideas", "accepted")}))


def cmd_note(text):
    s = load_state()
    s["notes_for_generators"] = text
    save_state(s)


def cmd_render_sectors():
    s = load_state()
    ideas = load_ideas()
    gen = Counter(i.get("sector") for i in ideas)
    res = Counter(i.get("sector") for i in ideas if i["status"] in ("researched", "scored", "accepted", "killed"))
    best = defaultdict(int)
    acc = Counter(i.get("sector") for i in ideas if i["status"] == "accepted")
    for i in ideas:
        if i.get("score") is not None:
            best[i.get("sector")] = max(best[i.get("sector")], i["score"])
    lines = ["# Sectors", "",
             "Canonical sector list for generators. 'Times fished' = rounds in which a generator was assigned it.",
             "Generators must set each idea's `sector` to exactly one of these names. (Auto-generated by tools/bof.py.)", "",
             "| # | Sector | Times fished | Ideas generated | Researched | Best score | Accepted |",
             "|---|---|---|---|---|---|---|"]
    for n, sec in enumerate(s["sector_fished"].keys(), 1):
        lines.append(f"| {n} | {sec} | {s['sector_fished'][sec]} | {gen.get(sec, 0)} | {res.get(sec, 0)} | "
                     f"{best.get(sec, '-') if sec in best else '-'} | {acc.get(sec, 0)} |")
    other = [k for k in gen if k not in s["sector_fished"]]
    if other:
        lines += ["", "Ideas tagged with non-canonical sectors (mostly breeder mutations):", ""]
        for k in sorted(other, key=str):
            lines.append(f"- {k}: {gen[k]} ideas, best {best.get(k, '-')}")
    open(SECTORS_MD, "w").write("\n".join(lines) + "\n")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    c, rest = a[0], a[1:]
    fn = {
        "init": cmd_init, "titles": cmd_titles, "pick-sectors": cmd_pick_sectors,
        "merge-cast": cmd_merge_cast, "list": cmd_list, "sort": cmd_sort, "haul": cmd_haul,
        "researched": cmd_researched, "judge": cmd_judge, "scored": cmd_scored,
        "qualifiers": cmd_qualifiers, "verdicts": cmd_verdicts, "accept": cmd_accept,
        "kill": lambda iid, *r: cmd_kill(iid, " ".join(r)), "top": cmd_top, "stats": cmd_stats,
        "set-state": cmd_set_state, "note": lambda *t: cmd_note(" ".join(t)),
        "render-sectors": cmd_render_sectors,
    }.get(c)
    if not fn:
        print(__doc__)
        sys.exit(1)
    conv = []
    for x in rest:
        conv.append(int(x) if x.isdigit() else x)
    fn(*conv)


if __name__ == "__main__":
    main()
