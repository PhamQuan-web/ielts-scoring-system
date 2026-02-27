import json

# Define file paths
FILE_P1 = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_15_part2.jsonl"
FILE_P2 = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_15.jsonl" # This was overwritten by generate_batch_15_p1.py? No, wait.
# generate_batch_15.py wrote to batch_p2_15.jsonl (samples 701-710, short versions)
# generate_batch_15_p1.py wrote to batch_p2_15.jsonl (Samples 701-725, detailed versions) - THIS OVERWROTE THE FIRST ONE. GOOD.
# generate_batch_15_p2.py wrote to batch_p2_15_part2.jsonl (Samples 726-750)

# So we need to merge p1 and p2 into the final file.
FINAL_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_15.jsonl"
PART2_FILE = "ielts-data/phase3/v76_review_output/synthetic_batches/batch_p2_15_part2.jsonl"

# Read samples from the first file (which currently holds 701-725)
samples = []
with open(FINAL_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            samples.append(json.loads(line))

# Read samples from the second file (726-750)
with open(PART2_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            samples.append(json.loads(line))

# Sort by sample_id to be safe
samples.sort(key=lambda x: x['sample_id'])

# Write all back to the final file
with open(FINAL_FILE, 'w', encoding='utf-8') as f:
    for sample in samples:
        f.write(json.dumps(sample) + '\n')

print(f"Merged {len(samples)} samples into {FINAL_FILE}")
