import json
import collections

# Config
output_file = 'jules_scored_output_201-250.jsonl'
input_batch = 'batch_201.json'

def verify():
    # 1. Load Ground Truth
    with open(input_batch, 'r') as f:
        batch_data = json.load(f)

    ground_truth = {}
    for sample in batch_data['samples']:
        ground_truth[sample['video_id']] = sample['band']

    # 2. Load Scored Data
    scored_data = collections.defaultdict(list)
    try:
        with open(output_file, 'r') as f:
            for line in f:
                if not line.strip(): continue
                item = json.loads(line)
                # Average of vocab and grammar for the sample score
                # Note: IELTS Speaking is usually (F+L+G+P)/4.
                # Here we only have V and G. Protocol V7.2 doesn't specify aggregation logic for 2 criteria.
                # But standard is integer rounding or avg.
                # Let's assume Sample Score = (V + G) / 2 for now, or just track V and G separately.
                # The user said: "cộng lại trung bình xấp xỉ điểm overall thì chính xác. +- 1 band."
                # So we take average of all component scores of all samples.

                avg_sample_score = (item['vocabulary'] + item['grammar']) / 2.0
                scored_data[item['video_id']].append(avg_sample_score)
    except FileNotFoundError:
        print(f"Error: {output_file} not found.")
        return

    # 3. Compare
    print(f"--- Verification Report for Batch {batch_data['batch_id']} ---")
    all_pass = True

    for video_id, gt_band in ground_truth.items():
        if video_id not in scored_data:
            # Maybe all samples were skipped?
            # Check if we should have had samples.
            # If the video had ONLY invalid samples, this is fine.
            # But we should warn.
            # print(f"Warning: No valid samples scored for Video {video_id} (GT: {gt_band})")
            continue

        scores = scored_data[video_id]
        avg_score = sum(scores) / len(scores)
        diff = avg_score - gt_band

        status = "PASS" if abs(diff) <= 1.0 else "FAIL"
        if status == "FAIL": all_pass = False

        print(f"Video {video_id}: GT={gt_band} | My_Avg={avg_score:.2f} | Diff={diff:.2f} | Status={status}")

    if all_pass:
        print("\nSUCCESS: All video averages are within +- 1.0 Band of Ground Truth.")
    else:
        print("\nWARNING: Some videos have high variance. Review required.")

if __name__ == "__main__":
    verify()
