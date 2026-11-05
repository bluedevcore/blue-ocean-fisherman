#!/usr/bin/env python3
"""BLUE OCEAN FISHERMAN v2 — orchestrator helper. All paths are under v2/.

Only the orchestrator mutates state via this script. Subagents may run the read-only
commands: signals-for, problems-brief, signal-urls, show-problem.

Commands
  init                              create state.json, signals.jsonl, problems.jsonl, sectors.md, sources.md
  pick-sectors R [K]                assign K (default 5) least-mined sectors to each of S1..S7 -> work/rNN/sectors.json
  merge-signals R                   merge work/rNN/signals-*.jsonl and targeted-*.jsonl (from round R) into signals.jsonl
  signal-urls                       print every known signal URL (read-only, for miners to avoid repeats)
  signals-for HALF|all [ROUND]      compact signals for clusterer half 1/2 (by sector list) or all
  problems-brief [HALF]             compact list of existing problems (read-only)
  show-problem ID                   print one problem + its signals (read-only)
  merge-clusters R                  merge work/rNN/clusters-*.jsonl into problems.jsonl (new -> pool; existing -> add signals)
  import-v1 R [N]                   import top-N (default 15) scored v1 ideas as candidate problems (from_v1)
  select R [N]                      mark top-N (default 40) pool problems with >=2 source types as candidate
  research R [PER]                  researcher batches of candidates (default 5) -> work/rNN/research.json
  researched R                      candidates with evidence -> researched (+ url / S-type counts)
  judge R [PER]                     critic batches of researched (default 8) -> work/rNN/judge.json
  scored R                          merge critiques -> scored / killed(knockout); weighted totals
  qualifiers                        problems passing numeric acceptance gates (+ provisional, near-misses)
  verdicts                          devil's advocate first lines for scored problems
  accept ID | kill ID REASON | park ID REASON
  retarget R ID...                  send problems back to candidate for re-research (retries+1; >2 -> parked)
  top N [MIN] [MAX]                 top-N non-accepted scored problems in score range, with weakest criteria
  stats [R]                         score distribution, criterion averages, by source type / sector
  set-state R STEP                  update state.json + render sectors.md and sources.md
  note TEXT                         set state.notes_for_miners
  render                            regenerate sectors.md and sources.md
"""
import json, os, re, sys, glob, random, statistics
from collections import Counter, defaultdict

V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(V2)
P = lambda *a: os.path.join(V2, *a)
SIGNALS, PROBLEMS, STATE = P("signals.jsonl"), P("problems.jsonl"), P("state.json")
STYPES = {"S1": "Job ads", "S2": "Bad reviews", "S3": "Triggers", "S4": "Tenders & grants",
          "S5": "Freelance gigs", "S6": "Forums & communities", "S7": "Enforcement & losses"}
W = {"W1": 15, "W2": 15, "W3": 15, "W4": 10, "W5": 10, "W6": 10, "W7": 10, "W8": 10, "W9": 5}
WNAMES = {"W1": "Cost", "W2": "Budget proof", "W3": "Gap", "W4": "Why now", "W5": "Frequency",
          "W6": "Reachability", "W7": "Buildable", "W8": "Recurring", "W9": "Defensibility"}
KO = ["K1", "K2", "K3", "K4", "K5"]

