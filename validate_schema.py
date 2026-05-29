import json
import jsonschema
import sys
import glob
import os

schema = {
    "type": "object",
    "properties": {
        "lesson_id": {"type": "string"},
        "title": {"type": "string"},
        "grammar_goal": {"type": "string"},
        "core_rule": {
            "type": "object",
            "properties": {
                "formula": {"type": "string"},
                "usage": {"type": "string"},
                "signals": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["formula", "usage", "signals"]
        },
        "when_to_use": {
            "type": "array",
            "items": {"type": "string"}
        },
        "when_not_to_use": {
            "type": "array",
            "items": {"type": "string"}
        },
        "ielts_examples": {
            "type": "object",
            "properties": {
                "writing": {"type": "string"},
                "speaking": {"type": "string"}
            },
            "required": ["writing", "speaking"]
        },
        "repair_section": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "wrong": {"type": "string"},
                    "correct": {"type": "string"},
                    "better_band_upgrade": {"type": "string"}
                },
                "required": ["wrong", "correct", "better_band_upgrade"]
            }
        },
        "vietnamese_learner_mistakes": {
            "type": "array",
            "items": {"type": "string"}
        },
        "mini_sentence_repair_exercise": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "wrong_sentence": {"type": "string"},
                    "correct_sentence": {"type": "string"}
                },
                "required": ["wrong_sentence", "correct_sentence"]
            }
        },
        "image_url": {"type": ["string", "null"]},
        "image_prompt_fallback": {"type": "string"},
        "quiz": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "options": {
                        "type": "object",
                        "properties": {
                            "A": {"type": "string"},
                            "B": {"type": "string"},
                            "C": {"type": "string"},
                            "D": {"type": "string"}
                        },
                        "required": ["A", "B", "C", "D"]
                    },
                    "correct_answer": {
                        "type": "string",
                        "enum": ["A", "B", "C", "D"]
                    },
                    "explanation": {"type": "string"}
                },
                "required": ["question", "options", "correct_answer", "explanation"]
            }
        }
    },
    "required": [
        "lesson_id", "title", "grammar_goal", "core_rule", "when_to_use", "when_not_to_use",
        "ielts_examples", "repair_section", "vietnamese_learner_mistakes",
        "mini_sentence_repair_exercise", "image_url", "image_prompt_fallback", "quiz"
    ]
}

def validate_files():
    files = glob.glob('output/grammar_*.json')
    if not files:
        print("No files found to validate.")
        return False

    all_valid = True
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            jsonschema.validate(instance=data, schema=schema)
            print(f"✅ {file} is valid.")
        except jsonschema.exceptions.ValidationError as e:
            print(f"❌ {file} is invalid: {e.message}")
            all_valid = False
        except json.JSONDecodeError as e:
            print(f"❌ {file} is not valid JSON: {e}")
            all_valid = False
    return all_valid

if __name__ == '__main__':
    if validate_files():
        sys.exit(0)
    else:
        sys.exit(1)
