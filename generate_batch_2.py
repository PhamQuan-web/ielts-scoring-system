import json
import os

lesson_4 = {
    "lesson_id": "strat_04",
    "title": "How to Move from Band 6.5 to 7.0",
    "strategy_problem": "Students at Band 6.5 usually have a solid grasp of English but fall short of 7.0 due to a lack of 'flexibility' and 'idiomatic language' in Lexical Resource, or they make frequent small errors that prevent them from achieving 'frequent error-free sentences' in Grammatical Range and Accuracy.",
    "core_framework": [
        "Idiomatic Language (LR): Band 7 requires 'some awareness of style and collocation, including idiomatic vocabulary.' This doesn't just mean idioms like 'raining cats and dogs'. It means natural collocations (e.g., 'a profound impact' instead of 'a big impact') and phrasal verbs.",
        "Error-Free Sentences (GRA): To hit Band 7, the majority of your sentences must be error-free. You need to focus on accuracy with complex structures, not just attempting them.",
        "Topic Development (FC): Your answers in Part 3 need deeper development. Move beyond simple 'Reason + Example' to exploring alternatives, discussing hypotheticals, or analyzing causes and effects."
    ],
    "ielts_scenario": "A student answers a Part 3 question about the future of transportation by saying, 'I think cars will fly. It is good for people.' This is too simple for Band 7. A Band 7 answer would be, 'It's highly likely that we'll see a shift towards autonomous flying vehicles, which could drastically reduce congestion on the ground.'",
    "do_dont_table": {
        "do": [
            "Learn vocabulary in 'chunks' or collocations, not just isolated words.",
            "Practice self-correction. If you make a mistake while speaking, naturally correct it (e.g., 'He go... sorry, he goes...'). This is acceptable at Band 7.",
            "Use a wider range of cohesive devices naturally (e.g., 'Having said that...', 'On the flip side...')."
        ],
        "dont": [
            "Force unnatural idioms into your answers just to tick a box.",
            "Try to use overly complex grammar if you are unsure of how it works; it leads to too many errors.",
            "Give brief, superficial answers in Part 3."
        ]
    },
    "example_application": "Instead of using the basic idiom 'a piece of cake', use more natural phrasing like 'It was relatively straightforward' or 'I found it quite effortless.'",
    "personal_action_step": "Review a recent practice essay or speaking recording. Identify 3 basic verbs or adjectives you used (like 'good', 'bad', 'do', 'make') and find strong, natural collocations to replace them.",
    "image_url": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A close-up of a student writing in a notebook, with a focus on advanced vocabulary words crossed out and replaced with natural collocations.",
    "quiz": [
        {
            "question": "According to the IELTS Band Descriptors, what is a specific requirement for Band 7 Lexical Resource that is NOT required for Band 6?",
            "options": {
                "A": "Using only simple vocabulary",
                "B": "Using some less common and idiomatic vocabulary",
                "C": "Having a perfect, native-like accent",
                "D": "Never making any vocabulary mistakes"
            },
            "correct_answer": "B",
            "explanation": "Band 7 requires candidates to use some less common and idiomatic vocabulary and show some awareness of style and collocation, whereas Band 6 only requires an adequate range of vocabulary for the task."
        }
    ]
}

lesson_5 = {
    "lesson_id": "strat_05",
    "title": "The IELTS Improvement Loop",
    "strategy_problem": "Many students think doing endless practice tests is the key to improving. They take a test, check their score, feel disappointed, and immediately take another test. This is just measuring your current level, not improving it.",
    "core_framework": [
        "Phase 1: Practice (The Output) - Do a task under realistic, timed conditions to see what you can produce naturally.",
        "Phase 2: Analyze (The Diagnosis) - Critically review your performance. What went wrong? Did you lack vocabulary? Did you struggle with a specific grammar structure? Did you run out of time?",
        "Phase 3: Learn (The Input) - Based on your diagnosis, learn the specific missing pieces. Study the necessary grammar, learn the topical vocabulary, or read model answers.",
        "Phase 4: Apply (The Correction) - Redo the exact same task, applying what you just learned. This builds new, correct habits."
    ],
    "ielts_scenario": "A student writes a Task 2 essay and gets a 6.0. Instead of writing a new essay on a new topic, they analyze the 6.0 essay, realize they lacked vocabulary for the topic of 'Environment', study 10 new environmental collocations, and then rewrite the same essay aiming for a 7.0.",
    "do_dont_table": {
        "do": [
            "Spend as much time reviewing a practice test as you did taking it.",
            "Keep an 'error log' notebook to track your common mistakes.",
            "Rewrite essays and re-record speaking answers after getting feedback."
        ],
        "dont": [
            "Take multiple practice tests in one day without reviewing them.",
            "Just look at the overall band score and ignore the detailed feedback.",
            "Assume that 'more practice' automatically equals 'better score'."
        ]
    },
    "example_application": "You take a Listening test and score 25/40. During review, you realize you missed 5 points because you couldn't spell the words correctly, and 3 points because you lost focus. You spend the next day practicing spelling for common IELTS words and doing focus exercises, rather than just taking another test.",
    "personal_action_step": "Take the last essay or speaking recording you did. Do not do a new one today. Instead, spend 30 minutes identifying your top 3 weaknesses in that specific attempt, and find the resources to fix them.",
    "image_url": "https://images.unsplash.com/photo-1507925922837-326524661005?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A circular diagram drawn on a whiteboard showing a cycle of 'Practice -> Analyze -> Learn -> Apply'. A hand is holding a marker, pointing to the 'Analyze' step.",
    "quiz": [
        {
            "question": "What is the most common mistake students make regarding IELTS practice?",
            "options": {
                "A": "Taking too few practice tests",
                "B": "Focusing too much on learning new vocabulary",
                "C": "Taking test after test without analyzing their mistakes and learning from them",
                "D": "Practicing only the speaking section"
            },
            "correct_answer": "C",
            "explanation": "Continuous testing without analysis only measures your current ability; it does not build the new skills required to improve your score. The Improvement Loop requires pausing to learn and apply corrections."
        }
    ]
}

