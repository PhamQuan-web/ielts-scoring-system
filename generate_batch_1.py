import json

data_01 = {
    "lesson_id": "grammar_01",
    "title": "Relative Clauses",
    "grammar_goal": "This lesson boosts Grammatical Range and Accuracy (GRA) by demonstrating how to confidently create complex sentences using defining and non-defining relative clauses.",
    "core_rule": {
        "formula": "Main Clause + Relative Pronoun (who, which, that, where, when, whose) + Relative Clause",
        "usage": "Use relative clauses to add essential information (defining) without commas, or extra/bonus information (non-defining) with commas.",
        "signals": ["who", "which", "that", "where", "when", "whose"]
    },
    "when_to_use": [
        "To combine two simple sentences into one complex sentence.",
        "To give essential definitions of people or things (Task 2).",
        "To provide extra details without starting a new sentence (Speaking Part 2 & 3)."
    ],
    "when_not_to_use": [
        "Do not use 'that' in non-defining relative clauses (clauses with commas).",
        "Avoid using 'who' for things, or 'which' for people."
    ],
    "ielts_examples": {
        "writing": "The government should invest more in public transport, which would significantly reduce traffic congestion in urban areas.",
        "speaking": "I recently visited a small town where the locals still practice traditional crafts."
    },
    "repair_section": [
        {
            "wrong": "The book which I bought it last week is very interesting.",
            "correct": "The book which I bought last week is very interesting.",
            "better_band_upgrade": "The book that I purchased last week is highly informative."
        },
        {
            "wrong": "My brother that lives in New York is a doctor.",
            "correct": "My brother, who lives in New York, is a doctor.",
            "better_band_upgrade": "My brother, who currently resides in New York, works as a physician."
        }
    ],
    "vietnamese_learner_mistakes": [
        "Repeating the subject or object inside the relative clause (e.g., 'The man who he called me...').",
        "Using 'that' after a comma in non-defining relative clauses.",
        "Omitting the relative pronoun when it acts as the subject of the clause."
    ],
    "mini_sentence_repair_exercise": [
        {
            "wrong_sentence": "Students who they study hard usually get good grades.",
            "correct_sentence": "Students who study hard usually get good grades."
        },
        {
            "wrong_sentence": "Paris, that is the capital of France, is famous for its museums.",
            "correct_sentence": "Paris, which is the capital of France, is famous for its museums."
        }
    ],
    "image_url": "https://images.unsplash.com/photo-1516382766579-246e7f72439c?q=80&w=1600&auto=format&fit=crop",
    "image_prompt_fallback": "A well-dressed teacher pointing to a chalkboard with the words 'who', 'which', and 'that' written on it in clear chalk, with arrows connecting the words to diagrams of a person, a book, and a house.",
    "quiz": [
        {
            "question": "Which sentence is grammatically correct?",
            "options": {
                "A": "My father, that is a teacher, loves reading.",
                "B": "The restaurant where we ate at it last night was amazing.",
                "C": "The woman who called you is my manager.",
                "D": "The car, who I bought yesterday, is very fast."
            },
            "correct_answer": "C",
            "explanation": "Option C is correct. Option A incorrectly uses 'that' after a comma. Option B wrongly repeats 'it' inside the clause. Option D incorrectly uses 'who' for a thing ('car')."
        }
    ]
}

data_02 = {
    "lesson_id": "grammar_02",
    "title": "Conditionals (Zero, First, Second, Third)",
    "grammar_goal": "Improves GRA by showcasing ability to talk about general truths, future possibilities, hypothetical situations, and past regrets.",
    "core_rule": {
        "formula": "If + Condition Clause, Main Clause (Result)",
        "usage": "Zero (If + present, present) for facts; First (If + present, will + base verb) for future possibilities; Second (If + past, would + base verb) for hypothetical present/future; Third (If + past perfect, would have + past participle) for past regrets.",
        "signals": ["If", "Unless", "Provided that", "As long as", "In case"]
    },
    "when_to_use": [
        "Zero conditional: Stating scientific facts or universal truths (Task 1 / Task 2).",
        "First conditional: Discussing likely future consequences of current actions (Task 2 / Speaking Part 3).",
        "Second conditional: Imagining unlikely or impossible situations (Speaking Part 2 / Part 3).",
        "Third conditional: Reflecting on things that didn't happen in the past (Speaking Part 3)."
    ],
    "when_not_to_use": [
        "Do not use 'will' or 'would' immediately after 'If' in the condition clause.",
        "Avoid mixing conditionals incorrectly (e.g., using past simple with 'will')."
    ],
    "ielts_examples": {
        "writing": "If governments implement stricter environmental regulations, pollution levels will decrease significantly.",
        "speaking": "If I had more free time, I would definitely learn to play the piano."
    },
    "repair_section": [
        {
            "wrong": "If it will rain tomorrow, we will stay at home.",
            "correct": "If it rains tomorrow, we will stay at home.",
            "better_band_upgrade": "Should it rain tomorrow, we will remain indoors."
        },
        {
            "wrong": "If I was you, I will apply for that job.",
            "correct": "If I were you, I would apply for that job.",
            "better_band_upgrade": "If I were in your position, I would undoubtedly apply for the role."
        }
    ],
    "vietnamese_learner_mistakes": [
        "Using 'will' in the 'if' clause (e.g., 'If I will have money...').",
        "Forgetting the 'd' in 'would' for second conditional ('If I had time, I go...').",
        "Using 'was' instead of 'were' for all subjects in formal second conditionals (e.g., 'If I was rich...')."
    ],
    "mini_sentence_repair_exercise": [
        {
            "wrong_sentence": "If he study hard, he will pass the exam.",
            "correct_sentence": "If he studies hard, he will pass the exam."
        },
        {
            "wrong_sentence": "If I had knew the answer, I would have told you.",
            "correct_sentence": "If I had known the answer, I would have told you."
        }
    ],
    "image_url": "https://images.unsplash.com/photo-1587691592099-24045742c181?q=80&w=1600&auto=format&fit=crop",
    "image_prompt_fallback": "A split-screen illustration: on the left side, a person holding an umbrella in the rain; on the right side, the same person standing in sunshine thinking about the rain. Words like 'If' and 'Would' floating above.",
    "quiz": [
        {
            "question": "Choose the correct sentence to describe an unreal present situation (Second Conditional).",
            "options": {
                "A": "If I have enough money, I buy a new car.",
                "B": "If I had enough money, I will buy a new car.",
                "C": "If I had enough money, I would buy a new car.",
                "D": "If I will have enough money, I would buy a new car."
            },
            "correct_answer": "C",
            "explanation": "Option C correctly uses the second conditional structure: 'If + Past Simple, Subject + would + base verb' for hypothetical present situations."
        }
    ]
}

