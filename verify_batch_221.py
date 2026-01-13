import json

# Output file path
output_file = 'jules_scored_output_201-250.jsonl'
batch_file = 'batch_221.json'

# Load Ground Truth
with open(batch_file, 'r') as f:
    batch_data = json.load(f)

# Create a map of Video ID -> Band (Ground Truth)
video_gt = {}
for sample in batch_data['samples']:
    video_gt[sample['video_id']] = sample['band']

# Load My Scores
my_scores = {}
with open(output_file, 'r') as f:
    for line in f:
        if line.strip():
            item = json.loads(line)
            vid = item['video_id']
            if vid not in my_scores:
                my_scores[vid] = []

            # Calculate average of Vocab + Grammar for this sample
            sample_avg = (item['vocabulary'] + item['grammar']) / 2.0
            my_scores[vid].append(sample_avg)

# Compare
print("\n--- BATCH 221 VERIFICATION ---")
valid_videos = []
for vid, gt in video_gt.items():
    if vid in my_scores:
        scores = my_scores[vid]
        my_avg = sum(scores) / len(scores)
        diff = abs(my_avg - gt)

        status = "PASS" if diff <= 1.0 else "FAIL"
        if status == "FAIL":
            print(f"Video {vid}: GT={gt}, My_Avg={my_avg:.2f} (Diff={diff:.2f}) -> {status}")
            print(f"   Samples: {scores}")
        else:
            valid_videos.append(vid)

print(f"\nPassed Videos: {len(valid_videos)}/{len(video_gt.keys())}")
if len(valid_videos) == len(video_gt.keys()):
    print("ALL CHECKS PASSED.")
else:
    print("WARNING: Some videos failed verification.")
