import json

scored_file = 'jules_scored_output_101-150.jsonl'
input_files = ['batch_109.json', 'batch_110.json', 'batch_111.json', 'batch_112.json']

# Collect ground truth from both input files
video_bands = {}
target_ids = set()

for fpath in input_files:
    try:
        with open(fpath, 'r') as f:
            data = json.load(f)
            for s in data['samples']:
                target_ids.add(s['sample_id'])
                video_bands[s['video_id']] = s['band']
    except FileNotFoundError:
        pass

# Parse scored file
scored_data = []
with open(scored_file, 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['sample_id'] in target_ids:
            scored_data.append(data)

if not scored_data:
    print("No scored data found for Batches 109-112!")
    exit(1)

# Calculate average by video
video_scores = {}
for s in scored_data:
    vid = s['video_id']
    sample_score = (s['grammar'] + s['vocabulary']) / 2.0

    if vid not in video_scores:
        video_scores[vid] = []
    video_scores[vid].append(sample_score)

print("Consistency Report (Batches 109-112):")
for vid, scores in video_scores.items():
    avg_my_score = sum(scores) / len(scores)
    ground_truth = video_bands.get(vid, 0)
    diff = abs(avg_my_score - ground_truth)

    print(f"Video {vid}: My Avg {avg_my_score:.2f} vs GT {ground_truth} (Diff: {diff:.2f})")

    if diff > 1.0:
        print(f"WARNING: High variance for {vid}")
    else:
        print(f"PASS: {vid}")