SECTORS = [
    "Trades – electricians, plumbers, heating engineers", "Building maintenance & facilities management",
    "Residential lettings & property management", "Block management & leasehold", "Social housing",
    "Estate agents & property sales", "Construction – main contractors",
    "Construction – subcontractors & specialist trades", "Architecture, surveying & building control",
    "Care homes & domiciliary care", "Healthcare admin – GP practices & clinics", "Dental practices",
    "Veterinary practices", "Pharmacies", "Legal admin – law firms & conveyancing",
    "Accounting, bookkeeping & payroll bureaux", "Insurance brokers & claims handling",
    "Financial advice & mortgage brokers", "Recruitment & staffing agencies",
    "HR & employment compliance", "Logistics, haulage & couriers", "Warehousing & fulfilment",
    "Agriculture – arable & horticulture", "Livestock & dairy farming", "Food & drink manufacturing",
    "Restaurants, pubs & takeaways", "Hotels, B&Bs & holiday lets", "Education – schools & academy trusts",
    "Further & higher education", "Nurseries & childcare", "Local government & councils",
    "Charities & non-profits", "Places of worship & community halls", "Manufacturing & engineering",
    "Compliance, HSE & safety consultancy", "Fire safety & security installers", "Funeral services",
    "Events, festivals & venues", "Sport, leisure & gyms", "Marine – marinas, boatyards & fishing",
    "Energy installers – solar, heat pumps, EV charging", "Utilities – water, gas & electricity networks",
    "Waste management & recycling", "Environmental consultancy & permitting",
    "Retail – independent shops & chains", "E-commerce sellers & marketplaces",
    "Motor trade – garages, dealers & body shops", "Fleet management", "Plant & equipment hire",
    "Cleaning & hygiene services", "Pest control", "Landscaping & grounds maintenance",
    "Beauty, hair & wellness salons", "Travel agents & tour operators",
    "Import/export & customs brokers", "IT managed service providers & telecoms",
    "Data centres", "Laboratories & testing", "Medical device & life-science SMEs",
    "Museums, heritage & archives", "Mining & quarrying", "Aviation & airports",
    "Rail & public transport", "Ports & shipping", "Security guarding & key holding", "Self-storage",
]


def nn(r): return f"{int(r):02d}"


def wdir(r):
    d = P("work", f"r{nn(r)}"); os.makedirs(d, exist_ok=True); return d


