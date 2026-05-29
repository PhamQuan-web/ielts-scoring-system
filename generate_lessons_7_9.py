import json
import os

os.makedirs("output/grammar_lessons", exist_ok=True)

lesson_7 = {
  "lesson_id": "grammar_07",
  "title": "Past Perfect for Earlier Past Events",
  "grammar_goal": "Boosts Grammatical Range in Speaking Part 2 and Writing Task 1 by showing complex sequencing of historical events.",
  "core_rule": {
    "formula": "S + had + V3/Past Participle + O",
    "usage": "Used to describe an action that happened BEFORE another action in the past. It establishes the sequence of events (which happened first).",
    "signals": ["before", "after", "by the time", "already", "when"]
  },
  "when_to_use": [
    "Speaking Part 2: Explaining the background context of a story (e.g., 'When I arrived at the station, the train had already left.').",
    "Writing Task 1: Describing a sequence of changes in a historical map or data set (e.g., 'By 2010, the population had doubled.').",
    "Speaking Part 3: Discussing how things were different in the past before a specific change occurred."
  ],
  "when_not_to_use": [
    "Do not use Past Perfect if you are only listing events in chronological order (A happened, then B happened). Use Past Simple for that.",
    "Do not use Past Perfect for events that have a connection to the present (use Present Perfect instead)."
  ],
  "ielts_examples": {
    "writing": "By the year 2005, the percentage of university graduates had reached a record high.",
    "speaking": "I was very nervous before the interview because I had never done one in English before."
  },
  "repair_section": [
    {
      "wrong": "When I got to the airport, I realized I left my passport at home.",
      "correct": "When I got to the airport, I realized I had left my passport at home.",
      "better_band_upgrade": "Upon arriving at the departure terminal, I suddenly realized that I had carelessly left my passport at home."
    },
    {
      "wrong": "By 2010, the city built three new hospitals.",
      "correct": "By 2010, the city had built three new hospitals.",
      "better_band_upgrade": "By the end of the decade in 2010, the local government had successfully constructed three state-of-the-art hospitals."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using Past Simple for both actions, making the sequence confusing for the examiner.",
    "Overusing Past Perfect for simple past narratives where it is unnecessary."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "She didn't pass the test because she didn't study the night before.",
      "correct_sentence": "She didn't pass the test because she hadn't studied the night before."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A timeline diagram showing two points in the past. The first point (further left) is labeled 'Past Perfect (Action 1)' and the second point is labeled 'Past Simple (Action 2)'.",
  "quiz": [
    {
      "question": "Which sentence correctly uses the Past Perfect tense to show the sequence of events?",
      "options": {
        "A": "The movie already started when we arrived at the cinema.",
        "B": "The movie has already started when we arrived at the cinema.",
        "C": "The movie had already started when we arrived at the cinema.",
        "D": "The movie was starting when we had arrived at the cinema."
      },
      "correct_answer": "C",
      "explanation": "The movie starting is the 'first' action in the past, and arriving is the 'second' action. Past Perfect ('had started') correctly shows this earlier action."
    }
  ]
}

lesson_8 = {
  "lesson_id": "grammar_08",
  "title": "Past Perfect Continuous for Longer Earlier Actions",
  "grammar_goal": "Demonstrates very advanced grammatical control (Band 7.5+) by combining duration and past sequence.",
  "core_rule": {
    "formula": "S + had + been + V-ing + O",
    "usage": "Used to describe an action that was in progress up to a certain point in the past, often highlighting the duration or the cause of a past result.",
    "signals": ["for", "since", "all day", "by the time"]
  },
  "when_to_use": [
    "Speaking Part 2: Explaining the reason for a past state (e.g., 'I was exhausted because I had been travelling for 12 hours.').",
    "Speaking Part 2: Describing an ongoing effort before an interruption."
  ],
  "when_not_to_use": [
    "Do not use with stative verbs (know, like, belong).",
    "Do not use if the action was short and completed instantly."
  ],
  "ielts_examples": {
    "writing": "The company went bankrupt in 2018; they had been losing money for several years prior.",
    "speaking": "I had been waiting for the bus for over an hour when it finally arrived."
  },
  "repair_section": [
    {
      "wrong": "I was tired because I was working all day.",
      "correct": "I was tired because I had been working all day.",
      "better_band_upgrade": "I felt utterly exhausted because I had been working relentlessly throughout the entire day."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using Past Continuous ('I was waiting') instead of Past Perfect Continuous ('I had been waiting') when a duration ('for an hour') is mentioned."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "She was out of breath because she had run.",
      "correct_sentence": "She was out of breath because she had been running."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A runner who has just stopped to catch their breath. A clock in the background shows a 2-hour duration. Text: 'Past Perfect Continuous: Duration before a Past Point'.",
  "quiz": [
    {
      "question": "Choose the best sentence to explain a past result:",
      "options": {
        "A": "The streets were wet because it had been raining.",
        "B": "The streets were wet because it was raining.",
        "C": "The streets were wet because it has been raining.",
        "D": "The streets were wet because it rained."
      },
      "correct_answer": "A",
      "explanation": "'Had been raining' correctly explains the continuous cause leading up to the past result (streets were wet)."
    }
  ]
}

lesson_9 = {
  "lesson_id": "grammar_09",
  "title": "Future Simple with Will",
  "grammar_goal": "Essential for making predictions in Writing Task 2 and expressing spontaneous ideas in Speaking Part 3.",
  "core_rule": {
    "formula": "S + will + V(base form) + O",
    "usage": "Used for making predictions about the future, spontaneous decisions made at the moment of speaking, promises, and offers.",
    "signals": ["I think", "I believe", "probably", "perhaps", "in the future", "next year"]
  },
  "when_to_use": [
    "Speaking Part 3: Giving opinions about future trends (e.g., 'I think electric cars will replace petrol cars.').",
    "Writing Task 2: Making predictions or discussing potential future consequences of a current issue.",
    "Speaking Part 1: Stating a quick decision or promise."
  ],
  "when_not_to_use": [
    "Do not use 'will' for fixed, pre-arranged plans or intentions (use 'Be Going To' or Present Continuous instead)."
  ],
  "ielts_examples": {
    "writing": "It is highly likely that artificial intelligence will fundamentally change the job market in the coming decades.",
    "speaking": "I'm not sure yet, but perhaps I'll study a master's degree abroad."
  },
  "repair_section": [
    {
      "wrong": "I think the pollution is going to become worse if we don't act now.",
      "correct": "I think the pollution will become worse if we don't act now.",
      "better_band_upgrade": "It is highly probable that environmental degradation will worsen significantly unless immediate action is taken."
    },
    {
      "wrong": "Tomorrow I will fly to Paris. I have my tickets.",
      "correct": "Tomorrow I am flying to Paris. I have my tickets.",
      "better_band_upgrade": "I am scheduled to fly to Paris tomorrow, having already secured my tickets."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Overusing 'will' for every future action, even when 'be going to' or present continuous is more natural for plans.",
    "Forgetting to use base verbs after 'will' (e.g., 'will goes')."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "I believe that people will living on Mars one day.",
      "correct_sentence": "I believe that people will live on Mars one day."
    },
    {
      "wrong_sentence": "I promise I will to study harder.",
      "correct_sentence": "I promise I will study harder."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A futuristic image showing advanced technology, like a flying car or a robot, representing future predictions. Text: 'Future Simple (Will): Predictions and Beliefs'.",
  "quiz": [
    {
      "question": "Which sentence uses 'will' correctly for an IELTS Speaking Part 3 prediction?",
      "options": {
        "A": "I am sure the government will to solve this issue.",
        "B": "In my opinion, more people will working from home in the future.",
        "C": "I think renewable energy will completely replace fossil fuels by 2050.",
        "D": "Next week, I will having a meeting with my professor."
      },
      "correct_answer": "C",
      "explanation": "'Will' + base verb ('replace') is the correct form to make a future prediction based on opinion or belief."
    }
  ]
}

def save_json(data, filename):
    filepath = os.path.join("output/grammar_lessons", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json(lesson_7, "lesson_07.json")
save_json(lesson_8, "lesson_08.json")
save_json(lesson_9, "lesson_09.json")

print("Generated JSON files for Lessons 7-9.")