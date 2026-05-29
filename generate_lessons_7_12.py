import json
import os

lesson_7 = {
  "lesson_id": "reading_07_multiple_choice",
  "title": "Multiple Choice Questions",
  "skill_goal": "Learn how to eliminate distractor options and identify the subtle differences between four similar choices.",
  "question_type_strategy": "Multiple choice questions usually follow the order of the text. The key strategy is 'process of elimination'. Examiners will always include one option that contradicts the text, one that is not mentioned, and one that is a 'half-truth' (partially correct but missing a key element).",
  "how_to_recognise": "The instructions ask you to 'Choose the correct letter, A, B, C or D'. Sometimes, you may be asked to choose TWO letters from five options.",
  "step_by_step_method": [
    "1. Read the question stem only, NOT the options. The options will confuse you before you read the text.",
    "2. Identify keywords in the question stem and locate the relevant section in the text.",
    "3. Read that section carefully and try to answer the question in your own words first.",
    "4. Now look at the options A, B, C, D. Eliminate the obviously wrong ones.",
    "5. Compare the remaining options closely against the specific words in the text."
  ],
  "trap_example": "The 'Half-Truth' Trap. An option might contain exact words from the text, but it pairs them with a word like 'always' or 'all', changing the meaning entirely from the original text which might have said 'sometimes' or 'some'.",
  "micro_practice_example": "Text: While early critics dismissed the new painting style as amateurish, the general public embraced it enthusiastically within a few years. \nQuestion: How did people react to the new painting style? \nA. Everyone hated it at first. \nB. Critics eventually learned to love it. \nC. Regular people quickly grew to like it. \nD. It was immediately popular with all art experts. \n(Answer: C. 'Regular people' = 'general public', 'quickly grew to like it' = 'embraced it enthusiastically within a few years').",
  "review_method": "For every multiple-choice question you get wrong, write down exactly why the distractor you chose was wrong (e.g., 'Option B used the word *only*, but the text didn't').",
  "image_url": None,
  "image_prompt_fallback": "A close-up of a pencil crossing out three incorrect options (A, B, and D) on a multiple-choice test, leaving option C circled. The focus is on the process of elimination.",
  "quiz": [
    {
      "question": "Why is it usually a bad idea to read the options (A, B, C, D) before reading the text?",
      "options": {
        "A": "It takes too much time.",
        "B": "The options are designed to trick you; reading them first plants false information in your mind.",
        "C": "The options will not contain any keywords.",
        "D": "You should just guess the answer anyway."
      },
      "correct_answer": "B",
      "explanation": "Three out of the four options are deliberately written by examiners as plausible-sounding traps. Reading them first biases your understanding of the passage."
    }
  ]
}

lesson_8 = {
  "lesson_id": "reading_08_sentence_completion",
  "title": "Sentence Completion",
  "skill_goal": "Master the art of scanning for specific facts while adhering strictly to grammatical rules and word count limits.",
  "question_type_strategy": "This task tests your ability to find specific details and copy them accurately. The sentences in the question will paraphrase the text, but the word(s) you write in the blank MUST be taken exactly from the text without changing their form.",
  "how_to_recognise": "Instructions will say: 'Complete the sentences below. Choose NO MORE THAN TWO WORDS from the passage for each answer.'",
  "step_by_step_method": [
    "1. Highlight the word limit instruction (e.g., ONE WORD ONLY).",
    "2. Read the incomplete sentence and predict the *type* of word needed (e.g., noun, verb, date) and guess possible answers.",
    "3. Identify scan-able keywords in the sentence.",
    "4. Scan the text to locate the paraphrased sentence.",
    "5. Find the exact word(s) in the text that fill the blank grammatically.",
    "6. Check your word count."
  ],
  "trap_example": "The 'Word Count Violation' Trap. If the limit is 'ONE WORD ONLY' and the text says 'bright red car', you cannot write 'red car' (2 words). You must choose the most essential word, which is 'car'. Also, hyphenated words like 'state-of-the-art' count as ONE word.",
  "micro_practice_example": "Limit: NO MORE THAN TWO WORDS. \nText: The ancient Romans constructed complex aqueducts to provide a steady supply of fresh water to their sprawling cities. \nQuestion: The Romans built ______________ to ensure their cities had water. \n(Answer: 'complex aqueducts' OR 'aqueducts'. 'fresh water' is wrong because they built the aqueducts, not the water).",
  "review_method": "Always double-check the grammar of your completed sentence. Read it aloud in your head. If it sounds grammatically incorrect, you chose the wrong word from the text.",
  "image_url": None,
  "image_prompt_fallback": "A visual representation of filling in a blank puzzle piece. The puzzle piece has the word 'aqueduct' on it, and it fits perfectly into a gap in a printed sentence.",
  "quiz": [
    {
      "question": "If the instruction says 'NO MORE THAN TWO WORDS', how many words does the hyphenated term 'long-term' count as?",
      "options": {
        "A": "One word",
        "B": "Two words",
        "C": "Three words",
        "D": "It depends on the context."
      },
      "correct_answer": "A",
      "explanation": "In the IELTS test, hyphenated words (words joined by a dash like 'part-time' or 'state-of-the-art') are always counted as a single word."
    }
  ]
}

