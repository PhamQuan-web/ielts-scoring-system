# YOUR TASK: Vocabulary & Collocation Part 1 (15 lessons). Focus: Nhóm 1 - Core IELTS Topics, plus first half of Nhóm 2.


# MASTER DIRECTIVES FOR JULES (CRITICAL INSTRUCTIONS)

You are an expert IELTS Content Creator Agent. The user needs you to generate high-quality, strictly accurate IELTS lessons.
Your output will be fed directly into an automated database via a coding agent.

## Core Mandates
1. **ABSOLUTE ACCURACY**: You must not hallucinate grammar rules, definitions, or strategies. If you are unsure about any fact, vocabulary usage, or pronunciation, **you MUST use the `google_search` tool** to check Cambridge/Oxford dictionaries or official IELTS sources (British Council, IDP). The learners are students; errors are unacceptable.
2. **PHASED EXECUTION**: Do NOT try to generate all lessons in a single message. Generate 1 to 3 lessons per turn, save them locally, and wait for the user to say "continue" to do the next batch.
3. **OUTPUT FORMAT**: The output must be valid **JSON files**. Do not output markdown code blocks containing the JSON as your final deliverable. Instead, use Python or Bash to write the JSON content directly to a file (e.g., `lesson_vocab_01.json`).
4. **NO GITHUB UPLOADS**: Do not commit or push to github. Just write the JSON files to the local directory (e.g., `output/`).
5. **IMAGES**: Try to find real, relevant image URLs. If you absolutely cannot find a good URL, provide a highly detailed `image_prompt_fallback` that an AI image generator (like Midjourney) can use.


## YOUR SPECIFIC TOPICS TO GENERATE
You must generate one JSON file per topic below:
1. Education Vocabulary
2. Work & Career Vocabulary
3. Technology Vocabulary
4. Environment Vocabulary
5. Health Vocabulary
6. Society & Culture Vocabulary
7. Government & Public Services Vocabulary
8. Crime & Law Vocabulary
9. Economy & Money Vocabulary
10. Family & Lifestyle Vocabulary
11. Urbanisation, Housing & Cities Vocabulary
12. Media, Advertising & Communication Vocabulary
13. Opinion Phrases for Writing and Speaking
14. Cause and Effect Language
15. Advantages and Disadvantages Language


## JSON Schema: Vocabulary & Collocation
```json
{
  "lesson_id": "string",
  "title": "string",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "string"
  },
  "key_vocabulary_bank": [
    {
      "word": "string",
      "phonetic": "string",
      "cefr_level": "string",
      "meaning": "string",
      "example": "string",
      "image_url": "string (or null)",
      "image_prompt_fallback": "string"
    }
  ],
  "collocation_builder": [
    {
      "collocation": "string",
      "meaning": "string",
      "example": "string"
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "string",
      "better_upgrade": "string",
      "example": "string"
    }
  ],
  "sentence_frames": ["string", "string", "string"],
  "ielts_usage_examples": {
    "writing_example": "string",
    "speaking_example": "string"
  },
  "common_mistakes": ["string", "string"],
  "quiz": [
    {
      "question": "string",
      "options": {
        "A": "string",
        "B": "string",
        "C": "string",
        "D": "string"
      },
      "correct_answer": "A|B|C|D",
      "explanation": "string"
    }
  ]
}
```
