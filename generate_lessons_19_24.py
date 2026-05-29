import json
import os

lesson_19 = {
  "lesson_id": "listening_19_map_diagram",
  "title": "Map and Diagram Labelling",
  "skill_goal": "Learn how to follow spatial directions and identify locations on a map using specific directional vocabulary.",
  "question_type_strategy": "This task requires you to visualize movement. You must locate the starting point on the map immediately. The audio will then guide you from that point using directional language. If you get lost, do not panic; listen for a known landmark to find your place again.",
  "how_to_recognise": "You will see a map of a town, building, or a diagram of a machine, with letters (A, B, C) marking specific parts. You must match the question items to the letters.",
  "step_by_step_method": [
    "1. Read the instructions. Are you matching letters, or writing words?",
    "2. Locate the starting point. It often says 'You are here' or 'Entrance'.",
    "3. Scan the map and familiarize yourself with the named landmarks (e.g., 'Library', 'Lake').",
    "4. Note the compass points (North, South, East, West) if they are provided.",
    "5. Listen carefully for prepositions of place: 'next to', 'opposite', 'just past the', 'on your left'."
  ],
  "trap_example": "The 'Compass vs Left/Right' Trap. If the map has a compass rose, the speaker will likely use 'North/South' rather than 'Top/Bottom'. Conversely, if there is no compass, they will use 'on the left/right'.",
  "micro_practice_example": "Map shows: Entrance at the bottom. A path goes straight, with a Cafe on the left and a Gift Shop on the right. \nAudio: 'Go through the entrance and walk straight ahead. *Just past* the cafe on your left, you'll see the restrooms.' \n(The answer is not the cafe, but the building *past* it).",
  "review_method": "Draw a simple map of your house or street. Record yourself giving directions from the front door to your bedroom, using IELTS vocabulary like 'adjacent to' and 'opposite'.",
  "image_url": None,
  "image_prompt_fallback": "A line drawing of a park map with a large red 'X' saying 'You Are Here' at the bottom entrance, and dashed lines showing a path moving North past a pond.",
  "quiz": [
    {
      "question": "What is the most important thing to do before the audio starts for a Map Labelling task?",
      "options": {
        "A": "Translate all the building names into your native language.",
        "B": "Find the starting point (e.g., 'Entrance' or 'You are here').",
        "C": "Guess the answers randomly.",
        "D": "Look at the next section of the test."
      },
      "correct_answer": "B",
      "explanation": "If you do not know where the speaker is starting from, all their directions ('turn left', 'go straight') will be meaningless and you will be completely lost."
    }
  ]
}

lesson_20 = {
  "lesson_id": "listening_20_form_table",
  "title": "Form, Note and Table Completion",
  "skill_goal": "Develop scanning and tracking skills to complete factual information in structured layouts, primarily in Part 1 and 4.",
  "question_type_strategy": "These tasks look like real-world documents (a hotel booking form, or a summary table of a lecture). The key advantage is that the visual layout helps you predict the flow of the audio.",
  "how_to_recognise": "You will see a structured form with blanks, usually with headings organizing the information (e.g., 'Name', 'Address', 'Date of Arrival').",
  "step_by_step_method": [
    "1. Read the word limit instruction carefully (e.g., NO MORE THAN ONE WORD AND/OR A NUMBER).",
    "2. Look at the headings of the table or form to understand the structure.",
    "3. Use the information already in the table to predict what goes in the blank (e.g., if column 2 is 'Price', you know the blank needs a number).",
    "4. Follow the numbering of the questions strictly. In a table, questions might go horizontally or vertically.",
    "5. Listen for the speaker to move from one heading to the next."
  ],
  "trap_example": "The 'Wrong Flow' Trap. In a table, questions might be numbered 1, 2, 3 going *down* a column, or going *across* a row. If you follow the wrong visual path, you will miss the answers.",
  "micro_practice_example": "Table Heading: Accommodation Type | Price | Included \nRow 1: Single Room | £45 | Breakfast \nRow 2: Double Room | Question 1 | Dinner \n(Prediction: Question 1 must be a price in pounds, likely higher than £45).",
  "review_method": "Practice tracking. When reviewing, trace the exact path of the audio on the physical paper to see how the speaker moved through the table.",
  "image_url": None,
  "image_prompt_fallback": "A neatly organized table with columns for 'Item', 'Cost', and 'Notes', with a glowing pencil filling in a blank space in the 'Cost' column.",
  "quiz": [
    {
      "question": "What is a major advantage of Table Completion tasks compared to other listening questions?",
      "options": {
        "A": "They never use distractors.",
        "B": "The answers are always numbers.",
        "C": "The visual layout (columns and rows) helps you clearly predict the type of information needed and track the speaker's progress.",
        "D": "They only appear in Part 1."
      },
      "correct_answer": "C",
      "explanation": "Tables provide a rigid visual structure. The headings and the existing data give you massive clues about what to listen for and when the speaker is changing topics."
    }
  ]
}

