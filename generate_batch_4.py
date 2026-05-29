import json
import os

os.makedirs('output', exist_ok=True)

# Lesson 10: Paraphrasing Common Words
lesson_10 = {
  "lesson_id": "vocab_colloc_10",
  "title": "Paraphrasing Common Words",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Essential strategies and vocabulary to replace overused, low-level words (like 'important', 'people', 'many') to demonstrate Lexical Resource depth in IELTS."
  },
  "key_vocabulary_bank": [
    {
      "word": "Paramount",
      "phonetic": "/ˈpær.ə.maʊnt/",
      "cefr_level": "C2",
      "meaning": "More important than anything else; supreme.",
      "example": "Passenger safety is of paramount importance to the airline industry.",
      "image_url": None,
      "image_prompt_fallback": "A glowing golden crown resting on top of a mountain peak, symbolizing supremacy and absolute importance."
    },
    {
      "word": "Individuals",
      "phonetic": "/ˌɪn.dɪˈvɪdʒ.u.əlz/",
      "cefr_level": "B2",
      "meaning": "Single people, considered separately from the rest of a group or society.",
      "example": "It is crucial that individuals take responsibility for their own carbon footprint.",
      "image_url": None,
      "image_prompt_fallback": "A crowd of people represented as grey silhouettes, with one person highlighted in bright color to emphasize the individual."
    },
    {
      "word": "Plethora",
      "phonetic": "/ˈpleθ.ər.ə/",
      "cefr_level": "C1",
      "meaning": "A very large amount of something, especially a larger amount than you need, want, or can deal with.",
      "example": "The internet offers a plethora of resources for independent learners.",
      "image_url": None,
      "image_prompt_fallback": "An overflowing treasure chest bursting with colorful gems and gold coins, representing an abundance."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Of paramount importance",
      "meaning": "The most important thing to consider.",
      "example": "Developing sustainable energy sources is of paramount importance for our future."
    },
    {
      "collocation": "A significant proportion",
      "meaning": "A large part or share of a whole.",
      "example": "A significant proportion of the budget is allocated to defense spending."
    },
    {
      "collocation": "A multitude of",
      "meaning": "A large number of people or things.",
      "example": "The decision was influenced by a multitude of complex factors."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Very important",
      "better_upgrade": "Of paramount importance / Crucial / Indispensable",
      "example": "Learning digital skills is indispensable in the modern workforce."
    },
    {
      "weak_phrase": "Many people",
      "better_upgrade": "A vast majority of individuals / A significant proportion of society",
      "example": "A vast majority of individuals now rely entirely on their smartphones for news."
    },
    {
      "weak_phrase": "A lot of things",
      "better_upgrade": "A plethora of options / A multitude of factors",
      "example": "Consumers today are faced with a plethora of choices when buying technology."
    }
  ],
  "sentence_frames": [
    "It is of paramount importance that governments...",
    "A vast majority of individuals argue that...",
    "There exists a plethora of reasons why [Topic] is becoming increasingly..."
  ],
  "ielts_usage_examples": {
    "writing_example": "While some argue that space exploration is a waste of funds, others maintain that it is of paramount importance, offering a plethora of scientific breakthroughs.",
    "speaking_example": "Well, I think a significant proportion of individuals in my country are worried about housing prices. It's an issue of paramount importance right now."
  },
  "common_mistakes": [
    "Using 'a plethora of' for negative, countable things in a clumsy way (e.g., 'a plethora of murders'). It is better used for resources, choices, or reasons.",
    "Writing 'paramount important' instead of 'of paramount importance' or just 'paramount'."
  ],
  "quiz": [
    {
      "question": "Which phrase is the highest-level replacement for 'very important'?",
      "options": {
        "A": "Really big deal",
        "B": "Of paramount importance",
        "C": "Highly needed",
        "D": "Super crucial"
      },
      "correct_answer": "B",
      "explanation": "'Of paramount importance' is a formal, C2-level phrase demonstrating an excellent command of Lexical Resource."
    },
    {
      "question": "What does 'a plethora of' mean?",
      "options": {
        "A": "A small amount",
        "B": "A specific type",
        "C": "An abundance or excess of something",
        "D": "A dangerous lack of something"
      },
      "correct_answer": "C",
      "explanation": "'Plethora' means a very large amount or abundance."
    }
  ]
}

