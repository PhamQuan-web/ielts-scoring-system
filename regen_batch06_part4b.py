import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch06.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v7_g7_539",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a house party last Saturday. It was crowded and lively. People were dancing in the living room to loud music. I met some interesting people and had good conversations. We talked for hours about our hobbies. We ate pizza and chips. It was a lively social gathering where I felt comfortable. I had a blast dancing with my friends.",
        "word_count": 63,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'crowded', 'lively', 'social gathering', 'had a blast'. Band 7 level.",
             "grammar: 'dancing in the', 'gathering where I felt'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'crowded', 'lively', 'social gathering', 'had a blast'. >Band 6: 'Lively', 'blast'. Not Band 8: 'Music' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'dancing in the', 'gathering where I felt'. >Band 6: Participles and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": True,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a house party last Saturday. It was crowded and lively. People were dancing in the living room to loud music. I met some interesting people and had good conversations. We talked for hours about our hobbies. We ate pizza and chips. It was a lively social gathering where I felt comfortable. I had a blast dancing with my friends.\n\nWord Count: 63 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'crowded', 'lively', 'social gathering', 'had a blast'. \n\n>Band 6: 'Lively', 'blast'.\n\nNot Band 8: 'Music' is common.\n\n**Idiom present:** Yes\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'dancing in the', 'gathering where I felt'. \n\n>Band 6: Participles and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_540",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a laptop stand to improve my posture. It raises my screen to eye level, preventing neck pain. It is adjustable and sturdy. I use an external keyboard with it for better typing. It makes my workspace ergonomic and comfortable. It is a simple but effective tool for anyone who works at a desk. I highly recommend it.",
        "word_count": 60,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'posture', 'raises', 'eye level', 'preventing', 'neck pain', 'adjustable', 'sturdy', 'external keyboard', 'workspace', 'ergonomic', 'effective'. Band 7 level.",
             "grammar: 'raises... preventing', 'tool for anyone who'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'posture', 'raises', 'eye level', 'preventing', 'neck pain', 'adjustable', 'ergonomic'. >Band 6: 'Ergonomic', 'posture'. Not Band 8: 'Screen' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'raises... preventing', 'tool for anyone who'. >Band 6: Participles and relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a laptop stand to improve my posture. It raises my screen to eye level, preventing neck pain. It is adjustable and sturdy. I use an external keyboard with it for better typing. It makes my workspace ergonomic and comfortable. It is a simple but effective tool for anyone who works at a desk. I highly recommend it.\n\nWord Count: 60 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'posture', 'raises', 'eye level', 'preventing', 'neck pain', 'adjustable', 'ergonomic'. \n\n>Band 6: 'Ergonomic', 'posture'.\n\nNot Band 8: 'Screen' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'raises... preventing', 'tool for anyone who'. \n\n>Band 6: Participles and relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_541",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I saw the Acropolis in Athens. It is located on a hill overlooking the city. The Parthenon is the main temple, dedicated to Athena. It has white marble columns that are very old. It represents Greek history and democracy. The view from the top is nice. I liked walking around the ruins and imagining the past. It is a significant site.",
        "word_count": 62,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'overlooking', 'temple', 'dedicated', 'columns', 'represents', 'democracy', 'ruins', 'imagining', 'significant'. Band 7 level.",
             "grammar: 'located on a hill', 'columns that are', 'imagining the past'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'overlooking', 'temple', 'dedicated', 'columns', 'represents', 'democracy', 'ruins', 'imagining', 'significant'. >Band 6: 'Parthenon', 'ruins'. Not Band 8: 'Old' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'located on a hill', 'imagining the past'. >Band 6: Participles and gerunds used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I saw the Acropolis in Athens. It is located on a hill overlooking the city. The Parthenon is the main temple, dedicated to Athena. It has white marble columns that are very old. It represents Greek history and democracy. The view from the top is nice. I liked walking around the ruins and imagining the past. It is a significant site.\n\nWord Count: 62 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'overlooking', 'temple', 'dedicated', 'columns', 'represents', 'democracy', 'ruins', 'imagining', 'significant'. \n\n>Band 6: 'Parthenon', 'ruins'.\n\nNot Band 8: 'Old' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'located on a hill', 'imagining the past'. \n\n>Band 6: Participles and gerunds used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_542",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I had to give a presentation, which was scary. I prepared my slides carefully. I practiced my speech in front of a mirror. I spoke clearly and confidently. The audience listened attentively. They asked questions, which I answered well. I felt proud of my performance. It was a good experience that boosted my confidence.",
        "word_count": 53,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'presentation', 'slides', 'practiced', 'confidently', 'attentively', 'performance', 'boosted'. Band 7 level.",
             "grammar: 'presentation, which was', 'questions, which I answered'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'presentation', 'slides', 'practiced', 'confidently', 'attentively', 'performance', 'boosted'. >Band 6: 'Slides', 'practiced'. Not Band 8: 'Good' is implied.",
        "grammar_reason": "[GRA7] Key evidence: 'presentation, which was', 'questions, which I answered'. >Band 6: Relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I had to give a presentation, which was scary. I prepared my slides carefully. I practiced my speech in front of a mirror. I spoke clearly and confidently. The audience listened attentively. They asked questions, which I answered well. I felt proud of my performance. It was a good experience that boosted my confidence.\n\nWord Count: 53 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'presentation', 'slides', 'practiced', 'confidently', 'attentively', 'performance', 'boosted'. \n\n>Band 6: 'Slides', 'practiced'.\n\nNot Band 8: 'Good' is implied.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'presentation, which was', 'questions, which I answered'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_543",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read a biography of Steve Jobs. He was an innovator who started Apple. The book describes his life and career. He was a visionary but difficult person to work with. He changed technology forever. It was an inspiring story about determination. I learned a lot about business from reading it.",
        "word_count": 51,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'biography', 'innovator', 'visionary', 'technology', 'inspiring', 'determination', 'business'. Band 7 level.",
             "grammar: 'innovator who started', 'person to work with'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'biography', 'innovator', 'visionary', 'technology', 'inspiring', 'determination', 'business'. >Band 6: 'Innovator', 'visionary'. Not Band 8: 'Person' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'innovator who started', 'person to work with'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read a biography of Steve Jobs. He was an innovator who started Apple. The book describes his life and career. He was a visionary but difficult person to work with. He changed technology forever. It was an inspiring story about determination. I learned a lot about business from reading it.\n\nWord Count: 51 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'biography', 'innovator', 'visionary', 'technology', 'inspiring', 'determination', 'business'. \n\n>Band 6: 'Innovator', 'visionary'.\n\nNot Band 8: 'Person' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'innovator who started', 'person to work with'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_544",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a Halloween party wearing a costume. There was spooky music playing. We danced and ate candy. I talked to my friends all night. It was fun and exciting. I stayed late because I was enjoying myself. It was a great way to celebrate the holiday.",
        "word_count": 48,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'costume', 'spooky', 'candy', 'exciting', 'celebrate', 'holiday'. Band 7 level.",
             "grammar: 'party wearing a', 'stayed... because I was'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'costume', 'spooky', 'candy', 'exciting', 'celebrate'. >Band 6: 'Spooky', 'costume'. Not Band 8: 'Music' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'party wearing a', 'stayed... because I was'. >Band 6: Participles and causal clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a Halloween party wearing a costume. There was spooky music playing. We danced and ate candy. I talked to my friends all night. It was fun and exciting. I stayed late because I was enjoying myself. It was a great way to celebrate the holiday.\n\nWord Count: 48 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'costume', 'spooky', 'candy', 'exciting', 'celebrate'. \n\n>Band 6: 'Spooky', 'costume'.\n\nNot Band 8: 'Music' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'party wearing a', 'stayed... because I was'. \n\n>Band 6: Participles and causal clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_545",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a coffee maker that makes hot coffee quickly. I drink it in the morning to wake up. It is easy to use and clean. I like the smell of fresh coffee brewing. It is a good machine that I rely on. It helps me start my day right.",
        "word_count": 51,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'coffee maker', 'wake up', 'brewing', 'machine', 'rely on'. Band 7 level.",
             "grammar: 'maker that makes', 'morning to wake up'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'coffee maker', 'brewing', 'machine', 'rely on'. >Band 6: 'Machine', 'wakes'. Not Band 8: 'Hot' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'maker that makes', 'morning to wake up'. >Band 6: Relative clauses and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a coffee maker that makes hot coffee quickly. I drink it in the morning to wake up. It is easy to use and clean. I like the smell of fresh coffee brewing. It is a good machine that I rely on. It helps me start my day right.\n\nWord Count: 51 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'coffee maker', 'brewing', 'machine', 'rely on'. \n\n>Band 6: 'Machine', 'wakes'.\n\nNot Band 8: 'Hot' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'maker that makes', 'morning to wake up'. \n\n>Band 6: Relative clauses and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_546",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I saw the Eiffel Tower, which is very tall. It is made of iron and looks impressive. I went to the top to see the view. It is in Paris, a beautiful city. It is a famous landmark that everyone knows. I took many photos of it. It was a great experience.",
        "word_count": 52,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'iron', 'impressive', 'view', 'landmark', 'experience'. Band 7 level.",
             "grammar: 'Tower, which is', 'made of iron', 'landmark that everyone'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'iron', 'impressive', 'view', 'landmark'. >Band 6: 'Landmark', 'tower'. Not Band 8: 'Tall' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'Tower, which is', 'landmark that everyone'. >Band 6: Relative clauses and passive voice used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I saw the Eiffel Tower, which is very tall. It is made of iron and looks impressive. I went to the top to see the view. It is in Paris, a beautiful city. It is a famous landmark that everyone knows. I took many photos of it. It was a great experience.\n\nWord Count: 52 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'iron', 'impressive', 'view', 'landmark'. \n\n>Band 6: 'Landmark', 'tower'.\n\nNot Band 8: 'Tall' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'Tower, which is', 'landmark that everyone'. \n\n>Band 6: Relative clauses and passive voice used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_547",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I cleaned my garage, which was messy. I threw away old things I didn't need. I organized my tools neatly. It took all day to finish. I was tired but happy with the result. It looks much better now. It was hard work.",
        "word_count": 43,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'messy', 'threw away', 'organized', 'neatly', 'hard work'. Band 7 level.",
             "grammar: 'garage, which was', 'things I didn't need'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'messy', 'threw away', 'organized', 'neatly', 'tools'. >Band 6: 'Organized', 'messy'. Not Band 8: 'Day' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'garage, which was', 'things I didn't need'. >Band 6: Relative clauses used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I cleaned my garage, which was messy. I threw away old things I didn't need. I organized my tools neatly. It took all day to finish. I was tired but happy with the result. It looks much better now. It was hard work.\n\nWord Count: 43 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'messy', 'threw away', 'organized', 'neatly', 'tools'. \n\n>Band 6: 'Organized', 'messy'.\n\nNot Band 8: 'Day' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'garage, which was', 'things I didn't need'. \n\n>Band 6: Relative clauses used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_548",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book.",
        "transcript_cleaned": "I read a fantasy book with dragons. The hero was brave and strong. He fought a bad guy to save the world. I liked the story very much. It was fun to read. I imagined being there. It was exciting.",
        "word_count": 40,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'fantasy', 'dragons', 'hero', 'brave', 'fought', 'imagined', 'exciting'. Band 7 level.",
             "grammar: 'book with dragons', 'fought... to save'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'fantasy', 'dragons', 'hero', 'brave', 'fought'. >Band 6: 'Fantasy', 'hero'. Not Band 8: 'Bad guy' is informal.",
        "grammar_reason": "[GRA7] Key evidence: 'book with dragons', 'fought... to save'. >Band 6: Prepositional phrases and infinitives used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book.\n\nTranscript: I read a fantasy book with dragons. The hero was brave and strong. He fought a bad guy to save the world. I liked the story very much. It was fun to read. I imagined being there. It was exciting.\n\nWord Count: 40 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'fantasy', 'dragons', 'hero', 'brave', 'fought'. \n\n>Band 6: 'Fantasy', 'hero'.\n\nNot Band 8: 'Bad guy' is informal.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'book with dragons', 'fought... to save'. \n\n>Band 6: Prepositional phrases and infinitives used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_549",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party.",
        "transcript_cleaned": "I went to a birthday party. We ate cake and ice cream. We played music and danced. I gave a gift to my friend. Everyone was happy and smiling. It was a good night. I enjoyed it.",
        "word_count": 38,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'birthday party', 'ice cream', 'gift', 'smiling'. Band 7 level.",
             "grammar: 'music and danced', 'gift to my friend'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'birthday party', 'gift', 'music'. >Band 6: 'Gift', 'party'. Not Band 8: 'Cake' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'music and danced', 'gift to my friend'. >Band 6: Coordinating conjunctions and prepositions used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party.\n\nTranscript: I went to a birthday party. We ate cake and ice cream. We played music and danced. I gave a gift to my friend. Everyone was happy and smiling. It was a good night. I enjoyed it.\n\nWord Count: 38 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'birthday party', 'gift', 'music'. \n\n>Band 6: 'Gift', 'party'.\n\nNot Band 8: 'Cake' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'music and danced', 'gift to my friend'. \n\n>Band 6: Coordinating conjunctions and prepositions used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v7_g7_550",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a phone to make calls. It has many apps I like. I text my friends daily. It takes good photos. It is small and fits in my pocket. I carry it everywhere. It is very useful.",
        "word_count": 38,
        "response_type": "long_turn",
        "micro_flaws": [
             "vocab: 'apps', 'text', 'pocket', 'useful'. Band 7 level.",
             "grammar: 'phone to make', 'apps I like'. Band 7 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "good",
            "flexibility": "moderate"
        },
        "vocab_reason": "[LR7] Key evidence: 'apps', 'text', 'pocket', 'useful'. >Band 6: 'Apps', 'text'. Not Band 8: 'Phone' is common.",
        "grammar_reason": "[GRA7] Key evidence: 'phone to make', 'apps I like'. >Band 6: Infinitives and relative clauses (reduced) used correctly. Not Band 8: Very short sentences.",
        "vocabulary": 7,
        "grammar": 7,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a phone to make calls. It has many apps I like. I text my friends daily. It takes good photos. It is small and fits in my pocket. I carry it everywhere. It is very useful.\n\nWord Count: 38 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 7\n\n**Reasoning:** [LR7] Key evidence: 'apps', 'text', 'pocket', 'useful'. \n\n>Band 6: 'Apps', 'text'.\n\nNot Band 8: 'Phone' is common.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 7\n\n**Reasoning:** [GRA7] Key evidence: 'phone to make', 'apps I like'. \n\n>Band 6: Infinitives and relative clauses (reduced) used correctly.\n\nNot Band 8: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
