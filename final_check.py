import json
import glob
import sys

def check_files():
    files = glob.glob("output/lesson_*.json")
    if not files:
        print("No files found!")
        sys.exit(1)

    for filepath in files:
        with open(filepath, 'r') as f:
            data = json.load(f)

            # Check image prompt
            if not data.get("image_prompt_fallback"):
                print(f"[FAIL] {filepath}: Missing image_prompt_fallback")
                sys.exit(1)
            if len(data.get("image_prompt_fallback", "")) < 10:
                 print(f"[FAIL] {filepath}: image_prompt_fallback is too short")
                 sys.exit(1)

            # Check quizzes
            quizzes = data.get("quiz", [])
            if not quizzes:
                print(f"[FAIL] {filepath}: Missing quiz array")
                sys.exit(1)
            for i, q in enumerate(quizzes):
                if not q.get("explanation"):
                    print(f"[FAIL] {filepath}: Quiz {i} missing explanation")
                    sys.exit(1)
                if len(q.get("explanation", "")) < 10:
                    print(f"[FAIL] {filepath}: Quiz {i} explanation is too short")
                    sys.exit(1)

    print("[SUCCESS] All files passed strict quality validation for images and quizzes.")

check_files()
