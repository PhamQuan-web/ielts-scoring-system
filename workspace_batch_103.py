import json

with open('batch_103.json', 'r') as f:
    data = json.load(f)

print(f"Total samples: {len(data['samples'])}")

for s in data['samples']:
    # I will NOT print the 'band' here to ensure I am scoring blindly.
    print(f"\n--- Sample ID: {s['sample_id']} ---")
    print(f"Question: {s['question']}")
    print(f"Transcript Cleaned: {s['transcript_cleaned']}")
    print(f"Original Transcript: {s['transcript']}")
