import json
import re

# Load batch data
input_file = "batch_182.json"
with open(input_file, 'r') as f:
    batch_data = json.load(f)

# Initialize lists
valid_samples = []
invalid_samples = []

# Filtering logic
for sample in batch_data["samples"]:
    text = sample.get("transcript_cleaned", "").strip()
    original_text = sample.get("transcript_original", "").strip()

    # Skip empty transcripts
    if not text:
        invalid_samples.append({
            "id": sample["sample_id"],
            "reason": "Empty transcript"
        })
        continue

    # Skip procedural/instructional/feedback samples
    # Heuristics:
    # 1. Contains "instructions will be based on"
    # 2. Contains "examiner will stop you"
    # 3. Contains "put on a great performance" (feedback)
    # 4. Short length (< 10 words) AND procedural content

    is_invalid = False

    # Check for specific instructional/feedback phrases
    feedback_phrases = [
        "put on a great performance",
        "examiner will stop you",
        "voice recorder stop",
        "repeat that sentence",
        "talk about it for up to two minutes",
        "have a paper and a pencil"
    ]

    for phrase in feedback_phrases:
        if phrase.lower() in text.lower():
            is_invalid = True
            invalid_samples.append({
                "id": sample["sample_id"],
                "reason": "Instruction/Feedback detected"
            })
            break

    if is_invalid:
        continue

    # Check for short procedural samples
    word_count = len(text.split())
    if word_count < 15:
        # Check if it looks like a valid short answer vs procedural
        # Valid short answer: "I like reading books."
        # Procedural: "Okay thank you." "Yes I am ready."
        is_invalid = True # Assume invalid for now if very short, unless manually verified
        # But wait, some short answers are valid.
        # "I find relaxation in reading." is valid.
        # "He was." is invalid (too short).

        # Let's mark as potentially valid but print for manual review in my thought process
        # For now, I'll include them in valid list but I will manually filter in the next step.
        pass

    valid_samples.append(sample)

# Output summary
print(f"Total samples: {len(batch_data['samples'])}")
print(f"Valid Candidates: {len(valid_samples)}")
print(f"Invalid/Filtered: {len(invalid_samples)}")

print("\n--- Valid Candidates ---")
for s in valid_samples:
    print(f"ID: {s['sample_id']}")
    print(f"Q: {s.get('question', 'N/A')}")
    print(f"Text: {s['transcript_cleaned'][:100]}...")
    print("-" * 20)
