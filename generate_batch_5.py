import json
import os

os.makedirs('output', exist_ok=True)

# Lesson 13: Natural Speaking Phrases
lesson_13 = {
  "lesson_id": "vocab_colloc_13",
  "title": "Natural Speaking Phrases",
  "topic_snapshot": {
    "target_skills": ["Speaking"],
    "description": "Native-like fillers, introductory phrases, and idioms to improve Fluency and Lexical Resource in the IELTS Speaking test."
  },
  "key_vocabulary_bank": [
    {
      "word": "To be honest",
      "phonetic": "/tə bi ˈɒn.ɪst/",
      "cefr_level": "B1",
      "meaning": "Used to emphasize that what you are saying is true, even if it is slightly embarrassing or negative.",
      "example": "To be honest, I've never been very interested in classical music.",
      "image_url": None,
      "image_prompt_fallback": "A person looking earnest with their hand on their heart, speaking truthfully."
    },
    {
      "word": "Off the top of my head",
      "phonetic": "/ɒf ðə tɒp əv maɪ hed/",
      "cefr_level": "C1",
      "meaning": "From the knowledge you have in your memory, without checking any sources.",
      "example": "Off the top of my head, I'd say the population is around two million.",
      "image_url": None,
      "image_prompt_fallback": "A person pointing to their temple playfully as a lightbulb appears, recalling information instantly."
    },
    {
      "word": "Not my cup of tea",
      "phonetic": "/nɒt maɪ kʌp əv tiː/",
      "cefr_level": "B2",
      "meaning": "Not the type of thing that you like.",
      "example": "Thanks for inviting me, but horror movies are just not my cup of tea.",
      "image_url": None,
      "image_prompt_fallback": "A person politely pushing away a teacup decorated with a spooky pattern, expressing dislike."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "A massive fan of",
      "meaning": "To like something very much.",
      "example": "I'm a massive fan of outdoor activities like hiking and cycling."
    },
    {
      "collocation": "To be keen on",
      "meaning": "To be very interested in or enthusiastic about something.",
      "example": "I've always been really keen on learning new languages."
    },
    {
      "collocation": "It depends on",
      "meaning": "Used to say that the answer is not certain because it is affected by other things.",
      "example": "Well, it really depends on the weather, to be frank."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "I don't know",
      "better_upgrade": "I've never really thought about it before, but... / That's a tricky question, I suppose...",
      "example": "That's a tricky question, I suppose it depends on the context."
    },
    {
      "weak_phrase": "I like",
      "better_upgrade": "I'm quite partial to / I'm incredibly passionate about",
      "example": "I'm quite partial to a quiet evening at home rather than going out."
    },
    {
      "weak_phrase": "I think that",
      "better_upgrade": "As far as I'm concerned / I firmly believe that",
      "example": "As far as I'm concerned, public transport should be free for everyone."
    }
  ],
  "sentence_frames": [
    "To be completely honest, I'm not entirely sure, but off the top of my head I'd say...",
    "While some people are massive fans of [A], it's not really my cup of tea.",
    "Well, that's a really interesting question. I've never really thought about it before, but..."
  ],
  "ielts_usage_examples": {
    "writing_example": "N/A - This language is strictly for speaking. Using idioms like 'cup of tea' in Task 2 will lower your score.",
    "speaking_example": "To be honest, I've never really thought about whether I'd like to live in space. Off the top of my head, I'd say it sounds fascinating, but it's probably not my cup of tea because I love nature too much."
  },
  "common_mistakes": [
    "Overusing idioms. Using one or two natural idioms is great for Band 7+, but forcing too many sounds unnatural and rehearsed.",
    "Using informal speaking fillers (like 'you know', 'kinda', 'gonna') in the Writing test."
  ],
  "quiz": [
    {
      "question": "If an examiner asks you a question you have never considered before, what is a natural way to buy time?",
      "options": {
        "A": "I absolutely do not know the answer.",
        "B": "Please skip this question.",
        "C": "That's a tricky question, I've never really thought about it before...",
        "D": "Wait a minute for me to think."
      },
      "correct_answer": "C",
      "explanation": "Option C is a perfect, native-like filler phrase that buys time naturally without showing panic."
    },
    {
      "question": "What is the meaning of 'not my cup of tea'?",
      "options": {
        "A": "I don't like drinking tea.",
        "B": "It is not something I am interested in or enjoy.",
        "C": "I spilled my drink.",
        "D": "It belongs to someone else."
      },
      "correct_answer": "B",
      "explanation": "'Not my cup of tea' is a common idiom meaning 'not the type of thing that I like'."
    }
  ]
}

