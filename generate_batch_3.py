import json
import os

os.makedirs('output', exist_ok=True)

# Lesson 7: Adjective + Noun Collocations
lesson_7 = {
  "lesson_id": "vocab_colloc_07",
  "title": "Adjective + Noun Collocations",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Powerful descriptive pairings to enhance clarity and precision in task responses. Expanding vocabulary beyond simple adjectives."
  },
  "key_vocabulary_bank": [
    {
      "word": "Profound",
      "phonetic": "/prəˈfaʊnd/",
      "cefr_level": "C2",
      "meaning": "Felt or experienced very strongly or in an extreme way.",
      "example": "The invention of the smartphone has had a profound impact on how we communicate.",
      "image_url": None,
      "image_prompt_fallback": "A visual metaphor of a deep impact, like a heavy stone dropped in a calm pond creating massive, far-reaching ripples."
    },
    {
      "word": "Inherent",
      "phonetic": "/ɪnˈher.ənt/",
      "cefr_level": "C1",
      "meaning": "Existing as a natural or basic part of something.",
      "example": "There are inherent risks associated with extreme sports like BASE jumping.",
      "image_url": None,
      "image_prompt_fallback": "A DNA strand glowing, symbolizing something that is naturally built-in or intrinsic."
    },
    {
      "word": "Viable",
      "phonetic": "/ˈvaɪ.ə.bəl/",
      "cefr_level": "C1",
      "meaning": "Able to work as intended or able to succeed.",
      "example": "Solar power is becoming a increasingly viable alternative to fossil fuels.",
      "image_url": None,
      "image_prompt_fallback": "A thriving, green plant growing out of a lightbulb, representing a successful and workable idea."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Profound impact",
      "meaning": "A very strong and deep effect.",
      "example": "The new policy will have a profound impact on the local economy."
    },
    {
      "collocation": "Inherent risk",
      "meaning": "A danger that is an unavoidable part of a situation.",
      "example": "Investors must be aware of the inherent risks of cryptocurrency."
    },
    {
      "collocation": "Viable solution",
      "meaning": "A practical and effective answer to a problem.",
      "example": "We need to find a viable solution to the city's housing shortage."
    },
    {
      "collocation": "Integral part",
      "meaning": "An essential or necessary component of something.",
      "example": "Technology has become an integral part of modern education."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "A big effect",
      "better_upgrade": "A profound impact / A significant influence",
      "example": "Climate change is having a profound impact on global weather patterns."
    },
    {
      "weak_phrase": "A real choice",
      "better_upgrade": "A viable alternative",
      "example": "Wind energy is a viable alternative to traditional power sources."
    },
    {
      "weak_phrase": "An important part",
      "better_upgrade": "An integral component",
      "example": "Teamwork is an integral component of any successful business."
    }
  ],
  "sentence_frames": [
    "It is undeniable that [A] has had a profound impact on [B].",
    "One viable alternative to [A] is to implement [B].",
    "Despite the inherent risks, many still choose to..."
  ],
  "ielts_usage_examples": {
    "writing_example": "While transitioning to green energy involves inherent financial risks, it remains the only viable solution to combat global warming.",
    "speaking_example": "Smartphones have become an integral part of our daily routines; they've had a profound impact on how we interact with the world."
  },
  "common_mistakes": [
    "Using 'a strong impact' instead of the more academic 'a profound impact' or 'a significant impact'.",
    "Confusing 'invaluable' (meaning extremely useful) with 'valueless' (meaning having no value). An invaluable asset is a good thing!"
  ],
  "quiz": [
    {
      "question": "Which adjective correctly collocates with 'alternative' to mean 'practical and able to succeed'?",
      "options": {
        "A": "Profound",
        "B": "Inherent",
        "C": "Viable",
        "D": "Integral"
      },
      "correct_answer": "C",
      "explanation": "A 'viable alternative' is one that can actually work successfully."
    },
    {
      "question": "What does 'inherent risk' mean?",
      "options": {
        "A": "A risk that is easily avoided.",
        "B": "A risk that is a natural and unavoidable part of something.",
        "C": "A risk that was created by mistake.",
        "D": "A risk that is extremely dangerous but rare."
      },
      "correct_answer": "B",
      "explanation": "Inherent means existing as a natural or basic part of something."
    }
  ]
}

