# YOUR TASK: Writing Foundations (24 lessons). Focus: Basics, Task 2 Core, Task 2 Essay Types, Task 1 Foundations.


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
1. Understanding IELTS Writing Criteria
2. Task 2 Question Types
3. How to Analyse a Task 2 Question
4. How to Plan Before Writing
5. How to Write a Clear Thesis Statement
6. How to Write an Introduction
7. How to Build a Body Paragraph
8. Topic Sentence, Explanation and Example
9. Coherence and Cohesion Basics
10. How to Use Linking Words Naturally
11. How to Write a Conclusion
12. Common Task 2 Mistakes
13. Agree or Disagree Essays
14. Discussion Essays
15. Advantages and Disadvantages Essays
16. Problem and Solution Essays
17. Two-Part Question Essays
18. Counterarguments and Balanced Opinions
19. Understanding Academic Task 1
20. How to Write a Strong Overview
21. Line Graphs and Trend Language
22. Bar Charts, Pie Charts and Comparisons
23. Process Diagrams and Maps
24. Band 6 to Band 7 Writing Upgrade


## JSON Schema: Writing Foundations
```json
{
  "lesson_id": "string",
  "title": "string",
  "writing_skill_goal": "string",
  "band_descriptor_link": ["Task Response", "Coherence", "Lexical", "Grammar"],
  "core_writing_framework": "string",
  "weak_vs_improved": [
    {
      "weak_version": "string",
      "improved_version": "string",
      "explanation": "string"
    }
  ],
  "step_by_step_build": [
    {
      "step": "string",
      "content": "string"
    }
  ],
  "common_mistakes": ["string"],
  "original_ielts_prompt": "string (Must be 100% original, do not copy Cambridge)",
  "model_micro_answer": "string",
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
