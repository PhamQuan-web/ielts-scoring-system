import json
import os

lesson_13 = {
  "lesson_id": "listening_13_sections_overview",
  "title": "IELTS Listening Sections Overview",
  "skill_goal": "Understand the structure, context, and progressive difficulty of the four parts of the IELTS Listening test.",
  "question_type_strategy": "The Listening test is 30 minutes long (plus 10 minutes to transfer answers in the paper test). It has 4 parts, 40 questions, and gets progressively harder. Part 1 and 2 are everyday social contexts; Part 3 and 4 are educational/training contexts.",
  "how_to_recognise": "Part 1: Conversation between 2 speakers (e.g., booking a hotel). Part 2: Monologue (e.g., a tour guide). Part 3: Academic conversation with up to 4 speakers (e.g., students discussing an assignment). Part 4: Academic monologue (e.g., a university lecture).",
  "step_by_step_method": [
    "1. Recognize the context immediately: Who is speaking and why?",
    "2. Adapt your listening style: Part 1 requires listening for highly specific facts (names, numbers).",
    "3. Adapt for Part 3: Focus on opinions, agreement/disagreement between speakers.",
    "4. Adapt for Part 4: Follow complex signposting language in a long, unbroken lecture.",
    "5. Use the pauses: You are given time before each section to read the questions. Use this time aggressively to predict answers."
  ],
  "trap_example": "The 'Losing Focus' Trap. Part 4 is a single 5-minute speech with no breaks in the middle. If you lose focus and miss a question, do not panic. Move your eyes to the next question immediately so you don't lose the rest of the section.",
  "micro_practice_example": "Audio: 'Welcome everyone to the museum. Today I'll be showing you around...' (Context: Part 2 Monologue, everyday context). \nAudio: 'So, Dr. Smith, regarding the methodology for our thesis...' (Context: Part 3 Conversation, academic context).",
  "review_method": "Listen to BBC Radio 4 or TED talks to get used to native speaker monologues and conversations of varying lengths.",
  "image_url": None,
  "image_prompt_fallback": "A visual timeline showing 4 distinct audio wave graphs. The graphs get progressively larger and more complex from left to right, representing the 4 parts of the IELTS listening test.",
  "quiz": [
    {
      "question": "Which part of the IELTS Listening test features an academic monologue, such as a university lecture?",
      "options": {
        "A": "Part 1",
        "B": "Part 2",
        "C": "Part 3",
        "D": "Part 4"
      },
      "correct_answer": "D",
      "explanation": "Part 4 is the most difficult section, featuring a single speaker delivering an academic lecture without any pauses in the middle."
    }
  ]
}

lesson_14 = {
  "lesson_id": "listening_14_predicting_answers",
  "title": "Predicting Answers Before Listening",
  "skill_goal": "Learn how to actively use the 30 seconds of silent reading time to predict the grammar and content of the answers.",
  "question_type_strategy": "Never wait for the audio to start before thinking. Use the silent preparation time to become an 'active listener'. If you know what kind of word you are listening for, it is much easier to catch it.",
  "how_to_recognise": "Look at the gaps in completion tasks or the options in multiple-choice tasks before the audio begins.",
  "step_by_step_method": [
    "1. Read the instructions (e.g., ONE WORD ONLY).",
    "2. Look at the word before and after the gap.",
    "3. Predict the grammar: Do I need a noun, verb, adjective, or number?",
    "4. Predict the context: If the form says 'Date of Birth: _______', you know you are listening for a date.",
    "5. Anticipate synonyms: If the question says 'cheap', listen for 'inexpensive' or 'budget'."
  ],
  "trap_example": "The 'Passive Listening' Trap. Staring blankly at the paper waiting for the audio. If the gap says 'Requires ________ shoes' and you haven't predicted that an adjective (like 'special' or 'running') is needed, the answer will fly by too fast.",
  "micro_practice_example": "Question Form: \nDestination: ___________ \nCost: £___________ \nPrediction: The first blank must be a noun (a place/city name). The second blank must be a number (price).",
  "review_method": "Before taking a practice test, spend 10 minutes ONLY looking at the questions and writing down your predictions for the type of word needed for every single gap.",
  "image_url": None,
  "image_prompt_fallback": "A student looking at a test paper with a blank space. A thought bubble above their head shows them predicting 'Noun? Number? Date?'.",
  "quiz": [
    {
      "question": "If you see the gap: 'The course will teach students how to improve their ________', what part of speech are you most likely listening for?",
      "options": {
        "A": "A verb",
        "B": "A noun (or noun phrase)",
        "C": "An adverb",
        "D": "A pronoun"
      },
      "correct_answer": "B",
      "explanation": "Grammatically, 'their' is a possessive adjective that must be followed by a noun (e.g., 'their skills', 'their writing'). Predicting this helps you ignore verbs and adverbs in the audio."
    }
  ]
}

