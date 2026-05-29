import json
import os

# Create directory if it doesn't exist
os.makedirs("output/grammar_lessons", exist_ok=True)

lesson_1 = {
  "lesson_id": "grammar_01",
  "title": "Present Simple for Habits, Facts and General Truths",
  "grammar_goal": "Fixes tense inconsistency in Speaking Part 1 and Writing Task 1/2. Boosts Grammatical Range and Accuracy (GRA) by ensuring basic structures are error-free.",
  "core_rule": {
    "formula": "S + V(s/es) + O / S + do/does + not + V + O",
    "usage": "Used to describe permanent situations, regular habits, routines, general scientific facts, and timetabled future events.",
    "signals": ["always", "usually", "often", "sometimes", "rarely", "never", "every day/week/month", "on Mondays", "twice a week"]
  },
  "when_to_use": [
    "Speaking Part 1: Describing your hometown, daily routine, or job/studies.",
    "Writing Task 2: Stating general facts, universal truths, or common opinions.",
    "Writing Task 1 (Academic): Describing a cyclical process diagram."
  ],
  "when_not_to_use": [
    "Do not use to describe temporary actions happening right now (use Present Continuous).",
    "Do not use to describe past experiences without a connection to the present (use Past Simple)."
  ],
  "ielts_examples": {
    "writing": "Nowadays, a large number of people commute to work by public transport every day.",
    "speaking": "I usually wake up early to go to the gym before my classes start."
  },
  "repair_section": [
    {
      "wrong": "Many people is thinking that the government should ban plastic bags.",
      "correct": "Many people think that the government should ban plastic bags.",
      "better_band_upgrade": "A significant proportion of the population believes that the government should strictly prohibit single-use plastics."
    },
    {
      "wrong": "She always go to the library on weekends.",
      "correct": "She always goes to the library on weekends.",
      "better_band_upgrade": "She frequently visits the local library on weekends to conduct research."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Forgetting the 's' or 'es' ending for third-person singular subjects (he, she, it).",
    "Overusing 'is/are' with normal verbs (e.g., 'I am agree' instead of 'I agree').",
    "Using Present Continuous for general facts instead of Present Simple (e.g., 'The sun is rising in the east')."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "I am work as a software engineer in a multinational company.",
      "correct_sentence": "I work as a software engineer in a multinational company."
    },
    {
      "wrong_sentence": "The train leave the station at exactly 8:00 AM every morning.",
      "correct_sentence": "The train leaves the station at exactly 8:00 AM every morning."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A high-quality educational illustration showing a timeline with repeated daily habits. A person is shown waking up, going to work, and exercising. Text overlay says 'Present Simple: Habits and Facts'. Minimalist, clean corporate style, white background.",
  "quiz": [
    {
      "question": "Which sentence correctly uses the Present Simple to describe a general truth?",
      "options": {
        "A": "Water is boiling at 100 degrees Celsius.",
        "B": "Water boils at 100 degrees Celsius.",
        "C": "Water boiled at 100 degrees Celsius.",
        "D": "Water has boiled at 100 degrees Celsius."
      },
      "correct_answer": "B",
      "explanation": "Scientific facts and general truths are always expressed using the Present Simple tense, not the continuous or past tenses."
    }
  ]
}

lesson_2 = {
  "lesson_id": "grammar_02",
  "title": "Present Continuous for Current and Temporary Situations",
  "grammar_goal": "Improves precision when discussing changing trends in Writing Task 1 and current studies/work in Speaking Part 1. Boosts GRA by showing tense variety.",
  "core_rule": {
    "formula": "S + am/is/are + V-ing + O",
    "usage": "Used for actions happening exactly now, temporary situations around the present time, and changing or developing situations.",
    "signals": ["right now", "at the moment", "currently", "nowadays", "at present", "these days"]
  },
  "when_to_use": [
    "Speaking Part 1: Describing temporary situations (e.g., 'I am currently preparing for my exams').",
    "Writing Task 1: Describing a changing trend over a period up to the present (e.g., 'The population is increasing rapidly').",
    "Writing Task 2: Discussing modern trends or ongoing global issues (e.g., 'More and more people are choosing to work from home')."
  ],
  "when_not_to_use": [
    "Do not use with stative verbs (verbs of thinking, feeling, owning: know, believe, like, belong). E.g., 'I am knowing the answer' is wrong.",
    "Do not use for permanent routines or established facts."
  ],
  "ielts_examples": {
    "writing": "Currently, the global climate is changing at an unprecedented rate due to human activities.",
    "speaking": "At the moment, I'm taking an intensive English course to improve my IELTS score."
  },
  "repair_section": [
    {
      "wrong": "Currently, I study Economics at university.",
      "correct": "Currently, I am studying Economics at university.",
      "better_band_upgrade": "At present, I am pursuing an undergraduate degree in Economics at university."
    },
    {
      "wrong": "The number of tourists increases these days.",
      "correct": "The number of tourists is increasing these days.",
      "better_band_upgrade": "The influx of international tourists is experiencing a steady upward trend these days."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Omitting the 'to be' verb (am/is/are) before the V-ing form (e.g., 'I learning English').",
    "Incorrectly using continuous forms with stative verbs (e.g., 'I am understanding the lesson').",
    "Using Present Simple for temporary situations instead of Present Continuous."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "She reading a really interesting book at the moment.",
      "correct_sentence": "She is reading a really interesting book at the moment."
    },
    {
      "wrong_sentence": "Nowadays, more and more people work remotely instead of commuting.",
      "correct_sentence": "Nowadays, more and more people are working remotely instead of commuting."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A split-screen illustration. On the left, a person is doing a temporary task like studying for an exam with a clock showing the current time. On the right, a line graph showing a rising trend with an arrow. Text overlay: 'Present Continuous: Temporary & Changing Trends'.",
  "quiz": [
    {
      "question": "Which of the following sentences is grammatically INCORRECT because of stative verb usage?",
      "options": {
        "A": "The city's population is expanding rapidly.",
        "B": "I am currently living with my parents.",
        "C": "She is knowing the director of the company very well.",
        "D": "They are working on a new renewable energy project."
      },
      "correct_answer": "C",
      "explanation": "'Know' is a stative verb representing a state of mind, not an action, so it cannot be used in the continuous form. It should be 'She knows the director...'."
    }
  ]
}

lesson_3 = {
  "lesson_id": "grammar_03",
  "title": "Present Perfect for Experience, Change and Unfinished Time",
  "grammar_goal": "Crucial for Speaking Part 1/2 (life experiences) and Writing Task 1/2 (recent changes). Demonstrates complex tense usage for Band 7+ GRA.",
  "core_rule": {
    "formula": "S + have/has + V3/Past Participle + O",
    "usage": "Used for actions that happened at an unspecified time in the past, actions that started in the past and continue to the present, or past actions with a strong result in the present.",
    "signals": ["already", "yet", "just", "ever", "never", "recently", "lately", "since + [point in time]", "for + [period of time]", "so far"]
  },
  "when_to_use": [
    "Speaking Part 1 & 2: Talking about life experiences (e.g., 'I have visited Japan twice').",
    "Writing Task 1: Describing changes that have occurred up to the present moment (e.g., 'The city has developed significantly since 2010').",
    "Writing Task 2: Introducing recent phenomena or ongoing societal shifts (e.g., 'Technology has drastically altered the way we communicate')."
  ],
  "when_not_to_use": [
    "Do not use when a specific past time is mentioned (e.g., 'yesterday', 'in 1999', 'last year'). Use Past Simple instead.",
    "Do not use if the time period is completely finished."
  ],
  "ielts_examples": {
    "writing": "Over the past decade, the government has invested heavily in renewable energy infrastructure.",
    "speaking": "I have never been to Europe, but I've always wanted to visit Italy."
  },
  "repair_section": [
    {
      "wrong": "I have travelled to Paris last year.",
      "correct": "I travelled to Paris last year.",
      "better_band_upgrade": "I had the opportunity to explore Paris last year, which was a remarkable experience."
    },
    {
      "wrong": "The number of international students rose significantly since 2015.",
      "correct": "The number of international students has risen significantly since 2015.",
      "better_band_upgrade": "There has been a substantial surge in the enrollment of international students since 2015."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using Present Perfect with specific past time markers (e.g., 'I have seen him yesterday').",
    "Confusing 'since' (point in time) and 'for' (duration).",
    "Using Past Simple instead of Present Perfect when describing an experience without a specific timeframe."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "She has graduated from university in 2020.",
      "correct_sentence": "She graduated from university in 2020."
    },
    {
      "wrong_sentence": "I didn't finish my assignment yet.",
      "correct_sentence": "I haven't finished my assignment yet."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A visual diagram showing a bridge connecting the past to the present. On one side is 'Past Event' and the bridge leads to 'Present Result'. Icons representing travel stamps and a calendar marked 'Since 2015' and 'For 10 Years'.",
  "quiz": [
    {
      "question": "Choose the correct sentence to describe an ongoing state starting from a specific year:",
      "options": {
        "A": "I have lived in this city for 2018.",
        "B": "I am living in this city since 2018.",
        "C": "I have lived in this city since 2018.",
        "D": "I lived in this city since 2018."
      },
      "correct_answer": "C",
      "explanation": "We use the Present Perfect ('have lived') with 'since' + a specific point in time in the past to describe an action that started in the past and continues to the present."
    }
  ]
}

def save_json(data, filename):
    filepath = os.path.join("output/grammar_lessons", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json(lesson_1, "lesson_01.json")
save_json(lesson_2, "lesson_02.json")
save_json(lesson_3, "lesson_03.json")

print("Generated JSON files for Lessons 1-3.")
