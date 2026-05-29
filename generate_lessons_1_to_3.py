import json

lesson_1 = {
    "lesson_id": "WF_01",
    "title": "Understanding IELTS Writing Criteria",
    "writing_skill_goal": "Understand the four assessment criteria used by IELTS examiners to score Writing Task 2.",
    "band_descriptor_link": ["Task Response", "Coherence", "Lexical", "Grammar"],
    "core_writing_framework": "Task Response (TR), Coherence and Cohesion (CC), Lexical Resource (LR), and Grammatical Range and Accuracy (GRA) each contribute 25% to your final writing band score.",
    "weak_vs_improved": [
        {
            "weak_version": "I think free education is good. It helps poor people. Poor people can go to university.",
            "improved_version": "Providing free education is highly beneficial because it ensures that individuals from low-income backgrounds have equal access to university studies.",
            "explanation": "The improved version demonstrates better Lexical Resource (vocabulary) and Grammatical Range (complex sentence structure) while logically connecting ideas (Coherence)."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Task Response (TR)",
            "content": "You must address all parts of the prompt, present a clear position throughout the essay, and support your main ideas with relevant examples."
        },
        {
            "step": "Coherence and Cohesion (CC)",
            "content": "Your essay must be organised into logical paragraphs. There should be a clear progression of ideas, and linking words should be used naturally to connect sentences."
        },
        {
            "step": "Lexical Resource (LR)",
            "content": "You need to use a wide range of vocabulary with precision. While it is good to use less common words, accuracy in collocations and context is more important than using 'big words'."
        },
        {
            "step": "Grammatical Range and Accuracy (GRA)",
            "content": "Use a mix of simple and complex sentence structures. To achieve a high band score, the majority of your sentences should be error-free, particularly regarding punctuation and verb tenses."
        }
    ],
    "common_mistakes": [
        "Failing to answer all parts of a two-part question (lowers Task Response).",
        "Overusing transition words like 'Furthermore' and 'Moreover' at the start of every sentence (lowers Coherence).",
        "Memorising and inserting complex words that do not fit the context (lowers Lexical Resource).",
        "Writing long, convoluted sentences that contain multiple grammatical errors (lowers Grammatical Accuracy)."
    ],
    "original_ielts_prompt": "Many people argue that the government should provide free healthcare for all citizens, while others believe that individuals should pay for their own medical treatment. Discuss both views and give your own opinion.",
    "model_micro_answer": "While some assert that citizens should be responsible for their own medical costs to reduce the tax burden, I firmly believe that governments must provide free healthcare to ensure the well-being and equality of all members of society.",
    "image_url": None,
    "image_prompt_fallback": "A well-lit, top-down view of an IELTS examiner's assessment sheet on a wooden desk, highlighting four columns labeled TR, CC, LR, and GRA, with a premium pen resting nearby.",
    "quiz": [
        {
            "question": "Which of the following directly impacts your Task Response score?",
            "options": {
                "A": "Using a wide variety of advanced vocabulary.",
                "B": "Writing without any grammatical mistakes.",
                "C": "Presenting a clear position and fully answering all parts of the prompt.",
                "D": "Using linking words effectively between paragraphs."
            },
            "correct_answer": "C",
            "explanation": "Task Response evaluates how well you address the prompt, including giving a clear position and supporting your arguments. Vocabulary, grammar, and linking words fall under LR, GRA, and CC respectively."
        }
    ]
}

lesson_2 = {
    "lesson_id": "WF_02",
    "title": "Task 2 Question Types",
    "writing_skill_goal": "Identify the five main types of IELTS Writing Task 2 essays and understand the specific requirements for each.",
    "band_descriptor_link": ["Task Response"],
    "core_writing_framework": "Recognise the five core essay types: Opinion (Agree/Disagree), Discussion (Discuss both views), Advantages & Disadvantages, Problem & Solution, and Two-Part Questions.",
    "weak_vs_improved": [
        {
            "weak_version": "In this essay, I will talk about why public transport is good and then why it is bad.",
            "improved_version": "This essay will explore the primary benefits of investing in public transport, followed by an analysis of its potential drawbacks.",
            "explanation": "The improved version clearly states the essay's purpose in an academic tone, showing exactly what type of essay (Advantages/Disadvantages) it is."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Opinion Essays (Agree / Disagree)",
            "content": "You are asked to give your clear opinion on a statement. You must decide whether you agree, disagree, or partially agree, and defend this stance throughout the essay."
        },
        {
            "step": "Discussion Essays (Discuss both views)",
            "content": "You must objectively discuss two opposing viewpoints provided in the prompt. Even if you agree with one side, you must give equal attention to explaining both sides before stating your opinion."
        },
        {
            "step": "Advantages and Disadvantages",
            "content": "The prompt asks you to evaluate the pros and cons of a specific situation or trend. Sometimes, it also asks if the advantages outweigh the disadvantages, requiring a clear overall judgment."
        },
        {
            "step": "Problem and Solution (or Causes and Effects)",
            "content": "You need to identify the reasons behind a specific problem and propose viable solutions. Structure your essay to address causes in one paragraph and solutions in the next."
        },
        {
            "step": "Two-Part Questions (Direct Questions)",
            "content": "The prompt contains two distinct questions (e.g., 'Why is this happening? Is it a positive or negative development?'). You must answer both questions fully, usually dedicating one body paragraph to each."
        }
    ],
    "common_mistakes": [
        "Giving only one side in a 'Discuss both views' essay.",
        "Forgetting to include your own opinion when the prompt specifically asks for it.",
        "Answering only one part of a 'Two-Part Question' prompt.",
        "Listing too many ideas without developing any of them fully."
    ],
    "original_ielts_prompt": "Due to the increasing shift towards remote work, many city centres are becoming empty. Why is this happening? Do you think this is a positive or a negative development?",
    "model_micro_answer": "This phenomenon is primarily caused by technological advancements that allow professionals to work from anywhere. In my view, this is a positive development because it reduces traffic congestion and lowers living costs for workers.",
    "image_url": None,
    "image_prompt_fallback": "An infographic style illustration showing five different pathways or signposts, each representing a different essay type like Opinion, Discussion, and Problem/Solution, in an academic setting.",
    "quiz": [
        {
            "question": "If a prompt asks 'Discuss both these views and give your own opinion', what MUST you include in your essay?",
            "options": {
                "A": "Arguments for one side only, along with your opinion.",
                "B": "An analysis of both viewpoints and a clear statement of your own opinion.",
                "C": "Only a list of advantages and disadvantages.",
                "D": "The causes of the situation and how to solve it."
            },
            "correct_answer": "B",
            "explanation": "In a 'Discuss both views and give your opinion' essay, the Task Response criteria mandates that you explore both sides of the argument and also explicitly state your own position."
        }
    ]
}

