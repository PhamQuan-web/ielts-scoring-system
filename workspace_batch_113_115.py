import json

files = ['batch_113.json', 'batch_114.json', 'batch_115.json']

for filename in files:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"\n=== Analyzing {filename} (Total: {len(data['samples'])}) ===")
        for s in data['samples']:
            if len(s['transcript_cleaned'].split()) < 5:
                continue

            print(f"\n--- Sample ID: {s['sample_id']} ---")
            print(f"Question: {s['question']}")
            print(f"Transcript Cleaned: {s['transcript_cleaned']}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