lesson_9 = {
  "lesson_id": "reading_09_summary_completion",
  "title": "Summary and Note Completion",
  "skill_goal": "Learn how to navigate summaries that condense multiple paragraphs, deciding whether to use exact words from the text or choose from a given list.",
  "question_type_strategy": "A summary condenses a section of the text. It usually covers 2-3 specific paragraphs rather than the whole passage. The key is finding where the summary begins in the text and tracking the paraphrasing sentence by sentence.",
  "how_to_recognise": "You will see a paragraph with multiple blanks. There are two variations: Type A requires you to pick words directly from the text. Type B provides a box of words (synonyms) to choose from.",
  "step_by_step_method": [
    "1. Read the title of the summary if there is one—it tells you exactly which part of the text to scan for.",
    "2. Read the entire summary first to get the overall meaning.",
    "3. Predict the grammar (noun/verb/adjective) and meaning for each blank.",
    "4. Use names, dates, or unique nouns in the summary to locate the correct paragraphs in the text.",
    "5. If it's Type B (with a box), find the word in the text first, THEN look in the box for its synonym."
  ],
  "trap_example": "The 'Box Synonym' Trap in Type B summaries. The exact word you find in the text will almost never be in the box. If the text says ' plummet ', the answer in the box will be 'decrease'. Do not waste time looking for the exact word in the box.",
  "micro_practice_example": "Text: The CEO decided to terminate the project immediately due to unforeseen financial constraints. \nSummary Box Options: [A. start] [B. cancel] [C. delay] [D. budget] \nSummary: The initiative had to be ________ because of money problems. \n(Answer: B. 'terminate' in the text matches 'cancel' in the box).",
  "review_method": "For Type B summaries, create a synonym map mapping the exact word from the text to the correct option in the box to train your vocabulary recognition.",
  "image_url": None,
  "image_prompt_fallback": "A graphic showing a large paragraph being funnelled down into a smaller, condensed paragraph with blanks, illustrating the concept of summarization.",
  "quiz": [
    {
      "question": "When doing a summary completion task that provides a box of word options, what should you do first?",
      "options": {
        "A": "Try to guess the answers from the box without reading the text.",
        "B": "Find the answer in the text first, then look for its synonym in the box.",
        "C": "Read the box options first to memorize them.",
        "D": "Look for the exact words from the box in the reading passage."
      },
      "correct_answer": "B",
      "explanation": "The words in the box are usually synonyms of the words in the text. Finding the concept in the passage first ensures you understand the context before choosing the matching synonym from the box."
    }
  ]
}

