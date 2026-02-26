import json
import re
import os

FILES = [
    'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl',
    'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'
]

REQUIRED_FIELDS = [
    "sample_id", "video_id", "part", "question", "transcript_cleaned",
    "word_count", "response_type", "micro_flaws", "grammar_profile",
    "vocab_reason", "grammar_reason", "vocabulary", "grammar",
    "is_valid", "dataset_source", "idiom_present", "risk_level",
    "instruction", "input", "output"
]

def count_words(text):
    clean_text = re.sub(r'[^\w\s]', '', text)
    words = clean_text.split()
    return len(words)

def process_file(filepath):
    print(f"Processing {filepath}...")
    temp_file = filepath + '.temp'
    errors = []
    line_count = 0
    ids = set()

    with open(filepath, 'r') as infile, open(temp_file, 'w') as outfile:
        for line in infile:
            line_count += 1
            if not line.strip():
                continue
            try:
                data = json.loads(line)

                # Fix word count
                transcript = data.get('transcript_cleaned', '')
                actual_count = count_words(transcript)
                if data.get('word_count') != actual_count:
                    data['word_count'] = actual_count
                    if 'input' in data:
                        data['input'] = re.sub(r'Word Count: \d+ words', f'Word Count: {actual_count} words', data['input'])

                # Validation
                missing = [field for field in REQUIRED_FIELDS if field not in data]
                if missing:
                    errors.append(f"Line {line_count}: Missing fields {missing}")

                sample_id = data.get("sample_id")
                if sample_id in ids:
                    errors.append(f"Line {line_count}: Duplicate ID {sample_id}")
                ids.add(sample_id)

                if actual_count < 80:
                     errors.append(f"Line {line_count}: Word count too low ({actual_count})")

                json.dump(data, outfile)
                outfile.write('\n')

            except json.JSONDecodeError:
                errors.append(f"Line {line_count}: Invalid JSON")

    if errors:
        print(f"Errors in {filepath}:")
        for e in errors:
            print(e)
        os.remove(temp_file)
        return False
    else:
        print(f"File {filepath} valid and fixed.")
        os.replace(temp_file, filepath)
        return True

if __name__ == "__main__":
    all_valid = True
    for f in FILES:
        if not process_file(f):
            all_valid = False

    if all_valid:
        print("All files processed successfully.")
    else:
        print("Some files failed validation.")
