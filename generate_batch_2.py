import json
import os

os.makedirs('output', exist_ok=True)

# Lesson 4: Examples, Evidence and Explanation Language
lesson_4 = {
  "lesson_id": "vocab_colloc_04",
  "title": "Examples, Evidence and Explanation Language",
  "topic_snapshot": {
    "target_skills": ["Writing", "Speaking"],
    "description": "Sophisticated vocabulary and structures to introduce examples, provide compelling evidence, and explain complex ideas in depth for IELTS Writing Task 2 and Speaking Part 3. Detailed to provide comprehensive options."
  },
  "key_vocabulary_bank": [
    {
      "word": "Corroborate",
      "phonetic": "/kəˈrɒb.ə.reɪt/",
      "cefr_level": "C2",
      "meaning": "To add proof to an account, statement, idea, etc. with new information.",
      "example": "Recent statistical data corroborates the theory that early childhood education is vital for cognitive development.",
      "image_url": None,
      "image_prompt_fallback": "Two puzzle pieces fitting together perfectly, with a magnifying glass examining the joint, symbolizing proof confirming an idea."
    },
    {
      "word": "Substantiate",
      "phonetic": "/səbˈstæn.ʃi.eɪt/",
      "cefr_level": "C1",
      "meaning": "To show something to be true, or to support a claim with facts.",
      "example": "Candidates must substantiate their arguments with relevant real-world examples.",
      "image_url": None,
      "image_prompt_fallback": "A lawyer presenting a glowing document of evidence to a judge in a courtroom."
    },
    {
      "word": "Illustrate",
      "phonetic": "/ˈɪl.ə.streɪt/",
      "cefr_level": "B2",
      "meaning": "To show the meaning or truth of something more clearly, especially by giving examples.",
      "example": "To illustrate this point, consider the rapid technological advancements in the medical field.",
      "image_url": None,
      "image_prompt_fallback": "A presenter pointing to a vibrant, detailed chart on a whiteboard that clearly explains a complex concept."
    },
    {
      "word": "Exemplify",
      "phonetic": "/ɪɡˈzem.plɪ.faɪ/",
      "cefr_level": "C1",
      "meaning": "To be or give a typical example of something.",
      "example": "The city's efficient public transport system perfectly exemplifies sustainable urban planning.",
      "image_url": None,
      "image_prompt_fallback": "A sleek, modern, green-energy tram smoothly gliding through a clean city, representing a perfect example of sustainability."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Provide compelling evidence",
      "meaning": "To offer very strong and convincing proof.",
      "example": "Numerous studies provide compelling evidence that sedentary lifestyles lead to long-term health issues."
    },
    {
      "collocation": "A prime example",
      "meaning": "A very typical or excellent example.",
      "example": "The success of the recycling initiative serves as a prime example of effective community action."
    },
    {
      "collocation": "Lend weight to",
      "meaning": "To make an opinion or claim seem more likely to be true or correct.",
      "example": "The testimonies of multiple experts lend weight to the argument for stricter environmental regulations."
    },
    {
      "collocation": "Empirical data",
      "meaning": "Information derived from observation or experiment rather than theory.",
      "example": "Arguments supported by empirical data are generally considered more robust in academic writing."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "For example",
      "better_upgrade": "A striking example of this is / To illustrate this point",
      "example": "A striking example of this is the profound impact of social media on youth mental health."
    },
    {
      "weak_phrase": "This proves that",
      "better_upgrade": "This provides compelling evidence that / This substantiates the claim that",
      "example": "This provides compelling evidence that transitioning to renewable energy is not just viable, but essential."
    },
    {
      "weak_phrase": "This means that",
      "better_upgrade": "This implies that / Therefore, it stands to reason that",
      "example": "This implies that current educational models may be outdated for the modern workforce."
    }
  ],
  "sentence_frames": [
    "A prime example of this phenomenon can be seen in...",
    "To substantiate this claim, one need only look at...",
    "These findings lend considerable weight to the argument that...",
    "This perfectly exemplifies how [Idea A] fundamentally impacts [Idea B]."
  ],
  "ielts_usage_examples": {
    "writing_example": "To substantiate the claim that remote work boosts productivity, numerous recent surveys provide compelling evidence showing a significant reduction in employee burnout and commuting stress.",
    "speaking_example": "A prime example of this is my own city. Over the last five years, they've completely overhauled the public transport system, which perfectly exemplifies how government investment can improve daily life."
  },
  "common_mistakes": [
    "Using 'an advice' or 'an evidence' (these are uncountable nouns and cannot take an indefinite article 'a/an').",
    "Writing 'For instance, taking the example of...' which is tautological (repetitive). Use either 'For instance,' or 'Take the example of...'."
  ],
  "quiz": [
    {
      "question": "Which verb is the best C2-level upgrade for 'prove' when referring to adding new information to support a theory?",
      "options": {
        "A": "Illustrate",
        "B": "Corroborate",
        "C": "Exemplify",
        "D": "Show"
      },
      "correct_answer": "B",
      "explanation": "'Corroborate' means to confirm or give support to a statement, theory, or finding, and is a strong C2 verb."
    },
    {
      "question": "Select the correct collocation to describe a very strong and convincing piece of proof.",
      "options": {
        "A": "Compelling evidence",
        "B": "Heavy proof",
        "C": "Hardly evidence",
        "D": "Forced proof"
      },
      "correct_answer": "A",
      "explanation": "'Compelling evidence' is the natural academic collocation for evidence that makes you believe it or accept it because it is so strong."
    }
  ]
}

