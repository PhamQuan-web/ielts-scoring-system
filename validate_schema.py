import json
import glob

schema_keys = {
    "lesson_id", "title", "writing_skill_goal", "band_descriptor_link",
    "core_writing_framework", "weak_vs_improved", "step_by_step_build",
    "common_mistakes", "original_ielts_prompt", "model_micro_answer",
    "image_url", "image_prompt_fallback", "quiz"
}

files = glob.glob("output/lesson_*.json")

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        keys = set(data.keys())

        if keys == schema_keys:
            print(f"✅ {file} is valid.")
        else:
            missing = schema_keys - keys
            extra = keys - schema_keys
            print(f"❌ {file} is INVALID.")
            if missing: print(f"  Missing: {missing}")
            if extra: print(f"  Extra: {extra}")

    except Exception as e:
         print(f"❌ {file} is INVALID. Error: {e}")