# Lesson 11: Avoiding Repetition in Writing
lesson_11 = {
  "lesson_id": "vocab_colloc_11",
  "title": "Avoiding Repetition in Writing",
  "topic_snapshot": {
    "target_skills": ["Writing"],
    "description": "Techniques for using referencing words, pronouns, and elegant synonyms to create cohesive, flowing text without sounding repetitive."
  },
  "key_vocabulary_bank": [
    {
      "word": "Latter",
      "phonetic": "/ˈlæt.ər/",
      "cefr_level": "B2",
      "meaning": "The second of two people, things, or groups previously mentioned.",
      "example": "Given the choice between tea and coffee, I generally prefer the latter.",
      "image_url": None,
      "image_prompt_fallback": "A split image showing an apple on the left and an orange on the right, with a spotlight exclusively illuminating the orange (the latter)."
    },
    {
      "word": "Former",
      "phonetic": "/ˈfɔː.mər/",
      "cefr_level": "B2",
      "meaning": "The first of two people, things, or groups previously mentioned.",
      "example": "Both public and private schools have merits, but the former is more accessible to the masses.",
      "image_url": None,
      "image_prompt_fallback": "A split image showing a bus on the left and a train on the right, with a spotlight exclusively illuminating the bus (the former)."
    },
    {
      "word": "Respectively",
      "phonetic": "/rɪˈspek.tɪv.li/",
      "cefr_level": "C1",
      "meaning": "In a way that relates or belongs to each of the separate people or things you have just mentioned.",
      "example": "Julie and Mark are aged 27 and 30 respectively.",
      "image_url": None,
      "image_prompt_fallback": "Two arrows pointing from two names (A and B) directly to two numbers (1 and 2), showing a clear, ordered mapping."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "The aforementioned",
      "meaning": "Mentioned earlier in the text (very formal).",
      "example": "None of the aforementioned solutions are completely flawless."
    },
    {
      "collocation": "This phenomenon",
      "meaning": "A fact or situation that is observed to exist or happen.",
      "example": "This phenomenon is largely driven by rapid urbanization."
    },
    {
      "collocation": "Such a trend",
      "meaning": "Referring back to a pattern of change just described.",
      "example": "If such a trend continues, coastal cities will face severe flooding."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "The first one and the second one",
      "better_upgrade": "The former and the latter",
      "example": "When comparing solar and coal energy, the former is sustainable, while the latter is finite."
    },
    {
      "weak_phrase": "This problem",
      "better_upgrade": "This pressing issue / This phenomenon",
      "example": "Governments must act swiftly to address this pressing issue."
    },
    {
      "weak_phrase": "In the same order",
      "better_upgrade": "Respectively",
      "example": "In 1990 and 2000, the population stood at 2 million and 3 million respectively."
    }
  ],
  "sentence_frames": [
    "While both [A] and [B] offer benefits, the former is more... whereas the latter...",
    "The figures for [Country A] and [Country B] stood at [X]% and [Y]% respectively.",
    "The aforementioned strategies could significantly mitigate the impact of..."
  ],
  "ielts_usage_examples": {
    "writing_example": "The essay will discuss the benefits of both online and traditional learning; however, it will argue that the latter remains superior for developing social skills.",
    "speaking_example": "Well, I enjoy both reading and watching films, but I definitely prefer the latter because it’s much more relaxing after a long day at work."
  },
  "common_mistakes": [
    "Using 'the latter' when referring to the last item in a list of THREE or more things. (It should only be used for the second of exactly TWO things).",
    "Forgetting to use 'the' before former and latter."
  ],
  "quiz": [
    {
      "question": "If you mention 'cats and dogs' in a sentence, how would you refer back to 'dogs'?",
      "options": {
        "A": "The second",
        "B": "The former",
        "C": "The latter",
        "D": "The end one"
      },
      "correct_answer": "C",
      "explanation": "'The latter' refers to the second of two things mentioned."
    },
    {
      "question": "In the sentence 'Sales of cars and bikes reached 500 and 300 _______', which word correctly shows the order of the figures matches the order of the items?",
      "options": {
        "A": "respectively",
        "B": "consecutively",
        "C": "orderly",
        "D": "latterly"
      },
      "correct_answer": "A",
      "explanation": "'Respectively' is used to show that two or more items match two or more numbers/descriptions in the exact order they were mentioned."
    }
  ]
}