# Lesson 14: Academic Tone for Writing
lesson_14 = {
  "lesson_id": "vocab_colloc_14",
  "title": "Academic Tone for Writing",
  "topic_snapshot": {
    "target_skills": ["Writing"],
    "description": "Transforming casual, spoken English into formal, objective, and academic prose required for IELTS Task 2."
  },
  "key_vocabulary_bank": [
    {
      "word": "Objective",
      "phonetic": "/əbˈdʒek.tɪv/",
      "cefr_level": "B2",
      "meaning": "Based on real facts and not influenced by personal beliefs or feelings.",
      "example": "The essay must present an objective analysis of the issue.",
      "image_url": None,
      "image_prompt_fallback": "A balanced set of brass scales holding equal weights, symbolizing fairness and lack of bias."
    },
    {
      "word": "Compel",
      "phonetic": "/kəmˈpel/",
      "cefr_level": "C1",
      "meaning": "To force someone to do something.",
      "example": "The new law will compel employers to provide health insurance.",
      "image_url": None,
      "image_prompt_fallback": "A stern judge pointing a gavel, indicating a legally binding requirement."
    },
    {
      "word": "Facilitate",
      "phonetic": "/fəˈsɪl.ɪ.teɪt/",
      "cefr_level": "C1",
      "meaning": "To make something possible or easier.",
      "example": "The new ramp will facilitate access for wheelchair users.",
      "image_url": None,
      "image_prompt_fallback": "A person smoothly opening a heavy door for someone carrying a large box, making their path easier."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Draw a conclusion",
      "meaning": "To decide what to believe about something after you have considered the facts.",
      "example": "From these findings, we can draw the conclusion that the policy failed."
    },
    {
      "collocation": "Underlying cause",
      "meaning": "The root or fundamental reason for something.",
      "example": "Stress is often the underlying cause of many physical illnesses."
    },
    {
      "collocation": "Play a pivotal role",
      "meaning": "To be extremely important in the success of something.",
      "example": "Education plays a pivotal role in poverty reduction."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "People think",
      "better_upgrade": "It is widely believed / It is often argued",
      "example": "It is widely believed that globalization threatens local cultures."
    },
    {
      "weak_phrase": "This is because",
      "better_upgrade": "This can be attributed to / The underlying reason for this is",
      "example": "This surge in crime can be attributed to rising unemployment rates."
    },
    {
      "weak_phrase": "Make it easier",
      "better_upgrade": "Facilitate / Streamline",
      "example": "Digital platforms facilitate global communication."
    }
  ],
  "sentence_frames": [
    "It is often argued that [Subject] plays a pivotal role in...",
    "To facilitate this transition, governments must...",
    "While there are multiple factors, the underlying cause is arguably..."
  ],
  "ielts_usage_examples": {
    "writing_example": "To facilitate economic growth, it is imperative that the government addresses the underlying causes of inflation, as stable prices play a pivotal role in consumer confidence.",
    "speaking_example": "I think the government needs to make it easier for people to start businesses. I mean, small businesses play a really important role in the economy."
  },
  "common_mistakes": [
    "Using personal pronouns like 'I', 'You', and 'We' too frequently. Academic writing should be objective (e.g., instead of 'You can see that...', use 'It is evident that...').",
    "Using contractions (don't, can't, won't) in Task 2. Always write them out in full (do not, cannot, will not)."
  ],
  "quiz": [
    {
      "question": "Which sentence has a more appropriate academic tone for Task 2?",
      "options": {
        "A": "I think you should always try to eat healthy food so you don't get sick.",
        "B": "People need to eat good stuff because it stops them from getting ill.",
        "C": "It is widely believed that maintaining a nutritious diet plays a pivotal role in preventing illness.",
        "D": "It's super important to eat well to stay healthy."
      },
      "correct_answer": "C",
      "explanation": "Sentence C uses formal vocabulary ('nutritious diet', 'pivotal role'), passive structures ('It is widely believed'), and avoids personal pronouns and contractions."
    },
    {
      "question": "Which verb is a C1 upgrade for 'make easier'?",
      "options": {
        "A": "Help",
        "B": "Facilitate",
        "C": "Comfort",
        "D": "Smooth"
      },
      "correct_answer": "B",
      "explanation": "'Facilitate' means to make an action or process easy or easier."
    }
  ]
}

