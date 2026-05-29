import json
import os

lesson_13 = {
    "lesson_id": "strat_13",
    "title": "How to Use Vocabulary Naturally",
    "strategy_problem": "A major issue for candidates aiming for Band 7+ is 'forced vocabulary.' They learn lists of complex, obscure words and awkwardly shoehorn them into sentences where they don't belong, resulting in a lower Lexical Resource score due to poor collocation and style.",
    "core_framework": [
        "1. Learn Collocations, Not Single Words: Never learn 'impact' alone. Learn 'a profound impact,' 'a significant impact,' 'to mitigate an impact.' Words travel in packs.",
        "2. The Context Rule: Just because two words are synonyms in a dictionary does not mean they are interchangeable. 'Consequences' is usually negative, whereas 'results' is neutral. Using them incorrectly changes your meaning.",
        "3. Active vs. Passive Vocabulary: You don't need to actively use every complex word you understand. Aim to upgrade your 'active' vocabulary—words you can deploy instantly while speaking without hesitation.",
        "4. Phrasal Verbs in Speaking: In Speaking, idiomatic language often means natural phrasal verbs, not Shakespearean vocabulary. Using 'figure out' is often more natural than 'ascertain' in a spoken context."
    ],
    "ielts_scenario": "In Speaking Part 1, the examiner asks: 'Do you like your hometown?' The student answers: 'Yes, the ubiquitous nature of the benevolent local populace is highly advantageous.' This sounds ridiculous and will score poorly. A Band 8 answer would be: 'Absolutely, the locals are incredibly welcoming, and there's a real sense of community that I genuinely appreciate.'",
    "do_dont_table": {
        "do": [
            "Use online collocations dictionaries (like OZDIC) to see how words combine naturally.",
            "Record new vocabulary in full sentences context, not isolated lists.",
            "Use phrasal verbs and idiomatic expressions in the Speaking test to sound more natural."
        ],
        "dont": [
            "Use a complex word if you are unsure of exactly how it functions in a sentence.",
            "Try to use overly formal, academic language in Speaking Parts 1 and 2.",
            "Replace every simple word with a complex synonym; it ruins fluency."
        ]
    },
    "example_application": "Instead of trying to use the word 'ameliorate' (to make better) in a speaking test about your hobby, use a natural collocation like 'It really helps me unwind' or 'It takes my mind off things.'",
    "personal_action_step": "Take 5 words you recently learned. Look them up in a collocations dictionary and write down two common adjective-noun or verb-noun pairings for each. Then, write a sentence for each pairing.",
    "image_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A close up of a notebook. A single word is written, crossed out, and replaced by a phrase showing the word used naturally within a complete sentence context.",
    "quiz": [
        {
            "question": "Why is 'forced vocabulary' heavily penalized in the IELTS Speaking test?",
            "options": {
                "A": "Examiners prefer candidates to use only very simple, basic English.",
                "B": "It shows a lack of awareness of collocation, style, and natural usage, reducing clarity.",
                "C": "Complex words take too long to say, which wastes test time.",
                "D": "It proves the candidate has memorized their answers."
            },
            "correct_answer": "B",
            "explanation": "Higher bands in Lexical Resource require candidates to show an awareness of style and collocation. Using a 'big word' incorrectly demonstrates that the candidate does not truly understand how the language works."
        }
    ]
}

lesson_14 = {
    "lesson_id": "strat_14",
    "title": "How to Improve Grammar Accuracy",
    "strategy_problem": "Candidates know grammatical rules in theory but fail to apply them in real-time under exam conditions. This 'knowledge-performance gap' results in frequent minor errors (like dropping plurals or articles) that keep their GRA score at Band 6.",
    "core_framework": [
        "1. Identify Fossilized Errors: These are mistakes you've made so often they feel 'right' to you. You cannot fix them until you identify them through recording yourself or getting expert feedback.",
        "2. Focused Drilling: Do not study 'all of grammar.' If your issue is present perfect, spend a week writing and speaking sentences using *only* the present perfect until the structure becomes automatic.",
        "3. The 'Slow Down' Strategy (Speaking): Fluency does not equal speed. Speaking slightly slower gives your brain the millisecond it needs to process grammatical structures correctly before they leave your mouth.",
        "4. The Proofreading Pass (Writing): Dedicate the last 3-5 minutes of your Writing task strictly to checking for your known fossilized errors. Do not look for new ideas; only look for missing 's' endings, article issues, or verb tense mismatches."
    ],
    "ielts_scenario": "A student writing Task 1 accurately describes a chart but writes 'The number of cars have increased.' They know 'number' is singular and requires 'has', but in the rush of writing, their hand writes 'have'. Without a dedicated proofreading pass, they lose points for a basic error.",
    "do_dont_table": {
        "do": [
            "Speak at a deliberate, measured pace to allow for real-time grammatical processing.",
            "Target one specific grammar weakness at a time during practice.",
            "Always reserve 3 minutes at the end of Writing tasks specifically for error-checking."
        ],
        "dont": [
            "Try to use highly complex conditional structures if you still struggle with basic past tense.",
            "Assume that 'knowing the rule' means you won't make the mistake under pressure.",
            "Submit a practice essay without proofreading it yourself first."
        ]
    },
    "example_application": "If your fossilized error is dropping the 's' on third-person verbs ('he go' instead of 'he goes'), spend 10 minutes a day reading English texts aloud, heavily emphasizing every 's' sound at the end of verbs to retrain your mouth and ears.",
    "personal_action_step": "Review your last three marked essays or speaking feedback notes. Identify the single most frequent grammar mistake you make. Write out the rule for that grammar point and create 10 correct sentences using it.",
    "image_url": "https://images.unsplash.com/photo-1503694978374-8a2fa686963a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A person writing an essay, zooming in on the pen correcting a verb tense from past to present, symbolizing grammatical accuracy.",
    "quiz": [
        {
            "question": "What is a 'fossilized error'?",
            "options": {
                "A": "A grammar rule that is no longer used in modern English.",
                "B": "A mistake that a student has made repeatedly for a long time, so it feels natural and is hard to correct.",
                "C": "An error that only occurs when writing about historical topics.",
                "D": "A mistake made by the examiner."
            },
            "correct_answer": "B",
            "explanation": "Fossilized errors are ingrained habits. Because they feel correct to the speaker, they are very difficult to eliminate without conscious, targeted drilling."
        }
    ]
}

