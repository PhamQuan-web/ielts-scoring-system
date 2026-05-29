import json
import os

lesson_1 = {
  "lesson_id": "reading_01_question_types",
  "title": "IELTS Reading Question Types Overview",
  "skill_goal": "Understand the 14 different question types in the IELTS Reading test and know exactly what skills each type tests.",
  "question_type_strategy": "Different question types require different reading skills. For example, Matching Headings requires understanding the main idea (skimming), while Sentence Completion requires finding specific details (scanning). Always identify the question type before reading the passage.",
  "how_to_recognise": "Look at the instructions. For example, 'Choose NO MORE THAN TWO WORDS from the passage' indicates a completion task. 'Do the following statements agree with the information given...' indicates True/False/Not Given.",
  "step_by_step_method": [
    "1. Read the title and subtitle of the passage to get the context.",
    "2. Quickly look at the first set of questions to identify the question type.",
    "3. Determine whether the questions follow the order of the text (e.g., Multiple Choice, T/F/NG do; Matching types usually do not).",
    "4. Decide which reading skill to use: skimming for general meaning or scanning for specific facts."
  ],
  "trap_example": "Assuming all questions follow the order of the text. Matching questions (Headings, Information, Features) will NOT be in the order of the passage.",
  "micro_practice_example": "The history of the bicycle is fascinating. Early models, like the penny-farthing, were dangerous due to their disproportionately large front wheel. Later, the 'safety bicycle' revolutionised transport with two equal-sized wheels and a chain drive. (Question: What made the penny-farthing dangerous?)",
  "review_method": "When reviewing mistakes, classify them by question type. If you consistently fail Matching Headings, focus on improving your skimming skills and finding topic sentences.",
  "image_url": None,
  "image_prompt_fallback": "A well-organized study desk with an IELTS reading test paper, showing different types of questions highlighted in different colors, soft natural lighting, photorealistic.",
  "quiz": [
    {
      "question": "Which of the following question types usually does NOT follow the order of information in the passage?",
      "options": {
        "A": "True / False / Not Given",
        "B": "Multiple Choice Questions",
        "C": "Matching Information",
        "D": "Sentence Completion"
      },
      "correct_answer": "C",
      "explanation": "Matching questions (Information, Headings, Features) require you to search the whole text and do not follow the chronological order of the passage."
    }
  ]
}

lesson_2 = {
  "lesson_id": "reading_02_skimming_scanning",
  "title": "Skimming vs Scanning",
  "skill_goal": "Master the difference between skimming to understand the main idea and scanning to locate specific information quickly.",
  "question_type_strategy": "Use skimming for Matching Headings and understanding the author's purpose. Use scanning for identifying names, dates, numbers, and specific facts required in Completion tasks and Matching Features.",
  "how_to_recognise": "Skimming involves reading the title, introduction, first sentences of paragraphs (topic sentences), and conclusion. Scanning involves letting your eyes dart over the text looking for a specific visual trigger, like a capital letter or a number.",
  "step_by_step_method": [
    "1. Skimming: Read the title and first paragraph. Then read only the first sentence of each remaining paragraph to grasp the structure.",
    "2. Skimming: Do not stop at unknown words. Your goal is the 'big picture'.",
    "3. Scanning: Identify a clear keyword from the question (e.g., '1995' or 'Dr. Smith').",
    "4. Scanning: Move your eyes quickly across the text, backwards or in a zig-zag, looking ONLY for that specific keyword or its obvious synonym."
  ],
  "trap_example": "Reading every single word (reading for detail) when you should be skimming or scanning. This wastes precious time in the test.",
  "micro_practice_example": "In 1928, Alexander Fleming discovered penicillin. This breakthrough changed modern medicine. However, it wasn't until 1945 that it was mass-produced. (Task: Scan for the year mass production began).",
  "review_method": "Time yourself. Try to skim a full IELTS passage in under 3 minutes, then write a 3-sentence summary of what it was about to test your comprehension.",
  "image_url": None,
  "image_prompt_fallback": "A close-up of a person's eyes moving quickly over a densely printed document, with a magnifying glass hovering over a specific date '1995', illustrating the concept of scanning, cinematic lighting.",
  "quiz": [
    {
      "question": "What is the primary purpose of skimming a text?",
      "options": {
        "A": "To find a specific name or date.",
        "B": "To understand the general idea and layout of the text.",
        "C": "To understand the exact meaning of complex vocabulary.",
        "D": "To read every sentence carefully."
      },
      "correct_answer": "B",
      "explanation": "Skimming is reading quickly to get the gist, main idea, and overall structure of the text, not for finding specific details or reading carefully."
    }
  ]
}

lesson_3 = {
  "lesson_id": "reading_03_keywords_paraphrasing",
  "title": "Keywords and Paraphrasing",
  "skill_goal": "Learn how to identify essential keywords in questions and locate their paraphrased forms in the reading passage.",
  "question_type_strategy": "Paraphrasing is the core skill of IELTS Reading. The exact words in the question will rarely appear in the text. You must train yourself to look for synonyms and structural changes.",
  "how_to_recognise": "Keywords are usually nouns, verbs, or adjectives that carry the meaning. Unchangeable keywords (names, dates) are easy to scan for. Changeable keywords (ideas, descriptions) will almost certainly be paraphrased.",
  "step_by_step_method": [
    "1. Underline the key content words in the question.",
    "2. Identify 'unchangeable' keywords (proper nouns, numbers, unique terms) to scan for the location in the text.",
    "3. Identify 'changeable' keywords (regular verbs, adjectives, nouns) and brainstorm 1-2 quick synonyms in your head.",
    "4. Scan the text for the unchangeable keywords first, then read carefully around that area to find the paraphrased changeable keywords."
  ],
  "trap_example": "The 'Exact Word' Trap. If you see the exact same word in the question and the passage, be careful! It is often a trap to distract you from the true answer which uses a synonym.",
  "micro_practice_example": "Question: The project required significant financial support. \nPassage: The initiative could only proceed with substantial funding from the government. (Notice how 'project' became 'initiative', 'significant' became 'substantial', and 'financial support' became 'funding').",
  "review_method": "Keep a 'Paraphrase Journal'. Every time you do a reading test, write down the words used in the question next to the words used in the passage for the correct answer.",
  "image_url": None,
  "image_prompt_fallback": "A split screen image. On the left side, a piece of paper with the words 'financial support'. On the right side, a dictionary page highlighting the word 'funding', connected by an arrow, showing the concept of synonyms.",
  "quiz": [
    {
      "question": "Why is it dangerous to only look for the exact words from the question in the reading passage?",
      "options": {
        "A": "Because exact words are always the wrong answer.",
        "B": "Because IELTS reading tests your ability to recognize paraphrasing and synonyms, so exact words are often distractors.",
        "C": "Because the text is too long to find exact words.",
        "D": "Because questions never use any words from the text."
      },
      "correct_answer": "B",
      "explanation": "IELTS actively tests your vocabulary through paraphrasing. Examiners often use exact words as traps for lower-level candidates, while the correct answer will use synonyms."
    }
  ]
}

os.makedirs('output', exist_ok=True)

with open('output/lesson_01.json', 'w') as f:
    json.dump(lesson_1, f, indent=2)

with open('output/lesson_02.json', 'w') as f:
    json.dump(lesson_2, f, indent=2)

with open('output/lesson_03.json', 'w') as f:
    json.dump(lesson_3, f, indent=2)

print("Created 3 lesson files successfully.")
