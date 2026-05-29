import json
import os

os.makedirs("output/grammar_lessons", exist_ok=True)

lesson_10 = {
  "lesson_id": "grammar_10",
  "title": "Future with Be Going To and Present Continuous",
  "grammar_goal": "Demonstrates precision in Speaking Part 1/3 when discussing future plans and arrangements, avoiding the overuse of 'will'.",
  "core_rule": {
    "formula": "S + am/is/are + going to + V(base) OR S + am/is/are + V-ing",
    "usage": "'Be going to' is used for future plans, intentions, and predictions based on present evidence. Present Continuous is used for fixed, confirmed future arrangements (often with a specific time/place).",
    "signals": ["next week", "tomorrow", "this weekend", "in the near future"]
  },
  "when_to_use": [
    "Speaking Part 1: Discussing study or career plans (e.g., 'I am going to study a Master\\'s next year.').",
    "Speaking Part 1: Talking about fixed appointments (e.g., 'I am meeting my friends for dinner tonight.').",
    "Speaking Part 3: Making predictions based on current clear evidence (e.g., 'Look at the traffic; we are going to be late.')."
  ],
  "when_not_to_use": [
    "Do not use 'be going to' or Present Continuous for spontaneous decisions made at the moment of speaking (use 'will').",
    "Do not use Present Continuous for predictions; it is strictly for human arrangements."
  ],
  "ielts_examples": {
    "writing": "In the near future, the government is going to implement stricter environmental regulations.",
    "speaking": "After I pass my IELTS test, I am going to apply to several universities in Australia."
  },
  "repair_section": [
    {
      "wrong": "Tomorrow I will meet my doctor at 10 AM.",
      "correct": "Tomorrow I am meeting my doctor at 10 AM.",
      "better_band_upgrade": "I have an appointment tomorrow morning; I am seeing my physician at exactly 10 AM."
    },
    {
      "wrong": "Look at those dark clouds. It will rain.",
      "correct": "Look at those dark clouds. It is going to rain.",
      "better_band_upgrade": "Given those heavy, dark clouds forming, it is certainly going to rain heavily very soon."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Overusing 'will' for every future concept, failing to distinguish between spontaneous decisions and planned intentions.",
    "Using 'will' for predictions when there is obvious present physical evidence (e.g., dark clouds, heavy traffic)."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "I will visit my grandparents this weekend. We bought the train tickets yesterday.",
      "correct_sentence": "I am visiting my grandparents this weekend. We bought the train tickets yesterday."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A calendar showing a circled date for 'Next Friday' with a drawn airplane icon next to it, representing a fixed future arrangement.",
  "quiz": [
    {
      "question": "Which sentence correctly uses a future tense for a fixed arrangement?",
      "options": {
        "A": "I will fly to New York next Monday.",
        "B": "I am flying to New York next Monday.",
        "C": "I fly to New York next Monday.",
        "D": "I will have flown to New York next Monday."
      },
      "correct_answer": "B",
      "explanation": "When discussing a fixed, confirmed future arrangement (like a booked flight), the Present Continuous ('am flying') is the most natural and accurate choice."
    }
  ]
}

lesson_11 = {
  "lesson_id": "grammar_11",
  "title": "Future Continuous for Future Progress",
  "grammar_goal": "Enhances Band 7+ grammatical range by showing the ability to project an action into a specific future timeline.",
  "core_rule": {
    "formula": "S + will + be + V-ing + O",
    "usage": "Used to describe an action that will be in progress at a specific time in the future, or a routine/expected future event.",
    "signals": ["this time next year", "at 8 PM tomorrow", "in three years' time"]
  },
  "when_to_use": [
    "Speaking Part 3: Discussing future scenarios (e.g., 'In 20 years, people will be working from home even more.').",
    "Writing Task 2: Projecting the ongoing consequences of a current trend into the future.",
    "Speaking Part 1: Describing a planned future activity at a specific time (e.g., 'This time next week, I will be relaxing on a beach.')."
  ],
  "when_not_to_use": [
    "Do not use with stative verbs (e.g., know, believe).",
    "Do not use for sudden, short future actions."
  ],
  "ielts_examples": {
    "writing": "By the middle of the century, society will be relying almost entirely on renewable energy sources.",
    "speaking": "I can't meet you at 7 PM because I will be studying for my exams."
  },
  "repair_section": [
    {
      "wrong": "At this time tomorrow, I will take the IELTS test.",
      "correct": "At this time tomorrow, I will be taking the IELTS test.",
      "better_band_upgrade": "At this exact time tomorrow, I will be sitting in the examination hall taking my IELTS test."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using Future Simple ('will do') when a specific ongoing future time is mentioned ('at 8 PM tomorrow').",
    "Omitting the 'be' verb (e.g., 'I will studying')."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "In ten years, many people will living in smart homes.",
      "correct_sentence": "In ten years, many people will be living in smart homes."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A futuristic city with flying cars. A clock hovers showing a future year (e.g., 2050). Text: 'Future Continuous: Actions in Progress in the Future'.",
  "quiz": [
    {
      "question": "Which sentence correctly describes an action that will be in progress at a specific time tomorrow?",
      "options": {
        "A": "Tomorrow at 9 AM, I will work.",
        "B": "Tomorrow at 9 AM, I am working.",
        "C": "Tomorrow at 9 AM, I will be working.",
        "D": "Tomorrow at 9 AM, I work."
      },
      "correct_answer": "C",
      "explanation": "Because a specific time is mentioned ('at 9 AM') for an ongoing action, the Future Continuous ('will be working') is required."
    }
  ]
}

lesson_12 = {
  "lesson_id": "grammar_12",
  "title": "Future Perfect and Future Perfect Continuous",
  "grammar_goal": "Aims at Band 8.0+ by demonstrating mastery of the most complex English tenses to set future deadlines and durations.",
  "core_rule": {
    "formula": "Future Perfect: S + will + have + V3. Future Perfect Continuous: S + will + have + been + V-ing.",
    "usage": "Future Perfect is used to say an action will be COMPLETED before a specific time in the future. Future Perfect Continuous emphasizes the DURATION of an action up to a specific future time.",
    "signals": ["by next week", "by the time", "by 2050", "for 10 years by next month"]
  },
  "when_to_use": [
    "Writing Task 2: Making strong predictions about the completion of global goals (e.g., 'By 2050, many species will have become extinct.').",
    "Speaking Part 3: Discussing long-term future achievements or consequences.",
    "Speaking Part 1: Describing future milestones (e.g., 'By next year, I will have been studying English for five years.')."
  ],
  "when_not_to_use": [
    "Do not use these tenses without a clear future deadline or 'by' phrase.",
    "Do not overcomplicate simple future predictions with these tenses if a deadline isn't relevant."
  ],
  "ielts_examples": {
    "writing": "By the end of the next decade, scientists will hopefully have discovered a cure for the disease.",
    "speaking": "By the time I finish my university degree, I will have been living in this city for four years."
  },
  "repair_section": [
    {
      "wrong": "By 2030, the government will build a new transport system.",
      "correct": "By 2030, the government will have built a new transport system.",
      "better_band_upgrade": "By the year 2030, the municipal authorities will have successfully finalized the construction of a comprehensive public transport network."
    },
    {
      "wrong": "Next month, I will work here for 5 years.",
      "correct": "Next month, I will have been working here for 5 years.",
      "better_band_upgrade": "By this time next month, I will have been dedicating my services to this company for exactly five years."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using Future Simple ('will do') instead of Future Perfect ('will have done') when there is a clear 'by + time' deadline.",
    "Confusing the structure, often saying 'will has' instead of 'will have' for third-person subjects."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "By 5 PM today, I will finish my essay.",
      "correct_sentence": "By 5 PM today, I will have finished my essay."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A timeline ending in a future deadline (e.g., 'By 2030') with a red flag indicating completion. Text: 'Future Perfect: Completed Before a Future Time'.",
  "quiz": [
    {
      "question": "Which sentence correctly uses the Future Perfect tense?",
      "options": {
        "A": "By the end of this year, I will graduate.",
        "B": "By the end of this year, I will have graduated.",
        "C": "By the end of this year, I have graduated.",
        "D": "By the end of this year, I will be graduating."
      },
      "correct_answer": "B",
      "explanation": "The phrase 'By the end of this year' sets a future deadline. The action of graduating will be completed before that deadline, requiring 'will have graduated'."
    }
  ]
}

def save_json(data, filename):
    filepath = os.path.join("output/grammar_lessons", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json(lesson_10, "lesson_10.json")
save_json(lesson_11, "lesson_11.json")
save_json(lesson_12, "lesson_12.json")

print("Generated JSON files for Lessons 10-12.")