lesson_21 = {
  "lesson_id": "listening_21_matching",
  "title": "Matching Questions",
  "skill_goal": "Learn how to match a list of items to a list of options, usually involving opinions or decisions in Part 3.",
  "question_type_strategy": "Matching questions often appear in Part 3 (two students discussing a project). You will have a list of items (e.g., parts of an essay) and must match them to options (e.g., 'A. John will do it', 'B. Sarah will do it', 'C. They will skip it').",
  "how_to_recognise": "A numbered list of items (1, 2, 3...) and a box with lettered options (A, B, C...). The instructions say 'Choose the correct letter A, B, or C'.",
  "step_by_step_method": [
    "1. Read the list of numbered items. The audio will mention these *in exact order*.",
    "2. Read the lettered options. These are the answers, and they will likely be paraphrased.",
    "3. Focus on the relationship: Are they deciding who does what? Are they giving opinions (good, bad, average)?",
    "4. Listen to the interaction. One person might suggest an option, but the other person might disagree. Wait for the final agreement."
  ],
  "trap_example": "The 'Initial Suggestion' Trap. Student A says 'I'll write the introduction.' (Option A). Student B replies, 'Actually, you did that last time. Let me do it.' (Option B). The correct answer is B.",
  "micro_practice_example": "Options: A. Keep, B. Change, C. Delete \nItem 1: The title \nAudio: 'So, the title of the presentation. I think it's a bit boring.' 'Yes, let's come up with something more exciting.' \n(Answer: B. Change).",
  "review_method": "Focus on agreement/disagreement phrases. Make a list of phrases speakers use to disagree politely (e.g., 'I see your point, but...', 'I'm not so sure about that').",
  "image_url": None,
  "image_prompt_fallback": "An illustration of two students sitting at a desk discussing a document, with lines connecting different parts of the document to speech bubbles indicating who will do what.",
  "quiz": [
    {
      "question": "In a Part 3 Matching task where two students are dividing work, what must you listen for carefully?",
      "options": {
        "A": "The very first suggestion made by either student.",
        "B": "The final agreement or decision reached after they discuss an item.",
        "C": "Only the words spoken by the male student.",
        "D": "Exact words from the options box."
      },
      "correct_answer": "B",
      "explanation": "Part 3 tests your ability to follow a negotiation. Students will often suggest one thing, debate it, and then agree on a completely different final outcome."
    }
  ]
}

lesson_22 = {
  "lesson_id": "listening_22_accents",
  "title": "Accents and Pronunciation Awareness",
  "skill_goal": "Familiarize yourself with the variety of accents used in the IELTS Listening test to avoid missing answers due to unfamiliar pronunciation.",
  "question_type_strategy": "IELTS is an *International* English test. You will hear British, Australian, New Zealand, and North American accents. You cannot rely solely on American English pronunciation (which is common in movies).",
  "how_to_recognise": "This is a general skill applied to the whole test.",
  "step_by_step_method": [
    "1. Be aware of the 'R' sound: British/Aussie accents are often non-rhotic (they drop the 'r' at the end of words like 'car' or 'water').",
    "2. Be aware of the 'T' sound: Americans often flap the 't' in 'water' (sounds like 'wader'), while British speakers might pronounce a hard 't' or use a glottal stop.",
    "3. Vowel differences: The 'a' in 'can't' or 'dance' is pronounced very differently in the UK vs the US.",
    "4. Exposure: Listen to podcasts from different regions to train your ear."
  ],
  "trap_example": "The 'Missing the Word' Trap. An Australian speaker might say 'data' pronouncing it 'dah-tah', while you might only know the American pronunciation 'day-tah'. If you aren't familiar with both, you won't recognize the word.",
  "micro_practice_example": "Word: 'Schedule'. \nUK pronunciation: 'Shed-yool'. \nUS pronunciation: 'Sked-yool'. \nYou must be able to recognize both instantly.",
  "review_method": "Use IELTS practice tests to identify which accents give you the most trouble. If Australian accents confuse you, watch Australian news or documentaries specifically.",
  "image_url": None,
  "image_prompt_fallback": "A map of the world with speech bubbles coming from the UK, Australia, and North America, showing different phonetic spellings of the same English word.",
  "quiz": [
    {
      "question": "Which of the following accents might you hear in the IELTS Listening test?",
      "options": {
        "A": "Only British accents.",
        "B": "Only American accents.",
        "C": "A mix of British, Australian, New Zealand, and North American accents.",
        "D": "Only the accent of the country where you are taking the test."
      },
      "correct_answer": "C",
      "explanation": "IELTS stands for International English Language Testing System. It deliberately uses a variety of native-speaker accents from across the English-speaking world."
    }
  ]
}