lesson_15 = {
  "lesson_id": "listening_15_spelling_numbers",
  "title": "Spelling, Numbers and Dates",
  "skill_goal": "Master the precise phonetic rules for how English speakers dictate names, postal codes, phone numbers, and dates.",
  "question_type_strategy": "This is entirely focused on Part 1. You will lose points if you spell a name wrong, even if you heard it correctly. You must know the English alphabet perfectly, especially the tricky vowels (A, E, I) and consonants (G/J, M/N).",
  "how_to_recognise": "The speaker will say a difficult name and then spell it out letter by letter: 'My name is Smythe. That's S-M-Y-T-H-E.'",
  "step_by_step_method": [
    "1. Vowels: Memorize the difference in pronunciation between A (/eɪ/), E (/iː/), and I (/aɪ/).",
    "2. Consonants: Practice distinguishing G (/dʒiː/) and J (/dʒeɪ/), as well as M and N.",
    "3. Doubles: Listen for 'double L' or 'double O'.",
    "4. Numbers: Understand how native speakers group numbers (e.g., '0' is often pronounced 'oh', '44' is 'double four').",
    "5. Dates: 'The 15th of May', 'May 15th', or 'May the 15th' should all be written as '15 May' to avoid word limit issues."
  ],
  "trap_example": "The 'Similar Sounds' Trap. Confusing 13 (thirteen) and 30 (thirty). The stress is at the end for 'thir-TEEN' and at the beginning for 'THIR-ty'.",
  "micro_practice_example": "Audio: 'My post code is J - W - 8 - double 4 - E.' \nYou must write: JW844E. \nIf you write 'G' instead of 'J', it is completely wrong.",
  "review_method": "Have a friend dictate random license plates, postal codes, and phone numbers to you quickly.",
  "image_url": None,
  "image_prompt_fallback": "A visual chart showing the tricky letters of the English alphabet (A/E/I, G/J) with phonetic spelling next to them to show how they sound.",
  "quiz": [
    {
      "question": "How do native speakers frequently pronounce the number '0' in a telephone number?",
      "options": {
        "A": "Zero",
        "B": "Nought",
        "C": "Oh",
        "D": "Nil"
      },
      "correct_answer": "C",
      "explanation": "While 'zero' is technically correct, native speakers almost always pronounce '0' as the letter 'O' (oh) when dictating phone numbers or codes."
    }
  ]
}

