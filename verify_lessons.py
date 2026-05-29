import json
import os

schema_keys = {
    "lesson_id": str,
    "title": str,
    "topic_snapshot": dict,
    "key_vocabulary_bank": list,
    "collocation_builder": list,
    "upgrade_section": list,
    "sentence_frames": list,
    "ielts_usage_examples": dict,
    "common_mistakes": list,
    "quiz": list
}

def validate_file(filepath):
    print(f"Validating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, expected_type in schema_keys.items():
        assert key in data, f"Missing key: {key}"
        assert isinstance(data[key], expected_type), f"Invalid type for key: {key}, expected {expected_type}"

    # topic_snapshot
    assert "target_skills" in data["topic_snapshot"]
    assert "description" in data["topic_snapshot"]

    # key_vocabulary_bank
    for item in data["key_vocabulary_bank"]:
        assert "word" in item
        assert "phonetic" in item
        assert "cefr_level" in item
        assert "meaning" in item
        assert "example" in item
        assert "image_url" in item
        assert "image_prompt_fallback" in item

    # collocation_builder
    for item in data["collocation_builder"]:
        assert "collocation" in item
        assert "meaning" in item
        assert "example" in item

    # upgrade_section
    for item in data["upgrade_section"]:
        assert "weak_phrase" in item
        assert "better_upgrade" in item
        assert "example" in item

    # ielts_usage_examples
    assert "writing_example" in data["ielts_usage_examples"]
    assert "speaking_example" in data["ielts_usage_examples"]

    # quiz
    for item in data["quiz"]:
        assert "question" in item
        assert "options" in item
        assert "A" in item["options"]
        assert "B" in item["options"]
        assert "C" in item["options"]
        assert "D" in item["options"]
        assert "correct_answer" in item
        assert item["correct_answer"] in ["A", "B", "C", "D"]
        assert "explanation" in item

    print(f"✓ {filepath} passed validation!")

import glob

def main():
    files_to_check = glob.glob("output/lesson_vocab_*.json")
    files_to_check.sort()

    if not files_to_check:
        print("No lesson files found in output directory.")
        return

    for f in files_to_check:
        validate_file(f)

if __name__ == "__main__":
    main()
