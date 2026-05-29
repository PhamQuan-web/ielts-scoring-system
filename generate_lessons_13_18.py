import json
import os

os.makedirs("output/grammar_lessons", exist_ok=True)

lesson_13 = {
  "lesson_id": "grammar_13",
  "title": "Sentence Structure: Simple, Compound and Complex Sentences",
  "grammar_goal": "A core requirement for Band 6.0+ in GRA is a 'mix of simple and complex sentence forms'. This lesson ensures control over sentence variety.",
  "core_rule": {
    "formula": "Simple: 1 Independent Clause. Compound: 2 Independent Clauses + FANBOYS (for, and, nor, but, or, yet, so). Complex: Independent Clause + Dependent Clause (because, although, if, when).",
    "usage": "Use simple sentences for clarity and strong statements. Use compound and complex sentences to connect ideas, show relationships (cause/effect, contrast), and demonstrate grammatical range.",
    "signals": ["and", "but", "so", "although", "because", "while", "whereas"]
  },
  "when_to_use": [
    "Writing Task 2: Use complex sentences to develop arguments (e.g., 'Although renewable energy is expensive initially, it saves money in the long term.').",
    "Speaking Part 3: Use compound sentences to expand answers without pausing (e.g., 'I agree with the statement, but we also have to consider the economic impact.').",
    "Writing Task 1: Use complex sentences to compare data (e.g., 'While sales in the UK increased, sales in the US fell.')."
  ],
  "when_not_to_use": [
    "Do not write overly long run-on sentences with multiple 'and's or 'because's, as this reduces clarity.",
    "Do not write paragraphs consisting only of simple sentences (subject + verb + object)."
  ],
  "ielts_examples": {
    "writing": "Even though technological advancements have improved living standards, they have also led to significant environmental degradation.",
    "speaking": "I used to live in a small town, but I moved to the city because I wanted to find a better job."
  },
  "repair_section": [
    {
      "wrong": "The city is very polluted. Many people have respiratory problems.",
      "correct": "Because the city is very polluted, many people have respiratory problems.",
      "better_band_upgrade": "As a direct result of the severe urban pollution, a growing number of citizens are suffering from respiratory issues."
    },
    {
      "wrong": "He studied hard. He failed the exam.",
      "correct": "Although he studied hard, he failed the exam.",
      "better_band_upgrade": "Despite his rigorous study schedule, he ultimately failed to pass the examination."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using 'Although' and 'But' in the same sentence (e.g., 'Although it rained, but I went out.').",
    "Creating comma splices by joining two independent clauses with only a comma, instead of a conjunction."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "Because it was raining, so we stayed at home.",
      "correct_sentence": "Because it was raining, we stayed at home."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1516321497487-e288fb19713f?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "An architectural diagram showing building blocks. One block says 'Simple', two linked blocks say 'Compound', and nested blocks say 'Complex'.",
  "quiz": [
    {
      "question": "Which of the following is a grammatically correct COMPLEX sentence?",
      "options": {
        "A": "It was raining, so I took an umbrella.",
        "B": "Because it was raining, I took an umbrella.",
        "C": "It was raining, I took an umbrella.",
        "D": "Because it was raining, so I took an umbrella."
      },
      "correct_answer": "B",
      "explanation": "A complex sentence uses a subordinating conjunction ('Because') to link a dependent clause to an independent clause without adding a second conjunction like 'so'."
    }
  ]
}

lesson_14 = {
  "lesson_id": "grammar_14",
  "title": "Subject–Verb Agreement",
  "grammar_goal": "Eliminates basic errors. Frequent subject-verb agreement errors will restrict the GRA score to a maximum of Band 5.0.",
  "core_rule": {
    "formula": "Singular Subject -> Singular Verb (usually adds -s/-es). Plural Subject -> Plural Verb.",
    "usage": "The verb must always match the subject in number, even if phrases or clauses separate them. Uncountable nouns always take singular verbs.",
    "signals": ["everyone", "each", "both", "neither", "the number of", "a number of"]
  },
  "when_to_use": [
    "Throughout all Writing and Speaking tasks, strict adherence to subject-verb agreement is mandatory."
  ],
  "when_not_to_use": [
    "Do not let prepositional phrases separating the subject and verb confuse the agreement (e.g., 'The list of items IS on the desk', not ARE)."
  ],
  "ielts_examples": {
    "writing": "The number of students choosing to study abroad has increased dramatically.",
    "speaking": "Everyone in my family enjoys spending time together on the weekends."
  },
  "repair_section": [
    {
      "wrong": "The new regulations for environmental protection is very strict.",
      "correct": "The new regulations for environmental protection are very strict.",
      "better_band_upgrade": "The newly implemented environmental protection policies are exceptionally stringent."
    },
    {
      "wrong": "Everyone have to submit their assignments on time.",
      "correct": "Everyone has to submit their assignments on time.",
      "better_band_upgrade": "Every student is required to submit their coursework prior to the deadline."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Failing to add the 's' to third-person singular verbs in the present tense, often due to L1 interference (Vietnamese verbs do not conjugate).",
    "Treating 'The number of' as plural (it is singular) and 'A number of' as singular (it is plural)."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "A number of people is waiting outside.",
      "correct_sentence": "A number of people are waiting outside."
    },
    {
      "wrong_sentence": "The information provided by the scientists are useful.",
      "correct_sentence": "The information provided by the scientists is useful."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A balanced scale showing a single weight (Singular Subject) balanced perfectly with another single weight (Singular Verb). Text: 'Subject-Verb Agreement: Perfect Balance'.",
  "quiz": [
    {
      "question": "Choose the correct verb to complete the sentence: 'The group of students _____ preparing for their final presentation.'",
      "options": {
        "A": "are",
        "B": "is",
        "C": "were",
        "D": "have"
      },
      "correct_answer": "B",
      "explanation": "The actual subject is 'The group' (singular), not 'students'. Therefore, the singular verb 'is' is correct."
    }
  ]
}

lesson_15 = {
  "lesson_id": "grammar_15",
  "title": "Articles: A, An, The and Zero Article",
  "grammar_goal": "Improves precision and 'native-like' flow. Accurate article usage is a hallmark of Band 7.0+ writing.",
  "core_rule": {
    "formula": "A/An = Indefinite, singular, countable nouns. The = Definite, specific nouns known to both speaker and listener. Zero Article = Plural or uncountable nouns in general.",
    "usage": "Use 'a/an' when introducing something for the first time. Use 'the' when referring to something already mentioned or unique. Use no article when speaking generally about plural or uncountable things.",
    "signals": ["the sun", "an apple", "water (general)", "the water (in this glass)"]
  },
  "when_to_use": [
    "Writing Task 1: Using 'the' with superlatives (e.g., 'the highest percentage', 'the most popular').",
    "Writing Task 2: Using Zero Article for general statements (e.g., 'Education is crucial' NOT 'The education is crucial')."
  ],
  "when_not_to_use": [
    "Do not use 'a/an' with uncountable nouns or plural nouns.",
    "Do not use 'the' when making generalisations about plural nouns (e.g., 'Computers are useful' NOT 'The computers are useful' unless referring to specific ones)."
  ],
  "ielts_examples": {
    "writing": "The advent of the internet has had a profound impact on communication.",
    "speaking": "I work as an accountant in a large multinational company."
  },
  "repair_section": [
    {
      "wrong": "The pollution is a major problem in big cities.",
      "correct": "Pollution is a major problem in big cities.",
      "better_band_upgrade": "Environmental pollution remains a pressing issue in major metropolitan areas."
    },
    {
      "wrong": "He is best student in class.",
      "correct": "He is the best student in the class.",
      "better_band_upgrade": "He consistently demonstrates that he is the most outstanding pupil in the entire cohort."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Omitting articles entirely because Vietnamese does not have direct equivalents to 'a/an/the'.",
    "Overusing 'the' when making general statements about uncountable concepts like 'nature', 'technology', or 'education'."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "I want to buy a new car. Car must be fast.",
      "correct_sentence": "I want to buy a new car. The car must be fast."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1512314889357-e157c22f938d?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A magnifying glass focusing on three small words: A, An, The. Text: 'Articles: Small Words, Big Impact'.",
  "quiz": [
    {
      "question": "Which sentence uses articles correctly for a general statement?",
      "options": {
        "A": "The money cannot buy the happiness.",
        "B": "Money cannot buy the happiness.",
        "C": "Money cannot buy happiness.",
        "D": "A money cannot buy a happiness."
      },
      "correct_answer": "C",
      "explanation": "When speaking generally about uncountable abstract nouns like 'money' and 'happiness', the zero article (no article) should be used."
    }
  ]
}

lesson_16 = {
  "lesson_id": "grammar_16",
  "title": "Countable and Uncountable Nouns",
  "grammar_goal": "Crucial for avoiding basic vocabulary/grammar clashes. Correctly using quantifiers (much/many) determines lexical and grammatical accuracy.",
  "core_rule": {
    "formula": "Countable: can be pluralized (books, ideas). Uncountable: cannot be pluralized, always singular verbs (information, advice, research).",
    "usage": "Use 'many', 'few', 'a/an' with countable nouns. Use 'much', 'little', 'a piece of' with uncountable nouns. Use 'some', 'a lot of' with both.",
    "signals": ["many vs much", "few vs little", "number of vs amount of"]
  },
  "when_to_use": [
    "Writing Task 1: Using 'the number of' for countable items (cars, people) and 'the amount of' for uncountable items (money, water, energy).",
    "Speaking Part 3: Discussing abstract concepts which are often uncountable (knowledge, progress, traffic)."
  ],
  "when_not_to_use": [
    "Do not add '-s' to uncountable nouns.",
    "Do not use 'a/an' immediately before an uncountable noun."
  ],
  "ielts_examples": {
    "writing": "A significant amount of money was allocated to healthcare, whereas the number of schools remained the same.",
    "speaking": "My teacher gave me some excellent advice on how to improve my pronunciation."
  },
  "repair_section": [
    {
      "wrong": "I need to do a lot of researches before writing the essay.",
      "correct": "I need to do a lot of research before writing the essay.",
      "better_band_upgrade": "I must conduct extensive research before commencing my essay."
    },
    {
      "wrong": "The city has too much cars, causing heavy traffics.",
      "correct": "The city has too many cars, causing heavy traffic.",
      "better_band_upgrade": "The city suffers from an excessive number of vehicles, which results in severe traffic congestion."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Pluralizing common uncountable IELTS nouns like 'informations', 'advices', 'equipments', 'knowledges'.",
    "Using 'many' with uncountable nouns (e.g., 'many money')."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "She gave me a good advice.",
      "correct_sentence": "She gave me a piece of good advice. OR She gave me some good advice."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1534452203293-494d7ddbf7e0?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A split image. Left side shows individual apples (Countable). Right side shows a bowl of water or rice (Uncountable). Text: 'Countable vs Uncountable Nouns'.",
  "quiz": [
    {
      "question": "Which of the following phrases is grammatically correct for an IELTS Writing Task 1 chart?",
      "options": {
        "A": "The amount of people visiting the museum.",
        "B": "The number of energy consumed.",
        "C": "The amount of electricity produced.",
        "D": "The much cars on the road."
      },
      "correct_answer": "C",
      "explanation": "'Electricity' is uncountable, so 'the amount of' is correct. 'People' is countable (needs 'number of'), and 'energy' is uncountable (needs 'amount of')."
    }
  ]
}

lesson_17 = {
  "lesson_id": "grammar_17",
  "title": "Pronouns and Clear Referencing",
  "grammar_goal": "Directly impacts the 'Cohesion and Coherence' (CC) score in Writing and Speaking by ensuring the listener/reader can follow ideas smoothly without repetition.",
  "core_rule": {
    "formula": "Pronouns (it, they, this, these, those) replace nouns to avoid repetition. Relative Pronouns (who, which, that) connect clauses.",
    "usage": "Use pronouns to refer back to a noun mentioned in the previous sentence. Ensure the referent (the noun the pronoun replaces) is absolutely clear and unambiguous.",
    "signals": ["this issue", "these problems", "it", "they", "which"]
  },
  "when_to_use": [
    "Writing Task 2: Linking sentences in a paragraph (e.g., 'Global warming is rising. THIS is causing sea levels to increase.').",
    "Speaking Part 3: Maintaining fluency without repeating the subject over and over."
  ],
  "when_not_to_use": [
    "Do not use a pronoun if there are two nouns in the previous sentence and it becomes unclear which one you mean (ambiguity).",
    "Do not shift pronouns randomly (e.g., 'If ONE studies hard, YOU will pass' -> keep it consistent)."
  ],
  "ielts_examples": {
    "writing": "Children nowadays spend hours on screens; this sedentary lifestyle often leads to obesity.",
    "speaking": "My grandfather is a person who has always inspired me."
  },
  "repair_section": [
    {
      "wrong": "Electric cars are expensive. Electric cars are also hard to charge.",
      "correct": "Electric cars are expensive, and they are also hard to charge.",
      "better_band_upgrade": "Electric vehicles are cost-prohibitive; furthermore, they present significant charging logistical challenges."
    },
    {
      "wrong": "Many students use smartphones in class. It is very distracting.",
      "correct": "Many students use smartphones in class. This habit is very distracting.",
      "better_band_upgrade": "A large number of students utilize smartphones during lectures; this particular behavior is highly detrimental to their concentration."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Using 'it' to refer to a plural noun, or 'they' to refer to a singular noun.",
    "Using 'this' without a summary noun (e.g., 'This causes problems' vs 'This trend causes problems'), which is a missed opportunity for vocabulary scoring."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "Parents should monitor their child. They need to ensure he is safe.",
      "correct_sentence": "Parents should monitor their children. They need to ensure they are safe."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A diagram showing a chain link connecting two sentences. An arrow points from the word 'They' back to the word 'Students'. Text: 'Pronouns: Links for Cohesion'.",
  "quiz": [
    {
      "question": "Which of the following uses referencing most effectively for an IELTS essay?",
      "options": {
        "A": "Plastic pollution is killing fish. It is a big problem.",
        "B": "Plastic pollution is killing fish. This environmental disaster requires immediate action.",
        "C": "Plastic pollution is killing fish. Which is bad.",
        "D": "Plastic pollution is killing fish. They are dying."
      },
      "correct_answer": "B",
      "explanation": "Using 'This environmental disaster' acts as a highly cohesive summarizing phrase (demonstrative pronoun + noun), improving both Coherence and Lexical Resource scores."
    }
  ]
}

lesson_18 = {
  "lesson_id": "grammar_18",
  "title": "Prepositions in IELTS Writing and Speaking",
  "grammar_goal": "Fixes micro-errors that prevent candidates from reaching Band 7+ GRA. Correct prepositions demonstrate idiomatic, natural language control.",
  "core_rule": {
    "formula": "Prepositions of time (in, on, at), place (in, on, at), and dependent prepositions (adjective + prep / verb + prep).",
    "usage": "Used to show relationships in time and space, and intrinsically linked to specific verbs and adjectives (collocations).",
    "signals": ["interested IN", "depend ON", "responsible FOR", "increase IN"]
  },
  "when_to_use": [
    "Writing Task 1: Describing data changes accurately (e.g., 'an increase OF 5%', 'increased BY 5%', 'increased TO 50%').",
    "Speaking & Writing: Using correct dependent prepositions to sound natural (e.g., 'I am good AT math')."
  ],
  "when_not_to_use": [
    "Do not translate prepositions directly from your first language, as they rarely match up."
  ],
  "ielts_examples": {
    "writing": "There was a sharp rise in the number of unemployed citizens, peaking at 15% in 2020.",
    "speaking": "I am really passionate about learning foreign languages, especially Spanish."
  },
  "repair_section": [
    {
      "wrong": "The government should invest more money on education.",
      "correct": "The government should invest more money in education.",
      "better_band_upgrade": "It is imperative that the government allocates substantially more financial resources into the education sector."
    },
    {
      "wrong": "Sales dropped from 50% to 30%, which is a decrease by 20%.",
      "correct": "Sales dropped from 50% to 30%, which is a decrease of 20%.",
      "better_band_upgrade": "Sales figures plummeted from 50% to 30%, representing a significant overall decrease of 20%."
    }
  ],
  "vietnamese_learner_mistakes": [
    "Confusing 'in', 'on', and 'at' for time (e.g., 'in the weekend' instead of 'on the weekend' or 'at the weekend').",
    "Using the wrong preposition after 'increase/decrease' in Task 1 (e.g., 'an increase of 2005' instead of 'an increase in 2005')."
  ],
  "mini_sentence_repair_exercise": [
    {
      "wrong_sentence": "I strongly agree to this statement.",
      "correct_sentence": "I strongly agree with this statement."
    },
    {
      "wrong_sentence": "The chart shows a rise of temperatures.",
      "correct_sentence": "The chart shows a rise in temperatures."
    }
  ],
  "image_url": "https://images.unsplash.com/photo-1516962080544-eac695c92f91?q=80&w=1000&auto=format&fit=crop",
  "image_prompt_fallback": "A visual puzzle with pieces fitting together perfectly. The pieces have words like 'rely' and 'on', 'invest' and 'in'. Text: 'Prepositions: Perfect Matches'.",
  "quiz": [
    {
      "question": "Choose the correct preposition for Writing Task 1: 'The unemployment rate increased _____ 5%, rising from 10% to 15%.",
      "options": {
        "A": "to",
        "B": "in",
        "C": "by",
        "D": "of"
      },
      "correct_answer": "C",
      "explanation": "When describing the difference/margin of change, use 'by' (increased by 5%). Use 'to' for the final destination (increased to 15%)."
    }
  ]
}

def save_json(data, filename):
    filepath = os.path.join("output/grammar_lessons", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json(lesson_13, "lesson_13.json")
save_json(lesson_14, "lesson_14.json")
save_json(lesson_15, "lesson_15.json")
save_json(lesson_16, "lesson_16.json")
save_json(lesson_17, "lesson_17.json")
save_json(lesson_18, "lesson_18.json")

print("Generated JSON files for Lessons 13-18.")