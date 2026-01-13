import json

files = ['batch_111.json', 'batch_112.json']

for filename in files:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"\n=== {filename} Samples ===")
        for s in data['samples']:
            if len(s['transcript_cleaned'].split()) > 5:
                print(f"ID: {s['sample_id']} | Len: {len(s['transcript_cleaned'].split())}")
    except FileNotFoundError:
        print(f"File {filename} not found")
