import json
import sys
import re

REQUIRED_FIELDS = {
    "sample_id", "video_id", "part", "question", "transcript_cleaned",
    "word_count", "response_type", "micro_flaws", "grammar_profile",
    "vocab_reason", "grammar_reason", "vocabulary", "grammar",
    "is_valid", "dataset_source", "idiom_present", "risk_level",
    "instruction", "input", "output"
}

FIXED_INSTRUCTION = "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning."

def validate_line(line, line_num):
    try:
        data = json.loads(line)
    except json.JSONDecodeError as e:
        print(f"ERROR: Line {line_num} is not valid JSON: {e}")
        return False

    # Check fields
    missing_fields = REQUIRED_FIELDS - set(data.keys())
    if missing_fields:
        print(f"ERROR: Line {line_num} is missing fields: {missing_fields}")
        return False

    extra_fields = set(data.keys()) - REQUIRED_FIELDS
    if extra_fields:
        print(f"WARNING: Line {line_num} has extra fields: {extra_fields}")
        # Not a hard fail, but worth noting. Specifically check for 'overall'
        if 'overall' in extra_fields:
             print(f"ERROR: Line {line_num} contains forbidden field 'overall'")
             return False

    # Check fixed values
    if data["part"] != 1:
        print(f"ERROR: Line {line_num} 'part' must be 1")
        return False
    if data["video_id"] != "synthetic":
        print(f"ERROR: Line {line_num} 'video_id' must be 'synthetic'")
        return False
    if data["dataset_source"] != "synthetic":
        print(f"ERROR: Line {line_num} 'dataset_source' must be 'synthetic'")
        return False
    if data["is_valid"] is not True:
        print(f"ERROR: Line {line_num} 'is_valid' must be true")
        return False
    if data["instruction"] != FIXED_INSTRUCTION:
        print(f"ERROR: Line {line_num} 'instruction' does not match fixed string")
        return False

    # Check word count
    transcript = data["transcript_cleaned"]
    actual_word_count = len(transcript.split())
    if abs(actual_word_count - data["word_count"]) > 2: # Allow small margin for hyphenated words etc
        print(f"ERROR: Line {line_num} word_count mismatch. Claimed: {data['word_count']}, Actual: {actual_word_count}")
        return False

    if actual_word_count < 15 or actual_word_count > 95: # Allow slightly wider range for safety, but warn
         print(f"WARNING: Line {line_num} word count {actual_word_count} is outside typical range (20-80)")

    # Check ID format and consistency
    sample_id = data["sample_id"]
    # Expected format: syn_p1_v{V}_g{G}_{GLOBAL_INDEX}
    match = re.match(r"syn_p1_v(\d)_g(\d)_(\d+)", sample_id)
    if not match:
        print(f"ERROR: Line {line_num} sample_id '{sample_id}' has invalid format")
        return False

    v_id, g_id, index_id = map(int, match.groups())

    if v_id != data["vocabulary"]:
        print(f"ERROR: Line {line_num} Vocabulary mismatch. ID says {v_id}, field says {data['vocabulary']}")
        return False
    if g_id != data["grammar"]:
        print(f"ERROR: Line {line_num} Grammar mismatch. ID says {g_id}, field says {data['grammar']}")
        return False

    # Check input format
    expected_input_start = f"Part: 1\nQuestion: {data['question']}\n\nTranscript: {transcript}"
    if not data["input"].startswith(expected_input_start):
         print(f"ERROR: Line {line_num} 'input' field does not start with expected formatted string.")
         return False

    return True

def validate_file(filepath):
    print(f"Validating {filepath}...")
    all_valid = True
    ids_seen = set()

    try:
        with open(filepath, 'r') as f:
            for i, line in enumerate(f, 1):
                if not line.strip(): continue
                if not validate_line(line, i):
                    all_valid = False

                # Check for duplicate IDs
                try:
                    data = json.loads(line)
                    sid = data.get("sample_id")
                    if sid in ids_seen:
                         print(f"ERROR: Line {i} Duplicate sample_id found: {sid}")
                         all_valid = False
                    ids_seen.add(sid)
                except: pass

    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return False

    if all_valid:
        print(f"SUCCESS: {filepath} is valid.")
    else:
        print(f"FAILURE: {filepath} has errors.")
    return all_valid

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_jules3_batch.py <jsonl_file>")
        sys.exit(1)

    validate_file(sys.argv[1])