# Lesson 5: Hedging and Precision Language
lesson_5 = {
  "lesson_id": "vocab_colloc_05",
  "title": "Hedging and Precision Language",
  "topic_snapshot": {
    "target_skills": ["Writing"],
    "description": "Crucial language for making claims more accurate, academic, and less absolute (Band 7+ requirement). Avoiding sweeping generalizations."
  },
  "key_vocabulary_bank": [
    {
      "word": "Arguably",
      "phonetic": "/ˈɑːɡ.ju.ə.bli/",
      "cefr_level": "B2",
      "meaning": "Used when stating an opinion or belief that you think can be shown to be true.",
      "example": "She is arguably the greatest athlete of her generation.",
      "image_url": None,
      "image_prompt_fallback": "A balanced scale showing a strong argument outweighing a weaker one, representing a defensible opinion."
    },
    {
      "word": "Predominantly",
      "phonetic": "/prɪˈdɒm.ɪ.nənt.li/",
      "cefr_level": "C1",
      "meaning": "Mostly or mainly.",
      "example": "The audience at the concert was predominantly young teenagers.",
      "image_url": None,
      "image_prompt_fallback": "A crowd of people where the vast majority are wearing blue shirts, highlighting the concept of 'mostly'."
    },
    {
      "word": "Plausible",
      "phonetic": "/ˈplɔː.zə.bəl/",
      "cefr_level": "C1",
      "meaning": "Seeming likely to be true, or able to be believed.",
      "example": "It is entirely plausible that artificial intelligence will replace certain routine administrative jobs.",
      "image_url": None,
      "image_prompt_fallback": "A person nodding thoughtfully while reviewing a realistic and logical plan on a document."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "A vast majority",
      "meaning": "Almost everyone or everything in a group (more precise than 'all').",
      "example": "A vast majority of the respondents indicated that they prefer flexible working hours."
    },
    {
      "collocation": "Highly unlikely",
      "meaning": "Very improbable (softer and more academic than 'impossible').",
      "example": "It is highly unlikely that a single solution will resolve the complex issue of climate change."
    },
    {
      "collocation": "Tend to",
      "meaning": "To be likely to behave in a particular way or have a particular characteristic.",
      "example": "People tend to be more productive when they work in a well-lit environment."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Everyone thinks that",
      "better_upgrade": "It is widely believed that / A vast majority argue that",
      "example": "It is widely believed that physical education is crucial for child development."
    },
    {
      "weak_phrase": "This will cause",
      "better_upgrade": "This is highly likely to result in / This may potentially trigger",
      "example": "Ignoring environmental policies is highly likely to result in irreversible ecological damage."
    },
    {
      "weak_phrase": "It is impossible",
      "better_upgrade": "It is highly improbable / It seems unlikely",
      "example": "It is highly improbable that global eradication of poverty can be achieved within a single decade."
    }
  ],
  "sentence_frames": [
    "It is generally accepted that [Subject] tends to...",
    "While it is plausible that [A], it is highly unlikely that [B].",
    "A significant proportion of society arguably benefits from..."
  ],
  "ielts_usage_examples": {
    "writing_example": "While strict censorship may arguably prevent the spread of misinformation, it is highly unlikely to be effective in an era dominated by decentralized social media.",
    "speaking_example": "I'd say people predominantly consume news through their smartphones nowadays, as it tends to be far more convenient than buying a physical newspaper."
  },
  "common_mistakes": [
    "Using absolute terms like 'All people', 'Always', or 'Never' which makes arguments vulnerable and lowers the Task Response score.",
    "Using 'majority of' without 'the' or 'a' (e.g., writing 'Majority of people' instead of 'The majority of people')."
  ],
  "quiz": [
    {
      "question": "Which of the following sentences uses appropriate academic hedging?",
      "options": {
        "A": "Technology always ruins interpersonal communication.",
        "B": "Nobody talks face-to-face anymore because of smartphones.",
        "C": "Heavy reliance on smartphones tends to diminish face-to-face interaction.",
        "D": "Smartphones will definitely destroy human relationships entirely."
      },
      "correct_answer": "C",
      "explanation": "Option C uses 'tends to' to hedge the claim, avoiding the absolute, generalized statements found in A, B, and D, which are penalized in IELTS."
    },
    {
      "question": "Which word is a C1-level synonym for 'mostly' or 'mainly'?",
      "options": {
        "A": "Plausibly",
        "B": "Arguably",
        "C": "Predominantly",
        "D": "Absolutely"
      },
      "correct_answer": "C",
      "explanation": "'Predominantly' is an excellent academic adverb to express that something consists mostly or primarily of a particular element."
    }
  ]
}

