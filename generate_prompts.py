import json
import os

PROMPT_DIR = "ielts_lesson_prompts"
os.makedirs(PROMPT_DIR, exist_ok=True)

# Common rules for all Jules
MASTER_RULES = """
# MASTER DIRECTIVES FOR JULES (CRITICAL INSTRUCTIONS)

You are an expert IELTS Content Creator Agent. The user needs you to generate high-quality, strictly accurate IELTS lessons.
Your output will be fed directly into an automated database via a coding agent.

## Core Mandates
1. **ABSOLUTE ACCURACY**: You must not hallucinate grammar rules, definitions, or strategies. If you are unsure about any fact, vocabulary usage, or pronunciation, **you MUST use the `google_search` tool** to check Cambridge/Oxford dictionaries or official IELTS sources (British Council, IDP). The learners are students; errors are unacceptable.
2. **PHASED EXECUTION**: Do NOT try to generate all lessons in a single message. Generate 1 to 3 lessons per turn, save them locally, and wait for the user to say "continue" to do the next batch.
3. **OUTPUT FORMAT**: The output must be valid **JSON files**. Do not output markdown code blocks containing the JSON as your final deliverable. Instead, use Python or Bash to write the JSON content directly to a file (e.g., `lesson_vocab_01.json`).
4. **NO GITHUB UPLOADS**: Do not commit or push to github. Just write the JSON files to the local directory (e.g., `output/`).
5. **IMAGES**: Try to find real, relevant image URLs. If you absolutely cannot find a good URL, provide a highly detailed `image_prompt_fallback` that an AI image generator (like Midjourney) can use.

"""

# Schemas
SCHEMA_VOCAB = """
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
"""

SCHEMA_GRAMMAR = """
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
"""

SCHEMA_STRATEGY = """
## JSON Schema: IELTS Strategy
```json
{
  "lesson_id": "string",
  "title": "string",
  "strategy_problem": "string (Common mistakes/misunderstandings)",
  "core_framework": ["string (Step 1)", "string (Step 2)"],
  "ielts_scenario": "string (Real exam situation)",
  "do_dont_table": {
    "do": ["string"],
    "dont": ["string"]
  },
  "example_application": "string",
  "personal_action_step": "string",
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
"""

SCHEMA_WRITING = """
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
"""

SCHEMA_SPEAKING = """
## JSON Schema: Speaking Foundations
```json
{
  "lesson_id": "string",
  "title": "string",
  "speaking_skill_goal": "string (Part 1, 2, or 3)",
  "answer_framework": "string",
  "useful_phrase_bank": ["string", "string"],
  "weak_vs_better": [
    {
      "weak_answer": "string",
      "better_answer": "string"
    }
  ],
  "fluency_pronunciation_note": "string (if applicable)",
  "sample_ielts_question": "string",
  "model_short_answer": "string",
  "common_mistakes": ["string"],
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
"""

SCHEMA_READ_LISTEN = """
## JSON Schema: Reading/Listening Foundations
```json
{
  "lesson_id": "string",
  "title": "string",
  "skill_goal": "string",
  "question_type_strategy": "string",
  "how_to_recognise": "string",
  "step_by_step_method": ["string", "string"],
  "trap_example": "string (e.g., paraphrase trap, extreme word)",
  "micro_practice_example": "string (3-5 sentences created by you)",
  "review_method": "string",
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
"""

