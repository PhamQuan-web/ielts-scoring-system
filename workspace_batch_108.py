import json

def analyze_batch(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"\n=== Analyzing {filename} (Total: {len(data['samples'])}) ===")
        valid_count = 0
        for s in data['samples']:
            if len(s['transcript_cleaned'].split()) < 5:
                continue

            print(f"\n--- Sample ID: {s['sample_id']} ---")
            print(f"Question: {s['question']}")
            print(f"Transcript Cleaned: {s['transcript_cleaned']}")
            print(f"Original Transcript: {s['transcript']}")
            valid_count += 1
        print(f"Potentially valid samples shown: {valid_count}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

analyze_batch('batch_108.json')
