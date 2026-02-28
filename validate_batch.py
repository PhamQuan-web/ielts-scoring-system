import json
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = {
    "sample_id", "video_id", "part", "question", "transcript_cleaned",
    "word_count", "response_type", "micro_flaws", "grammar_profile",
    "vocab_reason", "grammar_reason", "vocabulary", "grammar",
    "is_valid", "dataset_source", "idiom_present", "risk_level",
    "instruction", "input", "output"
}

def validate_batch(filepath):
    print(f"Validating {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return False

    if not lines:
        print("Error: File is empty.")
        return False

    valid_count = 0
    errors = []

    seen_ids = set()

    for i, line in enumerate(lines, 1):
        try:
            data = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"Line {i}: Invalid JSON - {e}")
            continue

        # Check fields
        missing = REQUIRED_FIELDS - set(data.keys())
        if missing:
            errors.append(f"Line {i}: Missing fields {missing}")

        # Check overall should NOT be present
        if "overall" in data:
             errors.append(f"Line {i}: 'overall' field present (should be removed)")

        # Check types and values
        if not isinstance(data.get("sample_id"), str):
            errors.append(f"Line {i}: sample_id must be string")
        elif data["sample_id"] in seen_ids:
            errors.append(f"Line {i}: Duplicate sample_id {data['sample_id']}")
        else:
            seen_ids.add(data["sample_id"])

        # Word count check
        transcript = data.get("transcript_cleaned", "")
        if not transcript:
             errors.append(f"Line {i}: Empty transcript")

        actual_wc = len(transcript.split())
        claimed_wc = data.get("word_count", 0)
        # Allow small deviation? User said "Ensure word_count matches actual". strict.
        if actual_wc != claimed_wc:
            errors.append(f"Line {i}: Word count mismatch. Claimed {claimed_wc}, Actual {actual_wc}")

        # Input field check
        inp = data.get("input", "")
        if transcript not in inp:
            errors.append(f"Line {i}: Input field does not contain transcript")

        # Output field check
        out = data.get("output", "")
        if not out:
             errors.append(f"Line {i}: Empty output field")

        # Band scores
        if not (4 <= data.get("vocabulary", 0) <= 9):
            errors.append(f"Line {i}: Vocabulary band out of range")
        if not (4 <= data.get("grammar", 0) <= 9):
            errors.append(f"Line {i}: Grammar band out of range")

    if errors:
        print(f"Found {len(errors)} errors:")
        for e in errors[:20]: # Show first 20
            print(e)
        if len(errors) > 20:
            print("...")
        return False
    else:
        print(f"✅ Successfully validated {len(lines)} samples.")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_batch.py <jsonl_file>")
        sys.exit(1)

    success = validate_batch(sys.argv[1])
    if not success:
        sys.exit(1)