lesson_16 = {
  "lesson_id": "listening_16_signposting",
  "title": "Signposting Language",
  "skill_goal": "Use specific transition words to navigate long audio passages and know exactly when to move to the next question.",
  "question_type_strategy": "Signposting language is how speakers organize their thoughts. Words like 'Firstly', 'Moving on to', or 'On the other hand' act like a map, telling you exactly where you are in the lecture.",
  "how_to_recognise": "Part 4 relies heavily on this. The headings in your question paper will directly match the signposting language used by the speaker.",
  "step_by_step_method": [
    "1. Identify the structural headings on your test paper (e.g., 'Background', 'Methodology', 'Results').",
    "2. Listen for transition phrases that introduce these sections (e.g., 'Let's start by looking at...', 'Now I'd like to discuss...').",
    "3. Listen for adding phrases (e.g., 'Furthermore', 'Another point is...') which mean the speaker is giving a second answer in a list.",
    "4. Listen for contrast phrases (e.g., 'However', 'But actually...') which often introduce the real answer after a distractor.",
    "5. When you hear a new signpost, physically move your pen to the next question."
  ],
  "trap_example": "The 'Getting Lost' Trap. If you miss Question 34, and you don't listen for the signpost 'Moving on to the results...' (which points to Question 35), you will miss the rest of the entire test.",
  "micro_practice_example": "Paper shows: \n- Disadvantages of the system \nAudio: 'So, the system was cheap. *However, there were significant drawbacks*. Firstly, it was slow...' \n(The signpost 'significant drawbacks' tells you to look at the 'Disadvantages' section on your paper).",
  "review_method": "Read the transcript of a Part 4 lecture and use a highlighter to mark every single transition word the speaker uses.",
  "image_url": None,
  "image_prompt_fallback": "A road map with several large, clear signposts pointing in different directions. The signposts have words like 'However', 'Furthermore', and 'Finally' written on them.",
  "quiz": [
    {
      "question": "If you hear the speaker say 'Turning now to the issue of funding...', what should you do?",
      "options": {
        "A": "Keep looking at the previous question in case they go back.",
        "B": "Immediately move your eyes to the section of the test paper that mentions 'money', 'budget', or 'funding'.",
        "C": "Stop listening and check your spelling.",
        "D": "Write 'funding' as the answer."
      },
      "correct_answer": "B",
      "explanation": "Signposting language tells you the speaker has moved to a new topic. You must physically move down your question paper to match where the speaker is."
    }
  ]
}

lesson_17 = {
  "lesson_id": "listening_17_distractors",
  "title": "Dealing with Distractors",
  "skill_goal": "Learn how to identify when speakers correct themselves or change their minds to avoid writing down the wrong answer.",
  "question_type_strategy": "A distractor is incorrect information given to test if you are listening carefully. The speaker will often say a possible answer, but then immediately correct themselves or disagree with it.",
  "how_to_recognise": "Listen for contrast words: 'but', 'however', 'no, wait', 'actually', 'instead', 'on second thought'.",
  "step_by_step_method": [
    "1. Do not write down the very first answer you hear immediately. Keep your pencil hovering.",
    "2. Listen for the next 5 seconds to see if the speaker changes their mind.",
    "3. If they say a contrast word, cross out the first answer in your head.",
    "4. Wait for the final, confirmed statement.",
    "5. Pay attention to who is speaking. In Part 3, one student might suggest an answer, but the professor might say 'I don't think that's correct'."
  ],
  "trap_example": "The 'Self-Correction' Trap. Audio: 'I'd like to book a flight for the 14th of June. Oh, wait, my meeting was moved, make that the 16th.' If you stop listening after '14th', you get it wrong.",
  "micro_practice_example": "Question: Cost of the ticket. \nAudio: 'Normally tickets are $50, but because you are a student, we can offer it for $35.' \n(The distractor is $50. The correct answer is 35).",
  "review_method": "Whenever you fall for a distractor in a practice test, read the transcript to find the exact word the speaker used to change their mind (e.g., 'actually').",
  "image_url": None,
  "image_prompt_fallback": "An image of a person writing a number '14' with a pencil, but an eraser is aggressively rubbing it out, while another hand writes '16', illustrating self-correction.",
  "quiz": [
    {
      "question": "Why is it dangerous to write down the very first number or name you hear in the IELTS listening test?",
      "options": {
        "A": "Because the audio might be too quiet.",
        "B": "Because speakers frequently use distractors, stating an incorrect fact before correcting themselves with phrases like 'No, actually...'.",
        "C": "Because the first thing they say is always a greeting.",
        "D": "Because you must wait until the end of the test to write anything."
      },
      "correct_answer": "B",
      "explanation": "Distractors are designed specifically to catch students who panic and write down the first relevant word they hear without listening to the full context."
    }
  ]
}

