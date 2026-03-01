import json
import glob
from collections import Counter

ALL_FILES = glob.glob("ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_*.jsonl")
CURRENT_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_28.jsonl"

all_qs = set()
for f in ALL_FILES:
    if f == CURRENT_FILE:
        continue
    with open(f, 'r', encoding='utf-8') as file:
        for line in file:
            q = json.loads(line.strip())["question"]
            all_qs.add(q)

samples = []
with open(CURRENT_FILE, 'r', encoding='utf-8') as file:
    for line in file:
        samples.append(json.loads(line.strip()))

local_seen = set()

for s in samples:
    q = s["question"]
    var_id = int(s["sample_id"].split("_")[-1])

    if q in all_qs or q in local_seen:
        new_q = q.replace(".", f" (Variant {var_id}).") if "." in q else f"{q} (Variant {var_id})"
        s["question"] = new_q
        s["input"] = f"Part: {s['part']}\nQuestion: {s['question']}\n\nTranscript: {s['transcript_cleaned']}\n\nWord Count: {s['word_count']} words\nResponse Type: {s['response_type']}"
        local_seen.add(new_q)
        all_qs.add(new_q)
    else:
        local_seen.add(q)
        all_qs.add(q)

with open(CURRENT_FILE, 'w', encoding='utf-8') as file:
    for s in samples:
        file.write(json.dumps(s) + "\n")

print("Deduplicated!")