data_03 = {
    "lesson_id": "grammar_03",
    "title": "Passive Voice",
    "grammar_goal": "Boosts GRA by demonstrating objective, formal language, crucial for IELTS Writing Task 1 (Process) and Task 2.",
    "core_rule": {
        "formula": "Object of active sentence + to be (in correct tense) + Past Participle (V3) + (by Subject)",
        "usage": "Use the passive voice when the action is more important than who did it, when the doer is unknown, or to maintain a formal, academic tone.",
        "signals": ["is done", "was completed", "has been finished", "will be made", "can be seen"]
    },
    "when_to_use": [
        "Describing processes or manufacturing steps in Writing Task 1.",
        "Stating general opinions formally in Task 2 (e.g., 'It is widely believed that...').",
        "Focusing on the recipient of an action rather than the actor."
    ],
    "when_not_to_use": [
        "Avoid using passive voice when talking about personal experiences in Speaking Part 1 or 2 (active voice is more natural).",
        "Do not use passive voice with intransitive verbs (verbs without an object, e.g., 'happen', 'die', 'arrive')."
    ],
    "ielts_examples": {
        "writing": "First, the raw materials are collected, and then they are transported to the factory for processing.",
        "speaking": "My hometown is known for its beautiful beaches and historical architecture."
    },
    "repair_section": [
        {
            "wrong": "The accident was happened last night.",
            "correct": "The accident happened last night.",
            "better_band_upgrade": "The incident occurred late yesterday evening."
        },
        {
            "wrong": "Many new schools are build in the city.",
            "correct": "Many new schools are being built in the city.",
            "better_band_upgrade": "Numerous educational facilities are currently being constructed across the municipality."
        }
    ],
    "vietnamese_learner_mistakes": [
        "Using passive voice with intransitive verbs (e.g., 'He was died').",
        "Forgetting the 'to be' verb (e.g., 'The house built in 1990').",
        "Using the base form of the verb instead of the past participle (e.g., 'The work was finish')."
    ],
    "mini_sentence_repair_exercise": [
        {
            "wrong_sentence": "This problem should solve immediately.",
            "correct_sentence": "This problem should be solved immediately."
        },
        {
            "wrong_sentence": "A new hospital is building near my house.",
            "correct_sentence": "A new hospital is being built near my house."
        }
    ],
    "image_url": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=1600&auto=format&fit=crop",
    "image_prompt_fallback": "A factory assembly line showing a car being built by robotic arms, symbolizing an automated process where the action is more important than the doer.",
    "quiz": [
        {
            "question": "Identify the grammatically correct passive sentence.",
            "options": {
                "A": "The new bridge was built by the government last year.",
                "B": "The new bridge built last year by the government.",
                "C": "The new bridge was builded last year.",
                "D": "The new bridge was been built last year."
            },
            "correct_answer": "A",
            "explanation": "Option A correctly uses 'was' (past tense 'to be') + 'built' (past participle) to form the past simple passive."
        }
    ]
}

with open('output/grammar_01.json', 'w', encoding='utf-8') as f:
    json.dump(data_01, f, ensure_ascii=False, indent=2)

with open('output/grammar_02.json', 'w', encoding='utf-8') as f:
    json.dump(data_02, f, ensure_ascii=False, indent=2)

with open('output/grammar_03.json', 'w', encoding='utf-8') as f:
    json.dump(data_03, f, ensure_ascii=False, indent=2)

print("Generated output/grammar_01.json, output/grammar_02.json, output/grammar_03.json")