# Lesson 23: Keep concise, focusing on cognitive load management
lesson_23 = {
  "lesson_id": "listening_23_concentration",
  "title": "Concentration and Note-Taking",
  "skill_goal": "Maintain focus for the entire 30-minute audio track and learn when to take brief notes versus just listening.",
  "question_type_strategy": "The IELTS listening test is played exactly ONCE. If you lose concentration for 30 seconds, you can miss 3 questions. Managing cognitive load is as important as English proficiency.",
  "how_to_recognise": "This applies to the entire test, but is most critical in Part 4.",
  "step_by_step_method": [
    "1. Active Posture: Sit up straight and physically track the questions with the tip of your pencil as the audio plays.",
    "2. Don't Look Back: If you miss an answer, guess immediately and move on. Thinking about a missed question guarantees you will miss the next one.",
    "3. Minimal Note-Taking: In IELTS, you generally write answers directly into the gaps. Do not try to take extensive notes like a university lecture; it takes too much brain power.",
    "4. Use the 10-minute transfer time (paper test only): Do not worry about spelling or neatness during the audio. Fix spelling errors only when transferring answers at the end."
  ],
  "trap_example": "The 'Panic Cascade' Trap. Missing Question 32, panicking, trying to remember what they said, and suddenly realizing the speaker is now on Question 36. You lost 4 points because you couldn't let go of 1 point.",
  "micro_practice_example": "Audio is playing. You realize you missed the answer to gap 14. \nCorrect Action: Immediately drop your pencil down to gap 15, listen for the keywords for 15, and refocus.",
  "review_method": "Take full 30-minute practice tests without pausing. Train your stamina. Never pause the audio during practice, as you cannot do it in the real exam.",
  "image_url": None,
  "image_prompt_fallback": "A tight close-up of a student's face showing intense concentration, with the reflection of an audio waveform playing in their glasses.",
  "quiz": [
    {
      "question": "What is the best course of action if you realize you have missed an answer?",
      "options": {
        "A": "Stop the recording and rewind it.",
        "B": "Panic and try to remember what the speaker said a minute ago.",
        "C": "Immediately forget about it, move your eyes to the keywords of the next question, and refocus.",
        "D": "Ask the invigilator to play it again."
      },
      "correct_answer": "C",
      "explanation": "The audio never stops. Dwelling on a missed question will distract you from the current audio, causing a chain reaction where you miss several subsequent answers."
    }
  ]
}

lesson_24 = {
  "lesson_id": "listening_24_review_mistakes",
  "title": "How to Review Listening Mistakes with Transcript",
  "skill_goal": "Learn how to use audio transcripts effectively to diagnose whether your errors are due to vocabulary, spelling, or getting lost.",
  "question_type_strategy": "Just checking the answer key is not enough. To improve, you must use the transcript at the back of the practice book to understand *why* you didn't hear the answer.",
  "how_to_recognise": "This is a post-test study technique.",
  "step_by_step_method": [
    "1. Mark your test. Identify the questions you got wrong.",
    "2. Open the audio transcript. Read the section where the answer was located.",
    "3. Play the audio again while reading the transcript.",
    "4. Diagnose the error: Did you not know the vocabulary word? Did you spell it wrong? Did you fall for a distractor? Or did you just lose your place?",
    "5. Highlight paraphrases: In the transcript, highlight the words the speaker used, and draw a line to the keywords in the question booklet."
  ],
  "trap_example": "The 'Passive Listening' Trap. Just listening to English music or podcasts in the background while cooking will not improve your IELTS score. You must do active, transcript-based analysis to improve.",
  "micro_practice_example": "You missed Question 15. The answer was 'exhibition'. \nTranscript Analysis: You read the transcript and see the speaker said 'exhibition'. You realize you heard the word, but didn't know what it meant, so you didn't write it down. Action: Add 'exhibition' to your vocabulary flashcards.",
  "review_method": "Shadowing: Play a small section of the audio and try to speak along with the transcript exactly matching the speaker's rhythm and pronunciation.",
  "image_url": None,
  "image_prompt_fallback": "A student wearing headphones, looking closely at a printed transcript of an audio recording, highlighting a specific sentence with a yellow marker.",
  "quiz": [
    {
      "question": "What is the most effective way to understand why you got a listening question wrong?",
      "options": {
        "A": "Listen to the whole 30-minute test again.",
        "B": "Look at the answer key and try to memorize it.",
        "C": "Read the audio transcript while listening to the specific section, identifying exactly where the answer was given and what distractors were used.",
        "D": "Complain about the speaker's accent."
      },
      "correct_answer": "C",
      "explanation": "The transcript is the ultimate diagnostic tool. It allows you to visually see what you missed auditorily, helping you distinguish between vocabulary issues and concentration issues."
    }
  ]
}

os.makedirs('output', exist_ok=True)

with open('output/lesson_19.json', 'w') as f:
    json.dump(lesson_19, f, indent=2)

with open('output/lesson_20.json', 'w') as f:
    json.dump(lesson_20, f, indent=2)

with open('output/lesson_21.json', 'w') as f:
    json.dump(lesson_21, f, indent=2)

with open('output/lesson_22.json', 'w') as f:
    json.dump(lesson_22, f, indent=2)

with open('output/lesson_23.json', 'w') as f:
    json.dump(lesson_23, f, indent=2)

with open('output/lesson_24.json', 'w') as f:
    json.dump(lesson_24, f, indent=2)

print("Generated lessons 19 through 24 successfully.")