lesson_3 = {
    "lesson_id": "WF_03",
    "title": "How to Analyse a Task 2 Question",
    "writing_skill_goal": "Learn how to deconstruct an IELTS Writing Task 2 prompt to identify the topic, focus, and exact instruction.",
    "band_descriptor_link": ["Task Response", "Lexical"],
    "core_writing_framework": "Use the T.F.I. method: Topic (the general subject), Focus (the specific angle), and Instruction (what you must do).",
    "weak_vs_improved": [
        {
            "weak_version": "Topic: Environment. Focus: Good. Instruction: Write essay.",
            "improved_version": "Topic: Global warming. Focus: Individual vs Government responsibility. Instruction: Discuss both views and give an opinion.",
            "explanation": "A precise analysis ensures you address the specific nuance of the prompt rather than writing a generic essay about the broad topic."
        }
    ],
    "step_by_step_build": [
        {
            "step": "Identify the Topic",
            "content": "Read the first sentence of the prompt to find the broad theme. For example, 'Many people believe that technology is making us less sociable.' The topic is 'Technology and Social Interaction'."
        },
        {
            "step": "Identify the Focus",
            "content": "Look closer to find the specific context or restriction. In the example, you cannot just write about technology in general; you must focus specifically on whether it makes humans 'less sociable' or not."
        },
        {
            "step": "Identify the Instruction Words",
            "content": "Find the action words that tell you the essay type. Examples include 'To what extent do you agree?', 'Discuss both views', or 'What are the causes?'. This dictates your entire essay structure."
        },
        {
            "step": "Underline Keywords and Brainstorm Synonyms",
            "content": "Identify the most important words in the prompt. Before writing, think of 2-3 synonyms for these words to avoid repeating the prompt's exact vocabulary in your introduction (which demonstrates better Lexical Resource)."
        }
    ],
    "common_mistakes": [
        "Writing a generic essay about the broad topic instead of answering the specific focus (e.g., writing about all 'education' instead of specifically 'university funding').",
        "Missing the instruction entirely and writing an opinion essay when asked for a problem/solution essay.",
        "Failing to brainstorm synonyms, resulting in copying the prompt word-for-word in the introduction.",
        "Rushing into writing without taking 2-3 minutes to properly analyse the prompt."
    ],
    "original_ielts_prompt": "In recent years, the average lifespan of people in many countries has increased significantly. What are the main causes of this phenomenon? Are the effects on society mostly positive or negative?",
    "model_micro_answer": "Topic: Increased life expectancy. Focus: Causes and societal impacts. Instruction: Two-part question asking for causes and an evaluation of whether it is positive or negative.",
    "image_url": None,
    "image_prompt_fallback": "A close-up of a printed IELTS exam paper being highlighted with a bright yellow marker. Specific keywords like 'causes', 'effects', and 'agree' are circled in red ink by a student.",
    "quiz": [
        {
            "question": "What is the primary danger of failing to identify the 'Focus' of a prompt?",
            "options": {
                "A": "You might use the wrong grammar tenses.",
                "B": "You might write a generic essay that is off-topic, severely lowering your Task Response score.",
                "C": "You will write too many words.",
                "D": "You might misspell important vocabulary words."
            },
            "correct_answer": "B",
            "explanation": "If you only identify the broad topic and miss the specific focus, your essay will be off-topic. This means you have not answered the actual question asked, which limits your Task Response score to a maximum of Band 5."
        }
    ]
}

with open("output/lesson_01.json", "w", encoding="utf-8") as f:
    json.dump(lesson_1, f, indent=2)

with open("output/lesson_02.json", "w", encoding="utf-8") as f:
    json.dump(lesson_2, f, indent=2)

with open("output/lesson_03.json", "w", encoding="utf-8") as f:
    json.dump(lesson_3, f, indent=2)

print("Created lesson_01.json, lesson_02.json, lesson_03.json")
