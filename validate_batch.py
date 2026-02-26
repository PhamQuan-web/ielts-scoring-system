import json, re, sys
from collections import Counter

FILE = sys.argv[1]
FIELDS = ["sample_id","video_id","part","question","transcript_cleaned","word_count",
          "response_type","micro_flaws","grammar_profile","vocab_reason","grammar_reason",
          "vocabulary","grammar","is_valid","dataset_source","idiom_present","risk_level",
          "instruction","input","output"]
errs = 0
samples = []
for i, line in enumerate(open(FILE, encoding="utf-8"), 1):
    if not line.strip(): continue
    try:
        obj = json.loads(line); samples.append(obj)
    except:
        print(f"ERR L{i}: bad JSON"); errs += 1; continue
    for f in FIELDS:
        if f not in obj: print(f"ERR L{i}: missing '{f}'"); errs += 1
    if "overall" in obj: print(f"ERR L{i}: banned 'overall'"); errs += 1
    wc = len(obj.get("transcript_cleaned","").split())
    claimed = obj.get("word_count",0)
    if abs(wc - claimed) > 2: print(f"ERR L{i}: wc {claimed} vs actual {wc}"); errs += 1
    p = obj.get("part",0)
    if p == 2 and wc < 100: print(f"ERR L{i}: Part 2 only {wc}w (min 120)"); errs += 1
    if p == 1 and wc > 90: print(f"ERR L{i}: Part 1 has {wc}w (max 85)"); errs += 1
    sid = obj.get("sample_id","")
    sp = sid.split("_")
    if len(sp) >= 4:
        sv, sg = int(sp[2][1]), int(sp[3][1])
        if sv != obj.get("vocabulary"): print(f"ERR L{i}: ID V{sv} != data V{obj['vocabulary']}"); errs += 1
        if sg != obj.get("grammar"): print(f"ERR L{i}: ID G{sg} != data G{obj['grammar']}"); errs += 1
    t = obj.get("transcript_cleaned","")[:30]
    if t not in obj.get("input",""): print(f"ERR L{i}: input missing transcript"); errs += 1

ids = [s["sample_id"] for s in samples]
dupes = [k for k,v in Counter(ids).items() if v > 1]
if dupes: print(f"ERR: {len(dupes)} duplicate IDs"); errs += len(dupes)
qs = set(s["question"] for s in samples)
if len(qs) < len(samples): print(f"ERR: {len(qs)} unique questions / {len(samples)} (need 100%)"); errs += 1

vd = Counter(s["vocabulary"] for s in samples)
gd = Counter(s["grammar"] for s in samples)
lengths = [len(s["transcript_cleaned"].split()) for s in samples]
print(f"\nSamples: {len(samples)} | Errors: {errs}")
print(f"Vocab: {dict(sorted(vd.items()))}")
print(f"Grammar: {dict(sorted(gd.items()))}")
print(f"Unique Qs: {len(qs)}/{len(samples)}")
if lengths:
    print(f"Words: min={min(lengths)} max={max(lengths)} avg={sum(lengths)//len(lengths)}")
else:
    print(f"Words: min=0 max=0 avg=0")
print(f"\n{'PASS' if errs == 0 else 'FAIL - FIX ERRORS ABOVE'}")
