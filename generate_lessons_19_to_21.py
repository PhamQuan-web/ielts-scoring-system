import json

lesson_19 = {
    "lesson_id": "WF_19",
    "title": "Understanding Academic Task 1",
    "writing_skill_goal": "Learn the core requirements of Academic Task 1, including the word count, time limit, and overall structure.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "Task 1 requires you to summarise visual information in at least 150 words within 20 minutes. Structure: 1. Introduction. 2. Overview. 3. Detail Paragraph 1. 4. Detail Paragraph 2.",
    "weak_vs_improved": [
        {
            "weak_version": "This graph is about cars. I think it is interesting because my father has a car. In 2010, the line went up.",
            "improved_version": "The provided line graph illustrates the number of vehicles purchased in Europe between 2010 and 2020. Overall, there was a steady upward trend in car sales throughout the period.",
            "explanation": "The weak version includes personal opinion ('I think it is interesting') which is strictly forbidden in Task 1. The improved version objectively paraphrases the title and provides a clear overview."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Introduction (1 sentence)",
            "content": "Simply paraphrase the title of the chart or graph. Change words like 'shows' to 'illustrates' or 'compares', but do not change the core meaning."
        },
        {
            "step": "Overview (2 sentences)",
            "content": "Identify the 2 or 3 most significant main features (e.g., the highest point, the lowest point, or the general trend). Do not include any specific numbers or data in this paragraph."
        },
        {
            "step": "Detail Paragraphs (4-6 sentences total)",
            "content": "Group the specific data logically into two paragraphs. This is where you must cite specific numbers, dates, and percentages to support the main features you mentioned in the overview."
        }
    ],
    "common_mistakes": [
        "Giving your personal opinion or trying to explain *why* the data changed (e.g., 'Sales went up because the economy was good'). You must only report what you see.",
        "Listing every single number on the chart, making the essay read like a robot.",
        "Forgetting to write an Overview paragraph, which limits your Task Achievement score to a Band 5."
    ],
    "original_ielts_prompt": "The chart below shows the number of men and women studying engineering at Australian universities between 1992 and 2012. Summarise the information by selecting and reporting the main features, and make comparisons where relevant.",
    "model_micro_answer": "Introduction: The bar chart compares the gender distribution of engineering students in Australia over a 20-year period from 1992 to 2012.",
    "image_url": None,
    "image_prompt_fallback": "A magnifying glass looking closely at a line graph, with a red circle with a slash through it over a thought bubble showing personal opinion, indicating 'no opinions allowed'.",
    "quiz": [
        {
            "question": "What happens if you include a personal opinion or explanation in your Task 1 essay?",
            "options": {
                "A": "You show the examiner you are smart and get a Band 9.",
                "B": "You lose marks in Task Achievement because you are not following the instruction to simply 'summarise the information'.",
                "C": "It increases your word count, which is always good.",
                "D": "You get a higher score for Lexical Resource."
            },
            "correct_answer": "B",
            "explanation": "Task 1 is strictly a factual reporting task. If you interpret the data or give reasons for the trends that are not explicitly shown in the chart, you are not answering the prompt correctly."
        }
    ]
}

lesson_20 = {
    "lesson_id": "WF_20",
    "title": "How to Write a Strong Overview",
    "writing_skill_goal": "Master the Overview paragraph, the single most important part of an IELTS Task 1 essay for achieving a Band 7 or higher.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "An overview must start with the word 'Overall'. It should highlight 2 or 3 main trends, differences, or stages, without mentioning any specific data points (numbers, percentages).",
    "weak_vs_improved": [
        {
            "weak_version": "Overall, the highest number was 500 in 1990 and the lowest was 20 in 2000. Apples went up to 40%.",
            "improved_version": "Overall, it is clear that the consumption of apples experienced a significant increase over the period, while the figures for bananas and oranges saw a steady decline. Furthermore, apples consistently remained the most popular fruit.",
            "explanation": "The weak version lists specific data, which belongs in the detail paragraphs, not the overview. The improved version correctly identifies the broad trends (increase vs. decline) and the highest category overall."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Identify Trends (for over-time charts)",
            "content": "Look at the start and end of the lines/bars. Did the category go up, down, or fluctuate? Group similar categories together (e.g., 'A and B increased, while C decreased')."
        },
        {
            "step": "Identify Extremes (for static charts)",
            "content": "If there is no time period, look for the highest and lowest points, or the biggest differences between categories."
        },
        {
            "step": "Write 2 Clear Sentences",
            "content": "Start with 'Overall, it is clear that...'. Use the first sentence for your biggest observation, and the second sentence for your next biggest observation using a linker like 'Furthermore,' or 'In addition,'."
        }
    ],
    "common_mistakes": [
        "Including data points (numbers/percentages). If you include numbers, it is a detail paragraph, not an overview, and your score will drop.",
        "Putting the overview at the very end of the essay and running out of time to finish it.",
        "Starting the overview without a clear signpost word like 'Overall'."
    ],
    "original_ielts_prompt": "The graph below shows the percentage of households with different technology in the UK from 1995 to 2015.",
    "model_micro_answer": "Overall, it is evident that the ownership of mobile phones and internet connections grew dramatically over the twenty years. Conversely, the percentage of households with landline telephones experienced a noticeable decline.",
    "image_url": None,
    "image_prompt_fallback": "A bird's-eye view illustration of a person standing on a mountain looking down at a forest, representing looking at the 'big picture' overview rather than looking closely at individual trees (data details).",
    "quiz": [
        {
            "question": "Which of the following is a rule for writing an Overview paragraph?",
            "options": {
                "A": "It must include the exact numbers from the chart.",
                "B": "It must be at least 100 words long.",
                "C": "It must NOT include any specific numbers, percentages, or data points.",
                "D": "It must give your personal opinion on the chart."
            },
            "correct_answer": "C",
            "explanation": "The overview is meant to be a summary of the 'main features'. Specific data points belong exclusively in the subsequent detail paragraphs where you support the overview."
        }
    ]
}