lesson_10 = {
  "lesson_id": "reading_10_time_management",
  "title": "Reading Time Management",
  "skill_goal": "Develop a strict pacing strategy to ensure you complete all 40 questions within the 60-minute limit.",
  "question_type_strategy": "Time is the biggest enemy in IELTS Reading. You have 60 minutes for 3 passages. However, the passages get progressively more difficult. Spending 20 minutes on Passage 1 is a fatal mistake.",
  "how_to_recognise": "This is an overarching strategy, not a specific question type.",
  "step_by_step_method": [
    "1. Allocate your time unequally: Aim for 15 minutes on Passage 1 (easiest), 20 minutes on Passage 2, and 25 minutes on Passage 3 (hardest).",
    "2. Never spend more than 1.5 minutes looking for a single answer. If you can't find it, mark it with a star, guess an answer, and move on.",
    "3. Transfer your answers to the answer sheet directly after finishing each passage. Do not wait until the end.",
    "4. Do the easiest questions first. Detail questions (scanning) are faster than global questions (Matching Headings)."
  ],
  "trap_example": "The 'Stubbornness' Trap. Spending 5 minutes looking for the answer to Question 3 because you 'know it's right there'. Those 5 minutes cost you the chance to answer three easier questions at the end of the test.",
  "micro_practice_example": "Scenario: You are on Question 12. It's a tricky T/F/NG question and you've looked for 2 minutes. \nAction: Guess 'Not Given', circle question 12 on your paper so you can return to it if you have spare time at the end, and immediately start Question 13.",
  "review_method": "Always practice with a strict stopwatch. Write down your completion times for P1, P2, and P3 to identify where you are slowing down.",
  "image_url": None,
  "image_prompt_fallback": "A dynamic image of a stopwatch split into three unequal sections labeled Passage 1 (15m), Passage 2 (20m), and Passage 3 (25m), conveying urgency and strategy.",
  "quiz": [
    {
      "question": "What is the recommended time distribution for the three IELTS Reading passages?",
      "options": {
        "A": "20 minutes for each passage.",
        "B": "10 minutes for Passage 1, 20 for Passage 2, 30 for Passage 3.",
        "C": "15 minutes for Passage 1, 20 minutes for Passage 2, and 25 minutes for Passage 3.",
        "D": "Spend all your time on Passages 1 and 2 to ensure high accuracy, and guess Passage 3."
      },
      "correct_answer": "C",
      "explanation": "Because Passage 3 contains the most complex vocabulary and arguments, it naturally requires more time. You must speed through the easier Passage 1 to bank time for the end."
    }
  ]
}

lesson_11 = {
  "lesson_id": "reading_11_common_traps",
  "title": "Common Reading Traps",
  "skill_goal": "Identify and systematically avoid the psychological and linguistic tricks examiners use to mislead candidates.",
  "question_type_strategy": "IELTS Reading tests your attention to detail. Examiners design traps for students who read superficially or rush.",
  "how_to_recognise": "Look for absolute words ('all', 'always', 'never'), slight modifications in meaning, and exact word matches from the text used in wrong contexts.",
  "step_by_step_method": [
    "1. The Absolute Word Trap: Be highly suspicious of options containing 'always', 'never', 'only', or 'all'. The text usually uses softer words like 'often', 'rarely', 'mostly', or 'some'.",
    "2. The Exact Match Trap: If an option uses the exact same words as the passage, it's often a distractor. The correct answer usually uses synonyms.",
    "3. The Half-Right Trap: An option might be 80% correct, but one tiny word at the end makes it false.",
    "4. The Time Trap: Mixing up past, present, and future. The text might say something *will* happen, while the question states it *has* happened."
  ],
  "trap_example": "The 'Qualifying Word' Trap. Text: 'Many doctors recommend the treatment.' Question Statement: 'All doctors recommend the treatment.' (The answer is False because 'many' does not equal 'all').",
  "micro_practice_example": "Text: The new policy was implemented last year and will likely reduce pollution over the next decade. \nStatement: The policy has already reduced pollution significantly. \n(Answer: FALSE. The text says it 'will likely' reduce it in the future, it hasn't happened yet. This is a tense trap).",
  "review_method": "When reviewing practice tests, explicitly label the traps you fell into (e.g., 'Fell for an absolute word trap here' or 'Fell for a tense trap here').",
  "image_url": None,
  "image_prompt_fallback": "A metaphorical image of a bear trap hidden under leaves. On the trap, there is a piece of paper that says 'EXACT MATCH'.",
  "quiz": [
    {
      "question": "If a text states 'Most scientists agree...', and a True/False/Not Given statement says 'All scientists agree...', what is the answer?",
      "options": {
        "A": "True",
        "B": "False",
        "C": "Not Given",
        "D": "Yes"
      },
      "correct_answer": "B",
      "explanation": "The statement is False because it contradicts the text. 'Most' leaves room for some who disagree, whereas 'All' implies 100% agreement. This is a classic 'Absolute Word' trap."
    }
  ]
}

