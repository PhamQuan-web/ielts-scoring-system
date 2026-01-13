import json

with open('batch_110.json', 'r') as f:
    data = json.load(f)

for s in data['samples']:
    print(f"Sample: {s['sample_id']}")
    print(f"Transcript: {s['transcript']}")
    print(f"Question: {s['question']}")
    print("-" * 20)
