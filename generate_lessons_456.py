import json
import os

# Lesson 4: Deep detail because T/F/NG is notoriously difficult and requires nuanced explanation
lesson_4 = {
  "lesson_id": "reading_04_tfng",
  "title": "True / False / Not Given Basics",
  "skill_goal": "Understand the strict logical difference between False (contradictory) and Not Given (insufficient information) in factual statements.",
  "question_type_strategy": "This task tests your ability to identify factual information. The golden rule is: True means the statement perfectly matches the text. False means the text explicitly says the OPPOSITE of the statement. Not Given means you cannot confirm or deny the statement based *only* on the text.",
  "how_to_recognise": "The instructions will explicitly state: 'Do the following statements agree with the information given in Reading Passage X?'. Note: Y/N/NG is the same logic, but deals with writer's opinions rather than concrete facts.",
  "step_by_step_method": [
    "1. Underline keywords in the statement to understand the core meaning.",
    "2. Locate the relevant sentence in the text using scanning techniques (these questions appear in order).",
    "3. Read the text sentence very carefully. Do not use outside knowledge.",
    "4. Ask yourself: 'Does the text confirm this?' -> TRUE.",
    "5. Ask yourself: 'Does the text prove this is impossible or wrong?' -> FALSE.",
    "6. Ask yourself: 'Is it possible, but the text doesn't actually say it?' -> NOT GIVEN."
  ],
  "trap_example": "The 'Outside Knowledge' Trap. A statement might be a well-known scientific fact (e.g., 'Water boils at 100 degrees Celsius'), but if the reading passage doesn't mention it, the answer must be NOT GIVEN.",
  "micro_practice_example": "Text: The restaurant opened in 1995 and serves primarily Italian cuisine. \nStatement 1: The restaurant has been open since 1995. (Answer: TRUE) \nStatement 2: The restaurant serves only French food. (Answer: FALSE - contradicts 'Italian') \nStatement 3: The restaurant is very popular with tourists. (Answer: NOT GIVEN - it might be true in real life, but the text doesn't mention popularity or tourists).",
  "review_method": "When reviewing a 'False' answer, you must be able to underline the exact word in the text that contradicts the statement. If you can't find a contradicting word, the answer was likely Not Given.",
  "image_url": None,
  "image_prompt_fallback": "A minimalist graphic design showing three scales of justice. The first is balanced (TRUE). The second is tipped heavily to one side (FALSE). The third is missing the weights entirely, represented by a question mark (NOT GIVEN).",
  "quiz": [
    {
      "question": "If a statement in the question is logically possible, but the specific information is missing from the reading passage, what is the correct answer?",
      "options": {
        "A": "True",
        "B": "False",
        "C": "Not Given",
        "D": "It depends on outside knowledge."
      },
      "correct_answer": "C",
      "explanation": "Not Given is used when there is insufficient information in the text to prove the statement true or false, regardless of whether it might be true in the real world."
    }
  ]
}

# Lesson 5: Medium detail. The focus is on the specific technique of finding the main idea.
lesson_5 = {
  "lesson_id": "reading_05_matching_headings",
  "title": "Matching Headings",
  "skill_goal": "Learn how to identify the main idea of a paragraph to choose the correct heading, avoiding distractors.",
  "question_type_strategy": "Matching Headings tests your ability to grasp the overall theme of a paragraph. You must distinguish between the main idea and specific supporting details. This task always appears BEFORE the reading passage in the test booklet.",
  "how_to_recognise": "You will see a box with a list of headings (indicated by Roman numerals like i, ii, iii) and you must choose the correct heading for Paragraphs A, B, C, etc.",
  "step_by_step_method": [
    "1. Read the list of headings first and underline key concepts. Note any similarities between headings.",
    "2. Skim Paragraph A. Focus heavily on the first sentence (topic sentence) and the last sentence (concluding thought).",
    "3. Formulate your own brief idea of what the paragraph is about before looking back at the headings.",
    "4. Choose the heading that best matches your idea. If stuck between two, look for a heading that covers the *entire* paragraph, not just one sentence.",
    "5. Cross out the heading you used so you don't use it again."
  ],
  "trap_example": "The 'Specific Detail' Trap. A heading might contain words exactly matching a sentence in the middle of the paragraph. However, if that sentence is just an example and not the main point, the heading is a trap.",
  "micro_practice_example": "Paragraph: Solar power has seen massive investments recently. In 2022 alone, Europe spent billions on new solar farms. Furthermore, the cost of solar panels has dropped by 40%. Consequently, it is becoming the dominant energy source. \nHeading A: The cost of solar panels (Trap - too specific). \nHeading B: The rise of solar energy (Correct - covers the main theme).",
  "review_method": "Practice writing your own headings. Read a paragraph from an article and try to summarize its main point in a 4-5 word title.",
  "image_url": None,
  "image_prompt_fallback": "A visual metaphor showing an umbrella (representing the main heading) sheltering several smaller objects underneath (representing the supporting details of a paragraph).",
  "quiz": [
    {
      "question": "When completing a Matching Headings task, what part of the paragraph is usually the most important to read?",
      "options": {
        "A": "The middle sentences containing statistics.",
        "B": "The first and last sentences.",
        "C": "Every single word in detail.",
        "D": "The longest sentence."
      },
      "correct_answer": "B",
      "explanation": "The first sentence (topic sentence) usually introduces the main idea, and the last sentence often summarizes it, making them the most critical parts for finding the heading."
    }
  ]
}

