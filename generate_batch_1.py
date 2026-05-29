import json
import os

lesson_1 = {
    "lesson_id": "strat_01",
    "title": "IELTS Band Descriptors Explained Simply",
    "strategy_problem": "Many students try to memorize 'Band 9 vocabulary' but ignore the actual rules examiners use to score them. They don't realize that speaking is graded on four equal criteria: Fluency and Coherence, Lexical Resource, Grammatical Range and Accuracy, and Pronunciation.",
    "core_framework": [
        "Fluency and Coherence (FC): Speak continuously without long pauses, and link your ideas smoothly using connectives.",
        "Lexical Resource (LR): Use a variety of words accurately. It's better to use common words perfectly than rare words incorrectly.",
        "Grammatical Range and Accuracy (GRA): Use a mix of simple and complex sentences. Don't worry about minor mistakes if your meaning is clear.",
        "Pronunciation (PR): Speak clearly and naturally. You don't need a British or American accent; your examiner just needs to understand you easily."
    ],
    "ielts_scenario": "In Part 3, the examiner asks a complex question. A student tries to use the word 'ubiquitous' but hesitates for 5 seconds and mispronounces it. The examiner will lower their Fluency and Pronunciation scores, even if the vocabulary word is advanced.",
    "do_dont_table": {
        "do": [
            "Read the official IELTS public band descriptors.",
            "Balance your practice across all four scoring criteria.",
            "Focus on clear communication over complex memorization."
        ],
        "dont": [
            "Memorize long lists of rare words without knowing how to use them.",
            "Worry about your natural accent, as long as it is clear.",
            "Sacrifice fluency just to think of a difficult grammar structure."
        ]
    },
    "example_application": "Instead of saying, 'The ubiquitous nature of vehicular congestion is deleterious' (which sounds unnatural and forced), say, 'Traffic jams are very common nowadays and they cause a lot of problems.' This is fluent, clear, and perfectly grammatical.",
    "personal_action_step": "Download the official IELTS Speaking Public Band Descriptors. Highlight the differences between Band 6 and Band 7 for all four criteria.",
    "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A well-organized study desk with a printed document titled 'IELTS Band Descriptors' highlighted in yellow. A cup of coffee and a notebook are nearby, bright natural lighting.",
    "quiz": [
        {
            "question": "Which of the following is NOT one of the four IELTS Speaking assessment criteria?",
            "options": {
                "A": "Fluency and Coherence",
                "B": "Grammatical Range and Accuracy",
                "C": "Idea Originality and Logic",
                "D": "Pronunciation"
            },
            "correct_answer": "C",
            "explanation": "IELTS tests your language skills, not your general knowledge or the originality of your ideas. The four criteria are Fluency and Coherence, Lexical Resource, Grammatical Range and Accuracy, and Pronunciation."
        }
    ]
}

lesson_2 = {
    "lesson_id": "strat_02",
    "title": "How to Diagnose Your Current Band",
    "strategy_problem": "Students often guess their band score based on how they 'feel' or rely on uncertified feedback. This leads to false confidence or unnecessary panic, because they don't have an objective baseline.",
    "core_framework": [
        "Step 1: Record Yourself - Choose a full practice test (Parts 1, 2, and 3) and record your answers on your phone without stopping.",
        "Step 2: Transcribe and Analyze - Listen back or use a dictation tool to transcribe your answer. Look for hesitation markers, repeated vocabulary, and grammar errors.",
        "Step 3: Compare to Descriptors - Look at the official band descriptors to see where your performance fits. Are you using complex sentences (Band 6+)? Are you pausing frequently (Band 5)?",
        "Step 4: Get Expert Feedback - Have a qualified IELTS tutor or a high-quality AI tool assess your recording to confirm your self-diagnosis."
    ],
    "ielts_scenario": "A student thinks they are Band 7 because they know a lot of vocabulary. However, when they record themselves doing a full 14-minute mock test, they realize they pause frequently in Part 3 and struggle to maintain past tense accuracy in Part 2. Their actual score is closer to Band 5.5.",
    "do_dont_table": {
        "do": [
            "Record audio of your full practice tests.",
            "Listen to your own recordings, even if it feels uncomfortable.",
            "Identify specific, repeated errors (e.g., forgetting 's' on plural nouns)."
        ],
        "dont": [
            "Stop the recording to try again if you make a mistake.",
            "Guess your score based on how well you understood the questions.",
            "Only practice Part 1 because it feels easier."
        ]
    },
    "example_application": "Listen to a 2-minute Part 2 recording. Tally every time you say 'um', 'ah', or pause for more than 2 seconds. Also, count how many different linking words you used (like 'however', 'moreover', 'because'). This gives you hard data on your Fluency and Coherence.",
    "personal_action_step": "Tonight, choose one IELTS Speaking Part 2 topic. Record yourself speaking for exactly 2 minutes. Listen to the recording tomorrow morning and write down three things you want to improve.",
    "image_url": "https://images.unsplash.com/photo-1588196749597-9ff0463949ce?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A student wearing headphones, looking intently at a smartphone recording a voice memo. Notebook open on the desk, concentrated expression.",
    "quiz": [
        {
            "question": "What is the most effective first step to diagnosing your IELTS speaking band?",
            "options": {
                "A": "Reading a vocabulary book",
                "B": "Recording yourself taking a full practice test under timed conditions",
                "C": "Asking a friend who speaks English well to chat with you",
                "D": "Watching YouTube videos of Band 9 speakers"
            },
            "correct_answer": "B",
            "explanation": "Recording yourself under realistic test conditions provides objective evidence of your fluency, grammar, pronunciation, and vocabulary, which you can then analyze against the band descriptors."
        }
    ]
}

