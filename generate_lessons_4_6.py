import json
import os

os.makedirs("output/grammar_lessons", exist_ok=True)

lesson_4 = {
  "lesson_id": "grammar_04",
  "title": "Present Perfect Continuous for Ongoing Actions",
  "grammar_goal": "Shows high-level grammatical range in Speaking Part 1/2. Demonstrates the ability to distinguish between completed results and ongoing progress.",
  "core_rule": {
    "formula": "S + have/has + been + V-ing + O",
    "usage": "Used to emphasize the duration of an action that started in the past and is still continuing, or an action that has just finished but has a visible present result.",
    "signals": ["for + [duration]", "since + [point in time]", "recently", "lately", "all day", "all week"]
  },
  "when_to_use": [
    "Speaking Part 1: Describing how long you've been doing a hobby or living somewhere (e.g., 'I've been studying English for 5 years.').",
    "Speaking Part 2: Describing a long-term project, hobby, or effort leading up to the present."
  ],
  "when_not_to_use": [
    "Do not use with stative verbs (e.g., know, own, like). Use Present Perfect instead ('I have known him for years', not 'I have been knowing him').",
    "Do not use when emphasizing the quantity or number of things finished (e.g., 'I have written 3 essays', not 'I have been writing 3 essays')."
  ],
  "ielts_examples": {
    "writing": "Governments have been trying to solve the issue of air pollution for decades, yet little progress has been made.",
    "speaking": "I've been preparing for the IELTS exam for the last three months, so I've been quite busy lately."
  },
  "repair_section": [
    {
      "wrong": "I am waiting for you since 2 PM.",
      "correct": "I have been waiting for you since 2 PM.",
      "better_band_upgrade": "I have been waiting here patiently since 2 PM."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using Present Continuous instead of Present Perfect Continuous for actions that started in the past (e.g., 'I am learning English for 3 years').",
    "Incorrectly using it with state verbs."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "She has been knowing him since childhood.",
      "correct_sentence": "She has known him since childhood."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A high-quality educational illustration. A person is sitting at a desk surrounded by books, looking tired but focused. A clock shows the passage of time. Text overlay says 'Present Perfect Continuous: Focus on Duration'.",
  "quiz": [
    {
      "question": "Which sentence is correct for describing an ongoing action?",
      "options": {
        "A": "I am working on this project since Monday.",
        "B": "I work on this project since Monday.",
        "C": "I have been working on this project since Monday.",
        "D": "I have worked on this project since Monday."
      },
      "correct_answer": "C",
      "explanation": "When an action starts in the past and continues to the present with an emphasis on duration ('since Monday'), Present Perfect Continuous is the most natural choice."
    }
  ]
}

lesson_5 = {
  "lesson_id": "grammar_05",
  "title": "Past Simple for Finished Events",
  "grammar_goal": "Essential for Speaking Part 2 storytelling and Writing Task 1 historical data descriptions. Fixes common tense inconsistencies.",
  "core_rule": {
    "formula": "S + V2/ed + O / S + did not + V + O",
    "usage": "Used to describe completed actions, events, or states at a specific, finished time in the past.",
    "signals": ["yesterday", "last week/month/year", "in 1990", "ago", "when I was a child"]
  },
  "when_to_use": [
    "Speaking Part 1: Talking about childhood, past holidays, or previous studies.",
    "Speaking Part 2: Narrating the main events of a story ('What happened?', 'Where did you go?').",
    "Writing Task 1: Describing line graphs or bar charts with dates in the past (e.g., 'In 2010, the population reached a peak.')."
  ],
  "when_not_to_use": [
    "Do not use if the action has a direct connection/result in the present without a specific time mentioned (use Present Perfect).",
    "Do not use Present tenses when the prompt specifically asks about a past event."
  ],
  "ielts_examples": {
    "writing": "In 2015, the percentage of electric car sales rose sharply by 15%.",
    "speaking": "When I was younger, I used to play football every weekend, but I stopped when I went to university."
  },
  "repair_section": [
    {
      "wrong": "The number of tourists increase significantly in 2018.",
      "correct": "The number of tourists increased significantly in 2018.",
      "better_band_upgrade": "The influx of tourists experienced a significant surge in the year 2018."
    },
    {
      "wrong": "I have visited London last year.",
      "correct": "I visited London last year.",
      "better_band_upgrade": "I had the pleasure of exploring London last year."
    },
    {
      "wrong": "Did you went to the cinema yesterday?",
      "correct": "Did you go to the cinema yesterday?",
      "better_band_upgrade": "Did you manage to catch a film at the cinema yesterday?"
    }
  ],
  "vietnamese_learner_mistakes": [
    "Forgetting to add '-ed' to regular verbs or using the wrong irregular past form.",
    "Slipping back into the Present Simple halfway through a Speaking Part 2 story.",
    "Using 'did' with the past form of the main verb (e.g., 'didn't went' instead of 'didn't go')."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "Last summer, I travel to Japan with my family.",
      "correct_sentence": "Last summer, I travelled to Japan with my family."
    },
    {
      "wrong_sentence": "The price of oil fall steadily during the 1990s.",
      "correct_sentence": "The price of oil fell steadily during the 1990s."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A vintage calendar showing a past date with a red circle around it. A photograph of a past memory is pinned next to it. Text overlay: 'Past Simple: Completed Actions'.",
  "quiz": [
    {
      "question": "Which sentence correctly describes a chart showing data from 2005?",
      "options": {
        "A": "In 2005, the unemployment rate has dropped by 5%.",
        "B": "In 2005, the unemployment rate drops by 5%.",
        "C": "In 2005, the unemployment rate dropped by 5%.",
        "D": "In 2005, the unemployment rate was dropping by 5%."
      },
      "correct_answer": "C",
      "explanation": "Because 'In 2005' is a specific, finished time in the past, the Past Simple tense ('dropped') is required."
    }
  ]
}

lesson_6 = {
  "lesson_id": "grammar_06",
  "title": "Past Continuous for Background Actions",
  "grammar_goal": "Enhances storytelling in Speaking Part 2 by creating atmosphere and showing the ability to combine complex tenses (Past Continuous + Past Simple).",
  "core_rule": {
    "formula": "S + was/were + V-ing + O",
    "usage": "Used to describe an action that was in progress at a specific time in the past, or a longer background action that was interrupted by a shorter, sudden event.",
    "signals": ["while", "when", "at 8 PM last night", "all morning yesterday"]
  },
  "when_to_use": [
    "Speaking Part 2: Setting the scene for a story (e.g., 'The sun was shining and birds were singing when I suddenly heard a loud noise.').",
    "Speaking Part 2: Describing an interrupted action ('I was walking to school when I saw my friend.')."
  ],
  "when_not_to_use": [
    "Do not use for consecutive, completed actions in a sequence (e.g., 'I was waking up, was having breakfast, and was going to work' is wrong. Use Past Simple).",
    "Do not use with stative verbs."
  ],
  "ielts_examples": {
    "writing": "While the percentage of car owners was increasing, the use of public transport began to decline.",
    "speaking": "I was studying for my final exams when my friend called to invite me to a concert."
  },
  "repair_section": [
    {
      "wrong": "When I arrived, they had dinner.",
      "correct": "When I arrived, they were having dinner.",
      "better_band_upgrade": "By the time I arrived, they were already in the middle of enjoying their evening meal."
    },
    {
      "wrong": "While I drove to work, I listened to a podcast.",
      "correct": "While I was driving to work, I listened to a podcast.",
      "better_band_upgrade": "During my morning commute, while I was driving to the office, I listened to an educational podcast."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Overusing Past Continuous for main events in a story instead of background events.",
    "Failing to match plural subjects with 'were' and singular subjects with 'was'.",
    "Not using 'when' and 'while' correctly to link Past Continuous and Past Simple."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "I read a book when the phone rang.",
      "correct_sentence": "I was reading a book when the phone rang."
    },
    {
      "wrong_sentence": "While they was watching TV, the power went out.",
      "correct_sentence": "While they were watching TV, the power went out."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "An illustration showing a person walking in a park (background action) and suddenly it starts raining (interruption). Text overlay: 'Past Continuous: Setting the Scene & Interruptions'.",
  "quiz": [
    {
      "question": "Which combination of tenses correctly links a background action and an interruption?",
      "options": {
        "A": "While I cooked dinner, I was burning my hand.",
        "B": "While I was cooking dinner, I burned my hand.",
        "C": "While I was cooking dinner, I was burning my hand.",
        "D": "While I cooked dinner, I burned my hand."
      },
      "correct_answer": "B",
      "explanation": "'Was cooking' represents the longer background action in progress (Past Continuous), and 'burned' represents the sudden, short interrupting event (Past Simple)."
    }
  ]
}

def save_json(data, filename):
    filepath = os.path.join("output/grammar_lessons", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json(lesson_4, "lesson_04.json")
save_json(lesson_5, "lesson_05.json")
save_json(lesson_6, "lesson_06.json")

print("Generated JSON files for Lessons 4-6.")