# Lesson 8: Verb + Noun Collocations
lesson_8 = {
  "lesson_id": "vocab_colloc_08",
  "title": "Verb + Noun Collocations",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Essential action-oriented collocations that demonstrate a high command of English phrasing."
  },
  "key_vocabulary_bank": [
    {
      "word": "Implement",
      "phonetic": "/ˈɪm.plɪ.ment/",
      "cefr_level": "B2",
      "meaning": "To start using a plan or system.",
      "example": "The school has decided to implement a new dress code.",
      "image_url": None,
      "image_prompt_fallback": "A team of workers assembling a large gear mechanism, representing putting a plan into action."
    },
    {
      "word": "Alleviate",
      "phonetic": "/əˈliː.vi.eɪt/",
      "cefr_level": "C1",
      "meaning": "To make pain or problems less severe.",
      "example": "The medicine did nothing to alleviate her discomfort.",
      "image_url": None,
      "image_prompt_fallback": "A soothing, cool blue glowing aura wrapping around a painful, red inflamed joint, showing relief."
    },
    {
      "word": "Foster",
      "phonetic": "/ˈfɒs.tər/",
      "cefr_level": "C1",
      "meaning": "To encourage the development or growth of ideas or feelings.",
      "example": "The club aims to foster a sense of community among local youths.",
      "image_url": None,
      "image_prompt_fallback": "Hands gently cupping a small, glowing sprout in soil, symbolizing nurturing and encouraging growth."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Implement a policy",
      "meaning": "To put a rule or plan into action.",
      "example": "Governments must implement stricter policies regarding emissions."
    },
    {
      "collocation": "Alleviate poverty",
      "meaning": "To reduce the severity of financial hardship.",
      "example": "Micro-loans can help alleviate poverty in developing nations."
    },
    {
      "collocation": "Foster a sense of",
      "meaning": "To cultivate a feeling (like belonging, community, or responsibility).",
      "example": "Team sports foster a sense of cooperation and mutual respect."
    },
    {
      "collocation": "Allocate resources",
      "meaning": "To distribute money, time, or materials for a specific purpose.",
      "example": "The council needs to allocate more resources to public healthcare."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Make a rule",
      "better_upgrade": "Implement a policy / Introduce legislation",
      "example": "To ensure safety, the factory introduced strict legislation regarding protective gear."
    },
    {
      "weak_phrase": "Reduce the problem",
      "better_upgrade": "Alleviate the issue / Mitigate the problem",
      "example": "Building new roads is unlikely to fully alleviate the issue of congestion."
    },
    {
      "weak_phrase": "Give money to",
      "better_upgrade": "Allocate funds to / Invest resources in",
      "example": "The state should allocate more funds to renewable energy research."
    }
  ],
  "sentence_frames": [
    "By implementing stricter policies, authorities can...",
    "One effective way to alleviate this issue is to...",
    "It is crucial that schools foster a sense of..."
  ],
  "ielts_usage_examples": {
    "writing_example": "If governments allocate sufficient funds to education, they can effectively alleviate poverty and foster a sense of social equality.",
    "speaking_example": "I think the local council should implement better recycling policies to help alleviate the waste management problem in our city."
  },
  "common_mistakes": [
    "Saying 'make a policy' instead of the natural 'implement/introduce a policy'.",
    "Using 'alleviate' for physical objects (e.g., 'alleviate the traffic' - instead, use 'alleviate congestion')."
  ],
  "quiz": [
    {
      "question": "Which verb best completes the collocation: 'The government needs to _______ more resources to the healthcare sector.'",
      "options": {
        "A": "Alleviate",
        "B": "Foster",
        "C": "Allocate",
        "D": "Implement"
      },
      "correct_answer": "C",
      "explanation": "'Allocate resources' means to assign or distribute resources (like money or staff) for a specific purpose."
    },
    {
      "question": "Which phrase is the most academic way to say 'encourage teamwork'?",
      "options": {
        "A": "Push teamwork",
        "B": "Make teamwork",
        "C": "Foster a sense of collaboration",
        "D": "Build working together"
      },
      "correct_answer": "C",
      "explanation": "'Foster a sense of collaboration' is a highly advanced, natural academic collocation."
    }
  ]
}

