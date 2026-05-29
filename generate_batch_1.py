import json
import os

os.makedirs('output', exist_ok=True)

# Lesson 1
lesson_1 = {
  "lesson_id": "vocab_colloc_01",
  "title": "Problem and Solution Language",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Essential vocabulary and collocations to describe problems and propose solutions effectively in IELTS Writing Task 2 and Speaking Part 3."
  },
  "key_vocabulary_bank": [
    {
      "word": "Exacerbate",
      "phonetic": "/ɪɡˈzæs.ə.beɪt/",
      "cefr_level": "C1",
      "meaning": "To make something that is already bad even worse.",
      "example": "The lack of public funding will only exacerbate the current healthcare crisis.",
      "image_url": None,
      "image_prompt_fallback": "A stressed city planner looking at a map with growing red traffic zones indicating worsening congestion."
    },
    {
      "word": "Mitigate",
      "phonetic": "/ˈmɪt.ɪ.ɡeɪt/",
      "cefr_level": "C1",
      "meaning": "To make something less severe, harmful, or painful.",
      "example": "Planting trees can help mitigate the effects of climate change.",
      "image_url": None,
      "image_prompt_fallback": "Volunteers planting trees in an urban environment to reduce pollution."
    },
    {
      "word": "Predicament",
      "phonetic": "/prɪˈdɪk.ə.mənt/",
      "cefr_level": "C1",
      "meaning": "A difficult, unpleasant, or embarrassing situation.",
      "example": "Many young adults find themselves in a financial predicament after graduating from university.",
      "image_url": None,
      "image_prompt_fallback": "A recent graduate looking worried while holding a stack of bills and student loan documents."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Pose a threat",
      "meaning": "To create a dangerous situation or cause harm.",
      "example": "Unregulated industrial waste poses a severe threat to marine ecosystems."
    },
    {
      "collocation": "Tackle an issue",
      "meaning": "To make a determined effort to deal with a problem.",
      "example": "Governments must collaborate internationally to tackle the issue of global warming."
    },
    {
      "collocation": "Implement a solution",
      "meaning": "To put a plan or system into operation to solve a problem.",
      "example": "The council has decided to implement a solution involving strict fines for littering."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "A big problem",
      "better_upgrade": "A pressing issue / A formidable challenge",
      "example": "Youth unemployment has become a pressing issue in recent decades."
    },
    {
      "weak_phrase": "Solve the problem",
      "better_upgrade": "Resolve the underlying issue",
      "example": "Merely providing financial aid is not enough to resolve the underlying issue of poverty."
    },
    {
      "weak_phrase": "Make it worse",
      "better_upgrade": "Exacerbate the situation / Aggravate the problem",
      "example": "Ignoring infrastructure maintenance will only exacerbate the situation in the long run."
    }
  ],
  "sentence_frames": [
    "One viable solution to address this pressing issue is to...",
    "If this problem is not tackled promptly, it will inevitably exacerbate...",
    "The most effective way to mitigate the negative impacts of [Topic] would be to..."
  ],
  "ielts_usage_examples": {
    "writing_example": "To mitigate the environmental impact of urban sprawl, governments must implement stricter zoning regulations and invest heavily in green infrastructure.",
    "speaking_example": "Well, I think the most pressing issue in my hometown right now is traffic congestion. A viable solution to tackle this predicament would be to upgrade public transport networks."
  },
  "common_mistakes": [
    "Using 'solve an issue' instead of 'resolve an issue' or 'tackle an issue' (Problems are solved, issues are resolved).",
    "Confusing 'affect' (verb) and 'effect' (noun) when describing the consequences of a problem."
  ],
  "quiz": [
    {
      "question": "Which word is a C1-level synonym for 'making a bad situation worse'?",
      "options": {
        "A": "Alleviate",
        "B": "Mitigate",
        "C": "Exacerbate",
        "D": "Implement"
      },
      "correct_answer": "C",
      "explanation": "'Exacerbate' means to make a problem, bad situation, or negative feeling worse. 'Mitigate' and 'Alleviate' mean to make it better."
    },
    {
      "question": "Choose the most natural collocation: 'Pollution from factories _______ a significant threat to local wildlife.'",
      "options": {
        "A": "makes",
        "B": "poses",
        "C": "gives",
        "D": "does"
      },
      "correct_answer": "B",
      "explanation": "The standard academic collocation is 'pose a threat'. We do not say 'make a threat' in the context of creating a danger."
    }
  ]
}

