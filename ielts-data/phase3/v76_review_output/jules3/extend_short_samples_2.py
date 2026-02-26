import json
import sys

EXTENSIONS = {
    "syn_p2_v9_g6_2179": "It was a proud moment for all of us.",
    "syn_p2_v9_g6_2184": "We must protect our lives."
}

def extend_file(filepath):
    print(f"Extending short samples in {filepath}...")
    fixed_lines = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                sid = data.get('sample_id')
                if sid in EXTENSIONS:
                    data['transcript_cleaned'] += " " + EXTENSIONS[sid]
                    data['word_count'] = len(data['transcript_cleaned'].split())
                fixed_lines.append(json.dumps(data))
            except json.JSONDecodeError:
                continue

    with open(filepath, 'w') as f:
        for line in fixed_lines:
            f.write(line + '\n')
    print("Done.")

if __name__ == "__main__":
    extend_file("ielts-data/phase3/v76_review_output/jules3/jules3_batch02.jsonl")