lesson_21 = {
    "lesson_id": "WF_21",
    "title": "Line Graphs and Trend Language",
    "writing_skill_goal": "Learn the specific vocabulary and grammatical structures needed to describe upward, downward, and fluctuating trends accurately.",
    "band_descriptor_link": ["Lexical", "Grammar"],
    "core_writing_framework": "Use a mix of Verb + Adverb structures (e.g., 'increased dramatically') and Adjective + Noun structures (e.g., 'a dramatic increase') to demonstrate grammatical range.",
    "weak_vs_improved": [
        {
            "weak_version": "The number went up fast. Then it went down slow. Then it went up again.",
            "improved_version": "The figure experienced a sharp increase before declining gradually. Subsequently, it saw a significant recovery.",
            "explanation": "The weak version uses repetitive, basic vocabulary ('went up/down'). The improved version uses precise academic trend language ('sharp increase', 'declining gradually') and varied sentence structures."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Upward Trend Vocabulary",
            "content": "Verbs: rose, increased, climbed, surged, rocketed. Nouns: a rise, an increase, a surge."
        },
        {
            "step": "Downward Trend Vocabulary",
            "content": "Verbs: fell, decreased, dropped, declined, plummeted. Nouns: a fall, a decrease, a decline."
        },
        {
            "step": "Describing the Speed/Size (Adverbs & Adjectives)",
            "content": "Big changes: sharply, dramatically, significantly (sharp, dramatic, significant). Small changes: slightly, gradually, steadily (slight, gradual, steady)."
        },
        {
            "step": "Prepositions are Crucial",
            "content": "Increased 'to' = the final number. Increased 'by' = the difference. (e.g., 'Sales increased by 10% to 50%')."
        }
    ],
    "common_mistakes": [
        "Mixing up adjectives and adverbs (e.g., 'It increased sharp' instead of 'It increased sharply').",
        "Using extreme words like 'plummeted' or 'rocketed' for very small, gradual changes on the graph.",
        "Using the wrong prepositions, completely changing the factual meaning of the data."
    ],
    "original_ielts_prompt": "The line graph below shows the changes in the price of bread and milk in USD from 2000 to 2010.",
    "model_micro_answer": "In 2000, the price of milk stood at $2. Over the next five years, it experienced a steady rise, reaching $3.50 in 2005. Following this peak, the cost fell gradually to $3 by the end of the period.",
    "image_url": None,
    "image_prompt_fallback": "A chart showing a line rocketing upwards, with words like 'surge', 'plummet', and 'fluctuate' written next to different parts of the line graph.",
    "quiz": [
        {
            "question": "If a number changes from 20 to 50, which sentence uses prepositions correctly?",
            "options": {
                "A": "The number increased by 50.",
                "B": "The number increased to 30.",
                "C": "The number increased by 30 to reach 50.",
                "D": "The number increased at 50."
            },
            "correct_answer": "C",
            "explanation": "The preposition 'by' shows the amount of change (50 - 20 = 30). The preposition 'to' shows the final destination point (50)."
        }
    ]
}

with open("output/lesson_19.json", "w", encoding="utf-8") as f:
    json.dump(lesson_19, f, indent=2)

with open("output/lesson_20.json", "w", encoding="utf-8") as f:
    json.dump(lesson_20, f, indent=2)

with open("output/lesson_21.json", "w", encoding="utf-8") as f:
    json.dump(lesson_21, f, indent=2)

print("Created lesson_19.json, lesson_20.json, lesson_21.json")