jules_tasks = {
    "Jules_1_Vocab_P1": {
        "description": "Vocabulary & Collocation Part 1 (15 lessons). Focus: Nhóm 1 - Core IELTS Topics, plus first half of Nhóm 2.",
        "schema": SCHEMA_VOCAB,
        "topics": [
            "Education Vocabulary", "Work & Career Vocabulary", "Technology Vocabulary",
            "Environment Vocabulary", "Health Vocabulary", "Society & Culture Vocabulary",
            "Government & Public Services Vocabulary", "Crime & Law Vocabulary",
            "Economy & Money Vocabulary", "Family & Lifestyle Vocabulary",
            "Urbanisation, Housing & Cities Vocabulary", "Media, Advertising & Communication Vocabulary",
            "Opinion Phrases for Writing and Speaking", "Cause and Effect Language", "Advantages and Disadvantages Language"
        ]
    },
    "Jules_2_Vocab_P2": {
        "description": "Vocabulary & Collocation Part 2 (15 lessons). Focus: Second half of Nhóm 2 and Nhóm 3 (Collocation & Naturalness).",
        "schema": SCHEMA_VOCAB,
        "topics": [
            "Problem and Solution Language", "Comparison and Contrast Language", "Trend and Data Description Language",
            "Examples, Evidence and Explanation Language", "Hedging and Precision Language",
            "Academic Verb Collocations", "Adjective + Noun Collocations", "Verb + Noun Collocations",
            "Preposition Patterns in IELTS", "Paraphrasing Common Words", "Avoiding Repetition in Writing",
            "Topic-Specific High-Frequency Collocations", "Natural Speaking Phrases", "Academic Tone for Writing",
            "Vocabulary Error Repair for Vietnamese Learners"
        ]
    },
    "Jules_3_Grammar_P1": {
         "description": "Grammar Part 1 (18 lessons). Focus: Nhóm 1 (The 12 Tenses) and first half of Nhóm 2 (Core Grammar).",
         "schema": SCHEMA_GRAMMAR,
         "topics": [
            "Present Simple for Habits, Facts and General Truths", "Present Continuous for Current and Temporary Situations",
            "Present Perfect for Experience, Change and Unfinished Time", "Present Perfect Continuous for Ongoing Actions",
            "Past Simple for Finished Events", "Past Continuous for Background Actions",
            "Past Perfect for Earlier Past Events", "Past Perfect Continuous for Longer Earlier Actions",
            "Future Simple with Will", "Future with Be Going To and Present Continuous",
            "Future Continuous for Future Progress", "Future Perfect and Future Perfect Continuous",
            "Sentence Structure: Simple, Compound and Complex Sentences", "Subject–Verb Agreement",
            "Articles: A, An, The and Zero Article", "Countable and Uncountable Nouns",
            "Pronouns and Clear Referencing", "Prepositions in IELTS Writing and Speaking"
         ]
    },
    "Jules_4_Grammar_P2": {
         "description": "Grammar Part 2 (18 lessons). Focus: Second half of Nhóm 2, Nhóm 3 (Upgrade), and Nhóm 4 (Application).",
         "schema": SCHEMA_GRAMMAR,
         "topics": [
            "Relative Clauses", "Conditionals", "Passive Voice", "Comparisons", "Modal Verbs", "Reported Speech Basics",
            "Linking Clauses: Although, Because, While and Whereas", "Participle Clauses", "Noun Phrases and Academic Style",
            "Nominalisation", "Parallel Structure", "Punctuation for IELTS Writing", "Inversion Basics",
            "Complex Sentence Control", "Grammar for Task 1 Trends", "Grammar for Task 2 Opinions",
            "Grammar Flexibility for IELTS Speaking", "Common Grammar Mistakes by Vietnamese Learners"
         ]
    },
    "Jules_5_Strategy": {
        "description": "IELTS Strategy (16 lessons). Focus: Understanding IELTS, Study Strategy, Exam Strategy, Band Upgrade Strategy.",
        "schema": SCHEMA_STRATEGY,
        "topics": [
            "IELTS Band Descriptors Explained Simply", "How to Diagnose Your Current Band", "How to Move from Band 5.5 to 6.5",
            "How to Move from Band 6.5 to 7.0", "The IELTS Improvement Loop", "How to Build Ideas Quickly",
            "How to Review Your Own Mistakes", "How to Use AI Feedback Effectively", "Time Management Across the Four Skills",
            "Exam Mindset and Avoiding Panic", "Common Mistakes That Keep Students Below Band 6.5", "How to Build a Weekly Study Plan",
            "How to Use Vocabulary Naturally", "How to Improve Grammar Accuracy", "How to Practise Speaking Alone",
            "How to Review a Mock Test Properly"
        ]
    },
    "Jules_6_Writing": {
        "description": "Writing Foundations (24 lessons). Focus: Basics, Task 2 Core, Task 2 Essay Types, Task 1 Foundations.",
        "schema": SCHEMA_WRITING,
         "topics": [
            "Understanding IELTS Writing Criteria", "Task 2 Question Types", "How to Analyse a Task 2 Question", "How to Plan Before Writing",
            "How to Write a Clear Thesis Statement", "How to Write an Introduction", "How to Build a Body Paragraph",
            "Topic Sentence, Explanation and Example", "Coherence and Cohesion Basics", "How to Use Linking Words Naturally",
            "How to Write a Conclusion", "Common Task 2 Mistakes", "Agree or Disagree Essays", "Discussion Essays",
            "Advantages and Disadvantages Essays", "Problem and Solution Essays", "Two-Part Question Essays", "Counterarguments and Balanced Opinions",
            "Understanding Academic Task 1", "How to Write a Strong Overview", "Line Graphs and Trend Language",
            "Bar Charts, Pie Charts and Comparisons", "Process Diagrams and Maps", "Band 6 to Band 7 Writing Upgrade"
        ]
    },
    "Jules_7_Speaking": {
        "description": "Speaking Foundations (20 lessons). Focus: Basics, Part 2 Long Turn, Part 3 Discussion, Fluency & Pronunciation.",
        "schema": SCHEMA_SPEAKING,
        "topics": [
             "Understanding IELTS Speaking Criteria", "Part 1 Answer Structure", "Extending Part 1 Answers Naturally", "Paraphrasing the Question",
             "How to Build a 2-Minute Answer", "Storytelling Framework for Part 2", "How to Use the 1-Minute Preparation Time",
             "How to Add Details Without Memorising", "Giving Clear Opinions", "Explaining Reasons", "Giving Examples",
             "Comparing and Evaluating", "Speculating About the Future", "Handling Abstract Questions",
             "Fluency: How to Avoid Long Pauses", "Pronunciation Basics for Vietnamese Learners", "Word Stress and Intonation",
             "Natural Speaking Vocabulary", "Safe Idioms and Natural Expressions", "Common Speaking Mistakes and Band 6 to Band 7 Upgrade"
        ]
    },
    "Jules_8_ReadListen": {
        "description": "Reading & Listening Foundations (24 lessons). Focus: Reading (12 lessons), Listening (12 lessons).",
        "schema": SCHEMA_READ_LISTEN,
        "topics": [
            "IELTS Reading Question Types Overview", "Skimming vs Scanning", "Keywords and Paraphrasing", "True / False / Not Given Basics",
            "Matching Headings", "Matching Information", "Multiple Choice Questions", "Sentence Completion",
            "Summary and Note Completion", "Reading Time Management", "Common Reading Traps", "How to Review Reading Mistakes",
            "IELTS Listening Sections Overview", "Predicting Answers Before Listening", "Spelling, Numbers and Dates", "Signposting Language",
            "Dealing with Distractors", "Listening Multiple Choice", "Map and Diagram Labelling", "Form, Note and Table Completion",
            "Matching Questions", "Accents and Pronunciation Awareness", "Concentration and Note-Taking", "How to Review Listening Mistakes with Transcript"
        ]
    }
}

for name, info in jules_tasks.items():
    filepath = os.path.join(PROMPT_DIR, f"{name}.md")
    with open(filepath, "w") as f:
        f.write(f"# YOUR TASK: {info['description']}\n\n")
        f.write(MASTER_RULES)
        f.write("\n## YOUR SPECIFIC TOPICS TO GENERATE\n")
        f.write("You must generate one JSON file per topic below:\n")
        for i, t in enumerate(info['topics'], 1):
            f.write(f"{i}. {t}\n")
        f.write("\n")
        f.write(info['schema'])

print("All prompt files generated successfully.")
