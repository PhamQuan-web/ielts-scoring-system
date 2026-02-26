import json

OUTPUT_FILE = 'ielts-data/phase3/v76_review_output/jules1/jules1_batch03.jsonl'

samples = [
    {
        "sample_id": "syn_p2_v6_g5_201",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical figure.",
        "transcript_cleaned": "I admire Queen Elizabeth. She was the monarch of the United Kingdom for a long time. She was very dedicated to her duty. She attended many ceremonies. She met presidents and prime ministers. I respect her because she was dignified. However, she pass away recently. It was sad news. People mourn for her. She serve her country well. She is a symbol of stability.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'she pass away' -> 'she passed away'",
            "grammar: 'People mourn for her' -> 'People mourned for her' (past)",
            "grammar: 'She serve her country' -> 'She served her country'",
            "vocab: 'monarch', 'dedicated', 'duty', 'ceremonies', 'presidents', 'prime ministers', 'dignified', 'mourn', 'stability'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'monarch', 'dedicated', 'duty', 'ceremonies', 'dignified', 'mourn', 'stability'. >Band 5: Uses precise topic vocabulary ('monarch', 'stability'). Not Band 7: Lacks idiomatic expressions.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences mostly. 'She pass away', 'She serve'. >Band 4: Some correct complex sentences. Not Band 6: Frequent tense errors in simple structures.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical figure.\n\nTranscript: I admire Queen Elizabeth. She was the monarch of the United Kingdom for a long time. She was very dedicated to her duty. She attended many ceremonies. She met presidents and prime ministers. I respect her because she was dignified. However, she pass away recently. It was sad news. People mourn for her. She serve her country well. She is a symbol of stability.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'monarch', 'dedicated', 'duty', 'ceremonies', 'dignified', 'mourn', 'stability'. \n\n>Band 5: Uses precise topic vocabulary ('monarch', 'stability').\n\nNot Band 7: Lacks idiomatic expressions.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences mostly. 'She pass away', 'She serve'. \n\n>Band 4: Some correct complex sentences.\n\nNot Band 6: Frequent tense errors in simple structures.\n\n**Micro flaws identified:**\n- verb tense: 'pass', 'mourn', 'serve'"
    },
    {
        "sample_id": "syn_p2_v6_g5_202",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a job you would like to do.",
        "transcript_cleaned": "I would like to be an architect. It is a creative profession. Architects design buildings and structures. They need to be artistic and technical. I like drawing plans. I want to create sustainable buildings. It is important for the environment. I need study architecture in university. It is hard course. Architects works with engineers. They collaborate on projects. It is a challenging but rewarding career.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'I need study' -> 'I need to study'",
            "grammar: 'It is hard course' -> 'It is a hard course'",
            "grammar: 'Architects works' -> 'Architects work'",
            "vocab: 'architect', 'profession', 'design', 'structures', 'technical', 'sustainable', 'environment', 'collaborate', 'projects', 'rewarding'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'architect', 'profession', 'structures', 'technical', 'sustainable', 'collaborate', 'rewarding'. >Band 5: Uses less common items like 'sustainable', 'collaborate'. Not Band 7: Collocations are standard.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences dominate. 'Architects works', 'need study'. >Band 4: Meaning is clear despite errors. Not Band 6: Frequent basic errors (S-V agreement, articles).",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a job you would like to do.\n\nTranscript: I would like to be an architect. It is a creative profession. Architects design buildings and structures. They need to be artistic and technical. I like drawing plans. I want to create sustainable buildings. It is important for the environment. I need study architecture in university. It is hard course. Architects works with engineers. They collaborate on projects. It is a challenging but rewarding career.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'architect', 'profession', 'structures', 'technical', 'sustainable', 'collaborate', 'rewarding'. \n\n>Band 5: Uses less common items like 'sustainable', 'collaborate'.\n\nNot Band 7: Collocations are standard.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences dominate. 'Architects works', 'need study'. \n\n>Band 4: Meaning is clear despite errors.\n\nNot Band 6: Frequent basic errors (S-V agreement, articles).\n\n**Micro flaws identified:**\n- verb pattern: 'need study'\n- article error: 'hard course'\n- subject-verb agreement: 'Architects works'"
    },
    {
        "sample_id": "syn_p2_v6_g5_203",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult decision.",
        "transcript_cleaned": "I decided to quit my previous job. It was a stressful environment. My boss was demanding. I was unhappy. I wanted to pursue my passion for photography. It was a risky decision because I need money. My parents advise me to stay. But I follow my heart. I started my own business. It is struggling now, but I am optimistic. I believe I will succeed eventually.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'My parents advise me' -> 'My parents advised me' (past)",
            "grammar: 'But I follow my heart' -> 'But I followed my heart' (past)",
            "grammar: 'It is struggling now' (Correct)",
            "vocab: 'quit', 'previous', 'stressful', 'environment', 'demanding', 'pursue', 'passion', 'risky', 'advise', 'struggling', 'optimistic', 'eventually'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'previous', 'demanding', 'pursue', 'passion', 'risky', 'optimistic', 'eventually'. >Band 5: 'Pursue passion', 'demanding'. Not Band 7: Vocabulary is accurate but not sophisticated.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. Tense inconsistency ('advise', 'follow' in past context). >Band 4: Meaning clear. Not Band 6: Frequent tense shifts.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult decision.\n\nTranscript: I decided to quit my previous job. It was a stressful environment. My boss was demanding. I was unhappy. I wanted to pursue my passion for photography. It was a risky decision because I need money. My parents advise me to stay. But I follow my heart. I started my own business. It is struggling now, but I am optimistic. I believe I will succeed eventually.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'previous', 'demanding', 'pursue', 'passion', 'risky', 'optimistic', 'eventually'. \n\n>Band 5: 'Pursue passion', 'demanding'.\n\nNot Band 7: Vocabulary is accurate but not sophisticated.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. Tense inconsistency ('advise', 'follow' in past context). \n\n>Band 4: Meaning clear.\n\nNot Band 6: Frequent tense shifts.\n\n**Micro flaws identified:**\n- verb tense: 'advise', 'follow'"
    },
    {
        "sample_id": "syn_p2_v6_g5_204",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a book you read.",
        "transcript_cleaned": "I read \"The Great Gatsby\". It is a classic novel by F. Scott Fitzgerald. It is set in the 1920s. The story is about a wealthy man named Gatsby. He is mysterious. He throws lavish parties. He loves a woman named Daisy. It is a tragic love story. The themes are wealth and corruption. I enjoyed the descriptions. However, the language was bit difficult. I use dictionary to understand words. It is a masterpiece of literature.",
        "word_count": 89,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'language was bit difficult' -> 'language was a bit difficult'",
            "grammar: 'I use dictionary' -> 'I used a dictionary'",
            "vocab: 'classic', 'novel', 'set in', 'wealthy', 'mysterious', 'lavish', 'tragic', 'themes', 'corruption', 'descriptions', 'literature', 'masterpiece'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'novel', 'set in', 'wealthy', 'mysterious', 'lavish', 'tragic', 'themes', 'corruption', 'masterpiece'. >Band 5: 'Lavish parties', 'tragic love story'. Not Band 7: Good range but some mechanical usage.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences mostly. 'I use dictionary'. >Band 4: Complex sentences attempted. Not Band 6: Article errors and tense errors.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a book you read.\n\nTranscript: I read \"The Great Gatsby\". It is a classic novel by F. Scott Fitzgerald. It is set in the 1920s. The story is about a wealthy man named Gatsby. He is mysterious. He throws lavish parties. He loves a woman named Daisy. It is a tragic love story. The themes are wealth and corruption. I enjoyed the descriptions. However, the language was bit difficult. I use dictionary to understand words. It is a masterpiece of literature.\n\nWord Count: 89 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'novel', 'set in', 'wealthy', 'mysterious', 'lavish', 'tragic', 'themes', 'corruption', 'masterpiece'. \n\n>Band 5: 'Lavish parties', 'tragic love story'.\n\nNot Band 7: Good range but some mechanical usage.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences mostly. 'I use dictionary'. \n\n>Band 4: Complex sentences attempted.\n\nNot Band 6: Article errors and tense errors.\n\n**Micro flaws identified:**\n- article error: 'bit difficult', 'dictionary'\n- verb tense: 'use'"
    },
    {
        "sample_id": "syn_p2_v6_g5_205",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical place.",
        "transcript_cleaned": "I visited Machu Picchu in Peru. It is an ancient city of the Incas. It is located on a mountain ridge. The scenery is breathtaking. I was amazed by the architecture. The stone walls are impressive. No mortar was used. It is a mystery how they built it. I hired a local guide. He explain the history. It is a UNESCO World Heritage Site. I recommend this destination to everyone. It is a unique experience.",
        "word_count": 87,
        "response_type": "long_turn",
        "micro_flaws": [
            "grammar: 'He explain the history' -> 'He explained the history'",
            "vocab: 'ancient', 'Incas', 'located', 'ridge', 'breathtaking', 'amazed', 'architecture', 'mortar', 'mystery', 'heritage', 'destination', 'unique'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'ancient', 'ridge', 'breathtaking', 'architecture', 'mortar', 'heritage', 'destination'. >Band 5: 'Breathtaking scenery', 'architecture'. Not Band 7: Uses standard collocations.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences mostly. 'He explain'. >Band 4: Passive voice used correctly ('was used'). Not Band 6: Tense error 'explain' reduces accuracy.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical place.\n\nTranscript: I visited Machu Picchu in Peru. It is an ancient city of the Incas. It is located on a mountain ridge. The scenery is breathtaking. I was amazed by the architecture. The stone walls are impressive. No mortar was used. It is a mystery how they built it. I hired a local guide. He explain the history. It is a UNESCO World Heritage Site. I recommend this destination to everyone. It is a unique experience.\n\nWord Count: 87 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'ancient', 'ridge', 'breathtaking', 'architecture', 'mortar', 'heritage', 'destination'. \n\n>Band 5: 'Breathtaking scenery', 'architecture'.\n\nNot Band 7: Uses standard collocations.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences mostly. 'He explain'. \n\n>Band 4: Passive voice used correctly ('was used').\n\nNot Band 6: Tense error 'explain' reduces accuracy.\n\n**Micro flaws identified:**\n- verb tense: 'explain'"
    },
    {
        "sample_id": "syn_p2_v6_g5_206",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult task.",
        "transcript_cleaned": "I organized a charity event at school. It was a fundraising activity. I was responsible for planning. I had to coordinate with many students. It was chaotic at first. We sold baked goods. I designed posters to promote the event. It was exhausting but fulfilling. We raised a lot of money for the orphanage. I learned leadership skills. It was a significant achievement for me. I felt proud of my team.",
        "word_count": 83,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'organized', 'charity', 'fundraising', 'responsible', 'coordinate', 'chaotic', 'promote', 'exhausting', 'fulfilling', 'orphanage', 'leadership', 'significant'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'fundraising', 'coordinate', 'chaotic', 'promote', 'exhausting', 'fulfilling', 'leadership', 'significant'. >Band 5: 'Chaotic', 'fulfilling'. Not Band 7: Good range but standard usage.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences mostly. Correct use of past tense. >Band 4: Accurate simple sentences. Not Band 6: Lacks complex structures. Very choppy.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult task.\n\nTranscript: I organized a charity event at school. It was a fundraising activity. I was responsible for planning. I had to coordinate with many students. It was chaotic at first. We sold baked goods. I designed posters to promote the event. It was exhausting but fulfilling. We raised a lot of money for the orphanage. I learned leadership skills. It was a significant achievement for me. I felt proud of my team.\n\nWord Count: 83 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'fundraising', 'coordinate', 'chaotic', 'promote', 'exhausting', 'fulfilling', 'leadership', 'significant'. \n\n>Band 5: 'Chaotic', 'fulfilling'.\n\nNot Band 7: Good range but standard usage.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences mostly. Correct use of past tense. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks complex structures. Very choppy.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_207",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful skill.",
        "transcript_cleaned": "I learned coding. It is a valuable skill in the modern world. I learned Python language. It is used for data analysis. I took an online course. The instructor was knowledgeable. I found it challenging. I made many errors in the code. I had to debug them. It requires logic and patience. Now I can write simple programs. I want to become a software developer. It is a lucrative career.",
        "word_count": 82,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'coding', 'valuable', 'modern', 'analysis', 'online course', 'instructor', 'knowledgeable', 'challenging', 'errors', 'debug', 'logic', 'software developer', 'lucrative'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'valuable', 'analysis', 'knowledgeable', 'debug', 'logic', 'developer', 'lucrative'. >Band 5: 'Lucrative', 'debug', 'knowledgeable'. Not Band 7: Standard phrasing.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I took', 'I found'. >Band 4: Accurate simple sentences. Not Band 6: Very repetitive sentence structure (Subject-Verb-Object).",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful skill.\n\nTranscript: I learned coding. It is a valuable skill in the modern world. I learned Python language. It is used for data analysis. I took an online course. The instructor was knowledgeable. I found it challenging. I made many errors in the code. I had to debug them. It requires logic and patience. Now I can write simple programs. I want to become a software developer. It is a lucrative career.\n\nWord Count: 82 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'valuable', 'analysis', 'knowledgeable', 'debug', 'logic', 'developer', 'lucrative'. \n\n>Band 5: 'Lucrative', 'debug', 'knowledgeable'.\n\nNot Band 7: Standard phrasing.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I took', 'I found'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very repetitive sentence structure (Subject-Verb-Object).\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_208",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a party you enjoyed.",
        "transcript_cleaned": "I attended a wedding reception last month. It was for my cousin. The venue was a luxury hotel. The decorations were elegant. There were flowers everywhere. The bride looked stunning. We had a buffet dinner. There was a variety of dishes. I tried some exotic food. The music was lively. Everyone danced on the dance floor. It was a joyous occasion. I caught up with my relatives. It was memorable.",
        "word_count": 81,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'reception', 'venue', 'luxury', 'decorations', 'elegant', 'stunning', 'buffet', 'variety', 'exotic', 'lively', 'joyous', 'occasion', 'memorable'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'reception', 'venue', 'elegant', 'stunning', 'exotic', 'joyous', 'occasion'. >Band 5: 'Joyous occasion', 'stunning', 'exotic'. Not Band 7: Good range but lack of idiom.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'There were'. >Band 4: Accurate simple sentences. Not Band 6: Lacks complex sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a party you enjoyed.\n\nTranscript: I attended a wedding reception last month. It was for my cousin. The venue was a luxury hotel. The decorations were elegant. There were flowers everywhere. The bride looked stunning. We had a buffet dinner. There was a variety of dishes. I tried some exotic food. The music was lively. Everyone danced on the dance floor. It was a joyous occasion. I caught up with my relatives. It was memorable.\n\nWord Count: 81 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'reception', 'venue', 'elegant', 'stunning', 'exotic', 'joyous', 'occasion'. \n\n>Band 5: 'Joyous occasion', 'stunning', 'exotic'.\n\nNot Band 7: Good range but lack of idiom.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'There were'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks complex sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_209",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a beautiful place.",
        "transcript_cleaned": "I visited the Grand Canyon in USA. It is a natural wonder. The landscape is spectacular. The rocks have different colors. Red, orange, and brown. It is vast and deep. I felt insignificant standing there. We hiked on a trail. It was rugged. The weather was scorching hot. I took panoramic photos. It is a breathtaking view. Nature is powerful. I recommend this site to tourists.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'natural wonder', 'landscape', 'spectacular', 'vast', 'insignificant', 'hiked', 'trail', 'rugged', 'scorching', 'panoramic', 'breathtaking'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'wonder', 'spectacular', 'vast', 'insignificant', 'rugged', 'scorching', 'panoramic'. >Band 5: 'Scorching', 'insignificant', 'spectacular'. Not Band 7: Standard descriptors.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'The rocks have'. >Band 4: Accurate simple sentences. Not Band 6: Lacks variety in sentence structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a beautiful place.\n\nTranscript: I visited the Grand Canyon in USA. It is a natural wonder. The landscape is spectacular. The rocks have different colors. Red, orange, and brown. It is vast and deep. I felt insignificant standing there. We hiked on a trail. It was rugged. The weather was scorching hot. I took panoramic photos. It is a breathtaking view. Nature is powerful. I recommend this site to tourists.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'wonder', 'spectacular', 'vast', 'insignificant', 'rugged', 'scorching', 'panoramic'. \n\n>Band 5: 'Scorching', 'insignificant', 'spectacular'.\n\nNot Band 7: Standard descriptors.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'The rocks have'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks variety in sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_210",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a movie.",
        "transcript_cleaned": "I saw a documentary about oceans. It was informative. It showed marine life. I saw whales and sharks. The cinematography was amazing. The colors were vibrant. It explained the ecosystem. It also talked about pollution. Plastic waste is a big problem. It threatens the creatures. I felt sad about it. We must protect the environment. This documentary raised my awareness. It was educational and moving.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'documentary', 'informative', 'marine life', 'cinematography', 'vibrant', 'ecosystem', 'pollution', 'waste', 'threatens', 'creatures', 'awareness', 'moving'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'documentary', 'marine', 'cinematography', 'vibrant', 'ecosystem', 'threatens', 'awareness', 'moving'. >Band 5: 'Cinematography', 'ecosystem', 'vibrant'. Not Band 7: Good range but standard collocations.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'It showed'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structures.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a movie.\n\nTranscript: I saw a documentary about oceans. It was informative. It showed marine life. I saw whales and sharks. The cinematography was amazing. The colors were vibrant. It explained the ecosystem. It also talked about pollution. Plastic waste is a big problem. It threatens the creatures. I felt sad about it. We must protect the environment. This documentary raised my awareness. It was educational and moving.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'documentary', 'marine', 'cinematography', 'vibrant', 'ecosystem', 'threatens', 'awareness', 'moving'. \n\n>Band 5: 'Cinematography', 'ecosystem', 'vibrant'.\n\nNot Band 7: Good range but standard collocations.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'It showed'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_211",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a piece of news.",
        "transcript_cleaned": "I read news about a scientific breakthrough. Scientists discovered a new cure for a disease. It was cancer. They developed a new drug. It was tested on patients. The results were promising. Many people recovered. This is a medical miracle. It gives hope to patients. I read it on a news portal. I shared it on social media. It went viral. Science is advancing rapidly.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'scientific', 'breakthrough', 'cure', 'disease', 'developed', 'patients', 'promising', 'recovered', 'medical miracle', 'portal', 'viral', 'advancing'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'breakthrough', 'cure', 'promising', 'recovered', 'miracle', 'viral', 'advancing'. >Band 5: 'Breakthrough', 'promising', 'viral'. Not Band 7: Standard reporting language.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'They developed'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a piece of news.\n\nTranscript: I read news about a scientific breakthrough. Scientists discovered a new cure for a disease. It was cancer. They developed a new drug. It was tested on patients. The results were promising. Many people recovered. This is a medical miracle. It gives hope to patients. I read it on a news portal. I shared it on social media. It went viral. Science is advancing rapidly.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'breakthrough', 'cure', 'promising', 'recovered', 'miracle', 'viral', 'advancing'. \n\n>Band 5: 'Breakthrough', 'promising', 'viral'.\n\nNot Band 7: Standard reporting language.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'They developed'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_212",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a gift.",
        "transcript_cleaned": "I received a digital camera. It was a graduation present. It is a Canon camera. It has a high resolution. The lens is powerful. I can zoom in far. I like photography. I take portraits and landscapes. The quality is superb. It was a generous gift. I was grateful. I use it to capture moments. I will cherish it. It is my most prized possession.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'digital', 'graduation', 'resolution', 'lens', 'zoom', 'photography', 'portraits', 'landscapes', 'quality', 'superb', 'generous', 'grateful', 'capture', 'cherish', 'prized possession'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'resolution', 'lens', 'portraits', 'landscapes', 'superb', 'generous', 'capture', 'cherish', 'prized possession'. >Band 5: 'Prized possession', 'superb'. Not Band 7: Standard phrasing.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'I can'. >Band 4: Accurate simple sentences. Not Band 6: Lacks complex structures.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a gift.\n\nTranscript: I received a digital camera. It was a graduation present. It is a Canon camera. It has a high resolution. The lens is powerful. I can zoom in far. I like photography. I take portraits and landscapes. The quality is superb. It was a generous gift. I was grateful. I use it to capture moments. I will cherish it. It is my most prized possession.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'resolution', 'lens', 'portraits', 'landscapes', 'superb', 'generous', 'capture', 'cherish', 'prized possession'. \n\n>Band 5: 'Prized possession', 'superb'.\n\nNot Band 7: Standard phrasing.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'I can'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks complex structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_213",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a game.",
        "transcript_cleaned": "I play a video game called Minecraft. It is a sandbox game. You can build anything. I build houses and castles. You have to gather resources. Wood and stone. There are monsters at night. You must survive. It is very addictive. I play online with friends. We collaborate on projects. It stimulates creativity. The graphics are simple, but the gameplay is deep. I enjoy it.",
        "word_count": 75,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'sandbox', 'resources', 'monsters', 'survive', 'addictive', 'online', 'collaborate', 'stimulates', 'creativity', 'graphics', 'gameplay'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'sandbox', 'resources', 'collaborate', 'stimulates', 'creativity', 'gameplay'. >Band 5: 'Stimulates creativity', 'gameplay'. Not Band 7: Standard game review words.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'You can build', 'You have to'. >Band 4: Accurate simple sentences. Not Band 6: Short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a game.\n\nTranscript: I play a video game called Minecraft. It is a sandbox game. You can build anything. I build houses and castles. You have to gather resources. Wood and stone. There are monsters at night. You must survive. It is very addictive. I play online with friends. We collaborate on projects. It stimulates creativity. The graphics are simple, but the gameplay is deep. I enjoy it.\n\nWord Count: 75 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'sandbox', 'resources', 'collaborate', 'stimulates', 'creativity', 'gameplay'. \n\n>Band 5: 'Stimulates creativity', 'gameplay'.\n\nNot Band 7: Standard game review words.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'You can build', 'You have to'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_214",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a historical building.",
        "transcript_cleaned": "I visited the Eiffel Tower in Paris. It is an iconic landmark. It was constructed in 1889. It is made of iron. It is massive. I took an elevator to the top. The view was panoramic. I could see the whole city. It is a popular tourist attraction. Millions of visitors come every year. It is a symbol of France. It was a breathtaking experience.",
        "word_count": 77,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'iconic', 'landmark', 'constructed', 'iron', 'massive', 'elevator', 'panoramic', 'tourist attraction', 'symbol', 'breathtaking'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'iconic', 'landmark', 'constructed', 'panoramic', 'tourist attraction', 'breathtaking'. >Band 5: 'Iconic landmark', 'panoramic'. Not Band 7: Standard travel vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'It was'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a historical building.\n\nTranscript: I visited the Eiffel Tower in Paris. It is an iconic landmark. It was constructed in 1889. It is made of iron. It is massive. I took an elevator to the top. The view was panoramic. I could see the whole city. It is a popular tourist attraction. Millions of visitors come every year. It is a symbol of France. It was a breathtaking experience.\n\nWord Count: 77 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'iconic', 'landmark', 'constructed', 'panoramic', 'tourist attraction', 'breathtaking'. \n\n>Band 5: 'Iconic landmark', 'panoramic'.\n\nNot Band 7: Standard travel vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'It was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_215",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a skill.",
        "transcript_cleaned": "I learned to play the guitar. It is a versatile instrument. I learned chords and strumming. I practiced daily. It requires dexterity. My fingers hurt initially. I learned songs from YouTube. It was satisfying to play a melody. Music is expressive. I can express my emotions. I played for my friends. They were impressed. Learning an instrument improves discipline. It is a rewarding hobby.",
        "word_count": 72,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'versatile', 'instrument', 'chords', 'strumming', 'dexterity', 'initially', 'satisfying', 'melody', 'expressive', 'emotions', 'impressed', 'discipline', 'rewarding'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'versatile', 'strumming', 'dexterity', 'expressive', 'discipline', 'rewarding'. >Band 5: 'Dexterity', 'versatile'. Not Band 7: Standard music vocab.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'I learned'. >Band 4: Accurate simple sentences. Not Band 6: Very short sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a skill.\n\nTranscript: I learned to play the guitar. It is a versatile instrument. I learned chords and strumming. I practiced daily. It requires dexterity. My fingers hurt initially. I learned songs from YouTube. It was satisfying to play a melody. Music is expressive. I can express my emotions. I played for my friends. They were impressed. Learning an instrument improves discipline. It is a rewarding hobby.\n\nWord Count: 72 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'versatile', 'strumming', 'dexterity', 'expressive', 'discipline', 'rewarding'. \n\n>Band 5: 'Dexterity', 'versatile'.\n\nNot Band 7: Standard music vocab.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'I learned'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_216",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult journey.",
        "transcript_cleaned": "I traveled to a remote island. The journey was arduous. First, I took a flight. Then, I took a ferry. The sea was rough. I felt seasick. The ferry was old and rusty. It took four hours. When we arrived, there was no transport. We hiked to the hotel. It was exhausting. However, the destination was pristine. The beaches were unspoiled. The struggle was worth it.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'remote', 'arduous', 'ferry', 'rough', 'seasick', 'rusty', 'transport', 'hiked', 'exhausting', 'destination', 'pristine', 'unspoiled', 'struggle'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'remote', 'arduous', 'seasick', 'exhausting', 'pristine', 'unspoiled'. >Band 5: 'Arduous', 'pristine', 'unspoiled'. Not Band 7: Good adjectives but standard.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I took', 'The sea was'. >Band 4: Accurate simple sentences. Not Band 6: Lacks complex structures.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult journey.\n\nTranscript: I traveled to a remote island. The journey was arduous. First, I took a flight. Then, I took a ferry. The sea was rough. I felt seasick. The ferry was old and rusty. It took four hours. When we arrived, there was no transport. We hiked to the hotel. It was exhausting. However, the destination was pristine. The beaches were unspoiled. The struggle was worth it.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'remote', 'arduous', 'seasick', 'exhausting', 'pristine', 'unspoiled'. \n\n>Band 5: 'Arduous', 'pristine', 'unspoiled'.\n\nNot Band 7: Good adjectives but standard.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I took', 'The sea was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks complex structures.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_217",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a person you admire.",
        "transcript_cleaned": "I admire my teacher, Mrs. Smith. She is an inspiring educator. She teaches history. She is passionate about her subject. She makes lessons engaging. She uses multimedia. She is knowledgeable. She answers all questions. She cares about students' welfare. She encourages us to think critically. She is a role model. I respect her dedication. She influenced my career choice. I want to be a teacher too.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'inspiring', 'educator', 'passionate', 'engaging', 'multimedia', 'knowledgeable', 'welfare', 'encourages', 'critically', 'role model', 'dedication', 'influenced'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'educator', 'passionate', 'engaging', 'knowledgeable', 'welfare', 'critically', 'dedication'. >Band 5: 'Engaging', 'critically', 'welfare'. Not Band 7: Standard vocabulary for topic.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'She is', 'She teaches'. >Band 4: Accurate simple sentences. Not Band 6: Very repetitive sentence openings.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a person you admire.\n\nTranscript: I admire my teacher, Mrs. Smith. She is an inspiring educator. She teaches history. She is passionate about her subject. She makes lessons engaging. She uses multimedia. She is knowledgeable. She answers all questions. She cares about students' welfare. She encourages us to think critically. She is a role model. I respect her dedication. She influenced my career choice. I want to be a teacher too.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'educator', 'passionate', 'engaging', 'knowledgeable', 'welfare', 'critically', 'dedication'. \n\n>Band 5: 'Engaging', 'critically', 'welfare'.\n\nNot Band 7: Standard vocabulary for topic.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'She is', 'She teaches'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very repetitive sentence openings.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_218",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a place.",
        "transcript_cleaned": "I visited a museum in London. It is a massive building. It has a vast collection of artifacts. I saw ancient sculptures. They were well-preserved. The exhibitions were informative. I learned about different civilizations. There were interactive displays. It was fascinating. I spent the whole day there. The architecture of the museum was grand. It is a cultural hub. I highly recommend it.",
        "word_count": 73,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'massive', 'vast', 'collection', 'artifacts', 'ancient', 'sculptures', 'well-preserved', 'exhibitions', 'informative', 'civilizations', 'interactive', 'fascinating', 'architecture', 'cultural hub'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'artifacts', 'well-preserved', 'civilizations', 'interactive', 'cultural hub'. >Band 5: 'Cultural hub', 'artifacts'. Not Band 7: Standard museum words.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'I saw'. >Band 4: Accurate simple sentences. Not Band 6: Lacks variety.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a place.\n\nTranscript: I visited a museum in London. It is a massive building. It has a vast collection of artifacts. I saw ancient sculptures. They were well-preserved. The exhibitions were informative. I learned about different civilizations. There were interactive displays. It was fascinating. I spent the whole day there. The architecture of the museum was grand. It is a cultural hub. I highly recommend it.\n\nWord Count: 73 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'artifacts', 'well-preserved', 'civilizations', 'interactive', 'cultural hub'. \n\n>Band 5: 'Cultural hub', 'artifacts'.\n\nNot Band 7: Standard museum words.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'I saw'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Lacks variety.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_219",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a traditional event.",
        "transcript_cleaned": "I attended a traditional wedding. It was a formal ceremony. The bride wore a magnificent gown. The groom wore a tuxedo. The venue was decorated with floral arrangements. It was elegant. Guests brought generous gifts. We enjoyed a lavish feast. There was traditional music and folk dancing. It was a celebration of love. The rituals were meaningful. It was a memorable occasion.",
        "word_count": 71,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'formal', 'ceremony', 'magnificent', 'gown', 'tuxedo', 'venue', 'floral arrangements', 'elegant', 'generous', 'lavish', 'feast', 'folk dancing', 'celebration', 'rituals', 'memorable'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'magnificent', 'floral arrangements', 'lavish', 'feast', 'rituals', 'memorable'. >Band 5: 'Lavish', 'rituals'. Not Band 7: Good adjectives but standard structure.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It was', 'The bride wore'. >Band 4: Accurate simple sentences. Not Band 6: Very repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a traditional event.\n\nTranscript: I attended a traditional wedding. It was a formal ceremony. The bride wore a magnificent gown. The groom wore a tuxedo. The venue was decorated with floral arrangements. It was elegant. Guests brought generous gifts. We enjoyed a lavish feast. There was traditional music and folk dancing. It was a celebration of love. The rituals were meaningful. It was a memorable occasion.\n\nWord Count: 71 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'magnificent', 'floral arrangements', 'lavish', 'feast', 'rituals', 'memorable'. \n\n>Band 5: 'Lavish', 'rituals'.\n\nNot Band 7: Good adjectives but standard structure.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It was', 'The bride wore'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_220",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a difficult choice.",
        "transcript_cleaned": "I had to choose a university course. It was a crucial decision. I was torn between art and science. I am creative, but science offers stability. I consulted my parents. They were supportive. I researched the curriculum. I considered my career prospects. It was agonizing. Finally, I chose graphic design. It combines creativity and technology. I am satisfied with my choice. It was the right path.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'crucial', 'torn', 'stability', 'consulted', 'supportive', 'researched', 'curriculum', 'considered', 'prospects', 'agonizing', 'combines', 'satisfied'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'crucial', 'torn between', 'stability', 'consulted', 'curriculum', 'prospects', 'agonizing'. >Band 5: 'Agonizing', 'prospects', 'torn between'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I had to', 'It was'. >Band 4: Accurate simple sentences. Not Band 6: Short choppy sentences.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a difficult choice.\n\nTranscript: I had to choose a university course. It was a crucial decision. I was torn between art and science. I am creative, but science offers stability. I consulted my parents. They were supportive. I researched the curriculum. I considered my career prospects. It was agonizing. Finally, I chose graphic design. It combines creativity and technology. I am satisfied with my choice. It was the right path.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'crucial', 'torn between', 'stability', 'consulted', 'curriculum', 'prospects', 'agonizing'. \n\n>Band 5: 'Agonizing', 'prospects', 'torn between'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I had to', 'It was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Short choppy sentences.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_221",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a plant.",
        "transcript_cleaned": "I like the cactus plant. It is a unique plant. It grows in deserts. It can survive in arid conditions. It has thick skin and spines. It stores water. I have a cactus in my room. It is low maintenance. I water it rarely. It blooms once a year. The flower is vibrant. Cactuses are resilient. They symbolize endurance. I think they are fascinating plants.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'cactus', 'unique', 'deserts', 'survive', 'arid', 'conditions', 'spines', 'stores', 'low maintenance', 'rarely', 'blooms', 'vibrant', 'resilient', 'endurance', 'fascinating'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'arid', 'spines', 'low maintenance', 'vibrant', 'resilient', 'endurance'. >Band 5: 'Resilient', 'arid', 'low maintenance'. Not Band 7: Good topic vocabulary.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'It has'. >Band 4: Accurate simple sentences. Not Band 6: Very repetitive sentence structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a plant.\n\nTranscript: I like the cactus plant. It is a unique plant. It grows in deserts. It can survive in arid conditions. It has thick skin and spines. It stores water. I have a cactus in my room. It is low maintenance. I water it rarely. It blooms once a year. The flower is vibrant. Cactuses are resilient. They symbolize endurance. I think they are fascinating plants.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'arid', 'spines', 'low maintenance', 'vibrant', 'resilient', 'endurance'. \n\n>Band 5: 'Resilient', 'arid', 'low maintenance'.\n\nNot Band 7: Good topic vocabulary.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'It has'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very repetitive sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_222",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a useful object.",
        "transcript_cleaned": "I use a coffee maker daily. It is an essential appliance. I cannot start my day without coffee. It is automatic. I put water and beans in. It grinds the beans. The aroma is invigorating. It brews coffee quickly. It saves me time. I do not need to go to a cafe. It is convenient and efficient. I maintain it regularly. It is a durable machine.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'appliance', 'essential', 'automatic', 'grinds', 'aroma', 'invigorating', 'brews', 'convenient', 'efficient', 'maintain', 'regularly', 'durable'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'appliance', 'essential', 'grinds', 'aroma', 'invigorating', 'brews', 'efficient', 'durable'. >Band 5: 'Invigorating', 'brews', 'durable'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'It is', 'I put'. >Band 4: Accurate simple sentences. Not Band 6: Monotonous sentence structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a useful object.\n\nTranscript: I use a coffee maker daily. It is an essential appliance. I cannot start my day without coffee. It is automatic. I put water and beans in. It grinds the beans. The aroma is invigorating. It brews coffee quickly. It saves me time. I do not need to go to a cafe. It is convenient and efficient. I maintain it regularly. It is a durable machine.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'appliance', 'essential', 'grinds', 'aroma', 'invigorating', 'brews', 'efficient', 'durable'. \n\n>Band 5: 'Invigorating', 'brews', 'durable'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'It is', 'I put'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Monotonous sentence structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_223",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a busy time.",
        "transcript_cleaned": "I had a hectic week last month. It was exam period. I had five exams in five days. I was overwhelmed. I studied day and night. I felt stressed and anxious. I drank a lot of coffee. I reviewed my notes constantly. I had no leisure time. I was exhausted. However, I persevered. I finished the exams. I felt a sense of accomplishment. It was intense.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'hectic', 'period', 'overwhelmed', 'stressed', 'anxious', 'reviewed', 'constantly', 'leisure', 'exhausted', 'persevered', 'accomplishment', 'intense'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'hectic', 'overwhelmed', 'anxious', 'leisure', 'persevered', 'accomplishment', 'intense'. >Band 5: 'Hectic', 'persevered', 'overwhelmed'. Not Band 7: Strong words used simply.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I had', 'I was'. >Band 4: Accurate simple sentences. Not Band 6: No complex structures used.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a busy time.\n\nTranscript: I had a hectic week last month. It was exam period. I had five exams in five days. I was overwhelmed. I studied day and night. I felt stressed and anxious. I drank a lot of coffee. I reviewed my notes constantly. I had no leisure time. I was exhausted. However, I persevered. I finished the exams. I felt a sense of accomplishment. It was intense.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'hectic', 'overwhelmed', 'anxious', 'leisure', 'persevered', 'accomplishment', 'intense'. \n\n>Band 5: 'Hectic', 'persevered', 'overwhelmed'.\n\nNot Band 7: Strong words used simply.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I had', 'I was'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: No complex structures used.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_224",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a competition.",
        "transcript_cleaned": "I entered a photography contest. It was a local competition. The theme was \"nature\". I submitted three photos. I captured a sunset and a forest. The competition was fierce. There were many talented photographers. I waited for the results eagerly. I did not win the first prize. But I received a special mention. I was satisfied. It motivated me to improve my skills. It was a rewarding experience.",
        "word_count": 78,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'contest', 'theme', 'submitted', 'captured', 'fierce', 'talented', 'eagerly', 'special mention', 'satisfied', 'motivated', 'rewarding'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'contest', 'theme', 'submitted', 'captured', 'fierce', 'eagerly', 'motivated', 'rewarding'. >Band 5: 'Fierce competition', 'eagerly', 'motivated'. Not Band 7: Good range.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'I entered', 'I submitted'. >Band 4: Accurate simple sentences. Not Band 6: Repetitive structure.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a competition.\n\nTranscript: I entered a photography contest. It was a local competition. The theme was \"nature\". I submitted three photos. I captured a sunset and a forest. The competition was fierce. There were many talented photographers. I waited for the results eagerly. I did not win the first prize. But I received a special mention. I was satisfied. It motivated me to improve my skills. It was a rewarding experience.\n\nWord Count: 78 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'contest', 'theme', 'submitted', 'captured', 'fierce', 'eagerly', 'motivated', 'rewarding'. \n\n>Band 5: 'Fierce competition', 'eagerly', 'motivated'.\n\nNot Band 7: Good range.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'I entered', 'I submitted'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Repetitive structure.\n\n**Micro flaws identified:**\n- none significant"
    },
    {
        "sample_id": "syn_p2_v6_g5_225",
        "video_id": "synthetic",
        "part": 2,
        "question": "Describe a friend.",
        "transcript_cleaned": "My best friend is Sarah. She is reliable and supportive. We have known each other for a decade. She is a good listener. I confide in her. She gives sound advice. We share similar interests. We like hiking and reading. She is also humorous. She makes me laugh. We have a strong bond. I value her friendship. She is always there for me. She is indispensable.",
        "word_count": 76,
        "response_type": "long_turn",
        "micro_flaws": [
            "vocab: 'reliable', 'supportive', 'decade', 'listener', 'confide', 'sound advice', 'interests', 'humorous', 'bond', 'value', 'indispensable'. Band 6 level."
        ],
        "grammar_profile": {
            "complexity": "moderate",
            "accuracy": "controlled",
            "flexibility": "low"
        },
        "vocab_reason": "[LR6] Key evidence: 'reliable', 'supportive', 'confide', 'sound advice', 'humorous', 'bond', 'indispensable'. >Band 5: 'Indispensable', 'confide', 'sound advice'. Not Band 7: Strong vocabulary.",
        "grammar_reason": "[GRA5] Key evidence: Simple sentences. 'She is', 'We have'. >Band 4: Accurate simple sentences. Not Band 6: Very short and choppy.",
        "vocabulary": 6,
        "grammar": 5,
        "is_valid": True,
        "dataset_source": "synthetic",
        "idiom_present": False,
        "risk_level": "low",
        "instruction": "Score this IELTS Speaking response for Vocabulary (Lexical Resource) and Grammar (Grammatical Range and Accuracy) based on IELTS band descriptors (4-9). Provide band scores with detailed reasoning.",
        "input": "Part: 2\nQuestion: Describe a friend.\n\nTranscript: My best friend is Sarah. She is reliable and supportive. We have known each other for a decade. She is a good listener. I confide in her. She gives sound advice. We share similar interests. We like hiking and reading. She is also humorous. She makes me laugh. We have a strong bond. I value her friendship. She is always there for me. She is indispensable.\n\nWord Count: 76 words\nResponse Type: long_turn",
        "output": "## Vocabulary (Lexical Resource): Band 6\n\n**Reasoning:** [LR6] Key evidence: 'reliable', 'supportive', 'confide', 'sound advice', 'humorous', 'bond', 'indispensable'. \n\n>Band 5: 'Indispensable', 'confide', 'sound advice'.\n\nNot Band 7: Strong vocabulary.\n\n**Idiom present:** No\n**Risk level:** Low\n\n---\n\n## Grammar (Grammatical Range & Accuracy): Band 5\n\n**Reasoning:** [GRA5] Key evidence: Simple sentences. 'She is', 'We have'. \n\n>Band 4: Accurate simple sentences.\n\nNot Band 6: Very short and choppy.\n\n**Micro flaws identified:**\n- none significant"
    }
]

with open(OUTPUT_FILE, 'a') as f:
    for sample in samples:
        json.dump(sample, f)
        f.write('\n')