lesson_6 = {
    "lesson_id": "strat_06",
    "title": "How to Build Ideas Quickly",
    "strategy_problem": "Students often freeze in the Speaking or Writing exams because they don't know 'what' to say. They think they need profound, highly original ideas to score well. This leads to long pauses and lost points for Fluency and Coherence.",
    "core_framework": [
        "1. The 'Personal to Global' Method: Start by thinking about how the topic affects you personally, then your family/friends, then your city/country, and finally the world. This provides a natural progression of ideas.",
        "2. The 'Wh- Questions' Technique: If stuck, silently ask yourself: Who, What, Where, When, Why, and How. This generates immediate angles to talk about.",
        "3. The 'Opposite Perspective' Trick: If you can't think of why something is good, think about what would happen if it didn't exist. E.g., 'Why is exercise important?' -> 'Well, without it, people become lethargic and develop health issues...'",
        "4. The 'Lie' Strategy: IELTS is a language test, not a polygraph. If you can't remember a real example, invent a plausible one quickly. The examiner only cares about your English."
    ],
    "ielts_scenario": "In Speaking Part 3, the examiner asks: 'How has technology changed the way we work?' A student freezes because they don't know much about the global economy. Instead, they use the 'Personal to Global' method: 'Well, personally, I can work from home now. This is true for many of my friends too. On a larger scale, companies no longer need huge offices...'",
    "do_dont_table": {
        "do": [
            "Use brainstorming frameworks like 'Personal to Global'.",
            "Remember that simple, clear ideas expressed in excellent English score higher than complex ideas expressed in poor English.",
            "Invent examples if you need to; the truth doesn't matter, only the language."
        ],
        "dont": [
            "Wait for the 'perfect' idea before you start speaking or writing.",
            "Worry that your ideas are too simple or unoriginal.",
            "Try to discuss topics you have no vocabulary for, just because they sound impressive."
        ]
    },
    "example_application": "Topic: 'The importance of museums'. Using the 'Wh- Questions' technique: WHO visits them? (Students, tourists). WHY are they important? (Preserve history). WHAT would happen without them? (We'd lose our connection to the past). You now have three solid points to discuss.",
    "personal_action_step": "Pick 5 random IELTS Task 2 essay prompts. Give yourself exactly 2 minutes per prompt to brainstorm 3 main ideas using the 'Personal to Global' or 'Wh- Questions' methods.",
    "image_url": "https://images.unsplash.com/photo-1512314889357-e157c22f938d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A person sitting at a desk with a notebook, brainstorming ideas with a mind map. The central bubble says 'Technology' and branches out into 'Personal', 'Work', and 'Society'.",
    "quiz": [
        {
            "question": "If you are asked a question in IELTS Speaking and you don't know the factual answer, what is the best strategy?",
            "options": {
                "A": "Tell the examiner you don't know and ask for a different question.",
                "B": "Invent a plausible answer or example, because IELTS tests your language, not your factual knowledge.",
                "C": "Stay silent until you can think of the correct factual answer.",
                "D": "Apologize repeatedly for your lack of knowledge."
            },
            "correct_answer": "B",
            "explanation": "IELTS is purely a test of English proficiency. The examiner is evaluating how well you can communicate an idea, not whether the idea is factually true or profound."
        }
    ]
}

os.makedirs("output", exist_ok=True)
with open("output/lesson_04.json", "w", encoding="utf-8") as f:
    json.dump(lesson_4, f, indent=2)
with open("output/lesson_05.json", "w", encoding="utf-8") as f:
    json.dump(lesson_5, f, indent=2)
with open("output/lesson_06.json", "w", encoding="utf-8") as f:
    json.dump(lesson_6, f, indent=2)

print("Generated lessons 4-6.")