# Lesson 18: Very detailed as multiple choice in listening is very complex
lesson_18 = {
  "lesson_id": "listening_18_multiple_choice",
  "title": "Listening Multiple Choice",
  "skill_goal": "Develop techniques to process long audio clips and long text options simultaneously without getting confused.",
  "question_type_strategy": "Listening Multiple Choice is extremely challenging because you must read complex options (A, B, C) while simultaneously listening to complex audio. The speakers will almost always mention words from ALL THREE options to confuse you.",
  "how_to_recognise": "You must choose the correct letter (A, B, or C). Sometimes, it's 'choose TWO letters from A-E'.",
  "step_by_step_method": [
    "1. Use preparation time to read the question stem carefully. Understand exactly what is being asked.",
    "2. Skim the options and underline only the key differences between them.",
    "3. Do NOT expect to hear the exact words from the options. The correct answer will be heavily paraphrased.",
    "4. Expect to hear distractors for the wrong options. Just because you hear a word from Option A, does not mean A is correct.",
    "5. Listen for the speaker's tone and agreement (especially in Part 3) to confirm the final choice."
  ],
  "trap_example": "The 'Mentioned ≠ Correct' Trap. Option B says 'The project lacked funding'. The audio says 'Funding was not an issue for this project'. You heard the word 'funding', so you choose B. This is wrong; the audio contradicted the option.",
  "micro_practice_example": "Question: Why did the student choose the topic? \nA. It was recommended by a tutor. \nB. She read a fascinating book about it. \nC. She has personal experience with it. \nAudio: 'My tutor suggested I do my essay on Roman history, but I actually decided on marine biology because my family used to live on a boat, so I know a lot about it.' \n(Answer: C. A is a distractor. B is not mentioned).",
  "review_method": "Print the transcript. Highlight the phrase that proves the correct answer in green. Highlight the phrases that act as distractors for the wrong options in red.",
  "image_url": None,
  "image_prompt_fallback": "A split brain image. One side of the brain has a pair of headphones (listening). The other side has an eye looking at a multiple choice test (reading), showing the cognitive load required.",
  "quiz": [
    {
      "question": "If you hear the speaker say exactly the same words that are written in Option C, what should you do?",
      "options": {
        "A": "Immediately choose Option C, it's definitely correct.",
        "B": "Be highly suspicious. Exact words are often used in distractors, while the correct answer is usually paraphrased.",
        "C": "Stop listening to the rest of the audio.",
        "D": "Choose another option randomly."
      },
      "correct_answer": "B",
      "explanation": "In listening multiple choice, examiners often read out exact words from the wrong options to trick students. The correct answer usually expresses the same meaning using completely different words."
    }
  ]
}

os.makedirs('output', exist_ok=True)

with open('output/lesson_13.json', 'w') as f:
    json.dump(lesson_13, f, indent=2)

with open('output/lesson_14.json', 'w') as f:
    json.dump(lesson_14, f, indent=2)

with open('output/lesson_15.json', 'w') as f:
    json.dump(lesson_15, f, indent=2)

with open('output/lesson_16.json', 'w') as f:
    json.dump(lesson_16, f, indent=2)

with open('output/lesson_17.json', 'w') as f:
    json.dump(lesson_17, f, indent=2)

with open('output/lesson_18.json', 'w') as f:
    json.dump(lesson_18, f, indent=2)

print("Generated lessons 13 through 18 successfully.")
