import json
import re

def is_vietnamese(text):
    # Check for Vietnamese-specific characters
    vietnamese_chars = r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ]'
    return bool(re.search(vietnamese_chars, text))

def is_instructional(text):
    # Heuristics for instructional text
    keywords = ["modal subject", "example", "prepare", "topic", "chủ đề", "ví dụ", "samples", "model answer"]
    text_lower = text.lower()
    match_count = sum(1 for k in keywords if k in text_lower)
    return match_count >= 2

with open('batch_180.json', 'r') as f:
    data = json.load(f)

print(f"Total samples: {len(data['samples'])}")

valid_candidates = []

for sample in data['samples']:
    transcript = sample.get('transcript_cleaned', '') or sample.get('transcript', '')

    if is_vietnamese(transcript):
        print(f"Skipping {sample['sample_id']} (Vietnamese detected)")
        continue

    if is_instructional(transcript):
        print(f"Skipping {sample['sample_id']} (Instructional detected)")
        continue

    valid_candidates.append(sample)

print("\n--- Valid Candidates ---")
for s in valid_candidates:
    print(f"ID: {s['sample_id']}")
    print(f"Q: {s['question']}")
    print(f"A: {s['transcript']}")
    print("-" * 20)
