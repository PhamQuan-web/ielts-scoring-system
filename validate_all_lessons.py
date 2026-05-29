import json
import os
import glob
import sys

def validate_json_file(filepath):
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"INVALID JSON SYNTAX: {str(e)}"]
    except Exception as e:
        return [f"FILE READ ERROR: {str(e)}"]

    # Basic Schema Checks
    if not data.get('lesson_id'):
        errors.append("Missing or empty 'lesson_id'")
    if not data.get('title'):
        errors.append("Missing or empty 'title'")

    # Image Verification (Strict)
    has_image_url = bool(data.get('image_url'))
    fallback_prompt = data.get('image_prompt_fallback', '')

    # Check at root level (Strategy, Grammar, Writing, etc)
    if 'image_prompt_fallback' in data or 'image_url' in data:
         if not has_image_url and (not fallback_prompt or len(fallback_prompt) < 20):
             errors.append("Root level: 'image_url' is null AND 'image_prompt_fallback' is missing/too short (must be >= 20 chars). Lazy generation detected.")

    # Check inside Vocab Bank (Vocabulary lessons)
    if 'key_vocabulary_bank' in data:
        for i, word in enumerate(data['key_vocabulary_bank']):
            w_url = word.get('image_url')
            w_fallback = word.get('image_prompt_fallback', '')
            if not w_url and (not w_fallback or len(w_fallback) < 20):
                errors.append(f"Vocab '{word.get('word', 'UNKNOWN')}': Missing image and fallback prompt is too short.")

    # Quiz Verification (Strict)
    quizzes = data.get('quiz', [])
    if not quizzes:
        errors.append("Missing 'quiz' section entirely.")
    else:
        for i, q in enumerate(quizzes):
            if not q.get('question'):
                errors.append(f"Quiz {i+1}: Missing question.")
            options = q.get('options', {})
            if len(options) != 4 or not all(k in options for k in ['A', 'B', 'C', 'D']):
                errors.append(f"Quiz {i+1}: Does not have exactly 4 options (A, B, C, D).")
            if not q.get('correct_answer') in ['A', 'B', 'C', 'D']:
                errors.append(f"Quiz {i+1}: 'correct_answer' is invalid or missing.")
            explanation = q.get('explanation', '')
            if not explanation or len(explanation) < 15:
                errors.append(f"Quiz {i+1}: 'explanation' is missing or too short/lazy.")

    return errors

def main():
    target_dir = "output"
    if not os.path.exists(target_dir):
        print(f"Directory '{target_dir}' not found. Ensure you have fetched the branches correctly.")
        sys.exit(1)

    json_files = glob.glob(os.path.join(target_dir, "**/*.json"), recursive=True)
    if not json_files:
        print(f"No JSON files found in '{target_dir}'.")
        sys.exit(1)

    total_files = len(json_files)
    failed_files = 0

    print(f"Starting validation for {total_files} lesson files...\n")

    for filepath in sorted(json_files):
        errors = validate_json_file(filepath)
        if errors:
            failed_files += 1
            print(f"❌ FAILED: {filepath}")
            for err in errors:
                print(f"   - {err}")
        else:
            print(f"✅ PASSED: {filepath}")

    print("-" * 40)
    print(f"Validation Complete.")
    print(f"Total: {total_files} | Passed: {total_files - failed_files} | Failed: {failed_files}")

    if failed_files > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