def load(path):
    out = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def save(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def lstate(): return json.load(open(STATE))


def sstate(s):
    json.dump(s, open(STATE, "w"), indent=2, ensure_ascii=False); open(STATE, "a").write("\n")


URL_RE = re.compile(r"https?://[^\s<>\"'`\]\)|]+")


def norm_url(u):
    u = (u or "").strip().rstrip(".,;:!?*_")
    u = re.sub(r"#.*$", "", u).rstrip("/")
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://www\.", "https://", u)
    return u.lower()


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", (s or "").lower()) if len(w) > 2}


def jacc(a, b):
    a, b = toks(a), toks(b)
    return len(a & b) / max(1, len(a | b))


def halves():
    h1 = SECTORS[0::2]; h2 = SECTORS[1::2]
    return {1: set(h1), 2: set(h2)}


# ---------------------------------------------------------------- setup
def cmd_init():
    if os.path.exists(STATE):
        sys.exit("v2/state.json exists — resumed run; refusing to init")
    s = {"round": 0, "accepted": [], "last_completed_step": "setup", "source_type_yield": {},
         "notes_for_miners": "", "sector_mined": {k: 0 for k in SECTORS}}
    sstate(s)
    open(SIGNALS, "a").close(); open(PROBLEMS, "a").close()
    cmd_render(); print("initialised v2")


def cmd_pick_sectors(r, k=5):
    k = int(k)
    s = lstate(); mined = s["sector_mined"]
    names = list(mined); random.seed(2000 + int(r)); random.shuffle(names)
    names.sort(key=lambda x: mined[x])
    groups = {}
    pool = names[:]
    for st in STYPES:
        g = pool[:k]; pool = pool[k:] + g  # rotate through least-mined
        groups[st] = g
        for sec in g:
            mined[sec] += 1
    sstate(s)
    json.dump(groups, open(os.path.join(wdir(r), "sectors.json"), "w"), indent=1, ensure_ascii=False)
    for st, g in groups.items():
        print(f"{st}: " + " ; ".join(g))


# ---------------------------------------------------------------- signals
def cmd_merge_signals(r):
    sigs = load(SIGNALS)
    have = {s["id"] for s in sigs}
    by_url = defaultdict(list)
    for s in sigs:
        by_url[norm_url(s["url"])].append(s)
    files = sorted(glob.glob(os.path.join(wdir(r), "signals-S*.jsonl"))) + \
        sorted(glob.glob(os.path.join(wdir(r), "targeted-*.jsonl")))
    added = dup = bad = 0
    per = Counter()
    for fp in files:
        base = os.path.basename(fp)
        targeted = base.startswith("targeted-")
        n = 0
        for ln, line in enumerate(open(fp, encoding="utf-8"), 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception as e:
                print(f"!! {base}:{ln} bad JSON: {e}"); bad += 1; continue
            st = str(o.get("source_type", "")).upper()[:2]
            if st not in STYPES or not o.get("url"):
                print(f"!! {base}:{ln} missing source_type/url"); bad += 1; continue
            u = norm_url(o["url"])
            if any(jacc(o.get("pain_summary", ""), x.get("pain_summary", "")) > 0.5 for x in by_url[u]):
                dup += 1; continue
            n += 1
            prefix = f"R{nn(r)}-{'T' if targeted else 'S'}{st[1]}"
            k = n
            iid = f"{prefix}-{k:03d}"
            while iid in have:
                k += 1; iid = f"{prefix}-{k:03d}"
            rec = {"id": iid, "round": int(r), "source_type": st, "url": o["url"],
                   "date_found": o.get("date_found"), "source_date": o.get("source_date"),
                   "sector": o.get("sector"), "quote_or_datapoint": (o.get("quote_or_datapoint") or "")[:400],
                   "who_suffers": o.get("who_suffers"), "implied_payer": o.get("implied_payer"),
                   "pain_summary": o.get("pain_summary"), "money": o.get("money")}
            if targeted:
                rec["for_problem"] = o.get("for_problem") or base[len("targeted-"):-len(".jsonl")]
            for extra in ("what_changes", "effective_date", "who_affected", "must_do", "jurisdiction"):
                if o.get(extra):
                    rec[extra] = o[extra]
            sigs.append(rec); have.add(iid); by_url[u].append(rec)
            per[st] += 1; added += 1
        print(f"{base}: {n} new")
    save(SIGNALS, sigs)
    print(f"added {added}, duplicates skipped {dup}, bad {bad}; per type {dict(per)}; total signals {len(sigs)}")


def cmd_signal_urls():
    for s in load(SIGNALS):
        print(s["url"])


def cmd_signals_for(half, rnd=None):
    hv = halves()
    for s in load(SIGNALS):
        if rnd is not None and s["round"] != int(rnd):
            continue
        if half != "all":
            sec = s.get("sector")
            if int(half) == 1 and sec in hv[2]:
                continue
            if int(half) == 2 and sec not in hv[2]:
                continue
        print(f"{s['id']} | {s['source_type']} | {s.get('sector')} | {s.get('pain_summary')} | payer: {s.get('implied_payer')}"
              + (f" | money: {s['money']}" if s.get("money") else ""))


def cmd_problems_brief(half=None):
    hv = halves()
    for p in load(PROBLEMS):
        if half and half != "all":
            sec = p.get("sector")
            if int(half) == 1 and sec in hv[2]:
                continue
            if int(half) == 2 and sec not in hv[2]:
                continue
        print(f"{p['id']} | {p['status']} | {','.join(p.get('source_types') or [])} | {p.get('sector')} | "
              f"{p.get('statement')} | buyer: {p.get('buyer_job_title')}")


def cmd_show_problem(pid):
    sig = {s["id"]: s for s in load(SIGNALS)}
    for p in load(PROBLEMS):
        if p["id"] == pid:
            print(json.dumps({k: v for k, v in p.items() if k not in ("criterion_scores",)}, indent=1, ensure_ascii=False))
            for sid in p.get("signal_ids", []):
                s = sig.get(sid)
                if s:
                    print(f"- {sid} [{s['source_type']}] {s['url']} :: {s.get('quote_or_datapoint')} :: {s.get('pain_summary')}")
            return
    sys.exit(f"no problem {pid}")


# ---------------------------------------------------------------- problems
def types_for(signal_ids, sig):
    return sorted({sig[i]["source_type"] for i in signal_ids if i in sig})


def cmd_merge_clusters(r):
    sig = {s["id"]: s for s in load(SIGNALS)}
    probs = load(PROBLEMS)
    byid = {p["id"]: p for p in probs}
    n_new = n_upd = 0
    seq = 1 + max([int(p["id"].split("-")[-1]) for p in probs if p["id"].startswith(f"R{nn(r)}-P-")] or [0])
    for fp in sorted(glob.glob(os.path.join(wdir(r), "clusters-*.jsonl"))):
        for ln, line in enumerate(open(fp, encoding="utf-8"), 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception as e:
                print(f"!! {fp}:{ln} {e}"); continue
            ids = [i for i in o.get("signal_ids", []) if i in sig]
            if not ids:
                print(f"!! {os.path.basename(fp)}:{ln} no valid signal ids — skipped"); continue
            ex = o.get("existing_problem_id")
            if ex and ex in byid:
                p = byid[ex]
                p["signal_ids"] = sorted(set(p.get("signal_ids", [])) | set(ids))
                p["source_types"] = types_for(p["signal_ids"], sig)
                p["signal_count"] = len(p["signal_ids"])
                n_upd += 1
                continue
            pid = f"R{nn(r)}-P-{seq:03d}"; seq += 1
            p = {"id": pid, "round": int(r), "statement": o.get("statement"),
                 "buyer_job_title": o.get("buyer_job_title"), "sector": o.get("sector"),
                 "signal_ids": sorted(set(ids)), "source_types": types_for(ids, sig),
                 "signal_count": len(set(ids)), "trigger": o.get("trigger"),
                 "solution_form": None, "wedge": None, "status": "pool", "score": None,
                 "criterion_scores": None, "knockouts": None, "notes": o.get("notes", ""), "retries": 0}
            probs.append(p); byid[pid] = p; n_new += 1
    # refresh source types for all
    for p in probs:
        if p.get("signal_ids"):
            p["source_types"] = types_for(p["signal_ids"], sig); p["signal_count"] = len(p["signal_ids"])
    save(PROBLEMS, probs)
    gold = sum(1 for p in probs if len(p.get("source_types") or []) >= 3 and p["status"] == "pool")
    print(f"new problems {n_new}, updated {n_upd}, total {len(probs)}, gold (3+ types) in pool {gold}")


def cmd_import_v1(r, n=15):
    v1 = load(os.path.join(REPO, "v1", "ideas.jsonl"))
    sc = sorted([i for i in v1 if i.get("score") is not None], key=lambda i: -i["score"])[: int(n)]
    probs = load(PROBLEMS); have = {p.get("v1_id") for p in probs}
    k = 0
    for i in sc:
        if i["id"] in have:
            continue
        k += 1
        probs.append({"id": f"R{nn(r)}-V-{k:02d}", "round": int(r), "statement": f"{i['title']} — {i.get('problem')}",
                      "buyer_job_title": i.get("buyer"), "sector": i.get("sector"), "signal_ids": [],
                      "source_types": [], "signal_count": 0, "trigger": None, "solution_form": None, "wedge": None,
                      "status": "candidate", "score": None, "criterion_scores": None, "knockouts": None,
                      "notes": f"from_v1 (v1 score {i['score']}; v1 evidence: v1/evidence/{i['id']}.md)",
                      "tags": ["from_v1"], "v1_id": i["id"], "retries": 0})
    save(PROBLEMS, probs); print(f"imported {k} v1 ideas")


def cmd_select(r, n=40):
    probs = load(PROBLEMS)
    pool = [p for p in probs if p["status"] == "pool" and len(p.get("source_types") or []) >= 2]
    pool.sort(key=lambda p: (-len(p["source_types"]), -p.get("signal_count", 0)))
    chosen = pool[: int(n)]
    for p in chosen:
        p["status"] = "candidate"; p["selected_round"] = int(r)
    save(PROBLEMS, probs)
    for p in chosen:
        print(f"{p['id']} | {len(p['source_types'])} types {','.join(p['source_types'])} | {p['signal_count']} sig | {p['statement'][:110]}")
    print(f"selected {len(chosen)} (pool with >=2 types: {len(pool)})")


def batches(ids, per):
    return [ids[x:x + per] for x in range(0, len(ids), per)]


def cmd_research(r, per=5):
    ids = [p["id"] for p in load(PROBLEMS) if p["status"] == "candidate"]
    b = batches(ids, int(per)); json.dump(b, open(os.path.join(wdir(r), "research.json"), "w"), indent=1)
    for x in b: print(" ".join(x))


SRC_LINE = re.compile(r"\[(S[1-7]|OTHER)\][^\n]*?(https?://[^\s<>\"'`\]\)|]+)", re.I)


def evidence_stats(pid):
    fp = P("evidence", f"{pid}.md")
    if not os.path.exists(fp):
        return None
    txt = open(fp, encoding="utf-8", errors="ignore").read()
    urls = {norm_url(u) for u in URL_RE.findall(txt)}
    types = defaultdict(set)
    sec = txt.split("## Sources", 1)[1] if "## Sources" in txt else txt
    for t, u in SRC_LINE.findall(sec):
        types[t.upper()].add(norm_url(u))
    stypes = sorted(t for t in types if t != "OTHER")
    return {"urls": len(urls), "stypes": stypes, "url_set": urls}


def cmd_researched(r):
    probs = load(PROBLEMS)
    for p in probs:
        if p["status"] == "candidate":
            e = evidence_stats(p["id"])
            if e is None:
                print(f"MISSING evidence {p['id']}"); continue
            p["status"] = "researched"; p["evidence_urls"] = e["urls"]; p["evidence_stypes"] = e["stypes"]
            print(f"{p['id']}: urls={e['urls']} stypes={','.join(e['stypes'])}")
    save(PROBLEMS, probs)


def cmd_judge(r, per=8):
    ids = [p["id"] for p in load(PROBLEMS) if p["status"] == "researched"]
    b = batches(ids, int(per)); json.dump(b, open(os.path.join(wdir(r), "judge.json"), "w"), indent=1)
    for x in b: print(" ".join(x))


def weighted(cs):
    return round(sum(float(cs.get(k, 0)) * W[k] / 10 for k in W), 1)


def cmd_scored(r):
    probs = load(PROBLEMS)
    out = []
    for p in probs:
        if p["status"] not in ("researched",):
            continue
        fp = P("critiques", f"{p['id']}.json")
        if not os.path.exists(fp):
            print(f"MISSING critique {p['id']}"); continue
        try:
            c = json.load(open(fp))
        except Exception as e:
            print(f"!! bad critique {p['id']}: {e}"); continue
        cs = {k: float(c.get("criterion_scores", {}).get(k, 0)) for k in W}
        kos = {k: v for k, v in (c.get("knockouts") or {}).items() if isinstance(v, dict) and v.get("hit")}
        e = evidence_stats(p["id"]) or {"urls": 0, "stypes": [], "url_set": set()}
        vok = sum(1 for v in c.get("verified_urls", []) if str(v.get("result", "")).lower().startswith("ok")
                  and norm_url(v.get("url")) in e["url_set"])
        sok = len({norm_url(v.get("url")) for v in c.get("verified_urls", [])
                   if str(v.get("result", "")).lower().startswith("search-confirmed") and norm_url(v.get("url")) in e["url_set"]})
        tot = weighted(cs)
        p.update({"score": tot, "criterion_scores": cs, "knockouts": sorted(kos) or [],
                  "evidence_urls": e["urls"], "evidence_stypes": e["stypes"], "verified_ok": vok, "search_ok": sok,
                  "solution_form": c.get("solution_form") or p.get("solution_form"),
                  "notes": ("weakest: " + str(c.get("weakest", "")))[:400]})
        if kos:
            p["status"] = "killed"
            p["notes"] = ("KNOCKOUT " + ", ".join(f"{k}: {v.get('reason','')}" for k, v in kos.items()))[:500]
        else:
            p["status"] = "scored"
        out.append((tot, p["id"], p["status"]))
    save(PROBLEMS, probs)
    for t, i, s in sorted(out, reverse=True):
        print(f"{i}: {t} {'' if s == 'scored' else s}")


def gates(p):
    return {"score": (p.get("score") or 0) >= 80, "no_ko": not p.get("knockouts"),
            "urls": (p.get("evidence_urls") or 0) >= 8, "stypes": len(p.get("evidence_stypes") or []) >= 3,
            "fetched": (p.get("verified_ok") or 0) >= 3}


def cmd_qualifiers():
    for p in load(PROBLEMS):
        if p["status"] != "scored":
            continue
        g = gates(p)
        if all(g.values()):
            print(f"QUALIFIES {p['id']} {p['score']} | {p['statement'][:100]}")
        elif all(v for k, v in g.items() if k != "fetched") and (p.get("verified_ok", 0) + p.get("search_ok", 0)) >= 3:
            print(f"PROVISIONAL (needs fetch-verification) {p['id']} {p['score']} ok={p.get('verified_ok')} search={p.get('search_ok')} | {p['statement'][:90]}")
        elif (p.get("score") or 0) >= 80:
            print(f"near: {p['id']} {p['score']} failing {[k for k, v in g.items() if not v]}")


def cmd_verdicts():
    for p in load(PROBLEMS):
        fp = P("devils", f"{p['id']}.md")
        if os.path.exists(fp):
            print(f"{p['id']} [{p['status']}]: {open(fp).readline().strip()[:300]}")


def setst(pid, st, note=None):
    probs = load(PROBLEMS)
    for p in probs:
        if p["id"] == pid:
            p["status"] = st
            if note:
                p["notes"] = (note + " | " + (p.get("notes") or ""))[:600]
            save(PROBLEMS, probs); return p
    sys.exit(f"no problem {pid}")


def cmd_accept(pid):
    setst(pid, "accepted", "ACCEPTED (survived devil's advocate)")
    s = lstate()
    if pid not in s["accepted"]:
        s["accepted"].append(pid)
    sstate(s); print(f"accepted {pid}; total {len(s['accepted'])}")


def cmd_retarget(r, *ids):
    probs = load(PROBLEMS)
    for p in probs:
        if p["id"] in ids:
            p["retries"] = p.get("retries", 0) + 1
            if p["retries"] > 2:
                p["status"] = "parked"; p["notes"] = "parked after 2 re-tries | " + (p.get("notes") or "")
            else:
                p["status"] = "candidate"; p["selected_round"] = int(r)
            print(f"{p['id']} -> {p['status']} (retries {p['retries']})")
    save(PROBLEMS, probs)


def weakest(cs, n=3):
    # weakest by weighted points lost
    lost = sorted(((W[k] * (10 - cs.get(k, 0)) / 10, k) for k in W), reverse=True)
    return ", ".join(f"{k}({WNAMES[k]})={cs.get(k, 0):g}/10" for _, k in lost[:n])


def cmd_top(n, lo=0, hi=100):
    pool = [p for p in load(PROBLEMS) if p["status"] in ("scored", "killed") and p.get("score") is not None
            and float(lo) <= p["score"] <= float(hi)]
    pool.sort(key=lambda p: -p["score"])
    for p in pool[: int(n)]:
        print(f"{p['id']} | {p['score']} | {p['status']} {','.join(p.get('knockouts') or [])} | types={','.join(p.get('evidence_stypes') or [])} | "
              f"{p['statement'][:90]} | weakest: {weakest(p['criterion_scores'])}")


def cmd_stats(r=None):
    probs = [p for p in load(PROBLEMS) if r is None or p.get("selected_round", p["round"]) == int(r) or p["round"] == int(r)]
    print("status:", dict(Counter(p["status"] for p in probs)))
    sc = [p for p in probs if p.get("score") is not None]
    if sc:
        bins = Counter(int(p["score"] // 10 * 10) for p in sc)
        print("score bins:", {f"{b}-{b+9}": bins[b] for b in sorted(bins)})
        print(f"mean {statistics.mean(p['score'] for p in sc):.1f} max {max(p['score'] for p in sc)}")
        print("criterion avg (0-10):", " ".join(f"{k}:{WNAMES[k]}={statistics.mean(p['criterion_scores'][k] for p in sc):.1f}" for k in W))
        print("knockouts:", dict(Counter(k for p in sc for k in (p.get("knockouts") or []))))
    sigs = load(SIGNALS)
    print("signals by type:", dict(Counter(s["source_type"] for s in sigs if r is None or s["round"] == int(r))))


def yield_table():
    sigs = load(SIGNALS); probs = load(PROBLEMS)
    y = {}
    for st in STYPES:
        inp = [p for p in probs if st in (p.get("source_types") or [])]
        y[st] = {"signals": sum(1 for s in sigs if s["source_type"] == st), "in_problems": len(inp),
                 "researched": sum(1 for p in inp if p.get("score") is not None),
                 "score_65_plus": sum(1 for p in inp if (p.get("score") or 0) >= 65),
                 "score_80_plus": sum(1 for p in inp if (p.get("score") or 0) >= 80),
                 "accepted": sum(1 for p in inp if p["status"] == "accepted")}
    return y


def cmd_render():
    s = lstate(); sigs = load(SIGNALS); probs = load(PROBLEMS)
    nsig = Counter(x.get("sector") for x in sigs)
    best = defaultdict(float)
    for p in probs:
        if p.get("score") is not None:
            best[p.get("sector")] = max(best[p.get("sector")], p["score"])
    L = ["# Sectors (v2)", "", "Canonical sector list. Miners must set each signal's `sector` to exactly one of these.",
         "'Times mined' = number of miner assignments. (Auto-generated by v2/tools/bof.py.)", "",
         "| # | Sector | Times mined | Signals | Best problem score |", "|---|---|---|---|---|"]
    for i, sec in enumerate(s["sector_mined"], 1):
        L.append(f"| {i} | {sec} | {s['sector_mined'][sec]} | {nsig.get(sec, 0)} | {best.get(sec, '-') if sec in best else '-'} |")
    other = [k for k in nsig if k not in s["sector_mined"]]
    if other:
        L += ["", "Signals tagged with non-canonical sectors:", ""] + [f"- {k}: {nsig[k]}" for k in sorted(other, key=str)]
    open(P("sectors.md"), "w").write("\n".join(L) + "\n")
    y = yield_table()
    L = ["# Signal source types (v2)", "", "(Auto-generated by v2/tools/bof.py.)", "",
         "| Type | Name | Signals | Problems containing type | Researched | Score ≥65 | Score ≥80 | Accepted |",
         "|---|---|---|---|---|---|---|---|"]
    for st, name in STYPES.items():
        v = y[st]
        L.append(f"| {st} | {name} | {v['signals']} | {v['in_problems']} | {v['researched']} | {v['score_65_plus']} | {v['score_80_plus']} | {v['accepted']} |")
    L += ["", "Definitions: S1 job ads; S2 1–3★ reviews of incumbents; S3 triggers 2025–2028; S4 public tenders & grants;",
          "S5 recurring freelance gigs; S6 forums & communities; S7 enforcement, fines, ombudsman, insurer losses."]
    open(P("sources.md"), "w").write("\n".join(L) + "\n")


def cmd_set_state(r, step):
    s = lstate(); s["round"] = int(r); s["last_completed_step"] = step
    s["accepted"] = [p["id"] for p in load(PROBLEMS) if p["status"] == "accepted"]
    s["source_type_yield"] = yield_table(); s["total_signals"] = len(load(SIGNALS)); s["total_problems"] = len(load(PROBLEMS))
    sstate(s); cmd_render()
    print(json.dumps({k: s[k] for k in ("round", "last_completed_step", "accepted", "total_signals", "total_problems")}))


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    c, rest = a[0], a[1:]
    fn = {"init": cmd_init, "pick-sectors": cmd_pick_sectors, "merge-signals": cmd_merge_signals,
          "signal-urls": cmd_signal_urls, "signals-for": cmd_signals_for, "problems-brief": cmd_problems_brief,
          "show-problem": cmd_show_problem, "merge-clusters": cmd_merge_clusters, "import-v1": cmd_import_v1,
          "select": cmd_select, "research": cmd_research, "researched": cmd_researched, "judge": cmd_judge,
          "scored": cmd_scored, "qualifiers": cmd_qualifiers, "verdicts": cmd_verdicts, "accept": cmd_accept,
          "kill": lambda pid, *x: (setst(pid, "killed", "KILLED: " + " ".join(x)), print("killed", pid)),
          "park": lambda pid, *x: (setst(pid, "parked", "PARKED: " + " ".join(x)), print("parked", pid)),
          "retarget": cmd_retarget, "top": cmd_top, "stats": cmd_stats, "set-state": cmd_set_state,
          "note": lambda *t: (lambda s: (s.__setitem__("notes_for_miners", " ".join(t)), sstate(s)))(lstate()),
          "render": cmd_render}.get(c)
    if not fn:
        print(__doc__); sys.exit(1)
    fn(*rest)


if __name__ == "__main__":
    main()
