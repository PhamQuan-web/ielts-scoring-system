import json
import os

lesson_7 = {
    "lesson_id": "strat_07",
    "title": "How to Review Your Own Mistakes",
    "strategy_problem": "Students often struggle to identify their own errors, particularly in speaking and writing. They rely entirely on teachers, which slows down their progress. Without the skill of self-correction, candidates repeat the same fossilized errors in the exam.",
    "core_framework": [
        "1. The 'Time Delay' Technique: Never review your writing immediately. Wait at least 24 hours. Your brain will reset, and you will read what you *actually* wrote, rather than what you *intended* to write.",
        "2. Single-Focus Editing: Do not try to find every mistake at once. Read your essay three times: once just for grammar (e.g., subject-verb agreement), once for vocabulary (looking for repetitions), and once for task response/logic.",
        "3. The 'Read Aloud' Test: Read your essay aloud. If you stumble or run out of breath, the sentence is likely too long, grammatically awkward, or poorly punctuated.",
        "4. The Error Log: Create a spreadsheet. When you find a mistake, log the error, the correction, and the *reason* why it was wrong. Review this log before your next practice test."
    ],
    "ielts_scenario": "A student consistently scores 6.0 in Writing because they frequently forget the 's' on third-person singular verbs. Because they read their essays silently and quickly, their brain auto-corrects the missing 's'. When they start using the 'Read Aloud' test, they hear the missing 's' and fix it, instantly improving their Grammatical Range and Accuracy score.",
    "do_dont_table": {
        "do": [
            "Wait a day before reviewing your own writing.",
            "Read your essays out loud to catch awkward phrasing.",
            "Maintain an active error log of your repeated mistakes."
        ],
        "dont": [
            "Try to fix grammar, vocabulary, and structure all at the same time.",
            "Rely 100% on a teacher to find every single mistake for you.",
            "Just look at the score and ignore the detailed feedback on what went wrong."
        ]
    },
    "example_application": "Instead of glancing over your essay for 2 minutes after writing it, put it away. Tomorrow, spend 10 minutes reading it strictly to check if every subject matches its verb. Then, spend another 5 minutes checking if you overused the word 'important'.",
    "personal_action_step": "Create a simple 'Error Log' in Excel or Google Sheets with three columns: 'Mistake', 'Correction', and 'Why it was wrong'. Log 5 mistakes from your last practice test.",
    "image_url": "https://images.unsplash.com/photo-1586282391129-76a6df230234?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A close-up of a printed essay with red pen marks circling mistakes. A neatly organized notebook labeled 'Error Log' sits next to it.",
    "quiz": [
        {
            "question": "What is the primary benefit of the 'Time Delay' technique when reviewing your own writing?",
            "options": {
                "A": "It gives you time to forget the topic so you can write a better essay.",
                "B": "It prevents your brain from 'auto-correcting' mistakes based on what you intended to write.",
                "C": "It ensures you are less tired so you can write faster.",
                "D": "It allows you time to ask a teacher for the answers."
            },
            "correct_answer": "B",
            "explanation": "Immediately after writing, you are too familiar with the text, and you will read what you meant to write rather than what is actually on the page. Waiting helps you see the text objectively."
        }
    ]
}

lesson_8 = {
    "lesson_id": "strat_08",
    "title": "How to Use AI Feedback Effectively",
    "strategy_problem": "Students treat AI tools (like ChatGPT) as absolute truth, blindly accepting all suggested changes without understanding *why*. This leads to essays that sound robotic, use overly complex vocabulary incorrectly, and don't actually reflect the student's true ability in the exam.",
    "core_framework": [
        "1. Prompt for Specificity, Not Just 'Fix This': Don't just say 'Correct my essay'. Say: 'Act as an IELTS examiner. Highlight my grammar mistakes but keep my original vocabulary level. Explain why the grammar is wrong.'",
        "2. The 'Reverse Engineering' Technique: When AI rewrites a sentence, do not just copy it. Compare it side-by-side with your original. Identify the exact grammatical structure or collocation the AI used that makes it better.",
        "3. Beware the 'Band 9' Hallucination: AI naturally writes in a highly academic, complex style that is often unnatural for spoken English and too dense for a realistic 40-minute essay. Downgrade AI vocabulary if you cannot naturally use it in a sentence yourself.",
        "4. Fact-Check with Dictionaries: If an AI suggests a new word, always check its usage and collocations in the Cambridge or Oxford dictionary before using it."
    ],
    "ielts_scenario": "A student writes a Band 6 essay. They ask AI to 'rewrite this for Band 9'. The AI produces a dense, academic essay full of words like 'ubiquitous' and 'paradigm shift'. The student tries to memorize this essay, but in the real exam, they misuse these words, resulting in a lower score for Lexical Resource.",
    "do_dont_table": {
        "do": [
            "Use AI to identify specific grammar patterns you struggle with.",
            "Ask AI to provide *explanations* for its corrections.",
            "Verify new vocabulary suggestions in an official dictionary."
        ],
        "dont": [
            "Blindly copy/paste AI-rewritten essays.",
            "Try to memorize the highly complex, robotic vocabulary AI often generates.",
            "Assume AI grading is 100% accurate (it struggles with Task Response nuance)."
        ]
    },
    "example_application": "Instead of asking AI to rewrite your essay, provide your essay and ask: 'Identify the top 3 repeated grammar errors in this text and provide the rule for how to fix them.'",
    "personal_action_step": "Take a paragraph you recently wrote. Ask an AI tool to 'Correct the grammar but do NOT change my vocabulary.' Compare the result to your original.",
    "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A split screen showing a student's simple essay on the left and an AI's heavily edited, overly complex version on the right, with a caution symbol in the middle.",
    "quiz": [
        {
            "question": "Why is it dangerous to ask AI to simply 'Rewrite my essay for a Band 9'?",
            "options": {
                "A": "The AI will refuse to do it.",
                "B": "The AI will write an essay that is too short.",
                "C": "The AI often uses unnatural, overly dense vocabulary that students cannot replicate correctly under exam conditions.",
                "D": "The AI will intentionally give bad advice."
            },
            "correct_answer": "C",
            "explanation": "AI tends to produce highly sophisticated text that doesn't sound like a real candidate. If a student tries to mimic this without understanding the collocations, they will make unnatural errors."
        }
    ]
}