# Lesson 9: Preposition Patterns in IELTS
lesson_9 = {
  "lesson_id": "vocab_colloc_09",
  "title": "Preposition Patterns in IELTS",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Mastering tricky verb+preposition and adjective+preposition combinations to avoid common grammatical errors."
  },
  "key_vocabulary_bank": [
    {
      "word": "Detrimental",
      "phonetic": "/ˌdet.rɪˈmen.təl/",
      "cefr_level": "C1",
      "meaning": "Causing harm or damage.",
      "example": "These chemicals have a detrimental effect on the environment.",
      "image_url": None,
      "image_prompt_fallback": "A dead, withered plant surrounded by toxic-looking soil, illustrating harmful effects."
    },
    {
      "word": "Conducive",
      "phonetic": "/kənˈdʒuː.sɪv/",
      "cefr_level": "C2",
      "meaning": "Providing the right conditions for something good to happen or exist.",
      "example": "A quiet room is conducive to studying.",
      "image_url": None,
      "image_prompt_fallback": "A perfectly organized, sunlit study desk with open books, representing an ideal environment for learning."
    },
    {
      "word": "Synonymous",
      "phonetic": "/sɪˈnɒn.ɪ.məs/",
      "cefr_level": "C1",
      "meaning": "Having the same or nearly the same meaning; closely associated with.",
      "example": "Wealth is not necessarily synonymous with happiness.",
      "image_url": None,
      "image_prompt_fallback": "Two interlocking puzzle pieces with equal signs on them, showing two concepts that are equivalent."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Detrimental to",
      "meaning": "Harmful to something or someone.",
      "example": "Excessive screen time is detrimental to children's sleep patterns."
    },
    {
      "collocation": "Conducive to",
      "meaning": "Favorable for making something happen.",
      "example": "The harsh climate is not conducive to agriculture."
    },
    {
      "collocation": "Synonymous with",
      "meaning": "Closely associated with or meaning the same as.",
      "example": "In the 1990s, the brand became synonymous with quality."
    },
    {
      "collocation": "Attributed to",
      "meaning": "Regarded as being caused by someone or something.",
      "example": "The fall in crime rates can be attributed to increased police presence."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Bad for",
      "better_upgrade": "Detrimental to",
      "example": "Smoking is highly detrimental to cardiovascular health."
    },
    {
      "weak_phrase": "Good for",
      "better_upgrade": "Conducive to / Beneficial for",
      "example": "Regular feedback is highly conducive to employee growth."
    },
    {
      "weak_phrase": "Caused by",
      "better_upgrade": "Attributed to",
      "example": "The recent economic slump can be largely attributed to global instability."
    }
  ],
  "sentence_frames": [
    "The decline in [A] can largely be attributed to [B].",
    "Such a harsh environment is clearly not conducive to...",
    "While some believe [A] is synonymous with [B], the reality is far more complex."
  ],
  "ielts_usage_examples": {
    "writing_example": "The sudden increase in childhood obesity can largely be attributed to a sedentary lifestyle, which is highly detrimental to long-term health.",
    "speaking_example": "I'd say my hometown isn't really conducive to cycling. The roads are narrow and there are no dedicated bike lanes, which is a bit detrimental to public safety."
  },
  "common_mistakes": [
    "Using 'detrimental for' instead of the correct 'detrimental to'.",
    "Writing 'attributed with' instead of 'attributed to' when explaining a cause."
  ],
  "quiz": [
    {
      "question": "Which preposition correctly follows the adjective 'conducive'?",
      "options": {
        "A": "For",
        "B": "With",
        "C": "To",
        "D": "In"
      },
      "correct_answer": "C",
      "explanation": "The correct pattern is 'conducive to' (e.g., conducive to learning)."
    },
    {
      "question": "Complete the sentence: 'His success can be largely attributed _______ his relentless work ethic.'",
      "options": {
        "A": "by",
        "B": "to",
        "C": "for",
        "D": "with"
      },
      "correct_answer": "B",
      "explanation": "We say something is 'attributed to' a cause."
    }
  ]
}

with open('output/lesson_07_adjective_noun.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_7, f, indent=2, ensure_ascii=False)
with open('output/lesson_08_verb_noun.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_8, f, indent=2, ensure_ascii=False)
with open('output/lesson_09_preposition_patterns.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_9, f, indent=2, ensure_ascii=False)

print("Successfully wrote Batch 3 (Lessons 7-9).")