# Lesson 2
lesson_2 = {
  "lesson_id": "vocab_colloc_02",
  "title": "Comparison and Contrast Language",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "High-level vocabulary and structures to draw comparisons, highlight differences, and show similarities in IELTS Writing Task 1 and Speaking Part 3."
  },
  "key_vocabulary_bank": [
    {
      "word": "Analogous",
      "phonetic": "/əˈnæl.ə.ɡəs/",
      "cefr_level": "C2",
      "meaning": "Comparable in certain respects, typically in a way which makes clearer the nature of the things compared.",
      "example": "The development of the internet is analogous to the invention of the printing press.",
      "image_url": None,
      "image_prompt_fallback": "A split screen showing an old printing press on one side and a modern global internet network on the other, symbolizing similarity."
    },
    {
      "word": "Disparity",
      "phonetic": "/dɪˈspær.ə.ti/",
      "cefr_level": "C1",
      "meaning": "A great difference, especially one connected with unfair treatment.",
      "example": "There is a growing disparity between the rich and the poor in urban areas.",
      "image_url": None,
      "image_prompt_fallback": "A visual representation of wealth inequality: a luxurious skyscraper directly next to a dilapidated slum."
    },
    {
      "word": "Conversely",
      "phonetic": "/kənˈvɜːs.li/",
      "cefr_level": "C1",
      "meaning": "In an opposite way; on the other hand.",
      "example": "Northern regions experience harsh winters; conversely, southern regions enjoy mild temperatures year-round.",
      "image_url": None,
      "image_prompt_fallback": "A dual-image showing a snowy landscape on the left and a sunny beach on the right."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Draw a comparison",
      "meaning": "To compare two or more things to highlight their similarities or differences.",
      "example": "The professor drew a comparison between the current economic crisis and the Great Depression."
    },
    {
      "collocation": "Stark contrast",
      "meaning": "A very clear and obvious difference.",
      "example": "The modern architecture of the museum stands in stark contrast to the historic buildings surrounding it."
    },
    {
      "collocation": "Pale in comparison",
      "meaning": "To seem much less important, serious, or good when compared with someone or something else.",
      "example": "The minor inconveniences of traveling pale in comparison to the joy of discovering new cultures."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "On the other hand",
      "better_upgrade": "Conversely / In stark contrast",
      "example": "City life offers many amenities; conversely, rural living provides tranquility."
    },
    {
      "weak_phrase": "Very different",
      "better_upgrade": "Distinctly different / Fundamentally distinct",
      "example": "The two theories are fundamentally distinct in their approach to human behavior."
    },
    {
      "weak_phrase": "The same as",
      "better_upgrade": "Analogous to / Strikingly similar to",
      "example": "The process of learning a new language is analogous to learning to play a musical instrument."
    }
  ],
  "sentence_frames": [
    "In stark contrast to [A], [B] has experienced...",
    "While [A] and [B] share analogous features in terms of..., they are fundamentally distinct when it comes to...",
    "There is a striking disparity between..."
  ],
  "ielts_usage_examples": {
    "writing_example": "In stark contrast to the dramatic fluctuations seen in 2010, the figures for 2015 remained relatively stable.",
    "speaking_example": "Well, the way my parents' generation consumed media is fundamentally distinct from today. They relied on scheduled TV broadcasts, whereas we demand everything on-demand, which is a massive disparity."
  },
  "common_mistakes": [
    "Using 'compare to' instead of 'compare with' when analyzing differences (Compare *to* is used to assert similarity, compare *with* is used to evaluate differences).",
    "Writing 'in contrary' instead of the correct phrase 'on the contrary' or 'in contrast'."
  ],
  "quiz": [
    {
      "question": "Which phrase is the best upgrade for 'a very big difference'?",
      "options": {
        "A": "A large opposite",
        "B": "A stark contrast",
        "C": "A heavy contrast",
        "D": "A strong apart"
      },
      "correct_answer": "B",
      "explanation": "'Stark contrast' is a high-level, highly natural academic collocation meaning a very clear and obvious difference."
    },
    {
      "question": "Complete the sentence: 'The challenges we face today _______ in comparison to what our ancestors endured.'",
      "options": {
        "A": "fade",
        "B": "drop",
        "C": "pale",
        "D": "weak"
      },
      "correct_answer": "C",
      "explanation": "The idiom is 'pale in comparison', meaning to seem much less significant when compared to something else."
    }
  ]
}

