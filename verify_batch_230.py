import json

# Input data
batch_file = 'batch_230.json'
output_file = 'jules_scored_output_201-250.jsonl'

# Ground Truth
video_ground_truth = {
    "Ut_jyNrnlYE": 5.5
}

# Load scored data
scored_data = {}
try:
    with open(output_file, 'r') as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                vid = item['video_id']
                if vid not in scored_data:
                    scored_data[vid] = []
                scored_data[vid].append(item)
except FileNotFoundError:
    print("Output file not found.")

# Verify
print(f"--- BATCH 230 VERIFICATION ---")
passed_videos = 0
total_videos = 0

for vid, band in video_ground_truth.items():
    if vid in scored_data:
        total_videos += 1
        samples = scored_data[vid]

        # Calculate average scores
        vocab_scores = [s['vocabulary'] for s in samples]
        grammar_scores = [s['grammar'] for s in samples]

        avg_vocab = sum(vocab_scores) / len(vocab_scores) if vocab_scores else 0
        avg_grammar = sum(grammar_scores) / len(grammar_scores) if grammar_scores else 0

        overall_avg = (avg_vocab + avg_grammar) / 2

        diff = overall_avg - band

        print(f"Video {vid} (GT: {band}): Scored Avg {overall_avg:.2f} (Vocab {avg_vocab:.2f}, Grammar {avg_grammar:.2f})")

        if abs(diff) <= 1.0:
            print(f"  -> PASSED (Diff: {diff:.2f})")
            passed_videos += 1
        else:
            print(f"  -> FAILED (Diff: {diff:.2f}) - Variance too high")

print(f"------------------------------")
print(f"Passed Videos: {passed_videos}/{total_videos}")