# Lesson 12: Topic-Specific High-Frequency Collocations
lesson_12 = {
  "lesson_id": "vocab_colloc_12",
  "title": "Topic-Specific High-Frequency Collocations",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "A targeted rapid-fire lesson covering the most essential collocations for the most common IELTS topics: Environment, Technology, and Education."
  },
  "key_vocabulary_bank": [
    {
      "word": "Ecosystem",
      "phonetic": "/ˈiː.kəʊˌsɪs.təm/",
      "cefr_level": "C1",
      "meaning": "All the living things in an area and the way they affect each other and the environment.",
      "example": "Pollution can have disastrous effects on the delicate marine ecosystem.",
      "image_url": None,
      "image_prompt_fallback": "A cross-section of a vibrant coral reef showing fish, plants, and water interacting harmoniously."
    },
    {
      "word": "Innovation",
      "phonetic": "/ˌɪn.əˈveɪ.ʃən/",
      "cefr_level": "B2",
      "meaning": "A new idea or method, or the use of new ideas and methods.",
      "example": "Technological innovation has revolutionized the way we work.",
      "image_url": None,
      "image_prompt_fallback": "A futuristic laboratory where scientists are designing a glowing, advanced piece of technology."
    },
    {
      "word": "Curriculum",
      "phonetic": "/kəˈrɪk.jə.ləm/",
      "cefr_level": "B2",
      "meaning": "The subjects studied in a school, college, etc. and what each subject includes.",
      "example": "Coding should be integrated into the primary school curriculum.",
      "image_url": None,
      "image_prompt_fallback": "A stack of diverse textbooks including math, art, science, and computer programming, representing a broad education plan."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Irreversible damage (Environment)",
      "meaning": "Harm that cannot be undone or repaired.",
      "example": "Deforestation causes irreversible damage to global biodiversity."
    },
    {
      "collocation": "Technological breakthrough (Technology)",
      "meaning": "An important discovery or event that helps to improve a situation or provide an answer to a technological problem.",
      "example": "The development of quantum computing is a major technological breakthrough."
    },
    {
      "collocation": "Holistic development (Education)",
      "meaning": "The development of a person's intellectual, emotional, social, and physical abilities.",
      "example": "Modern education systems should focus on the holistic development of students."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Nature problems",
      "better_upgrade": "Environmental degradation / Ecological crisis",
      "example": "Environmental degradation is the most pressing issue of our time."
    },
    {
      "weak_phrase": "New computer things",
      "better_upgrade": "Technological advancements / Cutting-edge technology",
      "example": "Hospitals now rely on cutting-edge technology for diagnostics."
    },
    {
      "weak_phrase": "Learning things well",
      "better_upgrade": "Academic excellence / Holistic education",
      "example": "The school has a long-standing reputation for academic excellence."
    }
  ],
  "sentence_frames": [
    "To prevent irreversible damage to the ecosystem, we must...",
    "Thanks to recent technological breakthroughs, society is now able to...",
    "A well-rounded curriculum is essential for the holistic development of..."
  ],
  "ielts_usage_examples": {
    "writing_example": "If schools update their curriculum to include digital literacy, it will not only foster academic excellence but also prepare students for an era of rapid technological advancement.",
    "speaking_example": "Well, regarding the environment, I think the biggest concern is that plastic pollution is causing irreversible damage to our oceans' ecosystems."
  },
  "common_mistakes": [
    "Saying 'equipments' or 'technologies' unnecessarily (Technology and equipment are mostly uncountable in general contexts).",
    "Confusing 'economic' (related to the economy) and 'economical' (good value for money)."
  ],
  "quiz": [
    {
      "question": "Which collocation describes harm to the environment that cannot be fixed?",
      "options": {
        "A": "Permanent hurt",
        "B": "Irreversible damage",
        "C": "Unfixable break",
        "D": "Tough ruin"
      },
      "correct_answer": "B",
      "explanation": "'Irreversible damage' is the standard, high-level collocation used to describe permanent environmental harm."
    },
    {
      "question": "What does 'holistic development' in education refer to?",
      "options": {
        "A": "Focusing only on test scores.",
        "B": "Developing the whole person: mind, body, and emotions.",
        "C": "Learning about religion.",
        "D": "Studying entirely online."
      },
      "correct_answer": "B",
      "explanation": "'Holistic' relates to the whole of something or to the total system instead of just to its parts."
    }
  ]
}

with open('output/lesson_10_paraphrasing_common.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_10, f, indent=2, ensure_ascii=False)
with open('output/lesson_11_avoiding_repetition.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_11, f, indent=2, ensure_ascii=False)
with open('output/lesson_12_topic_collocations.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_12, f, indent=2, ensure_ascii=False)

print("Successfully wrote Batch 4 (Lessons 10-12).")
