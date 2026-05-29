# YOUR TASK: Grammar Part 2 (18 lessons). Focus: Second half of Nhóm 2, Nhóm 3 (Upgrade), and Nhóm 4 (Application).


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
1. Relative Clauses
2. Conditionals
3. Passive Voice
4. Comparisons
5. Modal Verbs
6. Reported Speech Basics
7. Linking Clauses: Although, Because, While and Whereas
8. Participle Clauses
9. Noun Phrases and Academic Style
10. Nominalisation
11. Parallel Structure
12. Punctuation for IELTS Writing
13. Inversion Basics
14. Complex Sentence Control
15. Grammar for Task 1 Trends
16. Grammar for Task 2 Opinions
17. Grammar Flexibility for IELTS Speaking
18. Common Grammar Mistakes by Vietnamese Learners


## JSON Schema: Grammar
```json
{
  "lesson_id": "string",
  "title": "string",
  "grammar_goal": "string (What does this fix? Which criteria does it boost?)",
  "core_rule": {
    "formula": "string",
    "usage": "string",
    "signals": ["string"]
  },
  "when_to_use": ["string"],
  "when_not_to_use": ["string"],
  "ielts_examples": {
    "writing": "string",
    "speaking": "string"
  },
  "repair_section": [
    {
      "wrong": "string",
      "correct": "string",
      "better_band_upgrade": "string"
    }
  ],
  "vietnamese_learner_mistakes": ["string"],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "string",
      "correct_sentence": "string"
    }
  ],
  "image_url": "string (or null)",
  "image_prompt_fallback": "string",
  "quiz": [
    {
      "question": "string",
      "options": { "A": "string", "B": "string", "C": "string", "D": "string" },
      "correct_answer": "A|B|C|D",
      "explanation": "string"
    }
  ]
}
```
