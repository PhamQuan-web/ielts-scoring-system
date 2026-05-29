import json

lesson_data = {
  "lesson_id": "foundations_01",
  "title": "Understanding IELTS Speaking Criteria",
  "speaking_skill_goal": "Part 1, 2, or 3",
  "answer_framework": "Before you begin studying specific techniques, it is absolutely essential to understand exactly how the examiner will grade your performance. The IELTS Speaking test is assessed across four equally weighted criteria (25% each):\n\n1. Fluency and Coherence (FC): This measures your ability to speak at length without noticeable effort or loss of coherence. It involves speaking at a natural speed, avoiding long hesitations to search for words or grammar, and using cohesive devices (linking words) logically to connect your ideas.\n\n2. Lexical Resource (LR): This assesses your vocabulary. Examiners look for a wide range of vocabulary used accurately and appropriately. To score higher (Band 7+), you need to demonstrate the ability to use less common and idiomatic vocabulary, paraphrase effectively, and show awareness of style and collocation.\n\n3. Grammatical Range and Accuracy (GRA): This evaluates your ability to use a variety of grammatical structures correctly. It's not just about avoiding mistakes; it's about showing you can use complex sentences (e.g., conditionals, relative clauses, passive voice) naturally. Frequent errors in basic grammar will limit your score to a Band 5 or 6.\n\n4. Pronunciation (PRON): This isn't about having a 'British' or 'American' accent. It's about how easily the examiner can understand you. Key features include word stress (emphasising the correct syllable), sentence stress (highlighting important words), intonation (the rise and fall of your voice), and clearly pronouncing individual sounds.",
  "useful_phrase_bank": [
    "To begin with, ... (Useful for Coherence)",
    "In terms of ... (Useful for Coherence)",
    "On the one hand, ... on the other hand ... (Useful for Coherence and GRA)",
    "Moving on to ... (Useful for Coherence)"
  ],
  "weak_vs_better": [
    {
      "weak_answer": "I like reading. Reading is good. I read books. (Repetitive vocabulary, short simple sentences, poor fluency).",
      "better_answer": "I'm quite fond of reading, particularly historical fiction, as it allows me to unwind and escape from my daily routine. (Demonstrates less common vocabulary like 'unwind', complex sentence structure with 'as', and smooth delivery)."
    }
  ],
  "fluency_pronunciation_note": "A common misconception among students is that speaking extremely fast equals high fluency. In reality, true fluency is about maintaining a steady, natural rhythm, pausing appropriately between ideas (chunking), and expressing your thoughts clearly without excessive self-correction or hesitating to search for the right word.",
  "sample_ielts_question": "Do you enjoy reading?",
  "model_short_answer": "Yes, absolutely. I'm quite an avid reader. Whenever I have some free time, I usually delve into a good novel, as it helps me relax and expand my imagination.",
  "common_mistakes": [
    "Focusing too intensely on perfect grammar and losing natural fluency as a result.",
    "Forcing 'big, complicated words' into sentences incorrectly instead of using natural collocations.",
    "Speaking too quickly to sound 'fluent', which actually damages pronunciation clarity and intonation.",
    "Giving memorised answers, which the examiner will spot immediately due to unnatural intonation."
  ],
  "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/IELTS_logo.svg/1200px-IELTS_logo.svg.png",
  "image_prompt_fallback": "A well-lit, professional classroom setting showing an examiner with a clipboard and a candidate engaged in an IELTS speaking test, highlighting communication, assessment, and criteria.",
  "quiz": [
     {
      "question": "Which of the following best describes the 'Lexical Resource' criterion?",
      "options": {
        "A": "Speaking smoothly without stopping or hesitating.",
        "B": "Using a wide range of vocabulary accurately and appropriately.",
        "C": "Pronouncing words clearly without any accent.",
        "D": "Using complicated grammar tenses without making any mistakes."
      },
      "correct_answer": "B",
      "explanation": "Lexical Resource refers specifically to your vocabulary range, accuracy, and your ability to use idiomatic language and collocations naturally. Option A is Fluency, Option C is Pronunciation, and Option D is Grammatical Range and Accuracy."
    }
  ]
}

with open("output/lesson_01.json", "w", encoding="utf-8") as f:
    json.dump(lesson_data, f, indent=2, ensure_ascii=False)