lesson_3 = {
    "lesson_id": "strat_03",
    "title": "How to Move from Band 5.5 to 6.5",
    "strategy_problem": "Students stuck at 5.5 usually communicate effectively but rely on simple, short sentences, repeat the same basic words, and pause too frequently to search for language. They need to transition from 'basic survival English' to 'flexible conversational English'.",
    "core_framework": [
        "Expand Length (Fluency): Train yourself to give longer answers in Part 1 and Part 3. Instead of 1-sentence answers, aim for 3-4 sentences using the 'Answer + Reason + Example' structure.",
        "Introduce Complex Grammar (GRA): To reach Band 6, you must use a mix of simple and complex sentence forms. Start practicing relative clauses ('The city WHERE I live...'), conditionals ('If I have time...'), and compound sentences.",
        "Upgrade Vocabulary (LR): Stop repeating words from the examiner's question. Learn synonyms for common concepts (e.g., instead of 'good', use 'beneficial', 'enjoyable', or 'excellent').",
        "Improve Flow (Pronunciation/FC): Work on chunking your speech (grouping words together naturally) rather than speaking word-by-word like a robot."
    ],
    "ielts_scenario": "Examiner: 'Do you like reading?'\nBand 5.5 Answer: 'Yes, I like reading. I read books every day. Books are good.'\nBand 6.5 Answer: 'Absolutely, I'm quite keen on reading. I try to read a few pages every night before bed because it helps me unwind after a long day at work.'",
    "do_dont_table": {
        "do": [
            "Force yourself to extend answers by explaining 'why'.",
            "Practice using complex grammar structures until they feel natural.",
            "Paraphrase the examiner's question in your answer."
        ],
        "dont": [
            "Give one-word answers ('Yes' or 'No').",
            "Worry about making zero mistakes (Band 6 and 6.5 still allow for some grammar errors).",
            "Speak too fast, which leads to more grammatical errors."
        ]
    },
    "example_application": "Take a simple sentence: 'I like my job.' Upgrade it by adding a reason and a complex structure: 'I really enjoy my job because it allows me to work with interesting people, even though the hours can be long.'",
    "personal_action_step": "Choose 5 common IELTS Part 1 questions. Write down a 3-sentence answer for each using the 'Answer + Reason + Example' formula, then practice saying them aloud.",
    "image_url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A graphic showing an arrow moving upward from 5.5 to 6.5, with stylized icons representing 'longer answers', 'complex grammar', and 'better vocabulary'.",
    "quiz": [
        {
            "question": "What is a key requirement for achieving a Band 6.0 in Grammatical Range and Accuracy?",
            "options": {
                "A": "Making absolutely no grammatical mistakes.",
                "B": "Using only simple sentences to ensure complete accuracy.",
                "C": "Using a mix of simple and complex sentence forms.",
                "D": "Using highly advanced academic grammar exclusively."
            },
            "correct_answer": "C",
            "explanation": "According to the official IELTS Band Descriptors, a Band 6 in GRA requires the candidate to use a mix of simple and complex structures, even if they make some errors with the complex ones."
        }
    ]
}

os.makedirs("output", exist_ok=True)
with open("output/lesson_01.json", "w", encoding="utf-8") as f:
    json.dump(lesson_1, f, indent=2)
with open("output/lesson_02.json", "w", encoding="utf-8") as f:
    json.dump(lesson_2, f, indent=2)
with open("output/lesson_03.json", "w", encoding="utf-8") as f:
    json.dump(lesson_3, f, indent=2)

print("Generated lessons 1-3.")
