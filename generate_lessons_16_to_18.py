import json

lesson_16 = {
    "lesson_id": "WF_16",
    "title": "Problem and Solution Essays",
    "writing_skill_goal": "Learn how to systematically identify the causes of a problem and propose realistic, logically linked solutions.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "Structure: 1. Introduction (Paraphrase issue + outline). 2. Body Paragraph 1 (Causes/Problems). 3. Body Paragraph 2 (Solutions). 4. Conclusion (Summarise causes and solutions).",
    "weak_vs_improved": [
        {
            "weak_version": "Traffic is bad. A reason is cars. Another reason is roads. A solution is flying cars. Also, we should walk.",
            "improved_version": "The primary cause of traffic congestion is the over-reliance on private vehicles combined with inadequate public infrastructure. To mitigate this issue, governments must invest heavily in expanding and subsidising public transport networks.",
            "explanation": "The weak version lists unrelated, unrealistic ideas. The improved version directly links a realistic cause (over-reliance on cars) to a realistic, practical solution (subsidising public transport)."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Identify the Exact Problem",
            "content": "Ensure you are answering the specific problem in the prompt, not a general topic. If the prompt is about 'childhood obesity', do not write about 'general health'."
        },
        {
            "step": "Link Causes to Solutions",
            "content": "Your Body Paragraph 2 (Solutions) MUST directly fix the problems you mentioned in Body Paragraph 1 (Causes). Do not propose a solution to a problem you haven't discussed."
        },
        {
            "step": "Use Solution Vocabulary",
            "content": "Use language that suggests action and remedy: 'To tackle this issue...', 'A viable solution would be to...', 'Governments ought to implement...'."
        }
    ],
    "common_mistakes": [
        "Suggesting unrealistic or 'magic' solutions (e.g., 'The government should just ban all cars').",
        "Writing a solution that has nothing to do with the cause mentioned earlier.",
        "Failing to explain *how* the solution will actually fix the problem."
    ],
    "original_ielts_prompt": "In many cities, the cost of housing is highly expensive. What are the causes of this? What solutions can you suggest?",
    "model_micro_answer": "A significant factor driving up housing costs is the rapid influx of rural populations into urban centres, creating a demand that vastly outpaces supply. To resolve this, governments should focus on decentralisation, investing in infrastructure and job creation in rural areas to reduce urban migration.",
    "image_url": None,
    "image_prompt_fallback": "A split image: the left side shows a tangled, messy knot (the problem), and the right side shows a pair of hands neatly untangling it (the solution).",
    "quiz": [
        {
            "question": "What is the most important relationship between your 'Causes' paragraph and your 'Solutions' paragraph?",
            "options": {
                "A": "They should have exactly the same number of words.",
                "B": "The solutions you propose must directly address and attempt to fix the specific causes you just wrote about.",
                "C": "The solutions should be completely unrelated to the causes to show you have many ideas.",
                "D": "You should write about the solutions first, then the causes."
            },
            "correct_answer": "B",
            "explanation": "For a high Coherence and Task Response score, your essay must be logically linked. Proposing a solution (like 'build more schools') for a cause you never mentioned (like 'lack of education') confuses the reader."
        }
    ]
}

lesson_17 = {
    "lesson_id": "WF_17",
    "title": "Two-Part Question Essays",
    "writing_skill_goal": "Master the structure for Direct Question essays by ensuring both questions are answered equally and fully.",
    "band_descriptor_link": ["Task Response", "Coherence"],
    "core_writing_framework": "Structure: 1. Introduction (Paraphrase + address both questions). 2. Body Paragraph 1 (Answer Question 1). 3. Body Paragraph 2 (Answer Question 2). 4. Conclusion (Summarise both answers).",
    "weak_vs_improved": [
        {
            "weak_version": "Prompt: Why is art important? Should government fund it? Answer: Art is very important for culture. (Spends 250 words on why art is important, ignores the funding question).",
            "improved_version": "Art plays a crucial role in preserving a nation's cultural heritage. Consequently, I firmly believe that governments have a responsibility to subsidise artistic institutions.",
            "explanation": "The weak version fails the Task Response criteria completely by ignoring half of the prompt. The improved version directly answers both the 'why' and the 'should they fund it' questions."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Identify the Two Questions",
            "content": "These prompts literally have two question marks. For example: 'Why do people do this? Is it a positive or negative trend?'."
        },
        {
            "step": "Divide Your Body Paragraphs",
            "content": "The simplest and most effective structure is to use Body Paragraph 1 entirely to answer the first question, and Body Paragraph 2 entirely to answer the second question."
        },
        {
            "step": "Address Both in the Introduction",
            "content": "Your thesis statement MUST touch on both questions. Do not leave the examiner guessing what your answer to the second question will be."
        }
    ],
    "common_mistakes": [
        "Focusing 80% of the essay on the first question and only 20% on the second question.",
        "Forgetting to answer the second question entirely.",
        "Mixing the answers to both questions randomly throughout all paragraphs."
    ],
    "original_ielts_prompt": "Many people choose to work in foreign countries. Why do they do this? What problems might they face when working abroad?",
    "model_micro_answer": "Professionals often migrate overseas in search of better career prospects and higher salaries. However, upon arrival, they frequently encounter significant challenges, most notably language barriers and cultural isolation.",
    "image_url": None,
    "image_prompt_fallback": "A road sign splitting into two equal paths. One path is labeled 'Question 1: Why?', and the other path is labeled 'Question 2: What problems?'.",
    "quiz": [
        {
            "question": "If an IELTS prompt contains two distinct questions, how should you structure your body paragraphs?",
            "options": {
                "A": "Write three body paragraphs just in case.",
                "B": "Answer Question 1 in the Introduction, and Question 2 in the Conclusion.",
                "C": "Dedicate Body Paragraph 1 to answering the first question, and Body Paragraph 2 to answering the second question.",
                "D": "Mix the answers to both questions in one single, large paragraph."
            },
            "correct_answer": "C",
            "explanation": "Dedicating one body paragraph to each question is the safest and most logical way to ensure you fully and equally address both parts of the prompt, maximizing your Task Response and Coherence scores."
        }
    ]
}

