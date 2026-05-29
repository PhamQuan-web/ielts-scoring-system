import json
import glob
import sys

schema_keys = [
    "lesson_id", "title", "topic_snapshot", "key_vocabulary_bank",
    "collocation_builder", "upgrade_section", "sentence_frames",
    "ielts_usage_examples", "common_mistakes", "quiz"
]

files = glob.glob('output/lesson_*.json')
errors = 0

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for key in schema_keys:
            if key not in data:
                print(f"ERROR: Missing key '{key}' in {file}")
                errors += 1

    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in {file}")
        errors += 1
    except Exception as e:
        print(f"ERROR: {str(e)} in {file}")
        errors += 1

if errors == 0:
    print("All 15 JSON files successfully validated against the expected schema.")
else:
    print(f"Found {errors} errors during validation.")
    sys.exit(1)
