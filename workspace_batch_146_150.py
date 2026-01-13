import json

files = ['batch_146.json', 'batch_147.json', 'batch_148.json', 'batch_149.json', 'batch_150.json']

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