lesson_18 = {
    "lesson_id": "WF_18",
    "title": "Counterarguments and Balanced Opinions",
    "writing_skill_goal": "Learn advanced paragraph structuring by acknowledging the opposing view before successfully refuting it (Concession).",
    "band_descriptor_link": ["Task Response", "Lexical", "Coherence"],
    "core_writing_framework": "A counterargument acknowledges the other side ('While it is true that...'), but immediately follows with a stronger point supporting your own side ('...nevertheless, the benefits are far greater because...').",
    "weak_vs_improved": [
        {
            "weak_version": "Some people think zoos are bad. I think zoos are good. They protect animals.",
            "improved_version": "While opponents argue that keeping animals in captivity is unethical, it is important to recognise that modern zoos play a vital role in the conservation of endangered species.",
            "explanation": "The weak version is basic and disconnected. The improved version uses a concession structure ('While X, it is important to recognise Y') to acknowledge the opposing view while strengthening the writer's main argument."
        }
    ],
    "step_by_step_build": [
        {
            "step": "When to Use a Counterargument",
            "content": "This technique is best used in 'To what extent do you agree or disagree?' essays when you want to show the examiner you have a deep, nuanced understanding of the topic."
        },
        {
            "step": "The Concession Clause",
            "content": "Start the sentence by acknowledging the opposing view using words like 'While', 'Although', 'Admittedly', or 'It is true that'."
        },
        {
            "step": "The Refutation",
            "content": "In the second half of the sentence, introduce your stronger argument to show why the opposing view is flawed or less important. Use words like 'however' or 'nevertheless'."
        }
    ],
    "common_mistakes": [
        "Writing a counterargument but forgetting to refute it, making it seem like you accidentally agreed with the other side.",
        "Using this technique in a basic way that confuses the reader about what your actual opinion is.",
        "Using informal language like 'But they are wrong because...'."
    ],
    "original_ielts_prompt": "Some people think that violent sports such as boxing should be banned. To what extent do you agree or disagree?",
    "model_micro_answer": "Admittedly, combat sports carry a high risk of physical injury to the athletes involved. Nevertheless, banning them entirely would simply drive these activities underground where they would be unregulated, ultimately putting fighters in even greater danger.",
    "image_url": None,
    "image_prompt_fallback": "A fencing match where one fencer (the opposing view) makes a weak thrust, and the other fencer (the writer's argument) smoothly deflects it and lands a stronger counter-attack.",
    "quiz": [
        {
            "question": "What is the crucial second step of a counterargument after you have acknowledged the opposing view?",
            "options": {
                "A": "You must agree with it and change your essay's opinion.",
                "B": "You must refute it by presenting a stronger argument for your own side.",
                "C": "You must write a whole new paragraph explaining why the opposing view is brilliant.",
                "D": "You must stop writing."
            },
            "correct_answer": "B",
            "explanation": "A counterargument is only effective if you 'refute' it. You acknowledge the opposing side exists, but then you explain why your side is still better. If you don't refute it, you have just argued against yourself."
        }
    ]
}

with open("output/lesson_16.json", "w", encoding="utf-8") as f:
    json.dump(lesson_16, f, indent=2)

with open("output/lesson_17.json", "w", encoding="utf-8") as f:
    json.dump(lesson_17, f, indent=2)

with open("output/lesson_18.json", "w", encoding="utf-8") as f:
    json.dump(lesson_18, f, indent=2)

print("Created lesson_16.json, lesson_17.json, lesson_18.json")
