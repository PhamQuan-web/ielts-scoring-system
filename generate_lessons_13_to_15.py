import json

lesson_13 = {
    "lesson_id": "WF_13",
    "title": "Agree or Disagree Essays",
    "writing_skill_goal": "Learn how to structure and write an opinion essay by clearly taking a side and supporting it with strong arguments.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "Structure: 1. Introduction (Paraphrase + Clear Opinion). 2. Body Paragraph 1 (Reason 1 for opinion). 3. Body Paragraph 2 (Reason 2 for opinion). 4. Conclusion (Summarise and restate opinion).",
    "weak_vs_improved": [
        {
            "weak_version": "I agree with this a little bit, but I also disagree. There are good things and bad things.",
            "improved_version": "I completely agree with the assertion that university education should be free, as it promotes social equality and ensures a highly educated workforce.",
            "explanation": "The weak version is vague and fails to establish a clear position, which limits the Task Response score. The improved version states a firm opinion ('completely agree') and outlines the reasons."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Choose Your Stance",
            "content": "You can completely agree, completely disagree, or partially agree. For most students, it is easiest to strongly pick one side (100% agree or 100% disagree) as it simplifies the essay structure."
        },
        {
            "step": "Draft the Thesis Statement",
            "content": "Your introduction must contain a sentence explicitly stating your opinion. For example: 'I completely disagree with this idea because...'"
        },
        {
            "step": "Develop Body Paragraphs",
            "content": "If you completely agree, Body Paragraph 1 should explain your first reason for agreeing. Body Paragraph 2 should explain your second reason for agreeing."
        }
    ],
    "common_mistakes": [
        "Sitting on the fence (not making a clear decision) so the examiner cannot find your opinion.",
        "Discussing the opposite side in detail when you have already stated you completely agree with the first side.",
        "Forgetting to include a conclusion."
    ],
    "original_ielts_prompt": "Big salary is much more important than job satisfaction. Do you agree or disagree?",
    "model_micro_answer": "I strongly disagree with the idea that a high salary is more important than job satisfaction. The primary reason is that spending the majority of one's life in a stressful or unfulfilling job inevitably leads to severe mental health issues, such as depression, regardless of financial wealth.",
    "image_url": None,
    "image_prompt_fallback": "A balanced scale heavily tipped to one side, representing a strong opinion, with the words 'Agree' and 'Disagree' on the weighing pans.",
    "quiz": [
        {
            "question": "If you decide to 'completely agree' with a prompt, what should Body Paragraph 2 contain?",
            "options": {
                "A": "Arguments for why people might disagree.",
                "B": "A summary of the introduction.",
                "C": "A second distinct reason explaining why you agree.",
                "D": "Your final conclusion."
            },
            "correct_answer": "C",
            "explanation": "If you completely agree, the entire essay must defend that position. BP1 gives reason one, and BP2 gives reason two. You do not need to discuss the opposing view."
        }
    ]
}

lesson_14 = {
    "lesson_id": "WF_14",
    "title": "Discussion Essays",
    "writing_skill_goal": "Learn how to objectively analyze two opposing views before giving your own opinion.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "Structure: 1. Introduction (Paraphrase both views + state your opinion). 2. Body Paragraph 1 (Discuss View 1). 3. Body Paragraph 2 (Discuss View 2). 4. Conclusion (Summarise and restate opinion).",
    "weak_vs_improved": [
        {
            "weak_version": "I think students should wear uniforms because it is cheaper. Also, it looks nice.",
            "improved_version": "On the one hand, some argue that school uniforms suppress individuality. On the other hand, many believe they foster equality among students. I agree with the latter view because uniforms significantly reduce peer pressure related to fashion.",
            "explanation": "The weak version ignores the requirement to 'discuss both views' and jumps straight to an opinion. The improved version correctly addresses both sides before establishing a personal stance."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Acknowledge Both Sides",
            "content": "You must dedicate one full body paragraph to explaining why some people hold the first view, and another full body paragraph to explaining why others hold the second view."
        },
        {
            "step": "Use Objective Language",
            "content": "When discussing the side you don't agree with, use third-person language: 'Supporters of this view argue that...' or 'It is often believed that...'."
        },
        {
            "step": "Give Your Opinion",
            "content": "The prompt asks you to 'give your own opinion'. You can do this in the introduction, briefly at the end of the body paragraphs, and definitively in the conclusion."
        }
    ],
    "common_mistakes": [
        "Only writing about the view you agree with.",
        "Writing a third body paragraph for your opinion (this usually leads to running out of time). It is better to integrate your opinion into the introduction and conclusion, or side with one of the body paragraphs.",
        "Confusing a 'Discuss both views' essay with an 'Advantages/Disadvantages' essay."
    ],
    "original_ielts_prompt": "Some people think that strict environmental regulations are the only way to save our planet. Others believe that technology will provide the solution. Discuss both these views and give your own opinion.",
    "model_micro_answer": "While many experts argue that technological innovations, such as carbon capture, will eventually solve the climate crisis, I align with those who believe strict government regulations are immediately necessary to halt current ecological damage.",
    "image_url": None,
    "image_prompt_fallback": "An illustration of two people talking across a table, with speech bubbles representing opposing views, and a third person (the writer) standing in the middle holding a clipboard with an opinion.",
    "quiz": [
        {
            "question": "In a 'Discuss both views' essay, how should you write the body paragraph about the view you DISAGREE with?",
            "options": {
                "A": "You shouldn't write it. Only write about what you agree with.",
                "B": "Write about it using objective language (e.g., 'Some people argue that...') to explain their perspective fairly.",
                "C": "Write about it and aggressively insult the people who believe it.",
                "D": "Only write one sentence about it."
            },
            "correct_answer": "B",
            "explanation": "The task requires you to discuss both views objectively. You must explain the logic behind the opposing view, even if you ultimately conclude that it is incorrect."
        }
    ]
}

