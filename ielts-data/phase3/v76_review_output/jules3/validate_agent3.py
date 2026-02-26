import json
import sys
import re

REQUIRED_FIELDS = {
    'sample_id', 'video_id', 'part', 'question', 'transcript_cleaned', 'word_count',
    'response_type', 'micro_flaws', 'grammar_profile', 'vocab_reason', 'grammar_reason',
    'vocabulary', 'grammar', 'is_valid', 'dataset_source', 'idiom_present', 'risk_level',
    'instruction', 'input', 'output'
}

FORBIDDEN_FIELDS = {'overall'}

def validate_line(line_num, line):
    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        print(f"Line {line_num}: Invalid JSON")
        return False

    errors = []

    # Check fields
    keys = set(data.keys())
    missing = REQUIRED_FIELDS - keys
    forbidden = keys & FORBIDDEN_FIELDS

    if missing:
        errors.append(f"Missing fields: {missing}")
    if forbidden:
        errors.append(f"Forbidden fields present: {forbidden}")

    # Check ID format
    sample_id = data.get('sample_id', '')
    if not re.match(r'^syn_p2_v9_g[5-9]_\d{4}$', sample_id):
        errors.append(f"Invalid sample_id format: {sample_id}")

    # Check word count
    transcript = data.get('transcript_cleaned', '')
    word_count = data.get('word_count', 0)
    actual_count = len(transcript.split())
    if not (80 <= actual_count <= 150):
        errors.append(f"Word count out of range (80-150): {actual_count}")
    if word_count != actual_count:
        errors.append(f"Word count mismatch: claimed {word_count}, actual {actual_count}")

    # Check band scores
    vocab = data.get('vocabulary')
    grammar = data.get('grammar')
    if vocab != 9:
        errors.append(f"Vocabulary must be 9, got {vocab}")

    # Check ID suffix matches grammar score
    id_grammar = int(sample_id.split('_')[3][1]) if '_g' in sample_id else -1
    if grammar != id_grammar:
        errors.append(f"Grammar score {grammar} does not match ID {sample_id}")

    # Check reasoning format
    vocab_reason = data.get('vocab_reason', '')
    grammar_reason = data.get('grammar_reason', '')

    if not vocab_reason.startswith('[LR9]'):
        errors.append(f"vocab_reason must start with [LR9]")
    if not grammar_reason.startswith(f'[GRA{grammar}]'):
        errors.append(f"grammar_reason must start with [GRA{grammar}]")

    if '>Band' not in vocab_reason or 'Not Band' not in vocab_reason:
        errors.append(f"vocab_reason missing comparison structure")
    if '>Band' not in grammar_reason or 'Not Band' not in grammar_reason:
        errors.append(f"grammar_reason missing comparison structure")

    # Check micro_flaws type
    micro_flaws = data.get('micro_flaws')
    if not isinstance(micro_flaws, list):
        errors.append(f"micro_flaws must be a list")

    if errors:
        print(f"Line {line_num} (ID: {sample_id}): " + "; ".join(errors))
        return False
    return True

def validate_file(filepath):
    print(f"Validating {filepath}...")
    valid_count = 0
    with open(filepath, 'r') as f:
        for i, line in enumerate(f, 1):
            if validate_line(i, line):
                valid_count += 1
    print(f"Validation complete. {valid_count} valid samples found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_agent3.py <file.jsonl>")
        sys.exit(1)
    validate_file(sys.argv[1])
