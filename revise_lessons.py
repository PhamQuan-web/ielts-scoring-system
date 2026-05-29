import json
import os

# Lesson 1: Very detailed because there are many question types
lesson_1 = {
  "lesson_id": "reading_01_question_types",
  "title": "IELTS Reading Question Types Overview",
  "skill_goal": "Understand the 14 different question types in the IELTS Reading test and know exactly what skills each type tests, focusing on which questions follow the chronological order of the text.",
  "question_type_strategy": "The IELTS Reading test features 14 specific task types. Broadly, they fall into three categories: 'Order' questions (answers appear chronologically in the text, like Multiple Choice or True/False/Not Given), 'Non-Order' questions (like Matching Headings or Matching Information, where you must scan the whole text), and 'Completion' questions (like Summaries or Flowcharts, which may be localized to one paragraph). Recognizing the type immediately dictates whether you should skim, scan, or read for deep detail.",
  "how_to_recognise": "Always read the instructions carefully. 'Choose NO MORE THAN TWO WORDS' indicates a completion task with a strict word limit. 'Do the following statements agree with the views of the writer...' indicates a YES/NO/NOT GIVEN task, which focuses on opinions rather than facts.",
  "step_by_step_method": [
    "1. Read the main title, subtitle, and any accompanying graphs to grasp the overall topic within 10 seconds.",
    "2. Immediately skip to the first group of questions. Identify the question type (e.g., Matching Headings).",
    "3. Determine the 'order' status: Will these answers appear in order? If it is a matching task, the answer is NO.",
    "4. Decide on your reading strategy: If it's a detail question (e.g., Short Answer), scan for keywords. If it's a global question (e.g., Matching Headings), skim the first sentence of every paragraph.",
    "5. Group your questions: Try to keep a keyword from a detail question in your mind while skimming for a global question to save time."
  ],
  "trap_example": "The 'Order Assumption' Trap: Many students assume all questions follow the text. If you are doing a 'Matching Information to Paragraphs' task and expect the answer to question 1 to be in paragraph A, you will waste immense amounts of time.",
  "micro_practice_example": "The history of the bicycle is fascinating. Early models, like the penny-farthing, were dangerous due to their disproportionately large front wheel. Later, the 'safety bicycle' revolutionised transport with two equal-sized wheels and a chain drive. (Task: Identify if this is a chronological description or a comparison of safety features. Answer: It is chronological history leading to safety improvements).",
  "review_method": "When reviewing mistakes, create a tally chart of the question types you get wrong most often. If you consistently fail T/F/NG, you need to study logic and inferences. If you fail Summary Completion, you need to work on scanning and grammar matching.",
  "image_url": None,
  "image_prompt_fallback": "A highly detailed, well-organized study desk showing an IELTS reading test paper. The paper has 3 different sections highlighted in neon yellow, pink, and green, demonstrating different question types. Soft natural lighting, 4k, photorealistic.",
  "quiz": [
    {
      "question": "Which of the following question types usually does NOT follow the chronological order of information in the reading passage?",
      "options": {
        "A": "True / False / Not Given",
        "B": "Multiple Choice Questions",
        "C": "Matching Information to Paragraphs",
        "D": "Sentence Completion"
      },
      "correct_answer": "C",
      "explanation": "Matching questions (Information, Headings, Features) require you to search the whole text and do not follow the chronological order of the passage. T/F/NG and Multiple Choice almost always follow the text's order."
    }
  ]
}

