import json

with open('batch_102.json', 'r') as f:
    data = json.load(f)

print(f"Total samples: {len(data['samples'])}")

for s in data['samples']:
    print(f"\n--- Sample ID: {s['sample_id']} (Band {s['band']}) ---")
    print(f"Question: {s['question']}")
    print(f"Transcript Cleaned: {s['transcript_cleaned']}")
    print(f"Original Transcript: {s['transcript']}")
