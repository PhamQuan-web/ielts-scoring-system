# YOUR TASK: Vocabulary & Collocation Part 2 (15 lessons). Focus: Second half of Nhóm 2 and Nhóm 3 (Collocation & Naturalness).


# MASTER DIRECTIVES FOR JULES (CRITICAL INSTRUCTIONS)

You are an expert IELTS Content Creator Agent. The user needs you to generate high-quality, strictly accurate IELTS lessons.
Your output will be fed directly into an automated database via a coding agent.

## Core Mandates
1. **ABSOLUTE ACCURACY**: You must not hallucinate grammar rules, definitions, or strategies. If you are unsure about any fact, vocabulary usage, or pronunciation, **you MUST use the `google_search` tool** to check Cambridge/Oxford dictionaries or official IELTS sources (British Council, IDP). The learners are students; errors are unacceptable.
2. **PHASED EXECUTION**: Do NOT try to generate all lessons in a single message. Generate 1 to 3 lessons per turn, save them locally, and wait for the user to say "continue" to do the next batch.
3. **OUTPUT FORMAT**: The output must be valid **JSON files**. Do not output markdown code blocks containing the JSON as your final deliverable. Instead, use Python or Bash to write the JSON content directly to a file (e.g., `lesson_vocab_01.json`).
4. **GITHUB UPLOADS REQUIRED**: You MUST commit and push your generated JSON files to a remote github branch. Do not just leave them locally. Name your branch logically based on your task (e.g., `feat/ielts-lessons-vocab-part1`).
5. **IMAGES**: Try to find real, relevant image URLs. If you absolutely cannot find a good URL, provide a highly detailed `image_prompt_fallback` that an AI image generator (like Midjourney) can use.


## YOUR SPECIFIC TOPICS TO GENERATE
You must generate one JSON file per topic below:
1. Problem and Solution Language
2. Comparison and Contrast Language
3. Trend and Data Description Language
4. Examples, Evidence and Explanation Language
5. Hedging and Precision Language
6. Academic Verb Collocations
7. Adjective + Noun Collocations
8. Verb + Noun Collocations
9. Preposition Patterns in IELTS
10. Paraphrasing Common Words
11. Avoiding Repetition in Writing
12. Topic-Specific High-Frequency Collocations
13. Natural Speaking Phrases
14. Academic Tone for Writing
15. Vocabulary Error Repair for Vietnamese Learners


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