lesson_12 = {
  "lesson_id": "reading_12_review_mistakes",
  "title": "How to Review Reading Mistakes",
  "skill_goal": "Learn how to extract maximum value from practice tests by analyzing errors rather than just checking the score.",
  "question_type_strategy": "Doing practice tests does not improve your score; reviewing them does. You must analyze the gap between your thought process and the examiner's logic.",
  "how_to_recognise": "This applies to post-test review.",
  "step_by_step_method": [
    "1. Do not just look at the correct answer. Cover it up and try to find the evidence in the text again without the time pressure.",
    "2. Categorize the error: Was it a Vocabulary issue (didn't know a word)? A Paraphrase issue (didn't recognize the synonym)? A Trap (fell for 'always')? Or a Time issue (rushed and guessed)?",
    "3. Create a Paraphrase Table: Write the phrase from the question next to the phrase from the text.",
    "4. Create a Unknown Vocab List: Look up words that blocked your understanding and memorize them."
  ],
  "trap_example": "The 'Volume over Quality' Trap. Taking three reading tests a day but never reviewing your mistakes. You will just repeat the same mistakes faster.",
  "micro_practice_example": "You answered Question 5 wrong. \nBad Review: 'Oh, the answer is B. Okay, next.' \nGood Review: 'I chose C because I saw the exact word 'industry'. But B is correct because 'manufacturing sector' in the text paraphrases 'factories' in the question. Next time, I will beware of exact word traps.'",
  "review_method": "Spend equal time reviewing a test as you did taking it. If the test took 60 minutes, spend 60 minutes analyzing the answers.",
  "image_url": None,
  "image_prompt_fallback": "A student looking at a graded test paper, holding a magnifying glass and a notebook titled 'Error Log', with lines connecting incorrect answers to a 'Root Cause' column.",
  "quiz": [
    {
      "question": "What is the most common reason a student's reading score does not improve despite doing dozens of practice tests?",
      "options": {
        "A": "They are using the wrong brand of pencil.",
        "B": "They are doing the tests too slowly.",
        "C": "They are focusing on their score rather than deeply analyzing why they got questions wrong.",
        "D": "They are not reading enough English novels."
      },
      "correct_answer": "C",
      "explanation": "Improvement comes from error analysis. Without understanding why a trap worked on you or why you missed a paraphrase, you will continue to make the same errors."
    }
  ]
}

os.makedirs('output', exist_ok=True)

with open('output/lesson_07.json', 'w') as f:
    json.dump(lesson_7, f, indent=2)

with open('output/lesson_08.json', 'w') as f:
    json.dump(lesson_8, f, indent=2)

with open('output/lesson_09.json', 'w') as f:
    json.dump(lesson_9, f, indent=2)

with open('output/lesson_10.json', 'w') as f:
    json.dump(lesson_10, f, indent=2)

with open('output/lesson_11.json', 'w') as f:
    json.dump(lesson_11, f, indent=2)

with open('output/lesson_12.json', 'w') as f:
    json.dump(lesson_12, f, indent=2)

print("Generated lessons 7 through 12 successfully.")
