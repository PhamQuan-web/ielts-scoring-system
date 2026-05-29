import json
import os

lesson_16 = {
    "lesson_id": "strat_16",
    "title": "How to Review a Mock Test Properly",
    "strategy_problem": "Students often treat taking a mock test as the 'study' itself. They finish a test, check the answer key, calculate their band score, feel happy or sad, and move on. This guarantees they will make the exact same mistakes on the next test.",
    "core_framework": [
        "1. The 'Blind Retry' (Reading/Listening): When you check your answers, do not look at the correct answer. Only mark *which* questions you got wrong. Then, try to answer those specific questions again without time pressure. If you get it right the second time, your issue is time management or careless reading. If you still get it wrong, it's a vocabulary or comprehension issue.",
        "2. The Transcript Deep-Dive (Listening): For questions you got wrong, go to the transcript at the back of the book. Highlight the exact sentence where the answer was. Why did you miss it? Was it a synonym you didn't know? Was it spoken too fast? Was it a distractor?",
        "3. The 'Post-Mortem' (Writing): Don't just read the tutor's feedback. Rewrite the essay incorporating the feedback. A 6.0 essay rewritten to a 7.0 standard is infinitely more valuable than writing ten new 6.0 essays.",
        "4. Categorizing Errors: In Reading, track *types* of errors. Do you always fail 'True/False/Not Given'? Do you struggle with 'Matching Headings'? Focus your next week's study solely on that question type."
    ],
    "ielts_scenario": "A student gets 30/40 on a Reading test. Instead of immediately doing another test, they spend 2 hours reviewing the 10 wrong answers. They discover they missed 4 questions specifically because they assumed 'Not Given' meant 'False'. By correcting this single misunderstanding, their score jumps to 34/40 on the next test.",
    "do_dont_table": {
        "do": [
            "Spend at least 1 hour reviewing a 1-hour Reading or Listening test.",
            "Use the 'Blind Retry' method before looking at the correct answers.",
            "Analyze the listening transcripts to understand *how* the test tricked you."
        ],
        "dont": [
            "Just calculate your score and throw the test away.",
            "Look at the answer key immediately and say 'Oh yeah, I knew that.'",
            "Keep taking full mock tests every day without reviewing them."
        ]
    },
    "example_application": "You miss a Listening question about the location of a library. You check the transcript and realize the speaker said, 'It's adjacent to the bank.' You didn't know 'adjacent to' meant 'next to'. You add 'adjacent to' to your vocabulary notebook.",
    "personal_action_step": "Take the last Reading or Listening test you completed. Find 3 questions you got wrong. For each one, write down one sentence explaining exactly *why* you got it wrong (e.g., 'I didn't know the synonym for X', 'I misread the question', 'I fell for the distractor').",
    "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "image_prompt_fallback": "A student carefully reviewing an IELTS exam paper with a highlighter and a notebook, comparing the test questions to the transcript.",
    "quiz": [
        {
            "question": "What is the 'Blind Retry' method in reviewing a mock test?",
            "options": {
                "A": "Taking the test with your eyes closed to improve listening focus.",
                "B": "Guessing the answers without reading the passage.",
                "C": "Marking which questions are incorrect, but trying to solve them again without looking at the correct answer key.",
                "D": "Refusing to look at your score until the real exam."
            },
            "correct_answer": "C",
            "explanation": "The 'Blind Retry' helps diagnose whether your error was caused by time pressure (you get it right the second time) or a genuine lack of comprehension (you get it wrong again), guiding how you should study to fix it."
        }
    ]
}

os.makedirs("output", exist_ok=True)
with open("output/lesson_16.json", "w", encoding="utf-8") as f:
    json.dump(lesson_16, f, indent=2)

print("Generated lesson 16.")