# Lesson 15: Vocabulary Error Repair for Vietnamese Learners
lesson_15 = {
  "lesson_id": "vocab_colloc_15",
  "title": "Vocabulary Error Repair for Vietnamese Learners",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Fixing common false friends, literal translations (L1 interference), and collocation errors specifically made by Vietnamese learners."
  },
  "key_vocabulary_bank": [
    {
      "word": "Economy vs Economics",
      "phonetic": "/ɪˈkɒn.ə.mi/ vs /ˌiː.kəˈnɒm.ɪks/",
      "cefr_level": "B2",
      "meaning": "Economy is the system of trade/industry. Economics is the academic study of wealth.",
      "example": "The country's economy is struggling. He is studying economics at university.",
      "image_url": None,
      "image_prompt_fallback": "A split image: On the left, a bustling stock exchange floor (Economy). On the right, a student reading a thick textbook with a supply/demand graph (Economics)."
    },
    {
      "word": "Nature vs Environment",
      "phonetic": "/ˈneɪ.tʃər/ vs /ɪnˈvaɪ.rən.mənt/",
      "cefr_level": "B1",
      "meaning": "Nature = plants/animals (L1: thiên nhiên). Environment = surroundings where we live (L1: môi trường).",
      "example": "We must protect the environment from pollution. I love walking in nature.",
      "image_url": None,
      "image_prompt_fallback": "A split image: A pristine forest with deer (Nature) versus a city skyline with recycling bins (Environment)."
    },
    {
      "word": "Join vs Participate in",
      "phonetic": "/dʒɔɪn/ vs /pɑːˈtɪs.ɪ.peɪt/",
      "cefr_level": "B1",
      "meaning": "Join = become a member. Participate in = take part in an activity.",
      "example": "I want to join the club. I participated in the marathon.",
      "image_url": None,
      "image_prompt_fallback": "A person signing a membership card (Join) vs a person running in a race with a number bib (Participate)."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Solve a problem",
      "meaning": "To find an answer to an issue.",
      "example": "CORRECT: Solve a problem. WRONG (L1 interference): 'Solve an issue' (Issues are 'resolved' or 'tackled')."
    },
    {
      "collocation": "High standard of living",
      "meaning": "The level of wealth, comfort, and material goods available.",
      "example": "CORRECT: High standard of living. WRONG (L1 interference): 'High living standard'."
    },
    {
      "collocation": "Broaden my horizons",
      "meaning": "To expand one's range of interests, activities, and knowledge.",
      "example": "CORRECT: Broaden my horizons. WRONG (L1 interference): 'Expand my knowledge' is okay, but 'broaden my mind/horizons' is more natural."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Do a mistake (L1: làm sai)",
      "better_upgrade": "Make a mistake",
      "example": "Even experts can make mistakes when under pressure."
    },
    {
      "weak_phrase": "Protect the nature (L1: bảo vệ thiên nhiên)",
      "better_upgrade": "Protect the environment / Conserve nature",
      "example": "Strict laws are required to protect the environment from industrial waste."
    },
    {
      "weak_phrase": "Very crowded people (L1: rất đông người)",
      "better_upgrade": "Heavily populated / Crowded",
      "example": "The city center is heavily populated."
    }
  ],
  "sentence_frames": [
    "To ensure a high standard of living, the economy must be...",
    "While it is easy to make a mistake, resolving the issue requires...",
    "Participating in such events helps individuals broaden their horizons by..."
  ],
  "ielts_usage_examples": {
    "writing_example": "To protect the environment and maintain a high standard of living, governments must invest heavily in green technology rather than relying solely on traditional fossil fuels.",
    "speaking_example": "When I travelled abroad for the first time, I made a few cultural mistakes, but it really helped broaden my horizons and improve my understanding of the world."
  },
  "common_mistakes": [
    "Using 'the nature' instead of 'nature'. (e.g., 'I love the nature' is WRONG. 'I love nature' is CORRECT).",
    "Using 'discuss about'. The verb 'discuss' is transitive and does not take a preposition. (e.g., 'Let's discuss the issue' NOT 'Let's discuss about the issue')."
  ],
  "quiz": [
    {
      "question": "Which sentence is grammatically correct and natural?",
      "options": {
        "A": "The government needs to solve the issue of pollution to protect the nature.",
        "B": "The government needs to tackle the issue of pollution to protect the environment.",
        "C": "The government needs to do a policy to protect the environments.",
        "D": "The government must discuss about the pollution to protect nature."
      },
      "correct_answer": "B",
      "explanation": "'Tackle an issue' and 'protect the environment' are the correct collocations. 'Solve an issue' and 'protect the nature' are common L1 interference errors."
    },
    {
      "question": "Which is the correct collocation?",
      "options": {
        "A": "Do a mistake",
        "B": "Make a mistake",
        "C": "Have a mistake",
        "D": "Create a mistake"
      },
      "correct_answer": "B",
      "explanation": "In English, the standard collocation is 'make a mistake'."
    }
  ]
}

with open('output/lesson_13_natural_speaking.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_13, f, indent=2, ensure_ascii=False)
with open('output/lesson_14_academic_tone.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_14, f, indent=2, ensure_ascii=False)
with open('output/lesson_15_vocab_error_repair.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_15, f, indent=2, ensure_ascii=False)

print("Successfully wrote Batch 5 (Lessons 13-15).")