# Lesson 2: Keep it concise, as it's a straightforward skill comparison
lesson_2 = {
  "lesson_id": "reading_02_skimming_scanning",
  "title": "Skimming vs Scanning",
  "skill_goal": "Master the difference between skimming to understand the main idea and scanning to locate specific information quickly.",
  "question_type_strategy": "Skimming is your macro-tool (used for Matching Headings and understanding the author's purpose). Scanning is your micro-tool (used for identifying names, dates, numbers, and specific facts required in Completion tasks).",
  "how_to_recognise": "Skimming involves reading the title, introduction, first sentences of paragraphs (topic sentences), and the conclusion. Scanning involves letting your eyes dart over the text looking for a specific visual trigger, like a capital letter, a number, or a highly specific noun.",
  "step_by_step_method": [
    "1. Skimming: Read the title and first paragraph completely. Then read only the first sentence of each remaining paragraph.",
    "2. Skimming: Force your eyes forward. Do not stop at unknown words. Your goal is the 'big picture' structure.",
    "3. Scanning: Identify a highly specific keyword from the question (e.g., '1995', 'Dr. Smith', or 'Photosynthesis').",
    "4. Scanning: Move your eyes quickly across the text, backwards or in a zig-zag, looking ONLY for that specific keyword. Do not actually 'read' the sentences until you find the word."
  ],
  "trap_example": "The 'Reading Every Word' Trap: Treating an IELTS Reading passage like a novel. If you read every word for detail, you will run out of time before reaching Passage 3.",
  "micro_practice_example": "In 1928, Alexander Fleming discovered penicillin. This breakthrough changed modern medicine. However, it wasn't until 1945 that it was mass-produced. (Task: Scan for the year mass production began. Answer: 1945).",
  "review_method": "Time yourself. Try to skim a full 900-word IELTS passage in under 3 minutes, then verbally summarize the main point of each paragraph.",
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

# Lesson 3: Detailed because paraphrasing is the core of the entire IELTS exam
lesson_3 = {
  "lesson_id": "reading_03_keywords_paraphrasing",
  "title": "Keywords and Paraphrasing",
  "skill_goal": "Learn how to identify essential keywords in questions and accurately locate their heavily paraphrased forms within the reading passage.",
  "question_type_strategy": "Paraphrasing is the ultimate core skill of the IELTS exam. The exact words used in the question will rarely appear in the text. You must train your brain to look for synonyms, antonyms, and grammatical structural changes (e.g., changing an active voice sentence to passive voice, or a noun to an adjective).",
  "how_to_recognise": "Keywords are divided into two types. 'Unchangeable' keywords (proper nouns, dates, scientific terms) cannot be paraphrased easily and are perfect for scanning. 'Changeable' keywords (regular verbs, adjectives, common nouns) carry the meaning and will almost certainly be paraphrased by the examiner.",
  "step_by_step_method": [
    "1. Underline the key content words in the question.",
    "2. Categorize them: Find the 'unchangeable' keywords to use as your anchor points for scanning.",
    "3. Identify the 'changeable' keywords. Before looking at the text, take 5 seconds to brainstorm 1-2 possible synonyms (e.g., if the question says 'global', think 'worldwide' or 'international').",
    "4. Scan the text rapidly for your unchangeable anchor words.",
    "5. Once you locate the area, slow down and read carefully to find the paraphrased versions of your changeable keywords."
  ],
  "trap_example": "The 'Exact Word Distractor' Trap. Examiners deliberately place exact words from the question into the wrong paragraph. If you see the exact same adjective or verb in the text, be highly suspicious. The correct answer is usually hidden behind a synonym.",
  "micro_practice_example": "Question: The project required significant financial support. \nPassage: The initiative could only proceed with substantial funding from the local government. (Analysis: 'project' -> 'initiative', 'required' -> 'could only proceed with', 'significant' -> 'substantial', 'financial support' -> 'funding').",
  "review_method": "Keep a dedicated 'Paraphrase Journal'. After taking a practice test, write down the phrase from the question on the left, and the exact phrase used in the passage on the right. Review this list weekly.",
  "image_url": None,
  "image_prompt_fallback": "A split screen image. On the left side, a piece of paper with the words 'financial support'. On the right side, a dictionary page highlighting the word 'funding', connected by a glowing arrow, showing the concept of synonyms and paraphrasing.",
  "quiz": [
    {
      "question": "Why is it dangerous to only scan for the exact words from the question in the reading passage?",
      "options": {
        "A": "Because exact words are always the wrong answer.",
        "B": "Because IELTS reading primarily tests your ability to recognize paraphrasing and synonyms, meaning exact words are often used as deliberate distractors.",
        "C": "Because the text is too long to find exact words.",
        "D": "Because questions never use any words from the text."
      },
      "correct_answer": "B",
      "explanation": "IELTS actively tests your vocabulary through paraphrasing. Examiners often use exact words as traps to trick lower-level candidates who are just matching words visually, rather than understanding meaning."
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

print("Revised 3 lesson files successfully.")