lesson_15 = {
    "lesson_id": "strat_15",
    "title": "How to Practise Speaking Alone",
    "strategy_problem": "Students often believe they can only improve their speaking score if they have a native speaker to practice with. Since they lack a partner, they simply don't practice speaking, leading to stagnation.",
    "core_framework": [
        "1. Shadowing: Find a podcast or interview with a clear English speaker. Listen to a sentence, pause, and repeat it exactly, mimicking their intonation, stress, and rhythm. This improves Pronunciation and chunking.",
        "2. The 'Mirror and Record' Method: Answer a Part 2 cue card while looking in a mirror. More importantly, record it on your phone. Listening back provides immediate, objective feedback on hesitation and filler words (um, ah).",
        "3. Topical Brainstorming Aloud: Pick a random topic (e.g., 'Transport'). Talk to yourself out loud for 1 minute about anything related to that topic. This trains your brain to retrieve vocabulary quickly without the pressure of a specific question.",
        "4. The 4/3/2 Technique: Speak on a topic for 4 minutes. Then, speak on the exact same topic for 3 minutes, compressing your ideas. Finally, do it in 2 minutes. This forces you to eliminate hesitation and use more concise, advanced language."
    ],
    "ielts_scenario": "A student lives in a non-English speaking country and has no study partners. Instead of giving up, they use the 4/3/2 technique every morning with IELTS Part 2 cue cards. Over a month, their fluency improves dramatically because their brain learns to organize ideas faster and retrieve vocabulary more efficiently under time constraints.",
    "do_dont_table": {
        "do": [
            "Record your solo practice sessions; the recording is your 'partner'.",
            "Focus heavily on intonation and rhythm during shadowing exercises.",
            "Speak out loud, not just in your head. The physical muscles of your mouth need training."
        ],
        "dont": [
            "Just read model answers silently.",
            "Stop the recording every time you make a mistake.",
            "Use the excuse that you don't have a native speaker partner to avoid practicing."
        ]
    },
    "example_application": "Take a TED Talk transcript. Play 10 seconds of audio. Pause. Repeat it aloud, trying to match the speaker's emotional tone and where they placed stress on words (e.g., 'It was ABSOLUTELY essential').",
    "personal_action_step": "Find a random IELTS Speaking Part 2 cue card online. Do not prepare. Hit record on your phone and speak for 2 minutes. Listen back and count how many times you said 'um' or 'uh'.",
    "image_url": "https://images.unsplash.com/photo-1516383274235-5f42d6c6426d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A person looking into a mirror while holding a smartphone recording audio, actively practicing speaking alone in a quiet room.",
    "quiz": [
        {
            "question": "What is the primary purpose of the '4/3/2 Technique' in speaking practice?",
            "options": {
                "A": "To learn how to speak for exactly 4 minutes in the exam.",
                "B": "To memorize an answer perfectly by repeating it three times.",
                "C": "To force the speaker to organize ideas faster, eliminate hesitation, and become more concise and fluent on a topic.",
                "D": "To practice listening to instructions."
            },
            "correct_answer": "C",
            "explanation": "By reducing the time allowed to discuss the same topic, the 4/3/2 technique forces the brain to bypass filler words and hesitation, directly improving the fluency score."
        }
    ]
}

os.makedirs("output", exist_ok=True)
with open("output/lesson_13.json", "w", encoding="utf-8") as f:
    json.dump(lesson_13, f, indent=2)
with open("output/lesson_14.json", "w", encoding="utf-8") as f:
    json.dump(lesson_14, f, indent=2)
with open("output/lesson_15.json", "w", encoding="utf-8") as f:
    json.dump(lesson_15, f, indent=2)

print("Generated lessons 13-15.")