# Lesson 3
lesson_3 = {
  "lesson_id": "vocab_colloc_03",
  "title": "Trend and Data Description Language",
  "topic_snapshot": {
    "target_skills": ["Writing"],
    "description": "Essential vocabulary for precisely describing statistical trends, movements, and data in IELTS Writing Task 1."
  },
  "key_vocabulary_bank": [
    {
      "word": "Surge",
      "phonetic": "/sɜːdʒ/",
      "cefr_level": "C1",
      "meaning": "A sudden and great increase.",
      "example": "There has been a surge in demand for electric vehicles over the past decade.",
      "image_url": None,
      "image_prompt_fallback": "A line graph showing a sudden, sharp, and dramatic upward curve."
    },
    {
      "word": "Plummet",
      "phonetic": "/ˈplʌm.ɪt/",
      "cefr_level": "C1",
      "meaning": "To fall very quickly and suddenly.",
      "example": "House prices plummeted during the economic recession.",
      "image_url": None,
      "image_prompt_fallback": "A line graph showing a steep and sudden downward drop."
    },
    {
      "word": "Plateau",
      "phonetic": "/ˈplæt.əʊ/",
      "cefr_level": "C1",
      "meaning": "To reach a particular level and then stay the same.",
      "example": "After a period of rapid growth, the company's profits plateaued in 2020.",
      "image_url": None,
      "image_prompt_fallback": "A graph line that rises initially and then flattens out completely horizontally."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Upward trajectory",
      "meaning": "A continuous process of increasing or going up.",
      "example": "The number of international students followed a clear upward trajectory."
    },
    {
      "collocation": "Marginal decline",
      "meaning": "A very small or insignificant decrease.",
      "example": "There was only a marginal decline in unemployment rates last year."
    },
    {
      "collocation": "Wildly fluctuate",
      "meaning": "To change frequently and significantly in size, amount, or quality.",
      "example": "The price of cryptocurrency fluctuated wildly throughout the year."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Went up a lot",
      "better_upgrade": "Surged significantly / Witnessed a substantial increase",
      "example": "The proportion of renewable energy use surged significantly."
    },
    {
      "weak_phrase": "Went down a little bit",
      "better_upgrade": "Declined marginally / Experienced a slight dip",
      "example": "Sales declined marginally in the third quarter."
    },
    {
      "weak_phrase": "Stayed the same",
      "better_upgrade": "Reached a plateau / Remained stable",
      "example": "The birth rate reached a plateau after 1995."
    }
  ],
  "sentence_frames": [
    "The graph illustrates an upward trajectory in..., followed by...",
    "After plummeting to a low of [Data] in [Year], the figures subsequently plateaued.",
    "A marginal decline was observed in [Category], dropping from [Data] to [Data]."
  ],
  "ielts_usage_examples": {
    "writing_example": "Overall, while the consumption of fast food followed a clear upward trajectory, the intake of fresh produce plummeted before eventually reaching a plateau in 2018.",
    "speaking_example": "Although I don't look at graphs every day, I've noticed an upward trajectory in the cost of living recently; prices have absolutely surged."
  },
  "common_mistakes": [
    "Using adjectives instead of adverbs to modify verbs (e.g., 'increased rapid' instead of 'increased rapidly').",
    "Confusing 'a decrease of' (amount changed) with 'a decrease to' (the final number)."
  ],
  "quiz": [
    {
      "question": "Which verb means 'to fall very quickly and suddenly'?",
      "options": {
        "A": "Surge",
        "B": "Fluctuate",
        "C": "Plummet",
        "D": "Plateau"
      },
      "correct_answer": "C",
      "explanation": "'Plummet' is an excellent C1 verb used in Task 1 to describe a steep and sudden drop in figures."
    },
    {
      "question": "If a line graph shows figures going up and down repeatedly, what are they doing?",
      "options": {
        "A": "Plateauing",
        "B": "Fluctuating",
        "C": "Surging",
        "D": "Soaring"
      },
      "correct_answer": "B",
      "explanation": "'Fluctuate' means to rise and fall irregularly in number or amount."
    }
  ]
}

with open('output/lesson_01_problem_solution.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_1, f, indent=2, ensure_ascii=False)
with open('output/lesson_02_comparison_contrast.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_2, f, indent=2, ensure_ascii=False)
with open('output/lesson_03_trend_data.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_3, f, indent=2, ensure_ascii=False)

print("Successfully wrote Batch 1 (Lessons 1-3).")
