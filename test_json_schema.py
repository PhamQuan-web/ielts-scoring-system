import json
import os
import sys

SCHEMA_KEYS = {
    "lesson_id",
    "title",
    "grammar_goal",
    "core_rule",
    "when_to_use",
    "when_not_to_use",
    "ielts_examples",
    "repair_section",
    "vietnamese_learner_mistakes",
    "mini_sentence_repair_exercise",
    "image_url",
    "image_prompt_fallback",
    "quiz"
}

CORE_RULE_KEYS = {"formula", "usage", "signals"}
IELTS_EXAMPLES_KEYS = {"writing", "speaking"}
REPAIR_SECTION_KEYS = {"wrong", "correct", "better_band_upgrade"}
MINI_EXERCISE_KEYS = {"wrong_sentence", "correct_sentence"}
QUIZ_KEYS = {"question", "options", "correct_answer", "explanation"}

def validate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR: {filepath} is not valid JSON: {e}")
            return False

    is_valid = True

    # Check root keys
    missing_keys = SCHEMA_KEYS - set(data.keys())
    extra_keys = set(data.keys()) - SCHEMA_KEYS
    if missing_keys:
        print(f"ERROR: {filepath} missing root keys: {missing_keys}")
        is_valid = False
    if extra_keys:
        print(f"ERROR: {filepath} has extra root keys: {extra_keys}")
        is_valid = False

    if not is_valid: return False

    # Check core_rule
    if not isinstance(data["core_rule"], dict) or set(data["core_rule"].keys()) != CORE_RULE_KEYS:
        print(f"ERROR: {filepath} core_rule invalid. Expected keys: {CORE_RULE_KEYS}")
        is_valid = False

    # Check ielts_examples
    if not isinstance(data["ielts_examples"], dict) or set(data["ielts_examples"].keys()) != IELTS_EXAMPLES_KEYS:
        print(f"ERROR: {filepath} ielts_examples invalid. Expected keys: {IELTS_EXAMPLES_KEYS}")
        is_valid = False

    # Check repair_section
    if not isinstance(data["repair_section"], list) or len(data["repair_section"]) == 0:
        print(f"ERROR: {filepath} repair_section must be a non-empty list.")
        is_valid = False
    else:
        for item in data["repair_section"]:
            if set(item.keys()) != REPAIR_SECTION_KEYS:
                print(f"ERROR: {filepath} repair_section item invalid. Expected keys: {REPAIR_SECTION_KEYS}")
                is_valid = False

    # Check mini_sentence_repair_exercise
    if not isinstance(data["mini_sentence_repair_exercise"], list) or len(data["mini_sentence_repair_exercise"]) == 0:
        print(f"ERROR: {filepath} mini_sentence_repair_exercise must be a non-empty list.")
        is_valid = False
    else:
        for item in data["mini_sentence_repair_exercise"]:
            if set(item.keys()) != MINI_EXERCISE_KEYS:
                print(f"ERROR: {filepath} mini_sentence_repair_exercise item invalid. Expected keys: {MINI_EXERCISE_KEYS}")
                is_valid = False

    # Check quiz
    if not isinstance(data["quiz"], list) or len(data["quiz"]) == 0:
        print(f"ERROR: {filepath} quiz must be a non-empty list.")
        is_valid = False
    else:
        for item in data["quiz"]:
            if set(item.keys()) != QUIZ_KEYS:
                print(f"ERROR: {filepath} quiz item invalid. Expected keys: {QUIZ_KEYS}")
                is_valid = False
            elif set(item["options"].keys()) != {"A", "B", "C", "D"}:
                print(f"ERROR: {filepath} quiz options invalid. Expected exactly A, B, C, D.")
                is_valid = False
            elif item["correct_answer"] not in ["A", "B", "C", "D"]:
                print(f"ERROR: {filepath} quiz correct_answer must be one of A, B, C, D.")
                is_valid = False

    return is_valid


def main():
    directory = "output/grammar_lessons"
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    all_valid = True
    for file in files:
        filepath = os.path.join(directory, file)
        if not validate_file(filepath):
            all_valid = False
            print(f"Validation FAILED for {file}")
        else:
            print(f"Validation PASSED for {file}")

    if all_valid:
        print("All files passed validation.")
        sys.exit(0)
    else:
        print("Some files failed validation.")
        sys.exit(1)

if __name__ == "__main__":
    main()
