import json

scored_file = 'jules_scored_output_101-150.jsonl'
input_file = 'batch_108.json'

with open(input_file, 'r') as f:
    input_data = json.load(f)

# Map sample_id to video_id and ground truth band
video_bands = {}
target_ids = set()
for s in input_data['samples']:
    target_ids.add(s['sample_id'])
    video_bands[s['video_id']] = s['band']

# Parse scored file
scored_data = []
with open(scored_file, 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['sample_id'] in target_ids:
            scored_data.append(data)

if not scored_data:
    print("No scored data found for Batch 108 samples!")
    exit(1)

# Calculate average by video
video_scores = {}
for s in scored_data:
    vid = s['video_id']
    sample_score = (s['grammar'] + s['vocabulary']) / 2.0

    if vid not in video_scores:
        video_scores[vid] = []
    video_scores[vid].append(sample_score)

print("Consistency Report (Batch 108):")
for vid, scores in video_scores.items():
    avg_my_score = sum(scores) / len(scores)
    ground_truth = video_bands.get(vid, 0)
    diff = abs(avg_my_score - ground_truth)

    print(f"Video {vid}: My Avg {avg_my_score:.2f} vs GT {ground_truth} (Diff: {diff:.2f})")

    if diff > 1.0:
        print(f"WARNING: High variance for {vid}")
    else:
        print(f"PASS: {vid}")
