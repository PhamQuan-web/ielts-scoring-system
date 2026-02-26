import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch05.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g6_439",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I ran a marathon last year. It was a test of endurance and willpower. I trained for months. The race was grueling. I hit the wall at mile 20. My legs felt like lead. However, the crowd cheered me on. I crossed the finish line exhausted but elated. It was a personal victory. I am proud of myself for finishing. It showed me that I am stronger than I thought.",
        "word_count": 69,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'test of endurance' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'marathon', 'test of endurance', 'willpower', 'grueling', 'hit the wall', 'lead', 'cheered', 'finish line', 'elated', 'personal victory'. >Band 6: 'Grueling', 'elated'. Not Band 8: 'Trained' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'cheered me on', 'exhausted but elated'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I ran a marathon last year. It was a test of endurance and willpower. I trained for months. The race was grueling. I hit the wall at mile 20. My legs felt like lead. However, the crowd cheered me on. I crossed the finish line exhausted but elated. It was a personal victory. I am proud of myself for finishing. It showed me that I am stronger than I thought.\n\nWord Count: 69 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'marathon', 'test of endurance', 'willpower', 'grueling', 'hit the wall', 'lead', 'cheered', 'finish line', 'elated', 'personal victory'. \n\n>Band 6: 'Grueling', 'elated'.\n\nNot Band 8: 'Trained' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'cheered me on', 'exhausted but elated'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_440",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Eiffel Tower in Paris. It is an iconic structure. The iron lattice work is intricate. We took the elevator to the top. The panoramic view of the city was breathtaking. It sparkled at night. It is a symbol of romance. Millions of tourists visit it annually. I was amazed by its height. It is a masterpiece of engineering. I took many photos to remember the moment.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'iron lattice work' (noun phrase). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'iconic', 'structure', 'lattice work', 'intricate', 'elevator', 'panoramic view', 'breathtaking', 'sparkled', 'symbol of romance', 'annually'. >Band 6: 'Iconic', 'breathtaking'. Not Band 8: 'Tourists' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'view... was breathtaking', 'visit it annually'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Eiffel Tower in Paris. It is an iconic structure. The iron lattice work is intricate. We took the elevator to the top. The panoramic view of the city was breathtaking. It sparkled at night. It is a symbol of romance. Millions of tourists visit it annually. I was amazed by its height. It is a masterpiece of engineering. I took many photos to remember the moment.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'iconic', 'structure', 'lattice work', 'intricate', 'elevator', 'panoramic view', 'breathtaking', 'sparkled', 'symbol of romance', 'annually'. \n\n>Band 6: 'Iconic', 'breathtaking'.\n\nNot Band 8: 'Tourists' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'view... was breathtaking', 'visit it annually'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_441",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I organized a family reunion last summer. Coordinating schedules was a nightmare. I booked a venue and arranged catering. I sent out invitations to everyone. There were disagreements about the menu. I acted as a mediator. In the end, everyone showed up. We reconnected and shared memories. It was stressful but worth it. I was happy to see everyone together. It was a special day for our family.",
        "word_count": 67,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'Coordinating schedules was' (gerund). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'reunion', 'coordinating', 'schedules', 'nightmare', 'venue', 'catering', 'invitations', 'disagreements', 'mediator', 'reconnected'. >Band 6: 'Mediator', 'coordinating'. Not Band 8: 'Menu' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'Coordinating... was', 'stressful but worth it'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I organized a family reunion last summer. Coordinating schedules was a nightmare. I booked a venue and arranged catering. I sent out invitations to everyone. There were disagreements about the menu. I acted as a mediator. In the end, everyone showed up. We reconnected and shared memories. It was stressful but worth it. I was happy to see everyone together. It was a special day for our family.\n\nWord Count: 67 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'reunion', 'coordinating', 'schedules', 'nightmare', 'venue', 'catering', 'invitations', 'disagreements', 'mediator', 'reconnected'. \n\n>Band 6: 'Mediator', 'coordinating'.\n\nNot Band 8: 'Menu' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'Coordinating... was', 'stressful but worth it'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_442",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read To Kill a Mockingbird. It deals with racial injustice. The story is told through a child's eyes. Atticus Finch is a moral compass. He defends an innocent man. The trial scene is gripping. It highlights the prejudice of society. It is a timeless classic. It made me think about fairness. I learned a lot from it. It is a very important book.",
        "word_count": 64,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'moral compass' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'racial injustice', 'moral compass', 'defends', 'innocent', 'trial', 'gripping', 'highlights', 'prejudice', 'timeless classic'. >Band 6: 'Prejudice', 'gripping'. Not Band 8: 'Society' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'told through', 'highlights the prejudice'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read To Kill a Mockingbird. It deals with racial injustice. The story is told through a child's eyes. Atticus Finch is a moral compass. He defends an innocent man. The trial scene is gripping. It highlights the prejudice of society. It is a timeless classic. It made me think about fairness. I learned a lot from it. It is a very important book.\n\nWord Count: 64 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'racial injustice', 'moral compass', 'defends', 'innocent', 'trial', 'gripping', 'highlights', 'prejudice', 'timeless classic'. \n\n>Band 6: 'Prejudice', 'gripping'.\n\nNot Band 8: 'Society' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'told through', 'highlights the prejudice'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_443",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a New Year's Eve party. We counted down the seconds to midnight. Everyone toasted with champagne. We watched the fireworks on TV. I made some resolutions for the new year. The mood was optimistic. We danced until dawn. It was a fantastic way to welcome the new year. I had a great time with my friends. It was a memorable night.",
        "word_count": 64,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'counted down' (phrasal verb). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'counted down', 'midnight', 'toasted', 'champagne', 'resolutions', 'optimistic', 'dawn', 'fantastic', 'welcome'. >Band 6: 'Optimistic', 'resolutions'. Not Band 8: 'TV' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'way to welcome', 'danced until dawn'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a New Year's Eve party. We counted down the seconds to midnight. Everyone toasted with champagne. We watched the fireworks on TV. I made some resolutions for the new year. The mood was optimistic. We danced until dawn. It was a fantastic way to welcome the new year. I had a great time with my friends. It was a memorable night.\n\nWord Count: 64 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'counted down', 'midnight', 'toasted', 'champagne', 'resolutions', 'optimistic', 'dawn', 'fantastic', 'welcome'. \n\n>Band 6: 'Optimistic', 'resolutions'.\n\nNot Band 8: 'TV' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'way to welcome', 'danced until dawn'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_444",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I bought a robot vacuum cleaner. It navigates around furniture autonomously. It picks up dust and pet hair. It returns to its charging dock. It saves me from doing chores. I can schedule it to run when I am out. It is a smart home device. It is a great convenience. It keeps my house clean. I love using it.",
        "word_count": 60,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'robot vacuum cleaner' (compound noun). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'robot vacuum', 'navigates', 'autonomously', 'charging dock', 'chores', 'schedule', 'smart home', 'device', 'convenience'. >Band 6: 'Autonomously', 'navigates'. Not Band 8: 'Dust' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'schedule it to run', 'saves me from doing'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I bought a robot vacuum cleaner. It navigates around furniture autonomously. It picks up dust and pet hair. It returns to its charging dock. It saves me from doing chores. I can schedule it to run when I am out. It is a smart home device. It is a great convenience. It keeps my house clean. I love using it.\n\nWord Count: 60 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'robot vacuum', 'navigates', 'autonomously', 'charging dock', 'chores', 'schedule', 'smart home', 'device', 'convenience'. \n\n>Band 6: 'Autonomously', 'navigates'.\n\nNot Band 8: 'Dust' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'schedule it to run', 'saves me from doing'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_445",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I went to the Acropolis in Athens. It is situated on a rocky hilltop. The Parthenon is the main attraction. It is a symbol of democracy. The columns are massive and impressive. I hired a guide to explain the history. The view of the city below is spectacular. It is a cultural heritage site. I was amazed by its beauty. It is a very important place.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'situated on' (passive). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'situated', 'rocky hilltop', 'attraction', 'symbol of democracy', 'massive', 'impressive', 'guide', 'spectacular', 'cultural heritage'. >Band 6: 'Heritage', 'democracy'. Not Band 8: 'View' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'situated on', 'guide to explain'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I went to the Acropolis in Athens. It is situated on a rocky hilltop. The Parthenon is the main attraction. It is a symbol of democracy. The columns are massive and impressive. I hired a guide to explain the history. The view of the city below is spectacular. It is a cultural heritage site. I was amazed by its beauty. It is a very important place.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'situated', 'rocky hilltop', 'attraction', 'symbol of democracy', 'massive', 'impressive', 'guide', 'spectacular', 'cultural heritage'. \n\n>Band 6: 'Heritage', 'democracy'.\n\nNot Band 8: 'View' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'situated on', 'guide to explain'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_446",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I planted some lavender in my garden. It has a fragrant scent. The purple flowers are beautiful. It attracts bees and butterflies. I dry the flowers to make sachets. It helps me relax and sleep better. It is a hardy plant that needs sun. It adds color to my yard. I enjoy gardening very much. It is a peaceful hobby.",
        "word_count": 60,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'fragrant scent' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'lavender', 'fragrant scent', 'attracts', 'bees', 'butterflies', 'sachets', 'relax', 'hardy', 'needs sun'. >Band 6: 'Fragrant', 'hardy'. Not Band 8: 'Purple flowers' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'dry the flowers to make', 'plant that needs'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I planted some lavender in my garden. It has a fragrant scent. The purple flowers are beautiful. It attracts bees and butterflies. I dry the flowers to make sachets. It helps me relax and sleep better. It is a hardy plant that needs sun. It adds color to my yard. I enjoy gardening very much. It is a peaceful hobby.\n\nWord Count: 60 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'lavender', 'fragrant scent', 'attracts', 'bees', 'butterflies', 'sachets', 'relax', 'hardy', 'needs sun'. \n\n>Band 6: 'Fragrant', 'hardy'.\n\nNot Band 8: 'Purple flowers' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'dry the flowers to make', 'plant that needs'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_447",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My roommate is a fitness fanatic. She wakes up early to jog. She eats healthy food. She encourages me to exercise. We go to the gym together. She is very disciplined. Her energy is contagious. She helps me stay motivated. I admire her dedication to health. She is a great role model for me. I am lucky to know her.",
        "word_count": 60,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'fitness fanatic' (idiom). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'roommate', 'fitness fanatic', 'jog', 'healthy food', 'encourages', 'disciplined', 'contagious', 'motivated', 'dedication'. >Band 6: 'Disciplined', 'contagious'. Not Band 8: 'Gym' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'encourages me to', 'admire her dedication'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My roommate is a fitness fanatic. She wakes up early to jog. She eats healthy food. She encourages me to exercise. We go to the gym together. She is very disciplined. Her energy is contagious. She helps me stay motivated. I admire her dedication to health. She is a great role model for me. I am lucky to know her.\n\nWord Count: 60 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'roommate', 'fitness fanatic', 'jog', 'healthy food', 'encourages', 'disciplined', 'contagious', 'motivated', 'dedication'. \n\n>Band 6: 'Disciplined', 'contagious'.\n\nNot Band 8: 'Gym' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'encourages me to', 'admire her dedication'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_448",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I considered adopting a pet. It is a big responsibility. I live in a small apartment. I worried about the cost of food and vet bills. However, I wanted companionship. I adopted a cat from the shelter. She is low-maintenance and affectionate. It was the right choice for me. I love my cat very much. She makes me happy.",
        "word_count": 58,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'big responsibility' (collocation). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'adopting', 'responsibility', 'vet bills', 'companionship', 'shelter', 'low-maintenance', 'affectionate'. >Band 6: 'Companionship', 'affectionate'. Not Band 8: 'Pet' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'worried about the cost', 'However, I wanted'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I considered adopting a pet. It is a big responsibility. I live in a small apartment. I worried about the cost of food and vet bills. However, I wanted companionship. I adopted a cat from the shelter. She is low-maintenance and affectionate. It was the right choice for me. I love my cat very much. She makes me happy.\n\nWord Count: 58 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'adopting', 'responsibility', 'vet bills', 'companionship', 'shelter', 'low-maintenance', 'affectionate'. \n\n>Band 6: 'Companionship', 'affectionate'.\n\nNot Band 8: 'Pet' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'worried about the cost', 'However, I wanted'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_449",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I joined a spelling bee. I have a good memory for words. The words got harder in each round. I was nervous but focused. I spelled a difficult word correctly. I won the trophy. My parents were proud. It boosted my confidence. It was a thrilling experience. I studied hard for it. It was worth the effort.",
        "word_count": 56,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'spelling bee' (compound noun). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'spelling bee', 'memory', 'nervous', 'focused', 'trophy', 'proud', 'boosted', 'confidence', 'thrilling'. >Band 6: 'Boosted', 'thrilling'. Not Band 8: 'Words' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'nervous but focused', 'difficult word correctly'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I joined a spelling bee. I have a good memory for words. The words got harder in each round. I was nervous but focused. I spelled a difficult word correctly. I won the trophy. My parents were proud. It boosted my confidence. It was a thrilling experience. I studied hard for it. It was worth the effort.\n\nWord Count: 56 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'spelling bee', 'memory', 'nervous', 'focused', 'trophy', 'proud', 'boosted', 'confidence', 'thrilling'. \n\n>Band 6: 'Boosted', 'thrilling'.\n\nNot Band 8: 'Words' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'nervous but focused', 'difficult word correctly'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g6_450",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I saw the Big Ben in London. It is a massive clock tower. The chimes are loud and distinct. It is located near the river. It is a landmark of the city. I took a selfie with it. It looks magnificent at night. It is a symbol of British culture. I really enjoyed seeing it. It is a very famous place.",
        "word_count": 61,
        "response_type": "long_turn",
        "micro_flaws": [
             "grammar: 'clock tower' (compound noun). Simple sentences."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "moderate",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'massive', 'clock tower', 'chimes', 'distinct', 'located', 'landmark', 'magnificent', 'symbol', 'culture'. >Band 6: 'Magnificent', 'distinct'. Not Band 8: 'Selfie' is common.",
        "grammar_reason": "[GRA6] Key evidence: 'located near', 'looks magnificent'. >Band 5: Mix of structures. Not Band 7: Very short sentences.",
        "vocabulary": 7,
        "grammar": 6,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I saw the Big Ben in London. It is a massive clock tower. The chimes are loud and distinct. It is located near the river. It is a landmark of the city. I took a selfie with it. It looks magnificent at night. It is a symbol of British culture. I really enjoyed seeing it. It is a very famous place.\n\nWord Count: 61 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'massive', 'clock tower', 'chimes', 'distinct', 'located', 'landmark', 'magnificent', 'symbol', 'culture'. \n\n>Band 6: 'Magnificent', 'distinct'.\n\nNot Band 8: 'Selfie' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 6\n\n**Reasoning:** [GRA6] Key evidence: 'located near', 'looks magnificent'. \n\n>Band 5: Mix of structures.\n\nNot Band 7: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
