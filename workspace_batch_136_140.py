import json

files = ['batch_136.json', 'batch_137.json', 'batch_138.json', 'batch_139.json', 'batch_140.json']

for filename in files:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"\n=== Analyzing {filename} (Total: {len(data['samples'])}) ===")
        for s in data['samples']:
            # Filtering heuristic
            if len(s['transcript_cleaned'].split()) < 5:
                continue

            print(f"\n--- Sample ID: {s['sample_id']} ---")
            print(f"Question: {s['question']}")
            print(f"Transcript Cleaned: {s['transcript_cleaned']}")
            print(f"Original Transcript: {s['transcript']}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
