import json

def analyze_batch(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    print(f"\n=== Analyzing {filename} (Total: {len(data['samples'])}) ===")
    for s in data['samples']:
        print(f"\n--- Sample ID: {s['sample_id']} ---")
        print(f"Question: {s['question']}")
        print(f"Transcript Cleaned: {s['transcript_cleaned']}")
        print(f"Original Transcript: {s['transcript']}")

analyze_batch('batch_104.json')
analyze_batch('batch_105.json')