lesson_15 = {
    "lesson_id": "WF_15",
    "title": "Advantages and Disadvantages Essays",
    "writing_skill_goal": "Learn how to evaluate the positive and negative aspects of a trend, and how to conclude if the benefits outweigh the drawbacks.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "Structure: 1. Introduction (Paraphrase topic + Thesis). 2. Body Paragraph 1 (Advantages). 3. Body Paragraph 2 (Disadvantages). 4. Conclusion (Summarise and final judgement).",
    "weak_vs_improved": [
        {
            "weak_version": "Computers are good. They are fast. But they are also bad. They hurt your eyes.",
            "improved_version": "Although the reliance on computers can lead to sedentary lifestyles and vision problems, the advantages of unparalleled processing speed and global connectivity far outweigh these health concerns.",
            "explanation": "The improved version clearly weighs the two sides against each other and explicitly states which side is stronger ('far outweigh'), fully addressing the prompt."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Identify the Type",
            "content": "Check if the prompt just asks 'What are the advantages and disadvantages?' OR if it asks 'Do the advantages outweigh the disadvantages?'. The second type requires you to give a clear opinion/judgement."
        },
        {
            "step": "Structure the Body",
            "content": "Dedicate Body Paragraph 1 entirely to the advantages. Dedicate Body Paragraph 2 entirely to the disadvantages. Do not mix them in the same paragraph."
        },
        {
            "step": "The 'Outweigh' Judgement",
            "content": "If asked whether one outweighs the other, make sure your thesis statement in the introduction and your conclusion clearly state your decision (e.g., 'I believe the drawbacks significantly outweigh the benefits')."
        }
    ],
    "common_mistakes": [
        "Failing to explicitly state which side outweighs the other when the prompt asks for it.",
        "Listing 5 advantages but not explaining any of them (it is better to have 2 well-explained advantages).",
        "Writing a generic conclusion without a final judgement."
    ],
    "original_ielts_prompt": "In many countries, more and more people are choosing to buy goods online rather than in physical stores. Do the advantages of this development outweigh the disadvantages?",
    "model_micro_answer": "The primary disadvantage of e-commerce is the decline of local businesses and traditional high streets. However, this is heavily outweighed by the convenience and cost-effectiveness that online shopping provides to the average consumer.",
    "image_url": None,
    "image_prompt_fallback": "A balancing scale with a heavy weight labeled 'Advantages' pulling down one side, lifting a smaller weight labeled 'Disadvantages' high in the air.",
    "quiz": [
        {
            "question": "If the prompt asks 'Do the advantages outweigh the disadvantages?', what MUST you include in your introduction?",
            "options": {
                "A": "A list of every advantage and disadvantage.",
                "B": "A clear statement indicating whether you think the advantages are stronger, or the disadvantages are stronger.",
                "C": "A definition of the word 'advantage'.",
                "D": "A question asking the examiner what they think."
            },
            "correct_answer": "B",
            "explanation": "This specific prompt type is asking for your judgement. If you do not explicitly state which side is stronger in your introduction (and conclusion), you have not fully answered the question."
        }
    ]
}

with open("output/lesson_13.json", "w", encoding="utf-8") as f:
    json.dump(lesson_13, f, indent=2)

with open("output/lesson_14.json", "w", encoding="utf-8") as f:
    json.dump(lesson_14, f, indent=2)

with open("output/lesson_15.json", "w", encoding="utf-8") as f:
    json.dump(lesson_15, f, indent=2)

print("Created lesson_13.json, lesson_14.json, lesson_15.json")
