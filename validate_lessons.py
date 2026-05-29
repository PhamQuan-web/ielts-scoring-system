import json
import glob
import os

schema_keys = {
  "lesson_id": str,
  "title": str,
  "speaking_skill_goal": str,
  "answer_framework": str,
  "useful_phrase_bank": list,
  "weak_vs_better": list,
  "fluency_pronunciation_note": str,
  "sample_ielts_question": str,
  "model_short_answer": str,
  "common_mistakes": list,
  "image_url": (str, type(None)),
  "image_prompt_fallback": str,
  "quiz": list
}

def validate_file(filepath):
    print(f"Validating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  [ERROR] Invalid JSON: {e}")
            return False

    is_valid = True
    for key, expected_type in schema_keys.items():
        if key not in data:
            print(f"  [ERROR] Missing key: {key}")
            is_valid = False
        elif not isinstance(data[key], expected_type):
            print(f"  [ERROR] Invalid type for {key}. Expected {expected_type}, got {type(data[key])}")
            is_valid = False

    if is_valid:
        print("  [SUCCESS] Schema validation passed.")
    return is_valid

if __name__ == "__main__":
    files = glob.glob("output/lesson_*.json")
    all_valid = True
    for file in files:
        if not validate_file(file):
            all_valid = False

    if all_valid:
        print("\nAll files are completely valid!")
    else:
        print("\nSome files failed validation.")
