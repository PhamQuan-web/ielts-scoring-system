import json
import glob

files = glob.glob("output/lesson_*.json")
all_passed = True

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        fallback = data.get("image_prompt_fallback", "")
        if not fallback or len(fallback.split()) < 10:
            print(f"❌ {file}: image_prompt_fallback is missing or too short.")
            all_passed = False

        quizzes = data.get("quiz", [])
        for q_idx, quiz in enumerate(quizzes):
            explanation = quiz.get("explanation", "")
            if not explanation or len(explanation.split()) < 5:
                print(f"❌ {file}: Quiz {q_idx} explanation is missing or too short.")
                all_passed = False

    except Exception as e:
         print(f"❌ {file} is INVALID. Error: {e}")
         all_passed = False

if all_passed:
    print("✅ All files passed the strict quality review (image prompts and quiz explanations).")
