import json

# Define file paths
FILE_P1 = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_18_p1.jsonl"
FILE_P2 = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_18_p2.jsonl"
FINAL_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_18.jsonl"

samples = []

# Read P1
with open(FILE_P1, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            samples.append(json.loads(line))

# Read P2
with open(FILE_P2, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            samples.append(json.loads(line))

# Sort
samples.sort(key=lambda x: x['sample_id'])

# Write
with open(FINAL_FILE, 'w', encoding='utf-8') as f:
    for sample in samples:
        f.write(json.dumps(sample) + '\n')

print(f"Merged {len(samples)} samples into {FINAL_FILE}")