lesson_9 = {
    "lesson_id": "strat_09",
    "title": "Time Management Across the Four Skills",
    "strategy_problem": "Poor time management is the silent killer of IELTS scores. Students miss out on easy marks because they spend too long on difficult Reading questions, fail to finish Writing Task 2, or panic during the Listening test transfer time.",
    "core_framework": [
        "Reading: The 20-20-20 Myth: Do NOT spend 20 minutes on each passage. Passage 1 is easiest; aim for 15 minutes. Passage 2 needs 20 minutes. Passage 3 is hardest; leave 25 minutes. If a question takes more than 90 seconds, guess, mark it, and move on.",
        "Writing: The 40/20 Rule + Planning: Spend 20 mins on Task 1 and 40 mins on Task 2. Crucially, spend the first 5 minutes of Task 2 *planning*. Writing without a plan leads to mid-essay panic and deleting paragraphs, wasting massive amounts of time.",
        "Listening: Transfer Time Strategy: (Paper-based only) Do not transfer answers during the audio. Write on the question paper. Use the 10 minutes at the end to transfer carefully, checking spelling.",
        "Speaking: Part 2 Preparation: Use the 1-minute prep time effectively. Do not write full sentences. Write keywords, collocations, and the structure of your story."
    ],
    "ielts_scenario": "A student taking the Reading test encounters a very difficult 'True/False/Not Given' question in Passage 1. They spend 5 minutes agonizing over it. Because of this, they only have 10 minutes left for Passage 3, and they have to guess the last 10 answers, dropping their score from a potential 7.0 to a 6.0.",
    "do_dont_table": {
        "do": [
            "Strictly enforce time limits during practice (e.g., snatch the paper away at 60 mins).",
            "Spend 5 minutes planning Writing Task 2 before writing a single sentence.",
            "Allocate more time to Reading Passage 3."
        ],
        "dont": [
            "Spend more than 1.5 minutes on any single Reading question.",
            "Write full sentences during your Speaking Part 2 1-minute prep time.",
            "Start Writing Task 2 immediately without a clear outline."
        ]
    },
    "example_application": "During Reading practice, set a timer for 15 minutes for Passage 1. When the timer rings, force yourself to move to Passage 2, even if you haven't finished. This trains you to prioritize easy marks.",
    "personal_action_step": "For your next Writing Task 2 practice, set a timer for 5 minutes. You are only allowed to write an outline (intro thesis, main ideas for body paragraphs, conclusion). Do not start writing the essay until the timer rings.",
    "image_url": "https://images.unsplash.com/photo-1495364141860-b0d03eccd065?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A close-up of an analog stopwatch on a desk next to an IELTS Reading test booklet, symbolizing strict time management.",
    "quiz": [
        {
            "question": "What is the recommended time allocation strategy for the IELTS Reading test?",
            "options": {
                "A": "Exactly 20 minutes for each of the three passages.",
                "B": "30 minutes for Passage 1, 20 for Passage 2, and 10 for Passage 3.",
                "C": "15 minutes for Passage 1, 20 minutes for Passage 2, and 25 minutes for Passage 3.",
                "D": "Spend as much time as needed on Passage 1 to ensure a perfect score, then rush the rest."
            },
            "correct_answer": "C",
            "explanation": "Because the reading passages increase in difficulty, allocating more time to the final, hardest passage (and less to the easiest first passage) is the most effective strategy to maximize your score."
        }
    ]
}

os.makedirs("output", exist_ok=True)
with open("output/lesson_07.json", "w", encoding="utf-8") as f:
    json.dump(lesson_7, f, indent=2)
with open("output/lesson_08.json", "w", encoding="utf-8") as f:
    json.dump(lesson_8, f, indent=2)
with open("output/lesson_09.json", "w", encoding="utf-8") as f:
    json.dump(lesson_9, f, indent=2)

print("Generated lessons 7-9.")