# Lesson 6: High detail, as it is easily confused with Matching Headings
lesson_6 = {
  "lesson_id": "reading_06_matching_information",
  "title": "Matching Information",
  "skill_goal": "Learn how to locate specific pieces of information within paragraphs, distinguishing this task from Matching Headings.",
  "question_type_strategy": "Unlike Matching Headings (which asks for the main idea of a whole paragraph), Matching Information asks you to find a specific detail hidden anywhere within a paragraph. This is a pure scanning exercise. Note: Answers do NOT come in order, and you may use a paragraph more than once if the instructions allow it.",
  "how_to_recognise": "The instructions will say: 'Which paragraph contains the following information?'. The statements will be specific things like 'a description of...', 'an example of...', or 'a comparison between...'.",
  "step_by_step_method": [
    "1. Read all the information statements first and underline highly specific, changeable keywords.",
    "2. Do NOT do this question first. Do other questions related to the passage first to familiarize yourself with where information is located.",
    "3. Think about synonyms for the keywords in the statements.",
    "4. Scan the paragraphs looking for those specific concepts. Unlike headings, the answer is usually buried in the middle of a paragraph.",
    "5. Check if the instructions say 'You may use any letter more than once.' If so, keep an open mind."
  ],
  "trap_example": "The 'Main Idea Confusion' Trap. Students often read the first sentence of a paragraph and move on, thinking it doesn't contain the information. In Matching Information, the detail you need could be in the very last sentence of a long paragraph.",
  "micro_practice_example": "Statement: an explanation of how the device is powered. \nParagraph C: The new smartphone features a revolutionary screen. It is waterproof up to 50 meters. To operate, it utilizes a microscopic solar cell embedded in the glass. \n(Answer: Paragraph C. The information is hidden in the final sentence, using the synonym 'utilizes a microscopic solar cell' instead of 'powered').",
  "review_method": "Highlighting practice. Take a practice test and use a bright highlighter to mark the exact sentence in the passage that corresponds to the matching statement.",
  "image_url": None,
  "image_prompt_fallback": "A 'Where's Waldo' style illustration showing a dense crowd of text, with a glowing magnifying glass highlighting one specific hidden sentence in the middle of a paragraph.",
  "quiz": [
    {
      "question": "What is the key difference between 'Matching Headings' and 'Matching Information'?",
      "options": {
        "A": "Matching Headings looks for specific details, while Matching Information looks for the main idea.",
        "B": "Matching Headings looks for the main idea of a paragraph, while Matching Information looks for specific details buried within the paragraph.",
        "C": "Matching Information always follows the order of the text.",
        "D": "There is no difference."
      },
      "correct_answer": "B",
      "explanation": "Matching Headings focuses on the macro-level 'big picture' (usually found at the start/end), whereas Matching Information is a micro-level scanning task for specific facts hidden anywhere inside the text."
    }
  ]
}

os.makedirs('output', exist_ok=True)

with open('output/lesson_04.json', 'w') as f:
    json.dump(lesson_4, f, indent=2)

with open('output/lesson_05.json', 'w') as f:
    json.dump(lesson_5, f, indent=2)

with open('output/lesson_06.json', 'w') as f:
    json.dump(lesson_6, f, indent=2)

print("Generated lessons 4, 5, and 6 successfully.")
