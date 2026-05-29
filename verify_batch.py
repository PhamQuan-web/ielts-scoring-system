import json
import glob
import jsonschema

schema = {
  "type": "object",
  "properties": {
    "lesson_id": {"type": "string"},
    "title": {"type": "string"},
    "strategy_problem": {"type": "string"},
    "core_framework": {
      "type": "array",
      "items": {"type": "string"}
    },
    "ielts_scenario": {"type": "string"},
    "do_dont_table": {
      "type": "object",
      "properties": {
        "do": {"type": "array", "items": {"type": "string"}},
        "dont": {"type": "array", "items": {"type": "string"}}
      },
      "required": ["do", "dont"]
    },
    "example_application": {"type": "string"},
    "personal_action_step": {"type": "string"},
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
          "correct_answer": {"type": "string", "pattern": "^[A-D]$"},
          "explanation": {"type": "string"}
        },
        "required": ["question", "options", "correct_answer", "explanation"]
      }
    }
  },
  "required": [
    "lesson_id", "title", "strategy_problem", "core_framework",
    "ielts_scenario", "do_dont_table", "example_application",
    "personal_action_step", "image_url", "image_prompt_fallback", "quiz"
  ]
}

for file in glob.glob("output/lesson_*.json"):
    with open(file, 'r') as f:
        data = json.load(f)
        try:
            jsonschema.validate(instance=data, schema=schema)
            print(f"{file} - VALID")
        except jsonschema.exceptions.ValidationError as e:
            print(f"{file} - INVALID: {e.message}")