# Lesson 6: Academic Verb Collocations
lesson_6 = {
  "lesson_id": "vocab_colloc_06",
  "title": "Academic Verb Collocations",
  "topic_snapshot": {
    "target_skills": ["Writing"],
    "description": "Essential verb-noun pairings that instantly elevate the academic tone of essays."
  },
  "key_vocabulary_bank": [
    {
      "word": "Ascertain",
      "phonetic": "/ˌæs.əˈteɪn/",
      "cefr_level": "C1",
      "meaning": "To discover something with certainty.",
      "example": "The police have so far been unable to ascertain the cause of the explosion.",
      "image_url": None,
      "image_prompt_fallback": "A detective looking intently through a magnifying glass at a clue, discovering the truth."
    },
    {
      "word": "Elicit",
      "phonetic": "/iˈlɪs.ɪt/",
      "cefr_level": "C2",
      "meaning": "To get or produce something, especially information or a reaction.",
      "example": "The questionnaire was designed to elicit detailed feedback about the new product.",
      "image_url": None,
      "image_prompt_fallback": "An interviewer asking a profound question that brings out an emotional and thoughtful response from the interviewee."
    },
    {
      "word": "Postulate",
      "phonetic": "/ˈpɒs.tʃə.leɪt/",
      "cefr_level": "C2",
      "meaning": "To suggest a theory, idea, or principle as a basic fact from which a further idea is formed.",
      "example": "The linguist postulated that all human languages share a deep, underlying structure.",
      "image_url": None,
      "image_prompt_fallback": "A scientist standing in front of a chalkboard filled with complex equations, presenting a new foundational theory."
    }
  ],
  "collocation_builder": [
    {
      "collocation": "Conduct research",
      "meaning": "To carry out a systematic investigation.",
      "example": "Universities conduct research to expand human knowledge."
    },
    {
      "collocation": "Address a concern",
      "meaning": "To start trying to solve a problem or worry.",
      "example": "The government must urgently address the growing concern regarding air quality."
    },
    {
      "collocation": "Yield results",
      "meaning": "To produce or provide findings or outcomes.",
      "example": "The new teaching methodology is expected to yield positive results by the end of the semester."
    }
  ],
  "upgrade_section": [
    {
      "weak_phrase": "Find out",
      "better_upgrade": "Ascertain / Determine",
      "example": "It is crucial to ascertain the root causes of urban poverty."
    },
    {
      "weak_phrase": "Get a reaction",
      "better_upgrade": "Elicit a response / Provoke a reaction",
      "example": "The controversial policy elicited a strong response from the public."
    },
    {
      "weak_phrase": "Give out information",
      "better_upgrade": "Disseminate information",
      "example": "The internet makes it incredibly easy to disseminate information globally."
    }
  ],
  "sentence_frames": [
    "To address this pressing concern, authorities must...",
    "Recent studies conducted by experts yield results that suggest...",
    "It is difficult to ascertain precisely why..."
  ],
  "ielts_usage_examples": {
    "writing_example": "Before implementing widespread educational reforms, it is vital to conduct comprehensive research to ascertain whether the new methods will yield tangible results.",
    "speaking_example": "If the council wants to address the concern of littering, they really need to disseminate information more effectively to elicit a change in public behavior."
  },
  "common_mistakes": [
    "Using 'do research' instead of the stronger academic collocation 'conduct research' or 'carry out research'.",
    "Writing 'make an effort to solve' when 'address an issue' is far more concise and academic."
  ],
  "quiz": [
    {
      "question": "Which verb accurately replaces 'get' in the phrase 'get a reaction from the crowd'?",
      "options": {
        "A": "Ascertain",
        "B": "Elicit",
        "C": "Postulate",
        "D": "Conduct"
      },
      "correct_answer": "B",
      "explanation": "'Elicit' means to draw out a response, answer, or fact from someone in reaction to one's own actions or questions."
    },
    {
      "question": "Which is the most natural academic collocation?",
      "options": {
        "A": "Make research",
        "B": "Perform research",
        "C": "Conduct research",
        "D": "Create research"
      },
      "correct_answer": "C",
      "explanation": "'Conduct research' is the standard, most frequently used academic collocation in English."
    }
  ]
}

with open('output/lesson_04_examples_evidence.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_4, f, indent=2, ensure_ascii=False)
with open('output/lesson_05_hedging_precision.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_5, f, indent=2, ensure_ascii=False)
with open('output/lesson_06_academic_verbs.json', 'w', encoding='utf-8') as f:
    json.dump(lesson_6, f, indent=2, ensure_ascii=False)

print("Successfully wrote Batch 2 (Lessons 4-6).")
