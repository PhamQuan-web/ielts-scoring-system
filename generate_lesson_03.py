import json

lesson_data = {
  "lesson_id": "foundations_03",
  "title": "Extending Part 1 Answers Naturally",
  "speaking_skill_goal": "Part 1",
  "answer_framework": "If you struggle to think of reasons or examples to hit that 3-4 sentence sweet spot in Part 1, you can extend your answer by using these advanced, yet natural, techniques:\n\n1. Contrast (Past vs. Present): Compare what you do now with what you used to do. Example: 'I used to take the bus, but nowadays I prefer riding my motorbike.'\n\n2. Concession (Admitting a downside or exception): Show that things aren't always black and white. Example: 'I love living in the city, although the pollution can be quite annoying sometimes.'\n\n3. Frequency/Dependence: Explain that your answer changes depending on the situation. Example: 'It really depends on my mood. If I'm tired, I stay in, but if I feel energetic, I go out.'\n\nThese techniques are excellent because they not only add length but also automatically force you to use a wider range of complex grammatical structures (like conditionals and contrasting clauses).",
  "useful_phrase_bank": [
    "It really depends on ... (Dependence)",
    "I used to ..., but nowadays I tend to ... (Past vs Present)",
    "When I was younger I would ..., whereas now I ... (Past vs Present)",
    "Although it's a bit ..., I still ... (Concession)",
    "I'm a big fan of it, even though ... (Concession)"
  ],
  "weak_vs_better": [
    {
      "weak_answer": "I play football on Sundays.",
      "better_answer": "Well, it really depends on the weather. If it's sunny and dry, I usually play football with my friends at the local park. But on rainy days, I tend to just stay indoors and watch matches on TV instead."
    }
  ],
  "fluency_pronunciation_note": "When using contrast words like 'but', 'although', or 'whereas', try placing a slight stress on them to highlight the shift in your idea. This natural intonation improves both your fluency score and your pronunciation score.",
  "sample_ielts_question": "Do you often use public transport?",
  "model_short_answer": "To be honest, it depends entirely on where I'm going. I used to take the bus every day when I was commuting to university, but nowadays I prefer riding my motorbike because it's much more convenient for navigating heavy traffic in my city.",
  "common_mistakes": [
    "Listing too many unrelated points (e.g., 'I like buses, trains, and taxis') instead of expanding deeply on just one idea.",
    "Relying on the word 'because' in every single answer instead of mixing it up with contrast or dependence structures.",
    "Trailing off and leaving sentences unfinished when you run out of ideas."
  ],
  "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
  "image_prompt_fallback": "A split image showing a busy city bus stop on one side and someone riding a modern scooter on the other, illustrating different transportation choices and contrasts.",
  "quiz": [
     {
      "question": "Which of the following is a 'Concession' technique?",
      "options": {
        "A": "I like swimming because it keeps me fit.",
        "B": "I used to hate swimming, but now I like it.",
        "C": "I enjoy swimming in the ocean, although the cold water can be a bit of a shock at first.",
        "D": "If I have time, I will go swimming."
      },
      "correct_answer": "C",
      "explanation": "Option C uses 'although' to admit a downside (cold water) while still maintaining the main positive point (enjoying swimming). This is a classic concession structure. Option B is Past vs Present."
    }
  ]
}

with open("output/lesson_03.json", "w", encoding="utf-8") as f:
    json.dump(lesson_data, f, indent=2, ensure_ascii=False)
