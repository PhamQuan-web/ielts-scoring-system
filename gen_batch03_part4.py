import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch03.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g5_226",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical figure.",
        "transcript_cleaned": "I want to talk about Abraham Lincoln. He was a prominent president of the USA. He abolished slavery. It was a significant achievement. He was a humble man who lived in a log cabin. He led the country during the Civil War. It was a turbulent time. He gave inspiring speeches. He was assassinated. It was a tragedy. He is an icon of freedom. His legacy endures.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'prominent', 'abolished', 'slavery', 'significant', 'achievement', 'humble', 'log cabin', 'turbulent', 'inspiring', 'assassinated', 'tragedy', 'icon', 'legacy', 'endures'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'prominent', 'abolished', 'slavery', 'turbulent', 'assassinated', 'icon', 'legacy', 'endures'. >Band 5: 'Abolished slavery', 'turbulent time'. Not Band 7: Good range but standard collocations.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'He was', 'He gave'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences. Lacks flow.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical figure.\n\nTranscript: I want to talk about Abraham Lincoln. He was a prominent president of the USA. He abolished slavery. It was a significant achievement. He was a humble man who lived in a log cabin. He led the country during the Civil War. It was a turbulent time. He gave inspiring speeches. He was assassinated. It was a tragedy. He is an icon of freedom. His legacy endures.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'prominent', 'abolished', 'slavery', 'turbulent', 'assassinated', 'icon', 'legacy', 'endures'. \n\n>Band 5: 'Abolished slavery', 'turbulent time'.\n\nNot Band 7: Good range but standard collocations.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'He was', 'He gave'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences. Lacks flow.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_227",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job you would like to have.",
        "transcript_cleaned": "I would like to be a journalist. It is a dynamic profession. Journalists report news. They interview people. They investigate stories. It requires curiosity and integrity. I like writing articles. I want to uncover the truth. It can be dangerous sometimes. Journalists work under pressure. They have deadlines. But it is a respectable career. I want to inform the public. It plays a vital role in society.",
        "word_count": 69,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'journalist', 'dynamic', 'profession', 'report', 'interview', 'investigate', 'curiosity', 'integrity', 'uncover', 'pressure', 'deadlines', 'respectable', 'inform', 'vital role'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'dynamic', 'profession', 'investigate', 'curiosity', 'integrity', 'uncover', 'pressure', 'deadlines', 'vital role'. >Band 5: 'Vital role', 'under pressure'. Not Band 7: Standard job vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'They interview', 'It requires'. >Band 4: Accurate simple sentences. Not Band 6: Monotonous sentence structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a job you would like to have.\n\nTranscript: I would like to be a journalist. It is a dynamic profession. Journalists report news. They interview people. They investigate stories. It requires curiosity and integrity. I like writing articles. I want to uncover the truth. It can be dangerous sometimes. Journalists work under pressure. They have deadlines. But it is a respectable career. I want to inform the public. It plays a vital role in society.\n\nWord Count: 69 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'dynamic', 'profession', 'investigate', 'curiosity', 'integrity', 'uncover', 'pressure', 'deadlines', 'vital role'. \n\n>Band 5: 'Vital role', 'under pressure'.\n\nNot Band 7: Standard job vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'They interview', 'It requires'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Monotonous sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_228",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I had to decide whether to buy a car or save money. It was a dilemma. I needed a car for work. But cars are expensive. I also wanted to save for a house. I weighed the pros and cons. I calculated my budget. It was a financial decision. Finally, I bought a used car. It was affordable. I compromised. It was a practical solution. I am happy with the outcome.",
        "word_count": 74,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'whether', 'dilemma', 'weighed', 'pros and cons', 'calculated', 'budget', 'financial', 'affordable', 'compromised', 'practical', 'solution', 'outcome'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'dilemma', 'weighed', 'pros and cons', 'budget', 'financial', 'affordable', 'compromised', 'outcome'. >Band 5: 'Pros and cons', 'financial decision'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I needed', 'I also wanted'. >Band 4: Accurate simple sentences. Not Band 6: Lacks complex structures.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I had to decide whether to buy a car or save money. It was a dilemma. I needed a car for work. But cars are expensive. I also wanted to save for a house. I weighed the pros and cons. I calculated my budget. It was a financial decision. Finally, I bought a used car. It was affordable. I compromised. It was a practical solution. I am happy with the outcome.\n\nWord Count: 74 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'dilemma', 'weighed', 'pros and cons', 'budget', 'financial', 'affordable', 'compromised', 'outcome'. \n\n>Band 5: 'Pros and cons', 'financial decision'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I needed', 'I also wanted'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks complex structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_229",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you read.",
        "transcript_cleaned": "I read \"Sherlock Holmes\". It is a mystery novel. The protagonist is a detective. He is brilliant but eccentric. He solves crimes in London. He uses deduction and logic. I was captivated by the plot. It was suspenseful. The clues were hidden. I tried to guess the culprit. The ending was unexpected. It is a classic literary work. I admire the author's creativity. It kept me on the edge of my seat.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'mystery', 'novel', 'protagonist', 'detective', 'brilliant', 'eccentric', 'solves', 'deduction', 'logic', 'captivated', 'plot', 'suspenseful', 'clues', 'culprit', 'unexpected', 'literary', 'creativity', 'edge of my seat'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'protagonist', 'eccentric', 'deduction', 'captivated', 'suspenseful', 'culprit', 'literary', 'edge of my seat'. >Band 5: 'Edge of my seat', 'captivated'. Not Band 7: Idiom used correctly but isolated.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'He is', 'He uses'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book you read.\n\nTranscript: I read \"Sherlock Holmes\". It is a mystery novel. The protagonist is a detective. He is brilliant but eccentric. He solves crimes in London. He uses deduction and logic. I was captivated by the plot. It was suspenseful. The clues were hidden. I tried to guess the culprit. The ending was unexpected. It is a classic literary work. I admire the author's creativity. It kept me on the edge of my seat.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'protagonist', 'eccentric', 'deduction', 'captivated', 'suspenseful', 'culprit', 'literary', 'edge of my seat'. \n\n>Band 5: 'Edge of my seat', 'captivated'.\n\nNot Band 7: Idiom used correctly but isolated.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'He is', 'He uses'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_230",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I visited the Pyramids of Giza. They are ancient structures in Egypt. They were tombs for pharaohs. They are massive and majestic. I marveled at their size. They were built thousands of years ago. It is an engineering marvel. I saw the Sphinx too. It is a mythical creature. The site is full of history. It is a popular tourist destination. I felt awestruck. It is a testament to human ingenuity.",
        "word_count": 74,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'ancient', 'structures', 'tombs', 'pharaohs', 'massive', 'majestic', 'marveled', 'engineering marvel', 'mythical', 'creature', 'destination', 'awestruck', 'testament', 'ingenuity'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'tombs', 'majestic', 'marveled', 'mythical', 'awestruck', 'testament', 'ingenuity'. >Band 5: 'Engineering marvel', 'awestruck'. Not Band 7: Advanced vocab used in simple frames.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'They were'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I visited the Pyramids of Giza. They are ancient structures in Egypt. They were tombs for pharaohs. They are massive and majestic. I marveled at their size. They were built thousands of years ago. It is an engineering marvel. I saw the Sphinx too. It is a mythical creature. The site is full of history. It is a popular tourist destination. I felt awestruck. It is a testament to human ingenuity.\n\nWord Count: 74 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'tombs', 'majestic', 'marveled', 'mythical', 'awestruck', 'testament', 'ingenuity'. \n\n>Band 5: 'Engineering marvel', 'awestruck'.\n\nNot Band 7: Advanced vocab used in simple frames.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'They were'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_231",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I learned to speak publically. It was a daunting task. I joined a debate club. I had to speak in front of an audience. I was terrified. My hands shook. I forgot my lines. But I persisted. I practiced my speech daily. I improved my articulation. I gained confidence. Now I can express my opinions clearly. It was a transformative experience. I overcame my fear of public speaking.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'publically', 'daunting', 'debate', 'audience', 'terrified', 'shook', 'persisted', 'articulation', 'confidence', 'express', 'opinions', 'transformative', 'overcame'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'daunting', 'debate', 'terrified', 'persisted', 'articulation', 'transformative', 'overcame'. >Band 5: 'Daunting task', 'transformative'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I joined', 'I was'. >Band 4: Accurate simple sentences. Not Band 6: Short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I learned to speak publically. It was a daunting task. I joined a debate club. I had to speak in front of an audience. I was terrified. My hands shook. I forgot my lines. But I persisted. I practiced my speech daily. I improved my articulation. I gained confidence. Now I can express my opinions clearly. It was a transformative experience. I overcame my fear of public speaking.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'daunting', 'debate', 'terrified', 'persisted', 'articulation', 'transformative', 'overcame'. \n\n>Band 5: 'Daunting task', 'transformative'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I joined', 'I was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_232",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful skill.",
        "transcript_cleaned": "I learned first aid. It is a vital skill. I attended a workshop. I learned CPR. I learned how to treat burns and cuts. It is practical knowledge. Emergencies can happen anytime. Being prepared is crucial. I can help injured people. I feel more responsible. It could save a life. I think everyone should learn the basics. It is a civic duty.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'first aid', 'vital', 'workshop', 'CPR', 'treat', 'burns', 'cuts', 'practical', 'emergencies', 'prepared', 'crucial', 'injured', 'responsible', 'basics', 'civic duty'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'vital', 'CPR', 'treat', 'practical', 'emergencies', 'crucial', 'civic duty'. >Band 5: 'Civic duty', 'vital skill'. Not Band 7: Standard health vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I learned', 'It is'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful skill.\n\nTranscript: I learned first aid. It is a vital skill. I attended a workshop. I learned CPR. I learned how to treat burns and cuts. It is practical knowledge. Emergencies can happen anytime. Being prepared is crucial. I can help injured people. I feel more responsible. It could save a life. I think everyone should learn the basics. It is a civic duty.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'vital', 'CPR', 'treat', 'practical', 'emergencies', 'crucial', 'civic duty'. \n\n>Band 5: 'Civic duty', 'vital skill'.\n\nNot Band 7: Standard health vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I learned', 'It is'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_233",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party you enjoyed.",
        "transcript_cleaned": "I went to a Halloween party. It was a costume party. Everyone dressed up. I wore a pirate costume. The decorations were spooky. There were pumpkins and ghosts. We played games like bobbing for apples. It was hilarious. We ate candy and snacks. The atmosphere was festive. I met many interesting characters. It was a fun night. I enjoy social gatherings like this.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'costume party', 'dressed up', 'pirate', 'decorations', 'spooky', 'pumpkins', 'ghosts', 'bobbing', 'hilarious', 'festive', 'characters', 'social gatherings'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'costume', 'spooky', 'bobbing', 'hilarious', 'festive', 'social gatherings'. >Band 5: 'Spooky', 'hilarious'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I wore', 'It was'. >Band 4: Accurate simple sentences. Not Band 6: Monotonous structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party you enjoyed.\n\nTranscript: I went to a Halloween party. It was a costume party. Everyone dressed up. I wore a pirate costume. The decorations were spooky. There were pumpkins and ghosts. We played games like bobbing for apples. It was hilarious. We ate candy and snacks. The atmosphere was festive. I met many interesting characters. It was a fun night. I enjoy social gatherings like this.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'costume', 'spooky', 'bobbing', 'hilarious', 'festive', 'social gatherings'. \n\n>Band 5: 'Spooky', 'hilarious'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I wore', 'It was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Monotonous structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_234",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a beautiful place.",
        "transcript_cleaned": "I visited the Swiss Alps. The mountains are majestic. They are covered in snow. The peaks are high. I went skiing there. The air was crisp and clean. I stayed in a cozy chalet. The scenery was picturesque. I felt peaceful. I saw pine forests and frozen lakes. It is a winter wonderland. Nature is stunning there. It was a memorable vacation.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'Alps', 'majestic', 'peaks', 'skiing', 'crisp', 'cozy', 'chalet', 'scenery', 'picturesque', 'peaceful', 'pine forests', 'frozen', 'wonderland', 'stunning', 'memorable'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'majestic', 'crisp', 'chalet', 'picturesque', 'wonderland', 'stunning'. >Band 5: 'Picturesque', 'majestic'. Not Band 7: Strong adjectives but listed.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'The mountains are', 'I went'. >Band 4: Accurate simple sentences. Not Band 6: Very repetitive.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a beautiful place.\n\nTranscript: I visited the Swiss Alps. The mountains are majestic. They are covered in snow. The peaks are high. I went skiing there. The air was crisp and clean. I stayed in a cozy chalet. The scenery was picturesque. I felt peaceful. I saw pine forests and frozen lakes. It is a winter wonderland. Nature is stunning there. It was a memorable vacation.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'majestic', 'crisp', 'chalet', 'picturesque', 'wonderland', 'stunning'. \n\n>Band 5: 'Picturesque', 'majestic'.\n\nNot Band 7: Strong adjectives but listed.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'The mountains are', 'I went'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very repetitive.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_235",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie.",
        "transcript_cleaned": "I watched a horror movie called \"The Conjuring\". It was terrifying. It is about a haunted house. A family moves in. Strange things happen. Doors slam shut. Ghosts appear. The atmosphere is eerie. The sound effects are scary. I screamed a few times. I covered my eyes. It was suspenseful. I could not sleep afterwards. I had nightmares. It is a classic horror film.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'horror', 'terrifying', 'haunted', 'moves in', 'strange', 'slam shut', 'ghosts', 'appear', 'atmosphere', 'eerie', 'sound effects', 'screamed', 'suspenseful', 'nightmares', 'classic'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'terrifying', 'haunted', 'slam shut', 'eerie', 'suspenseful', 'nightmares'. >Band 5: 'Eerie', 'terrifying'. Not Band 7: Standard genre words.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'I screamed'. >Band 4: Accurate simple sentences. Not Band 6: Short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie.\n\nTranscript: I watched a horror movie called \"The Conjuring\". It was terrifying. It is about a haunted house. A family moves in. Strange things happen. Doors slam shut. Ghosts appear. The atmosphere is eerie. The sound effects are scary. I screamed a few times. I covered my eyes. It was suspenseful. I could not sleep afterwards. I had nightmares. It is a classic horror film.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'terrifying', 'haunted', 'slam shut', 'eerie', 'suspenseful', 'nightmares'. \n\n>Band 5: 'Eerie', 'terrifying'.\n\nNot Band 7: Standard genre words.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'I screamed'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_236",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of news.",
        "transcript_cleaned": "I read about a space mission. Astronauts went to the International Space Station. They launched in a rocket. It was a successful launch. They will conduct experiments. They study zero gravity. It is a scientific milestone. I saw the video footage. It was impressive. Space exploration is fascinating. It expands our knowledge. I want to know more about the universe. It is an exciting field.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'mission', 'astronauts', 'launched', 'rocket', 'successful', 'conduct', 'experiments', 'zero gravity', 'milestone', 'footage', 'exploration', 'fascinating', 'expands', 'universe', 'field'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'astronauts', 'launched', 'conduct experiments', 'zero gravity', 'milestone', 'footage', 'exploration'. >Band 5: 'Conduct experiments', 'milestone'. Not Band 7: Good topic vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'They launched', 'It was'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of news.\n\nTranscript: I read about a space mission. Astronauts went to the International Space Station. They launched in a rocket. It was a successful launch. They will conduct experiments. They study zero gravity. It is a scientific milestone. I saw the video footage. It was impressive. Space exploration is fascinating. It expands our knowledge. I want to know more about the universe. It is an exciting field.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'astronauts', 'launched', 'conduct experiments', 'zero gravity', 'milestone', 'footage', 'exploration'. \n\n>Band 5: 'Conduct experiments', 'milestone'.\n\nNot Band 7: Good topic vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'They launched', 'It was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_237",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift.",
        "transcript_cleaned": "I received a bicycle for Christmas. It is a mountain bike. It has many gears. It is sturdy and durable. I ride it on trails. It handles rough terrain well. It gives me freedom. I explore my neighborhood. It is also good exercise. I maintain it properly. I oil the chain. It was a generous gift from my uncle. I appreciate it.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'bicycle', 'mountain bike', 'gears', 'sturdy', 'durable', 'trails', 'handles', 'rough terrain', 'freedom', 'explore', 'maintain', 'properly', 'generous', 'appreciate'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'gears', 'sturdy', 'durable', 'terrain', 'maintain', 'properly', 'appreciate'. >Band 5: 'Rough terrain', 'sturdy'. Not Band 7: Standard phrasing.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'I ride'. >Band 4: Accurate simple sentences. Not Band 6: Monotonous.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift.\n\nTranscript: I received a bicycle for Christmas. It is a mountain bike. It has many gears. It is sturdy and durable. I ride it on trails. It handles rough terrain well. It gives me freedom. I explore my neighborhood. It is also good exercise. I maintain it properly. I oil the chain. It was a generous gift from my uncle. I appreciate it.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'gears', 'sturdy', 'durable', 'terrain', 'maintain', 'properly', 'appreciate'. \n\n>Band 5: 'Rough terrain', 'sturdy'.\n\nNot Band 7: Standard phrasing.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'I ride'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Monotonous.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_238",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a game.",
        "transcript_cleaned": "I play tennis on weekends. It is a racquet sport. I play on a court. I need a racquet and balls. The rules are simple but playing is hard. It requires agility and stamina. I serve the ball. We hit it back and forth. It is competitive. I want to win. But it is also social. I play with my colleagues. It relieves stress. It is my favorite pastime.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'tennis', 'racquet sport', 'court', 'agility', 'stamina', 'serve', 'competitive', 'social', 'colleagues', 'relieves stress', 'pastime'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'racquet', 'agility', 'stamina', 'serve', 'competitive', 'relieves stress', 'pastime'. >Band 5: 'Agility', 'stamina', 'relieves stress'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I play', 'It is'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a game.\n\nTranscript: I play tennis on weekends. It is a racquet sport. I play on a court. I need a racquet and balls. The rules are simple but playing is hard. It requires agility and stamina. I serve the ball. We hit it back and forth. It is competitive. I want to win. But it is also social. I play with my colleagues. It relieves stress. It is my favorite pastime.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'racquet', 'agility', 'stamina', 'serve', 'competitive', 'relieves stress', 'pastime'. \n\n>Band 5: 'Agility', 'stamina', 'relieves stress'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I play', 'It is'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_239",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Great Wall of China. It is a massive fortification. It stretches for thousands of miles. It was built to protect the empire. It is made of brick and stone. I walked along the wall. The view was panoramic. I saw watchtowers. It is an architectural marvel. It took centuries to build. It represents Chinese history. I was impressed by its scale. It is a world wonder.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'massive', 'fortification', 'stretches', 'protect', 'empire', 'panoramic', 'watchtowers', 'architectural marvel', 'centuries', 'represents', 'scale', 'wonder'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'fortification', 'stretches', 'empire', 'panoramic', 'architectural marvel', 'represents', 'scale'. >Band 5: 'Fortification', 'architectural marvel'. Not Band 7: Advanced terms used simply.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'I walked'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Great Wall of China. It is a massive fortification. It stretches for thousands of miles. It was built to protect the empire. It is made of brick and stone. I walked along the wall. The view was panoramic. I saw watchtowers. It is an architectural marvel. It took centuries to build. It represents Chinese history. I was impressed by its scale. It is a world wonder.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'fortification', 'stretches', 'empire', 'panoramic', 'architectural marvel', 'represents', 'scale'. \n\n>Band 5: 'Fortification', 'architectural marvel'.\n\nNot Band 7: Advanced terms used simply.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'I walked'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_240",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill.",
        "transcript_cleaned": "I learned how to bake bread. It is a culinary skill. I mix flour, water, and yeast. I knead the dough. It requires strength. I let it rise. Then I bake it in the oven. The smell is heavenly. Fresh bread is delicious. It is healthier than store-bought bread. I experiment with ingredients. I add nuts and seeds. Baking is therapeutic. It relaxes me. I enjoy sharing it.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'bake', 'culinary', 'mix', 'yeast', 'knead', 'dough', 'rise', 'heavenly', 'store-bought', 'experiment', 'ingredients', 'therapeutic', 'relaxes'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'culinary', 'yeast', 'knead', 'dough', 'heavenly', 'store-bought', 'experiment', 'therapeutic'. >Band 5: 'Knead dough', 'therapeutic'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I mix', 'I knead'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill.\n\nTranscript: I learned how to bake bread. It is a culinary skill. I mix flour, water, and yeast. I knead the dough. It requires strength. I let it rise. Then I bake it in the oven. The smell is heavenly. Fresh bread is delicious. It is healthier than store-bought bread. I experiment with ingredients. I add nuts and seeds. Baking is therapeutic. It relaxes me. I enjoy sharing it.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'culinary', 'yeast', 'knead', 'dough', 'heavenly', 'store-bought', 'experiment', 'therapeutic'. \n\n>Band 5: 'Knead dough', 'therapeutic'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I mix', 'I knead'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_241",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult journey.",
        "transcript_cleaned": "I trekked in the Himalayas. It was an adventurous journey. The altitude was high. The air was thin. I had difficulty breathing. The terrain was rugged. We walked for days. I was exhausted. But the scenery was magnificent. I saw snow-capped peaks. I felt a sense of awe. We camped in tents. It was freezing at night. But I persisted. Reaching the summit was a triumph.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'trekked', 'Himalayas', 'adventurous', 'altitude', 'terrain', 'rugged', 'exhausted', 'magnificent', 'snow-capped', 'peaks', 'awe', 'freezing', 'persisted', 'summit', 'triumph'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'trekked', 'altitude', 'terrain', 'rugged', 'magnificent', 'snow-capped', 'awe', 'persisted', 'summit', 'triumph'. >Band 5: 'Rugged terrain', 'triumph'. Not Band 7: Advanced vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'I had'. >Band 4: Accurate simple sentences. Not Band 6: Short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult journey.\n\nTranscript: I trekked in the Himalayas. It was an adventurous journey. The altitude was high. The air was thin. I had difficulty breathing. The terrain was rugged. We walked for days. I was exhausted. But the scenery was magnificent. I saw snow-capped peaks. I felt a sense of awe. We camped in tents. It was freezing at night. But I persisted. Reaching the summit was a triumph.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'trekked', 'altitude', 'terrain', 'rugged', 'magnificent', 'snow-capped', 'awe', 'persisted', 'summit', 'triumph'. \n\n>Band 5: 'Rugged terrain', 'triumph'.\n\nNot Band 7: Advanced vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'I had'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_242",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I admire my boss. He is an effective leader. He manages a large team. He is fair and approachable. He listens to our ideas. He solves conflicts calmly. He has a clear vision. He motivates us to work hard. He is also knowledgeable. I learned a lot from him. He is a mentor to me. I respect his integrity. He is a role model for success.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'admire', 'effective', 'leader', 'manages', 'fair', 'approachable', 'conflicts', 'calmly', 'vision', 'motivates', 'knowledgeable', 'mentor', 'integrity', 'role model'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'effective', 'approachable', 'conflicts', 'vision', 'motivates', 'mentor', 'integrity'. >Band 5: 'Approachable', 'integrity'. Not Band 7: Standard business vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'He is', 'He manages'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive 'He'.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I admire my boss. He is an effective leader. He manages a large team. He is fair and approachable. He listens to our ideas. He solves conflicts calmly. He has a clear vision. He motivates us to work hard. He is also knowledgeable. I learned a lot from him. He is a mentor to me. I respect his integrity. He is a role model for success.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'effective', 'approachable', 'conflicts', 'vision', 'motivates', 'mentor', 'integrity'. \n\n>Band 5: 'Approachable', 'integrity'.\n\nNot Band 7: Standard business vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'He is', 'He manages'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive 'He'.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_243",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place.",
        "transcript_cleaned": "I visited a library in Dublin. It is an historic building. It is famous for its collection. The books are ancient. They are kept in glass cases. The architecture is stunning. The ceiling is high and painted. It smells of old paper. It is a scholarly atmosphere. Students and tourists visit it. I felt inspired there. It is a treasure trove of knowledge. I love such places.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'historic', 'collection', 'ancient', 'glass cases', 'architecture', 'stunning', 'scholarly', 'atmosphere', 'inspired', 'treasure trove'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'historic', 'collection', 'ancient', 'stunning', 'scholarly', 'atmosphere', 'treasure trove'. >Band 5: 'Treasure trove', 'scholarly'. Not Band 7: Good collocations.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'The books are'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a place.\n\nTranscript: I visited a library in Dublin. It is an historic building. It is famous for its collection. The books are ancient. They are kept in glass cases. The architecture is stunning. The ceiling is high and painted. It smells of old paper. It is a scholarly atmosphere. Students and tourists visit it. I felt inspired there. It is a treasure trove of knowledge. I love such places.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'historic', 'collection', 'ancient', 'stunning', 'scholarly', 'atmosphere', 'treasure trove'. \n\n>Band 5: 'Treasure trove', 'scholarly'.\n\nNot Band 7: Good collocations.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'The books are'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_244",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a traditional event.",
        "transcript_cleaned": "I attended a dragon boat festival. It is a cultural event in China. Teams row boats. The boats look like dragons. It is a race. The atmosphere is vibrant. People beat drums to set the rhythm. Crowds cheer loudly. We eat sticky rice dumplings. It commemorates a famous poet. It is a symbol of patriotism. I enjoyed the spectacle. It was thrilling to watch.",
        "word_count": 65,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'dragon boat', 'cultural', 'row', 'vibrant', 'rhythm', 'cheer', 'sticky rice dumplings', 'commemorates', 'poet', 'symbol', 'patriotism', 'spectacle', 'thrilling'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'cultural', 'vibrant', 'rhythm', 'commemorates', 'patriotism', 'spectacle', 'thrilling'. >Band 5: 'Commemorates', 'spectacle'. Not Band 7: Advanced words used simply.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'People beat'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a traditional event.\n\nTranscript: I attended a dragon boat festival. It is a cultural event in China. Teams row boats. The boats look like dragons. It is a race. The atmosphere is vibrant. People beat drums to set the rhythm. Crowds cheer loudly. We eat sticky rice dumplings. It commemorates a famous poet. It is a symbol of patriotism. I enjoyed the spectacle. It was thrilling to watch.\n\nWord Count: 65 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'cultural', 'vibrant', 'rhythm', 'commemorates', 'patriotism', 'spectacle', 'thrilling'. \n\n>Band 5: 'Commemorates', 'spectacle'.\n\nNot Band 7: Advanced words used simply.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'People beat'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_245",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult choice.",
        "transcript_cleaned": "I had to choose a pet. I wanted a dog or a cat. It was a tough choice. Dogs are loyal and playful. But they need walking. Cats are independent. They are low maintenance. I live in a small apartment. So space was an issue. I considered my lifestyle. I work long hours. Finally, I chose a cat. It suits my situation better. I am happy with my companion.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'tough choice', 'loyal', 'playful', 'independent', 'low maintenance', 'issue', 'considered', 'lifestyle', 'suits', 'situation', 'companion'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'tough choice', 'loyal', 'independent', 'low maintenance', 'lifestyle', 'suits', 'companion'. >Band 5: 'Low maintenance', 'companion'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'Dogs are'. >Band 4: Accurate simple sentences. Not Band 6: Short choppy sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult choice.\n\nTranscript: I had to choose a pet. I wanted a dog or a cat. It was a tough choice. Dogs are loyal and playful. But they need walking. Cats are independent. They are low maintenance. I live in a small apartment. So space was an issue. I considered my lifestyle. I work long hours. Finally, I chose a cat. It suits my situation better. I am happy with my companion.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'tough choice', 'loyal', 'independent', 'low maintenance', 'lifestyle', 'suits', 'companion'. \n\n>Band 5: 'Low maintenance', 'companion'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'Dogs are'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short choppy sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_246",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I like the bamboo plant. It grows very fast. It is common in Asia. It has a hollow stem. It is green and tall. It is versatile. People use it for building. They also make furniture from it. Pandas eat it. It symbolizes strength and flexibility. It bends in the wind but does not break. I have bamboo in my garden. It creates a serene atmosphere.",
        "word_count": 68,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'bamboo', 'hollow', 'stem', 'versatile', 'symbolizes', 'strength', 'flexibility', 'bends', 'serene', 'atmosphere'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'hollow', 'stem', 'versatile', 'symbolizes', 'flexibility', 'serene'. >Band 5: 'Versatile', 'serene atmosphere'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It grows', 'It is'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I like the bamboo plant. It grows very fast. It is common in Asia. It has a hollow stem. It is green and tall. It is versatile. People use it for building. They also make furniture from it. Pandas eat it. It symbolizes strength and flexibility. It bends in the wind but does not break. I have bamboo in my garden. It creates a serene atmosphere.\n\nWord Count: 68 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'hollow', 'stem', 'versatile', 'symbolizes', 'flexibility', 'serene'. \n\n>Band 5: 'Versatile', 'serene atmosphere'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It grows', 'It is'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_247",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a microwave oven. It is a kitchen appliance. It heats food quickly. It uses radiation. It is very convenient. I use it to warm up leftovers. It saves time and energy. It has different settings. I can defrost frozen food. It is easy to operate. I clean it often. It is an indispensable tool in my kitchen. It makes cooking simpler.",
        "word_count": 64,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'microwave oven', 'appliance', 'radiation', 'convenient', 'leftovers', 'settings', 'defrost', 'frozen', 'operate', 'indispensable'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'appliance', 'radiation', 'convenient', 'leftovers', 'defrost', 'operate', 'indispensable'. >Band 5: 'Indispensable tool', 'defrost'. Not Band 7: Standard household vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'It uses'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a microwave oven. It is a kitchen appliance. It heats food quickly. It uses radiation. It is very convenient. I use it to warm up leftovers. It saves time and energy. It has different settings. I can defrost frozen food. It is easy to operate. I clean it often. It is an indispensable tool in my kitchen. It makes cooking simpler.\n\nWord Count: 64 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'appliance', 'radiation', 'convenient', 'leftovers', 'defrost', 'operate', 'indispensable'. \n\n>Band 5: 'Indispensable tool', 'defrost'.\n\nNot Band 7: Standard household vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'It uses'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_248",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a busy time.",
        "transcript_cleaned": "I moved house last month. It was a hectic experience. I had to pack everything. I have many belongings. I rented a truck. Loading the boxes was exhausting. I asked friends for help. We worked all day. I was stressed. I had to clean the old house too. Unpacking was also tiring. It took a week to settle in. But now I am comfortable. It was worth the effort.",
        "word_count": 70,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'hectic', 'experience', 'pack', 'belongings', 'rented', 'loading', 'exhausting', 'stressed', 'unpacking', 'settle in', 'comfortable', 'worth the effort'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'hectic', 'belongings', 'exhausting', 'unpacking', 'settle in', 'worth the effort'. >Band 5: 'Hectic', 'settle in'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'I had'. >Band 4: Accurate simple sentences. Not Band 6: Short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a busy time.\n\nTranscript: I moved house last month. It was a hectic experience. I had to pack everything. I have many belongings. I rented a truck. Loading the boxes was exhausting. I asked friends for help. We worked all day. I was stressed. I had to clean the old house too. Unpacking was also tiring. It took a week to settle in. But now I am comfortable. It was worth the effort.\n\nWord Count: 70 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'hectic', 'belongings', 'exhausting', 'unpacking', 'settle in', 'worth the effort'. \n\n>Band 5: 'Hectic', 'settle in'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'I had'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_249",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I participated in a chess tournament. It was a regional competition. I love chess. It is a strategic game. I played five matches. My opponents were skilled. I had to think deeply. I won three games. I lost two. It was mentally draining. I received a certificate. I was proud of my performance. Chess improves concentration. I enjoy the intellectual challenge.",
        "word_count": 62,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'participated', 'tournament', 'regional', 'strategic', 'opponents', 'skilled', 'mentally draining', 'certificate', 'performance', 'concentration', 'intellectual challenge'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'participated', 'tournament', 'strategic', 'opponents', 'mentally draining', 'concentration', 'intellectual challenge'. >Band 5: 'Intellectual challenge', 'mentally draining'. Not Band 7: Advanced collocations.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'I played'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I participated in a chess tournament. It was a regional competition. I love chess. It is a strategic game. I played five matches. My opponents were skilled. I had to think deeply. I won three games. I lost two. It was mentally draining. I received a certificate. I was proud of my performance. Chess improves concentration. I enjoy the intellectual challenge.\n\nWord Count: 62 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'participated', 'tournament', 'strategic', 'opponents', 'mentally draining', 'concentration', 'intellectual challenge'. \n\n>Band 5: 'Intellectual challenge', 'mentally draining'.\n\nNot Band 7: Advanced collocations.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'I played'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_250",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "I want to talk about my friend, Tom. He is a graphic designer. He is very artistic. He draws beautiful pictures. He is also generous. He shares his food. We have been friends for years. He is a loyal companion. He supports me when I am sad. We have fun together. He has a good sense of humor. He cracks jokes. I cherish our friendship.",
        "word_count": 66,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'graphic designer', 'artistic', 'generous', 'loyal', 'companion', 'supports', 'sense of humor', 'cracks jokes', 'cherish'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'graphic designer', 'artistic', 'loyal companion', 'sense of humor', 'cracks jokes', 'cherish'. >Band 5: 'Cracks jokes', 'cherish'. Not Band 7: Good idioms/phrases.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'He is', 'He draws'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: I want to talk about my friend, Tom. He is a graphic designer. He is very artistic. He draws beautiful pictures. He is also generous. He shares his food. We have been friends for years. He is a loyal companion. He supports me when I am sad. We have fun together. He has a good sense of humor. He cracks jokes. I cherish our friendship.\n\nWord Count: 66 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'graphic designer', 'artistic', 'loyal companion', 'sense of humor', 'cracks jokes', 'cherish'. \n\n>Band 5: 'Cracks jokes', 'cherish'.\n\nNot Band 7: Good idioms/phrases.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'He is', 'He draws'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
