import json
import re

BATCH_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch03.jsonl'

REQUIRED_FIELDS = [
    "sample_id", "video_id", "part", "question", "transcript_cleaned",
    "word_count", "response_type", "micro_flaws", "grammar_profile",
    "vocab_reason", "grammar_reason", "vocabulary", "grammar",
    "is_valid", "dataset_source", "idiom_present", "risk_level",
    "instruction", "input", "output"
]

def validate_batch(filepath):
    print(f"Validating {filepath}...")

    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return False

    print(f"Total lines: {len(lines)}")
    if len(lines) != 100:
        print(f"Warning: Expected 100 lines, found {len(lines)}")

    seen_ids = set()
    errors = 0

    for i, line in enumerate(lines):
        try:
            sample = json.loads(line)
        except json.JSONDecodeError:
            print(f"Line {i+1}: Invalid JSON")
            errors += 1
            continue

        # Check required fields
        missing = [field for field in REQUIRED_FIELDS if field not in sample]
        if missing:
            print(f"Line {i+1} (ID: {sample.get('sample_id', 'Unknown')}): Missing fields {missing}")
            errors += 1

        # Check sample_id
        sid = sample.get('sample_id')
        if not sid:
            print(f"Line {i+1}: Missing sample_id")
            errors += 1
        elif sid in seen_ids:
            print(f"Line {i+1}: Duplicate sample_id {sid}")
            errors += 1
        else:
            seen_ids.add(sid)
            # Check format: syn_p2_vX_gY_NNN
            if not re.match(r'syn_p2_v[4-9]_g[4-9]_\d{3}', sid):
                print(f"Line {i+1}: Invalid sample_id format {sid}")
                errors += 1

        # Check word count
        transcript = sample.get('transcript_cleaned', '')
        wc = sample.get('word_count', 0)
        actual_wc = len(transcript.split())
        if wc != actual_wc:
            print(f"Line {i+1} (ID: {sid}): Word count mismatch. Claimed {wc}, Actual {actual_wc}")
            errors += 1

        # Check input contains transcript
        inp = sample.get('input', '')
        if transcript not in inp:
            print(f"Line {i+1} (ID: {sid}): Input field does not contain transcript")
            errors += 1

        # Check types
        if not isinstance(sample.get('vocabulary'), int):
            print(f"Line {i+1}: Vocabulary score not integer")
            errors += 1
        if not isinstance(sample.get('grammar'), int):
            print(f"Line {i+1}: Grammar score not integer")
            errors += 1

    if errors == 0:
        print("Validation successful! No errors found.")
        return True
    else:
        print(f"Validation failed with {errors} errors.")
        return False

if __name__ == "__main__":
    validate_batch(BATCH_FILE)
